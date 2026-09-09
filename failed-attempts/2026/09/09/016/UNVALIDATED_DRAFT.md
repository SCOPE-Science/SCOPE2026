# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Selmer-conditioned rank census in the quadratic twist family of 15.a2 (|d| <= 100, signed)

## Claim (partial theorem — CLAIMED at fallback scope)

Let $E_0$ be LMFDB 15.a2 in minimal model $y^2+xy+y = x^3+x^2-135x-660$
(rank $0$, torsion $\mathbf{Z}/2 \times \mathbf{Z}/2$).
For squarefree $d$, let $E_d: y^2 = x(x-9d)(x-729d)$
(shifted full-$2$-torsion model; $A=-738d$, $B=6561d^2$).

1. **Rank-one census.** $39$ of the $122$ signed squarefree twists with
   $0 < |d| \le 100$ have certified analytic-free algebraic rank $\ge 1$:
   an explicit rational point $P \notin E_d(\mathbf{Q})_{\mathrm{tors}}$,
   certified by exact-arithmetic $24P \ne \mathcal{O}$
   (sound: every torsion group containing $\mathbf{Z}/2\times\mathbf{Z}/2$
   has exponent dividing $24$ by Mazur).
   Point list: `output/artifacts/pts_pos.json`, `pts_neg.json`,
   `pts_deep.json`; certificates: `nontorsion.json`.
2. **Rank-two witness.** $E_{-17}$ has rank $\ge 2$ via
   $P=(-833, 80920)$, $Q=(-729, 69984)$, since
   $(-833)(-833+153)(-833+12393) = 80920^2 = 6548046400$ and
   $(-729)(-729+153)(-729+12393) = 69984^2 = 4897760256$ exactly,
   and the Kummer images $\delta(P),\delta(Q)$ together with the
   empirically calibrated torsion cosets span $16$ distinct classes in
   $(\mathbf{Q}^\times/\mathbf{Q}^{\times 2})^2$, so
   $\dim E_{-17}(\mathbf{Q})/2E_{-17}(\mathbf{Q}) \ge 4$, i.e. rank $\ge 2$.
   Four further rank-$\ge 2$ twists: $d \in \{38, 91, -65, -77\}$.
   Certificate: `output/artifacts/rank2emp.json` (+ script `rank2emp.py`
   with per-curve self-validating torsion: $4$ distinct, subgroup-closed).
3. **Search-minimality (bounded, honest).** No squarefree twist with
   $0<|d|<17$ yields two Kummer-independent points within the committed
   search ($x=p/q$, $q\le 8$, $|p|\le 1500$; follow-up $q\le 20$,
   $|p|\le 4000$ on point-less twists); $d=-17$ is hence the minimal
   *found* rank-$2$ twist, not a proven global minimal (a large-height
   generator below $17$ is not excluded).
4. **Sound Selmer upper-bound table.** `sel2b_le100.json` gives a
   full-$2$-descent *sound* upper bound per twist (keep-on-inconclusive;
   drops only for real-interval impossibility, exhaustive mod-$p^k$
   insolubility at bad primes, or Legendre obstruction at good primes).
   It is too weak to close ranks in general (only the method, not the
   table values, is claimed) and is supplied as method evidence only.

## What is NOT claimed

- No closed per-twist rank equality table; no $\dim\mathrm{Sel}_2 - \mathrm{rank} \ge 2$
  gap frequency; no root-number agreement; no $|d|\le 200$ coverage.
  The target claim's gap census is **not** achieved — this report claims
  only the fallback-shaped partial result above.
- Full minimality of $d=-17$ as a rank-$2$ twist is conjectural
  (search-bounded); the proven fact is rank $\ge 2$ with exact generators.

## Verification (stdlib + sympy only, seconds)

- `python3 output/artifacts/rank2emp.py` re-derives the five rank-$\ge 2$
  verdicts (asserts torsion self-validation per curve).
- On-curve checks: integer multiplications above; nontorsion: exact
  `Fraction` arithmetic in `ecarith.py` ($24P\ne\mathcal{O}$).
- Family model: `base_model.json`; twist enumeration: `dlist.json`.

## Limitations

- Naive-search lower bounds only; $83$ of $122$ twists have no found
  point (rank $0$ vs large generator undecided).
- Selmer UB not tight (e.g. $d=1$ gives $\dim\mathrm{Sel}_2 = 4$ rather
  than the sharp $2$); the gap statistic is therefore absent.
- Kummer torsion calibration is empirical-per-curve (asserted closed in
  code) rather than via a closed formula; an earlier closed-form attempt
  failed closure and was withdrawn (see WORKLOG Steps 9–12).
