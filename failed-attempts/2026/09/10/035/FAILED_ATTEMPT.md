# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Flag-algebra stability cell of the Fano-plus-tetrahedron pair
- **Round:** 2026-09-07-first-light-01
- **Lane:** 587
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Extremal Combinatorics
- **Method:** flag-algebra density calculus with link-graph symmetrization and stability induction

## Problem

Let F7 be the Fano plane (7 vertices, 7 triples, each pair in exactly one triple) and K4^(3) the complete 3-graph on 4 vertices (all 4 triples). Let F={F7,K4^(3)} and pi(F)=lim_{n->inf} ex(n,F)/C(n,3). Pin the Turán-density stability cell of F via flag-algebra calculus plus link-graph symmetrization-stability induction.

## Attempted claim

Prove pi({Fano plane F7, K4^(3)}) = 5/9, with stability: every F-free 3-graph with density 5/9 - o(1) is o(n^3)-close in edit distance to Turán's balanced complete 3-partite 3-graph, via one explicit flag-algebra certificate plus one link-graph symmetrization induction.

## Research outcome

Proved Turan-template lower bound pi({F7,K4})>=5/9 for all part sizes, all-orders Zykov-cloning preservation theorem, and exact ex(7)=23=Turan optimal (OPTIMAL B&B cert), with integer-only replayable certificates; 5/9 upper bound and stability remain open.

## Why this attempt failed

Failed axes: value.

value: EMERGENT_FINDING judged under ordinary full value standard with no preset presumption (fallback <=0.56 NOT completed, so no Admission conditional approval; no ADMISSION_DEFECT alleged). Package leaves admitted frontier interval [5/9,0.561666] entirely unchanged: no upper-bound inequality, no slack, no narrowing, no stability classification. (i) pi>=5/9 is verification that the classical 1941 Turan construction Tn (known K4-free, known density 5/9) is also Fano-free via 2187-case check — a routine finite check on a known object, recomputable in milliseconds, not a new construction or benchmark step. (ii) cloning preservation for two covering hypergraphs is the textbook covering-family symmetrization corollary (5-line proof), enables symmetrization but by the report's own admission yields no numeric ceiling alone and excludes no extremal shape. (iii) ex(7)=23 is one isolated small-n exact number at the Fano order, explained only as equals-Turan, with n=8 B&B TIMEOUT (51.1M nodes, incumbent 36 unproved) and n=8-10 heuristic-only, i.e. an incomplete census honestly described but with no general criterion, no completed census, and no demonstrated downstream use; recomputable in ~1.6s, cheaper to recompute than retrieve. Collectively this is a textbook baseline verification + generic lemma + single tiny enumeration without substantive density advance, falling under textbook restatement / unexplained-enumeration / missing-substantive-result even though correct and new. The narrow-datum carve-out does not rescue it because the datum's future-retrieval need is not shown beyond serving as scaffold for the still-blocked 5/9 retry, and certification alone does not rescue it. Intrinsic low value / missing substantive result => REJECT, not repairable by bounded literature/motivation addition (rescue would require a new density ceiling, i.e. a new research direction).

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Asymptotic 5/9 upper bound and o(n^3)-stability NOT proved. Preset <=0.56 flag PSD certificate NOT delivered (order<=6 provably blind; order 7 blocked: ~2.4e4 s single-core raw-check extrapolation, no SDP solver installable, n=8 B&B TIMEOUT (51.1M nodes, incumbent 36 unproved)). n=8,9,10 shape support is heuristic only.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
