# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# A certified finite extra-relator quotient in a small-exponent triangle window

## Claim
Let `T(3,4,5) = <a,b | a^3 = b^4 = (ab)^5 = 1>` (hyperbolic baseline:
`1/3+1/4+1/5 = 47/60 < 1`, infinite by the classical triangle trichotomy) and let

```
G = G(3,4,5;2) = <a,b | a^3 = b^4 = (ab)^5 = [a,b]^2 = 1>.
```

**Theorem.** `|G| = 360.` The group is presented by four relators, is perfect
(trivial abelianization), has center of order 1, generator orders
`|a| = 3`, `|b| = 4`, `|ab| = 5`, element-order distribution
`{1:1, 2:45, 3:80, 4:90, 5:144}`, conjugacy-class sizes
`[1, 40, 40, 45, 72, 72, 90]`, and satisfies `G/[G:<a>]` index equation
`360 = 120 x 3`. Hence `G` is a proper finite quotient of the infinite
baseline `T(3,4,5)`.

## Evidence (machine-checkable, committed integers)
- `output/artifacts/cert_G345k2.json`: closed coset table over the trivial
  subgroup as explicit permutations `pa, pb` of `{0..359}` (Todd–Coxeter: 402
  definitions, 618 passes). The four defining relators close at all 360 points
  (1440 traces) and the action is transitive, so the table proves `|G| = 360`.
- `output/artifacts/verify_G345k2.py` (stdlib only, imports nothing project-side):
  checks V1 permutations, V2 relator closure, V3 transitivity, V4 generator
  orders, V5 RS index equation, V6 structure file. All six pass in seconds:
  `python3 output/artifacts/verify_G345k2.py`.
- `output/artifacts/tc.py`: from-scratch HLT Todd–Coxeter engine plus independent
  certificate checker (no GAP/Magma/SmallGroups); validated on A5/A4/trivial
  controls and correct non-termination on the infinite `C2*C3` control.
- `output/artifacts/rs_index_check_G345k2.json`: independent Todd–Coxeter over
  `H = <a>` terminates at index 120; with `|<a>| = 3` this cross-validates
  `N = 360`.
- `output/artifacts/structure_G345k2.json`: BFS order 360, class sizes, center,
  element orders.
- Sibling finite certificates in the same window (same method, checked):
  `G(3,3,4;2)` of order 12, `G(3,3,5;2)` of order 3, `G(3,3,6;2)` of order 144,
  `G(3,4,4;2)` of order 240, `G(3,3,4;3)` of order 504.

## Separation from the baseline
The committed permutations satisfy the three baseline relators
`a^3 = b^4 = (ab)^5 = 1`, so `G` is a quotient image of `T(3,4,5)`; since
`|G| = 360` is finite while `T(3,4,5)` is infinite (classical hyperbolic case),
`G` is a proper finite quotient, as required.

## Census context and limitations
- All 76 presentations (19 hyperbolic triples x `k = 2..5`) were enumerated with a
  1500-coset cap: exactly the six tuples above closed; the remaining 70 did not
  terminate at this cap and are reported as inconclusive at that cap — no
  infiniteness claim is made for any of them.
- Baseline infiniteness is cited classical background (Fuchsian trichotomy), not
  re-proved here.
- No isomorphism identification (e.g. with any named group of order 360) is
  claimed; the order-360 numerical match is noted only as an observation.
- Novelty statement: the admission triage found no prior closing this
  commutator-power window with a coset-table certificate; this report supplies
  the terminating table plus replay files. Independent literature verification
  beyond that triage was out of scope for this pass.
