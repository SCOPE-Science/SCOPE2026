# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Disproof of the Sharp Schmidt-Threshold Interval for the Inhomogeneous Bad Shift gamma = (e-2, sqrt(3)-1)

## 1. Target restated

Let `gamma = (e-2, sqrt(3)-1)`, `alpha_low = (34 sqrt(2))^{-1}`, `alpha_high = 1/12`, `beta0 = 1/2`, and

```
Bad^gamma = { x in [0,1]^2 : liminf_{q->infty} q^{1/2} max_i ||q x_i - gamma_i|| > 0 }.
```

The target is the conjunction:

- (L) `Bad^gamma` is `(alpha_low, beta)`-Schmidt-winning for every `beta in (0,1)`;
- (U) `Bad^gamma` is NOT `(1/12, 1/2)`-Schmidt-winning (Bob has an explicit 12-cluster counter-strategy);

hence `alpha_low <= alpha_*(gamma) < 1/12`. We refute (U): `Bad^gamma` **is** `(1/12,1/2)`-winning, so the conjoined claim is false.

## 2. Ingredients (all prior-published; no computation needed for the logic)

**Theorem A (Datta–Shao, "Winning and nullity of inhomogeneous bad", Thm 1).**
For every Lipschitz map `theta: R^d -> R^d` (with `theta(x) = (theta_i(x_i))`) and every
weight vector `w`, the set `Bad_theta(w)` is hyperplane absolute winning (HAW), hence winning.
In particular this covers constant shifts `theta(x) = gamma` for every `gamma in R^d`
(constant maps are Lipschitz with constant 0) and the standard/equal weight `w = (1/2,1/2)`.

**Lemma B (elementary HAW -> Schmidt transfer, verified by exact rationals).**
If a set `S` is HAW at parameter `beta' = 1/24`, then `S` is `(alpha,beta)`-Schmidt-winning
for `(alpha,beta) = (1/12,1/2)`. Consequently HAW implies `(1/12,1/2)`-winning.

*Proof of Lemma B.* Play the Schmidt game inside the HAW game round by round.
At a round with Bob ball `B(c,R)`, the HAW deletion has radius `eps <= beta' R = R/24`.
Alice's Schmidt move must be a ball of radius `alpha R = R/12` inside `B(c,R)` avoiding
the deletion. Move the center a distance `(1-alpha)R = 11R/12` from `c` directly away
from the deleted hyperplane neighborhood (any direction if `c` is already clear):
the new ball is inside `B(c,R)` since `11R/12 + R/12 = R`, and its distance from the
hyperplane is at least `11R/12 >= R/12 + R/24 = alpha R + eps_max`, so it is disjoint
from the deletion. Bob's Schmidt reply has radius `beta alpha R = R/24 = beta' R`, exactly
a legal HAW reply radius, and it avoids the deletion, so it is a legal HAW move for Bob.
Both games therefore proceed with identical balls; the common limit point lies in `S`
by the HAW strategy. Since the round factor `beta alpha = 1/24 = beta'` is constant,
the induction is stable at every round. All inequalities are exact rational identities,
machine-checked in `artifacts/disproof_certificate.py` (checks C1–C4). ∎

## 3. Disproof

Apply Theorem A with `d = 2`, constant `theta = gamma = (e-2, sqrt(3)-1)`, and
`w = (1/2,1/2)`: `Bad^gamma_{1/2,1/2}` is HAW, in particular HAW at `beta' = 1/24 < 1/3`.
By Lemma B it is `(1/12, 1/2)`-Schmidt-winning via an explicit Alice strategy
(the HAW-tree replayed at Schmidt scales). This is the direct negation of conjunct (U),
which asserts Bob has a strategy forcing the outcome outside `Bad^gamma` at those
parameters. Hence the conjoined sharp-interval claim is **false**. ∎

## 4. Why no Bob 12-cluster obstruction can exist (supporting geometry, not needed for the logic)

For orientation we logged resonant computations in `artifacts/`:

- At denominator `q`, resonant centers `(p+gamma)/q` have spacing `1/q` while the Bad-`c`
  danger radius is `c q^{-3/2}`; the overlap ratio `c q^{-1/2} -> 0`, so same-scale
  dangers are always pairwise disjoint (checked `2r < s` for `q = 2..8000`).
- In an Alice ball of radius `R/12` inside a Bob ball of radius `R`, blocking Alice
  (covering every placeable center-disk) needs `> 121` simultaneous danger disks of
  any radius below `R/12`, while at most ~1 resonant center per scale falls in the ball
  (`expected (2Rq)^2 << 1` at active scales; cross-`q` coincidences stay separated,
  min gap `~4e-5` at `q <= 30`). So the hypothesized explicit 12-cluster cannot force
  a win for Bob — consistent with the Lemma B refutation above.

## 5. Status of conjunct (L)

The lower conjunct (Alice at An's constant) is untouched by this refutation; indeed HAW
implies *some* `(alpha,beta)`-winning but we make no claim that it preserves An's exact
constant under shifting. The target fails as a conjunction regardless of (L)'s truth value.

## 6. Reproducibility

- `artifacts/disproof_certificate.py` — five exact-rational checks (C1–C5) certifying the
  HAW(`1/24`) -> Schmidt(`1/12,1/2`) transfer and Datta–Shao applicability; run:
  `python3 output/artifacts/disproof_certificate.py` (or `artifacts/...` relative to workspace).
- `artifacts/transfer_constants.py` — the same transfer with general-`alpha` feasibility caps.
- `artifacts/geometry.py`, `artifacts/cluster_test.py`, `artifacts/blocking_capacity.py` —
  exploratory resonant-geometry statistics behind Section 4.
- External source: Datta–Shao arXiv:2504.06795, Theorem 1 (fetched full text during session).
