# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Twist-stable Khovanov thickness with linearly growing Jones span in single-region extensions of 9_42
- **Round:** 2026-09-07-first-light-01
- **Lane:** 147
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Knot Theory
- **Method:** Kauffman-bracket skein recurrence plus Turaev-genus width bound with base cube anchoring and skein propagation

## Problem

Let D_m be the prime-knot family obtained from the 9_42 seed diagram by lengthening a single designated twist region through m=1,3,5,7,9 extensions (crossings 9, 11, 13, 15, 17). Prove by Kauffman-bracket skein recurrence that Jones span grows linearly as span(D_m)=6+k with constant deficit, certify Turaev genus exactly 1 for all D_m, and prove Khovanov homological width is exactly 3 for every member by base cube-anchored off-diagonal support propagated through the skein long exact sequence.

## Attempted claim

For the single-twist-region extension family D_m of the 9_42 seed (crossings 9, 11, 13, 15, 17): (a) the Kauffman-bracket skein recurrence yields Jones span span(D_m)=6+k growing linearly with added twists at constant deficit; (b) every D_m has Turaev genus exactly 1, hence Khovanov width at most 3; (c) logged base cube computations plus skein exact-sequence propagation certify width exactly 3 for all members, giving a proved infinite span-growth/width-persistence decoupling sequence replayable from the seed diagram plus insertion rule alone.

## Research outcome

Consolidated the interrupted attempt into a meaningful partial theorem: a machine-verified single-component + Turaev-genus-1 + bracket-span-bound table for five 9_42 twist extensions (9-17 crossings), a KnotAtlas-anchored exact width-3 seed certificate, and a conditional skein-LES width-persistence lemma, with two prior-script interpretation errors (component doubling, span-vs-bound) explicitly corrected and all exact-span/width conclusions honestly conditioned on stated hypotheses.

## Why this attempt failed

Failed axes: correctness, value.

correctness: Target requires: (a) exact Jones spans span=6+k (later corrected to 8+2j) by skein recurrence, (b) Turaev genus exactly 1 for all D_m, (c) width exactly 3 for all five via base cube + LES propagation, replayable from seed+rule without archives. DRAFT honestly retreats: unconditional result is only single-component diagrams of diagram-genus 1 with bracket-span UPPER bounds 8,10,12,14,16 and width<=3; exact spans and exact widths beyond seed are conditional on unverified H1 (adequacy) + H2 (no cancellation) and stated as Conjecture 4.3. Reruns confirm the unconditional fragment: verify_family.py + verify_corrections.py reproduce sA=4,6,8,10,12, sB=5, genus (c+2-sA-sB)/2=1, bracket spans 32,40,48,56,64, directed cycles [2c,2c] = one undirected component, PD-valid. Bound reading is proved by seed: bound 8 vs KnotAtlas true span 6. But essential headline inferences fail: no exact Jones for D1-D4; no Kh cube beyond seed; knot (not diagram) genus exactly 1 unproved (only <=1); primeness/crossing-minimality unproved; Lemma 4.1 even conditionally unproved - DRAFT admits 'full bigrading-shift arithmetic is logged as conjecture-level schema, not a line-by-line verified LES computation' with unsupported claim that resolved twist links are thin and third term misses witness bigrading; seed width exactly 3 cites live KnotAtlas table rather than independent logged cube, violating seed+rule-only replay. Distinguishing proof from conjecture does not supply the missing proofs. value: Proved fragment alone is not independently worth retrieving. What is rigorously established is: five site-0 twist diagrams are single-component, diagram-genus 1 (hence knot genus <=1, width <=3), with non-sharp bracket upper bounds growing +2 per pair, plus re-citation of already-published seed width 3. Bounds are not exact invariants - seed proves strictness (8 vs 6) - so linear growth of bounds does not establish span growth or span/width decoupling, the motivated question (whether span growth forces width growth, where width<=genus+2 is sharp). No new exact order, span, width beyond seed, presentation, or witness is proved for D1-D4; 13/15/17 rows are new only as diagram statistics for an ad-hoc twist site, i.e. unexplained enumeration. Certification (PD-validity, state counts 512-131072, C1/C2 corrections) does not rescue arbitrary object/unexplained number. Admitted fallback (verified exact spans + width exactly 3 at 9-15 with two rows beyond tables) is also not delivered - spans remain bounds, widths beyond seed remain conditional. Exact headline, if proved, would be valuable, but value requires a proved retrievable fact, not a conjectured one. Hence missing substantive result / intrinsic low value of what remains.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Exact Jones spans for D_1..D_4 not computed (claimed formula corrected to conditional conjecture with intercept 8, not 6+k); exact width 3 beyond the seed is conditional on unverified adequacy H1 and cancellation H2 hypotheses (no LES naturality log or Kh cube at 11-17 crossings); primeness and crossing-minimality of extended diagrams unproved; 13/15/17 rows are new computed bounds data, not exact table entries.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
