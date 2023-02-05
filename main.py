# Exercise!
# Display the image below to the right hand side where the 0 is
# going to be ' ', and the 1 is going to be '*'. This will reveal
# an image!
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
GUI = []
new_GUI = []
k = ' '
i = 0
while i < len(picture):
    for j in picture[i]:
        if j == 0:
            print(' ', end=' ')
        else:
            print('*', end=' ')

    print('\n')

    i += 1
