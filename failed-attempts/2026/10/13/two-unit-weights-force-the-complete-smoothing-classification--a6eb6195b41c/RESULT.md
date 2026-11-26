# Two unit weights force the complete smoothing classification
## Finding
Let \(a,b\) be positive integers and set
\[
X=\mathbf P(1,1,a,b).
\]
Then \(X\) admits a \(\mathbb Q\)-Gorenstein smoothing to \(\mathbf P^3\) if and only if, up to interchanging \(a\) and \(b\),
\[
(a,b)=(1,1)\qquad\text{or}\qquad(a,b)=(2,4).
\]
Thus the complete two-unit-weight slice consists of
\[
\mathbf P(1,1,1,1)=\mathbf P^3
\quad\text{and}\quad
\mathbf P(1,1,2,4).
\]

This resolves the two-unit-weight subfamily without assuming canonical singularities or the codimension-two \(A\)-type hypothesis used in stronger general classification results.

## Assumptions and scope
The weights \(a,b\) are arbitrary positive integers. Because two weights are \(1\), the weighted projective threefold \(\mathbf P(1,1,a,b)\) is automatically well formed.

The deformation under consideration is a \(\mathbb Q\)-Gorenstein smoothing whose general fiber is \(\mathbf P^3\).

No converse is claimed for other weight patterns. In particular, the argument does not classify \(\mathbf P(1,a,b,c)\) with only one unit weight.

## Proof
A necessary condition for a well-formed weighted projective threefold
\[
\mathbf P(w_0,w_1,w_2,w_3)
\]
to admit a \(\mathbb Q\)-Gorenstein smoothing to \(\mathbf P^3\) is the anticanonical volume equation
\[
(w_0+w_1+w_2+w_3)^3=64w_0w_1w_2w_3.
\]
For
\[
(w_0,w_1,w_2,w_3)=(1,1,a,b),
\]
this becomes
\[
(a+b+2)^3=64ab.
\]

Put
\[
s=a+b.
\]
By the arithmetic-geometric mean inequality,
\[
ab\le \frac{s^2}{4},
\]
so
\[
(s+2)^3=64ab\le 16s^2.
\]
For
\[
F(s)=(s+2)^3-16s^2,
\]
one has
\[
F(9)=35>0
\]
and
\[
F'(s)=3s^2-20s+12>0
\]
for every real \(s\ge9\). Hence the displayed inequality is impossible for \(s\ge9\), and therefore
\[
2\le s\le8.
\]

The volume equation also says
\[
ab=\frac{(s+2)^3}{64}\in\mathbb Z.
\]
Since
\[
4\le s+2\le10,
\]
divisibility by \(64=2^6\) forces \(s+2\) to be divisible by \(4\). The only possibilities in this interval are
\[
s+2=4\qquad\text{or}\qquad s+2=8.
\]
Thus
\[
s=2\qquad\text{or}\qquad s=6.
\]

If \(s=2\), then the volume equation gives \(ab=1\), so
\[
(a,b)=(1,1).
\]
If \(s=6\), then it gives \(ab=8\). The positive integers with sum \(6\) and product \(8\) are
\[
\{a,b\}=\{2,4\}.
\]
This proves necessity.

For sufficiency, \(\mathbf P(1,1,1,1)=\mathbf P^3\) is already smooth. The space \(\mathbf P(1,1,2,4)\) is one of the standard weighted-projective \(\mathbb Q\)-Gorenstein degenerations of \(\mathbf P^3\); the initiating source recalls it among the known smoothable families. Hence both possibilities occur.

## Verification
The initiating paper was checked in full text at its setup, Lemma 2.1, Example 2.4, Proposition 3.2, Theorem 4.1, and Remark 4.2.

Lemma 2.1 gives the exact volume equation
\[
S^3=64w_0w_1w_2w_3
\]
for every well-formed weighted projective threefold admitting the required smoothing. Example 2.4 records the two known smoothable families and includes \(\mathbf P(1,1,2,4)\). The paper's stronger classification theorems impose additional gcd or \(A\)-type hypotheses and do not state the unrestricted two-unit-weight classification proved here.

The earlier paper of DeVleming was also checked at Proposition 4.47 and the following discussion. It derives the same volume equation, lists \(\mathbf P(1,1,1,1)\) and \(\mathbf P(1,1,2,4)\) among the first computer-generated solutions, and exhibits a smoothing of \(\mathbf P(1,1,2,4)\), but does not state that these exhaust every solution with two unit weights.

The proof above is exact. The only inequality is \(ab\le(a+b)^2/4\); after it bounds \(a+b\), the remaining divisibility argument is exhaustive and contains no computational search.

## Relationship to prior work
DeVleming proved the anticanonical volume obstruction and exhibited \(\mathbf P(1,1,2,4)\) as a smoothable example, while leaving the general weighted-projective classification open. Chen and Lee add Hilbert-polynomial and local smoothing-section constraints and prove the expected classification in several broader subfamilies.

The present result isolates the natural family \(\mathbf P(1,1,a,b)\) and closes it completely using only the volume obstruction. In contrast with the canonical two-heavy classifications available elsewhere, no singularity-class assumption is required here.

A recent paper of DeVleming, Li, and Torres studies weighted-projective degenerations of projective space broadly. Its abstract and the initiating paper's discussion were checked; the initiating paper explicitly characterizes that work as providing deformation-gluing tools rather than the desired numerical classification. Direct full-text access to that preprint was unavailable in this check, so possible unstated special-case overlap is retained as a residual literature risk.

Targeted searches for the exact two-unit-weight classification, the specialized equation
\[
(a+b+2)^3=64ab,
\]
and the assertion that only \(\mathbf P^3\) and \(\mathbf P(1,1,2,4)\) occur did not locate a covering statement.

## Limitations
This is a classification only of weighted projective threefolds with at least two weights equal to \(1\). It does not address the substantially harder one-unit-weight family \(\mathbf P(1,a,b,c)\).

The argument establishes the exact smoothing classification in this slice because both surviving volume-equation solutions are known to be smoothable. It does not claim that the volume equation is sufficient in any larger family.

## References
J. A. Chen and Y. Lee, “Weighted projective spaces admitting \(\mathbb Q\)-Gorenstein smoothings to \(\mathbf P^3\),” arXiv:2609.37242v1, first public 2026-09-29.

K. DeVleming, “Moduli of surfaces in \(\mathbf P^3\),” Compositio Mathematica 158 (2022), 1329–1374, especially Proposition 4.47 and Example 4.51.

K. DeVleming, J. Li, and S. Torres, “Weighted projective degenerations of \(\mathbf P^n\),” arXiv:2606.21660.
