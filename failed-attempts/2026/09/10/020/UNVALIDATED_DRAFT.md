# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Low-index second-area-gap rigidity in S⁴: index ≤ 4 and area below Clifford forces the equator

## Theorem (target claim)
Let Σ³ be a closed embedded minimal hypersurface in the round unit
4-sphere S⁴(1). If Morse index ind(Σ) ≤ 4 and
area(Σ) < 16π²/(3√3), then Σ is isometric to the equatorial 3-sphere
(hence area(Σ) = 2π² and ind(Σ) = 1).

## Remarks on strength and attribution
1. The proof below establishes a **stronger index-only** statement:
   every non-equatorial closed embedded minimal hypersurface Σ³ ⊂ S⁴(1)
   has ind(Σ) ≥ 6 > 4. The area hypothesis is therefore redundant but
   consistent: the equator has area 2π² ≈ 19.739 < 30.391 ≈ 16π²/(3√3),
   so the full claim as written follows.
2. **Prior-art honesty note.** The index-gap core (non-equatorial ⇒
   index ≥ 6) is the classical Simons/El Soufi gap: A. El Soufi,
   *Applications harmoniques…*, Compositio 85 (1993), Thm 2.2
   (ambient Sⁿ ⇒ variational index 1 or ≥ n+2; i.e. ≥ 6 for n = 4).
   Survey restatements (e.g. Colberg et al.) phrase it as ≥ n+3 in
   hypersurface-dimension notation. The proof here is a self-contained
   reproduction of that gap specialised to Σ³ ⊂ S⁴(1), plus the explicit
   area-threshold packaging (equator 2π² vs Clifford 16π²/(3√3)) and a
   machine-checked reference-value certificate
   (`output/artifacts/verify_references.py`). The area–index window
   formulation is not claimed as a new method; the novelty, if any, is
   only the explicit window. Nothing below overclaims a new classification
   theorem beyond this fragment.

## Preliminaries and conventions
- Δ = trace Hess (non-positive spectrum); Jacobi operator
  J = −Δ − 3 − |A|²; Q(f) = ∫_Σ fJf = ∫(|∇f|² − (3+|A|²)f²).
  ind(Σ) = number of negative eigenvalues of J counted with multiplicity
  (finite by ellipticity; Σ closed).
- Embedded closed hypersurface in S⁴ is two-sided (hence orientable with
  globally defined unit normal; J is well defined). Proof: by Alexander
  duality with ℤ/2 coefficients, for connected closed Σ³ ⊂ S⁴,
  H̃₀(S⁴∖Σ; ℤ/2) ≅ H̃³(Σ; ℤ/2) ≅ ℤ/2 (top class mod 2 exists regardless
  of orientability), so the complement has exactly two components
  U₁, U₂. Let N be a tubular neighbourhood (normal disc bundle).
  N meets both U₁ and U₂, so N∖Σ = (N∩U₁) ∪ (N∩U₂) is disconnected.
  But N∖Σ deformation-retracts onto the unit normal 0-sphere bundle;
  a real line bundle whose 0-sphere bundle is disconnected is trivial.
  Hence the normal bundle is trivial (global unit normal exists) and,
  since S⁴ is orientable, Σ is orientable. (This covers arbitrary
  topology — e.g. Clifford S²×S¹ — not just spheres, where bare
  Jordan–Brouwer would be insufficient.)
- By Frankel's theorem (positive Ricci curvature), any two closed minimal
  hypersurfaces in S⁴ intersect; hence an embedded closed Σ is connected
  (its components would otherwise be disjoint closed minimal hypersurfaces).
  Connectedness is used for unique continuation below.
- Takahashi (1966): for Σ³ ⊂ S⁴(1) minimal, position components satisfy
  Δl_v + 3l_v = 0 where l_v(x) = ⟨x, v⟩, v ∈ ℝ⁵. Derivation: write
  x: Σ → ℝ⁵ for the inclusion; Δ_Σx = (Δ_Σx)^⊤ + (Δ_Σx)^⊥. The tangential
  part is 3H⃗_{S⁴} = 0 by minimality in S⁴, and the ℝ⁵-normal part is
  −3x (mean curvature vector of S⁴ ⊂ ℝ⁵ is −x per unit volume, times
  dim Σ = 3). Projecting onto fixed v gives Δl_v = −3l_v.
- Spectrum of −Δ on round S³(1): k(k+2), k = 0,1,2,…, mult (k+1)².
- Aronszajn unique continuation: a solution of (Δ+3)u = 0 on connected Σ
  vanishing on a nonempty open set vanishes identically.

## Reference values (machine-checked)
- Vol(S³(1)) = 2π² ≈ 19.7392088022.
- Clifford T = S¹(1/√3) × S²(√(2/3)): minimal since principal curvatures
  k₁ = −√2 (mult 1), k₂ = +1/√2 (mult 2) sum to zero; |A|² = 2+2·(1/2) = 3;
  area = (2π/√3)(4π·2/3) = 16π²/(3√3) ≈ 30.3905000414 > 2π²
  (ratio 8/(3√3) ≈ 1.5396).
- Equator Jacobi spectrum: J = −Δ − 3 gives −3 (mult 1), 0 (mult 4),
  ≥ 5 after ⇒ ind = 1.
- Clifford Jacobi spectrum: J = −Δ − 6 on the product; −Δ eigenvalues
  3m² + (3/2)ℓ(ℓ+1) give negative modes (m,ℓ) = (0,0)[−6,mult 1],
  (0,1)[−3,mult 3], (1,0)[−3,mult 2] ⇒ ind = 6 > 4, nullity 6.
- All identities above are replayed by `verify_references.py` (E1–E6).

## Lemma 1 (test-space identity)
For constants a ∈ ℝ and l_v = ⟨x, v⟩,
  Q(a + l_v) = −3a²Vol(Σ) − ∫_Σ |A|²(a + l_v)².
*Proof.* ∇(a+l_v) = ∇l_v; ∫|∇l_v|² = −∫l_vΔl_v = 3∫l_v² (closed, parts).
∫l_v = −(1/3)∫Δl_v = 0, so ∫(a+l_v)² = a²Vol + ∫l_v². Then
Q = 3∫l_v² − 3(a²Vol + ∫l_v²) − ∫|A|²(a+l_v)². ∎

## Lemma 2 (linear independence unless equator)
If Σ is not the equator, the six functions {1, l₁,…,l₅} are linearly
independent (l_i = ⟨x, e_i⟩).
*Proof.* A dependence is a pair (a,v) ≠ (0,0) with f := a + l_v ≡ 0,
where l_v = Σ v_i l_i. Applying Δ and Takahashi,
0 = Δf = Δl_v = −3l_v, so l_v ≡ 0 and then a ≡ 0; hence v ≠ 0 and
⟨x(p), v⟩ = 0 for all p ∈ Σ. Thus the image lies in the hyperplane
section E = S⁴ ∩ v^⊥ (a great S³). The corestricted inclusion Σ → E is
an immersion of equal dimension 3, hence open; Σ compact ⇒ image closed
in connected E ⇒ surjective covering; the inclusion Σ ↪ S⁴ is injective
(embedded) ⇒ equality Σ = E as sets. Contrapositively, a
non-equatorial Σ has independent {1, l_i}. ∎
Totally geodesic ⇒ equator is also seen directly: through any p₀, Σ
contains every great circle tangent at p₀ (geodesics coincide), whose
union is the great S³ spanned by {x(p₀), T_{p₀}Σ}; closed embedded of the
same dimension ⇒ equality. In detail: let E = S⁴ ∩ span{p₀, V} with
V = T_{p₀}Σ (a great S³). Every q ∈ E lies on some S⁴-geodesic from p₀
with initial velocity in V (minimizing geodesic, or any great circle
through the antipode), and each such geodesic is a geodesic of the totally
geodesic Σ, so q ∈ Σ: E ⊂ Σ. E is compact (closed in Σ) and, as a
3-dimensional submanifold contained in the embedded 3-manifold Σ, open in
Σ by invariance of domain; Σ connected ⇒ E = Σ.

## Lemma 3 (negativity)
If Σ is closed embedded minimal and not totally geodesic (equivalently,
not the equator), Q is strictly negative definite on
E = span{1, l₁,…,l₅} (dim 6 by Lemma 2), so ind(Σ) ≥ 6.
*Proof.* Let 0 ≠ (a,v), f = a + l_v. By Lemma 1,
Q(f) = −3a²Vol − ∫|A|²f². If a ≠ 0 the first term is already < 0 and the
second ≤ 0. If a = 0 (v ≠ 0), Q = −∫|A|²l_v². Since Σ is not totally
geodesic, |A|² ≥ c > 0 on some small ball B. If l_v ≡ 0 on B,
Aronszajn ⇒ l_v ≡ 0 on connected Σ ⇒ equator by Lemma 2, contradiction.
Hence l_v ≠ 0 on a smaller open B′ ⊂ B and ∫_B′|A|²l_v² > 0 ⇒ Q < 0.
The globally-dependent case f ≡ 0 with (a,v) ≠ 0 likewise forces the
equator (Lemma 2 proof), excluded here. ∎

## Proof of theorem
Let Σ satisfy the hypotheses. If Σ were not the equator, Lemma 3 gives
ind(Σ) ≥ 6, contradicting ind ≤ 4 (this already excludes the Clifford
hypersurface, whose index is exactly 6, and every exotic). Hence Σ is the
equator: totally geodesic great S³, area 2π² (< 16π²/(3√3) as required)
and index 1 (equator spectrum above). In particular Σ is isometric to the
round S³. ∎

## Stress-test checklist
- Sign conventions: Δ ≤ 0, −Δl_v = 3l_v corroborated by symmetric
  quadrature (E5: ⟨|∇l|²⟩ = 3⟨l²⟩, ⟨l²⟩ = 1/4, ⟨l⟩ = 0).
- Disconnected Σ ruled out by Frankel (needed for UC connectedness).
- One-sidedness ruled out by Jordan–Brouwer (embedded in S⁴ ⇒ two-sided).
- a ≠ 0 branch needs no UC; a = 0 branch uses only eigenfunction UC, not
  analyticity of |A|.
- Totally-geodesic ⇒ equator uses only great-circle containment +
  dimension; no curvature pinching assumed.
- Index conventions cross-checked both ways (hypersurface-dim n+3 = 6 and
  ambient-dim n+2 = 6 for n = 3/4); no off-by-one: explicit spectra give
  1 (equator) and 6 (Clifford) directly.
- Area inequality strict and with margin: 2π²/Clifford ≈ 0.6495.

## References
- J. Simons, Minimal varieties in Riemannian manifolds, Ann. Math. 1968
  (stability form; Lemma 5.1.4 negative space).
- T. Takahashi, Minimal immersions of Riemannian manifolds, J. Math. Soc.
  Japan 1966 (Δx = −nx).
- H. B. Lawson, Local rigidity theorems…, Ann. Math. 1969;
  Chern–do Carmo–Kobayashi 1970 (|A|² ≡ 3 ⇒ Clifford).
- A. El Soufi, Compositio 85 (1993), Thm 2.2 (index 1 or ≥ n+2).
- F. Frankel, On the fundamental group of a compact minimal submanifold,
  Ann. Math. 1966 (connectedness); Aronszajn 1957 (UC).
- Perdomo 2001/2019; Chen–Wang 2405.10843; Carlotto–Schulz–Wiygul
  2407.11147; Kapouleas–Zou 2405.18283 (context; doublings have area
  ≈ 39.48 − δ, above the 30.39 threshold, hence no conflict).
