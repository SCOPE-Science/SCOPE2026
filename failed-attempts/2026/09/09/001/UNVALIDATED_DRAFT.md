# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Attaining-witness enumerators at the live-open BKLC boundary (35–37, 10–11) with MacWilliams certificates, plus a new [37,10,13] record witness

## Abstract
We give explicit binary linear codes attaining the Grassl BKLC lower bounds at the
contiguous live-open boundary block $(35,10)$, $(36,10)$, $(36,11)$, with exact full
weight enumerators certified by exhaustive enumeration and exact-rational MacWilliams
($=$ Krawtchouk) duality. In addition, exhaustive single-column extension of our best
$[36,10,12]$ witnesses yields an explicit $[37,10,13]$ code, which meets the BKLC lower
bound $12$–$13$ at $(37,10)$ and is the first published witness enumerator there known
to us. No open interval is closed: we log the exact obstruction data (puncture census,
Griesmer/Plotkin/residual admissibility) so every number below is checkable.

## 1. Codes

All generator matrices are in systematic form $G=[I_k\mid P]$, stored as $0/1$ rows in
`output/artifacts/G_*.txt`. Let $A_i$ be the number of codewords of weight $i$.

**Theorem 1 (certified attaining witnesses).** The following binary linear codes exist;
each tally sums to $2^k$ by exhaustive Gray-code enumeration (replay `verify.py`):

- $C_{35}$: $[35,10,12]$, $A_{12}=26$,
  $A=(1,0^{11},26,64,84,106,116,124,121,108,104,80,46,26,9,4,5,0^8)$.
- $C_{36}$: $[36,10,12]$, $A_{12}=5$,
  $A=(1,0^{11},5,53,86,84,103,120,129,125,105,85,56,30,26,14,1,1,0^8)$.
- $C_{36,11}$: $[36,11,12]$, $A_{12}=84$, even-weight code (all odd $A_i=0$),
  $A=(1,0^{11},84,0,253,0,429,0,525,0,428,0,231,0,82,0,15,0^{10})$.
- $C_{37}$: $[37,10,13]$, $A_{13}=34$,
  $A=(1,0^{12},34,69,78,97,120,123,118,112,98,75,42,30,20,5,2,0^9)$.

Each $G$ has full row rank $k$ (machine-checked). Distances are exact minima from the
complete codeword lists ($2^{10}=1024$, $2^{11}=2048$ words).

**Theorem 2 (MacWilliams certificates).** For each code above, the exact-rational
Krawtchouk transform $B_j=2^{-k}\sum_i A_iK_j(i)$ is integral, nonnegative, sums to
$2^{\,n-k}$, and equals the independently enumerated dual weight distribution wherever
the dual was enumerated:

- $C_{35}$: $B$ sums to $2^{25}$, $d^\perp=4$, $B_{0..7}=(1,0,0,0,29,327,1701,6667)$;
  coefficient-wise equal to the enumerated $[35,25,4]$ dual. Zero residual.
- $C_{36}$: $B$ sums to $2^{26}$, $d^\perp=4$, $B_{0..7}=(1,0,0,0,33,391,1996,8252)$;
  coefficient-wise equal to the enumerated $[36,26,4]$ dual. Zero residual.
- $C_{37}$: $B$ sums to $2^{27}$, integral/nonnegative
  ($B_{0..5}=(1,0,0,1,37,451)$); dual dimension $27$ ($2^{27}$ words) exceeds the
  verification window, so this is a MacWilliams-integrality certificate only.
- $C_{36,11}$: $B$ sums to $2^{25}$, integral/nonnegative, symmetric
  ($B_{0..5}=(1,0,0,0,10,187)$, $B_{36}=1$); dual dimension $25$ likewise certified by
  integrality only. The even-weight property ($A_{\rm odd}=0$, $B_{36}=1$ says the
  all-one word is in the dual) is consistent with $d=12$ even.

Full $B$ vectors are in `cert.json`; `verify.py` recomputes every tally, rank,
Krawtchouk dual, and (where stored) dual enumeration from the matrices alone and
prints `VERIFY_OK`.

## 2. How $C_{37}$ was found; what it does and does not imply

Scanning all $2^{10}-1=1023$ nonzero single-column extensions of each of two
independently found $[36,10,12]$ witnesses gave distance $13$ extensions in both cases
($A_{13}=34$ and $39$); we keep the $A_{13}=34$ one as $C_{37}$. Puncturing $C_{37}$ at
every one of its $37$ positions yields minimum distance $12$ in all $37$ cases, so
$C_{37}$ does **not** induce a $[36,10,13]$ code: the $(36,10)=13$–$14$ interval stays
open. $C_{37}$ does meet the BKLC lower bound at $(37,10)=12$–$13$ with $d=13$.

## 3. Negative/constraining data (exact, checkable)

- Griesmer needs $\sum_{i<k}\lceil d/2^i\rceil$: $[35,10,13]\!\to\!32\le35$,
  $[36,10,14]\!\to\!33\le36$, $[36,11,13]\!\to\!33\le36$ — all admissible, no
  elimination. Attaining witnesses have defects $35-29=6$, $36-29=7$, $36-30=6$.
- Plotkin ($d>n/2$) applies to none of the upper ends. Residuals
  $[36,10,14]\!\to\![22,9,\ge7]$, $[35,10,13]\!\to\![22,9,\ge7]$,
  $[36,11,13]\!\to\![23,10,\ge7]$ are Griesmer-admissible (needs $19,19,20$).
- Direct stochastic search ($\sim 10^5$ code evaluations across seeds/moves, including
  seeded anneals from the best $[36,10,12]$) never reached $[36,10,13]$, $[35,10,13]$,
  or $[36,11,13]$; this is logged effort, not a nonexistence proof.

## 4. Reproduction
`output/artifacts/`: `G_35_10_12.txt`, `G_36_10_12.txt`, `G_36_11_12.txt`,
`G_37_10_13.txt`, `cert.json` (exact tallies, exact $B$ vectors, ranks, dual data),
`verify.py` (stdlib $+$ numpy; `python3 verify.py` $\to$ `VERIFY_OK` in $\sim 1$–$2$ min).

## 5. Originality and limits
BKLC tables publish only $[n,k,d]$ bounds (plus lower-bound matrices) at these cells,
with no weight enumerator; the four enumerators above, the $[37,10,13]$ witness, the
$37/37$ puncture census, and the dual zero-residual equalities are computed in-run.
No interval is closed and no complete feasible-enumerator census of the upper ends is
claimed; the MacWilliams-feasible survivor-list part of the topic plan is explicitly
**not** delivered (combinatorial explosion), and duals of dimensions $25$/$27$ are
certified by exact integrality only, not by word-by-word enumeration.
