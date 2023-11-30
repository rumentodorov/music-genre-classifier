from sklearn.metrics import classification_report

import mlflow


def mlflow_log_classification_report(attributes, classes,  model, target_names, file = "classification_report.json"):
    predicted = model.predict(attributes)
    result = classification_report(predicted, classes, target_names=target_names)
    print(result)
    result_dict = classification_report(predicted, classes, target_names=target_names, output_dict=True)
    mlflow.log_dict(result_dict, file)

def mlflow_log_model(grid_search, train_score, validation_score):
    mlflow.log_metric("Train score", train_score)
    mlflow.log_metric("Validation score", validation_score)
    mlflow.sklearn.log_model(grid_search.best_estimator_, "Model")
    mlflow_log_best_params(grid_search)

def mlflow_log_best_params(grid_search):
    for key in grid_search.best_params_.keys():
        mlflow.log_param(key, grid_search.best_params_[key])