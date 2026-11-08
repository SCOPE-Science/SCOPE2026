# Sharp ternary multiset two-deletion code sizes through length twenty

## Finding

For an integer \(n\) with \(6\le n\le20\), let \(\mathcal S_{n,3}=\{(a,b,c)\in\mathbb Z_{\ge0}^{3}:a+b+c=n\}\). Write \(S_3(n,2)\) for the largest size of a subset \(C\subseteq\mathcal S_{n,3}\) from which two deleted symbols, with their positions and order forgotten, can always be corrected. Equivalently, its codewords have pairwise deletion distance at least three.

The **exact** optima are

\[
(S_3(n,2))_{n=6}^{20}=(6,6,8,10,11,12,15,17,19,21,24,26,29,32,35).
\]

The table includes the maximum cardinality among the seven classes of the cyclic two-deletion syndrome \(a+3b\pmod7\), and the total weight of a rational clique-cover certificate used for each upper bound.

| Length \(n\) | Sharp optimum \(S_3(n,2)\) | Best cyclic syndrome class | Certified upper weight |
|---:|---:|---:|---:|
| 6 | 6 | 4 | 6 |
| 7 | 6 | 6 | 6 |
| 8 | 8 | 7 | 8 |
| 9 | 10 | 8 | 10 |
| 10 | 11 | 10 | 11 |
| 11 | 12 | 12 | 51/4 |
| 12 | 15 | 13 | 15 |
| 13 | 17 | 15 | 17 |
| 14 | 19 | 18 | 444/23 |
| 15 | 21 | 20 | 282/13 |
| 16 | 24 | 22 | 2151/89 |
| 17 | 26 | 25 | 431/16 |
| 18 | 29 | 28 | 149/5 |
| 19 | 32 | 30 | 6490/199 |
| 20 | 35 | 33 | 1291/36 |

## Assumptions and scope

The alphabet is the fixed, labeled three-symbol alphabet. The message is an unordered multiset, encoded by its three nonnegative multiplicities; the receiver loses exactly two symbol occurrences and obtains another unordered multiset. The theorem includes every integer length from \(6\) through \(20\), and no other lengths or alphabets. An output is counted once even if it can arise from multiple deletion choices.

For vectors \(u,v\) of the same length define
\[
d(u,v)=\frac12\sum_{i=0}^{2}|u_i-v_i|=n-\sum_{i=0}^{2}\min(u_i,v_i).
\]
Two vectors have a common deletion output of length \(n-2\) exactly when \(d(u,v)\le2\). Therefore, a correcting code is precisely a family with all distinct pairs at distance at least \(3\).

## Proof

Fix one of the fifteen permitted lengths. The file `s3_cert.json` contains a record with a positive integer `optimum`, a list `witness` of that many integer triples, and a finite list `dual_cliques` of pairs \((K,w_K)\) with positive rational weights. The rational weights and the total `dual_cost` are written as exact fractions, not floating-point approximations. The definitions of these certificate fields are part of the proof:

**Lower bound.** Every triple in `witness` lies in \(\mathcal S_{n,3}\), and the certificate verifies
\[
d(u,v)\ge3\qquad(u,v\in\mathrm{witness},\ u\ne v).
\]
Thus the witnesses form correctable codes of cardinality `optimum`.

**Upper bound.** Each listed \(K\) consists of vertices pairwise at distance at most \(2\), so any correctable code intersects \(K\) in at most one vertex. The certificate also verifies, for every vertex \(v\in\mathcal S_{n,3}\),
\[
\sum_{K\ni v}w_K\ge1,\qquad w_K\ge0.
\]
Consequently, for any correctable code \(C\),
\[
|C|\le\sum_{v\in C}\sum_{K\ni v}w_K
=\sum_K w_K|C\cap K|\le\sum_Kw_K.
\]
Since \(|C|\) is an integer, its value is at most the floor of the rational `dual_cost`. For every record, this floor equals `optimum` (as the table displays), so the lower and upper bounds coincide. This completes a finite, exact proof of all fifteen optima; no optimization solver, probabilistic inference, or numerical tolerance is used in the certificate replay.

The cyclic comparison follows by partitioning \(\mathcal S_{n,3}\) by \(a+3b\pmod7\). If two distinct vectors in one such class were at distance \(1\) or \(2\), the difference of their weighted coordinates would be a nonzero signed difference of multisets of at most two elements from \(\{0,1,3\}\subset\mathbb Z_7\). All six **unordered two-element** sums from the weights \(\{0,1,3\}\) modulo seven are distinct: \(0,1,2,3,4,6\). Pad each shorter deletion multiset with zero-weight symbols to reach two elements. Hence equality of two syndromes forces equality of the corresponding deletion-count triples, so the two source vectors coincide. Thus every syndrome class is a valid code; its size is counted directly in the table. The sharp optimum strictly exceeds the largest such class at thirteen of the fifteen lengths, including size \(6\) versus \(4\) at \(n=6\).

## Verification

Place `s3_cert.json` and `s3_check.py` in the same directory and run:

```bash
python3 s3_check.py s3_cert.json
```

The standard-library checker reconstructs all \(\binom{n+2}{2}\) vertices for each length, checks the validity and pairwise distance of every witness, checks every pair inside every dual clique, accumulates every vertex's exact rational cover weight, and compares the exact rational total with the proposed optimum plus one. It finishes with `CERTIFICATE VERIFIED: 15 length values, exact rational upper bounds and explicit lower witnesses`.

In addition to the replay, the candidate bounds were obtained by integer optimization and fractional clique-cover optimization; these solvers are **not** needed to validate the proof. The complete certificate is independent of solver-specific outputs.

## Relationship to prior work

Kovačević and Vukobratović determined the existence and structure of perfect codes in the discrete simplex, including the ternary one-perfect case at length \(4\), outside the claimed length interval [1]. Kovačević and Tan developed general Sidon-code constructions and the leading fixed-alphabet asymptotic, \(S_3(n,2)\sim n^2/14\), without a finite-length profile through \(20\) [2]. Kreindel, Essayag and Zabokritskiy established the cyclic two-deletion construction and analyzed exact ternary *single*-deletion optima, not these two-deletion maxima [3]. Their subsequent work gives exact ball enumerators and general finite upper and lower estimates, but does not supply these sharp fifteen integer optima [4].

The statement is the finite interval of exact maximum code cardinalities, together with its explicit primal and dual certificates. It does not claim a new Sidon principle, a new perfect-code characterization, or a new asymptotic coefficient. The close literature concerns the same multiset metric, but the cited results do not entail the fifteen numeric equalities.

## Limitations

This is an exact **finite** length profile, not a formula valid for every length. It does not classify all maximizing codes, imply optimality of cyclic syndrome classes, or provide a uniform construction above length \(20\). The uploaded exact certificates provide a direct check of the theorem, but have not undergone an independent mathematical audit. Some earlier computational tables or indexing variants may be unknown; priority beyond the inspected material is not guaranteed.

## References

1. M. Kovačević and D. Vukobratović, *Perfect Codes in the Discrete Simplex*, arXiv:1307.3142 (first public 2013-07-11), https://arxiv.org/html/1307.3142v2 .
2. M. Kovačević and V. Y. F. Tan, *Codes in the Space of Multisets—Coding for Permutation Channels with Impairments*, arXiv:1612.08837 (first public 2016-12-28), https://arxiv.org/abs/1612.08837 .
3. A. Kreindel, I. Barouch Essayag and A. Lev Zabokritskiy, *Multiset Deletion-Correcting Codes: Bounds and Constructions*, arXiv:2601.05636 (first public 2026-01-09), https://arxiv.org/abs/2601.05636 .
4. A. Kreindel, I. Barouch Essayag and A. Lev Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322 (first public 2026-03-18), https://arxiv.org/abs/2603.18322 .
