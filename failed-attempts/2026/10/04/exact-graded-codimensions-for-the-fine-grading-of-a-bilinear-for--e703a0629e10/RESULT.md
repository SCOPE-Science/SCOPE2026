# Exact graded codimensions for the fine grading of a bilinear-form Jordan algebra
## Finding
Let \(K\) be a field with \(\operatorname{char}K\ne2\). Let \(V\) be an \(n\)-dimensional vector space carrying a nondegenerate symmetric bilinear form \(\beta\), and write
\[
B_n(K)=K1\oplus V,
\qquad
(a1+v)(b1+w)=(ab+\beta(v,w))1+aw+bv.
\]
Choose an orthogonal basis \(v_1,\ldots,v_n\). With \(G=(\mathbb Z/2\mathbb Z)^n\), give \(B_n(K)\) the fine grading
\[
\deg 1=0,\qquad \deg v_i=e_i.
\]
For every \(m\ge1\), its total multilinear graded codimension is
\[
c_m^G(B_n)=2^{-n}\sum_{j=0}^n\binom{n}{j}(n+1-2j)^{m+1}.
\]
A labeled degree assignment contributes dimension \(1\) exactly when every variable has degree in \(\{0,e_1,\ldots,e_n}\) and at most one nonzero degree occurs an odd number of times; otherwise it contributes dimension \(0\). Therefore
\[
\lim_{m\to\infty}\bigl(c_m^G(B_n)\bigr)^{1/m}=n+1=\dim B_n.
\]
For \(n=2\), which is the Klein grading on the three-dimensional Jordan algebra of symmetric \(2\times2\) matrices,
\[
c_m^G=\frac{3^{m+1}+2+(-1)^{m+1}}4.
\]

## Assumptions and scope
The field is arbitrary except for \(\operatorname{char}K\ne2\). The form \(\beta\) is symmetric and nondegenerate. An orthogonal basis exists under this hypothesis, and nondegeneracy gives \(\beta(v_i,v_i)\ne0\) for every basis vector. The codimension here is the dimension of the full multilinear \(G\)-graded polynomial space modulo the graded identities, summed over all labeled degree assignments.

The result is independent of the cardinality of \(K\). It therefore applies both to the finite-field setting of the motivating 2026 paper and to infinite fields.

## Proof
Fix a labeled degree tuple \(\mathbf h=(h_1,\ldots,h_m)\in G^m\). The homogeneous components of the fine grading are
\[
(B_n)_0=K1,\qquad (B_n)_{e_i}=Kv_i,
\]
and every other homogeneous component is zero. Hence if some \(h_r\notin\{0,e_1,\ldots,e_n}\), every graded evaluation in that degree tuple vanishes.

Assume all degrees are in the support, and let \(r_i\) be the number of variables of degree \(e_i\). Because each input homogeneous component is one-dimensional, every multilinear graded polynomial with the fixed degree tuple evaluates to a scalar multiple of a single vector in the homogeneous component of degree \(h_1+\cdots+h_m\). Thus the corresponding multilinear quotient has dimension at most \(1\).

If at least two of the integers \(r_i\) are odd, then the sum degree \(h_1+\cdots+h_m\) has Hamming weight at least \(2\), so its homogeneous component is zero. The quotient dimension is therefore \(0\).

If every \(r_i\) is even, pair variables of each degree \(e_i\) and bracket each pair first. Since
\[
v_i^2=\beta(v_i,v_i)1\ne0,
\]
these pair-products are nonzero scalars, and multiplying the resulting scalars with the neutral variables gives a nonzero evaluation. If exactly one \(r_i\) is odd, do the same pairing and leave one \(v_i\) unpaired; the resulting product is a nonzero scalar multiple of \(v_i\). Hence the quotient dimension is \(1\) exactly in the stated parity cases.

It remains to count the supported labeled degree tuples. For \(p\in(\mathbb Z/2\mathbb Z)^n\), let \(N_p(m)\) be the number of length-\(m\) words in the alphabet \(\{0,e_1,\ldots,e_n}\) whose nonzero-degree parity vector is \(p\). Fourier inversion on \((\mathbb Z/2\mathbb Z)^n\) gives
\[
N_p(m)=2^{-n}\sum_{\varepsilon\in\{\pm1\}^n}
\varepsilon^p\left(1+\sum_{i=1}^n\varepsilon_i\right)^m.
\]
Summing over the parity vectors of Hamming weight at most \(1\), namely \(0,e_1,\ldots,e_n\), multiplies the summand by
\[
1+\sum_{i=1}^n\varepsilon_i.
\]
Therefore
\[
c_m^G(B_n)=2^{-n}\sum_{\varepsilon\in\{\pm1\}^n}
\left(1+\sum_{i=1}^n\varepsilon_i\right)^{m+1}.
\]
Grouping sign vectors by the number \(j\) of negative coordinates yields the announced formula.

The term \(j=0\) equals \(2^{-n}(n+1)^{m+1}\), while every other base has absolute value at most \(n-1\). Hence the \(m\)-th root limit is \(n+1\).

## Verification
The standalone checker `verify.py` exhaustively enumerates degree words for \(1\le n\le6\) and \(1\le m\le8\), compares the parity count with the closed formula, and separately checks the Klein-grading specialization. Its captured output is stored in `verify_output.txt` and ends with `CHECK_OK`.

The checker verifies only the finite combinatorial identity. The arbitrary-field proof above is symbolic and uses only the one-dimensional homogeneous components and the nonzero squares \(v_i^2\).

## Relationship to prior work
Fideles, Salomão, and Riva describe the fine \((\mathbb Z/2\mathbb Z)^n\)-grading of \(B_n\), determine its graded identities over finite fields, and give a basis of the corresponding relatively free graded algebra. Their inspected full-text presentation contains Theorem 3.26 for the fine grading and Theorem 3.27 for the Klein grading, but no occurrence of “codimension”, “cocharacter”, or “PI-exponent” was found in the inspected source. The present result extracts an exact field-independent multilinear codimension sequence directly from the multiplication structure, not from a finite-field interpolation argument.

Koshlukov and Silva study two \(\mathbb Z_2\)-gradings of the symmetric \(2\times2\) Jordan algebra and the scalar grading on \(B_n\) over infinite fields. That grading is different from the fine \((\mathbb Z/2\mathbb Z)^n\)-grading considered here.

## Limitations
No statement is made in characteristic \(2\). The formula concerns multilinear graded codimensions only; it does not enumerate non-multilinear identities over finite fields. The result depends on the fine grading coming from an orthogonal basis and does not claim the same formula for the scalar or classical gradings.

The originality comparison did not locate an equivalent formula, but older literature on graded codimensions of Jordan algebras could contain the same count under different terminology.

## References
1. C. Fideles, M. E. Salomão, E. Riva, “Graded identities for the Jordan algebra of the symmetric matrices of order two over finite fields,” *Finite Fields and Their Applications* 113 (2026), 102826. DOI: 10.1016/j.ffa.2026.102826.
2. P. Koshlukov, D. Diniz P. S. Silva, “2-graded polynomial identities for the Jordan algebra of the symmetric matrices of order two,” arXiv:2009.02530.
