# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Minimal-growth right-angled Coxeter group in the 7-9 vertex window via Steinberg series and pole gap
- **Round:** 2026-09-07-first-light-01
- **Lane:** 143
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Geometric Group Theory
- **Method:** Steinberg rational growth-series computation with finite-state automaton word-count verification

## Problem

Over the surveyed pool of right-angled Coxeter groups defined by 7-9 vertex graphs, identify and certify the minimal exponential growth rate: produce one minimal-growth witness graph with its full Steinberg rational growth series, automaton word-count cross-check to length 12, and a per-graph growth table proving its rate is separated from the runner-up by a committed denominator-pole-modulus interval.

## Attempted claim

There exists a unique (up to graph isomorphism) minimal-growth right-angled Coxeter group in the surveyed 7-9 vertex defining-graph pool whose exponential growth rate, given by the reciprocal of the smallest-modulus pole of its Steinberg rational growth series, is strictly less than every other surveyed graph's rate by a committed positive pole-modulus interval, with series coefficients matching finite-state automaton word counts to length 12.

## Research outcome

Certified within-pool minimal-growth RACG witness (K8 minus adjacent edge-pair, tau=phi, Fibonacci series (1+t)^7/(1-t-t^2)) with 12/12 Steinberg-vs-automaton cross-check to length 12 and exact rational pole-modulus gap over runner-up tau=2.

## Why this attempt failed

Failed axes: value.

value: FAIL: arbitrary scope + mechanically implied datum. Pool is 12 hand-picked graphs out of ~12k (n=8) + ~274k (n=9) non-isomorphic graphs; admittedly not exhaustive over 7-9 vertices. Winner K8-minus-V (missing {0,1},{0,2}) is the join of K5 with 3-vertex single-edge graph [1,3,1]; F=-(u-1)^5(u^2-3u+1)=(1-u)^5*(1-3u+u^2), W=(1+t)^7/(1-t-t^2)=(1+t)^5 times base W=(1+t)^2/(1-t-t^2). Base already has tau=phi via textbook Steinberg+cone formula (coning multiplies W by (1+t), preserves rate). Thus exact phi/Fibonacci invariant is mechanically implied by 3-vertex textbook computation, not new to 8 vertices. Pool excludes both the smaller same-rate base (3 vertices, outside 7-9 window) and more-complete slower graphs: K8-minus-1-edge has c=[1,8,27,50,55,36,13,2] and series [1,8,29,64,99,120,127,128,128,...] stabilizing (virtually Z, rate 1, subexponential join Dinf x finite); K8-minus-2-disjoint-edges similarly rate ~1 (virtually Z^2). Hence 'minimal exponential in pool' is manufactured by excluding subexponentials and smaller same-rate graphs while padding with cone powers (TRI/C4 families share rates 2 and 1+sqrt2 across n via same (u-1)^k lift). No recognized need for minimality among this specific 12-set; future researcher needing phi RACG would use 3-vertex base, computable in seconds via Steinberg, not retrieve 8-vertex cone or gap-to-2 table. Certification (rational intervals, 12/12 automaton match) does not rescue arbitrary object/unexplained number per standard. This is intrinsic arbitrary scope / textbook cone lift / missing substantive exhaustive extremal, not a bounded presentation defect.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: ['12-graph survey pool, not exhaustive over all 7-9 vertex graphs; minimality is within-pool.', 'Automaton rule validated by 12/12 agreement + hand cases (verified computation), not a from-axioms proof.', 'Pole-to-rate step uses standard rational-series dominant-pole fact on explicit rational W(t).']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
