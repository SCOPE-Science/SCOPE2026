# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Griesmer-defect spectrum and certified sporadic witnesses for optimal binary linear codes with k ≤ 5, n ≤ 15

## Abstract
We determine, for every optimal binary linear $[n,k]$ code with $1\le k\le 5$,
$1\le n\le 15$ (65 cells), the exact minimum distance $d(n,k)$, the Griesmer
number $g(k,d)=\sum_{i<k}\lceil d/2^i\rceil$, and the Griesmer defect
$\delta(n,k)=n-g(k,d(n,k))$. Sixty-one cells are Griesmer-tight
($\delta=0$); four proper optima sit below the Griesmer max:
$d(8,5)=2$, $d(9,5)=3$, $d(12,5)=4$, $d(13,5)=5$.
Since Solomon–Stiffler and Belov codes meet the Griesmer bound
($\delta=0$), all 21 positive-defect optimal cells are certified sporadic
(outside both families). The maximal defect in scope is $\delta=3$ at
$[12,5,4]$, exhibited with a MacWilliams-verified enumerator and a
residual-chain log. Every cell carries an explicit generator and exact
weight enumerator, replayable by a stdlib-only script.

## 1. Definitions and typing rule
For binary $[n,k,d]$, $g(k,d)=\sum_{i=0}^{k-1}\lceil d/2^i\rceil\le n$ is the
Griesmer bound; $\delta=n-g(k,d)\ge 0$. Solomon–Stiffler codes (simplex minus
a union of subspaces) and Belov codes are Griesmer codes, i.e. $\delta=0$
(classical; recalled as the starting point of Wang–Chen–Wu arXiv:2605.11431:
positive-defect optima are "certainly not equivalent to Solomon–Stiffler
codes or Belov codes"). Hence for an *optimal* code, $\delta>0$ certifies
sporadic status with no further isomorphism test. Codes with $\delta=0$ are
typed "Griesmer" (the finer SS-vs-Belov subdivision is not attempted here).

## 2. Exact distances
Upper bounds: the Griesmer inequality $n\ge g(k,d)$ caps every cell at
$g_{\max}(k,n)$, tight in 61 cells. The four exceptions:
- $[8,5,3]$ impossible by Hamming: $A(8,3)\le 2^8/(1+8)=28.4$, so
  $A(8,3)\le 28<32$; hence $d(8,5)=2$ (construction below).
- $[9,5,4]$ impossible by puncturing: $A(9,4)\le A(8,3)\le 28<32$; hence
  $d(9,5)=3$.
- $[12,5,5]$ and $[13,5,6]$ ruled out by exhaustive systematic-form search:
  fix the first $k$ columns to the identity (every linear code has a
  systematic form), enumerate nondecreasing multisets of the remaining
  $n-k$ nonzero columns with partial-weight pruning; both trees close with
  625654 nodes and no survivor (replayed in `replay.py`, ~seconds).
Lower bounds: explicit column multisets (as $k$-bit integers, identity block
first for $k=5$) in `results.json`; minweight verified by enumerating all
$2^k\le 32$ codewords.

## 3. Defect spectrum (sporadic = δ > 0)
| k | (n, d, δ) with δ>0 |
|---|---------------------|
| 2 | (4,2,1), (7,4,1), (10,6,1), (13,8,1) |
| 3 | (5,2,1), (8,4,1), (9,4,2), (12,6,1), (15,8,1) |
| 4 | (6,2,1), (9,4,1), (10,4,2), (13,6,1) |
| 5 | (7,2,1), (8,2,2), (9,3,1), (10,4,1), (11,4,2), (12,4,3), (13,5,1), (14,6,1) |
All other cells in scope have δ=0. Full table with generators and
enumerators: `output/artifacts/results.json` (65 rows).

## 4. Headline witness: optimal [12,5,4], defect 3
Columns (k-bit integers): $[1,2,4,8,16,1,1,1,14,22,26,28]$.
$2^5=32$ recount gives $A(z)=1+15z^4+15z^8+z^{12}$, so $d=4$,
$g(5,4)=4+2+1+1+1=9$, $\delta=12-9=3>0$, hence sporadic by §1.
Dual ($[12,7]$) recount gives $B=(0{:}1,2{:}6,4{:}15,6{:}84,8{:}15,10{:}6,12{:}1)$,
satisfying the MacWilliams identities
$B_j=2^{-5}\sum_i A_i K_j(i)$ exactly (checked in `replay.py`).
Residual chain: any weight-4 word has support size 4; puncturing it leaves a
$[8,4,4]$ residual (computed minimum 4, needs $\ge\lceil 4/2\rceil=2$),
itself a Griesmer code ($g(4,4)=8$), consistent with optimality.
Optimality of $d=4$: $[12,5,5]$ excluded by the replayed DFS (§2), and the
witness attains 4.

## 5. Reproduction
`output/artifacts/replay.py` (stdlib only; run in that directory):
recounts every rank/weight/enumerator/defect, replays the Hamming, puncture,
and both DFS kills, and rechecks the headline dual + MacWilliams + residual,
printing `VERIFY_OK`. `exact_table.py` is the table generator; `verify.py`
is an exploratory toolkit.

## 6. Limitations and originality
- The $k\le 4$ achieving generators were found by seeded stochastic search
  but are frozen and re-verify exactly; any equivalent optima give the same
  $(d,\delta)$ claims.
- The $[12,5,5]$/$[13,5,6]$ nonexistence certificates are replayed computer
  enumerations (625654 nodes each), not closed-form inequalities.
- Only the sporadic/Griesmer typing is claimed; no SS-vs-Belov subdivision
  of the 44 Griesmer cells.
- Grassl's tables hold the bare $d(n,k)$ values; the new layer is the
  certified defect spectrum, the sporadic typing, and the replayable
  witness package.
