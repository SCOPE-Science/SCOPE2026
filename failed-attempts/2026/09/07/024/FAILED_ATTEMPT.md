# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact Alabama-Paradox Census for the Five-State House-18 Stratum: Hamilton versus Jefferson/Webster/Huntington-Hill with Minimal Witness and Quota Certificates
- **Round:** 2026-09-07-first-light-01
- **Lane:** 34
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Social Choice Theory
- **Method:** exact quota-method comparison with house-monotonicity verification and population-symmetry reduction

## Problem

Close the 5-state house-18 Alabama stratum. Enumerate canonical population vectors S = {p in Z^5: 30>=p1>=p2>=p3>=p4>=p5>=1, gcd(p)=1} (118755 raw combos with replacement, primitive subset), compute Hamilton largest-remainder apportionments at H=18 and H=19 with exact rational quotas, flag Alabama violations a_i(19)<a_i(18) for some i, and recompute Jefferson (floor/D'Hondt), Webster (arithmetic-mean/Sainte-Lague) and Huntington-Hill (geometric-mean) divisor apportionments at H=18,19 with exact integer-arithmetic rounding certificates, all quotiented by S5 permutation symmetry.

## Attempted claim

Exact census integer N_18 = number of canonical vectors in S exhibiting an Alabama paradox under Hamilton from H=18 to H=19, plus an explicit minimal witness p* in S with full tables: Hamilton quotas/remainders/seats at 18 and 19 showing a seat loss for some state, and Jefferson, Webster and Huntington-Hill divisor apportionments at 18 and 19 showing house-monotonicity (no loss) with divisor and rounding-inequality certificates and quota-compliance checks.

## Research outcome

Exact 5-state house-18 Alabama census closed: N_primitive=264463, N_18=13343, minimal witness p*=(4,4,1,1,1) P=11 with Hamilton 6-6-2-2-2 -> 7-7-2-2-1 (state 4 loses 2->1) and Jefferson/Webster/HH house-monotone certificates; stratum-wide divisor monotonicity 0 violations; full agreement matrix; paradox-free prefixes max<=3 and P<=10; ~15s stdlib-only rerun with independent verifier.

## Why this attempt failed

Failed axes: value.

value: Even though correct and narrowly new, result as stated is not independently worth finding later. The headline count N_18=13343 is an artifact of arbitrary box [1,30], S5-quotient, primitive filter and index tie-break (DRAFT Sec.7 admits counts are rule-relative and boundary vectors move with tie-break). Box cutoff chosen for <60s rerun (fallback to max<=20 shows negotiability), not principled applied or theoretical boundary; real populations are not 1..30. No formula, asymptotic, or structural explanation for 13343, histogram, or agreement percentages (Ham-Web ~88.5% vs Ham-Jeff ~45% tabulated without insight). Distribution note max==5 gap (69 primitive, 0 Alabama) explicitly computed-only with no general explanation offered. Stratum-wide divisor 0 violations is Balinski-Young theorem instantiated by prefix construction (highest-averages from zero guarantees monotonicity by definition), not discovery. Minimal witness (4,4,1,1,1) is stratum-relative minimality (least (max,lex) for n=5 H=18->19) with box-independent prefixes max<=3/P<=10, but Alabama phenomenon itself is textbook; another small instance in an arbitrary (n=5,H=18) slice is mere parameter substitution, and DRAFT admits no new paradox theorem and no priority claim. A future teacher/researcher would not independently search for this exact box count. Analogous to prior SCOPE value REJECTs (RT(30,K4,6) SAT number, M22 4x4 Nash count, order-96 subgroup maxima): narrow-slice brute-force enumeration with witness but without insight. Hence textbook phenomenon + arbitrary-slice enumeration + unexplained numbers = value failure.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Fixed stratum only (n=5, H=18->19, box [1,30], S5-quotiented, index tie-break; counts are rule-relative). Divisor methods via highest-averages + weak-optimality characterization. HH H19 on p* needs irrational d=sqrt(8/21), certified by squared-integer ledger not Fraction d. No scholarly-priority claim beyond topic.json triage (web probes failed there). Max==5 zero-Alabama gap is computed-only, unexplained.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
