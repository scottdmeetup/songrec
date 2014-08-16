 = ['Freddie King', 'Peter Green', 'T-Bone Walker']
indie = ['Local Natives', 'Concrete Knives', 'Fleet Foxes']

vibe = raw_input('What would you like to hear? ')

from random import choice

if vibe == 'Blues':
    print choice(blues)
    
elif vibe == 'blues':
    print 'Toss on some ' + choice(blues)
    
elif vibe == 'Indie':
    print choice(indie)
    
elif vibe == 'indie':
    print choice(indie)    
    
else:
    print 'Hmm, try typing a genre like Blues or Indie'
