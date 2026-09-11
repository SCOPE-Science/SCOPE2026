# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact diameter and eccentricity census at p=1009
- **Round:** 2026-09-07-first-light-01
- **Lane:** 883
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Arithmetic Geometry
- **Method:** finite-field isogeny enumeration with breadth-first search over F_{p^2} j-graph

## Problem

Determine the exact diameter of the full supersingular 2-isogeny graph at p=1009 over F_{p^2}, with full eccentricity histogram and explicit diametral-pair shortest-path witnesses verified by Velu steps.

## Attempted claim

At p=1009 the full supersingular 2-isogeny graph over F_{p^2} is connected with exact diameter D (computed integer, conjecturally single-digit) attained by an explicit diametral pair (j_a, j_b) with logged shortest 2-isogeny chains in both directions, plus the complete vertex-eccentricity histogram.

## Research outcome

Full supersingular 2-isogeny graph at p=1009: 84 vertices, connected simple 3-regular, exact diameter D=8, radius 7, eccentricity histogram {7:61, 8:23}, 30 diametral pairs, with a diametral j-path and all 16 bidirectional translated-Velu steps logged; independent verify.py prints VERIFY_OK.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL. Core headline integer D=8 at p=1009, l=2 is already published in the official Isogeny Database table (isogenies.enricflorit.com/graphs/g1/577-1259.html, section p=1009: 84 nodes, l=2 diameter 8, c_ell 7, lambda values). Database Glossary defines Gamma_1(ell;p) as supersingular j vertices + ell-isogeny edges, i.e. the same Phi_2 graph under synonymous notation. Admission claim that 'no exact full-graph diameter at p=1009 is published' and 'database publishes no diameter' is factually false. Stronger logarithmic/Ramanujan/spine results do not imply exact D, but the database table literally states it, so equivalent-formulation and exact-table checks cover the claim. Histogram {7:61,8:23}, 30 pairs, and one diametral j-pair are BFS corollaries mechanically derivable in seconds from the public downloadable adjacency (npz to 30000, covers p=1009); Velu chains certify one arbitrary pair among 30, i.e. recomputation/certificate/repackaging, not a new invariant. Prior source need not state histogram verbatim: public adjacency + published diameter substantively covers the headline. Route is TARGET (report states TARGET and matches target_claim), so no preset presumption applies. value: FAIL as independent retrieval. The natural object (full 2-isogeny graph at p=1009) and diameter question are motivated, but the precise value D=8 is already tabulated and the remaining data (eccentricity histogram, diametral-pair count, one pair) are mechanically implied by the public adjacency matrix via stdlib BFS. Per value policy, an exact invariant must be not known and not mechanically implied to be independently worth retrieving; here both fail. One of 30 diametral pairs with bidirectional Velu chains is an arbitrary selection with certification only, serving the already-known diameter rather than a new downstream benchmark need. This is database repackaging: fresh BFS/Velu computation that does not add a non-mechanical fact beyond the published table+adjacency. Correctness PASS does not rescue it.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Diameter upper bound rests on all-pairs BFS over the Phi_2 adjacency table (rebuilt independently by the verifier); only one of 30 diametral pairs carries logged Velu chains (others extractable by BFS from the committed table). Graph rule is Phi_2=0 undirected; no loops/multi-edges occur at this prime so conventions cannot shift distances.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
