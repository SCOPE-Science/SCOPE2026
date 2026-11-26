# Independent mathematical audit

## correctness

PASS

Convex averaging over within-part permutations and A/B exchange preserves stochasticity and the support and attains the unrestricted optimum value in the invariant class. With r=q/p, u=px, v=qy, the feasibility conditions are u,v>=0, u+v<=1, v<=r/2; the four nonconstant Laplacian modes are 2u+v, u+v, 2v/r, and (1+2/r)v. At modulus t the first two reduce to max(0,1-t-v)<=u<=min(1-v,(1+t-v)/2). The constraint v>=1-3t meets v<=r/2 for r<=1/2 and v<=r(1+t)/(r+2) for 1/2<=r<=1, forcing the first two singleton choices. For 1<=r<=4 the last two modes force t>=r/(r+4), equality fixing v=2r/(r+4). Substitution gives the two u intervals split at r=2. For r>=4, v<=1 and the 2v/r mode force t>=1-2/r, with equality at v=1,u=0. The displayed weights meet the remaining bounds, agree at shared endpoints, and every optimum averages to one of them. Nonnegative AB weights give the forced-positive-total and forced-zero unrestricted statements from the invariant average; the intermediate endpoint witnesses are valid. The uniqueness used in the proof is of invariant weights. Inspected the supplied verification notes and verify.py; their recorded run is not an independent rerun. The independently authored /workspace/branches/dc7aa6fc-b11b-475d-91cd-ccd4e8e3ab0c/endpoint_lp.py checks the invariant LP at p=12 with 13 q values including the four boundaries and neighboring integers; worst SLEM difference was 1.11e-16 and returned weights met the listed ranges. The finite LP panel does not prove the theorem or classify nonsymmetric optima.

## originality

FAIL

The cited literature supplies the general framework and balanced/bipartite examples. The distinct indexed result c991250fdec2 solves the more general prescribed-class-mass reversible problem, including every invariant optimizer interval and the same unrestricted AB support conclusions. At uniform per-vertex mass its feasible matrices are exactly the frozen symmetric ones; its formulas and thresholds specialize to the frozen table without any additional result. Its visible November 2 date is later than the frozen October 27 date. This finding is about duplicate mathematical coverage, not priority, chronology of discovery, or dependence.

## value

FAIL

Phase transitions and unrestricted support properties are worthwhile in themselves, but each claimed property here is directly available by converting the existing prescribed-mass solution to uniform stationarity. This specialization supplies no independently useful unknown invariant or structural conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
