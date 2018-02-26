from numpy import random

heroes = ['Captain America', 'Black Widow', 'Hawkeye', 'Hulk', 'Iron Man', 'Thor',
          'Cyclops', 'Emma Frost', 'Storm', 'Rogue', 'Gambit', 'Wolverine', 'Spider-man'
          , 'Nick Fury', 'Deadpool']

pickh = []
pickh = random.choice(heroes, 5, replace=False)
print(pickh)

mm = ['Red Skull', 'Magneto', 'Dr. Doom', 'Loki']

pickmm = random.choice(mm)

print(pickmm)

scheme = ['Legacy Virus', 'Midtown Bank Robbery', 'Negative Zone Prison Breakout',
          'Portals to the Dark Dimension', 'Repleace Earths Leaders with Killerbots',
          'Secret Invasion of the Skrull Shapeshifters', 'Super Hero Civil War',
          'Unlease the Power of the Cosmic Cube']
picks = random.choice(scheme)

print(picks)

henchmen = ['Doombot', 'Hand Ninjas', 'Sentinel', 'Savage Land Mutants']

pickh = random.choice(henchmen)
print(pickh)

villians = ['Brotherhood', 'Masters of Evil', 'Spider-Foes', 'Hydra', 'Skrulls', 'Enemies of Asgard', 'Radiation']
pickv = random.choice(villians, 2, replace=False)
print(pickv)


