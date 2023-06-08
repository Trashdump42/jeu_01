from custom_player import *
from custom_entities import *


app = Ursina()
# proprietes joueur :
player_start_position = (1, 0, -.5)

player = Player(scale=(.3, 1, .01), start_position=player_start_position,
                jump_height=1.5, gravity=0.4, walk_speed=3, max_jumps=2,
                texture="perso")

# proprietes des entites utilisables :
z_utilisable = 1
z_scale_utilisable = .5

poubelle = Poubelle()
#poubelle.fill_rand_trash(4)
banana = Trash()
banana.etiquette = "banane"
banana.position= (1, 0, -.5)
chocolat = Trash()
chocolat.etiquette = "chocolat"

poubelle.trash_list.append(banana)
poubelle.trash_list.append(chocolat)

poubelle.position = Vec3(3, .5, z_utilisable)
poubelle.scale = Vec3(1, 1, z_scale_utilisable)

marmite = Marmite()
marmite.position = Vec3(-3, .5, z_utilisable)
marmite.scale = Vec3(1, 1, z_scale_utilisable)

# proprietes monstres :
z_monstres = 0
z_scale_monstres = .1

keuf = Entity(model='cube', position=(0, -1, z_monstres), scale=(1, 1, z_scale_monstres), collider="box", color=color.blue)



# proprietes univers :

ground = Entity(model='cube', position=(0, -2, 0), scale_x=50, collider="box", texture="imgs/mur2.png")
wall = Entity(model='cube', scale=(1, 5), position=(5.5, 0, 0), collider="box", texture='brick')
etage1 = Entity(model='cube', scale=(10, 1, .01), position=(1, 0, 0), collider="box")
etage2 = Entity(model='cube', scale=(2, 1, .01), position=(3, 2, 0), collider="box", texture='brick')

#Camera
camera.orthographic = True
camera.fov = 13
camera.add_script(SmoothFollow(target=player, offset=(1, 1, -100)))
###

app.run()