import numpy as n

import board as b

n.random.seed(1)

boardSize = 8
initialX = 0
initialY = 0

def generateValidGene(size, x=initialX, y=initialY):
  gene = n.random.randint(1, size + 1)

  [deltaX, deltaY] = b.getMovementDelta(gene)
  newX = x + deltaX
  newY = y + deltaY

  if b.isValidCoordinate(newX, newY, size):
    # print 'gene', newX, newY, size
    return gene

  return generateValidGene(size, x, y)

def generateValidChromossome(size, x=initialX, y=initialY):
  chromossome = list()
  
  while len(chromossome) < size * size:
    gene = generateValidGene(size, x, y)
    chromossome.append(gene)

    [deltaX, deltaY] = b.getMovementDelta(gene)
    x += deltaX
    y += deltaY
    # print 'chromossome', x, y, size

  return chromossome

def validateGene(board, size, x, y, gene, attempt=1):
  [deltaX, deltaY] = b.getMovementDelta(gene)
  # print 'board actual', x, y
  # print 'board delta', deltaX, deltaY
  newX = x + deltaX
  newY = y + deltaY

  # print 'board future', newX, newY
  if board[newX][newY] is None:
    return [newX, newY]

  # if attempt < 10:
  #   newGene = generateValidGene(size)
  #   return validateGene(board, size, x, y, newGene, attempt + 1)
  
  return [False, False]

def calculateFitness(board, chromossome):
  visited = 1
  step = 1
  x = initialX
  y = initialY

  for gene in chromossome:
    [newX, newY] = validateGene(board, boardSize, x, y, gene)

    if newX is False:
      break

    board[newX][newY] = step
    visited += 1
    step += 1
    
    x = newX
    y = newY

  return visited

def mutate(chromossome, size):
  index = n.random.randint(0, len(chromossome))
  childGenes = list(chromossome)
  newGene = generateValidChromossome(size)
  childGenes[index] = newGene[index]
  return childGenes

def start(size):
  board = b.generateBoard(size)
  chromossome = generateValidChromossome(size)

  iteration = 1
  fitness = 0
  while fitness < 50 and iteration < 10:
    fitness = calculateFitness(board, chromossome)
    newChromossome = mutate(chromossome, size)
    newFitness = calculateFitness(board, newChromossome)

    print '#%s: %s => %s' % (iteration, fitness, newFitness)
    if newFitness > fitness:
      chromossome = newChromossome
    iteration += 1

start(boardSize)