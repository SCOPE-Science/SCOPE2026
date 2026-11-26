# A sharp short-block deletion-covering bound and the quaternary optimum

## Finding
For every integer \(q\ge 2\), the minimum size \(D(q,4,1)\) of a length-four \(q\)-ary single-deletion covering code satisfies
\[
D(q,4,1)\ge \left\lceil\frac{q(2q^2+q+1)}8\right\rceil.
\]
For the four-symbol alphabet the inequality is attained:
\[
\boxed{D(4,4,1)=19}.
\]
Both statements hold for arbitrary alphabets of the indicated cardinalities, without linearity or other structural restrictions on the code.

## Assumptions and scope
Fix a finite alphabet \(\Sigma\) of size \(q\ge2\). For \(x=x_1x_2x_3x_4\in\Sigma^4\), let \(\mathcal D(x)\subseteq\Sigma^3\) be the **set of distinct** words obtained by deleting exactly one position of \(x\). A single-deletion covering code \(C\subseteq\Sigma^4\) satisfies \(\bigcup_{x\in C}\mathcal D(x)=\Sigma^3\). The number \(D(q,4,1)\) is the least possible size \(|C|\). Repetitions arising from different deletions of the same word do not increase the size of its deletion shadow.

## Proof
**A universal rational packing of deletion shadows.** Define a nonnegative weight on every \(y=abc\in\Sigma^3\) by
\[
w(abc)=\begin{cases}
1/2,&a=b=c,\\
3/8,&a=b\ne c\ \text{or}\ a\ne b=c,\\
1/8,&a=c\ne b,\\
1/4,&a,b,c\ \text{pairwise distinct}.
\end{cases}
\]
We claim that every \(x\in\Sigma^4\) obeys
\[
\sum_{y\in\mathcal D(x)}w(y)\le1.\tag{1}
\]
Relabeling distinct symbols of \(x\) bijectively cannot change the left side. There are exactly fifteen equality patterns for a four-position word. Write each pattern in restricted-growth normal form, assigning label zero to the first symbol and introducing each new label in increasing order of first appearance. Deleting each of the four positions, identifying coincident outputs, and summing the displayed rational weights gives the following **exhaustive** values:

| Four-position equality pattern | Shadow weight | Four-position equality pattern | Shadow weight | Four-position equality pattern | Shadow weight |
|---|---:|---|---:|---|---:|
| `0000` | \(1/2\) | `0001` | \(7/8\) | `0010` | \(1\) |
| `0011` | \(3/4\) | `0012` | \(1\) | `0100` | \(1\) |
| `0101` | \(1\) | `0102` | \(1\) | `0110` | \(7/8\) |
| `0111` | \(7/8\) | `0112` | \(1\) | `0120` | \(3/4\) |
| `0121` | \(1\) | `0122` | \(1\) | `0123` | \(1\) |

This proves (1) for every alphabet: equality patterns requiring more than \(q\) symbols simply do not occur.

Among all target words \(y\in\Sigma^3\), precisely \(q\) have all three symbols equal, \(2q(q-1)\) have equality between adjacent positions only, \(q(q-1)\) have equality between first and last positions only, and \(q(q-1)(q-2)\) have three distinct symbols. Therefore
\[
\sum_{y\in\Sigma^3}w(y)
=\frac q2+\frac{7q(q-1)}8+\frac{q(q-1)(q-2)}4
=\frac{q(2q^2+q+1)}8.\tag{2}
\]
If \(C\) covers \(\Sigma^3\), all weights are nonnegative, so
\[
\frac{q(2q^2+q+1)}8
=\sum_{y\in\Sigma^3}w(y)
\le\sum_{x\in C}\sum_{y\in\mathcal D(x)}w(y)
\le |C|.
\]
Taking a ceiling proves the claimed universal lower bound.

**Attaining the bound for four symbols.** Set \(\Sigma=\{0,1,2,3\}\). The following \(19\) words form a covering code:

```text
0010 0032 0213 1010 1012 1033 1131 1230 2020 2031
2121 2122 2323 3011 3022 3030 3132 3210 3313
```

Their distinct length-three deletion descendants together comprise **all** \(4^3=64\) length-three words over \(\Sigma\). Explicitly, exactly \(60\) targets have one covering codeword and exactly \(4\) targets have two; no target is missed. This is proved by the standalone finite enumeration in `verify.py`, which reconstructs every descendant directly from the displayed codewords. Thus \(D(4,4,1)\le 19\). Formula (2) equals \(37/2\) at \(q=4\), so every covering code has at least \(\lceil37/2\rceil=19\) words. The upper and lower bounds coincide.

## Verification
Running `python3 verify.py` (Python standard library only) proves the fifteen universal equality-pattern inequalities exactly using rational arithmetic, recomputes the total weight formula for independently enumerated small alphabets, and verifies the complete \(64\)-word deletion cover of the explicit \(19\)-word code. The saved output is `verification_output.txt`; its last line is `VERIFY_OK`. The logical all-alphabet step is the exhaustive equality-pattern classification together with the symbolic count (2), **not** extrapolation from the finite tests. No integer-programming solution status or floating-point bound is used as proof.

## Relationship to prior work
Xie, Sun, and Ge (2026) introduce and analyze precisely this deletion-covering parameter and prove a basic \(q^{n-R}/\binom nR\) lower bound and asymptotically tight large-alphabet constructions. Their Sections I and V do not determine \(D(4,4,1)\) or give the rational equality-pattern bound proved here. The earlier paper of Lenz, Rashtchian, Siegel, and Yaakobi presents a different general weighted lower bound (Theorem 3), along with nonbinary covering constructions, without determining this four-symbol, length-four optimum. In particular the elementary bound is \(16\) when \(q=4,n=4,R=1\), while the present weighted certificate raises it to \(19\).

The publicly available exact ternary length-five result concerns \(D(3,5,1)=21\), and the exact odd-alphabet length-three result concerns \(D(q,3,1)\); neither implies an exact value for \(D(4,4,1)\). Results on maximal deletion-**correcting** codes or Hamming/edit-metric coverings are not statements about this deletion-**covering** minimum. The fractional-shadow method is a standard general technique; the specialized universal weights and sharp four-symbol construction are the asserted contribution.

## Limitations
The formula is a lower bound, not an exact evaluation for every alphabet size. Exact optimality is established here only for the four-symbol length-four single-deletion covering parameter. No uniqueness or classification of the optimal \(19\)-word codes is claimed. No conclusion is drawn for longer blocks, multiple deletions, or the distinct insertion-covering problem. Mathematical originality is assessed against examined public sources, not guaranteed against every unindexed historical computation.

## References
1. C. Xie, Y. Sun, and G. Ge, “New bounds for covering codes under insertions or deletions,” arXiv:2606.15379, first public version 13 June 2026, https://arxiv.org/abs/2606.15379.
2. A. Lenz, C. Rashtchian, P. H. Siegel, and E. Yaakobi, “Covering Codes using Insertions or Deletions,” arXiv:1911.09944, first public version 22 November 2019, https://arxiv.org/abs/1911.09944.
3. “Exact ternary length-five single-deletion covering number,” publicly available research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-ternary-length-five-single-deletion-covering-number--fc12c4f98e83.
4. “Exact length-three single-deletion covering number for odd alphabets,” publicly available research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-length-three-single-deletion-covering-number-for-odd-alpha--9607d49b27ed.
