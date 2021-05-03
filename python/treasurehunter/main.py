import random
import time

events = ['healing_potion','enemy_weak', 'enemy_normal', 'enemy_hard', 'treasure_common', 'treasure_rare', 'treasure_epic', 'treasure_mythic', 'weapon_upgrade', 'shield_upgrade']
Treasure = 0
answer = 0
HP = 50
weapon_lvl = 1
weapon_dmg = weapon_lvl*5
shield_lvl = 1
shield_blk = shield_lvl*5
room_count = 0
enemy_strength = 1
treasure_rarity = 1
damage_taken = 0
prev_HP = HP
x = 0
Enemy_strength = 0
print('You are a treasure hunter. You just found a map to a secret dungeon with an \nabundance of loot.\nBut there are rumors of it being haunted.')
print('You have just entered into the Dungeon.')
input()
print('\n'*15 + ' '*26 + 'Welcome to the Dungeon' + '\n'*15)
for i in range(100):
    room_event = events[random.randint(0, len(events)-1)]
    room_count += 1
    print(' '*34 + 'Room ' + str(room_count) + ':')
    print(f'There is a {room_event} in this room!')
    if room_event == 'enemy_weak':
        enemy_strength = 1 + Enemy_strength
        print('Time to fight!')
        print(f'You took {enemy_strength*5 - shield_blk}')
        HP -= enemy_strength*5 - shield_blk
        if HP >= prev_HP:
            HP = prev_HP
        if HP >= 50:
            HP = 50
        print(f'Your HP is at {HP}')
        if HP <= 0:
            print('You have no HP left. You died.')
            exit()
    elif room_event == 'enemy_normal':
        enemy_strength = 2 + Enemy_strength
        print('Time to fight!')
        print(f'You took {enemy_strength*5 - shield_blk}')
        HP -= enemy_strength*5 - shield_blk
        if HP >= prev_HP:
            HP = prev_HP
        if HP >= 50:
            HP = 50
        print(f'Your HP is at {HP}')
        if HP <= 0:
            print('You have no HP left. You died.')
            exit()
    elif room_event == 'enemy_hard':
        enemy_strength = 3 + Enemy_strength
        print('Time to fight!')
        print(f'You took {enemy_strength*5 - shield_blk}')
        HP -= enemy_strength*5 - shield_blk
        if HP >= prev_HP:
            HP = prev_HP
        if HP >= 50:
            HP = 50
        print(f'Your HP is at {HP}')
        if HP <= 0:
            print('You have no HP left. You died.')
            exit()
    elif room_event == 'treasure_common':
        print('You found bronze!')
        treasure_rarity = 1
        Treasure += treasure_rarity
        print(f'Your Treasure is now at {Treasure}!')
        if Treasure >= 100:
            print('You found a great amount of Treasure. You left the Dungeon to reap the rewards.')
            quit()
    elif room_event == 'treasure_rare':
         print('You found silver!')
         treasure_rarity = 2
         Treasure += treasure_rarity
         print(f'Your Treasure is now at {Treasure}!')
         if Treasure >= 100:
            print('You found a great amount of Treasure. You left the Dungeon to reap the rewards.')
            quit()
    elif room_event == 'treasure_epic':
        print('You found gold!')
        treasure_rarity = 5
        Treasure += treasure_rarity
        print(f'Your Treasure is now at {Treasure}!')
        if Treasure >= 100:
            print('You found a great amount of Treasure. You left the Dungeon to reap the rewards.')
            quit()
    elif room_event == 'treasure_mythic':
        print('You found diamond!')
        treasure_rarity = 10
        Treasure += treasure_rarity
        print(f'Your Treasure is now at {Treasure}!')
        if Treasure >= 100:
            print('You found a great amount of Treasure. You left the Dungeon to reap the rewards.')
            quit()
    elif room_event == 'weapon_upgrade':
        weapon_lvl += 1
        print('You upgraded your Weapon. It is now level ' + str(weapon_lvl))
        weapon_dmg = weapon_lvl*3
        shield_blk += 3
        print('Your sword now blocks 3 more damage from an enemy.')
        print('Shield_BLK = ' + str(shield_blk))
    elif room_event == 'shield_upgrade':
        shield_lvl += 1
        print('You upgraded your Shield. It is now level ' + str(shield_lvl))
        shield_blk += 5
        print('Your shield now blocks 5 more damage from an enemy.')
        print('Shield_Block = ' + str(shield_blk))
    elif room_event == 'healing_potion':
        print('You healed 10 HP')
        HP += 10
    Enemy_strength += 0.2
    input()
    time.sleep(0.1)