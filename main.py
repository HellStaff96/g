from pygame import *
init()
level1 = [
    "r                                                                    .",
    "r                                                                    .",
    "r                                                                    .",
    "r                                                                    .",
    "rr    °  °      l                             r    °  °  °     l     .",
    "r  ------------                                ---------------       .",
    "rr / l                                       r / l         r / l     .",
    "rr   l                                       r   l         r   l     .",
    "rr     °  l                       r     °  °     l   r         l     .",
    "r  ------                           ------------       -------       .",
    "r     r / l                                          r / l           .",
    "r     r   l                                          r   l           .",
    "r     r       °  °   l                       r   °  °    l           .",
    "r       ------------                           ---------             .",
    "r                r / l                       r / l                   .",
    "r                r   l                       r   l                   .",
    "r                                                                    .",
    "----------------------------------------------------------------------"] #Матір Божьє это уровень 

level1_width = len(level1[0]) * 48  # Ширина уровня
lever_height = len(level1) * 40     # Высота уровня

W = 1280
H = 720


window = display.set_mode((W, H))
back = transform.scale(image.load('images/bgr.png'), (W, H))
display.set_caption('Blocked')
display.set_icon(image.load('images/portal.png')) # Иконка окна

''''Тута картиночки :3'''

# Спрайт игрока
hero_l = "images/sprite1.png"
hero_r = "images/sprite1_r.png"
# Спрайт врага
enemy_l = "images/cyborg.png"
enemy_r = "images/cyborg_r.png"
# Спрайт монеточЕк 
coin_img = "images/coin.png"

door_img = "images/door.png" # Спрайт дверей
key_img = "images/key.png"# Спрайт ключа
# Спрайты Сундука
chest_open = "images/cst_open.png"
chest_close = "images/cst_close.png"

stairs = "images/stair.png"# Спрайт лестницы
portal_img = "images/portal.png" # Спрайт порталаа
platform = "images/platform.png" # Спрайт платформы
power = "images/mana.png" # Мана какая-то О_о
nothing = "images/nothing.png" # Спрайт... ааээ.. Пустоты?

class Settings(sprite.Sprite): # Это - база 😋
    def __init__(self, x, y, width, height, speed, img):
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.image = transform.scale(image.load(img), (self.width, self.height))
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Settings): #Для игрока
    def r_l(self):
        pass
    def u_d(self):
        pass

class Enemy(Settings): #Для врага
    def __init__(self, x, y, width, height, speed, img, side):
        Settings.__init__(self, x, y, width, height, speed, img)
        self.side = side

    def update(self):
        pass

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)
    
    def apply(self, target):
        return target.rect.move(self.state.topleft)
    
    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

    def camera_config(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + W / 2, -t + H / 2
    
    l = min(0, l)  # Не виходимо за ліву межу
    l = max(-(camera.width - W), l)  # Не виходимо за праву межу
    t = max(-(camera.height - H), t)  # Не виходимо за нижню межу
    t = min(0, t)  # Не виходимо за верхню межу
    
    return Rect(l, t, w, h)

def collides():
    pass

def menu():
    pass

def rules():
    pass

def pause():
    pass

def restart():
    pass



def start_pos():
    global items
    global camera
    camera = Camera(camera_config, level1_width, lever_height)

    items = sprite.Group()
    
    block_r = []
    block_l = []
    plat = []
    coins = []
    stairs_lst = []
    x = 0
    y = 0

    for r in level1:
        for c in r:
            if c == '-':
                p1 == Settings(x, y, 40, 40, 0, platform)
                plat.append(p1)
                items.add(p1)
            if c == 'l':
                p2 == Settings(x, y, 40, 40, 0, nothing)
                block_l.append(p2)
                items.add(p2)
            if c == 'r':
                p3 == Settings(x, y, 40, 40, 0, nothing)
                block_r.append(p3)
                items.add(p3)
            if c == '°':
                p4 == Settings(x, y, 40, 40, 0, coin_img)
                coins.appends(p4)
                items.add(p4)
            if c == '/':
                p5 == Settings(x, y, 40, 40, 0, stairs)
                stairs_lst.append(p5)
                items.add(p5)
            x += 40
        y += 40
        x = 0

def lvl1():
    game = True
    while game:
        time.dilay(18)
        for e in event.get():
            if e.type == QUIT:
                game == False
    
    for i in items:
        window.blit(i.image, camera.apply(i))

    display.update()

def lvl1_end():
    pass

start_pos()
lvl1()