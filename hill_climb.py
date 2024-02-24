import numpy as np

def mutations(individual):
    res = []
    for i in individual:
        if int(i) == 0:
            r = 1
        elif int(i) == 1:
            r = 0
        res.append(np.random.choice([int(i), r], p=[0.7, 0.3]))
    return ''.join([str(i) for i in res])

def hill_climber(pop):
    generations=0
    fitness = pop[0].count('1')
    while fitness < len(pop[0]):
        generations = generations + 1
        res = mutations(*pop)
        fitness2 = res.count('1')
        if fitness2 > fitness:
            pop = [res]
            fitness = fitness2
        print('Gen:',generations,'Fitness:', fitness, ' Individual:', pop,'\n')
    return fitness, pop

fitness, pop = hill_climber(['000000000000'])
print('Fitness:', fitness, '\nResulting Individual:', pop)
