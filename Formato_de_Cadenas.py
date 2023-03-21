name = 'Ganymede'
gravity = '1.43'
planet = 'Mars'

template = """Gravity Facts about {0}
--------------------------
Planet Name: {2}
Gravity on {0}: {1} m/s2""" .format(name,gravity,planet)

print(template)