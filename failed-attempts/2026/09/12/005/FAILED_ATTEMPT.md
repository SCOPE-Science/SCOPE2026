# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Insertion-automaton growth separation of Av(1324,1234) versus Av(1324,1243)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1066
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Permutation Pattern Theory
- **Method:** insertion-encoding regular-language automata with transfer-matrix growth analysis

## Problem

Decide the growth-rate ordering of the sibling 1324-type classes Av(1324,1234) and Av(1324,1243) by building their insertion-encoding automata and comparing transfer-matrix spectral radii with rigorous enclosures.

## Attempted claim

The Stanley-Wilf growth rate of Av(1324,1234) is strictly smaller than that of Av(1324,1243), witnessed by regular insertion-encoding DFAs whose transfer-matrix spectral radii admit disjoint rigorous interval enclosures establishing gr(Av(1324,1234)) < gr(Av(1324,1243)).

## Research outcome

Dual-verified exact census of Av(1324,1234) vs Av(1324,1243) to n=14 with certified Fekete lower bounds 3.8817 vs 3.8222 and insertion-state obstruction record, submitted as emergent finding after target block.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Enumeration engines are structurally sound and cross-agree to n=10 (auditor re-ran all three to n=10 with identical 224352/206098) and gen_full to n=12 matches counts_n12; min-insertion (new-min role 1, exact 4-tuple test) and max-insertion (triples-left plus t1<t2<g<t3 logic) are correctly derived. However Section 4 is mathematically false: all three forbidden patterns ARE sum-decomposable (1324=1+213, 1234=1+123, 1243=1+132), and sum-decomposable bases imply the class is NOT sum-closed (counterexample 1 in C, 213 in C since n=3, but 1(+)213=1324 not in Av(1324,1234); similarly 1(+)132=1243 not in Av(1324,1243)). Hence a_{m+n}>=a_m a_n and Fekete sup formula do not follow; spot checks in verify14.py do not prove general supermultiplicativity. The Arratia/Fekete existence justification via sum-closure is therefore invalid and the certified lower bounds 3.8817/3.8222 are unproved as stated (numerically plausible but not derived). The state-growth obstruction is only a computed datum, not a non-regularity proof, as the DRAFT admits. originality: EMERGENT_FINDING route is genuine (same sibling pair, methods and growth question as the target investigation, in the survey valuable-partial-target form), so no scope evasion; it is assessed under the ordinary full standard with no presumption. It still FAILS originality: both exact n=14 integers already appear verbatim in official databases. Class A row equals OEIS A053617 (Av(1234,1324)) whose fetched entry lists 1,1,2,6,22,90,396,1837,8864,44074,224352,1163724,6129840,32703074,176351644,959658200,... with b-file to n=600 (Baxter/Pantone). Class B row equals the large Schroder numbers OEIS A006318 (shifted by one: B_n=A006318_{n-1}), whose fetched b-file lists ...27297738,142078746,745387038... and literature explicitly states Av(1324,1243) is enumerated by the large Schroder numbers (Kremer 2000; Claesson et al. thesis Table 5.8; Kremer-Shiu Table 1). The n=9..14 counts, and any root lower bounds derived from them, are therefore database recomputation/corollary of a known stronger exact enumeration and algebraic generating function, not new material. Fused literature search (two scope_literature_search calls, full provider coverage, no partial failure) plus direct OEIS fetches confirm coverage. value: Because both rows to n=14 (and far beyond: A to n=600, B to arbitrary n via Schroder algebraic generating function (1-x-sqrt(1-6x+x^2))/(2x) with growth 3+2*sqrt(2)≈5.828) are already published with exact formulas, the dual census to n=14 is known-database recomputation which the STANDARD explicitly rejects even if correctly certified. The Fekete bounds are both unproved (see correctness) and dominated by the known exact growth data (Schroder rate 5.828; A053617 600-term asymptotics), adding no new benchmark. The gap-mask/future-type numbers are an unexplained computed datum without a theorem (no non-regularity proof, no upper bound, no rate separation), and finite counts cannot decide the ra…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Finite counts through n=14 cannot decide the asymptotic Stanley-Wilf rate ordering, so neither gr(A)<gr(B) nor its reverse is proven here; the Fekete bounds are one-sided lower bounds only (no rigorous upper bound on either rate is established); the insertion-state-growth record is a computed obstruction datum, not a proof of non-regularity; n=10..14 counts rest on cross-agreed insertion engines (third engine and brute force verified only to n=9 and n=8 respectively).

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
