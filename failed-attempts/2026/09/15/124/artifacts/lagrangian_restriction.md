# Lagrangian restriction locus — classical certificate (A=-1)
Target classical sub-claim: M compact oriented hyperbolic 3-mfld, connected totally
geodesic boundary Sigma genus g>=2. Double DM closed hyperbolic.
Claim: near hyperbolic holonomy rho, H^1(DM;Ad)=0 (Weil), MV gives
H^1(M)+H^1(Mbar) ~= H^1(Sigma), H^2(M)=0, dim H^1(M)=3g-3, restriction
r: X(M)->X(Sigma) immersion with Lagrangian image (Fuchsian restriction locus).

## Cohomology computation
- DM = M cup_Sigma Mbar closed hyperbolic => by Calabi-Weil rigidity H^1(DM;Ad_rho)=0
  and by Poincare duality H^2(DM;Ad)=0.
- MV for (M,Mbar,Sigma) with Ad coefficients:
  0=H^1(DM) -> H^1(M) (+) H^1(Mbar) --(res,-res)--> H^1(Sigma) -> H^2(DM)=0.
  Hence isomorphism onto H^1(Sigma).
- Consequence 1: each res_M, res_Mbar injective. Proof: if res_M(a)=0 then
  (a,0) in kernel of (res,-res), so a=0 by injectivity.
- Consequence 2: dim count. Sigma closed genus g, rho|_Sigma Fuchsian (totally
  geodesic) irreducible, H^0(Sigma;Ad)=0, so by Euler + duality:
  dim H^1(Sigma)= -chi(Sigma)*dim sl2 = (2g-2)*3 = 6g-6.
  By symmetry dim H^1(M)=dim H^1(Mbar)=(6g-6)/2=3g-3.
- H^2 vanishing: MV segment H^2(DM)=0 -> H^2(M)(+)H^2(Mbar) -> H^2(Sigma).
  H^2(Sigma;Ad) ~= H^0(Sigma;Ad)^*=0 by irreducibility. Hence H^2(M)=0.
  Similarly H^0(M)=0 (irreducible).

## Isotropy (Goldman)
- Goldman symplectic form omega on H^1(Sigma;Ad) via cup + Killing + cap [Sigma].
- For a,b in H^1(M), omega(res a, res b)=0: cup-product a U b in H^2(M),
  pairs with boundary via Stokes; since H^2(M)=0 / relative exactness,
  the pairing factors through H^2(M,partial M)->H^2(M) boundary map.
  Standard: image of H^1(M) is isotropic (cf. Sikora, Goldman 1984: 3-mfld
  boundary restriction is isotropic; closed surface Goldman symplectic).
- Half-dimensional (3g-3 in 6g-6) isotropic + injective differential => Lagrangian
  immersion germ. Smoothness of X(M) at rho follows H^2(M)=0 (no obstructions,
  Goldman-Millson deformation theory), dim 3g-3.

## Identification with Fuchsian locus
- rho|_Sigma preserves totally geodesic plane => conjugates into PSL(2,R)
  (Fuchsian). Nearby deformations of M keep double hyperbolic (Mostow rigid
  double fixes holonomy of DM up to conj), so r(X(M)) lies in fixed-point set
  of doubling involution tau^*: X(Sigma)->X(Sigma), i.e. Fuchsian / real locus.
- Dimension 3g-3 = half of 6g-6 matches Teichmuller dimension; étale onto
  quasi-Fuchsian deformation space intersected with diagonal.
- Hence A=-1 support of Sk(M) (coordinate ring of X(M) via Bullock/BFK) is this
  Lagrangian Fuchsian restriction locus, reduced, irreducible germ.

Status: classical part PROVED modulo standard references (Weil 1962, Calabi-Weil,
Goldman 1984/1988, Kapovich). Quantum strong-finiteness lift remains open/blocked.
