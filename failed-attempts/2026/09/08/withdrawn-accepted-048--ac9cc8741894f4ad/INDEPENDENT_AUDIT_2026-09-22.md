# Independent audit — 2026-09-22 campaign

**Record:** `SCOPE-20260908-048` / `2026/09/08/048`  
**Reviewed UTC date:** 2026-09-24  
**Audited public commit:** `f1bee63e7115a5c2a8df4210f09faab70a83c26b`  
**Source tree:** `c6155484d7df807dbc5a2de6b86861988e14a579`  
**RESULT.md blob:** `04a67fa8056fd35153a031ff7478d73a2e50bfd6`

## Claim audited

The record gives exact one-sided support-feasibility counts for 3x3 payoff matrices with entries in {0,1,2,3}, then combines two such matrices into a nondegenerate bimatrix-game witness with seven Nash equilibria, including a fully mixed equilibrium and welfare-6 pure equilibria. It explicitly does not claim the full joint distribution over all `4^18` bimatrix games.

## Correctness — PASS

I reconstructed the finite calculations independently rather than relying on the historical `AUDIT.json`.

For one-player support feasibility, exact enumeration gives:

- 1x1: core count 14 and `14*4^6 = 57344`;
- 2x2: core count 486 and `486*4^3 = 31104`;
- 3x3: 34032 matrices, split 17016/17016 by determinant sign.

For the displayed witness
`A=[[0,1,3],[0,3,0],[2,2,1]]`,
`B=[[0,1,3],[2,3,1],[2,1,0]]`,
I enumerated all equal-size support pairs with exact rational arithmetic, solved the indifference equations, and enforced strict outside best-response inequalities. Exactly seven equilibria were found: three pure, three 2x2 mixed, and one fully mixed with row strategy `(3/8,1/8,1/2)` and column strategy `(1/11,6/11,4/11)`. The stated pure-equilibrium welfare maximum 6 and next-best 4 are also reproduced. I separately checked the usual nondegeneracy condition: no opponent support of size 1 has more than one best response and no support-2 opponent mixture induces three best responses.

These checks reproduce the substantive finite claims. They do not elevate the record's deliberately unclaimed full `4^18` joint census.

## Originality — PASS, narrowly qualified

Searches included `"3x3 bimatrix 7 equilibria"`, `"3x3 bimatrix 0 1 2 3 exhaustive Nash"`, the exact count strings `57344` and `34032`, and dataset searches for enumerated 3x3 games. I did not find the exact one-sided `{0,1,2,3}` support-count table in the inspected literature.

The seven-equilibrium phenomenon itself is not new. Quint and Shubik proved that every odd number through `2^n-1` is realized by an `n x n` bimatrix game and conjectured the tight bound; modern work confirms the bound for `n<=4`. See:
- Thomas Quint and Martin Shubik, *A Theorem on the Number of Nash Equilibria in a Bimatrix Game*, IJGT 26 (1997), abstract: https://econpapers.repec.org/RePEc:spr:jogath:v:26:y:1997:i:3:p:353-359
- C. Ickstadt, T. Theobald, B. von Stengel, *A Stable-Set Bound and Maximal Numbers of Nash Equilibria in Bimatrix Games*, arXiv:2411.12385.
- Fourny and Sulser's 2020 "Ten million 3-by-3 strategic games" dataset is a large sampled game dataset, not this exact finite cube census: https://data.mendeley.com/datasets/xynvvrjvrv

Accordingly, originality is limited to the exact small-alphabet marginal counts and this particular witness, not to seven equilibria, support enumeration, or nondegeneracy theory.

## Scientific value — FAIL

The new material is an exhaustive census over an arbitrary tiny payoff alphabet, and only a one-sided marginal census: it does not produce the joint distribution of realized equilibrium counts over the `4^18` game pairs, a new asymptotic or structural theorem, a new algorithmic bound, or a new extremal phenomenon. The seven-equilibrium headline is already a classical n=3 extremal fact, and the displayed witness is therefore illustrative rather than frontier evidence.

The table can serve as a regression/benchmark fixture for equilibrium software, but that is too limited a scientific contribution for an accepted finding under this campaign's value criterion.

## Final disposition

**FAILED.** Correctness passes and the exact marginal census appears narrowly original to the best of this search, but scientific value fails. No claim was moved to failed status merely for an access or tooling issue.
