import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import os

nltk.download('stopwords')
nltk.download('wordnet')

model_filename = r'trained_model.pkl'
vectorizer_filename = r'fidf_vectorizer.pkl'

def preprocess_string(string1):
    string2 = string1.lower()
    string1 = string1.translate(str.maketrans('', '', string.punctuation))
    return string1

lemmatizer = WordNetLemmatizer()
def lemmatize_string(string1):
    return ' '.join([lemmatizer.lemmatize(word) for word in string1.split()])

def train_and_save_model():
    print("Veri yükleniyor...")


    file_path = 'ml_dataset.csv'
    df = pd.read_csv(file_path)

    print("Veri yükleme tamamlandı.")
    print("İlk birkaç satır:")
    print(df.head())


    print(df.columns)


    df = df[['Country', 'Ingredients']].dropna()

    print("Veri temizleme tamamlandı.")

    # Veriyi ön işliyoruz
    df['Ingredients'] = df['Ingredients'].apply(preprocess_string)
    df['Ingredients'] = df['Ingredients'].apply(lemmatize_string)

    print("Veri ön işleme tamamlandı.")

    # TF-IDF vektörizer ve Logistic Regression modeli pipeline oluşturan yer
    vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'), ngram_range=(1, 2))
    X = vectorizer.fit_transform(df['Ingredients'])
    y = df['Country']

    print("Veri seti eğitim ve test setlerine ayrılıyor...")
    # Veri setini eğitim ve test setlerine ayırdık
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Model eğitiliyor...")
    # Modeli eğitiyoruz
    model = LogisticRegression(max_iter=1000, C=1.0)
    model.fit(X_train, y_train)

    print("Model eğitildi. Test seti ile doğruluk ölçülüyor...")
    # Test seti ile modelin doğruluğunu ölçüyoruz
    y_pred = model.predict(X_test)
    print(f'Test set accuracy: {accuracy_score(y_test, y_pred)}')

    print("Model ve vektörizer kaydediliyor...")
    # Modeli ve vektörizeri kaydetme
    joblib.dump(model, model_filename)
    joblib.dump(vectorizer, vectorizer_filename)
    print("Model ve vektörizer başarıyla kaydedildi.")

def load_model():
    if os.path.exists(model_filename) and os.path.exists(vectorizer_filename):
        print("Model ve vektörizer yükleniyor...")
        model = joblib.load(model_filename)
        vectorizer = joblib.load(vectorizer_filename)
        print("Model ve vektörizer başarıyla yüklendi.")
        return model, vectorizer
    else:
        print("Kaydedilmiş model bulunamadı. Model eğitiliyor...")
        train_and_save_model()
        return load_model()

def predict_country(query):
    model, vectorizer = load_model()
    query = preprocess_string(query)
    query = lemmatize_string(query)
    query_vector = vectorizer.transform([query])
    prediction = model.predict(query_vector)
    return prediction[0]


query = input("Enter at least 5 ingredient in comma-seperated form")
liste = query.split((","))
if len(liste)>=5:
    predicted_country = predict_country(query)
    print(f'The predicted country for the given ingredients is: {predicted_country}')
else:
    print("Invalid input")
