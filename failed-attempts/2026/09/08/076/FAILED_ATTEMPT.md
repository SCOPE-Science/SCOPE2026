# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Replayable systole census over smooth Fricke octagon and dodecagon gluings in genus 2-3 with a Bolza-type extremal witness
- **Round:** 2026-09-07-first-light-01
- **Lane:** 229
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Differential Geometry
- **Method:** Fricke trace-identity discreteness check with systole enumeration by hyperbolic trigonometry replay

## Problem

Census the hyperbolic systoles over the complete combinatorial scope of smooth orientation-preserving side-pairing gluings of the regular octagon (genus 2) and regular dodecagon (genus 3) with their regular-polygon hyperbolic metrics: for each smooth gluing (single vertex cycle, angle sum 2*pi), verify discreteness via Fricke trace identities, enumerate the closed-geodesic length spectrum to a fixed cutoff L_cut by generator-word BFS with trace-cosh replay L=2*arccosh(|tr|/2), and tabulate the systole with a collar-lemma lower-bound cross-check and a logged realizing word.

## Attempted claim

The complete per-gluing systole table over all smooth orientation-preserving octagon (genus-2) and dodecagon (genus-3) regular-polygon gluings, with each systole enclosed by a realized-word upper bound and a collar-lemma lower bound at fixed cutoff L_cut, in which the Bolza-type genus-2 pairing uniquely attains the maximum 2*arcosh(1+sqrt(2)) with a full trace-word log and collar-gap certificate.

## Research outcome

Complete replayable systole census (W-ball certified) over all 21 smooth genus-2 and 1485 smooth genus-3 regular-polygon gluings with explicit SL(2,R) word logs, Poincare relation residuals, collar consistency data, and an exact Bolza-type extremal witness at 2*arcosh(1+sqrt2); independently re-verified VERIFY_OK on all 1506 rows.

## Why this attempt failed

Failed axes: value.

value: Strongest self-contained headline (W-ball minima + Bolza witness) is correct and new as a computation but not independently worth retrieving. Motivated invariant was true systole for systolic/maximal-surface calibration; delivered invariant is cutoff-dependent W-ball minimum (W=6/W=4) plus realized-word upper bounds with no lower-bound proof (collar used only as consistency check; JSON contains no collar/area fields; research_report admits no lower-bound proof). W-ball minima are not geometric invariants (depend on generator choice and W) and a future worker needing exact systoles cannot cite them as systoles. Tier values are mechanically implied: 20/21 g2 rows at 2.2567679299 realized by single generators (cosh(L/2)=1.70710...=1+sqrt2/2, the common side-pairing translation length of the regular octagon); 1214/1485 g3 rows at 2.4718020466 realized by single generators (cosh=1.86602...=1+sqrt3/2). Only distinctive row (opposite/Bolza pairing at 3.05714...) replays the long-known Bolza value, not a new inequality; g3 top tier (7 rows at ~3.32577, length-2 words) is explicitly scope-relative, not a global genus-3 maximum. Census collapses to 2-3 tiers of short-word upper bounds over a regular-polygon Teichmuller slice. Certification (VERIFY_OK) alone does not rescue cutoff-dependent numbers. This is an unexplained enumeration of upper bounds / tiny-slice artifact, not a rigorously established new exact invariant of the motivated object. Rescuing would require global optimality certification beyond cutoff (unbounded search + genuine lower-bound proof), which is a new research direction, not a bounded addition.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: W-ball minimality certified only to stated cutoffs (W=6 g2, W=4 g3); global true-systole optimality beyond cutoff is conjectural, so table values are rigorously realized-word upper bounds + in-ball minima; collar lemma used as one-sided consistency check, not a lower-bound proof of global systole; Bolza value classical, replayed as witness; no directed-rounding interval certificates (double precision + 50-digit witness only); genus-3 top tier is scope-relative, not a global genus-3 maximum.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
