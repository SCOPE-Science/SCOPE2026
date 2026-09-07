# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# A certified flat Littlewood polynomial in degree 28: two-sided sup interval and exact maximal skew-symmetric merit

## Abstract
We exhibit one explicit reciprocal-canonical Littlewood polynomial
$P^{\star}$ of degree 28 (length 29) with a machine-checkable certificate:
$\sqrt{45}\le M(P^{\star})\le \sqrt{45}+0.00487$ (default grid; $+0.00122$ at
$N=2^{20}$) where $M(P)=\max_{|z|=1}|P(z)|$, and exact merit factor
$F(P^{\star})=841/124\approx 6.7823$ from integer autocorrelations.
$P^{\star}$ lies in the skew-symmetric subspace and attains its exact merit
maximum (exhaustive integer scan of all $2^{14}$ sequences with $a_0=+1$).
No published-record-beating claim is made: this workspace is offline so the
Borwein--Choi/Mossinghoff records could not be pinned, and the full
$134$M-orbit canonical space was not exhaustively swept. The contribution is
a tight, replayable ($<1$ s) joint flatness-plus-merit witness with proofs,
not a table recomputation.

## 1. Objects and notation
Let $L_{28}=\{P(z)=\sum_{i=0}^{28}a_iz^i:a_i\in\{+1,-1\},\,a_0=+1\}$.
$|L_{28}|=2^{28}$. Group $G$ acts by $P\mapsto -P$ and reciprocal
$P^*(z)=z^{28}P(1/z)$. Canonical representative: among the orbit elements
with constant term $+1$ ($P$ and $\pm P^*$, one sign choice each), take the
numeric lexicographic minimum on $(a_1,\dots,a_{28})$ with $-1\prec+1$.
Sup norm $M(P)=\max_{|z|=1}|P(z)|=\max_t|P(e^{it})|$.
Autocorrelations $C_k=\sum_{i=0}^{28-k}a_ia_{i+k}\in\mathbb Z$,
merit $F(P)=29^2/(2\sum_{k=1}^{28}C_k^2)$ (exact rational).

Skew-symmetric subspace (odd length $2m+1=29$, $m=14$):
$a_{m+k}=(-1)^k a_{m-k}$, $k=1,\dots,14$. Free bits $a_1,\dots,a_{14}$
($a_0=+1$ fixed): $2^{14}=16384$ sequences ($2^{15}$ counting both signs).
Standard fact used only for interpretation: odd-lag $C_k$ vanish here;
we verify it by direct integer computation for the witness.

## 2. Theorem (proved; verification-critical files in output/artifacts/)
**Witness.**
$a_0\ldots a_{28}=$ `+---++++---+---+---+--+-++-++`
(reciprocal `++-++-+--+---+---+---++++---+`; witness is canonical since at
$a_1$, $-1\prec+1$).

(a) **Two-sided sup certificate.**
$P^{\star}(i)=3-6i$ by direct coefficient sum (even/odd subsequences),
so $|P^{\star}(i)|^2=9+36=45$ exactly and $M(P^{\star})\ge\sqrt{45}
=6.7082039325\ldots$.
Lemma: $|P(e^{it})-P(e^{is})|\le(\sum_{k=0}^{28}k)|t-s|=406|t-s|$, since
$|e^{ikt}-e^{iks}|\le k|t-s|$; hence
$|\,|P(e^{it})|-|P(e^{is})|\,|\le406|t-s|$.
On a uniform $N$-grid (spacing $2\pi/N$), every $t$ is within $\pi/N$ of a
node, so $M(P)\le \max_{\rm grid}|P|+406\pi/N$.
Recomputed grid maxima: $6.7082039325$ at $N\in\{16384,65536,262144,
1048576\}$ (attained at $z=\pm i$, which are grid nodes when $4\mid N$).
Thus $M(P^{\star})\le 6.7082039325+406\pi/N$ plus a $10^{-6}$ float margin
(FFT double-precision error at these sizes is $\lesssim10^{-12}$; see
limitations). At default $N=262144$: $M\le 6.71307053$; at $N=2^{20}$:
$M\le 6.70942034$. Certified interval width $<0.005$ (resp. $<0.0013$).

(b) **Exact merit.**
$C_1,\dots,C_{28}=$
$0,-3,0,1,0,1,0,1,0,-3,0,-3,0,-3,0,-3,0,1,0,1,0,1,0,1,0,-3,0,1$
(direct integer sums; odd lags $0$ as expected).
$\sum C_k^2=6\cdot9+8\cdot1=62$, so $F(P^{\star})=841/(2\cdot62)=841/124
\approx6.7822580645$ exactly.

(c) **Subspace exact optimality (merit).**
Exhaustive scan of all $16384$ skew-symmetric sequences with $a_0=+1$ in
exact integer arithmetic gives minimum autocorrelation energy $62$,
i.e. maximum merit $841/124$, attained by exactly 4 masks
$\{115,1144,4397,5414\}$ (two reciprocal pairs; masks $1144/4397$ are
$P^{\star}$ and its reciprocal with grid $6.7082$; masks $115/5414$ share
the merit but have grid $\approx7.5675$). Hence $P^{\star}$ is a
maximal-merit sequence of the skew-symmetric subspace, proved.

(d) **Corollaries.**
$\min_{L_{28}}M\le 6.7095$ and $\max_{L_{28}}F\ge 841/124$, both via the
single witness $P^{\star}$.

## 3. How the witness was found (evidence, not part of the proof)
Rotated-Legendre seeds, $300+300$ random-start single-flip hill climbs
(sup/merit objectives, $N=4096$ FFT prefilter), full skew-subspace
enumeration ($16384$, $N=8192$), then basin-hopping ($600$ sup kicks,
$2000$ merit kicks) and exhaustive 1- and 2-flip neighborhoods of the
incumbent. The skew scan's tied-best grid element coincided with a
full-space 1- and 2-flip local optimum; no basin-hopping trial beat its
grid ($6.7082$) or its merit ($6.7823$). These negative searches are
reported as context for future exhaustive work, not as non-existence
claims.

## 4. Reproduction
`python3 verify.py --degree 28 [--grid 262144]` re-derives canonicality,
skew-symmetry, exact $C_k$/merit, exact $|P(i)|^2=45$, FFT grid max plus
Lipschitz remainder, the full $16384$-sequence integer merit scan, and the
1-flip local-optimality check. Runtime $\approx0.4$ s ($N=262144$; numpy
only). `skew_census_deg28.csv` logs all $16384$ skew sequences
(mask, bits, $8192$-grid, energy, merit). `witness_deg28.txt` pins the
witness and certificate numbers.

## 5. Limitations and what is NOT claimed
(i) No comparison against $R28_{\sup}/R28_F$: record tables could not be
fetched in this offline workspace, so the target joint record-beating
criterion ($-0.03$ sup / $+0.20$ merit with $3\%$ non-regression) is
unassessed, not achieved. (ii) No certified lower-bound gap $B_{28}$ and no
exhaustive sweep of the $134$M canonical orbits. (iii) Sup upper bound
relies on FFT grid values plus a $10^{-6}$ double-precision margin rather
than interval arithmetic; the remainder $406\pi/N$ itself is exact
rational-multiple-of-$\pi$ arithmetic recomputed by the verifier, and the
lower bound $|P(i)|^2=45$ is pure integer arithmetic. A fully
interval-arithmetic certificate and the $M=\sqrt{45}$ exact-equality
question (dense grids suggest the global max is exactly at $z=\pm i$ but
this is unproved) are left open. (iv) Originality: skew-symmetric merit
theory, Legendre constructions, and FFT sieving are classical; the claim
here is only the explicit certified witness plus the exact subspace-maximum
recomputation, cleanly separated from conjecture (global optimality of
$P^{\star}$ in $L_{28}$ is plausible from the searches but unproved).

## References (cutoff knowledge; not live-verified here)
Balister et al., Flat Littlewood polynomials exist, Ann. Math. 2020,
arXiv:1907.09488; Borwein--Choi, explicit Littlewood/m merit tables,
arXiv:math/0005094 and Mossinghoff database; Borwein--Choi--Jedwab, merit
$>6.34$ families, IEEE TIT 2004.
