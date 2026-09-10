# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Interacting-cycle resurgence witness for the theta cell Theta(2,3,3): rho >= 4/3 via minimal non-containment
- **Round:** 2026-09-07-first-light-01
- **Lane:** 615
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Commutative Algebra
- **Method:** prime-avoidance containment comparison with extremal Waldschmidt-divisor isolation and Betti-splitting membership check

## Problem

Decide interacting-cycle resurgence for the named non-cactus flag cell Theta(2,3,3) via prime-avoidance containment comparison: exhibit a minimal monomial non-containment witness in J^{(4)} \ J^3 pinning rho(J(Theta)) >= 4/3 and isolating the extremal Waldschmidt divisor, or settle the weaker (6,5) interaction test while the cell stays open.

## Attempted claim

Let Theta = Theta(2,3,3) be the theta graph on vertices {a,b,p,q1,q2,r1,r2} with edges a-p,p-b,a-q1,q1-q2,q2-b,a-r1,r1-r2,r2-b, and J(Theta) its vertex cover ideal. Then rho(J(Theta)) >= 4/3, witnessed by an explicit minimal monomial w in J(Theta)^{(4)} \ J(Theta)^3 isolating the extremal Waldschmidt divisor.

## Research outcome

TARGET proved: explicit minimal monomial w=a*b*p^3*q1^3*q2^3*r1^3*r2^3 lies in J(Theta(2,3,3))^(4) but not in J^3 (exact exhaustive check), forcing resurgence >=4/3.

## Why this attempt failed

Failed axes: correctness, value.

correctness: Headline is FALSE. Independent re-enumeration over all 128 subsets confirms 27 vertex covers, but finds 7 inclusion-minimal covers, not 6: the draft omits C7 = {p,q1,q2,r1,r2}, exponent (0,0,1,1,1,1,1), of size 5. C7 is a genuine vertex cover (p covers a-p,p-b; q1 covers a-q1; q2 covers q2-b; r1 covers a-r1; plus internal edges) and is inclusion-minimal (deleting p uncovers a-p; deleting q1 uncovers a-q1; deleting q2 uncovers q2-b; deleting r1 uncovers a-r1; deleting r2 uncovers r2-b). The draft's claim 'every minimal cover meets {a,b}' and 'it suffices to test minimal covers' with only the six size-4 covers is therefore wrong: the size-5 cover is a minimal generator of J(Theta). With the full 7-generator set, the witness w=(1,1,3,3,3,3,3) IS in J^3: C1+C7+C7 = (1,1,0,1,0,1,0)+2*(0,0,1,1,1,1,1) = (1,1,2,3,2,3,2) <= w coordinatewise, i.e. w = C1*C7*C7*p*q2. The committed verifier only tested the 6 incomplete generators (216 triples), so its 'dividing_triples=0' is an artifact of the truncated generator list; with all 7 generators 25 of 343 ordered triples divide w. Stronger: exhaustive enumeration of all 6067 exponent vectors in [0,4]^7 satisfying edge sums >= 4 shows every one lies in J^3 under the full generator set (0 outside). The capping argument extends this to ALL monomials: for any e with edge sums >= 4, e'_i=min(e_i,4) still has all edge sums >= 4 (capped coordinate contributes 4), lies in the checked box hence in J^3, and divides x^e, so x^e in J^3. Thus J^(4) subseteq J^3 is proved, and no (4,3) witness exists at all. Parts (i) (edge sums) and (iii) (coordinate-minimality) of the draft Theorem are correct as stated, but part (ii), the load-bearing non-membership claim, is false, so rho >= 4/3 via this witness fails. The alpha ladder values (4,7,11,14,18,21) re-verified correctly but do not rescue the containment claim. value: The submitted headline, if true, would have met the admitted value case (first interacting-cycle witness attaining the chromatic bound). But correctness audit proves J^(4) subseteq J^3, so the claimed non-containment witness does not exist and the rho >= 4/3 lower bound is not established by this work. A refuted headline has no retrievable value under its stated form. The audit's own verified containment fact (J^(4) subseteq J^3 for this cell) is a different headline from the submitted one, was not claimed, motivated, or interpreted in the draft, and cannot be substituted as value for the rejected claim. No independently valuable exact headline survives in the submission as written.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Proves the TARGET lower bound rho>=4/3 only; exact equality rho=4/3 additionally uses the standard chromatic upper bound, cited not proved. Exhaustive-search certificate on 7 variables, not a general structural decomposition. Field-independent monomial-lattice argument.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
