def generateBoard(size):
  return [[None] * size] * size

def isValidCoordinate(x, y, size):
  return x >= 0 and x < size and y >= 0 and y < size

movements = {
  1: [2, 1],
  2: [2, -1],
  3: [-2, 1],
  4: [-2, -1],
  5: [1, 2],
  6: [1, -2],
  7: [-1, 2],
  8: [-1, -2],
}
def getMovementDelta(movementId):
  return movements[movementId]