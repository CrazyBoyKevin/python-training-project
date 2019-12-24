import pygal.maps.world

def get_country_code(country_name):
  for code, name in pygal.maps.world.COUNTRIES.items():
    if name == country_name:
      return code
    return None


