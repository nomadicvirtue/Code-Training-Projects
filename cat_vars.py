import pandas as pd
import numpy as np

car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())

print(car_eval.manufacturer_country.unique())
freq = (car_eval.manufacturer_country.value_counts())
print(freq)

proportion_mf = car_eval.manufacturer_country.value_counts(normalize=True, dropna=False)
print(proportion_mf)
buying_cost_categories = ['low','med', 'high', 'vhigh']
car_eval['buying_cost'] = pd.Categorical(car_eval['buying_cost'], buying_cost_categories, ordered=True)
print(car_eval['buying_cost'])

bcosts_median_num = np.median(car_eval['buying_cost'].cat.codes)
bcosts_median = buying_cost_categories[int(bcosts_median_num)]
print(bcosts_median)

luggage_proportion = car_eval.luggage.value_counts(normalize=True, dropna=False)
print(luggage_proportion)

print(car_eval['doors'].unique())
more_than_5 = np.sum(car_eval['doors'] == '5more')
print(more_than_5)

doors_prop = car_eval.doors.value_counts(normalize=True, dropna=False)
print(doors_prop)