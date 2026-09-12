# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Falsifiable radial revealment ledger for Voronoi annulus circuit window
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1067
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Statistical Mechanics
- **Method:** randomized-algorithm revealment with OSSS inequality and Russo-Margulis differential inequality

## Problem

For intensity-1 Poisson-Voronoi coloring on annulus A(n,2n) with n>=16, let Circ_n be a red circuit separating inner and outer boundaries. Does the inward radial exploration that reveals frontier cells achieve max-cell revealment at most 0.30 n^{-1/3} uniformly for p in [0.3,0.7], hence a 0.3-to-0.7 circuit threshold window of width at most 0.70 n^{-1/3}?

## Attempted claim

For annulus A(n,2n) with n>=16 under intensity-1 Poisson-Voronoi red coloring, the named inward radial exploration determining red circuit Circ_n satisfies sup_{p in [0.3,0.7]} max_i P[queries i] <= 0.30 n^{-1/3}, so the p-window on which P_p[Circ_n] rises from 0.3 to 0.7 has width at most 0.70 n^{-1/3}. At n=16 the bounds evaluate to 0.119 against cap 1 and 0.278 against maximum width 0.4, hence both constrain frontier-query probabilities at every scale n>=16.

## Research outcome

Disproved the target: any correct exhaustive inward radial exploration has query probability at least theta(0.7)^2 > 0 at p=0.7 uniformly in n, contradicting the 0.30 n^{-1/3} cap; exact audit-patch arithmetic plus seeded proxies document why the canonical proof route fails.

## Why this attempt failed

Failed axes: correctness, value.

correctness: TARGET route: universal revealment bound for exhaustive inward radial exploration determining Circ_n on A(n,2n). Core inequality (1) R_B>=P[B red-connected to seed-ray cluster] is false for any terminating correct algorithm. Correctness does NOT require exploring full whole-plane red components: once a red circuit witness is found the algorithm may stop and output 1 without querying distant B, even if B connects via the infinite cluster through far outside-annulus detours. The DRAFT's exhaustive whole-plane version would never terminate at p=0.7 (infinite cluster infinite) and is not the natural annulus-restricted decision tree; annulus-restricted connectivity was never lower-bounded. FKG monotonicity for Voronoi red-set under red-point addition plus colour flips is asserted without proof, and artifact B2 contradicts DRAFT Sec.7: code uses p=0.5 with phat=0.098 below cap 0.119, not p=0.7 query ~0.70 with CI>=0.63. Hence constant-vs-decaying separation is unproved. value: ADMISSION_DEFECT: admission preflight ruled out type/normalization defects and promised a checkable-scale obstruction already biting at A(16,32) (0.119 vs 1). The submitted disproof is only an asymptotic existential violation for n>(0.3/c0)^3 with no explicit violated n because theta_Voronoi(0.7) has no proved explicit lower bound, and it exploits the fixed-interval normalization overreach sup over [0.3,0.7] including deeply supercritical p where any red-exploring rule trivially stalls, rather than the motivated critical radial cost. That is exactly the cheap normalization/scope defect TARGET policy says fails value even if literally false. It leaves the qualitative small-exponent radial OSSS program intact and teaches no checkable frontier ledger, so independent retrieval value fails.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: The disproof is asymptotic (existence of a violated large scale) with no explicit violated n since theta_Voronoi(0.7) has no proved explicit lower bound; it falsifies the universal over n>=16 claim but leaves the qualitative small-exponent radial OSSS program intact. It targets correct exhaustive frontier explorations (AB-style correctness forces exhaustiveness); a hypothetical early-stopping variant would be a different algorithm. Triangular-lattice proxy numbers are heuristic illustrations on…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
