# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Eliminating the smallest open SRG tuple (69,20,7,5) in the 51-100 window via a replayable Bose-Mesner Gram certificate, with a certified Krein/absolute-bound ledger as fallback
- **Round:** 2026-09-07-first-light-01
- **Lane:** 330
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Spectral Graph Theory
- **Method:** Bose-Mesner feasibility algebra with Krein and absolute-bound certificates plus integer Gram verification

## Problem

In the committed window 51<=v<=100, recompute from integer data all SRG integrality conditions, Krein numbers, and absolute-bound certificates in exact rational arithmetic with a bit-for-bit replay log; headline attempt: eliminate the smallest open tuple SRG(69,20,7,5) (restricted eigenvalues 5^23, -3^45) via a replayable integer Gram-matrix positive-semidefiniteness obstruction derived from the Bose-Mesner minimal idempotents.

## Attempted claim

SRG(69,20,7,5) does not exist, witnessed by an explicitly logged integer Gram-matrix certificate: a fixed-template small principal submatrix (rational linear combination of the Bose-Mesner minimal idempotents for the putative parameters) whose failure of positive semidefiniteness is verified by exact integer arithmetic (a negative exact principal minor or negative exact quadratic-form value), accompanied by recomputed exact Krein numbers and absolute-bound rank data for the window.

## Research outcome

Delivered the fallback ledger as the verified result: a complete machine-checkable exact-rational Krein/absolute-bound census over 51<=v<=100 (10098 count solutions; 277 feasible spectra; 15 Krein-FAIL, 18 absbound-FAIL, 106 primitive double-PASS), with the headline tuple (69,20,7,5) certified unobstructed by this machinery (all Krein numbers positive, absolute bounds 299/1080), so existence remains open and only the census is claimed.

## Why this attempt failed

Failed axes: originality, value.

originality: Nearest prior work definitionally anticipates the fallback census content. The live Brouwer catalogue table srgtab51-100 already tabulates for every feasible tuple in 51<=v<=100 the spectrum r^f s^g and the classical obstruction marks (Krein1/Krein2/Absolute bound) or '?' for open cases. Spot comparison: ledger Krein-FAIL (56,22,3,12) = Brouwer 'Krein2; Absolute bound'; (56,33,22,15) = 'Krein1; Absolute bound'; (63,22,1,11) = 'Krein2; Absolute bound'; (63,40,28,20) = 'Krein1; Absolute bound'; (64,21,0,10) = 'Krein2; Absolute bound'; (64,42,30,22) = 'Krein1; Absolute bound'; absolute-only (64,30,18,10), (64,33,12,22), (81,40,13,26), (81,40,25,14), (100,33,18,7), (100,66,39,52) all already marked 'Absolute bound' in Brouwer; headline (69,20,7,5) already listed as '? 69 20 7 5 5^23 -3^45' with blank obstruction column (survives Krein/absolute). Thus PASS/FAIL verdicts are not new. Exact Krein fractions (e.g. 299/32) and counts (10098/277/15/18/106) are direct substitutions into long-known Delsarte/Bose-Mesner formulas (q_ij^k = 1/(v m_k) sum_l k_l Q_li Q_lj Q_lk with weights (1,k,v-k-1)) and trivial divisibility enumeration — mechanically implied, not a new boundary, witness, or criterion. The admitted headline elimination of (69,20,7,5) yielded no witness by the report's own statement, leaving only the recomputation. Single-tuple eliminations for different tuples (Azarija-Marc (75,32,10,16); Bondarenko-Prymak-Radchenko (76,30,8,14)) confirm the recognized-advance form but are different tuples/methods and do not confer priority on this ledger. A timestamp or stdlib replay log does not establish priority. value: Strongest self-contained headline after failure is the classical-feasibility census over 51<=v<=100; it is not independently worth retrieving later. It is a textbook restatement (count equation, integral/conference spectrum, Krein, absolute bound) plus an unexplained enumeration over a catalogue-pagination window (51-100 is the Brouwer HTML page block, not a mathematical boundary), with no new elimination, no tight absolute case (0 tight), no conference failure, and no sharpened criterion. Exact Krein fractions and exclusion-reason tallies are mechanically implied by plugging parameters into known formulas and are computable in seconds; a future existence-search researcher has no need to retrieve 10098 rows or fractions like 299/32, and the claimed downstream prune/replay use can be achieved by running the same seconds-long script rather than citing stored numbers. The four open cases are all certified unobstructed, so no boundary is moved. Per the shared standard, certification alone (exact Q(sqrt(D)) arithmetic, crosschecks, replay.log) does not rescue an arbitrary scope or mechanically implied numbers, and a rigorously established narrow datum is valuable only when the object/invariant was motivated, the value was not known or mechanically implied, and future retrieval is plausible — here verdicts were already known via Brouw…

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: No nonexistence proof for (69,20,7,5) or any open tuple; classical feasibility only (no clique/Terwilliger/structural constraints); conference rows verified formally; no live catalogue comparison re-fetched in this session.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
