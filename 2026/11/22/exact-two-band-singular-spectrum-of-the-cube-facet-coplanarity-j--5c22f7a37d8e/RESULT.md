# Exact two-band singular spectrum of the cube facet-coplanarity Jacobian

## Finding

For every integer \(n\ge3\), the full positive-coordinate-facet coplanarity-minor Jacobian at the standard cube has an exact spectrum with at most two positive levels on even radial vertex motions. In the normalization defined below, if
\[
c=\sum_{\substack{S\subseteq[n]\\|S|\,\mathrm{even}}}a_S\chi_S,\qquad \chi_S(q)=\prod_{j\in S}q_j,
\]
then
\[
\boxed{\|A_n c\|_2^2=2^{n^2-1}\left((n-2)\sum_{|S|=2}a_S^2+n\sum_{\substack{|S|\ge4\\|S|\,\mathrm{even}}}a_S^2\right).}
\]
The zero eigenspace of \(A_n^*A_n\) is the constant mode. The positive eigenvalues, relative to the unnormalized \(\ell^2(Q_n)\) domain inner product, are
\[
\begin{array}{c|c|c}
\text{eigenvalue}&\text{multiplicity}&\text{Walsh sector}\\\hline
(n-2)2^{n^2-n-1}&\binom n2&|S|=2\\
n2^{n^2-n-1}&2^{n-1}-1-\binom n2&|S|\ge4\text{ even}
\end{array}
\]
(the second multiplicity is zero for \(n=3\)). The best lower squared-norm bound is
\[
\boxed{\|A_n c\|_2^2\ge (n-2)2^{n^2-n-1}\|c-\overline c\mathbf1\|_{\ell^2(Q_n)}^2,\quad \overline c=2^{-n}\sum_{q\in Q_n}c(q).}
\]
Equality holds exactly when \(c-\overline c\mathbf1\) belongs to the span of the weight-two Walsh characters. The sharp nonzero singular-value condition number is \(1\) for \(n=3\) and \(\sqrt{n/(n-2)}\) for \(n\ge4\), tending to \(1\) with increasing dimension.

## Assumptions and scope

Set \(Q_n=\{-1,1\}^n\) and consider even real vertex labels
\[
E_n=\{c:Q_n\to\mathbb R:c(-q)=c(q)\}.
\]
For each \(i\in[n]\), set \(F_{i,+}=\{q\in Q_n:q_i=1\}\), of cardinality \(N=2^{n-1}\). For every **unordered** subset \(I\subset F_{i,+}\) with \(|I|=n+1\), define
\[
D_{i,I}(c)=\det\big[\big((1+c(q))q,1\big)\big]_{q\in I},
\]
where rows of the determinant are taken in any fixed ordering. Let \(\mathcal R_n(c)=(D_{i,I}(c))_{i,I}\) and \(A_n=D\mathcal R_n(0)\). Its codomain has exactly \(n\binom{2^{n-1}}{n+1}\) coordinates. Order changes affect individual determinant signs but not the summed squared norm. Use **counting-measure** inner products \(\|c\|_{\ell^2(Q_n)}^2=\sum_qc(q)^2\) and \(\|A_nc\|_2^2=\sum_{i,I}|D D_{i,I}(0)[c]|^2\). Do not divide the target by the number of minors; do not count the negative facets again. The Fourier normalization is \(a_S=2^{-n}\sum_qc(q)\chi_S(q)\), so \(\|c\|^2=2^n\sum_Sa_S^2\).

## Proof

**1. Linearized determinants are affine-fitting residual minors.** Fix a positive facet \(F=F_{i,+}\) and a subset \(I\) as above. At \(c=0\), the \(i\)-th spatial column of the determinant is the all-one column, which coincides with the last homogeneous column. Differentiation in any different spatial column leaves this duplication intact and contributes zero. Differentiating the \(i\)-th column yields the values \(c(q)q_i=c(q)\) for \(q\in F\). Therefore the derivative is, up to a sign independent of \(c\), the determinant of the row matrix
\[
[\,1,\ q_j\ (j\ne i),\ c(q)\,]_{q\in I}.
\]

**2. Sum all minors using Cauchy–Binet.** Let \(B_i\) be the \(N\times n\) matrix whose columns are \(1\) and the \(n-1\) free sign coordinates on \(F\); let \(f_i=(c(q))_{q\in F}\). Orthogonality of the sign functions on the facet gives \(B_i^TB_i=NI_n\). For \(M_i=[B_i\mid f_i]\), Cauchy–Binet followed by the Schur complement yields
\[
\begin{aligned}
\sum_{I\in\binom{F}{n+1}}|\det(M_i)_I|^2
&=\det(M_i^TM_i)\\
&=N^n\left(f_i^Tf_i-N^{-1}f_i^TB_iB_i^Tf_i\right)\\
&=N^n\|(I-P_i)f_i\|_2^2,
\end{aligned}
\]
where \(P_i=N^{-1}B_iB_i^T\) is orthogonal projection onto affine functions on the facet. Thus the identity has already summed **every** prescribed coplanarity minor with the correct multiplicity.

**3. Determine the Walsh residuals.** The restriction of \(\chi_S\) to \(F_{i,+}\) is the free-coordinate Walsh character on \(S\setminus\{i\}\). For even \(|S|\), its degree is \(|S|-1\) when \(i\in S\), and \(|S|\) otherwise. The projection \(P_i\) retains exactly degrees zero and one. Hence the constant character contributes zero on every facet; a degree-two character contributes on exactly \(n-2\) positive facets; and every even-degree character of degree at least four contributes on all \(n\) positive facets. A contributing character has squared norm \(N\) on each facet.

Distinct even Walsh characters restrict to distinct characters on any fixed \(F_{i,+}\): equality would require \(S\triangle T\subseteq\{i\}\), but \(|S\triangle T|\) is even. Their residuals under \(I-P_i\) are therefore orthogonal. The full quadratic form is diagonal, giving
\[
\|A_nc\|_2^2=N^{n+1}\left((n-2)\sum_{|S|=2}a_S^2+n\sum_{\substack{|S|\ge4\\|S|\,\mathrm{even}}}a_S^2\right).
\]
Finally \(N^{n+1}=2^{(n-1)(n+1)}=2^{n^2-1}\).

**4. Eigenvalues, sharpness, and multiplicities.** Divide the preceding squared norms by \(\|\chi_S\|_{\ell^2(Q_n)}^2=2^n\). There are \(\binom n2\) two-coordinate characters, and the total number of even characters is \(2^{n-1}\), including the constant. Both eigenvalues are positive for \(n\ge3\); the higher band exists precisely for \(n\ge4\). The smaller band is always the quadratic band and is attained by any nonzero weight-two character. The lower-norm equality classification follows by positivity of the band gap, and the condition numbers follow by taking square roots. For \(n=3\) there is only one positive band, giving condition number \(1\).

## Verification

A standalone standard-library Python program, `verify.py`, enumerates **all** \((n+1)\)-subsets on every positive facet in dimensions \(n=3,4,5\), evaluates the linearized determinants exactly using the integer Bareiss algorithm, and compares squared sums with the stated powers of two. It also computes three mixed inner products in dimension four and verifies they are exactly zero. The recorded execution produced **15 passing exact checks**; in particular the pairs of degree-two and degree-four squared norms are \(65536,131072\) at \(n=4\) and \(50331648,83886080\) at \(n=5\). Run `python3 verify.py` in a directory containing the extracted file. The program checks finitely many dimensions; the proof above, not the finite calculation, establishes all integers \(n\ge3\).

## Relationship to prior work

Jiménez Cuevas, *Discrete Coplanarity Rigidity and Local Mahler Volume Growth Near the Cube* (arXiv:2606.14709v4), Section 4, defines exactly this positive-facet complete-minor operator and proves its even-Walsh diagonalization and nonconstant injectivity. Its Theorem 4.6 explicitly leaves all general coefficients \(\lambda_{n,k}\) without a closed form and supplies only \(\lambda_{3,2}=256\). The statement here gives their complete closed forms, all multiplicities, the exact smallest singular value and sharp Euclidean stability for every dimension. The prior diagonalization and kernel result are not claimed anew.

Himmelmann, Schulze and Winter, *Rigidity of Polytopes with Edge Length and Coplanarity Constraints* (arXiv:2505.00874v3; *International Mathematics Research Notices*, 2026), study the different problem of first-order polytope flexes preserving **edge lengths as well as facet planarity**. Their general rigidity framework neither fixes the radial even-label slice nor defines the complete facet-minor Euclidean normalization whose exact spectrum is computed here. Standard Walsh orthogonality and Cauchy–Binet are well-known tools; their specific combination produces the new explicit coefficients for this geometric operator.

## Limitations

This is a theorem about the **linearized** coplanarity-minor map at the standard cube, on the even radial-label space with a fully specified counting-measure norm. It is not a formula for the nonlinear Mahler-product Hessian, not a sharp bound in the maximum norm, not a proof of global polytope rigidity, and not necessarily valid after selecting a subset of minors or reweighting them. In particular, the source's local nonlinear estimates use different norms. An independent literature-priority assessment and independent mathematical audit have not been performed.

## References

1. D. M. Jiménez Cuevas, *Discrete Coplanarity Rigidity and Local Mahler Volume Growth Near the Cube*, arXiv:2606.14709v4 (2026), especially Section 4, Definition 4.1 and Theorem 4.6. https://arxiv.org/abs/2606.14709
2. M. Himmelmann, B. Schulze and M. Winter, *Rigidity of Polytopes with Edge Length and Coplanarity Constraints*, arXiv:2505.00874v3 (2026); *International Mathematics Research Notices* 2026(7), rnag055. https://arxiv.org/abs/2505.00874
3. R. O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press (2014), for standard Fourier–Walsh orthogonality. https://arxiv.org/abs/2105.10386
