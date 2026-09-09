# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A modulation-spectral rate barrier for radial type-II blowup in 3D energy-critical focusing NLS
- **Round:** 2026-09-07-first-light-01
- **Lane:** 364
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Nonlinear Dispersive Equations
- **Method:** soliton modulation analysis with linearized-operator spectral coercivity transferred from parabolic stability theory

## Problem

Consider the 3D radial energy-critical focusing NLS i u_t + Delta u + |u|^4 u = 0. For finite-time type-II blowup solutions concentrating as a rescaled ground state W_{lambda(t)} plus remainder, derive from transferred linearized coercivity a finite-dimensional modulation ODE for lambda(t) and prove either a new quantized rate barrier or a certified spectral/virial obstruction excluding one rate regime.

## Attempted claim

For 3D radial type-II blowup with ansatz u(t) = W_{lambda(t)} + eps under explicit smallness and orthogonality hypotheses, the heat-transferred coercivity plus a localized virial identity imply an explicit differential inequality for lambda(t) that excludes a concrete previously-admissible rate regime (e.g. concentration exponents below an explicit quantized threshold), yielding a new type-II rate barrier.

## Research outcome

Consolidated interrupted lane-364 into a CLAIMED fallback fragment: proved exact modulation-profile calculus with explicit constants and certified kernel/virial numbers for radial 3D energy-critical NLS, plus a conditional localized virial inequality whose coercivity input is stated as an open hypothesis. Full quantized rate barrier remains open; no overclaim.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Unconditional elementary profile integrals (I=3√3π²/4, L=15√3π²/64, det=135π⁴/256, D(t)=5(t²-1)/2(1+t²)^{7/2}, ∫t²D²=75π/2048, ∫t⁴D²=25π/2048, ||ΔΛW||²=|||y|ΔΛW||²=225√3π²/512, E(W)=√3π²/4, C_S=I^{-1/6}, (W,ΛW)_Ḣ¹=0, L_+ΛW=0 ⇒ Q(ΛW)=0) were independently recomputed at 30-digit precision with mpmath and all agree exactly; W solves -ΔW-W⁵=0 checked pointwise. However the headline fallback claim — a 'proved modulation ODE reduction with explicit error bounds' plus a 'virial inequality with every coefficient traced' — is not proved. Lemma 2 asserts (J+E)(λ̇/λ,γ̇)=F with ||E||≤½min(I,L) when η≤1/24 via 'sharp Sobolev' but gives no derivation of E, no operator-norm estimate, and no F formula; the threshold 1/24 is admitted convenient not derived. Section 7 is labeled 'proof sketch': Q(χ_R^{1/2}ε)≥(c0/2)||ε||²-CR^{-2}||ε||², Err_mod, Err_cubic bounds and C2(R,Qw) are stated with O(·) and unspecified C, unquantified R≫1, no cutoff commutator proof, no Cauchy-Schwarz absorption shown, and C2 never given numerically. verify.py does NOT certify the analysis: it checks algebraic tautologies (0.5-3/6==0, L-L==0, CS⁶I==1 by definition, Qw==itself) not integral evaluations or PDE estimates. The conditional inequality is therefore not established even conditionally on (H4); only the elementary integrals are proved. Honest labeling of (H4) as assumed and barrier as open does not convert the sketch of Lemma 2/§7 into a proved explicit reduction. originality: Substantive comparison, not timestamp: (1) Kenig-Merle math/0610266 gives radial threshold scattering/blow-up, no rate quantization — DRAFT correctly does not reproduce it. (2) Duyckaerts-Kenig-Merle 0910.2594 gives wave-equation type-II profile universality, not NLS rate barrier. (3) Merle-Raphael-Rodnianski 1407.1415 constructs quantized type-II rates for supercritical NLS d≥11 (existence, disjoint regime), not a 3D critical exclusion — DRAFT correctly claims consistency. But the actually-proved content — explicit W norms, best Sobolev constant C_S=I^{-1/6}, E(W), Gram determinant from L²-critical scaling invariance, L_+ΛW=0 and Q(ΛW)=0, and the rational-function virial weight — is classical or mechanically implied by the explicit Aubin-Talenti formula W=(1+r²/3)^{-1/2} via Beta integrals; any modulation paper computes these. The claimed novel step — heat-transferred coercivity (H4) with explicit c0, a certified gap/resonance, or a rate-regime exclusion — is explicitly assumed/open, and DRAFT §9 admits 'no new spectral fact about L_+ beyond classical L_+ΛW=0'. A failed-search/timestamp argument cannot make direct integration of an explicit profile a new inequality/certificate. Hence no new theorem, lemma, or certificate beyond textbook/mechanical consequences. value: Headline target (quantized 3D radial critical NLS rate barrier or certified spectral/virial obstruction) is admitted open: 'No new quantized rate barrier, no exclusion of any rate regime, and no proof of (H4)'. Predefined fallbacks…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Transferred linearized coercivity (H4) with explicit c0 is assumed, not proved -- this is the load-bearing gap. No quantized rate barrier closed; no rate regime excluded (fallback (a)+(b) fragment only). Radial class with two orthogonality conditions only; smallness eta0=1/24 is convenient, not optimal; nonradial/phase/translation directions untreated.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
