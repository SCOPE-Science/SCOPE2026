# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Quantitative non-scarring on the shortest closed geodesic of the modular surface via Watson-Ichino transfer
- **Round:** 2026-09-07-first-light-01
- **Lane:** 459
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Quantum Chaos
- **Method:** semiclassical defect-measure invariance with Watson-Ichino triple-product period transfer and subconvex L-value comparison

## Problem

Rule out strong scarring of L^2-normalized Hecke-Maass cusp forms on the fixed shortest closed geodesic C5 of the modular surface X=PSL(2,Z)\H: prove a quantitative microlocal-mass cap <=1-delta on C5 via Watson-Ichino period transfer plus a cited subconvexity input, or isolate the thin-sequence period-ratio obstruction that stalls the arithmetic QUE attack in this frequency window.

## Attempted claim

Let X=PSL(2,Z)\H and C5 be the primitive closed geodesic of trace 3 (discriminant 5, length L0=2log((3+sqrt(5))/2)). There exist explicit r0=0.1 and delta=1/40 such that for every L^2-normalized Hecke-Maass cusp form phi_j with spectral parameter t_j large, the microlocal lift mass in the r0-tube satisfies mu_j(T_{r0}(C5)) <= 1-delta, equivalently the normalized geodesic restriction satisfies ||phi_j|_{C5}||_{L^2(C5)}^2 <= (1-delta')*L0^{-1}*vol-trace with delta'>0; the bound is obtained by the Watson-Ichino transfer plus a cited subconvexity exponent for the resulting triple-product L-value and defect-measure invariance under geodesic flow.

## Research outcome

Quantitative non-scarring on the systole C5 of the modular surface: mu_j(T_0.1(C5))<=1-1/40 for large t_j, unconditionally (QUE + explicit majorant, mean<=0.5535, gap>=0.4215) and effectively modulo cited subconvexity via a verified Watson-Ichino archimedean cap K_arch<=100 t^{-1}(log t)^3, with the HMN P=O(1) diagonal obstruction isolated in R_j.

## Why this attempt failed

Failed axes: originality, value.

originality: No prior source states the literal numbers (C5, r0=0.1, 1-1/40, K_arch<=100...), confirmed by admission triage and fetched abstracts (Watson 0810.0425 general triple identities; Bisain et al 2402.14050 general effective QUE from subconvexity; HMN 2207.14449 general subconvexity unless completely related; Soundararajan 0901.4060 qualitative QUE). Substantive comparison shows the headline is mechanically implied by known theorems, i.e. parameter substitution, not a new result: qualitative QUE implies <mu_j,Theta>->m(Theta) for EVERY fixed compactly supported continuous Theta, so for any fixed tube of Liouville fraction <0.975 (here 0.368) the cap <=0.975 for large j follows without any Watson-Ichino, archimedean, or subconvexity work. Fixing the general theorem to (C5,Theta0) and computing volume ratio to 50 digits adds no mathematical content beyond choosing a bump majorant. The archimedean cap is routine Stirling (A(t)~4pi/t via |Gamma(1/2+it)|^2=pi/cosh(pi t)); constant 100 is arbitrary slack over true ~12.57, not a new estimate. The HMN P=O(1) obstruction restates HMN's own hypothesis ('not completely related' / conductor-dropping fails in diagonal QUE-like case pi2~tilde pi1), explicitly discussed in HMN. The defined ratio R_j is a tautological rearrangement, not a proved sharpness lemma. A timestamp or failed arXiv search does not establish priority; substantive novelty is absent. value: Headline judged separately from unfinished survey per narrow-datum policy, but fails the policy's three conditions for a retrievable exact invariant. (i) Object C5/r0 are natural, but invariant 1-1/40=0.975 is not motivated before computation: true QUE limit is ~0.368 (tube fraction), so 0.975 is an extremely weak, arbitrary threshold (any number in (0.5535,1) would work identically; 1/40 has no extremal, rate, or defect-measure significance). (ii) Value is mechanically implied: qualitative QUE already gives the far stronger limit 0.5535, so a future researcher needing tube mass would retrieve QUE + volume, not this cap. (iii) No precise fact is needed later: unconditional threshold is non-effective (no j0), effective T* is conditional on open H with vacuous schema values (1e17 to 1e235) and no concrete exponent imported (HMN supplies no saving, admitted), so nothing can be imported by a QUE-rate/entropy/restriction argument beyond what Bisain/Watson already provide generally. K_arch constant 100 is slack certification of an arbitrary majorization, not a sharp or reusable bridge — certification alone does not rescue an unexplained number. Result is textbook restatement (qualitative QUE applied to a bump) + mere parameter substitution (general effective QUE specialized to Theta0) + tiny unmotivated gain (weak cap far above true mass), explicitly rejectable even if correct and new. No ADMISSION_DEFECT reopening needed; value fails on ordinary standard with no presumption.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Unconditional threshold is non-effective (qualitative QUE input). Effective threshold T* is conditional on the open diagonal subconvexity hypotheses H(delta_sub,A); Hu-Michel-Nelson Thm 1.3 does not supply H (P=O(1) conductor-dropping failure documented, not a proof gap). The literal per-j central-slice restriction bound ||phi_j|_C5||^2<=(1-delta')*uniform-trace for every large j is NOT claimed; only the tube cap plus averaged/coarea and subsequential-limit consequences. Archimedean enclosure i…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
