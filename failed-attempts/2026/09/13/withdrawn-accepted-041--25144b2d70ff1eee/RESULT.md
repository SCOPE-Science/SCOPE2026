# Disproof of the order-4 Sklyanin C3-twist census claim

## Context

The admitted target concerns the 3-dimensional Sklyanin algebra S attached to the harmonic curve E1: x^3+y^3+z^3-3*L*xyz=0 with L^2=2 and translation point of exact order 4, over an algebraically closed field k of characteristic 0 containing primitive cube roots of unity, with graded diagonal automorphism d(x,y,z)=(x,w*y,w^2*z) of order 3 generating C3, and the cocycle twist T=S^{C3,mu} for a nontrivial 2-cocycle mu on C3. The target conjunction claims: (a) T is PI of exact PI-degree 4; (b) T is finite over its center with explicit generators and one relation; (c) T has exactly 12 isolated point modules plus one elliptic family; (d) T is Azumaya exactly away from an explicit divisor containing the origin.

## Definitions

Point modules are cyclic graded modules M with dim M_i=1 for all i. The truncated point scheme X_2 in P^2xP^2 is cut out by multilinearizations of the three quadratic relations. H^2(C3,k^x) classifies normalized 2-cocycles mu up to coboundary; a coboundary twist is N-graded isomorphic to the original algebra.

## Result

Clause (c) is false for every 2-cocycle mu on C3: T has zero isolated point modules, not 12. Hence the four-clause conjunction is false. This is a complete TARGET disproof. Clauses (a), (b), (d) are left open.

## Proof / Evidence

Lemma 1 (H^2 collapse): solving all 27 C3 cocycle identities gives b1=b2=a*d with free a,d in k^x; with b=a*d, s^3=a*b (exists since k algebraically closed, char not 3) and t=b/s, gamma(1)=1, gamma(g)=s, gamma(g^2)=t trivializes mu. So every twist T is N-graded isomorphic to S with identical point schemes. Note: the admitted premise of a nontrivial cocycle class is therefore vacuous over the stated ground field.

Lemma 2: d is an order-3 graded automorphism; each Sklyanin relation is semi-invariant with factors 1, w^2, w respectively (machine-verified).

Lemma 3: E1 is smooth; singular ideal is the whole ring on each affine chart, equivalently Hesse criterion L^3=2L != 1 since (L^3)^2=8.

Artin-Tate-Van den Bergh: for smooth-E Sklyanin with translation of order 4, the point scheme is the graph of sigma: one elliptic family, zero isolated points. Transfer to every T via the graded isomorphism.

Independent check: X_2 of T in P^2xP^2 is cut by 3 bidegree-(1,1) forms (twisted relations keep 3 generators and 3 nonzero relations by nonzero rescaling), so under Segre P^2xP^2 -> P^8 every component has dimension >= 4-3 = 1 by the projective dimension theorem; no zero-dimensional components, hence zero isolated point modules. 0 != 12 disproves clause (c) and the conjunction.

## Limitations

Clauses (a) PI-degree, (b) finite-center presentation, and (d) Azumaya divisor are not adjudicated. The ATV citation is a standard published theorem; all symbolic steps are machine-verified but the disproof depends on that theorem plus standard dimension theory.

## Reproducibility

Run output/artifacts/verify_disproof.py (sympy only); it prints ALL CHECKS PASSED covering cocycle classification, coboundary identity, semi-invariant factors, smoothness Groebner bases, and support preservation.

## References

Artin-Tate-Van den Bergh, Some algebras associated to automorphisms of elliptic curves; Hartshorne Ch. I projective dimension theorem; Davies arXiv:1512.05717 (nearest prior: 4-dim V4 twist, distinct); Walton-Wang-Yakimov PI Sklyanin literature.
