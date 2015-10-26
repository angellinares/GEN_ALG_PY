#    This file is part of DEAP.
#
#    DEAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    DEAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with DEAP. If not, see <http://www.gnu.org/licenses/>.

import random

from deap import base
from deap import creator
from deap import tools

# creamos el problema de optimizacion y el individuo
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# inicilizacion de los individuos
toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)

toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 100)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# fitness function
def evalOneMax(individual):
    return sum(individual),

# operaciones geneticas
toolbox.register("evaluate", evalOneMax)
toolbox.register("mate", tools.cxTwoPoint) # crossover de dos puntos
#toolbox.register("mate", tools.cxOnePoint) # crossover de dos puntos

toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3) # selecciona basada en torneo
#toolbox.register("select", tools.selRoulette) # seleccion basada en ruleta


def main():
    random.seed(64) # forma de inicializar la semilla
    
	# creamos la poblacion
    pop = toolbox.population(n=300)
    CXPB, MUTPB, NGEN = 0.5, 0.2, 40 # parametros del algoritmo genetico
    
    print("Comenzamos la evolucion")
    
    # evaluamos la poblacion inicial
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit
    
    print("  Evaluamos el individuo %i" % len(pop))
    
    # empezamos la evolucion
    for g in range(NGEN):
        print("-- Generacion %i --" % g)
        
        # seleccion de indicviduos
        offspring = toolbox.select(pop, len(pop))
        # clonamos los individuos seleccionados
        offspring = list(map(toolbox.clone, offspring))
    
        # aplicamos operaciones geneticas
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values
    
        # evaluamos los nuevos individuos
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        
        print("  Evaluados %i individuos" % len(invalid_ind))
        
        # reemplazamos por la nueva poblacion
        pop[:] = offspring
        
        # estadisticas
        fits = [ind.fitness.values[0] for ind in pop]
        
        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2 / length - mean**2)**0.5
        
        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)
    
    print("-- Final del algoritmo--")
    
    best_ind = tools.selBest(pop, 1)[0]
    print("El mejor indiviudo es %s, %s" % (best_ind, best_ind.fitness.values))

if __name__ == "__main__":
    main()
