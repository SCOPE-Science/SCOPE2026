# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** LOSS-distinguished non-loose trefoils T(2,3) at fixed tb=7 in Hopf-1 overtwisted S3
- **Round:** 2026-09-07-first-light-01
- **Lane:** 859
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Contact Topology
- **Method:** convex-surface bypass calculus with Heegaard-Floer LOSS comparison

## Problem

Decide whether two explicit non-loose Legendrian right-handed trefoils T(2,3) with tb=7 and rot=0 in the overtwisted S3 with Hopf invariant 1 (d3=1/2) are Legendrian isotopic or LOSS-distinguished.

## Attempted claim

There exist non-loose Legendrian knots L1, L2 of type T(2,3) in overtwisted (S3, xi_1) with Hopf invariant 1, each with tb=7 and rot=0 and tor=0 complement, presented by an explicit contact surgery diagram and joined by a documented bypass triangle of dividing slopes, such that LOSS(L1) != LOSS(L2) in HFK(-S3,T(2,3)) (one nonzero, one vanishing/distinct grading); hence L1 and L2 are not Legendrian isotopic (fine non-simple pair), or else the audit certifies the sharp bypass isotopy collapsing them.

## Research outcome

The admitted (7,0) Hopf-1 LOSS gap is a priori impossible: every Legendrian T(2,3) at tb=7, rot=0 in any contact S3 has vanishing (hat-)LOSS since Alexander grading 4 lies outside genus-1 HFK support. Certified sharp LOSS-collapse for the exact admitted cell, replayable via verify_grading.py.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL: headline is a one-line arithmetic instantiation of two textbook general facts that jointly dominate it, not a new Floer computation. General grading theorem A(LOSS)=(tb-rot+1)/2 plus general genus bound supp|A|<=g substantively implies the (T(2,3),7,0)->A=4>1= g vanishing with no additional diagram, bypass, or Floer work. Prior source need not state '(7,0)' verbatim; mechanical implication suffices per contract. Failed exact-identifier search does not establish priority. See decisive_checks: equivalent_formulations and broader_coverage COVER the claim; exact_database confirms support; claim_vs_prior_implication is corollary/repackaging of known stronger fact. value: FAIL: textbook restatement / mere parameter substitution. Plugging (7,0) into A=(tb-rot+1)/2=4 and observing 4 outside [-1,1] requires no fresh bypass log, surgery diagram, grid computation, or Floer differential; verify_grading.py only recomputes arithmetic and table membership. Under value standard, a narrow exact invariant is retrievable only when object+invariant were motivated, value is not known or mechanically implied, and future researcher could need precise fact. Here value IS mechanically implied by standard formulas any LOSS user already knows; no separate record needed to avoid budgeting a LOSS witness at (7,0). DRAFT decides no existence, no isotopy via other invariants, no bypass triangle, no tor/stabilization — the admitted valuable partial (bypass-triangle lemma + LOSS comparison log) is not delivered. Certification of elementary arithmetic does not rescue it. Intrinsic low value, not a bounded-addition defect.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['Does not decide existence of non-loose (7,0) trefoils in Hopf-1 overtwisted S3 nor Legendrian isotopy via non-LOSS invariants.', 'Named Hopf-1 surgery diagram and bypass triangle at (7,0) not constructed (mooted for LOSS purposes).', 'tor=0 and stabilization behavior not computed.', 'Covers LOSS/hat-LOSS only, not transverse or plus-flavoured invariants.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
