# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** dP1 nodal-boundary chamber: wall-crossing across an irreducible nodal anticanonical divisor
- **Round:** 2026-09-07-first-light-01
- **Lane:** 838
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Enumerative Geometry
- **Method:** tropical scattering-diagram wall-crossing with mirror cluster theta-function comparison

## Problem

For X=dP1 with irreducible nodal rational anticanonical divisor D_nod, compute the one-node scattering diagram to order 1 at one named joint and decide: does the unbounded-wall function encode the genus-0 maximal-tangency invariant N_{-K} (contact order w=1, tangency away from node) as the mirror theta coefficient, or does the node force a corrected wall?

## Attempted claim

For (dP1, D_nod) at class beta=-K_X with contact order 1 away from the node, the order-1 consistent diagram has unbounded-wall function f_out = 1 + N_{-K} z^{m_out} (times known node monomial), equating the log invariant to the theta coefficient; alternatively the joint exhibits an explicit named node-correction factor that must be added for consistency.

## Research outcome

Decided the dP1 nodal-boundary order-1 joint: identity f_out = 1 + 11 t z^{m_out} for the transverse (base-pointed) invariant, with explicit named node-exclusion correction; general-point invariant shown to vanish with recorded shift.

## Why this attempt failed

Failed axes: correctness, value.

correctness: Classical pencil lemmas 1-3 are correct: h0(-K)=2 by RR+Kodaira (chi=2), base point p0 mult 1 from (-K)^2=1, node!=p0 and all fibers smooth at p0 with transverse meeting at p0 from D.C=1 (mult>=2 would give i>=2>1), e(X)=11 e(Y)=12 so 12 singular fibers, 12xI1 for general 8 points by Persson-Miranda, minus D itself leaves 11 transverse fibers meeting D at p0. Script replay VERIFY_OK checks only arithmetic. Lemma 4 set-theoretic vanishing Ngen=0 is essentially correct under transverse (image-not-in-D) definition but proof omits reducible/contracted-domain exclusion (fixable by -K ampleness: (-K).beta=1 forbids >=2 non-contracted components; contracted tail at p!=p0 cannot attach to fiber C with C cap D={p0}). Lemma 5 set-theoretic enumeration of 11 normalizations is correct but virtual contribution +1 each is asserted, not proved: no log deformation/obstruction computation, no proof of rigidity/smoothness of 0-dim log moduli, automorphism discussion incomplete. Lemma 6 (scattering) is unproved: the premise 'each I1 fiber contributes one initial wall f_i=1+t z^{m_i} with all m_i parallel = m_out, node slab f_node=1+t z^{m_D} commuting mod t^2, focus-focus M=[[1,1],[0,1]] fixing m_out' is assumed, not derived from Gross-Hacking-Keel / Gross-Siebert / Auroux. Those citations do not state an I1-fiber-to-initial-wall rule; GHK initial diagram comes from toric model, not elliptic pencil fibers. Given the assumed inputs, consistency mod t^2 is automatic ((1+u)^11=1+11u mod u^2, cross terms O(t^2)), so no wall-crossing content is proved. The named 'node-exclusion correction C=-t z^{m_D}' is elementary subtraction 12-1, not a KS-computed correction, and the claimed parenthetical node monomial =1 is asserted via M m_out=m_out without proving M or m_out. Hence the headline scattering-theta identity f_out=1+11 t z^{m_out} equating log invariant to theta coefficient is assumed, not proved. Classical part proved; mirror part assumed. Distinguishing proof from assumption, correctness FAILS. value: Even taking enumerative counts at face value, the headline is textbook restatement + trivial mod-t^2 algebra, not an independently retrievable mirror result. 12 nodal members of pencil of cubics through 8 points (rational elliptic e=12, 12xI1) is standard elliptic-surface textbook; 11=12-1 is mechanical subtraction; Ngen=0 is immediate from D.C=1; (1+u)^11=1+11u mod u^2 and commutation mod t^2 are automatic. The scattering layer adds no computed content beyond assuming 11 parallel slabs. Moreover the identity is salvaged by redefining the invariant: the standard maximal-tangency invariant (general/unspecified contact point away from node) vanishes (Lemma 4: 0), while the wall shows 11; draft equates wall to ad hoc base-pointed count Nbp at p0 (the pencil base point) and records +11 shift. This does not decide the target structural question for the standard invariant — it shows mismatch 11 vs 0 repackaged as success. The node-exclusion is not a wall-crossi…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Order 1 (mod t^2) only; standard I1-slab input assumed from GHK/GS machinery; general 8 points (12xI1) required; N^{gen}=0 vs N^{bp}=11 distinction honestly recorded.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
