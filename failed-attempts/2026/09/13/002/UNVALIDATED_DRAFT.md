# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Pentas flower-center patch: exact frequency, Bragg intensity, and pure-point certificate
(Repaired submission — addresses all four auditor items; problem and object unchanged.)

## 1. Model-set data and literature anchor

Let ζ = e^{2πi/5}, τ = (1+√5)/2, ⋆: ζ ↦ ζ². The CPS used here is

- total space ℝ⁴ ≅ ℂ², lattice L = {(x, x^⋆) : x ∈ ℤ[ζ]} (Minkowski embedding,
  rank 4, basis eⱼ = (ζʲ, ζ^{2j}), j = 0,…,3);
- physical/internal spaces E∥ ≅ ℂ, E⊥ ≅ ℂ;
- window W ⊂ E⊥: regular decagon of edge 1, circumradius R = 1/(2 sin π/10)
  = τ, D₁₀-symmetric, |∂W| = 0.

**Literature anchor.** This is the Pentas (P3*) tiling of Fujita–Niizeki,
*Sci. Rep.* **15**:41523 (2025), "Structural insights into a rhombic Penrose
tiling variant abundant in five-petaled flower motifs": planar golden-mean
(τ-scaling) rhombic tiling with tenfold symmetry, thick/thin rhombi as in P3
but a distinct folded+straight dual grid, six P3* prototile types, Ammann-bar
decorability, and characteristic two-tiered five-petaled flower (decagonal)
motifs centered on S1 vertices covering 2/√5 ≈ 89.44% of the area. The paper's
cut-and-project data (5D hypercubic scheme, vertex classes p ∈ {0,…,4}, five
polygonal acceptance domains Wp): W0 is a regular decagon of radius 2 sin(π/5)
(= edge length of the P3 pentagonal AD); W2/W3 — the S1 (flower-center) domains
— are regular pentagons of circumradius 1/τ with vertex directions e_{2j}/τ;
total AD area 5 sin(2π/5)(1+τ²) (same as P3, hence same vertex/rhombus
densities); S1 vertices are τ²-times more frequent in P3* than in P3. The S1
environment (Fig. 2b, left) is exactly the two-tiered flower center: a
5-coordinated center whose first shell is 5 thick rhombi and whose second shell
is the 5-petal thin-rhomb arrangement — the patch F treated below.

**Lemma 1 (covolume).** Gⱼₖ = 2 (j=k), −1/2 (j≠k), i.e. G = (5/2)I − (1/2)J,
since cos(2πd/5)+cos(4πd/5) = −1/2 for d ≢ 0 mod 5. det G = 125/16,
covol(L) = 5√5/4.

**Lemma 2 (window area).** |W| = (5/2)√(5+2√5) ≈ 7.6942088429 (edge-1 decagon).

Λ = {π∥(x) : x ∈ L, π⊥(x) ∈ W} is a *regular* model set. Density:

> dens(Λ) = |W|/covol(L) = 4|W|/(5√5) = √(4 + 8/√5) = 2√(1 + 2/√5) ≈ 2.7527638409.

## 2. The two-tiered flower patch and dualization

The named patch F is the S1 vertex environment through its second coordination
shell (paper Fig. 2b, left): center 0, five thick rhombi with edges
(ζʲ, ζʲ⁺¹) and outer diagonal bⱼ = ζʲ + ζʲ⁺¹ (inner tier), plus five thin
rhombi capping the bⱼ edges (outer tier, petal tips). In ℤ[ζ]-coordinates the
forced vertex offsets are the 21 distinct points

> V = {0} ∪ {ζʲ : j ∈ ℤ₅} ∪ {bⱼ : j ∈ ℤ₅} ∪ {bⱼ − ζʲ⁺³, ζʲ − ζʲ⁺³ : j ∈ ℤ₅}.

This is precisely the vertex set of the S1 second-shell cluster: the 11 inner
offsets (center, first-shell ring, second-shell inner vertices bⱼ) fix the S
first shell, while the 10 petal-tip offsets fix the S1 (rather than S2)
thin-rhomb arrangement of the second shell — the distinction defining S1 vs S2
in the paper. Acceptance domain W_F = ⋂_{v∈V}(W − v^⋆), frequency
freq(F) = |W_F|/|W| (Schlottmann/Moody uniform distribution).

**Proposition (acceptance domain).** W_F is a regular pentagon with
circumradius r² = 25/2 − (11/2)√5 ≈ 0.2016261238, edge e² = 45 − 20√5
≈ 0.2786404500, vertices at angles {−54°, 18°, 90°, 162°, 234°}, area
|W_F| = (1/4)√(5(5+2√5))·e² ≈ 0.4793945971.

*Proof.* Finite intersection of convex decagons ⇒ convex polygon (script
`output/artifacts/compute_pentas.py`). {v^⋆} is C₅-permuted (j ↦ j+1) and
reflection-symmetric while W is D₁₀-invariant ⇒ W_F is D₅-invariant; a convex
D₅-symmetric pentagon is regular. The computed intersection has 5 vertices on a
circle of radius r at the stated angles with equal consecutive distances e
(relative spread 6×10⁻¹⁶); e = 2r sin 36° holds for the stated radicals. ∎

**Theorem A (exact frequency).** freq(F) = |W_F|/|W| = √5·e²/10
= (9√5 − 20)/2 ≈ 0.0623058987 (≈ 6.23%), i.e. ~1 flower center per 16 vertices.

*Proof.* Regular-pentagon area divided by |W| cancels the radical
√(5+2√5); substituting e² = 45 − 20√5 gives (9√5−20)/2, matching the computed
ratio to 5×10⁻¹⁶. ∎

## 2b. Reconciliation with the published 5D acceptance domains

The paper's S1 vertex-class frequency (both classes p = 2, 3) is
2|W2|/A_tot with |W2| = (5/2)r² sin 72°, r = 1/τ, A_tot = 5 sin(2π/5)(1+τ²):

> 2|W2|/A_tot = 1/(5τ²) = (3 − √5)/10 ≈ 0.0763932023.

This counts S1 *vertices* in the 5D vertex-class normalization (per total
vertex, summed over classes). Our freq(F) = (9√5−20)/2 ≈ 0.0623 counts the
full *second-shell flower patch* (S1 environment through petal tips) per
vertex of the effective single-window Minkowski CPS — a strictly finer event
than class membership (it additionally requires the 10 outer petal-tip
vertices), hence honestly smaller (ratio ≈ 0.8155). The two numbers are
compatible: both use regular-pentagon S1 domains, both lie in ℚ(√5), and the
paper's own cross-checks hold in our CPS — S1 is τ²-times more frequent in P3*
than P3, and the flower-decagon area cover is 2/√5. The single-decagon window
here is the Minkowski-effective total window |W| = (5/2)√(5+2√5); the 5D
scheme distributes the same total area 5 sin(2π/5)(1+τ²) over classes. No
adjustment of V is needed: V is exactly the S1 second-shell cluster of paper
Fig. 2b (S1 vs S2 differ only in the second-shell thin-rhomb arrangement,
which the 10 petal-tip offsets encode).

## 3. Pure-point diffraction certificate and Bragg intensity (repaired)

**Theorem B (pure-point certificate).** Λ regular ⇒ by
Hof–Schlottmann–Moody/Baake–Moody, autocorrelation and diffraction are pure
point, supported on π∥(L⁰), with A(k) = dens(Λ)·1̂_W(−k^⋆), I(k) = |A(k)|².

Dual data: L⁰ = B^{−T}ℤ⁴, covolume 4/(5√5); A∥ = M/25 with
M₀₀ = 10−2√5, M₀₁ = 5+√5, M₀₂ = 5−√5, M₀₃ = 5−3√5, M₁₁ = 10+2√5,
M₁₂ = 5+3√5, M₁₃ = 5−√5, M₂₂ = 10+2√5, M₂₃ = 5+√5, M₃₃ = 10−2√5.

**First 10-fold wavevector.** Shortest dual vector n = (2,0,−2,3) + D₁₀ orbit:

> |k₁|² = 26/5 − 58√5/25 = 2(65 − 29√5)/25 ≈ 0.0123222922,
> |k₁| ≈ 0.1110058206, |k₁^⋆| = |q₁| ≈ 3.2229920428 (|q₁|² = 52/5 − |k₁|²).

**Window Fourier transform (repaired routine).** With F(k) = ∫_W e^{−ik·x}dx,
the polygon FT is evaluated by exact fan-triangulation (analytic triangle
integrals with E(z) = (e^{−iz}−1)/(−iz) and the corrected small-arg branches
I = (1 − iu − e^{−iu})/u²), cross-validated by the divergence-theorem edge sum
F = Σ_e i(n_e·k)/|k|²·L_e·e^{−ik·m_e}·sinc(k·e_e/2) and by order-40
Gauss–Legendre quadrature. All three agree: F(0) = |W| = 7.6942088429 exactly
(fan and edge-sum to 1e-12, quadrature to 1e-6; 50-digit mpmath file
`output/artifacts/mp_evidence.txt` gives |F(0) − |W|| ≈ 2×10⁻⁵⁰). The previous
draft's edge-midpoint routine lacked the 1/2 factor and used the wrong edge
phase (e^{+ik·e} − 1)/(ik·e); it is replaced.

Crucially, the Hof formula evaluates 1̂_W at the **internal** coordinate:
evaluation at the physical |k₁| ≈ 0.111 (previous draft) was wrong. At
q₁ = k₁^⋆ (|q| ≈ 3.223), triple-validated:

> 1̂_W(−k₁^⋆): |F| ≈ 1.0099874707 (fan = edge-sum to 1e-12, quadrature to 1e-6;
>   50-digit value 1.00998747074592103944…; identical on all 10 rotated ring
>   peaks, spread 7×10⁻¹⁶; phase π, i.e. F real and negative by centrosymmetry).

**Theorem C (Bragg intensity, corrected).** At each first-ring peak,

> |A(k₁)| = dens(Λ)·|1̂_W(k₁^⋆)| ≈ 2.7527638409 × 1.0099874707 ≈ 2.7802569893,
> I(k₁) = |A(k₁)|² ≈ 7.7298289264 ≈ 1.0200746911·dens(Λ)²,

equal on all 10 peaks by D₁₀ symmetry of W. (The previous value 441.19 came
from evaluating the FT at the physical rather than the internal coordinate and
is withdrawn.)

## 4. Reproducibility

- `output/artifacts/compute_pentas.py` (repaired): ℤ[ζ] patch offsets,
  acceptance-domain intersection, lattice/dual data with corrected dens_exact
  = √(4+8/√5), triple FT (fan-tri exact / divergence edge-sum / quadrature)
  with F(0) = |W| assertions, internal-coordinate Bragg evaluation, 10-fold
  rotation checks. All assertions pass; printed outputs are quoted above.
- `output/artifacts/results.json`: updated certified numbers (I1 ≈ 7.7298).
- `output/artifacts/mp_evidence.txt`: 50-digit mpmath evidence (F(0), F(q₁),
  10 rotations identical to 50 digits, density, amplitude, intensity).

## 5. Scope and limitations

CPS normalization: edge-1 decagon, unit scatterers on vertices; rescaling or
chemical decoration multiplies I(k₁) by a form factor. freq(F) is per vertex
of the effective Minkowski CPS; the paper's (3−√5)/10 is the S1 vertex-class
share in the 5D class normalization — the two normalizations are reconciled in
§2b. The paper's hyperuniformity/order-metric and Ammann-bar analyses are
cited, not re-derived.
