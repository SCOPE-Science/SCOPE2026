# Exact hull spectrum of balanced fully twisted Reed–Solomon codes
## Finding

Let \(q\) be an odd prime power and \(k\ge3\) with \(2k\mid(q-1)\). In the Sun–Chen–Liu–Zhang–Wang fully twisted Reed–Solomon family of length \(n=2k\), take the evaluation set to be the multiplicative subgroup of order \(2k\), hooks \(h_i=i-1\), twists \(t_i=i\), and nonzero twist coefficients \(\boldsymbol{\eta}=(\eta_1,\ldots,\eta_k)\in(\mathbb F_q^\ast)^k\). Then the Euclidean hull dimension is exactly \[\dim(C_{\boldsymbol{\eta}}\cap C_{\boldsymbol{\eta}}^\perp)=\mathbf 1_{\{\eta_1^2=-1\}}+\#\{i\in\{2,\ldots,k\}:\eta_i+\eta_{k+2-i}=0\}.\] If \(r_q=2\) for \(q\equiv1\pmod4\) and \(r_q=0\) for \(q\equiv3\pmod4\), \(p=\lfloor(k-1)/2\rfloor\), and \(f=1\) for even \(k\) and \(f=0\) for odd \(k\), the complete hull enumerator is \[\sum_{\boldsymbol{\eta}\in(\mathbb F_q^\ast)^k}z^{\dim\operatorname{Hull}(C_{\boldsymbol{\eta}})}=(q-1)^f((q-1-r_q)+r_qz)\big((q-1)(q-2)+(q-1)z^2\big)^p.\] In particular, the sufficient LCD conditions in Theorem 4.2(ii) of arXiv:2609.16921v1 are necessary as well in the balanced case, and the exact number of LCD twist vectors is \[(q-1)^f(q-1-r_q)\big((q-1)(q-2)\big)^p.\]

## Assumptions and scope

Let \(q\) be an odd prime power, let \(k\ge3\), and assume \(2k\mid(q-1)\). Let
\[
A\subset\mathbb F_q^\ast
\]
be the multiplicative subgroup of order \(n=2k\), and enumerate its elements as the evaluation vector \(\boldsymbol{\alpha}\). Consider the fully twisted Reed–Solomon code from the recent construction with
\[
\boldsymbol{h}=(0,1,\ldots,k-1),\qquad
\boldsymbol{t}=(1,2,\ldots,k),\qquad
\boldsymbol{\eta}\in(\mathbb F_q^\ast)^k.
\]
The ordering of the elements of \(A\) changes the code only by a coordinate permutation and therefore does not affect its hull dimension.

Write
\[
\operatorname{Hull}(C)=C\cap C^\perp.
\]
The result concerns this precise balanced case \(n=2k\). It does not claim an analogous closed form for the other two twist-overlap regimes in the source paper.

## Proof

The source paper writes the generator rows in the Vandermonde basis
\[
V_j=(\alpha_1^j,\ldots,\alpha_n^j).
\]
When \(n=2k\), the \(k\) distinct twist parameters automatically satisfy \(t_i=i\). Hence the generator rows are
\[
C_i=V_{i-1}+\eta_iV_{k+i-1},
\qquad 1\le i\le k.
\]

The same source gives parity-check rows \(H_m\). Multiplying each parity-check row by the nonzero scalar \(n\) does not change the row space or any rank. In the balanced case the exceptional indices satisfy
\[
m_i=k+1-i.
\]
With respect to the Vandermonde basis, the stacked matrix formed from the \(C_i\) and the rescaled \(H_m\) can therefore be permuted into independent \(2\times2\) blocks.

The block involving \(C_1\) and \(H_k\), on coordinates \(V_0,V_k\), is
\[
B_1=
\begin{pmatrix}
1&\eta_1\\
-\eta_1&1
\end{pmatrix},
\qquad
\det B_1=1+\eta_1^2.
\]

For every \(2\le i\le k\), the block involving \(C_i\) and \(H_{i-1}\), on coordinates \(V_{i-1},V_{k+i-1}\), is
\[
B_i=
\begin{pmatrix}
1&\eta_i\\
1&-\eta_{k+2-i}
\end{pmatrix},
\qquad
\det B_i=-(\eta_i+\eta_{k+2-i}).
\]
Each singular block has rank exactly \(1\), because its first column is nonzero. Thus the rank deficiency of the entire \(2k\times2k\) stacked matrix is exactly
\[
\mathbf 1_{\{\eta_1^2=-1\}}
+\#\{i\in\{2,\ldots,k\}:\eta_i+\eta_{k+2-i}=0\}.
\]

For two \(k\)-dimensional subspaces \(C,C^\perp\subseteq\mathbb F_q^{2k}\),
\[
\operatorname{rank}
\begin{pmatrix}G_C\\H_C\end{pmatrix}
=\dim(C+C^\perp)
=2k-\dim(C\cap C^\perp).
\]
Therefore the rank deficiency above is exactly the hull dimension, proving the first formula.

It remains to count twist vectors. The involution
\[
i\longmapsto k+2-i
\]
on \(\{2,\ldots,k\}\) has
\[
p=\left\lfloor\frac{k-1}{2}\right\rfloor
\]
two-element orbits and, precisely when \(k\) is even, one fixed point. At a fixed point the singularity condition would be \(2\eta_i=0\), impossible because \(q\) is odd and \(\eta_i\ne0\).

For each two-element orbit \(\{i,j\}\), there are
\[
(q-1)(q-2)
\]
choices with \(\eta_i+\eta_j\ne0\), contributing hull dimension \(0\), and
\[
q-1
\]
choices with \(\eta_j=-\eta_i\), contributing hull dimension \(2\).

Finally, the equation \(\eta_1^2=-1\) has
\[
r_q=
\begin{cases}
2,&q\equiv1\pmod4,\\
0,&q\equiv3\pmod4
\end{cases}
\]
solutions in \(\mathbb F_q^\ast\). Thus the first coordinate contributes the factor
\[
(q-1-r_q)+r_qz,
\]
every two-element orbit contributes
\[
(q-1)(q-2)+(q-1)z^2,
\]
and the possible fixed coordinate contributes \(q-1\). Multiplying these independent factors gives the stated hull enumerator. Its constant coefficient is the exact number of LCD twist vectors.

## Verification

The bundled standard-library verifier constructs the actual generator and parity-check matrices over prime fields, computes the rank of the stacked matrix directly, and compares the resulting hull dimension with the formula above.

It exhausts all \(12^3=1728\) twist vectors for \((q,k)=(13,3)\), all \(18^3=5832\) vectors for \((q,k)=(19,3)\), and all \(16^4=65536\) vectors for \((q,k)=(17,4)\). The three exact hull histograms are respectively
\[
1320+264z+120z^2+24z^3,
\]
\[
5508+324z^2,
\]
and
\[
53760+7680z+3584z^2+512z^3.
\]
All agree exactly with the product formula. These finite computations are checks of the algebra; the theorem for arbitrary admissible \(q\) and \(k\) follows from the block decomposition.

## Relationship to prior work

Sun, Chen, Liu, Zhang, and Wang introduce the fully twisted family used here and prove in their Theorem 4.2(ii) that, when \(n=2k\), the conditions
\[
1+\eta_1^2\ne0,\qquad
\eta_i+\eta_{k+2-i}\ne0\quad(2\le i\le k)
\]
are sufficient for the code to be LCD. Their proof displays exactly the \(2\times2\) blocks used above, but the theorem is stated only as a sufficient LCD criterion and does not extract the rank deficiency or count the twist vectors by hull dimension.

Meena, Awasthi, and Sharma study a different double-twisted family with fixed twists \((1,2)\), give MDS/AMDS criteria, and report examples and counts together with hull dimensions up to \(3\). That family has only two twist terms, whereas the present result concerns the fully twisted balanced family with \(k\) twist terms and gives a closed hull enumerator for every admissible \(k\ge3\).

The new statement is therefore a complete rank classification inside the balanced branch of the recent fully twisted construction, rather than another sufficient construction.

## Limitations

The theorem requires the source paper's multiplicative-subgroup evaluation set and the balanced length \(n=2k\). It does not treat arbitrary evaluation sets, column multipliers, even characteristic, or the other overlap regimes of Theorem 4.2. The originality assessment is literature-dependent: exact-criterion, hull-enumerator, random-twist, and coefficient-formula searches found no equivalent statement, but an older result under different multi-twisted terminology could have been missed.

## References

1. Shuo Sun, Wenwen Chen, Chao Liu, Yaozong Zhang, and Xiaoqiang Wang, *Constructions of LCPs and LCD codes from twisted Reed-Solomon codes*, arXiv:2609.16921v1, first public version 2026-09-15. Primary MSC 94B05.
2. Kapish Chand Meena, Ambrish Awasthi, and Rajendra K. Sharma, *LCD and non-LCD (A)MDS DTRS codes with all possible hooks*, Advances in Mathematics of Communications, early access 2026-02-06, DOI 10.3934/amc.2026019.
