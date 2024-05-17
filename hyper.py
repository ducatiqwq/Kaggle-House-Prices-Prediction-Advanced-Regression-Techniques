import time
import numpy as np

TARGET = "SalePrice"
REPLACE_MODES = {"GarageYrBlt": ("const", 0),
				"GarageArea": ("const", 0),
				"GarageCars": ("const", 0),
				"GarageType": ("const", "None"),
				"GarageFinish": ("const", "None"),
				"GarageQual": ("const", "None"),
				"GarageCond": ("const", "None"),
				"BsmtQual": ("const", "None"),
				"BsmtCond": ("const", "None"),
				"BsmtExposure": ("const", "None"),
				"BsmtFinType1": ("const", "None"),
				"BsmtFinType2": ("const", "None"),
				"Functional": ("const", "Typ"),
				"Electrical": ("const", "SBrkr"),
				"KitchenQual": ("const", "TA"),
				"Exterior1st": ("random", None),
				"Exterior2nd": ("random", None),
				"SaleType": ("random", None),
				"Utilities": ("const", "None"),
				"MasVnrType": ("const", "None"),
				"MasVnrArea": ("const", 0),
				"BsmtFinSF1": ("const", 0),
				"BsmtFinSF2": ("const", 0),
				"BsmtUnfSF": ("const", 0),
				"TotalBsmtSF": ("const", 0),
				"BsmtFullBath": ("const", 0),
				"BsmtHalfBath": ("const", 0),
				"FireplaceQu": ("const", "None"),
				"SalePrice": ("const", 0),
				"LotFrontage": ("group", "Neighborhood", "median"),
				"MSZoning": ("group", "MSSubClass", "random")}

# All these indices must be in the range [1, 1460]
DROP_LISTS = [[457, 691, 1182],					# Reason: SalePrice do not match OverallQual(0.791)
			[523, 1298],						# Reason: SalePrice do not match GrLivArea(0.709)
			[581, 1190, 1298, 1061]]			# Reason: SalePrice do not match GarageArea(0.623)

DTYPE_CONVERT_LIST = ["MSSubClass", "MoSold", "YrSold"]

VERBOSE = False
DISPLAY_CORR_FIGURE = False
UNACCEPTABLE_MISSED_RATE = 0.8
ENABLE_OUTLIERS_DISCOVERY = False
DISPLAY_TARGET_HISTOGRAM = False
PRINT_SKEWS = False
MINIMUM_MONOTONOUS_PROPOTION = 0.91
DISPLAY_ENGINEERED_FEATURES = True
MINIMUM_ABANDONED_PROPOTION = 0.9994

####################################################################################

CNT_FOLDS = 5
RANDOM_STATE = 19260817

####################################################################################

SUBMIT = True
RIDGECV_EVAL = False
RIDGECV_TRAIN = True
GBR_EVAL = False
GBR_TRAIN = True

####################################################################################

RIDGECV_PARAM_GRID = {"ridgecv__alphas": [14.5]}
GBR_PARAM_GRID = {"gradientboostingregressor__loss": ["huber"],
				  "gradientboostingregressor__learning_rate": [0.03],
				  "gradientboostingregressor__n_estimators": [1000],
				  "gradientboostingregressor__min_samples_split": [10],
				  "gradientboostingregressor__min_samples_leaf": [5],
				  "gradientboostingregressor__random_state": [RANDOM_STATE],
				  "gradientboostingregressor__subsample": [0.6],
				  "gradientboostingregressor__max_features": [0.3]}

####################################################################################

RIDGECV_PARAM = {"alphas": np.array([14.5]),
				 "cv": CNT_FOLDS}
GBR_PARAM = {"loss": "huber",
			 "learning_rate": 0.03,
			 "n_estimators": 1000,
			 "min_samples_split": 10,
			 "min_samples_leaf": 5,
			 "random_state": RANDOM_STATE,
			 "subsample": 0.6,
			 "max_features": 0.3}

####################################################################################

RIDGE_WEIGHT = 0.7
GRB_WEIGHT = 0.3

####################################################################################

def getTime(as_file_name: bool = False) -> str:
	if as_file_name:
		return time.strftime("%Y-%m-%d-%H-%M-%S")
	else:
		return time.strftime("%Y-%m-%d %H:%M:%S")

def printLog(*msg, to_logs: bool = False) -> None:
	"""Print logs if verbose or force is set to True."""
	if VERBOSE:
		for msg_piece in msg:
			print(msg_piece, end=' ')
		print()
	
	if to_logs:
		with open("log.txt", "a+") as file:
			for msg_piece in msg:
				file.write(msg_piece)
			file.write("\n")

def boot() -> None:
	printLog("\n\n" + "=" * 20 + f"Boot at {getTime()}" + "=" * 20, to_logs=True)