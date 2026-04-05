# -*- coding: utf-8 -*-

# 데이터 준비
import numpy as np
import pandas as pd

housing = pd.read_csv('../week04/housing.csv')

# 테스트 세트 만들기
from sklearn.model_selection import train_test_split

housing["income_cat"] = pd.cut(housing["income_cat"])