# Weight-enumerator diversity among optimal binary [18,6,8] codes

## Context

Optimal binary linear-code tables (Grassl BKLC) record one distance and one
construction per cell, but not the set of weight enumerators realized by all
optimal codes at fixed parameters. Whether all optimal $[n,k]$ codes share one
enumerator (rigidity) or inequivalent optimals have distinct enumerators
(diversity) is a MacWilliams-theory classification question feeding
residual, shortening, and Griesmer-sharpness arguments, with downstream use in
code-based cryptography, storage, and fault tolerance. Cell $(18,6)$ is a
natural single-cell test: $k=6$ keeps full enumeration at $64$ codewords while
$n=18$ sits on the Golay shortening lineage.

## Definitions

- Binary linear $[n,k,d]$ code: $k$-dimensional subspace of $\mathrm{GF}(2)^n$
  with minimum Hamming weight $d$.
- Weight enumerator: $W_C(z)=\sum_i A_i z^i$, $A_i$ = number of codewords of
  weight $i$.
- Dual spectrum: $B_j$ = weight distribution of the dual code $C^\perp$
  (here $\dim 12$, $2^{12}=4096$ words).
- MacWilliams identities ($n=18$, $k=6$):
  $B_j = 2^{-6}\sum_{i=0}^{18} A_i K_j(i)$, $K_j$ = binary Krawtchouk
  polynomial; all $B_j$ must be nonnegative integers summing to $4096$.
- Shortening at positions $S$: subcode vanishing on $S$ with those coordinates
  deleted.
- Monomial equivalence over $\mathrm{GF}(2)$ = coordinate permutation
  (no nontrivial scalars); it preserves Hamming weights, so distinct
  enumerators imply monomial inequivalence.

## Result

Optimal distance $d(18,6)=8$ is cited closed input (Grassl BKLC: LB $8$ by
shortening of $[24,12,8]$, UB $8$ by Griesmer).

**Theorem (diversity witness).** There exist two binary linear $[18,6,8]$
codes $C_1, C_2$, each a $6$-fold shortening of the extended Golay code
$G_{24}$, with distinct weight enumerators

$$W_1(z)=1+45z^8+18z^{12},\qquad W_2(z)=1+46z^8+16z^{12}+z^{16}.$$

Hence not all optimal $[18,6]$ codes share one enumerator; distinct
enumerators imply monomial inequivalence. Both codes satisfy the full
MacWilliams identities against their directly tallied dual spectra.

Parent: cyclic $[23,12,7]$ Golay with
$g(x)=x^{11}+x^9+x^7+x^6+x^5+x+1$, extended by overall parity to $G_{24}$
$[24,12,8]$ with $A=\{0{:}1,8{:}759,12{:}2576,16{:}759,24{:}1\}$.

- $C_1$: shorten $G_{24}$ at positions $\{18,19,20,21,22,23\}$.
- $C_2$: shorten $G_{24}$ at positions $\{1,4,6,9,10,16\}$.

Generator/parity matrices: `artifacts/G_C1.txt, H_C1.txt, G_C2.txt, H_C2.txt`
(also JSON-embedded in `artifacts/C1.json, C2.json`). $G$ is $6\times 18$
systematic-form; $H$ is $12\times 18$.

$$G_{C_1}=\begin{pmatrix}
1 0 0 0 0 0 1 0 1 0 1 0 1 1 1 0 0 1\\
0 1 0 0 0 0 1 1 1 1 0 0 0 1 0 0 1 1\\
0 0 1 0 0 0 1 1 0 1 1 1 0 0 0 1 1 0\\
0 0 0 1 0 0 0 1 1 0 1 1 1 0 0 0 1 1\\
0 0 0 0 1 0 1 0 0 1 0 0 1 1 1 1 1 0\\
0 0 0 0 0 1 0 1 0 0 1 0 0 1 1 1 1 1
\end{pmatrix}$$

$G_{C_2}$: exact rows in `artifacts/G_C2.txt` (row space is the certified
object).

Dual spectra (direct $2^{12}$ tally = MacWilliams prediction, sum $4096$):

- $B^{(1)}=\{0{:}1,3{:}6,4{:}45,5{:}180,6{:}303,7{:}378,8{:}675,9{:}920,
  10{:}675,11{:}378,12{:}303,13{:}180,14{:}45,15{:}6,18{:}1\}$.
- $B^{(2)}=\{0{:}1,2{:}1,4{:}60,5{:}160,6{:}316,7{:}384,8{:}646,9{:}960,
  10{:}646,11{:}384,12{:}316,13{:}160,14{:}60,16{:}1,18{:}1\}$.

**Companion census A (MacWilliams/Krawtchouk feasibility, exact).**
Exactly $13$ integer vectors $(A_0=1, A_1=\dots=A_7=0, \sum A_i=64)$ yield
nonnegative integer dual spectra
$B_j=2^{-6}\sum_i A_iK_j(i)$ ($K$ = binary Krawtchouk, $n=18$); full list in
`artifacts/feasible_census.json`. The two realized enumerators above are
members; the other $11$ are feasibility survivors whose realizability is left
open (not claimed excluded).

**Reported census B (Golay-shortening lineage).** The candidate reports an
exhaustive $\binom{24}{6}=134596$ $6$-fold shortening enumeration of the fixed
$G_{24}$ with only $[18,6,8]$ enumerators $W_1$ ($113344$ sets) and $W_2$
($21252$ sets). The audit spot-checked this on $1500$ random sets (all
conforming) but did not fully replay all $134596$ sets; see Limitations.

## Proof / evidence

Computational proof (exact integer arithmetic, finite enumeration):

1. Rank $G=6$, $64$ distinct codewords, tally sums to $64$, min weight $8$
   (replayed for both codes).
2. Parity-check $H$ ($12\times 18$, rank $12$) from nullspace construction;
   $GH^T=0$ over $\mathrm{GF}(2)$ (replayed).
3. Direct dual tally ($2^{12}=4096$ words) equals exact-rational MacWilliams
   transform of $A$ term-by-term, zero remainder mod $64$, all $B_j\ge 0$
   (replayed).
4. Feasibility DFS over $A_8\ldots A_{18}$ with exact integer arithmetic
   (audit replay: $498339$ nodes with interval pruning) yields exactly the
   $13$ listed vectors; every $B$ spectrum rechecked.
5. Parent rebuilt from the cyclic Golay polynomial above reproduces the
   $G_{24}$ tally; shortening at the two claimed $6$-sets reproduces exactly
   $W_1$ and $W_2$ with dimension $6$ (replayed).
6. Distinct enumerators certify monomial inequivalence (weight-preserving);
   no separate permutation search needed.

## Limitations

- Distance optimality $d(18,6)=8$ is cited (Grassl), not re-proved.
- No claim on the $11$ non-realized MacWilliams-feasible vectors (open).
- No claim that $W_1,W_2$ are the only enumerators among ALL optimal
  $[18,6]$ codes (only the $13$-vector feasibility bound plus the reported
  Golay-shortening census). The rigidity-vs-diversity disjunction IS decided
  (diversity holds), but full classification is not.
- The $\binom{24}{6}$ count split ($113344$ vs $21252$) is a reported figure
  with a $1500$-set audit spot-check, not a fully audit-replayed enumeration.
- Monomial inequivalence rests on distinct enumerators; no separate
  permutation search claimed.

## Reproducibility

Stdlib-only Python + numpy. From `artifacts/`: read `G_C*.txt`, enumerate
$2^6$ codewords, check tally/rank; read `H_C*.txt`, check $GH^T=0$ and
$2^{12}$ dual tally vs MacWilliams
$B_j=2^{-6}\sum_i A_i\sum_t(-1)^t\binom{i}{t}\binom{n-i}{j-t}$.
Feasibility: DFS over $A_8\ldots A_{18}$ with $A_0=1$, $A_1\ldots A_7=0$,
$\sum A_i=64$, exact Krawtchouk dual check. SHA-256 codeword+enumerator
hashes: $C_1$ `19b27438…`, $C_2$ `1f5d987d…` (full in JSON).

## References

- Grassl BKLC detail $[18,6]$ over GF(2): LB $8$ (shortening of $[24,12,8]$),
  UB $8$ (Griesmer); one construction only, no enumerator data.
  https://www.codetables.de/BKLC/BKLC.php?q=2&n=18&k=6
- Hao Chen, Griesmer and Optimal Linear Codes from the Affine
  Solomon-Stiffler Construction, arXiv:2406.10825.
  https://arxiv.org/abs/2406.10825
  (Infinite-family distributions; no exhaustive $[18,6]$ enumerator set.)
- V. Pless / W. C. Huffman, Handbook of Coding Theory; Huffman (2005) on
  self-dual codes — disjoint regime ($k=n/2$), cited for separation.
