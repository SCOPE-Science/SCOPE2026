# Independent mathematical audit

## correctness

PASS

Theorem 4.5 and Proposition 4.9 of arXiv:1708.02351 justify the weight-three reduced integral model. The basis count is C(8,k)2^k C(14-k,3-k), giving 364,1248,1344,448. A unit pivot clears its row by integral column additions, then its column by integral row additions; a zero residual gives saturated image, and the homology subgroup of the corresponding free cokernel is free. Connectedness can also be proved directly in the reduced model: degree-one relations exchange adjacent edge variables in degree-three multisets; the line graph is connected, so all degree-three monomials represent the same class in H0. Independently, using Prue–Scrimshaw's once-bisected cubical model, I enumerated (1140,3672,3840,1296) cells, checked both integral boundary squares, and removed all 1296 cubes by free face pairs. Contracting a spanning tree of 1139 edges gave 2533 one-cells and 2544 two-cells; 2527 exact unit pivots and zero residual yield H1=Z^6 and H2=Z^17, and the spine gives the higher vanishing. Replay: python3 /tmp/opencode/graph_triples_audit.py. Neither calculation relies on modular ranks for the absence of torsion.

## originality

FAIL

The October 18 Resultary octahedral-character primary record explicitly states and proves the identical complete integral homology as well as a stronger rational representation theorem. An alternate exact chain model does not make these groups an original finding.

## value

FAIL

A precise integral invariant for this canonical graph is well motivated, but every group and torsion assertion in the frozen claim is already established. The new route certifies the same known groups without classifying any new invariant or offering a structural comparison beyond the finite calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
