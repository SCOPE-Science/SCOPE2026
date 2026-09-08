# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Regularity and projective-dimension records among edge ideals on 7-8 vertices with certified minimal resolutions and Betti census
- **Round:** 2026-09-07-first-light-01
- **Lane:** 137
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Commutative Algebra
- **Method:** minimal free resolution over Q by exact Taylor-to-minimal reduction with Hochster-formula Betti replay

## Problem

Over S=Q[x1..xn), survey edge ideals I(G) of all connected simple graphs G on n=7 and n=8 vertices: determine max reg(S/I(G)) and max pd(S/I(G)), exhibit and certify a regularity-record graph with its full minimal graded free resolution and Betti table, and publish the complete per-graph Betti census with independent verification.

## Attempted claim

Over Q, determine R7=max reg(S/I(G)) and R8=max reg(S/I(G)) over connected G with |V|=7,8, and P7,P8 for projective dimension, by complete census; exhibit an explicit record graph G* on 8 vertices attaining R8 (expected 3 or 4 in S/I convention, i.e. 4 or 5 in I convention) with its full graded Betti table, explicit minimal free-resolution differential matrices, rank-nullity minimality log, and Hochster-formula replay, plus a table proving every other connected 8-vertex graph has strictly smaller regularity.

## Research outcome

Certified extremal fragment: exact R7=3, P7=6, P8=7 proved; R8 in {3,4} (=3 under cited Matsuda-Yoshida); four exact Betti tables doubly verified by independent Hochster pipelines with Euler replay and closed-form checks.

## Why this attempt failed

Failed axes: value.

value: Result as achieved is not independently worth finding later. (1) P7=6/P8=7 + K7/K8 tables are textbook restatements / mere parameter substitutions of general facts pd_max=n-1 and 2-linear K_n formula. (2) R7=3 is floor(7/2) attained by trivial 3-disjoint-edges-plus-hub graph where Katzman and Woodroofe bounds coincide; already implied by MY classification, no new insight, no runner-up separation. (3) R8 not resolved unconditionally (interval {3,4}); record claim rests on cited MY, not proved here; G8reg only shows R8>=3, not maximality. (4) Committed census over 853+11117 connected types with record-vs-next separation and Taylor-to-minimal matrices not delivered (honestly disclosed); fallback interval table over full window also not delivered (only 4 graphs, not per-graph im/upper-bound intervals). Four isolated Betti tables without census, maximality, or demonstrated downstream reuse (no Stillman calibration, bound-sharpness test, or software benchmark use shown) are unexplained enumerations. Reusable Hochster script is standard 2^n enumeration. Hence fails value gate: textbook restatement + parameter substitution + unexplained enumeration even if correct and narrowly new.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: No complete census over the 853+11117 connected types (infeasible here: no nauty/geng/CAS); no Taylor-to-minimal differential matrices; R8<=3 upper bound rests on cited Matsuda-Yoshida classification, not proved here (unconditional result is R8 in {3,4}); all homology over Q, characteristic dependence not studied; record-vs-runner-up separation over the full window not established.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
