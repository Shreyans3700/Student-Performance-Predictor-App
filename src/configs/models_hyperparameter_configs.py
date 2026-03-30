from dataclasses import dataclass, field


@dataclass
class ModelsHyperParameterConfigs:
    params: dict = field(
        default_factory=lambda: {
            "LinearRegression": {
                "fit_intercept": [True, False],
                "copy_X": [True, False],
                "positive": [True, False],
            },
            "Ridge": {
                "alpha": [0.001, 0.01, 0.1, 1.0, 10.0, 100.0],
                "fit_intercept": [True, False],
                "solver": [
                    "auto",
                    "svd",
                    "cholesky",
                    "lsqr",
                    "sparse_cg",
                    "sag",
                    "saga",
                ],
            },
            "Lasso": {
                "alpha": [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0],
                "fit_intercept": [True, False],
                "selection": ["cyclic", "random"],
                "max_iter": [1000, 5000, 10000],
            },
            "Support Vector Regressor": {
                "kernel": ["linear", "poly", "rbf", "sigmoid"],
                "C": [0.1, 1, 10, 100, 1000],
                "epsilon": [0.001, 0.01, 0.1, 0.2, 0.5],
                "gamma": ["scale", "auto"],
                "degree": [2, 3, 4],  # used when kernel='poly'
                "shrinking": [True, False],
            },
            "KN Regressor": {
                "n_neighbors": [3, 5, 7, 9, 11, 15, 21],
                "weights": ["uniform", "distance"],
                "algorithm": ["auto", "ball_tree", "kd_tree", "brute"],
                "leaf_size": [20, 30, 40, 50],
                "p": [1, 2],  # 1=Manhattan, 2=Euclidean
            },
            "DecisionTree Regressor": {
                "criterion": [
                    "squared_error",
                    "friedman_mse",
                    "absolute_error",
                    "poisson",
                ],
                "splitter": ["best", "random"],
                "max_depth": [None, 5, 10, 20, 30, 50],
                "min_samples_split": [2, 5, 10, 20],
                "min_samples_leaf": [1, 2, 4, 10],
                "max_features": ["sqrt", "log2", None],
            },
            "RandomForest Regressor": {
                "n_estimators": [50, 100, 200, 300, 500],
                "criterion": ["squared_error", "absolute_error", "friedman_mse"],
                "max_depth": [None, 10, 20, 30, 50],
                "min_samples_split": [2, 5, 10, 20],
                "min_samples_leaf": [1, 2, 4, 10],
                "max_features": ["sqrt", "log2", None],
                "bootstrap": [True, False],
            },
            "XG Boost": {
                "n_estimators": [50, 100, 200, 300, 500],
                "learning_rate": [0.001, 0.01, 0.05, 0.1, 0.2],
                "max_depth": [3, 5, 7, 10, 15],
                "min_child_weight": [1, 3, 5, 7],
                "subsample": [0.6, 0.7, 0.8, 0.9, 1.0],
                "colsample_bytree": [0.6, 0.7, 0.8, 0.9, 1.0],
                "gamma": [0, 0.1, 0.2, 0.3, 0.5],
                "reg_alpha": [0, 0.01, 0.1, 1],
                "reg_lambda": [0.1, 1, 10, 100],
            },
        }
    )
