# Boundary completion of the finite \(3\times3\) min-plus Bruhat cell classification

## Finding

Put \(\mathbb T=\mathbb R\cup\{\infty\}\) with tropical sum \(\min\), tropical multiplication \(+\), and matrix product \((U\odot V)_{ij}=\min_k(U_{ik}+V_{kj})\). Let \(B\) be the monoid of upper-triangular \(3\times3\) matrices over \(\mathbb T\). The tropical permutation matrix \(P_p\) has zero in position \((i,p(i))\) and infinity elsewhere. Work **only with target matrices all of whose nine entries are finite real numbers**.

For \(A=(a_{ij})\in\mathbb R^{3\times3}\), set
\[
\begin{aligned}
 d_1&=a_{21}+a_{32}-a_{22}-a_{31},\\
 d_2&=a_{21}+a_{33}-a_{23}-a_{31},\\
 d_3&=a_{11}+a_{32}-a_{12}-a_{31},\\
 d_4&=a_{11}+a_{33}-a_{13}-a_{31},\\
 d_5&=a_{12}+a_{23}-a_{13}-a_{22}.
\end{aligned}
\]
They satisfy \(d_5=d_1-d_2-d_3+d_4\). The following conditions are exact, **with all boundary equalities included**:

**Theorem.**
\[
\begin{aligned}
 A\in B\odot P_{321}\odot B
 &\iff d_1,d_2,d_3,d_4\geq0\ \text{and}\ (d_5\geq0\ \text{or}\ d_2=0\ \text{or}\ d_3=0),\\
 A\in B\odot P_{231}\odot B
 &\iff d_1=0\ \text{and}\ d_2,d_3,d_4\geq0.
\end{aligned}
\]
Here \(321\) means \((p(1),p(2),p(3))=(3,2,1)\), and similarly for \(231\). No other permutation cell contains any finite \(3\times3\) matrix. Consequently,
\[
\boxed{A\text{ admits a min-plus Bruhat decomposition}}
\iff
\boxed{d_1,d_2,d_3,d_4\geq0\quad\text{and}\quad
(d_5\geq0\ \text{or}\ d_1d_2d_3=0).}
\]
The product criterion in the last display is an ordinary product of real numbers: \(d_1d_2d_3=0\) means that at least one of the three defects vanishes. All conditions are invariant under independently adding constants to target rows and columns.

In the four-dimensional space of independent defects, the entire finite decomposable locus consists of the five-inequality region \(d_1,d_2,d_3,d_4,d_5\geq0\) and three additional parts on its exterior side \(d_5<0\): the parts with \(d_1=0\), \(d_2=0\), or \(d_3=0\) inside \(d_1,d_2,d_3,d_4\geq0\). In particular, the finite targets that lie in the \(231\) cell but not the \(321\) cell are exactly those with \(d_1=0\), \(d_2,d_3>0\), and \(0\leq d_4<d_2+d_3\). This distinction, on the four-defect orthant's face \(d_1=0\), is not decided by the five-inequality sufficient condition for the longest cell.

For example,
\[
A_*=\begin{pmatrix}0&-3&-1\\0&-2&-3\\0&0&0\end{pmatrix}
\quad\text{has}\quad(d_1,d_2,d_3,d_4,d_5)=(2,3,3,1,-3).
\]
Although \(d_1,d_2,d_3,d_4>0\), this matrix has no min-plus Bruhat decomposition. It illustrates why retaining only the four defects involving \(a_{31}\) is insufficient. By contrast,
\[
 A_{231}=\begin{pmatrix}0&-3&0\\0&0&-3\\0&0&0\end{pmatrix}
 \quad\text{has}\quad(d_1,d_2,d_3,d_4,d_5)=(0,3,3,0,-6).
\]
This second matrix admits a decomposition, but only via \(231\).

## Assumptions and scope

The entries of the target matrix are arbitrary **finite real numbers**; no tropical nonsingularity is assumed, and equality cases are included. The upper-triangular factors may use \(\infty\) below the diagonal and may initially use \(\infty\) in other positions. Every finite target factorization can be realized with all on-or-above-diagonal factor entries finite, by replacing sufficiently large \(\infty\) entries without changing any attained minima. This justifies the finite normalized factor coordinates used below. There is no statement about targets with infinite entries or about elementary-matrix factorization in the broader sense.

## Proof

**Step 1: allowable permutations and normalization.** For a finite target, \(a_{31}<\infty\). The general Bruhat-product formula gives
\[
a_{31}=\min_{k\geq3,\ p(k)\leq1}\{b_{3k}+c_{p(k),1}\}.
\]
Only \(k=3\) is possible, forcing \(p(3)=1\), so \(p\) is either \(321\) or \(231\). For any factors producing a finite target, replace all their off-diagonal extra infinite entries above the diagonal by sufficiently large reals. A path that was previously unavailable can then be made strictly greater than all nine target minima. This also permits replacing infinite diagonal entries. Multiplying each factor's intermediate column-row pair by opposite tropical scalars normalizes the left diagonal entries to zero. Write the left factor as
\[
U=\begin{pmatrix}0&b&c\\\infty&0&d\\\infty&\infty&0\end{pmatrix}.
\]
For the right upper-triangular factor write
\[
V=\begin{pmatrix}u&v&w\\\infty&x&y\\\infty&\infty&z\end{pmatrix}.
\]

**Step 2: longest cell necessity.** For \(p=321\), the product is exactly
\[
U\odot P_{321}\odot V=
\begin{pmatrix}
c+u&\min(b+x,c+v)&\min(z,b+y,c+w)\\
d+u&\min(x,d+v)&\min(y,d+w)\\
u&v&w
\end{pmatrix}.
\]
Thus \(u=a_{31}\), \(v=a_{32}\), \(w=a_{33}\), \(c=a_{11}-a_{31}\), \(d=a_{21}-a_{31}\). The four inequalities \(d_1,d_2,d_3,d_4\geq0\) follow directly. If both \(d_2>0\) and \(d_3>0\), then \(a_{23}=y\), \(a_{12}=b+x\) and \(x\geq a_{22}\), hence \(b\leq a_{12}-a_{22}\). The upper-right entry also obeys \(a_{13}\leq b+y\). Combining gives \(a_{13}\leq a_{12}-a_{22}+a_{23}\), namely \(d_5\geq0\). This proves necessity, including the equality alternatives.

**Step 3: longest cell sufficiency with explicit factors.** Assume its stated criterion. Set
\[
u=a_{31},\quad v=a_{32},\quad w=a_{33},\quad c=a_{11}-u,\quad d=a_{21}-u,\quad x=a_{22},\quad z=a_{13}.
\]
If \(d_3=0\), take
\[
y=a_{23},\qquad b=\max\{a_{12}-a_{22},\ a_{13}-a_{23}\}.
\]
If \(d_3>0\), take \(b=a_{12}-a_{22}\) and choose
\[
y=\max\{a_{23},\ a_{13}-b\}.
\]
In the latter case, when \(d_5\geq0\) this gives \(y=a_{23}\); when \(d_5<0\), the hypothesis forces \(d_2=0\), so increasing \(y\) does not change \(a_{23}=\min(y,d+w)\). In both cases direct substitution into the displayed product yields each of the nine entries of \(A\). This proves sufficiency for \(321\).

**Step 4: the second cell.** For \(p=231\), multiplication gives exactly
\[
U\odot P_{231}\odot V=
\begin{pmatrix}
c+u&\min(x,c+v)&\min(y,b+z,c+w)\\
d+u&d+v&\min(z,d+w)\\
u&v&w
\end{pmatrix}.
\]
It immediately follows that \(d_1=0\) and \(d_2,d_3,d_4\geq0\). Conversely, under these four conditions choose \(u=a_{31}\), \(v=a_{32}\), \(w=a_{33}\), \(c=a_{11}-u\), \(d=a_{21}-u\), and
\[
x=a_{12},\quad y=a_{13},\quad z=a_{23},\quad b=a_{13}-a_{23}.
\]
Then all nine entries of \(U\odot P_{231}\odot V\) equal the target entries. This proves the second equivalence. Union with the longest cell gives the final criterion.

**Step 5: boundary distinction and examples.** Substituting \(d_1=0\) into the criterion for \(321\) shows that a member of \(231\) can fail to belong to \(321\) only if \(d_2,d_3>0\) and \(d_5=d_4-d_2-d_3<0\), and these conditions suffice. This gives the displayed exclusive membership of \(A_{231}\). The matrix \(A_*\) fails \(321\) because \(d_2,d_3>0\) and \(d_5<0\), and it fails \(231\) because \(d_1>0\).

## Verification

The standalone `verify.py` computes the five defects, implements both equivalences, constructs the explicit factors, and re-multiplies them. With deterministic seed 20261120 it passed 100,000 random forward product checks and 100,000 random conditional inverse checks **for each** permutation. For each permutation it also exhausted all \(3^9=19683\) matrices with entries in \(\{-1,0,1\}\), verifying every predicted positive instance by explicit factor reconstruction. Three boundary-wing examples and the excluded \(A_*\) example were additionally checked. These are finite consistency tests; the universal real statement follows from Steps 1–4, not from enumeration.

Run with `python3 verify.py` from the same directory. Only the Python standard library is required.

## Relationship to prior work

Grigoriev, arXiv:2611.03896v1, proves the dimension of general min-plus Bruhat cells and describes longest-cell membership up to lower-dimensional exceptions. At size three, the condition \(k+s=4\) of Theorem 1.2(i) selects exactly the five minors defining \(d_1,\ldots,d_5\): four with \(k=1,s=3\), and one with \(k=2,s=2,q=1,m=3\). Thus the five-inequality sufficient region is already covered by that theorem; \(A_*\) fails its hypothesis and is not a counterexample. Example 3.1 already exhibits a longest-cell member with \(d_5<0\). What the exact criteria above add is a description of *all* those longest-cell exceptions in size three, with reconstruction, as well as exact membership in the other finite cell \(231\) and the distinction between their boundary loci. Proposition 4.1 of Grigoriev identifies the only possible permutation for a tropically nonsingular target if a factorization exists, rather than giving these membership criteria for arbitrary finite targets.

Niv's *Factorization of Tropical Matrices* (arXiv:1202.3615, published 2014) classifies three-dimensional **elementary** tropical matrix factorizability. That permits arbitrary sequences of elementary factors, not the fixed two upper-triangular factors separated by one permutation required here. Thus that broader factorization theorem does not give this exact two-sided Bruhat membership test. This is a comparison of definitions and implications, not a claim that the 2014 result is weaker in its own setting.

## Limitations

The classification is for finite real \(3\times3\) targets only. It does not classify matrices with infinite target entries or higher dimensions. An equivalent unindexed classification of the same double-cosets cannot be ruled out.

## References

1. D. Grigoriev, *Min-plus Bruhat decomposition*, arXiv:2611.03896v1 (public 2026-11-02), especially Theorem 1.2, proof in Section 3, and Example 3.1. https://arxiv.org/html/2611.03896v1
2. A. Niv, *Factorization of tropical matrices*, arXiv:1202.3615; Journal of Algebra and Its Applications 13 (2014), 1350066, especially Definitions 2.4–2.5 and Lemma 4.5. https://arxiv.org/abs/1202.3615
