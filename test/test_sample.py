import numpy as np
from xgboost import XGBRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def test_xgb_model_runs():
    # regression_sample
    X, y = make_regression(n_samples=100, n_features=2, noise=0.1, random_state=42)
    
    # train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # XGBoost model train
    model = XGBRegressor(n_estimators=10, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    # test 
    assert not np.isnan(preds).any(), "Prediction contains NaNs"
    assert (preds > -1e10).all(), "Prediction contains absurd values"
    assert r2_score(y_test, preds) > 0, "R² score is too low"
