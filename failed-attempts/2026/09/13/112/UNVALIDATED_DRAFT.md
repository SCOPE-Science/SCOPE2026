# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Laminate rigidity of hydrostatic zero-energy microstructures (S3)

## Claim
With α=1.25, K=SO(3)∪α·SO(3), p=2, there is **no** homogeneous
W^{1,2} gradient Young measure ν supported on K with barycenter
t₀I₃, t₀=(1+α)/2=9/8. Hence claim S3 holds in strong (vacuous) form:
every such ν is a finite-order laminate, since the admissible class is empty.

## Setup
Let ν be a homogeneous W^{1,2} gradient Young measure (Kinderlehrer–Pedregal)
with supp ν ⊆ K and barycenter
$$ \bar\nu = \int F\,d\nu(F) = t_0 I_3. $$
Write λ=ν(SO(3)), so ν(αSO(3))=1−λ. Define partial barycenters
$$ M_1 = \int_{SO(3)} F\,d\nu,\qquad M_2 = \int_{\alpha SO(3)} F\,d\nu, $$
so M₁+M₂=t₀I.

## Quasiaffine test function: cofactor
Each entry of cof is a homogeneous quadratic polynomial, hence satisfies
|cof_{ij}(F)| ≤ C|F|² and is admissible for p=2. Each entry is quasiaffine
(a null Lagrangian: both f and −f are quasiconvex), so the
Kinderlehrer–Pedregal Jensen inequality is an equality:
$$ \langle\nu,\mathrm{cof}\rangle = \mathrm{cof}(\bar\nu). $$
(On cof/Jensen for gradient Young measures see e.g. Kinderlehrer–Pedregal 1991;
Müller 1999; Pedregal's monograph; Fonseca–Müller.)
We deliberately use cof, not det: det has cubic growth and is inadmissible at p=2.

On the wells and at the barycenter:
- F∈SO(3): cof(F)=(det F)F^{−T}=F.
- F=αQ, Q∈SO(3): det F=α³, F^{−T}=α^{−1}Q, so cof(F)=α²Q=αF.
- cof(t₀I)=t₀²I.

Hence, with M₁,M₂ as above,
$$ M_1 + M_2 = t_0 I,\qquad M_1 + \alpha M_2 = t_0^2 I, $$
the second line being the matrix form of ⟨ν,cof⟩=cof(t₀I).

## Exact solution
Subtracting, (α−1)M₂=(t₀²−t₀)I. With t₀=(1+α)/2,
$$ t_0^2-t_0 = t_0(t_0-1) = \frac{1+\alpha}{2}\cdot\frac{\alpha-1}{2}
   = \frac{(\alpha-1)(\alpha+1)}{4}, $$
so
$$ M_2 = \frac{t_0}{2}I,\qquad M_1 = \frac{t_0}{2}I. $$
For α=5/4: t₀=9/8, M₁=M₂=(9/16)I, tr(M₁)=tr(M₂)=27/16.
(Verified exactly in Fractions; see artifacts.)
This step uses no assumption on λ; edge cases λ∈{0,1} are included
(they would force M₁=0 or M₂=0, contradicting Mᵢ=(t₀/2)I≠0).

## Trace contradiction
For R∈SO(3), tr(R)=1+2cosθ≤3. For F=αQ, tr(F)≤3α. Thus
$$ \mathrm{tr}(M_1)\le 3\lambda,\qquad \mathrm{tr}(M_2)\le 3\alpha(1-\lambda). $$
With tr(Mᵢ)=3t₀/2:
$$ \lambda \ge \frac{t_0}{2} = \frac{9}{16},\qquad
   1-\lambda \ge \frac{t_0}{2\alpha} = \frac{9}{20}. $$
Adding: 1=λ+(1−λ)≥81/80=1.0125>1, impossible.
Hence no such ν exists. S3 follows vacuously.

*Remark (generality).* The contradiction is (1+α)²>4α ⟺ (1−α)²>0, so the
argument works for every α≠1; only α=5/4 is claimed here.

*Remark (rank-one picture, supplementary).* Independently, finite-order
laminates on K are Diracs only: inside SO(3),
rank(R₁−R₂)∈{0,2,3} (R₁−R₂=R₁(I−R) with R∈SO(3), rank(I−R)∈{0,2});
between wells, σ_min(R−αQ)≥α−1=1/4>0 by the reverse triangle inequality,
so R−αQ is always invertible (rank 3). A 2000-sample numerical audit in
artifacts confirms min σ_min≈0.25. This is not needed for S3 given the
empty-class result, but confirms the rigidity picture.

## Verification
- `output/artifacts/verify_exact_arithmetic.py`: exact Fractions check of
  t₀, Mᵢ coefficients, traces, mass bounds, 81/80>1. Passes.
- `output/artifacts/verify_S3.py` + `s3_verification.json`: same exact
  checks plus random-rotation audit of no rank-one connections. Passes.

## Limitations / scope
- Specific to hydrostatic barycenter t₀I with α=1.25 and homogeneous
  W^{1,2} measures; inhomogeneous or x-dependent measures not addressed.
- Uses p=2 essentially (quadratic cof admissible; cubic det inadmissible).
- Vacuous truth: proves the class empty rather than exhibiting laminates.
- Relies on the standard Kinderlehrer–Pedregal characterization (Jensen
  equality for quasiaffine integrands); no new Young-measure theory claimed.
