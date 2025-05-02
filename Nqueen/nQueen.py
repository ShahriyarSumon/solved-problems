
import random
def create_individual(n):
    return [random.randint(0, n - 1) for _ in range(n)]
def fitness(individual):
    n = len(individual)
    clashes = 0
    for i in range(n):
        for j in range(i + 1, n):
            if individual[i] == individual[j] or abs(individual[i] - individual[j]) == abs(i - j):
                clashes += 1
    return -clashes
def select_pair(population):
    return random.choice(population), random.choice(population)
def crossover(parent1, parent2):
    point = random.randint(0, len(parent1) - 1)
    child = parent1[:point] + parent2[point:]
    return child
def mutate(individual, mutation_rate=0.1):
    if random.random() < mutation_rate:
        index = random.randint(0, len(individual) - 1)
        individual[index] = random.randint(0, len(individual) - 1)
    return individual
def genetic_algorithm(n, population_size=100, generations=1000):
    population = [create_individual(n) for _ in range(population_size)]

    for gen in range(generations):
        population = sorted(population, key=fitness, reverse=True)

        if fitness(population[0]) == 0:
            print("Solution found in generation", gen)
            return population[0]

        new_population = []

        while len(new_population) < population_size:
            parent1, parent2 = select_pair(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    print("No perfect solution found.")
    return population[0]
solution = genetic_algorithm(n)
print("One solution:")
print(solution)

def print_board(solution):
    n = len(solution)
    for row in range(n):
        line = ""
        for col in range(n):
            if solution[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)

print("\nChess Board:")
print_board(solution)
