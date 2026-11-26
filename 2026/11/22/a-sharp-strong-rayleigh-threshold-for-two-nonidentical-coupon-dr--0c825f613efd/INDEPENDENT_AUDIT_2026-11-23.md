# Independent mathematical audit

## correctness

PASS

The ordered draws give linear coefficients (t,t²,t) and pair coefficients (t²+t,t²+1,t²+t) in order xy,xz,yz, with total (2t+1)². For the general degree-two form αx+βy+γz+Axy+Bxz+Cyz the xy Rayleigh difference is (α+Bz)(β+Cz)−Aγz. The three discriminants coincide and equal (u²−v²−w²)²−4v²w² with u=√(Aγ), v=√(Bβ), w=√(Cα); hence their being nonpositive is precisely the triangle condition for u,v,w. Here u=w=t√(t+1), v=t√(t²+1), giving t²+1≤4(t+1) or 0<t≤2+√7. All leading coefficients are positive, so discriminant equality is included by the all-real multiaffine criterion. The rederived exact witness is R_xz(7/36)=−325/36 at t=5. For each pair and each draw, joint absence has lower probability than the product of the two absence probabilities; combining independent draws and complementing yields strict negative covariance. The count is 1+Bernoulli with success probability 1−(t²+2t)/(2t+1)². One draw gives a stable linear form, at most two types give just Ax+By+Cxy with Rayleigh difference AB≥0 for nonzero rounds, and zero rounds give the constant 1. Thus the type and draw counts really are minimal. The supplied verify.py was inspected but not executed.

## originality

PASS

The supported distinct claim is the exact weighted two-draw transition, with a size-minimal separation of strong Rayleigh from pairwise negative correlation and real-rooted cardinality. Credit established multiaffine stability theory, uniform occupancy results, and standard pairwise negative dependence. No stronger evaluated weighted classification or equivalent exact threshold was established by the compared sources; priority is not certified.

## value

PASS

The explicit boundary answers how far uniform-packet stability persists in a strictly positive, round-dependent deformation, and exactly where it stops even though familiar negative-dependence and one-variable diagnostics still hold. The obstruction occurs at the smallest possible type and draw counts, not an arbitrary large example. This makes the sharp witness and transition useful; the shifted-Bernoulli marginal on its own is routine.

The dated certificate retains the supplied scientific assessment, sources and limitations.
