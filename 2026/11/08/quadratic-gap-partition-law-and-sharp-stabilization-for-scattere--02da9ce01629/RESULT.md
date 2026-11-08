# Quadratic-gap partition law and sharp stabilization for scattered `010` occurrences

## Finding

For a binary word \(w\), let \(c_{010}(w)\) count the increasing triples of positions spelling `010` (the positions need not be consecutive), and define
\[
B(n,k)=\#\{w\in\{0,1\}^n:c_{010}(w)=k\}.
\]
For each integer \(k\geq1\), define the finite polynomial
\[
Q_k(z)=\sum_{t=2}^{k+1}z^t[u^k]\prod_{j=1}^{t-1}\frac{1}{1-zu^{j(t-j)}}.
\tag{1}
\]
Here \([u^k]\) denotes coefficient extraction in the formal variable \(u\). Then, for **every** \(n\geq0\) and \(k\geq1\),
\[
\sum_{n\geq0}B(n,k)z^n=\frac{Q_k(z)}{(1-z)^2},\qquad
B(n,k)=\sum_{t=2}^{k+1}\ \sum_{\substack{g_1,\ldots,g_{t-1}\geq0\\\sum_{j=1}^{t-1}j(t-j)g_j=k}}
\max\!\left\{n-t-\sum_jg_j+1,0\right\}.
\tag{2}
\]
The polynomial \(Q_k\) has degree exactly \(k+2\), and its highest-degree coefficient equals \(1\) when \(k=1\) and equals \(3\) for every \(k\geq2\). In particular, writing
\[
a_k=Q_k(1),\quad d_k=Q_k'(1)-Q_k(1),\quad P_k(n)=a_kn-d_k,
\]
we have the **sharp universal linearity threshold**
\[
B(n,k)=P_k(n)\quad\text{for all }n\geq k+1;
\qquad
B(k,k)-P_k(k)=\begin{cases}1,&k=1,\\3,&k\geq2.\end{cases}
\tag{3}
\]
The slopes \(a_k>0\) have a locally finite quadratic-partition generating series:
\[
\sum_{k\geq1}a_ku^k=
\sum_{t\geq2}\left(\prod_{j=1}^{t-1}\frac{1}{1-u^{j(t-j)}}-1\right).
\tag{4}
\]
The zero-frequency count, already obtainable from general avoidance results, is included for completeness: \(B(n,0)=1+\binom{n+1}{2}\).

## Assumptions and scope

All variables \(n,k\) are nonnegative integers, with (1)--(4) applying to \(k\geq1\); words are indexed and binary, not identified up to rotation, reversal, or complementation. Subsequence occurrences are counted with multiplicity by position triples. The formal power series are interpreted coefficientwise, so no analytic convergence is assumed.

## Proof

**Canonical zero-gap representation.** Every word containing exactly \(t\geq1\) zeros has a unique representation
\[
w=1^{g_0}0\,1^{g_1}0\cdots0\,1^{g_{t-1}}0\,1^{g_t},
\qquad g_0,\ldots,g_t\in\mathbb Z_{\geq0}.
\tag{5}
\]
A one in gap \(j\), where \(1\leq j\leq t-1\), has exactly \(j\) zeros to its left and \(t-j\) zeros to its right. Each choice of a left zero, that one, and a right zero creates exactly one occurrence, and every occurrence has this form. Thus
\[
c_{010}(w)=\sum_{j=1}^{t-1}j(t-j)g_j.\tag{6}
\]
The two exterior gaps contribute no occurrences. If the right-hand side is \(k\geq1\), at least one interior gap is nonempty. Since \(j(t-j)\geq t-1\), necessarily \(t-1\leq k\). Thus there are only the finitely many values \(2\leq t\leq k+1\) in (1).

**Exact distribution.** Fix \(t\) and an interior-gap vector satisfying (6), and put \(s=\sum_{j=1}^{t-1}g_j\). The word length is \(t+s+g_0+g_t\). There are \(n-t-s+1\) nonnegative solutions \((g_0,g_t)\) when \(n\geq t+s\), and none otherwise. This proves the second formula in (2). Summing over the two unrestricted exterior gaps contributes \((1-z)^{-2}\), and each interior gap contributes the geometric series \((1-zu^{j(t-j)})^{-1}\). This proves the first formula in (2) and (1), without a convergence assumption. A word with no zeros is all ones; setting \(k=0\), words with zeros must have all interior gaps empty. This yields \(B(n,0)=1+\sum_{t=1}^n(n-t+1)=1+\binom{n+1}{2}\).

**The degree and the exact threshold.** For every vector counted by \(Q_k\), put \(s=\sum_jg_j\geq1\). Equation (6) gives \(k\geq(t-1)s\), with \(2\leq t\leq k+1\). If \(t=2\), then \(s=k\) and \(t+s=k+2\). If \(t\geq3\), then
\[
t+s\leq t+\frac{k}{t-1}\leq k+2,
\]
where the final inequality follows from \((t-2)(k-t+1)\geq0\). Equality in this final inequality occurs only when \(t=k+1\). In that case \(s=1\), and the single interior one must occupy either gap \(1\) or gap \(t-1\), both having weight \(k\). When \(k\geq2\) these are distinct. Therefore there are precisely three top-degree configurations: the unique \(t=2\) configuration, plus the two \(t=k+1\) configurations. When \(k=1\) the two descriptions coincide and there is just one. This proves the assertions about \(\deg Q_k\) and its leading coefficient.

Write \(Q_k(z)=\sum_{m=0}^{k+2}q_{k,m}z^m\), where \(q_{k,m}\geq0\). The first formula in (2) becomes
\[
B(n,k)=\sum_m q_{k,m}\max\{n-m+1,0\}.
\]
When \(n\geq k+1\), every summand is already equal to its unsaturated linear expression, including the zero contribution from \(m=k+2\) at the boundary. The sum is then \((n+1)Q_k(1)-Q_k'(1)=P_k(n)\). At \(n=k\), all terms except \(m=k+2\) remain unsaturated, while the latter would contribute \(-q_{k,k+2}\) to the linear expression. Thus \(B(k,k)-P_k(k)=q_{k,k+2}\), proving both the threshold and its sharpness. Since the \(t=2\) term always exists, \(a_k=Q_k(1)>0\).

Finally, evaluating (1) at \(z=1\) and summing over positive \(k\) gives (4). The subtraction of \(1\) removes each product's constant term, and for a fixed positive power \(u^k\), all \(t>k+1\) contribute zero. Thus this is a well-defined formal series.

## Verification

Two independent counting approaches are supplied as standalone Python 3 programs, without nonstandard dependencies. `verify_gap.py` builds the polynomials \(Q_k\) by exact quadratic-weight compositions and independently enumerates every binary word of length at most \(14\); it also tests the predicted top coefficient and exact boundary correction through \(k=40\). `verify_stream.py` uses a letter-by-letter dynamic program tracking the number of zeros, `01` subsequences, and `010` subsequences; it compares the resulting counts with an independently implemented gap formula for \(n,k\leq30\).

For \(1\leq k\leq8\), the exact eventual polynomials \(P_k(n)\), valid whenever \(n\geq k+1\), are
\[
\begin{array}{c|rrrrrrrr}
k&1&2&3&4&5&6&7&8\\\hline
a_k&1&3&3&7&3&12&5&14\\
d_k&2&9&12&31&18&66&34&92
\end{array}
\]
In particular, the slope sequence is not simply a fixed function of the length of the pattern; it records arithmetic representations of \(k\) by the quadratic weight sets \(\{j(t-j):1\leq j<t\}\).

## Relationship to prior work

Menon and Singh, *Subsequence frequency in binary words* (first posted June 13, 2023), prove a general avoidance formula and explicit counts for fixed frequencies \(0\leq k\leq4\). Their zero-frequency result includes the \(B(n,0)\) expression above, which is not claimed as new. Tian, *Counting occurrences of a pattern in a binary word* (first posted July 3, 2025), provides general occurrence and primitive-word construction algorithms, rather than this specific fixed-frequency polynomial and its sharp threshold. Bruda, *Enumerating binary words restricted by subsequence frequency* (first posted June 30, 2026), proves eventual polynomiality of bounded degree for any binary pattern with at least two runs, and exact degree for several run conditions. Applied to `010`, that theorem predicts eventual degree one, but it supplies neither the finite quadratic-weight partition polynomials \(Q_k\), their all-length generating functions, their explicit all-frequency slopes, nor the exact transition at \(n=k+1\). No claim is made that the broader eventual-polynomiality theorem is new.

## Limitations

The exact quadratic-gap formula is specialized to the binary scattered pattern `010` (and, by bit complementation, `101`). It is not a general solution for arbitrary patterns. The theorem proves linear stabilization and explicit finite coefficient formulas for each fixed positive frequency; it does not provide a simple closed elementary expression for the irregular integer sequence \(a_k\), nor a complete asymptotic for \(a_k\) as \(k\to\infty\). Finite checker runs independently corroborate many coefficients but are not the proof of the universal statements. Priority relative to unindexed or inaccessible work remains a genuine residual risk; no independent external mathematical audit has been performed.

## References

- G. Bruda, *Enumerating binary words restricted by subsequence frequency*, arXiv:2607.02578, first public posting 2026-06-30. https://arxiv.org/abs/2607.02578
- K. Menon and A. Singh, *Subsequence frequency in binary words*, arXiv:2306.07870, first public posting 2023-06-13. https://arxiv.org/abs/2306.07870
- R. Tian, *Counting occurrences of a pattern in a binary word*, arXiv:2507.03205, first public posting 2025-07-03. https://arxiv.org/abs/2507.03205
