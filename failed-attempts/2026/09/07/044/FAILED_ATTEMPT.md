# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A checkable rational-Dulac nonexistence box for a cubic Lienard family where classical Bendixson fails
- **Round:** 2026-09-07-first-light-01
- **Lane:** 85
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Ordinary Differential Equations
- **Method:** explicit rational Dulac function with cleared-denominator polynomial audit

## Problem

For the cubic Lienard family x' = y - (x^3 + b*x^2 + a*x), y' = -x with (a,b) in the box A = [1.1,1.2] x [1.9,2.0], prove with the explicit Dulac function B(x) = (1+2*x^2)^(-2) that div(B*X)/B =: M(x;a,b) <= -1/20 for all real x and all (a,b) in A, by clearing denominators to four explicit vertex quartics and verifying each via exact Sturm/SOS plus interval subdivision; conclude zero closed orbits in R^2 for the whole box.

## Attempted claim

For every (a,b) in [1.1,1.2] x [1.9,2.0], the system x' = y-(x^3+b*x^2+a*x), y' = -x has no periodic (closed) orbits in R^2: with B(x)=(1+2*x^2)^(-2), div(B*X)/B <= -1/20 uniformly in (x,a,b). Corollary: (0,0) is the unique equilibrium and a locally asymptotically stable focus; the box is a certified zero-limit-cycle patch inside the region where the B=1 Bendixson test is inconclusive.

## Research outcome

The assigned Dulac margin (B=(1+2x^2)^-2, div/B<=-1/20 uniformly) is FALSE: the audit derivation drops the y-term and flips a sign; exact counterexample gives +59/2, and a lemma rules out every x-only weight on R^2. The intended nonexistence corollary is TRUE and proved by a classical energy function V=(x^2+y^2)/2 with uniform decrement <=-(1/10)x^2, yielding zero closed orbits and GAS of the origin over the whole box. All identities are exact-rational/symbolic and replayed by a stdlib+sympy script.

## Why this attempt failed

Failed axes: originality, value.

originality: No substantive new mathematical object or method versus prior literature. (1) Rescue Theorem 2 is immediate textbook Lyapunov: V=(x^2+y^2)/2, Vdot=-xF=-x^2(x^2+bx+a) with x^2+bx+a>=a-b^2/4. Over A max(b^2-4a)=4-4.4=-0.4<0, so positivity holds with large margin; this is the standard xF(x)>0 exercise in Khalil/Perko/Strogatz and classical Lienard theory (Massera/Rychkov/Cherkas uniqueness). Fixing the numeric box [1.1,1.2]x[1.9,2.0] is a parameter substitution inside the open region {a>b^2/4}. (2) Theorem 1 + Lemma only refute the lane-internal unpublished audit-plan formula M (dropped y-term, flipped sign) and observe the one-line consequence that B(x)-only weights retain a y-term; this corrects no published prior claim from Gasull-Giacomini 2013/2021, Cherkas-Sidorenko 2008, or extended Dulac literature, and the Lemma follows immediately from div(BX)=B'(y-F)-BF'. Draft itself concedes energy argument is classical, not original. Hence no originality delta worth priority. value: Not independently worth finding later. Result is a textbook restatement (standard energy + LaSalle) evaluated at an arbitrary tiny box plus arithmetic exposure of an internal sign error. It provides no reusable weight, no new nonexistence phenomenon, no family-wide bound, and no method beyond completing the square and integrating Vdot around a putative cycle. The box is unmotivated except as the failure spot of the flawed plan; the same one-line proof covers the entire open slab a>b^2/4. A correction log for an unpublished derivation is not a retrievable research record. Falls squarely under rejectable categories: textbook restatement, mere parameter substitution, tiny unmotivated gain.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The rescue (energy + LaSalle) is classical, not a novel method; claimed only as a corrected certificate. LaSalle's invariance principle is cited (Khalil Thm 4.4), not re-proved; the no-cycle integral argument itself is proved in full. No claim outside box A, no new Dulac weight, no cycle-count bound beyond zero. Originality delta is the explicit refutation + certified replacement over this lane's box.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
