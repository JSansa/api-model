import joblib
import pandas as pd
from sklearn.base import ClassifierMixin
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


def ingest_data(filepath: str) -> pd.DataFrame:
    return pd.read_excel(filepath)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # suppression des lignes avec des valeurs manquantes
    df = df.dropna(axis=8)
    # remplacer les valeurs non numériques par des valeurs numériques
    df['sex'].replace(to_replace=['male', 'female'], value=[0, 1], inplace=True)
    return df

def train_model(df: pd.DataFrame) -> ClassifierMixin:
    # instantiate model
    model = KNeighborsClassifier()

    # split data
    y = df['survived']
    X = df.drop('survived', axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.28)

    # train model
    model.fit(X_train, y_train)

    # evaluate model
    model.score(X_test, y_test)

    return model

if __name__ == "__main__":
    df = ingest_data("titanic.xls")
    df = clean_data(df)
    model = train_model(df)
    joblib.dump(model, "model_titanic.joblib")