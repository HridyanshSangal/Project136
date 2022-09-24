import pandas as pd
df3 = pd.read_csv('filtered_stars.csv')
star_name = df3['Star_name'].to_list()
mass = df3['Mass'].to_list()
radius = df3['Radius'].to_list()
gravity = df3['Gravity'].to_list()
distance = df3['Distance'].to_list()
final_list = []
for planet_data in df3:
  temp_dict = {
    'Star_name':star_name,
    'Distance':distance,
    'Mass':mass,
    'Radius':radius,
    'Gravity':gravity
    }
  final_list.append(temp_dict)
print(final_list)