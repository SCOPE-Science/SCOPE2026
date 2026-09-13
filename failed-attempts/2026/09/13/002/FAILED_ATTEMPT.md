# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Pentas flower-center frequency and intensity
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1450
- **Disposition:** AUDIT_2_REJECT
- **Domain:** 2D planar model-set tiling
- **Method:** dualization window-area plus window-Fourier

## Problem

Let T be the Pentas rhombic quasiperiodic tiling of Fujita-Niizeki 2025 with golden-mean scaling, tenfold symmetry, and planar cut-and-project polygonal windows, distinguished from the rhombic Penrose tiling by its folded/straight dual grid and its two-tiered five-petaled flower motifs. Determine with proof the exact frequency of the two-tiered five-petaled flower-center patch and the pure-point Bragg-peak intensity at the first 10-fold wavevector, together with the model-set pure-point diffraction certificate. A complete answer is either a derivation of the window-area frequency formula and window-Fourier intensity for the named flower-center patch plus the pure-point certificate, or a rigorous exact window-volume recomputation disproving one stated value and identifying the correct frequency or intensity.

## Attempted claim

Let T be the Pentas rhombic quasiperiodic tiling of Fujita-Niizeki 2025 with golden-mean scaling, tenfold symmetry, and planar cut-and-project polygonal windows, distinguished from the rhombic Penrose tiling by its folded/straight dual grid and its two-tiered five-petaled flower motifs. Determine with proof the exact frequency of the two-tiered five-petaled flower-center patch and the pure-point Bragg-peak intensity at the first 10-fold wavevector, together with the model-set pure-point diffraction certificate. A complete answer is either a derivation of the window-area frequency formula and window-Fourier intensity for the named flower-center patch plus the pure-point certificate, or a rigorous exact window-volume recomputation disproving one stated value and identifying the correct frequency or intensity.

## Research outcome

Repaired TARGET: flower-center frequency (9sqrt5-20)/2 ~6.23% via window-area dualization; corrected first-ring Bragg intensity ~7.7298 (internal-coordinate FT, triple-validated) with pure-point certificate; reconciled with Sci Rep 15:41523 S1 domains; 50-digit evidence supplied; dens_exact fixed.

## Why this attempt failed

Failed axes: correctness.

correctness: Re-ran compute_pentas.py: density, covolume, window area, W_F pentagon (5 vertices, rel spread 6e-16, AWF 0.4793945971, freq 0.0623058987 matching (9*sqrt5-20)/2 to 5e-16) and triple FT (F0=|W|, |F(q1)|=1.0099874707, I1=7.7298289264) reproduce. BUT essential inferences fail: (1) 'shortest dual vector / first 10-fold wavevector' n=(2,0,-2,3),|k1|=0.111 is FALSE in the stated CPS. Exhaustive search to |ni|<=12 finds 10-fold orbits at |k|=0.06860537 (5,-5,3,0) and |k|=0.04240045 (-5,0,5,-8) with I~1.88 and ~0.009, so the labeled peak is not first/shortest; Fourier module pi_parallel(L^0) is dense so no shortest non-zero vector exists and 'first' is ill-defined without a cutoff/intensity threshold. (2) Single edge-1 decagon Minkowski CPS equivalence to Pentas P3* is asserted not proved: paper uses 5D hypercubic scheme with 5 ADs and 3D internal space; claimed 'same total area' is numerically false (7.694 vs 5*sin72*(1+tau^2)=17.205=sqrt5*7.694) and freq reconciliations (inner-11 intersection already tau^-4=0.1459 vs paper S1 share (3-sqrt5)/10=0.0764) do not derive. V=21-offset S1 second-shell encoding (S1 vs S2 thin-rhomb distinction) has no tiling-generation or coordinate cross-check. (3) Exact radicals e^2=45-20sqrt5 and freq formula are float-fit identifications (Q(sqrt5) search), not analytic proof; intensity is numeric (~7.73) not exact closed form required by 'exact' target. Pure-point certificate is correct conditionally (regular model set => Hof-Schlottmann-Moody/Baake-Moody) but does not rescue the above.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Edge-1 decagon, unit vertex scatterers; rescaling/decoration changes I by a form factor. freq(F) is per-vertex in the effective Minkowski CPS; paper (3-sqrt5)/10 is the S1 class share in 5D normalization (reconciled in DRAFT Sec 2b). Hyperuniformity/Ammann-bar results cited, not re-derived.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
