blues = ['Freddie King', 'Peter Green', 'T-Bone Walker']
indie = ['Local Natives', 'Concrete Knives', 'Fleet Foxes']
play = ['http://open.spotify.com/track/43dq9zGNruyR2WIWo5UrqF', 'http://open.spotify.com/track/2ebgoF10aoezaV3zece18B']

vibe = raw_input('What would you like to hear? ')

from random import choice

if vibe == 'Blues' or vibe == 'blues':
    print 'Toss on some ' + choice(blues)
    
elif vibe == 'Indie' or vibe == 'indie':
    print choice(indie) 
    
elif vibe == 'play':
    print choice(play)
    
else:
    print 'Hmm, try typing a genre like Blues or Indie'
