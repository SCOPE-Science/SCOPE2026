# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sharp parametric boundary for Erdos-Straus: first prime 1 mod 4 outside the classical Mordell family, with obstruction certificate
- **Round:** 2026-09-07-first-light-01
- **Lane:** 153
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Diophantine Equations
- **Method:** frozen classical identity family with divisibility/congruence non-coverability proof plus divisor-congruence witness

## Problem

Freeze the finite classical Mordell polynomial-identity family M for 4/n (Mordell 1967 as surveyed in Elsholtz-Tao/Ionascu-Wilson) before computing. Determine the least prime p* =1 mod 4 such that 4/p* is solvable in three unit fractions but is NOT an instance of any identity in M: prove non-membership for p* by finite divisibility/congruence elimination over M, exhibit one explicit divisor-congruence triple (x,y,z) with 4/p*=1/x+1/y+1/z verified by exact arithmetic, and tabulate M-parameters covering every smaller prime =1 mod 4.

## Attempted claim

Let M be the frozen finite classical Mordell splitting-identity family (fixed from the literature before computation). There is an explicitly computed least prime p* =1 mod 4, with p* inside a stated small search envelope, such that (i) for every prime p < p* with p =1 mod 4, 4/p is exhibited as an instance of a stated identity in M with logged parameters, (ii) 4/p* admits an explicit triple (x,y,z) with 4/p*=1/x+1/y+1/z, and (iii) NO identity in M instantiates 4/p*, proved by a finite divisibility/congruence elimination certificate per identity in M.

## Research outcome

Least 1-mod-4 prime outside the frozen 3-identity Mordell core is 73: full coverage table below, congruence elimination proof, explicit divisor-structured witness, stdlib replay passing.

## Why this attempt failed

Failed axes: originality, value.

originality: Headline fact is substantively anticipated by prior classical reduction to 1 mod 24, not new. Salez 1406.6307 Sec 1.1 explicitly gives identities 4/(4t-1), 4/(8t-3), 4/(3t-1) and concludes 'it is then sufficient to prove that 4/p is 3-Egyptian, for any prime p such that p=1 mod 24.' That is exactly the statement that the classical elementary toolkit covers all primes except 1 mod 24. The least prime =1 mod 24 is 73 (1,25,49 composite; 73 prime), a trivial arithmetic consequence. DRAFT's frozen set {F3=n=4k+3, F5=n=8M-3, F17=n=24M-7} is a candidate-defined variant: F3=F5 coincide with Salez's 4t-1 and 8t-3; F17 (17 mod24) is swapped for Salez's 3t-1 (2 mod3) but covers the same <73 1-mod-4 primes needing it (17=3*6-1, 41=3*14-1 are covered by either). Hence Salez's own classical triple also has least 1-mod-4 failure 73 (5,13,29,37,53,61 via 8t-3; 17,41 via 3t-1; 73 fails all three: 1 mod4, 1 mod8, 1 mod3). The threshold 73 is therefore mechanically implied by the long-published covering lemma, not a new sharp parametric-power boundary. Elsholtz-Tao 1107.1010 Sec 10 / Prop 1.9 plus Schinzel obstruction similarly surveys polynomial-identity limits. No freezing of exactly these 3 equations creates priority: narrowing/broadening a classical covering set and recomputing the same 73 is parameter substitution, and a timestamp/failed search does not establish priority. Originality FAIL. value: Even taken as correct, the scoped 3-identity threshold is not independently worth retrieving. The object M is arbitrary: DRAFT admits it is NOT the exhaustive Mordell(1967)/Ionascu-Wilson/Salez list (Salez proves 7 modular equations are complete for degree-1 prime polynomials; Elsholtz-Tao Prop 1.9 lists 4+3 polynomial families), but 3 hand-picked identities. Proving incompleteness of an arbitrarily narrowed subset does not separate parametric power from the full 1948 conjecture and does not tell identity-designers where new ideas must engage — a broader frozen list (e.g. adding 3t-1 or the other 4 Salez equations) changes/covers 73. The invariant p*=73 is the least prime 1 mod24, mechanically implied by the classical reduction, not a previously unknown/motivated constant a future researcher would need as 'least failure of this exact 3-set.' This is textbook restatement (1-mod-24 reduction) + arbitrary scope + certification of an unexplained narrow datum. Per value instructions, certification alone does not rescue an arbitrary object, and narrow exact data are valuable only when object/invariant were motivated before computation, not known/mechanically implied, and reasonably needed later — none holds here. Hence value FAIL.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Scoped to the frozen 3-identity core, not the exhaustive Mordell/Ionascu-Wilson/Salez congruence-specific lists; a broader frozen family could cover 73. Originality claimed only for this frozen-core boundary plus reusable elimination template. Existence at 73 is classical; novelty is proved non-coverability by M.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
