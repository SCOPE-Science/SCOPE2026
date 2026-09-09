# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Fixed-twist hypocoercivity no-go at Sobolev cell σ*=10 for the free-transport principal part of Vlasov–Poisson

## 1. Setup and claim

Work in 1D, periodic in x, on T_x × R_v. Let

T = v ∂_x

be the free-transport operator (principal part of Vlasov linearized about a
homogeneous Maxwellian). Use Fourier conventions

ĥ(k,η) = ∫_{T×R} h(x,v) e^{-ikx-iηv} dx dv, k ∈ Z, η ∈ R,

and the homogeneous Sobolev weight at fixed mode k=1 with exponent σ*=10:

W(η) = (1 + 1 + η²)^10 = (2 + η²)^10.

Consider the fixed-coefficient Villani-type twisted energy on that mode,

E_{a,b,c}(t) = (1/2) ∫_R W(η) Q(η) |ĥ(t,1,η)|² dη,
Q(η) = (1+a) + 2bη + cη²,

with real constants (a,b,c) independent of t, k, η (the "one fixed cell"
audit). Admissibility (norm-equivalence to the base H^10 norm on this mode)
means Q is uniformly positive: ∃κ>0 with Q(η) ≥ κ(1+η²) up to constants;
equivalently (Lemma 2) c > 0 and (1+a)c > b².

**Theorem (fixed-twist no-go, σ*=10).**
(a) Admissibility holds iff c>0 and (1+a)c−b²>0; otherwise E_{a,b,c} is not
equivalent to the H^10 norm on mode k=1 (Q attains negative values).
(b) For every admissible fixed triple (a,b,c), the free-transport flow does
not satisfy any uniform decay/monotonicity estimate dE/dt + λE ≤ 0 with
λ ≥ 0 along all solutions. Explicitly, on the Schwartz single-mode Gaussian
datum ĥ(0,1,η)=e^{−η²/2} (all other k zero), E(t) is an explicit degree-22
polynomial with positive leading coefficient c√π/2, hence E(t)→+∞.
(c) Filamentation growth certificate: on the same datum the untwisted
H^10-mode energy N(t)²=(1/2)∫W|ĥ|² is an explicit degree-20 polynomial with

N(3)²/N(0)² = 3405966412872299/5465416811 ≈ 6.23×10⁵ > 1000.

In particular E_{a,b,c}(3)/E_{a,b,c}(0) > 10² for each of 36 grid admissible
triples (minimal grid value 29059926375156783/59594395469 ≈ 4.88×10⁵),
and unboundedness holds for every admissible triple via (b), not only the grid.

**Transfer remark (not claimed as proved).** Linearized Vlasov–Poisson equals
T plus an electric-field coupling term that is smoothing/decaying in the
damping regime. This note proves the obstruction only for the principal part
T; it explains why a verbatim fixed Villani twist cannot close the full
linearized problem, and conditions any full-VP extension on controlling that
coupling. No nonlinear bootstrap, no Gevrey claim, and no echo-resonance
computation beyond filamentation is claimed here.

## 2. Proofs

**Lemma 1 (commutator and filamentation).** With D_x=∂_x, D_v=∂_v,
[T,D_v] = −D_x, i.e. [v∂_x,∂_v]=−∂_x. The transport equation ∂_t h+Th=0 has
Fourier solution ĥ(t,k,η)=ĥ(0,k,η+kt).

*Proof.* Direct differentiation; characteristics x−vt=const give the shift in
the dual variable. ∎

**Lemma 2 (admissibility).** Q(η)=(1+a)+2bη+cη² is strictly positive ∀η iff
c>0 and (1+a)c−b²>0.

*Proof.* Quadratic positivity criterion: leading coefficient positive and
discriminant 4b²−4(1+a)c<0. If c≤0, Q→−∞ or is affine non-constant; if
discriminant ≥0, Q has real roots. In either failure case Q takes negative
values so E is not norm-equivalent (it is negative on data concentrating near
such η). ∎

**Proof of (b).** Take ĥ(0,1,η)=e^{−η²/2}, so by Lemma 1
|ĥ(t,1,η)|²=e^{−(η+t)²}. Then

E(t) = (1/2) ∫_R (2+η²)^10 Q(η) e^{−(η+t)²} dη.

Substitute u=η+t: E(t)=(1/2)∫(2+(u−t)²)^10 Q(u−t)e^{−u²}du. Since σ*=10 is an
integer, (2+(u−t)²)^10 Q(u−t) is a polynomial in (u,t) of u-degree 22 and
t-degree 22. Termwise integration uses Gaussian moments
μ_p=∫u^p e^{−u²}du with μ_{2q}=√π(2q−1)!!/2^q and μ_odd=0, giving an exact
degree-22 polynomial in t (odd moments drop). The top term comes from
η^20·cη²=cη^22=c(u−t)^22, contributing c·(1/2)·μ_0·t^22=c√π/2·t^22. For
admissible triples c>0 (Lemma 2), so E(t)→+∞ polynomially and E(0)>0 finite
(Q>0 continuous, Gaussian weight). Any estimate dE/dt+λE≤0 with λ≥0 would
force E(t)≤E(0) (bounded), contradiction. ∎

**Proof of (c).** Same datum with Q≡1 gives N(t)², a degree-20 polynomial via
the same moment expansion. Exact rational evaluation (√π cancels in the
ratio) gives N(3)²/N(0)²=3405966412872299/5465416811≈623185. The twisted
ratios are likewise exact rationals; see verifier output. ∎

## 3. Reproduction

`output/artifacts/verify.py` (stdlib only, `Fraction` exact arithmetic,
Gaussian moments via double factorials) recomputes all ratios exactly:

- base-norm ratio ≈ 6.23×10⁵ (asserted >1000);
- all 36 admissible grid triples have E(3)/E(0) > 100 (in fact ≥ 4.8×10⁵);
- leading-coefficient identity e_22=c/2 asserted exactly per triple.

Run: `python3 output/artifacts/verify.py` → `VERIFY_OK`.

## 4. Limitations and scope

1. Principal-part only: proved for free transport T, not the full linearized
   Vlasov–Poisson operator with self-consistent E-field.
2. Fixed-coefficient twists only: time-dependent or η-dependent multipliers
   (gliding regularity) are not ruled out — indeed they are the standard way
   around filamentation.
3. One cell: σ*=10, mode k=1, Gaussian datum; no uniform-in-k or
   nonlinear claim.
4. No originality claim over hypocoercivity or Landau damping generally; the
   contribution is the explicit fixed-cell certificate pairing the
   admissibility discriminant with the degree-22 growth polynomial,
   checkable from definitions.
