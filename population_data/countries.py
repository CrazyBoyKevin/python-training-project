import pygal.maps.world

for country_code in sorted(pygal.maps.world.COUNTRIES.keys()):
  print(country_code, pygal.maps.world.COUNTRIES[country_code])