# Independent mathematical audit

## correctness

PASS

For integers m,r≥2, the complete DFA tracks the zero count modulo P, scattered 001 count modulo m, and trailing-one run in {0,…,r−1}, with one rejecting sink. The shift difference dz+binom(d,2) forces d divisible by m and binom(d,2)=0 mod m; hence the exact least period P is m for odd m and 2m for even m. Starting with two zeros, a single marker one followed by P zeros increments the count by one without changing the zero residue modulo P or exceeding the run cap. This reaches every count, after which appending zeros and a prescribed final run with a compensated count reaches every legal triple. For unequal runs, kill the longer run then calibrate the surviving state to acceptance; for equal zero residue and different count residues, a common calibration can accept only one. For unequal zero residues, write f(a),g(a) for their increments after a zeros, and choose B with f(B)=1 and C=g(B). There must be a b with g(b)−Cf(b) nonzero modulo m: otherwise second differences force C=1, and the equal shifts contradict exact period. A suitable increment at B makes two probes, using zero or one marker at b, both accept for the first state; they cannot both accept for the second. Leading and separating zeros make these probes run-safe including r=2. The sink is reachable and has no accepted continuation, unlike every nonsink state. Thus exactly rPm+1 states are necessary and sufficient. Independent bounded minimizations for (m,r)=(2,2),(3,2),(4,3),(5,2),(6,3) gave 17,19,97,51,217, with direct triple counting through word length nine; replay: /workspace/branches/9da90b86-f47e-4bf3-b804-7c20f171c2bc/record3_independent_check.py. Those tests do not prove the universal result. The supplied checker was inspected, not executed.

## originality

PASS

The modular counter and its odd/even state period are already covered for unrestricted words. Pass applies to exact simultaneous run-cap minimality, not to those ingredients. No matched statement covers the constrained theorem in the evidence available; this is a best-of-knowledge assessment, not a priority certification.

## value

PASS

This is an exact deterministic memory requirement for a natural conjunction of a scattered-count test and a local run constraint. It resolves whether enforcement of the run rule allows any of the modular-state memory to be shared or discarded, uniformly for all caps and composite as well as prime moduli: none can be discarded, and the unrestricted parity jump survives in full. The value is in the tight lower bound and constructive run-safe separation, not the obvious product construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
