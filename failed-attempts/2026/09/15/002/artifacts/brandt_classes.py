"""Ideal class enumeration for maximal order disc 109 + Brandt matrices.
Method: right ideals via HNF in basis; classes via theta-function fingerprints + equivalence test by shortvectors.
Represent lattice in R^4 via embedding: norm form diag(1,2,109,218) on L-coords; O element a+bv handled by half-integer coords.
Right ideal J (Z-basis 4 vecs in Q^4): test right-O-stability; norm N(J)=sqrt([O:J])... N(J) = sqrt(det(J-basis)/det(O-basis)).
Plan:
 1. O-basis HNF matrix (in half-integer coords scaled by 2): rows = 2*coords of {1,i,j,k... } use basis B_O = {(2,0,0,0),(0,2,0,0),(0,0,2,0),(0,0,0,2),(0,1,0,1)} scaled... simpler: work in Z^4 scaled lattice S=2*O with basis {(2,0,0,0),(0,2,0,0),(0,0,2,0),(0,0,0,2),(0,1,0,1)}.
 2. Enumerate right subideals of O of norm l via M2(F_l) minimal right ideals (pullback), as Z-modules (HNF).
 3. Class invariant: theta series / successive minima of (J, N/N(J)) + left-order size. Identify classes by BFS from O.
"""
from fractions import Fraction
from itertools import product
import numpy as np
print("numpy", np.__version__)
