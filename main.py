# names of hurricanes
from collections import defaultdict


names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille',
         'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September',
          'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977,
         1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160,
                       175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], [
    'Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M',
           'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11,
          2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# write your update damages function here:

# 1
# Update Recorded Damages


def updated_damages(damages_lst):
    new_damages_list = []
    for idx in range(len(damages_lst)):
        if damages_lst[idx] == "Damages not recorded":
            new_damages_list.append(damages_lst[idx])
        elif "M" in damages_lst[idx]:
            split_item = damages[idx].split("M")
            new_damages_list.append(float(split_item[0]) * 1000000)
        else:
            split_item = damages[idx].split("B")
            new_damages_list.append(float(split_item[0]) * 1000000000)
    return new_damages_list


updated_damages_lst = updated_damages(damages)

# print(updated_damages_lst)

# write your construct hurricane dictionary function here:


def hurricane_dict():
    hurricane = {}
    for name, month, year, wind, area, damage, death in zip(names, months, years, max_sustained_winds, areas_affected, updated_damages_lst, deaths):
        hurricane.update({name: {
            "Name": name,
            "Month": month,
            "Year": year,
            "Max. Sustained wind": wind,
            "Area affected": area,
            "Damages": damage,
            "Deaths": death
        }})
    return hurricane


dict = hurricane_dict()
# print(dict)


# for key, value in dict.items():
#     print("These is '{0}' hurricane \n".format(key))


# write your construct hurricane by year dictionary function here:
def hurricane_dict_year():
    hurricane_dict_by_year = {}

    for name, month, year, wind, area, damage, death in zip(names, months, years, max_sustained_winds, areas_affected, updated_damages_lst, deaths):
        hurricane_dict_by_year.update({year: [{
            "Name": name,
            "Month": month,
            "Year": year,
            "Max. Sustained wind": wind,
            "Area affected": area,
            "Damages": damage,
            "Deaths": death
        }]})
    return hurricane_dict_by_year


dict_year = hurricane_dict_year()

# print(dict_year[1932])


# write your count affected areas function here:
def count_affected_area(h_dict):
    area_affected_dict = {}
    for area in h_dict:
        for location in h_dict[area]['Area affected']:
            if not location in area_affected_dict:
                area_affected_dict[location] = 1
            else:
                area_affected_dict[location] += 1
    return area_affected_dict


count_area = count_affected_area(dict)
print(count_area)

# write your find most affected area function here:


# write your greatest number of deaths function here:


# write your catgeorize by mortality function here:


# write your greatest damage function here:


# write your catgeorize by damage function here:
