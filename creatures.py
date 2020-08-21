import random as rnd
import pandas as pd
import numpy as np


class Creature():
    def __init__(self, full_health, speed, nature, health, sex=None):
        self.full_health = full_health
        self.speed = speed
        self.nature = nature
        self.health = health
        alias = rnd.randint(1, 2)
        if alias == 2:
            self.sex = 0
        else:
            self.sex = 1

    def describe(self):
        print(f'Max Health: {self.full_health}')
        print(f'Current Health: {self.health}')
        print(f'Speed: {self.speed}')
        print(f'Sex: {self.sex}')
        print(f'Nature: {self.nature}')

    def adjust_speed(self):
        extra_bulk = self.full_health-27
        speed_adjustment = np.random.normal(extra_bulk, 3, 1)
        self.speed = self.speed - speed_adjustment
        if self.speed < 0:
            self.speed = 0


class SelfishCreature(Creature):
    def __init__(self, full_health, speed, health, nature=None, sex=None):
        Creature.__init__(self, full_health, speed, nature, health, sex=None)
        self.nature = 'selfish'


class SharingCreature(Creature):
    def __init__(self, full_health, speed, health, nature=None, sex=None):
        Creature.__init__(self, full_health, speed, nature, health, sex=None)
        self.nature = 'sharing'


def original_gen(group_size, group_nature):
    group = list()
    healths = np.random.normal(30, 3, group_size)
    speeds = np.random.normal(30, 3, group_size)
    for x in range(0, group_size):
        if group_nature == 'selfish':
            creature = SelfishCreature(
                full_health=healths[x],
                speed=speeds[x],
                health=healths[x])
            group.append(creature)
        elif group_nature == 'sharing':
            creature = SharingCreature(
                full_health=healths[x],
                speed=speeds[x],
                health=healths[x])
            group.append(creature)

    return group


def generate_child(mother, father):
    sm = np.random.normal(0, 3, 1)
    hm = np.random.normal(0, 3, 1)
    child_health = (father.full_health + mother.full_health)/2 + hm
    child_speed = (father.speed + mother.speed)/2 + sm
    if father.nature == 'selfish' and mother.nature == 'selfish':
        creature = SelfishCreature(
            full_health=float(child_health[0]),
            speed=float(child_speed[0]),
            health=float(child_health[0]))
    elif father.nature == 'sharing' and mother.nature == 'sharing':
        creature = SharingCreature(
            full_health=float(child_health[0]),
            speed=float(child_speed[0]),
            health=float(child_health[0]))
    else:
        x = rnd.randint(1, 2)
        if x == 1:
            creature = SelfishCreature(
                full_health=float(child_health[0]),
                speed=float(child_speed[0]),
                health=float(child_health[0]))
        else:
            creature = SharingCreature(full_health=float(
                child_health[0]), speed=float(child_speed[0]), health=float(child_health[0]))

    creature.adjust_speed()

    return creature


def mating(group):
    males = [creature for creature in group if creature.sex ==
             1 and creature.health > 0]
    females = [creature for creature in group if creature.sex ==
               0 and creature.health > 0]
    size = len(group)
    new_group = []
    if len(males) == 0 or len(females) == 0:
        pass
    else:
        for x in range(int(round(size/2))):
            father_index = rnd.randint(0, len(males) - 1)
            mother_index = rnd.randint(0, len(females) - 1)
            for x in range(2):
                creature = generate_child(
                    females[mother_index], males[father_index])
                new_group.append(creature)
    return new_group


def hunting(creature):
    x = rnd.randint(0, 100)
    if creature.speed > x:
        y = 1
    else:
        y = 0

    return y


def feeding(group, days):
    for day in range(days):
        for creature in group:
            if hunting(creature) == 1 and float(creature.health) > 0:
                if creature.nature == 'selfish':
                    creature.health += 10
                if creature.nature == 'sharing':
                    for x in range(0, 10):
                        r = rnd.randint(0, len(group)-1)
                        group[r].health += 1
                        if creature.health == 1:
                            creature.health = 0
            else:
                creature.health -= 3

        for creature in group:
            if creature.health > creature.full_health:
                creature.health = creature.full_health
            elif creature.health < 0:
                creature.health = 0
            else:
                pass

    return group
