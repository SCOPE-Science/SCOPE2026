# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Chermak-Delgado lattice-shape census and CD-minimal/maximal-width extremals for groups of orders 64 and 81
- **Round:** 2026-09-07-first-light-01
- **Lane:** 315
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Finite Group Theory
- **Method:** polycyclic presentation with centralizer-measure CD-lattice extraction and lattice-type classification

## Problem

From committed polycyclic presentations, construct every group of orders 64 and 81; for each compute centralizer orders, the Chermak-Delgado measure m(H)=|H||C_G(H)|, its maximum m(G), the CD-subgroup, the full CD(G) membership with |CD(G)|, width and lattice isomorphism type; and certify the CD-minimal groups (|CD(G)|=2) and the maximal-width quasi-antichain CD-lattice witness in each order by exhaustive replay.

## Attempted claim

The exhaustive CD-shape census over all 267 groups of order 64 and all 15 groups of order 81 determines for each group its CD-measure maximum m(G), CD-subgroup, |CD(G)|, width and lattice type; headline extremals are the explicit CD-minimal groups with |CD(G)|=2 and the maximal-width quasi-antichain CD-lattice witnesses of exact widths W_64 and W_81 (values decided by the replay), each certified by independent polycyclic centralizer-measure replay, with the maximizers lying outside the elementary-abelian and Qu-Tarnauceanu second-maximal S_max families.

## Research outcome

Downgraded the infeasible 282-group census (no GAP available) to a fully verified exact CD fragment: certified CD-minimal S4 witness, exact CD rows for 6 groups of order 64 and 5 (+C3^4 ranks) of order 81 with in-set maximal-width quasi-antichain witnesses M_3 (D8xC8) and M_4 (C27sem3), plus C3^4 subgroup-lattice width 130, all replayed by an independent verifier (VERIFY_OK).

## Why this attempt failed

Failed axes: originality, value.

originality: Strongest self-contained headline claims are previously known or mechanically implied, not new. (1) S4 CD={1,S4} (|CD|=2): McCulloch 1706.01431 explicitly cites 'the symmetric group on 4 elements is the smallest nontrivial example' of CD-simple groups; numeric fact is textbook prior. (2) D8/Q8 M_3 (m=16, orders [2,4,4,4,8], width 3) and S3 CD={A3}: admitted calibration from Brewster-Hauck-Wilcox / standard literature. (3) Abelian CD={G}, C3^4 Gaussian ranks [1,40,130,40,1] total 212, subgroup-lattice width 130: trivial lemma + textbook Gaussian/Sperner combinatorics. (4) D64/Q64/SD64 singleton CD: Tarnauceanu 1611.04155 proves CD of dihedral D_{2m} with m!=4 is a chain of length 0 (singleton), so shape is a prior theorem; exact m=1024 is instantiation. (5) D8xC8 M_3 size 5: mechanically implied by direct-product theorem CD(GxH)=CD(G)xCD(H) (Brewster-Wilcox, Lemma 2.5 in Burrell et al 2211.14910) combined with known CD(D8)=M_3 and CD(C8)={C8}. (6) Widths 3=1+2^1 and 4=1+3^1 conform to Brewster-Hauck-Wilcox/An 1407.6215+1705.06456 theorem that quasi-antichain widths are 1+p^a; no new width realization. No prior complete 267+15 census exists, but the draft explicitly abandons it (12 named groups, one of which C9sem3 is order 27, C2^6 omitted), so remaining per-group numbers for C27sem3/C9sem3 are an arbitrary fragment, not a new claim/boundary/classification fragment. A timestamp/failed search does not establish priority; substantive comparison shows overlap. value: Planned value (first complete CD-measure/subgroup/size/width/shape census over 267 groups order 64 + 15 order 81 testing quasi-antichain bounds and An's abelian-atom converse) was not delivered. Admitted scope is: 12-group fragment (6/267 order-64, 3/15 order-81 plus order-27 C9sem3 and 4 calibrations), S4 witness outside the 64/81 window, 'maximal-width within computed set' only, and C3^4 subgroup-lattice (not CD) width. This is arbitrary scope / unexplained enumeration: 'widest among groups I happened to compute' has no natural boundary, no global extremality, no test of the open converse, and widths 3,4 were already known realizable. Per instruction, certification alone does not rescue an arbitrary object or unexplained number, and textbook restatements / parameter substitutions / mechanically implied values (abelian lemma, Gaussian counts, direct-product corollary, dihedral singleton shape, D8/Q8/S4 calibrations) are rejected even if correct and new. No independently retrievable exact invariant is established whose object+invariant were motivated before computation, whose value was unknown and not mechanically implied, and which a future researcher would need. Hence intrinsic low value and missing substantive result.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Partial result only: 12 named groups of orders 64/81, not the full 267+15 census (no GAP/SmallGroups in this environment, no root to install). CD-minimal witness S4 is order 24, outside the 64/81 window. Maximal-width claims are restricted to the computed set, not global over all groups of order 64/81. C2^6 was not run (lattice too large for time budget) and is excluded from all claims.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
