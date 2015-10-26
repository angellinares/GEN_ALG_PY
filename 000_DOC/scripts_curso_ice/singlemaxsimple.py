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
import numpy
from deap import base
from deap import creator
from deap import tools
from deap import algorithms

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

toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3) # selecciona basada en torneo

def main():
	random.seed(64) # forma de inicializar la semilla
    
	# creamos la poblacion
	pop = toolbox.population(n=300)
	CXPB, MUTPB, NGEN = 0.5, 0.2, 40 # parametros del algoritmo genetico
	hof = tools.HallOfFame(1)
	stats = tools.Statistics(lambda ind: ind.fitness.values)
	stats.register("avg", numpy.mean)
	stats.register("std", numpy.std)
	stats.register("min", numpy.min)
	stats.register("max", numpy.max)

	pop = algorithms.eaSimple(pop, toolbox, CXPB, MUTPB, NGEN, stats=stats, 
                        halloffame=hof)    
	print "El mejor indiviudo es %s" % hof
	print "Con un fitness: %d" % len(hof[0])

if __name__ == "__main__":
    main()
