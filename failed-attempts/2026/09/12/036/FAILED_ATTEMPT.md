# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Maximal Pasch-free 48-block partial STS(19) with certified non-completion
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1131
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Combinatorial Design Theory
- **Method:** SAT-based completion search with leave-graph maximality check

## Problem

Decide the extremal same-order embeddability boundary for Pasch-free fragments on 19 points: either exhibit a linear-maximal Pasch-free partial system with 48 blocks whose leave is triangle-free and which provably extends to no STS(19), or prove that every such maximal fragment completes.

## Attempted claim

There exists a Pasch-free partial Steiner triple system P on point set [19] with exactly 48 blocks such that no triple outside P can be added without repeating a pair or creating a Pasch (its leave graph with 27 edges is triangle-free) and no Steiner triple system STS(19) on [19] contains all blocks of P as a subsystem.

## Research outcome

TARGET established: explicit 48-block Pasch-free partial STS on 19 points with triangle-free 27-edge leave, certified linear-maximal and STS(19)-incompletable by exhaustive census plus deterministic lemma (verify.py -> VERIFY_OK).

## Why this attempt failed

Failed axes: value.

value: ADMISSION_DEFECT: Admission credited a lane-requested hard obstruction template requiring fresh SAT solving at a canonical near-complete tier. The submitted proof exposes the opposite: non-completability is a trivial corollary of linear-maximality (any incomplete linear-maximal partial is automatically uncompletable), so no SAT certificate or Fano-residue obstruction is present; the leave-triangle census decides everything. The object is arbitrary (seeded greedy output seed 285, with DRAFT admitting seeds 11,94,285,298 of first 300 all give 48-block triangle-free-leave witnesses and greedy routinely reaches 43-51 blocks), and the number 48 is an unexplained slice within that routine band, not a proved cutoff, extremum, classification, or named structure. DRAFT disclaims any count or universality. Certification (VERIFY_OK) does not create value per STANDARD: certification alone does not rescue an arbitrary object or unexplained number. A future researcher has no reason to retrieve this specific random list versus millions of equivalent greedy outputs; it changes no stated boundary (no prior theorem asserted all such fragments complete) and supplies no reusable obstruction pattern beyond elementary pair counting. Hence independently not worth finding later: value FAILS.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Existential single-witness result, not a classification: no count of such partials and no claim about whether every 48-block maximal Pasch-free partial is incompletable. Pasch-freedom and leave-triangle-freedom are certified by exhaustive instance census (exact here); no general same-order completion theorem is proved. Verification run under CPython 3.12 with stdlib only.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
