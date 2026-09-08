# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Minimal-LCM distinct covering in the 2520-pinned slice: LCM-divisibility classification with obstruction certificates
- **Round:** 2026-09-07-first-light-01
- **Lane:** 216
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Combinatorial Number Theory
- **Method:** LCM-pinned divisor-lattice search with CRT replay and integer-programming/density obstruction certificates

## Problem

Classify all distinct-modulus covering systems whose moduli divide LCM 2520 with max modulus <=30 (universe: the 18 divisors of 2520 above 1 and <=30): decide feasibility for each of the 2^18 modulus sets by LCM-pinned divisor-lattice search with CRT replay (mod L|2520) and integer-programming/density obstruction certificates, and determine the exact minimal LCM L* among coverings with minimum modulus >=4, with witness and UNSAT certificates for every smaller divisor of 2520.

## Attempted claim

Exact LCM-pinned classification: the complete feasible/infeasible table for distinct-modulus sets drawn from divisors of 2520 (<=30), plus the exact minimal LCM L* attained by a distinct covering with minimum modulus >=4 in this slice, with an explicit residue witness attaining L* and ILP/density UNSAT certificates ruling out every smaller divisor of 2520, all replayable by CRT enumeration mod <=2520.

## Research outcome

Certified partial classification of the 2520-pinned min>=4 slice: exact 8-class reciprocal sieve, machine-checked UNSAT of LCM classes 120 and 180 (with full subset monopoly), and a verified 2422/2520-coverage residue witness; larger LCM classes left explicitly open.

## Why this attempt failed

Failed axes: originality, value.

originality: Strongest remaining substantive claims (reciprocal 8-class sieve + UNSAT of LCM classes 120 and 180 for min>=4) are substantively anticipated and mechanically implied by prior minimal-LCM theorems combined with elementary counting. Harrington et al. arXiv:2605.18644 states as Theorems 1.1-1.2: Dalton-Trifonov m=4 => L>=360; Klein m=5 => L>=1440, m=6 => L>=5040 (no 2-3-5 restriction on those bounds). L=120 and L=180 are both 2^a3^b5^c (hence inside Harrington universe) and both <360. Any distinct covering with min>=4 and lcm|L has m=min>=4: if m=4 contradicts L>=360; if m=5 contradicts L>=1440; if m=6 contradicts L>=5040; if m>=7 contradicts counting (eligible>=7 sums: L=120 gives 15+12+10+8+6+5+4=60<120; L=180 gives 20+18+15+12+10+9+6=90<180, and larger m only smaller). Hence UNSAT for L=120/180 with min>=4 follows directly from cited prior bounds + reciprocal sum, and prior bounds apply to ALL moduli (stronger) while DRAFT restricts to divisors of 2520 <=30 (weaker). Theorem 1.6(i)(ii)(iv) also directly rules out m=4 for exponents (3,1,1)=120 and (2,2,1)=180. The 8-class sieve is exact integer arithmetic sum(1/m)>=1 over 48 divisors, mechanically implied, not a new invariant. The 2422/2520 residue list is an arbitrary non-optimal lower bound with no maximality, not a substantive prior-overlapping theorem but also not a new exact invariant. Agrawal et al. (cardinality<=10), Hough (analytic min-modulus bound), Balister et al. (density/Schinzel) confirm no LCM-pinned table exists, but the minimal-LCM-table prior already decides the two closed classes. Timestamp/failed search does not establish priority; substantive implication does. value: Headline target in topic.json (complete feasible/infeasible table + exact minimal LCM L* for min>=4 with witness and UNSAT for every smaller divisor) is explicitly abandoned: DRAFT Sec.6/research_report limitations state classes 360,420 (12/10 timeouts), 504,840,1260,2520 open, no minimal-LCM extremal, no maximal-density claim, no covering-existence verdict. Judging strongest self-contained remainder separately: (a) 8-class reciprocal sieve is trivial counting (sum 2520/m>=2520), not independently retrievable; (b) L=120/180 UNSAT is a strict corollary of stronger prior general minima (see originality), adding no new benchmark; (c) 2422/2520 (173/180 approx 0.961111) 16-modulus partial cover is a one-sided heuristic lower bound with 98 uncovered, no optimality, no density-1 covering, no motivated precise fact a future researcher would need; certification alone does not rescue an arbitrary unexplained number. No maximal-density table, no density-1 witness, no minimal-LCM extremal achieved. Honest partial census does not erase the absence of an independently valuable exact headline invariant.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Classes L=360 (12 timeouts), L=420 (10 timeouts) censused with 0 covers but incomplete; L=504/840/1260/2520 open; full-16 covering existence undecided (DFS capped); 2422/2520 is a lower bound, not a proven maximum; no minimal-LCM extremal established.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
