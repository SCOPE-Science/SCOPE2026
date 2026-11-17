# Independent mathematical audit

## correctness

PASS

The claim is finite and algorithmically exhaustive: for each n<=6 encode all 2^binom(n,2) labelled graphs, test connectivity with BFS, compute each G-v exact integer characteristic polynomial and rational greatest-root isolation, compare roots using disjoint rational intervals or gcd-common-root certification, then quotient exceptions by all n! relabelings. Inspected actual checker.py has explicit loops and aborts on unresolved overlapping intervals; witnesses have characteristic polynomials giving spectral radii 2 versus sqrt(2+sqrt2), and a cubic maximum-degree root versus sqrt((5+sqrt17)/2). An independently written separate enumerator examined all 26,704 connected n=6 graphs and recovered connected totals 1,4,38,728,26704; arbitrary-degree failures 0,0,0,150,7740; all-max-degree failures 0,0,0,0,540; n=6 class sizes {180,360}. Independent second check used floating point and therefore corroborates but does not replace the repository exact root-isolation certificate. The smallest opposing eigenvalue gap was >0.031 in independent numerics.

## originality

PASS

Hanski–Ovaskainen define leading-eigenvalue metapopulation capacity; Ovaskainen gives perturbation formulas; Saha and colleagues analyze general node deletions and spectral-radius minimization. Their inspected claims do not directly state these minimum graph orders or complete five/six-vertex orbit censuses. Resultary semantic searches identified no earlier precise exception census. Best-of-knowledge acceptance carries risk from uninspected complete 2000/2003 original sources and other graph spectra tables.

## value

PASS

A completely classified small-order counterexample boundary for a common degree-based intervention heuristic has clear mathematical motivation and exact combinatorial structure. The strict distinction between arbitrary max-degree tie failure and every-max-degree failure is nontrivial; limited equal-patch adjacency proxy scope is explicitly stated, without extrapolating to real-species extinctions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
