# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certifying the optimal stabilizer distance of the [[12,2]] stratum with an explicit tableau and MacWilliams/shadow linear-programming certificate
- **Round:** 2026-09-07-first-light-01
- **Lane:** 43
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Quantum Coding Theory
- **Method:** symplectic stabilizer-tableau backtracking search with Pauli-weight enumeration and MacWilliams linear-programming bounds

## Problem

Determine the optimal binary stabilizer distance d* for the short stratum [[12,2,d]] (12 physical qubits, 2 logical qubits, 10 stabilizer generators). Grassl-type tables leave the interval containing {4,5} uncertified; recompute both sides from scratch: exhibit an explicit 10-generator symplectic tableau attaining d* with full Pauli-weight verification table, and prove no [[12,2,d*+1]] stabilizer exists via MacWilliams/Shor-Laflamme plus Rains-shadow linear-programming infeasibility, all rerunnable in minutes with a deterministic log.

## Attempted claim

The optimal binary stabilizer distance for [[12,2]] is d*=4: a genuinely non-CSS [[12,2,4]] stabilizer tableau attains distance 4 (verified by complete Pauli-weight enumeration), and MacWilliams plus Rains-shadow linear programming proves no [[12,2,5]] stabilizer code exists.

## Research outcome

Closed [[12,2]] at d*=4 with verified non-CSS [[12,2,4]] witness and exact MacWilliams/shadow Farkas excluding d=5 (plus MacWilliams-only excluding d=6). Replay under 1s stdlib-only.

## Why this attempt failed

Failed axes: originality, value.

originality: Live retrieval decisively anticipates the mathematical fact claimed as new. Grassl codetables.de live page https://www.codetables.de/QECC.php?q=4&n=12&k=2 (retrieved 2026-09-07) lists Bounds on [[12,2]]_2 lower bound 4 upper bound 4 with explicit Construction of [[12,2,4]] via ExtendCode from [[10,2,4]] plus 10x24 stabilizer matrix, last modified 2005-06-24, and Notes state most n<=100 upper bounds are based on MAGMA program by Eric Rains (i.e., Rains LP/shadow machinery). Hence optimal distance d*=4 for [[12,2]] has been publicly closed since 2005 with both existence and Rains-bound nonexistence sides. Draft's premise that 'Grassl-type tables leave interval {4,5} uncertified' is false per live lookup (table shows point 4-4). Other retrieved priors confirm method not new: Calderbank-Shor-Sloane quant-ph/9608006 gives GF(4)-additive correspondence, MacWilliams and tables to 30; Rains quant-ph/9611001 / DOI 10.1109/18.796376 introduces quantum shadow enumerators tightening Shor-Laflamme LP (exactly the S>=0 used); Huber-Grassl 1907.07733 gives QMDS/shadow theory for MDS/AME regime; Ezerman-Grassl 2405.15057 gives randomized Construction-X records (existence-only); Gottesman quant-ph/9705052 gives stabilizer formalism. None was found to leave [[12,2]] open; the specific Farkas dual (scale 21504) and alternative pure non-CSS tableau are a reformatting/recomputation of the known Rains LP bound for fixed (n=12,k=2) and a different witness for known parameters (draft itself concedes Pauli strings not claimed as previously unknown). Under SCOPE this is a mere parameter instantiation of known LP plus alternative witness, not a substantively new object, gap, or method. value: Even though correct, the result as stated is not independently worth finding later. The citable fact d*=4 for [[12,2]] is already directly citable from Grassl tables (4-4 since 2005) with construction and Rains upper bound. Providing a different (pure, strongly non-CSS, dx=dz=0) [[12,2,4]] witness when a degenerate [[12,2,4]] via ExtendCode (verified here to have distance 4 despite weight-1 stabilizers, B-A zero for j<4) already establishes existence, plus an explicit Farkas dual recomputing the known shadow-LP exclusion of [[12,2,5]], is a tiny unmotivated gain / mere parameter substitution and unexplained-enumeration variant: no new fault-tolerance motivation for purity/non-CSS is given beyond avoiding textbook CSS, no new bound or method, no new interval closed (interval already a point). A future researcher looking up [[12,2]] optimal distance would cite the 2005 table, not this replay. This matches SCOPE rejection precedents for narrow single-parameter closures that are correct but not independently citable (e.g., RT(30,K4,6) AUDIT_REJECT for value).

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['Rains shadow theorem cited not re-proved; fallback without shadow is 4-5 interval via d6 cert also archived.', 'LP drops integrality which is sound for nonexistence; covers pure and impure codes.', 'Tableau novelty is stratum closure with certificate, not Pauli-string novelty.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
