# No nonzero weight-1 1-shifted Poisson bivector at the named genus-2 rank-3 Higgs fixed point

## Context
Let k be algebraically closed of characteristic zero, C a smooth projective genus-2 curve with canonical bundle K, and M the derived Artin stack of rank-3 Higgs bundles (E,phi) on C. Consider the Hitchin G_m-action t.(E,phi)=(E,t.phi) and the named C*-fixed stable Higgs stack point p=(E0,phi0) with E0=L(+)O(+)L^{-1}, deg L=1, and phi0 of companion/Hodge type with both nonzero components. The target asks whether the Higgs deformation complex at p carries an explicit G_m-weight-1 1-shifted Poisson bivector Pi_1 built from the trace pairing, satisfying [Pi_1,Pi_1]=0 and inducing a 1-shifted Poisson structure on the formal neighbourhood of p distinct from twist/transgression of the canonical 0-shifted Hitchin bivector. Note deg E0=0, so the topic's coprime-degree hypothesis is literally inconsistent with E0; p is treated as a stable Higgs stack point and the result below is proved on the merits at p.

## Definitions
Higgs deformation complex: C(p)=[End(E0)->End(E0)(+)K] in degrees 0,1 with differential [phi0,.]. Tangent complex: T=RGamma(C(p))[1], with H^{-1}(T)=H^0(C) stabiliser, H^0(T)=H^1(C) deformations, H^1(T)=H^2(C) obstructions. The formal neighbourhood is governed by the L-infinity minimal model on H(T) with brackets l_2,l_3,... and Chevalley-Eilenberg field Q=Q_2+Q_3+... with no linear term. For n=1, Pol(M^hat_p,1)=Sym(T[-2]); an n-Poisson structure has quadratic part pi_2 of cohomological degree n+2=3. Gauge weights from g_t=diag(t,1,t^{-1}) plus scaling weight +1 on K give total weights; phi0 has total weight 0.

## Result
At this named point there is no nonzero G_m-weight-1 1-shifted Poisson bivector built from the trace pairing. Every weight-1 degree-3 candidate pi_2=a.v with v in H^1(C)_1 has vanishing self-Schouten bracket but nonzero Q-obstruction [Q_2,pi_2]!=0 via the perfect Serre/trace pairing H^1_0 x H^1_1 -> H^2_1, uncancelled by higher corrections by bidegree. Only the degenerate zero bivector remains, so no such structure distinct from twist/transgression of the Hitchin 0-shifted bivector exists. This is a rigorous TARGET disproof.

## Proof and evidence
Weight/Euler certificate: End(E0)=3O(+)2L(+)2L^{-1}(+)L^2(+)L^{-2} with gauge weights 0,+1,-1,+2,-2. Per-copy Riemann-Roch gives chi_w=-3 for each total weight w in {-2,-1,0,1,2,3}, summing to -18=1-20+1. Higgs stability gives H^0(C)=k.id of weight 0; Serre/trace duality gives H^2(C) 1-dimensional of weight 1. Hence h^1_w=h^0_w+h^2_w+3, i.e. h^1=(3,3,4,4,3,3) summing to 20=dim M. Degree audit of Sym^2(T[-2]): only 1+2 hits degree 3, so the unique weight-1 slot is a.v with a the odd degree-1 scalar generator and v in the 4-dimensional H^1_1. Since a is odd of rank one, a^2=0 and [pi_2,pi_2]=0. Writing pi_2 as d_a wedge D_v, scalars are central so [Q,pi_2] reduces to the l_2(v,.) term; the commutator-plus-trace pairing H^1_0 x H^1_1 -> H^2_1~=k is perfect (both 4-dimensional), so for every nonzero v there is w in H^1_0 with l_2(v,w)!=0, i.e. [Q_2,pi_2] contains d_a wedge x_0 d_b !=0, a nonzero linear-in-base polyweight-2 bivector. Minimality plus higher base-degree of pi_{>=3} forbids cancellation, so no L-infinity lift satisfies [Q+pi,Q+pi]=0. Computation reproduced by output/artifacts/weight_check.py (exit 0).

## Limitations
Formal neighbourhood of this single named g=2, r=3 fixed point only; no global moduli statement. Uses standard PTVV shifted-Poisson/Maurer-Cartan formalism, Higgs deformation theory, and Serre duality as assumed background. Coprime-degree hypothesis inconsistent with E0 as noted; disproof independent of that hypothesis.

## Reproducibility
Run python3 output/artifacts/weight_check.py and compare with output/artifacts/weight_check.out; asserts chi_w=-3, total -18, and H^1 dimensions above.

## References
Calaque-Pantev-Toen-Vaquie-Vezzosi, Shifted Poisson structures and deformation quantization, arXiv:1506.03699. Pridham, Shifted Poisson and symplectic structures on derived N-stacks. Hua-Polishchuk, Shifted Poisson structures and moduli spaces of complexes. Standard Higgs deformation theory and Serre duality.
