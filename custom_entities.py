from ursina import *


class Trash(Entity):
    def __init__(self):
        super().__init__(
            model='quad',
            scale=(.25, .25),
            origin=(-.5, .5),
            position=(0, 0),
            texture='white_cube',
            texture_scale=(1, 1),
            color=color.pink
        )
        self.name = "Trash"
        self.etiquette = "Non-identifiable"
        self.valeur = 0
        self.degat = 0


class Inventory(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            origin=(-.5, .5),
            position=(0, 0),
            texture='white_cube'
        )
        self.colonnes = 3
        self.lignes = 2
        self.texture_scale = (self.colonnes, self.lignes)
        self.scale_x = self.colonnes / 10
        self.scale_y = self.lignes / 10
        self.item_parent = Entity(parent=self, scale=(1 / self.colonnes, 1 / self.lignes))
        self.trash_list = []  # liste de Trash()
        # change enabled to activer ou desactiver l'inventaire --> inventaire invisible par defaut
        self.enabled = False
        self.taille = self.colonnes * self.lignes
        self.taille_max = self.colonnes * self.lignes  # taille maxe en fonction du scale

    def find_free_spot(self):
        taken_spots = []
        for e in self.trash_list:
            print(e.etiquette)
            taken_spots.append((e.x, e.y))
        for y in range(self.lignes):
            for x in range(self.colonnes):

                if not (x, -y) in taken_spots:
                    # print("FREE  x=" + str(x) + " / y=" + str(y))
                    return x, -y

    def append(self, t):
        # on place le trash au bon endroid dans l inventaire
        t.parent = self.item_parent
        t.model = 'quad'
        t.origin = (-.5, .5)
        t.position = self.find_free_spot()
        t.z = self.z - 1
        print("APPEND : " + t.etiquette + "pos= " + str(t.position))

        # on ajoute le trash a la liste de contenu de l inventaire
        self.trash_list.append(t)

    def pop(self, i=0):
        if self.trash_list:
            print(self.trash_list)
            t = self.trash_list.pop(i)
            t.parent = self.item_parent
            t.model = 'quad'
            t.origin = (-.5, .5)
            t.position = self.find_free_spot()
            t.z = self.z - 1
            print("POP : " + t.etiquette + "pos= " + str(t.position))

            return t
    def enable_inv(self):
        self.enable()
        for t in self.trash_list:
            # print("Enable " + t.etiquette + "pos= " + str(t.position))
            t.enable()

    def disable_inv(self):
        self.disable()
        for t in self.trash_list:
            t.disable()


class Contenant(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = 'cube'
        self.parent = scene
        self.origin_y = -.5
        self.scale_y = 1
        self.color = color.green
        self.collider = "box"

        self.animator = Animator({'idle': None, 'walk': None, 'jump': None})
        # self.animation_state_machine.state = 'jump'
        # self.idle_animation = None
        # self.walk_animation = None
        # self.jump_animation = None
        # self.idle_animation = Entity(parent=self, model='cube', color=color.gray, origin_y=-.5, scale_z=2)
        # self.walk_animation = Animation(parent=self, texture='ursina_wink', color=color.red, origin_y=-.5, scale=(2,2), double_sided=True)

        self.name = "Contenant"
        self.inventaire = Inventory()

    def append(self, t):
        self.inventaire.append(t)

    def pop(self, i=0):
        return self.inventaire.pop(i)

    def display_contenu(self):
        self.inventaire.enable_inv()

    def fill_rand_trash(self, n=0):
        for i in range(n):
            t = Trash()
            t.etiquette += str(i)
            self.append(t)


class Poubelle(Contenant):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = 'cube'
        self.collider = "box"
        self.color = color.green

        self.animator = Animator({'idle': None, 'walk': None, 'jump': None})
        # self.animation_state_machine.state = 'jump'
        # self.idle_animation = None
        # self.walk_animation = None
        # self.jump_animation = None
        # self.idle_animation = Entity(parent=self, model='cube', color=color.gray, origin_y=-.5, scale_z=2)
        # self.walk_animation = Animation(parent=self, texture='ursina_wink', color=color.red, origin_y=-.5, scale=(2,2), double_sided=True)
        # self.model = None

        self.name = "Poubelle"
        self.inventaire.position = (.45, .4)
        self.inventaire.color = color.green


class Marmite(Contenant):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = 'sphere'
        self.collider = "sphere"
        self.color = color.red

        self.animator = Animator({'idle': None, 'walk': None, 'jump': None})
        # self.animation_state_machine.state = 'jump'
        # self.idle_animation = None
        # self.walk_animation = None
        # self.jump_animation = None
        # self.idle_animation = Entity(parent=self, model='cube', color=color.gray, origin_y=-.5, scale_z=2)
        # self.walk_animation = Animation(parent=self, texture='ursina_wink', color=color.red, origin_y=-.5, scale=(2,2), double_sided=True)
        # self.model = None

        self.name = "Marmite"
        self.recette = []  # liste de Trash.name à ramener pour gagner la parte
        self.inventaire.position = (0, .4)
        self.inventaire.color = color.red
