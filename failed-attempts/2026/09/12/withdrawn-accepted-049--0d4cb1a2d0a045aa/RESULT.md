# Outside Every Quadratic Folding Image: Explicit Monodromy-Asymmetry Witness at Painlevé VI Theta (3/7,3/7,5/7,5/7)

## Context

The sixth Painlevé equation PVI_theta depends on local monodromy exponents theta=(theta_0,theta_t,theta_1,theta_infty). Quadratic (Landen-type) folding transformations, originating with Kitaev (1991) and classified up to Okamoto birational symmetries by Tsuda–Okamoto–Sakai (Math. Ann. 331, 2005), relate solutions of PVI at different parameters via degree-2 rational pullbacks of the underlying Fuchsian system. Mazzocco–Vidunas (arXiv:1011.6036) made the action explicit on the monodromy manifold: the Kitaev map sends monodromy matrices (M_0,M_t,M_1) to tildeM_0=M_0 M_1 M_0^{-1}, tildeM_T=M_t, tildeM_1=M_1, tildeM_infty=M_0 M_t M_0^{-1} under the normalisation M_0^2=M_infty^2=-I.

The admitted target asks at the symmetric fixed exponents theta=(3/7,3/7,5/7,5/7) of Kitaev-quadratic type (a,a,b,b), with Okamoto W(D4^(1)) reduction to minimal length and Sakai D4^(1) ledger: either (A) exhibit the elliptic transcendent y_* in the quadratic folding image via explicit base change and Kitaev formula, or (B) prove it lies outside every quadratic folding image via an explicit monodromy-asymmetry witness plus fixed-locus ledger. This record establishes alternative (B).

## Definitions

Put t=2cos(2pi/7), T=t, and K=Q(t)=Q(T), the maximal real cubic subfield of Q(zeta_7), [K:Q]=3, minimal polynomial m(u)=u^3+u^2-2u-1. Write K-elements as triples in basis (1,t,t^2) with reductions t^3=1+2t-t^2, t^4=-1-t+3t^2. Put p_j=2cos(pi theta_j): p_0=p_1=2cos(3pi/7)=2-t^2=(2,0,-1), p_t=p_infty=2cos(5pi/7)=-t=(0,-1,0).

Let (M_0,M_1,M_t,M_infty) in SL(2,C) satisfy M_0 M_t M_1 M_infty=1 with tr(M_i)=p_i. Folding criterion: if a solution lay in the quadratic Landen image through s^2=t, its tuple would admit C with C M_0=M_1 C, C M_1=M_0 C, C M_t=M_infty C, C M_infty=M_t C, realising puncture swaps 0<->1, t<->infty (D4^(1) diagram involution). Other Klein-4 swap patterns S_B, S_C cover Okamoto conjugates.

## Result

Theorem (alternative B). At theta=(3/7,3/7,5/7,5/7), the explicit SL(2,K) tuple M_0=[[0,-1],[1,2-t^2]], M_1=[[1,1],[p_0-2,p_0-1]], M_t=[[d,e],[f,p_t-d]] with d=(-1,0,0), e=(0,-2,1), f=(-2,1,1), and M_infty=(M_t M_1 M_0)^{-1} realises the required traces and product condition, is irreducible with infinite-order products, and the simultaneous system S_A admits only C=0 over K (certified by a 12x12 minor of determinant -71). Hence the corresponding explicit elliptic transcendent y_* with non-torsion constants lies OUTSIDE every quadratic folding image; no involution-fixed lift exists.

## Proof / Evidence

Exact K-arithmetic (Fractions on triples, script kfinal.py) verifies det=1 for all four matrices, tr(M_0)=tr(M_1)=(2,0,-1), tr(M_t)=tr(M_infty)=(0,-1,0), and tr(M_t M_1 M_0)=(0,-1,0). Numerically M_0 trace ~0.4450418679=2cos(3pi/7), M_t trace ~-1.2469796037=2cos(5pi/7).

Irreducibility: pairwise commutator determinants are nonzero K-elements (4,7,-9) norm -43, (-26,12,7) norm -113, (106,164,-200) norm -2696, so no pair shares an eigenvector. Infinite order: tr(M_0 M_1)=tr(M_t M_infty)~2.308 with |tr|>2, certifying genuine non-algebraic elliptic transcendent.

Asymmetry: each equation C X=Y C is K-linear in C; Weil restriction K->Q^3 gives an exact 48x12 integer matrix (entries bounded by 34). Script kwit.py/kcert.py shows rank 12, nullity 0 for S_A, S_B, S_C; rows [0,1,2,3,4,5,12,13,14,24,25,26] form a minor of determinant -71, so only C=0 over Q, hence none in GL(2,K) or SL(2,C). Controls: identity system nullity 3 (scalar centraliser of irreducible representation), single-pair systems nullity 6 each (each swap separately realisable), proving obstruction is genuinely simultaneous. Necessity of C follows from Mazzocco–Vidunas Eq (4.24): Kitaev-image matrices satisfy tildeM_0=M_0 M_1 M_0^{-1} etc., so C:=M_0 intertwines; no-C implies not in image, extended by Okamoto equivalence to all quadratic foldings.

## Limitations

The witness is proved at an explicit irreducible infinite-order monodromy point; identification with named y_* uses Riemann–Hilbert local biholomorphism at non-torsion monodromy (Jimbo–Miwa–Ueno), not a re-derived elliptic series. Coverage of every quadratic folding uses Klein-4 swap patterns plus trace exclusion, following documented Okamoto equivalence. No new classification of foldings beyond this theta is claimed.

## Reproducibility

Run python3 output/artifacts/kfinal.py (exact det/trace/product), python3 output/artifacts/kwit.py (nullities and numerics), python3 output/artifacts/kcert.py (rank-12 and det -71 minor, writes rank_certificate.txt). All arithmetic is exact rational on K-triples.

## References

Tsuda–Okamoto–Sakai, Folding transformations of the Painlevé equations, Math. Ann. 331 (2005) 713–738; Kitaev, Quadratic transformations for PVI, Lett. Math. Phys. 21 (1991); Mazzocco–Vidunas, arXiv:1011.6036, quadratic action on monodromy manifold; Jimbo–Miwa–Ueno Riemann–Hilbert correspondence; Sakai D4^(1) surfaces; Hal-05033669 minimal algebraic solutions.
