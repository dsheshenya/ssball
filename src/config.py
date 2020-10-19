from kivy.core.window import Window

window_width = Window.size[0]
window_height = Window.size[1]

nodesize_coef = 1
ballsize_coef = 1
net_width_coef = 1

nodesize = window_width * window_height / 19200 * nodesize_coef
ballsize = window_width * window_height / 19200 * ballsize_coef
net_width = window_width / 400 * net_width_coef

fps = 45
quantum = 1 / fps

# gravitational acceleration
g = 2 * window_height / 9

# how hard ball bounces depends on this thing
spring_ability = 1

# node and ball weights
node_weight = 1
ball_weight = 1

# number of goals that are needed to score to win the game
goals_count = 1

# labels font size
font_size = window_width * window_height / 16000

# number of seconds to wait after game ending
restart_waiting = 2
