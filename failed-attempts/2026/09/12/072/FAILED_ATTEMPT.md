# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Holonomy height 3 versus complexity 1 in degree 7
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1234
- **Disposition:** AUDIT_1_REJECT
- **Domain:** finite semigroup theory
- **Method:** holonomy decomposition with wreath divisor and flow obstruction

## Problem

Let (Q,S) be a faithful finite transformation monoid with |Q| <= 7, given by an explicit generating set of maps closed under composition. Let its holonomy height be the number of levels in the Eilenberg holonomy decomposition containing a nontrivial permutation group, and let c(S) in {0,1,2} be its Krohn-Rhodes group complexity. Does there exist such a (Q,S) whose holonomy height equals 3 while c(S) equals 1? A complete answer is either (i) one explicit (Q,S) with its computed holonomy skeleton, all holonomy permutation groups, an explicit divisor embedding certifying S divides A wr G wr B for finite aperiodic A,B and finite group G, and a certified obstruction proving S does not divide any finite aperiodic monoid, or (ii) a proof that no transformation monoid with |Q| <= 7 and holonomy height 3 has complexity 1.

## Attempted claim

Let (Q,S) be a faithful finite transformation monoid with |Q| <= 7, given by an explicit generating set of maps closed under composition. Let its holonomy height be the number of levels in the Eilenberg holonomy decomposition containing a nontrivial permutation group, and let c(S) in {0,1,2} be its Krohn-Rhodes group complexity. Does there exist such a (Q,S) whose holonomy height equals 3 while c(S) equals 1? A complete answer is either (i) one explicit (Q,S) with its computed holonomy skeleton, all holonomy permutation groups, an explicit divisor embedding certifying S divides A wr G wr B for finite aperiodic A,B and finite group G, and a certified obstruction proving S does not divide any finite aperiodic monoid, or (ii) a proof that no transformation monoid with |Q| <= 7 and holonomy height 3 has complexity 1.

## Research outcome

Explicit degree-7 monoid with 53 elements, holonomy height 3 (three C2 levels), and complexity exactly 1, fully machine-certified.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: audited normally against the admitted target; no value presumption applies. Independently recomputed from the three generators (right-action convention (f*g)(i)=g(f(i))): monoid closure has exactly 53 elements including identity; generator a satisfies a^2=id with a!=id and is the unique non-identity involution (15 elements are non-aperiodic witnesses), so c(S)>=1 is proved. Image sets: 21; mutual-subduction classes: 7 with the stated membership; bricks/stabilizer/permutation checks confirm nontrivial holonomy groups C2 at reps {0,2}, {0,6} and top Q (7 singleton bricks), all others trivial, so holonomy height exactly 3 is verified. BUT the complexity upper bound c(S)<=1 via claimed division S | U2 wr C2 wr U2 (972 elements on 8 states) is mathematically invalid: the certificate supplies only pointwise per-(generator,state) wreath elements w(g,q) with w(phi(q))=phi(g(q)), whereas transformation-semigroup division requires ONE uniform w_g per generator with w_g(phi(q))=phi(g(q)) for ALL q simultaneously (even for a Tilson relational morphism with singleton fibres). Exhaustive audit proves the stated route impossible: for phi(q)=q+1, each generator has 0 uniform covers in W; over ALL 20160 injective maps Q->X(8) zero admit simultaneous uniform covers for all three generators; over all 8^7 maps zero non-constant maps admit them. The verify.py 'word-lift consistency' check (following q-dependent covers along words) does not entail a divisor morphism and is unsound: pointwise covers exist trivially whenever W is transitive, so it proves nothing. Hence c(S)=1 is NOT established; the headline dichotomy answer 'Yes' is unproven. Minor corroborating defect: DRAFT Table claims singleton stabilizer size 53 while certificate.json says 8 (independently recomputed value is 8). No ADMISSION_DEFECT: the target question itself is sound; the failure is in the research proof.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: The complexity upper bound relies on the standard Krohn-Rhodes theorems that transformation-semigroup division does not increase group complexity and that c(X wr Y) <= c(X)+c(Y); these are cited, not re-proved. The wreath cascade action and holonomy conventions (Eilenberg subduction/brick definitions) are fixed as documented in DRAFT.md and the verifier. No GAP/Sage was available; all enumeration is pure-Python brute force, feasible only because |S|=53 and |W|=972.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
