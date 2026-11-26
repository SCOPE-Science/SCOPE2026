# Independent mathematical audit

## correctness

PASS

The frozen spectral formula is mathematically correct: on the sum-zero plane its quadratic is z^2+pz+2p-1; the real-root radius strictly decreases to the discriminant zero and the conjugate radius then strictly increases. At the double eigenvalue, the zeros preclude the scalar-on-the-plane form Pi+lambda(I-Pi), so the nilpotent term is nonzero and the generic n prefactor follows. The repaired claim no longer treats this as an independent optimization. In the repaired theorem Birkhoff support unions have at least five cells unless they are a single permutation. A five-cell union has a shared cell and a unique alternating square; diagonal shared cells give reducibility, whereas the off-diagonal pairs have one orbit, a three-cycle plus a transposition, and the mixture is primitive by the cycle and loop. Writing P=B23 C with C the displayed three-cycle gives P^3=B23 B13 B12 by conjugation and C^3=I. All edge orders are induced by vertex relabelings. Determinants of candidate cubes fix the real parameter via injectivity of x^3, even at p=1/2. In the representative B13 B23 B12, the first diagonal entry exceeds the other two by (1-p)^3; the remaining swap cannot stabilize the matrix since entries (1,2) and (1,3) differ by p(1-p)^2. Thus each labeled sweep has a unique root within the five-entry primitive bistochastic class. The exact rational checker `python3 /workspace/repairs/4/verify.py` passed 9 feasible supports, 6 primitive supports and 114 labeled sweeps; uniqueness over the continuum rests on the proof, not the grid.

## originality

PASS

Frozen originality fails for the central sharp mixing claim as an independent result: the exact matrix cube, not just an isospectral relative, is an already studied sweep. For the heat branch p>1/2 the previously optimized sweep rate gives the one-step optimum by taking cube roots. The earlier population result covers the cubic spectrum for all interior p at the same parameter and the generic Jordan term. The repaired finding instead claims the support threshold and the exhaustive, unique minimum-support cube-root correspondence. That support-constrained inverse problem is not settled by the earlier forward products or general stochastic-root classifications inspected here.

## value

PASS

The repair identifies an exact homogeneous realization of a time-ordered heterogeneous triangle sweep, with the smallest possible number of allowed transitions compatible with primitive uniform stationarity. It characterizes every such sparse realization and settles labeled uniqueness, including at singular weight, so a researcher designing or inferring a sparse one-step kernel from these three-step observations can use the exact claim. Value is not assigned to republishing the prior optimal rate or Jordan effect in different units.

The dated certificate retains the supplied scientific assessment, sources and limitations.
