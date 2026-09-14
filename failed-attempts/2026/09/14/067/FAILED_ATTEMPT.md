# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Explicit spectral-data reconstruction for closed constrained Willmore tori
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20046
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Differential Geometry
- **Method:** integrable-systems spectral-curve and loop-group analysis

## Problem

Let Σ be a smooth compact spectral curve of a constrained Willmore immersion of a closed torus f:T²→S³, equipped with its marked points over 0,∞, the quaternionic and holomorphic involutions, and a real two-dimensional Jacobian flow Ψ:T²→Jac(Σ) satisfying the spectral reality and closing conditions. Give a complete, explicit loop-group/Baker–Akhiezer reconstruction theorem: characterize necessary and sufficient spectral data for which the reconstructed twistor evaluation closes to a smooth immersion T²→S³, and prove that the resulting immersion is unique up to Möbius transformations (including the singular/reducible limiting cases).

## Attempted claim

Let Σ be a smooth compact spectral curve of a constrained Willmore immersion of a closed torus f:T²→S³, equipped with its marked points over 0,∞, the quaternionic and holomorphic involutions, and a real two-dimensional Jacobian flow Ψ:T²→Jac(Σ) satisfying the spectral reality and closing conditions. Give a complete, explicit loop-group/Baker–Akhiezer reconstruction theorem: characterize necessary and sufficient spectral data for which the reconstructed twistor evaluation closes to a smooth immersion T²→S³, and prove that the resulting immersion is unique up to Möbius transformations (including the singular/reducible limiting cases).

## Research outcome

Complete explicit spectral-data reconstruction theorem for closed constrained Willmore tori proved with closing characterization, uniqueness, limits, and computation.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: TARGET route: main theorem claims unconditional necessary+suff closing, non-speciality iff immersion, unconditional Moebius uniqueness, and continuous admissible nodal/reducible limits. Proof is citation assembly plus two toy scripts. Unconditional uniqueness is false as written: Heller (1212.2068 Sec.3.1, Def. simple) and BLPP prove F/f is in general not unique from (Sigma,Z); uniqueness holds only under simple / h0=4 / p=g condition, with dressing counterexamples preserving spectral curve. Closing (i)-(iii) omits asymptotics/nilpotent residue and pole data required in Heydel admissible (i)-(iv), so sufficiency unproved. Non-speciality equivalence and singular-limit continuity are asserted without computation. Scripts verify only abstract Laurent algebra c_2..c_-2 and a scalar genus-0 exponential toy, not theta/DPW/higher-genus closure. originality: Fused search over literal, equivalent (finite-type constrained-harmonic Gauss map, eigenline Jacobian flow, quaternionic/DPW/Sym-point), and dominance (Bohle finite-type, Hitchin harmonic, BLPP conformal, compactified-Jacobian singular, DPW) candidates shows the headline is substantively covered. BLPP Thm 4.2 / Heller Thm 6 give twistor reconstruction from (Sigma,Z); Heydel thesis main theorem gives Sym-Bobenko Fx2^-1 Fx1 reconstruction from admissible rank-2 families with intrinsic/extrinsic closing; Bohle gives associated family and finite-type dichotomy; Dorfmeister-Wang gives DPW/Iwasawa loop splitting. Assembly with Krichever theta and torsion-free-sheaf limits adds no new boundary, invariant, or counterexample; unconditional uniqueness is the only novelty and it is false. value: No independently retrievable advance under STANDARD: no new theorem, lemma, counterexample shifting a boundary, census, cutoff, exact invariant of a motivated natural object, or downstream use. The text synthesizes Bohle/BLPP/Heller/Heydel/Hitchin-Krichever-DPW machinery into one statement; higher-genus existence is cited and genus-0 script is a tuned illustration. Certification (Laurent recomposition, scalar closing toy) strengthens evidence properties but does not create value. A survey restatement, even if corrected to conditional uniqueness, would remain textbook repackaging.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The theorem synthesizes established integrable-systems machinery (quaternionic Willmore theory, Hitchin spectral curves, Krichever construction, DPW/Iwasawa splitting, Sym-point closing, compactified Jacobians) into one closed statement; the originality lies in the assembly and the sharp necessary-and-sufficient formulation with admissible limits, not in the individual classical tools. Higher-genus existence is cited from Schmidt/Heller-Ndiaye-Schmitt/Bohle theory rather than re-proved, and the…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
