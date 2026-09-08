# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Minimal no-show + monotonicity witness with dual power-index gap
## 6-voter weighted game at a Penrose-window quota

**Game.** $n=6$, weights $w=(6,5,4,3,2,1)$, total $W=21$,
absolute quota $Q=12$, i.e. normalized quota $q=12/21=4/7\approx 0.571\in[0.50,0.65]$.
**Election rule.** Weighted instant-runoff on three candidates $\{A,B,C\}$:
if some candidate has strictly more than half the cast weight it wins outright;
otherwise the uniquely lowest first-place total is eliminated and its ballots
transfer to the higher-ranked survivor (all tallies below are tie-break-free,
so no tie-breaking rule is ever invoked).

**Ballot profile $P$.**

| voter | weight | ranking |
|---|---|---|
| 0 | 6 | $A\succ B\succ C$ |
| 1 | 5 | $B\succ A\succ C$ |
| 2 | 4 | $C\succ A\succ B$ |
| 3 | 3 | $B\succ A\succ C$ |
| 4 | 2 | $C\succ A\succ B$ |
| 5 | 1 | $C\succ A\succ B$ |

**Full outcome.** First-place totals $A{:}6,\;B{:}8,\;C{:}7$ (all distinct;
unique minimum $A$ eliminated). Runoff $B$ vs $C$: voter 0's $A$ ballots go to
$B$, giving $B{:}14,\;C{:}7$. Winner: **$B$**.

## Theorem (no-show paradox, tie-break-free)

With the profile above, voter 4 (weight 2, ranking $C\succ A\succ B$)
obtains a strictly preferred outcome by abstaining: if voter 4 does not vote,
first-place totals are $A{:}6,\;B{:}8,\;C{:}5$ (distinct; $C$ eliminated) and
the runoff $A$ vs $B$ is $A{:}11,\;B{:}8$. Winner: **$A$**.
Since voter 4 ranks $A\succ B$, abstaining strictly improves the outcome
($B\to A$). All first-place totals and both runoffs are strict (no ties), so
the conclusion uses no tie-breaking.

## Theorem (upward-monotonicity failure on the same profile)

Starting from the same profile (winner $B$), if voter 4 raises $B$ one step,
$C\succ A\succ B\;\mapsto\;B\succ C\succ A$ (so $B$ moves from last to first),
the new first-place totals are $A{:}6,\;B{:}10,\;C{:}5$ ($A$ eliminated) and
the runoff $B$ vs $C$ is $B{:}10,\;C{:}11$. Winner: **$A$**.
More support for $B$ turned $B$ from winner into loser: weighted IRV violates
upward monotonicity at the same weights and profile (again with all tallies
strict, hence tie-break-free).

## Theorem (exact dual power-index gap vs the Penrose estimate)

For $[w;Q]=[6,5,4,3,2,1;12]$, exact enumeration over all $2^6=64$ coalitions gives
swing counts $(17,13,11,7,5,3)$ (total $56$), i.e. normalized Banzhaf

$$\beta=(17/56,\;13/56,\;11/56,\;1/8,\;5/56,\;3/56).$$

The subset-pivot formula (cross-checked by $6!=720$ permutation enumeration) gives

$$\phi=(19/60,\;7/30,\;1/5,\;7/60,\;1/12,\;1/20),\qquad\sum\phi_i=1.$$

Let $p_i=\sqrt{w_i}/\sum_j\sqrt{w_j}$ be the Penrose square-root share.
Rigorous bounds $r/10^8\le\sqrt{m}\le(r+1)/10^8$ with $r=\lfloor10^8\sqrt m\rfloor$
(isqrt certificate) confine $p_0$ to $[0.2261382,0.2261383]$. Hence

$$|\beta_0-p_0|\ge 0.077>1/25,\qquad |\phi_0-p_0|\ge 0.090>1/25,$$

certified in exact rational arithmetic (see `artifacts/verify_witness.py`).
So **both** indices deviate from the Penrose estimate by more than the stated
rational threshold $1/25$ at voter 0 (gaps $\approx 0.077$ and $\approx 0.091$).

After voter 4's abstention the 5-voter game $[6,5,4,3,1;12]$ (same absolute
quota) has swing counts $(7,7,5,5,1)$ (total $25$),

$$\beta'=(7/25,7/25,1/5,1/5,1/25),\quad
  \phi'=(17/60,17/60,1/5,1/5,1/30),$$

so the abstention also has an exactly documented power-index footprint
(the lightest remaining voter drops to Shapley value $1/30$).

## Remarks on scope and honesty

- A bare absolute-quota Yes/No referendum cannot exhibit a no-show paradox
  (adding a Yes vote never flips Yes$\to$No and vice versa); the paradox
  therefore lives in the weighted IRV election conducted with the same
  weights and a majority quota in the Penrose window. This is stated openly;
  the power-index half of the certificate is computed on the underlying
  weighted voting game $[w;Q]$.
- Exhaustive search over all $6^6=46656$ strict profiles on these weights
  shows $672$ profiles with a tie-break-free beneficial abstention, of which
  $192$ profiles additionally carry a tie-break-free upward-monotonicity
  failure; the profile above is one explicitly checked instance. The
  "no-tie" qualification is machine-checked, not hand-waving.
- Reproduce everything with: `python3 output/artifacts/verify_witness.py`
  (stdlib only; prints `ALL-OK`).

## Lemma (why the referendum reading cannot work — recorded to avoid overclaim)

For a fixed absolute quota, if $Y$ is the Yes-weight and $W$ the cast weight,
the outcome is $Y\ge qW$. An abstaining Yes-supporter restores $(Y+w_i,W+w_i)$,
and $Y\ge qW\Rightarrow Y+w_i\ge q(W+w_i)$; an abstaining No-supporter restores
$(Y,W+w_i)$, and $Y<qW\Rightarrow Y<q(W+w_i)$. Hence abstention never helps in
a quota referendum — the witness must use the runoff/transfer rule, as done here.
