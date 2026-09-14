# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Lebesgue-Nagell census for D=209 closing 5-divisible gap
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1872
- **Disposition:** AUDIT_2_REJECT
- **Domain:** number theory
- **Method:** Bilu-Hanrot-Voutier plus Thue and S-integral points

## Problem

Let D = 209 = 11 * 19, which is odd composite and squarefree. Determine with proof all integer triples (x, y, n) with n >= 3, y > 1 and gcd(x, y) = 1 satisfying x^2 + 209 = y^n. A complete answer is an explicit finite list of all such triples up to the sign of x, together with a rigorous proof that no other integer triple with n >= 3, y > 1 and coprime x, y satisfies the equation.

## Attempted claim

Let D = 209 = 11 * 19, which is odd composite and squarefree. Determine with proof all integer triples (x, y, n) with n >= 3, y > 1 and gcd(x, y) = 1 satisfying x^2 + 209 = y^n. A complete answer is an explicit finite list of all such triples up to the sign of x, together with a rigorous proof that no other integer triple with n >= 3, y > 1 and coprime x, y satisfies the equation.

## Research outcome

Complete Lebesgue-Nagell census for D=209 proved: unique coprime solution (54,5,5) with full case closure.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET proof of complete census fails at the p=5 gap it claims to close. Sections 1-2 verify: parity/y-odd, coprime ideals via ramified prime above 2, p=3 impossibility, even-n factor pairs (104,105),(4,15) non-powers, killer moduli for p=7..29 independently re-verified empty over all residues, and BHV reduction to p<=29 is legitimate modulo Lucas-pair check. Fatal gap: (x+s)=a^5 with 5|h=20 gives [a]=[P]^r, but writing (x+s)=eps*g^5*beta^k with integral g=u+vs and reducing to H_k(u,v)=+-1 assumes g in O. When r>t=v_5(y), g is fractional (v_P(g)=t-r<0); denominators require S-integral/Thue-Mahler H_k=+-5^e analysis, never done. Thus H_2..H_4=+-1 integral emptiness does not rule out fractional classes, and t=0/r!=0 cases are uncovered. The 'k mod 5 absorbs quotient' note does not prove integrality. Separately, the artifact claim qfbsolve(Qfb(1,0,209),5^j)=[] for j<=4 is false: 25=5^2+209*0^2 and 625=25^2+209*0^2 are solutions, confirmed by enumeration. PARI thue evidence therefore covers only the integral subcase; full uniqueness is unproved.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: BHV primitive-divisor bound invoked as standard reduction to p<=29 with Lucas-pair non-degeneracy certified in s8; PARI bnfcertify and thueinit/thue trusted as certified solvers; brute-force scan to 2e5 is supporting evidence only and the proof does not depend on any search bound.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
