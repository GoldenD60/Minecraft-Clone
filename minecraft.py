from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

grass_texture = load_texture('Minecraft Assets/grass_block_uv.png')
stone_texture = load_texture('Minecraft Assets/stone_uv.png')
brick_texture = load_texture('Minecraft Assets/bricks_uv.png')
dirt_texture  = load_texture('Minecraft Assets/dirt_uv.png')
sky_texture   = load_texture('Minecraft Assets/skybox.png')
arm_texture   = load_texture('Minecraft Assets/hand.png')
grass_sound1  = Audio('Minecraft Assets/grass_block_sound1.ogg', loop = False, autoplay = False)
grass_sound2  = Audio('Minecraft Assets/grass_block_sound2.ogg', loop = False, autoplay = False)
stone_sound1  = Audio('Minecraft Assets/stone_sound1.ogg', loop = False, autoplay = False)
stone_sound2  = Audio('Minecraft Assets/stone_sound2.ogg', loop = False, autoplay = False)
brick_sound1  = Audio('Minecraft Assets/stone_sound1.ogg', loop = False, autoplay = False)
brick_sound2  = Audio('Minecraft Assets/stone_sound2.ogg', loop = False, autoplay = False)
dirt_sound1   = Audio('Minecraft Assets/dirt_sound1.ogg', loop = False, autoplay = False)
dirt_sound2   = Audio('Minecraft Assets/dirt_sound2.ogg', loop = False, autoplay = False)
block_pick = 1

window.cog_button.visible = False

def update():
    global block_pick

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'Minecraft Assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.white,
            highlight_color = color.light_gray,
            scale = 0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                if block_pick == 1:
                    grass_sound1.play()
                    voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                elif block_pick == 2:
                    stone_sound1.play()
                    voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                elif block_pick == 3:
                    brick_sound1.play()
                    voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
                elif block_pick == 4:
                    dirt_sound1.play()
                    voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
            elif key == 'left mouse down':
                if block_pick == 1:
                    grass_sound2.play()
                elif block_pick == 2:
                    stone_sound2.play()
                elif block_pick == 3:
                    brick_sound2.play()
                elif block_pick == 4:
                    dirt_sound2.play()

                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            texture = arm_texture,
            scale = 0.4,
            position = Vec2(0.6, -0.31)
        )

for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x,0,z))

player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()