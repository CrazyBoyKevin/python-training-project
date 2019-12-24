import  pygal.maps.world

wm = pygal.maps.world.Worldmap()
wm.title = 'Population od Countries in North America'
wm.add('North America',
       {
         'ca': 34126000,
         'us': 309349000,
         'mx': 113423000
       })

wm.render_to_file('na_population.svg')
