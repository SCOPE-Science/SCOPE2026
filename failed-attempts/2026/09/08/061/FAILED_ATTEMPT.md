# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** First A2 (sl3) separation of a Jones-equal 11-crossing knot pair via spider skein recursion
- **Round:** 2026-09-07-first-light-01
- **Lane:** 187
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Low-Dimensional Topology
- **Method:** Kuperberg A2 spider skein recursion with web-resolution logs

## Problem

Close one Jones-collision class beyond the completed Jones tables: take the lexicographically first Jones-equal pair among nonalternating 11-crossing prime knots (Hoste-Thistlethwaite 11n1-11n185) whose KnotAtlas A2 pages carry no entry, recompute both ordinary Jones polynomials from DT codes to certify equality, then compute the exact A2 (quantum sl3) invariant of each member from its DT code by logged Kuperberg spider web-resolution skein recursion and certify whether the two A2 polynomials differ, with fundamental-representation reduction checks.

## Attempted claim

Exact A2 (quantum sl3, Kuperberg spider) polynomials for the two members of the lexicographically first Jones-equal nonalternating 11-crossing prime-knot pair with no prior A2 table entry, each computed from its DT code by logged spider web-resolution skein recursion with fundamental-representation reduction matching the tabulated Jones value, where the two A2 polynomials are provably distinct — closing that Jones-collision class by an sl3 certificate with replayable transcripts.

## Research outcome

Resumed with empty output/; built a verified from-scratch Jones pipeline, recomputed all 185 11n Jones polynomials (185/185 match published), enumerated 15 collision classes, volume-separated the non-mutant pairs K11n11/K11n112 and K11n7 vs K11n36/44, and certified via tabled values that A2 fails to separate all 7 fully-tabled Jones classes. The Kuperberg A2 computation itself remains open and is explicitly not claimed.

## Why this attempt failed

Failed axes: originality, value.

originality: No new mathematical fact beyond the cited tables is established; the admitted target (first exact A2 sl3 polynomials for a Jones-equal 11n pair via Kuperberg spider recursion, distinct) is explicitly abandoned in DRAFT sec.5 ('No new A2 polynomial is computed here... NOT established'). What remains is repackaging of already-tabled values: (a) The 15 Jones-collision classes are a deterministic sort of the 185 published KnotAtlas Jones polynomials; live pages already document the collisions (e.g. K11n11 page lists 'Same Jones: 9_39, K11n112'; K11n7 page lists 'Same Jones: K11n36,K11n44'). Recomputing tabled Jones values with a standard Kauffman-bracket implementation (Kauffman 1987 / KnotAtlas KB1) does not create a new value. (b) Volume/symmetry 'separation' of K11n11/K11n112 and K11n7 vs 36/44 is a direct read of two tabled volume/symmetry entries that already differ on the live pages; HOMFLY equality is likewise tabled on both pages. The tables themselves therefore anticipate the claimed (non-)equalities. (c) Tabled-A2 identity within 7 classes is a direct string comparison of already-published A2 polynomials (e.g. K11n34 A2 on live page). Substantive comparison: Jones 1985 defines the shared invariant; Kauffman bracket theory supplies only the checking method; Kuperberg q-alg/9712003 supplies spider theory but no 11-crossing values (correctly noted in topic.json) — however the draft uses none of it computationally; KnotAtlas Jones/A2/volume pages contain the exact polynomials/numbers compared. A timestamp or replay log does not establish priority, and verification of existing entries is not a new result. value: Judging the strongest self-contained delivered headline (K11n11/K11n112 same Jones+HOMFLY, different tabled volumes/symmetries; triple analogue; 7-class tabled-A2 non-separation) separately from the unfinished A2-separation survey, it is not independently worth retrieving later. All numbers compared are already tabled and mechanically implied by sorting/looking up those tables; a future researcher needing any of these precise facts would consult the live KnotAtlas Data pages directly, not this transcript. The pair is defined extensionally as 'lexicographically first colliding pair' — an ordering artifact, not an object motivated before computation — and volume-distinguishes-Jones-collisions is an expected lookup, not a surprising or structural finding; Kauffman polynomials on the same live pages already differ for K11n11 vs K11n112. The 15-class enumeration is a complete but unexplained sorting of published values with no new theorem, criterion, or downstream use demonstrated. The A2 contribution is a negative transcript ('as far as tabled, does not separate') with remaining classes explicitly undecided, not a citable new invariant value. Per the narrow-datum rule, certification alone does not rescue an already-known number: the exact-invariant exception requires the value be not known or mechanically implied, which fails h…

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: No new A2 (quantum sl3) polynomial computed: a verified Kuperberg-spider recursion was beyond budget, so the admitted A2-separation target is NOT claimed (open problem stated in DRAFT). Volume/symmetry/HOMFLY/A2 comparison values are cited tabled data, not recomputed. Live-table premise corrected: 87/185 11n knots already have A2 entries, so the gap is selective, not total. Pipeline convention fixed empirically on this corpus (185/185), not a general skein theorem.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
