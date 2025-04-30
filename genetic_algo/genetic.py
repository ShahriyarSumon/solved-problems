import random

T = int(input("T = "))
k = int(input("k = "))

population_size = 100
generations = 1000
mutation_rate = 0.2


def create_individual():
    individual = []
    for _ in range(k):
        individual.append(random.randint(1, 9))
    return individual

def get_fitness(individual):
    product = 1
    for num in individual:
        product *= num
    if product == T:
        return 999999
    return 1 / (1 + abs(T - product))

def select(population):
    selected = random.sample(population, 5)
    selected.sort(key=get_fitness, reverse=True)
    return selected[0]
def crossover(p1, p2):
    point = random.randint(1, k - 1)
    return p1[:point] + p2[point:]

def mutate(individual):
    if random.random() < mutation_rate:
        index = random.randint(0, k - 1)
        individual[index] = random.randint(1, 9)
    return individual

def genetic_algorithm():
    population = []
    for _ in range(population_size):
        population.append(create_individual())

    for _ in range(generations):
        population.sort(key=get_fitness, reverse=True)
        best = population[0]
        if get_fitness(best) == 999999:
            return best

        new_population = []
        for _ in range(population_size):
            parent1 = select(population)
            parent2 = select(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    return population[0]

result = genetic_algorithm()

print(result)

product = 1
for num in result:
    product *= num

