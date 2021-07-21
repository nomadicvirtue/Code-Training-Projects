# names of hurricanes
from typing import List, Any, Union

names: list[Union[str, Any]] = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# 1. Updated damages list

def updated(damages):
  new_list_damages = []
  for i in damages:
      if i == "Damages not recorded":
          new_list_damages.append("Damages not recorded")
      elif i[-1:] == "M":
          new_list_damages.append(float(i.removesuffix("M")) * 1000000)
      elif i[-1:] == "B":
          new_list_damages.append(float(i.removesuffix("B")) * 1000000000)
  return new_list_damages

updated_damages = updated(damages)
#print(updated_damages)


# 2. Hurricane dictionary defined by names

comb_list = list(zip(names, months, years, max_sustained_winds, areas_affected, updated_damages))
dictionary_1 = {}
def fun_dict(dictionary_1):
    for i in range(0, len(comb_list)):
      dictionary_1[names[i]] = {"Name": names[i], "Mounth": months[i], "Year": years[i],
                              "Max Sustained Wind": max_sustained_winds[i],
                              "Areas Affected": areas_affected[i],
                              "Damage": updated_damages[i], "Deaths": deaths[i]}
    return dictionary_1

hurricane_dict = fun_dict(dictionary_1)
#print(hurricane_dict)

# 3. Dictionary defined by years

dict = {}
def dict_by_years(dict):
  for value in hurricane_dict.values():
    year = value["Year"]
    if year not in dict:
      dict[year] = [value]
  return dict

d_by_year = dict_by_years(dict)
#print(d_by_year)


# 6. Dictionary of areas to store the number of hurricanes involved in
from collections import defaultdict
dict = defaultdict(int)
def count_areas(dict):
    for value in hurricane_dict.values():
        areas = value["Areas Affected"]
        for area in areas:
            if area not in dict:
                dict[area] = 1
            else:
                dict[area] += 1
    return dict

num_areas = count_areas(dict)
#print(num_areas)


# 7. Function indicating hurricane caused max number of deaths

def max_deaths(hurricane_dict):
    max_mortality_cane = "Cuba I"
    max_mortality = 0
    for k, v in hurricane_dict.items():
        if v['Deaths'] > max_mortality:
          max_mortality = v['Deaths']
          max_mortality_cane = k
    return max_mortality_cane, max_mortality
death_d = max_deaths(hurricane_dict)
#print(death_d)

# 8. Dictionary to store scale of mortality

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
hurricanes_by_mortality = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
def scale_canes(hurricanes_by_mortality):
    for v in hurricane_dict.values():
        if v['Deaths'] == 0:
            hurricanes_by_mortality[0].append(v)
        elif v['Deaths'] > 0 and v['Deaths'] <= 100:
            hurricanes_by_mortality[1].append(v)
        elif v['Deaths'] > 100 and v['Deaths'] <= 500:
            hurricanes_by_mortality[2].append(v)
        elif v['Deaths'] > 500 and v['Deaths'] <= 1000:
            hurricanes_by_mortality[3].append(v)
        elif v['Deaths'] > 100 and v['Deaths'] <= 10000:
            hurricanes_by_mortality[4].append(v)
        else:
            hurricanes_by_mortality[5].append(v)
    return hurricanes_by_mortality
mort_scale_canes = scale_canes(hurricanes_by_mortality)
#print(mort_scale_canes)

# 9. Function to indicate hurricane caused the greatest damage

new_damages = []
def greatest_damage(hurricane_dict):
    max_damage_cane = ''
    max_damage = 0
    for k, v in hurricane_dict.items():
        if v['Damage'] == 'Damages not recorded':
            pass
        else:
            new_damages.append(v['Damage'])
            for i in new_damages:
                if i > max_damage:
                    max_damage = i
                    max_damage_cane = k
    return max_damage_cane, max_damage

greatest_damage = greatest_damage(hurricane_dict)
#print(greatest_damage)


# 10. Dictionary to store scale of damage

damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
def damage_scale(hurricanes_by_damage):
    for v in hurricane_dict.values():
        if v['Damage'] == 'Damages not recorded':
            hurricanes_by_damage[0].append(v)
        elif v['Damage'] > 0 and v['Damage'] <= 100000000:
            hurricanes_by_damage[1].append(v)
        elif v['Damage'] > 100000000 and v['Damage'] <= 1000000000:
            hurricanes_by_damage[2].append(v)
        elif v['Damage'] > 1000000000 and v['Damage'] <= 10000000000:
            hurricanes_by_damage[3].append(v)
        elif v['Damage'] > 10000000000 and v['Damage'] <= 50000000000:
            hurricanes_by_damage[4].append(v)
    return hurricanes_by_damage
#print(damage_scale(hurricanes_by_damage))
