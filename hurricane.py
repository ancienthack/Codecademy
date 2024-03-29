# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(damages):
    damages_dict = {'B':1000000000, 'M':1000000}
    for i in range(len(damages)):
        if 'B' in damages[i]:
            damages[i] = damages[i].strip('B')
            damages[i] = float(damages[i]) * damages_dict['B']
        elif 'M' in damages[i]:
            damages[i] = damages[i].strip('M')
            damages[i] = float(damages[i]) * damages_dict['M']
    return damages

updated_damages = update_damages(damages)
# print(updated_damages)

# write your construct hurricane dictionary function here:
def hurricane_dict():
    hurricanes = {}
    for i in range(len(names)):
        hurricanes[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": updated_damages[i], "Deaths": deaths[i]}
    return hurricanes

hurricanes = hurricane_dict()
# print(hurricanes)
# print(hurricanes['Cuba I'])

# write your construct hurricane by year dictionary function here:
def hurricane_by_year(hurricanes):
    hurricane_years = {}
    for hurricane in hurricanes:
        current_year = hurricanes[hurricane]['Year']
        current_hurricane = hurricanes[hurricane]
        if current_year not in hurricane_years.keys():
            hurricane_years[current_year] = [hurricanes[hurricane]]
        else:
            hurricane_years[current_year].append(hurricanes[hurricane])
    return hurricane_years

hurricanes_by_year = hurricane_by_year(hurricanes)
# print(hurricanes_by_year)
# print(hurricanes_by_year[1932])

# write your count affected areas function here:
def count_affected_areas(hurricanes):
    counted_areas = {}
    for hurricane in hurricanes:
        current_list = hurricanes[hurricane]['Areas Affected']
        for area in current_list:
            if area not in counted_areas:
                counted_areas[area] = 1
            else:
                counted_areas[area] += 1
    return counted_areas

counted_areas = count_affected_areas(hurricanes)
# print(counted_areas)
# print(counted_areas['Mexico'])

# write your find most affected area function here:
def most_affected_area(areas):
    area_value_list = list(areas.values())
    area_value_list.sort()
    highest_value = area_value_list[-1]
    for area in areas:
        if highest_value in areas.values():
            return 'The most affected area is {area}, being hit {value} times.'.format(area = area, value = highest_value)

# function written as suggested by hint.
    # max_area = ''
    # max_count = 0
    # for area in areas:
    #     if max_count < areas[area]:
    #         max_count = areas[area]
    #         max_area = area
    # return 'The most affected area is {area}, being hit {value} times.'.format(area = max_area, value = max_count)

most_affected_area = most_affected_area(counted_areas)
# print(most_affected_area)

# write your greatest number of deaths function here:
def greatest_deaths(hurricanes):
    death_values = []
    for hurricane in hurricanes:
        death_values.append(hurricanes[hurricane]['Deaths'])
    death_values.sort()
    greatest_deaths = death_values[-1]
    for hurricane in hurricanes:
        if greatest_deaths in hurricanes[hurricane].values():
            return 'The greatest number of deaths were caused by Hurricane {hurricane}, totaling {deaths} lives lost.'.format(hurricane = hurricane, deaths = greatest_deaths)

# hint suggestioin
    # max_death_cane = ''
    # max_deaths = 0
    # for hurricane in hurricanes:
    #     if max_deaths < hurricanes[hurricane]['Deaths']:
    #         max_deaths = hurricanes[hurricane]['Deaths']
    #         max_death_cane = hurricane
    # return 'The greatest number of deaths were caused by Hurricane {hurricane}, totaling {deaths} lives lost.'.format(hurricane = max_death_cane, deaths = max_deaths)

# greatest_deaths = greatest_deaths(hurricanes)
# print(greatest_deaths)

# write your catgeorize by mortality function here:
def mortality_scale(hurricanes):
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    mortality_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane in hurricanes:
        deaths = hurricanes[hurricane]['Deaths']
        if deaths == 0:
            mortality_dict[0].append(hurricanes[hurricane])
        elif deaths > mortality_scale[0] and deaths <= mortality_scale[1]:
            mortality_dict[1].append(hurricanes[hurricane])
        elif deaths > mortality_scale[1] and deaths <= mortality_scale[2]:
            mortality_dict[2].append(hurricanes[hurricane])
        elif deaths > mortality_scale[2] and deaths <= mortality_scale[3]:
            mortality_dict[3].append(hurricanes[hurricane])
        elif deaths > mortality_scale[3] and deaths <= mortality_scale[4]:
            mortality_dict[4].append(hurricanes[hurricane])
        elif deaths > mortality_scale[4]:    
            mortality_dict[5].append(hurricanes[hurricane])
    return mortality_dict

mortality_scale = mortality_scale(hurricanes)
# print(mortality_scale)
# prints value of key, then access index of list value
# print(mortality_scale[4][0])

# write your greatest damage function here:
def greatest_damage(hurricanes):
    max_damage = 0
    max_damage_cane = ''
    for hurricane in hurricanes:
        damage = hurricanes[hurricane]['Damage']
        if damage == 'Damages not recorded':
            continue
        elif damage == int or float:
            if max_damage < damage:
                max_damage = damage
                max_damage_cane = hurricane
    return 'The greatest damage was caused by Hurricane {hurricane}, totaling ${damage} USD.'.format(hurricane = max_damage_cane, damage = max_damage)

greatest_damage = greatest_damage(hurricanes)
# print(greatest_damage)

# write your catgeorize by damage function here:
def damage_scale(hurricanes):
    damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
    damage_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane in hurricanes:
        damage = hurricanes[hurricane]['Damage']
        if damage == 'Damages not recorded':
            continue
        elif damage == 0:
            damage_dict[0].append(hurricanes[hurricane])
        elif damage > damage_scale[0] and damage <= damage_scale[1]:
            damage_dict[1].append(hurricanes[hurricane])
        elif damage > damage_scale[1] and damage <= damage_scale[2]:
            damage_dict[2].append(hurricanes[hurricane])
        elif damage > damage_scale[2] and damage <= damage_scale[3]:
            damage_dict[3].append(hurricanes[hurricane])
        elif damage > damage_scale[3] and damage <= damage_scale[4]:
            damage_dict[4].append(hurricanes[hurricane])
        elif damage > damage_scale[4]:    
            damage_dict[5].append(hurricanes[hurricane])
    return damage_dict

damage_scale = damage_scale(hurricanes)
# print(damage_scale)
# prints value of key, then access index of list value
print(damage_scale[5][0])





