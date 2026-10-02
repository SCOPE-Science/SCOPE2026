# Zoll–Crofton characterization in the projective RP^2 class: the (⇒) direction is false

## Context

Let F be a smooth reversible projective Finsler metric on RP^2: all projective
lines are unparametrized geodesics. Write Λ(F) for the common prime length of
projective-line closed geodesics when all such lengths coincide, ω_F for the
Gelfand double-fibration Crofton density on the dual RP^{2*}, and A(F) for
Holmes–Thompson area. The target two-sided claim asks whether: all prime
projective-line geodesics share one common length Λ if and only if ω_F is a
constant positive multiple of the round elliptic Crofton density (equivalently
the systolic ratio A/Λ^2 equals the constant-density value 2/π).

## Definitions

Work on the double cover p:S^2→RP^2 with antipodal involution a(x)=−x. A
reversible projective Finsler metric on RP^2 is an a-invariant reversible
smooth strongly convex 1-homogeneous F:TS^2→[0,∞) whose unparametrized
geodesics include all great circles. Each RP^2 projective line lifts to a
great circle; we normalize so S^2 great circles have length 8π and RP^2 prime
lines Λ=4π. A Crofton density is a smooth positive antipodally-even density
μ=f dλ on the pole sphere L≅S^2 (dλ = rotation-invariant area). Holmes–
Thompson area is A=∫|B*_x|dx with |B*_x|=½∫ρ^2dθ, ρ=1/F*, computed from the
exact fiber below as numerical evidence only.

## Result

The (⇒) direction is FALSE. With e=3/10 and even harmonic
f(ξ)=1+e(ξ_3^2−1/3) ∈ [0.9,1.2], define
F(x,v)=∫_{ξ·x=0}|ξ·v| f(ξ) dλ(ξ).
Then F is a smooth reversible projective Finsler metric on RP^2; every
projective-line geodesic is closed with common prime length Λ=4π (great
circles 8π), while ω_F=f dλ is smooth, positive and nonconstant, hence not a
constant multiple of the round density. The (⇐) direction is TRUE: constant
positive Crofton multiple implies equal line lengths by the Crofton count.

## Proof / evidence

Exact fiber formula: with x at colatitude β and v=cosα e_β+sinα e_φ,
m(β,α)=∫_0^{2π}|cos(t−α)|(1+e(sin^2β cos^2t−1/3))dt
=A(β)+B(β)cos2α, A(β)=4(1−e/3)+2e sin^2β, B(β)=(2e/3)sin^2β,
since K(α)=∫|cos(t−α)|cos^2t dt=2+(2/3)cos2α (J=∫|cos u|cos2u du=4/3).
Cross-checked against kink-split Gauss–Legendre quadrature to 1.6e−14.
Smoothness, reversibility, antipodal invariance follow since only sin^2β and
2α appear. Strong convexity: for r=1/m,
(r+r″)m^3=A^2+6ABc+8B^2−3B^2c^2=:N(c), c=cos2α, concave in c, minimum
N(−1)=(A−B)(A−5B)≥12.8, numeric min(r+r″)=0.20>0. Projectivity is Busemann's
cosine-transform theorem; uniqueness of the even density is Funk-transform
injectivity on even functions. Zoll property: Crofton length is proportional
to total mass μ(L) independent of the circle since each RP^2 line meets the
pencil once a.e.; anchored by equator L=2π·4=8π exactly and meridian/tilted
circles 8π to 1e−9. Nonconstancy of f over [0.9,1.2] is analytic. (⇐): if
ω_F=c ω_round, L(γ) is line-independent by the same count. HT integration
gives A(RP^2)≈100.43 vs 32π≈100.53 (ratio ≈0.63595 vs 2/π≈0.63662) as
computed evidence only with ~0.15 grid spread; the disproof does not depend on it.

## Limitations

HT area/systolic numbers are grid-dependent computed evidence, not a proved
inequality. Projectivity and density uniqueness invoke classical Busemann /
Pogorelov / Funk results. The stated Crofton prefactor in DRAFT §3 should be
read as proportionality (normalization-consistent constant); circle-
independence is unaffected and anchored exactly.

## Reproducibility

Run output/artifacts/check_zoll_crofton.py (numpy only): prints PASS for C1
Fourier constants, C2 exact-m cross-check, C3a–c circle lengths, C4 convexity,
C5 f range, then C6 HT values at three resolutions; ALL: OK.

## References

Busemann–Pogorelov solution of Hilbert's fourth problem; Pogorelov smooth
projective correspondence; Álvarez Paiva–Fernandes Crofton formulas in
projective Finsler spaces; Álvarez Paiva–Barbosa Gomes arXiv:1809.02783;
Bryant math/0107228; Schneider Crofton measures in projective Finsler spaces;
Bernig valuations with Crofton formula.
