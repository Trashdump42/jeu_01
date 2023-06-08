from ursina import *
from ursina.prefabs.health_bar import HealthBar
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
banana.color = color.yellow

chocolat = Trash()
chocolat.etiquette = "chocolat"
chocolat.color = color.brown

myrtille = Trash()
myrtille.etiquette = "myrtille"
myrtille.color = color.violet

orange = Trash()
orange.etiquette = "orange"
orange.color = color.orange

orange2 = Trash()
orange2.etiquette = "orange2"
orange2.color = color.orange

poubelle.append(banana)
poubelle.append(chocolat)
poubelle.append(myrtille)
poubelle.append(orange)
poubelle.append(orange2)





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


"""
print("Poubelle type : " + poubelle.type)
print("poubelle Z_scale = " + str(poubelle.scale_z))

print("player Z = " + str(player.z))
print("player Z_scale = " + str(player.scale_z))

"""

def hit_keuf():
    if player.intersects(keuf).hit:
        player.health_bar_1.value -= 1
        if player.x > keuf.x:
            player.position = (player.x + .5, player.y, player.z)
        if player.x <= keuf.x:
            player.position = (player.x - .5, player.y, player.z)
        if player.health_bar_1.value == 0:
            print('die')
            player.position = player.start_position

def display_contenu():
    if poubelle.x <= player.x < poubelle.x + poubelle.scale_x or poubelle.x <= player.x+player.scale_x < poubelle.x + poubelle.scale_x :
        poubelle.inventaire.enable_inv()
    else:
        poubelle.inventaire.disable_inv()
    if marmite.x <= player.x < marmite.x + marmite.scale_x or marmite.x <= player.x+player.scale_x < marmite.x + marmite.scale_x :
        marmite.inventaire.enable_inv()
    else:
        marmite.inventaire.disable_inv()

def update():
    hit_keuf()
    display_contenu()





"""# generation automatique de colliders

noise = PerlinNoise(octaves=randint(8, 10), seed=randint(1, 1000000000000))


class Voxel(Button):
    def __init__(self, position):
        super(Voxel, self).__init__(
            parent=scene,
            model='quad',
            scale=(.5, .5, .01),
            position=position,
            texture='imgs/mur2.png'
        )


for z in range(1):
    for x in range(10):
        y = 1 * noise([x / randint(8, 12), z / 20])
        voxel = Voxel(position=(x / 2 + 10, y, z))
###"""

# Camera
camera.orthographic = True
camera.fov = 13
camera.add_script(SmoothFollow(target=player, offset=(1, 1, -100)))
###

Sky()
app.run()
