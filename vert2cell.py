from numba import jit
import numpy as np

@jit(nopython=True)
def vert2cellnumba(nEdgesOnCell, verticesOnCell, fieldv):
    # Initialize the output fieldc array
    nVertLevels, nCells = fieldv.shape[0], verticesOnCell.shape[1]
    fieldc = np.zeros((nVertLevels, nCells), dtype=np.float64)

    for k in range(nVertLevels):
        for i in range(nCells):
            factor = 1.0 / nEdgesOnCell[i]
            fieldc[k, i] = 0.0
            for j in range(nEdgesOnCell[i]):
                fieldc[k, i] += fieldv[k, verticesOnCell[j, i]]
            fieldc[k, i] *= factor

    return fieldc
