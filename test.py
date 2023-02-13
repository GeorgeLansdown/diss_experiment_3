# importing required library
import pygame
import os

participant_number = input("Enter participant number:\n")
results = []

# activate the pygame library .
pygame.init()
X = 356
Y = 356
real_rect = [50,130, 120,50]
fake_rect = [190,130, 120,50]

# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('deepfake test')

images = [pygame.image.load("test_set/"+file_name).convert() for file_name in sorted(os.listdir(os.getcwd()+"/test_set"),key=lambda x: int(x[:-4]))]

smallfont = pygame.font.SysFont('Corbel',35)

pygame.display.flip()


def image(n):
    scrn.blit(images[n], (50,50))
    pygame.display.update()
    pygame.time.wait(2000)

def buttons(n,mouse):
    # if mouse is hovered on a button it
    # changes to lighter shade
    fake = smallfont.render('Deepfake' , True , (0,0,0))
    scrn.blit(fake, fake_rect)
    pygame.draw.rect(scrn,(217,33,33),fake_rect,1)


    real = smallfont.render('Real' , True , (0,0,0))
    scrn.blit(real, real_rect)
    pygame.draw.rect(scrn,(124,252,0),real_rect,1)


    # scrn.blit(smallfont.render('Real' , True , (0,0,0)) , (125,50))
    # pygame.draw.rect(scrn,(217,33,33),[50,50,125,125])
    # superimposing the text onto our button


    pygame.display.update()

n = 0
clicked = True
while (n < len(images)):
  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for i in pygame.event.get():

        if i.type == pygame.MOUSEBUTTONDOWN:
            if 50 <= mouse[0] <= 170 and 130 <= mouse[1] <= 180 and not clicked :
                clicked = True
                n+=1
                results.append((n,'REAL'))
            if 190 <= mouse[0] <= 310 and 130 <= mouse[1] <= 180 and not clicked:
                clicked = True
                n+=1
                results.append((n, 'FAKE'))

        if i.type == pygame.QUIT:
            n = len(images)+1

    scrn.fill((255,255,255))

    if clicked and n <len(images):
        image(n)
        clicked = False
    if not clicked:
        mouse = pygame.mouse.get_pos()
        buttons(n,mouse)


with open(str(participant_number)+'.csv','w') as file:
    for n,r in results:
        file.write("%s,%s\n" % (n,r) )
# deactivates the pygame library
pygame.quit()
