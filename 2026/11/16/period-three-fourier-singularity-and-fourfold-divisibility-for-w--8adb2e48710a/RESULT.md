# Period-three Fourier singularity and fourfold divisibility for wheel spanning-tree kernels

## Finding
Let \(W_n\) be the simple wheel with \(n\ge3\) labeled rim vertices, one hub, and \(2n\) edges. Write \(\mathcal T_n\subseteq\mathbb F_2^{E(W_n)}\) for the incidence vectors of its spanning trees. For \(b\in\mathbb F_2^{E(W_n)}\), use the unnormalized Walsh coefficient
\[
K_n(b)=\sum_{T\in\mathcal T_n}(-1)^{\sum_{e\in T}b_e}.
\]
Then the complete zero-free classification is
\[
\boxed{\ K_n(b)\ne0\ \text{for all }b\quad\Longleftrightarrow\quad 3\nmid n.\ }
\]
If \(3\nmid n\), every coefficient is odd. If \(n=3k\), every coefficient is divisible by four, and at least \(4^k\) distinct frequencies have coefficient exactly zero. In particular, convolution by the spanning-tree indicator on \(\mathbb F_2^{2n}\) is invertible over \(\mathbb C\) exactly for \(3\nmid n\).

## Assumptions and scope
The integer \(n\) ranges over all \(n\ge3\); thus the rim is a simple cycle, including the triangular rim at \(n=3\). No averaging is used in the Walsh transform. Label the rim edges \(e_i=\{i,i+1\}\) (indices cyclic modulo \(n\)) and hub spokes \(h_i=\{0,i\}\). A frequency is an arbitrary choice of independent signs \(r_i=(-1)^{b_{e_i}}\) and \(s_i=(-1)^{b_{h_i}}\) in \(\{\pm1\}\).

## Proof
**1. Determinantal Fourier representation.** The weighted matrix-tree identity is a polynomial identity and remains valid when the edge weights are negative. Removing the hub row and column gives
\[
K_n(b)=\det M_n(r,s),\qquad
(M_nx)_i=s_ix_i+r_{i-1}(x_i-x_{i-1})+r_i(x_i-x_{i+1}).
\]
The formula holds for every sign assignment, since the determinant expands into the weighted products over all spanning trees. Consequently \(K_n\) vanishes precisely when its signed reduced Laplacian has a nonzero nullvector.

**2. Zero-free dimensions.** Let \(L_0=2\), \(L_1=1\), and \(L_{j+2}=L_{j+1}+L_j\) be the Lucas sequence. Classical wheel-tree enumeration gives
\[
|\mathcal T_n|=L_{2n}-2.
\]
Modulo two the Lucas sequence repeats \(0,1,1\) with period three. Therefore \(|\mathcal T_n|\) is odd exactly when \(3\nmid n\). Every \(K_n(b)\) is a signed sum of \(|\mathcal T_n|\) units, so \(K_n(b)\equiv|\mathcal T_n|\pmod2\) and is nonzero in those dimensions.

**3. Explicit singular frequencies.** Suppose \(n=3k\). Choose arbitrary \(u_j,t_j\in\{\pm1\}\) for \(0\le j<k\), with \(t_{-1}=t_{k-1}\). Prescribe the rim and spoke signs, respectively, by
\[
\begin{aligned}
r_{3j+1}&=u_j,&r_{3j+2}&=t_j,&r_{3j+3}&=t_j,\\
s_{3j+1}&=t_{j-1},&s_{3j+2}&=t_j,&s_{3j+3}&=-t_j.
\end{aligned}
\]
Consider the cyclic vector \(x=(1,1,2,1,1,2,\ldots,1,1,2)^\mathsf T\). For each successive triple, the three row expressions in the displayed matrix equation are
\[
 t_{j-1}(1)+(t_{j-1})(1-2)+u_j(1-1)=0,\quad
 t_j(1)+u_j(1-1)+t_j(1-2)=0,\quad
 (-t_j)(2)+t_j(2-1)+t_j(2-1)=0.
\]
Thus \(M_n(r,s)x=0\), and \(K_n(b)=0\). The \(2k\) freely chosen signs yield exactly \(2^{2k}=4^k\) distinct frequencies, proving both existence and the stated lower bound.

**4. The modulo-four strengthening.** For any set \(B\) of negative-weight edges, and with \(N_e\) denoting the number of spanning trees containing \(e\), the elementary identity \((-1)^a\equiv1-2a\pmod4\) gives
\[
K_n(B)\equiv|\mathcal T_n|-2\sum_{e\in B}N_e\pmod4.
\]
Rotation invariance gives one common spoke count \(N_s\) and one rim count \(N_r\). Differentiating the weighted wheel determinant with respect to one spoke weight at all weights one, or equivalently taking its principal minor, yields
\[
N_s=\det\operatorname{tridiag}_{n-1}(-1,3,-1)=F_{2n},
\]
where \(F_0=0\), \(F_1=1\), \(F_{j+2}=F_{j+1}+F_j\). Each tree has exactly \(n\) edges, so counting all incidences implies \(N_r+N_s=|\mathcal T_n|\). If \(3\mid n\), the Fibonacci parity period gives \(F_{2n}\equiv0\pmod2\), hence both \(N_s,N_r\) are even. Moreover, with \(A=\begin{pmatrix}1&1\\1&0\end{pmatrix}\), one has \(A^6\equiv I\pmod4\), so \(L_{6k}=\operatorname{tr}(A^{6k})\equiv2\pmod4\) and \(|\mathcal T_n|=L_{6k}-2\equiv0\pmod4\). The preceding congruence proves \(K_n(B)\equiv0\pmod4\) for every frequency.

**5. Invertibility.** On the finite abelian edge cube, convolution by \(\mathbf1_{\mathcal T_n}\) is diagonalized by the Walsh characters, with eigenvalues \(K_n(b)\). Its invertibility is therefore equivalent to simultaneous nonvanishing, already classified in steps 2 and 3.

## Verification
An accompanying standalone Python script independently enumerates labeled spanning trees, performs complete exact integer Walsh transforms in every rim size \(3\le n\le9\), checks the Lucas counts and vanishing criterion, and checks all coefficient congruences. It also verifies selected Fourier coefficients against exact signed Laplacian determinants and explicitly checks all \(4^{n/3}\) constructed nullvectors for \(n=3,6,9,12\). Run `python verify_wheel.py` from the directory containing the script; no external packages are needed. Finite tests do not replace the general proof.

## Relationship to prior work
The weighted spanning-tree determinant is classical, and the ordinary wheel spanning-tree count \(L_{2n}-2\) is due to earlier work; both are used as inputs, not claimed as new. Constantine and Buliga (2004) study determinantal colored-tree enumerators; Benjamin and Yerger (manuscript dated 2004, published 2006) prove the unweighted Lucas count. Those results establish tools and counts, but do not identify the complete all-frequency Walsh zero-free dimensions, construct a period-three family of singular signings, or establish the modulo-four divisibility of every coefficient. The statement concerns the entire signed spanning-tree sum at all \(2^{2n}\) characters, not a one- or two-edge covariance matrix.

## Limitations
The theorem classifies whether any Walsh coefficient vanishes, but does not determine the exact number of zero coefficients when \(3\mid n\), all nonzero coefficient values, or sharp endpoint Fourier-projection norms. The \(4^{n/3}\) lower bound is not asserted to be sharp. Historical priority was assessed against accessible literature and research records, not certified exhaustively. No independent mathematical audit is claimed.

## References
1. G. M. Constantine and M. G. Buliga, *Determinantal generating functions of colored spanning forests*, International Journal of Mathematics and Mathematical Sciences 2004 (2004), 273–283. DOI: 10.1155/S0161171204302206. Public PDF: https://onlinelibrary.wiley.com/doi/pdf/10.1155/S0161171204302206 (first published 2004-02-09).
2. A. T. Benjamin and C. R. Yerger, *Combinatorial Interpretations of Spanning Tree Identities*, manuscript dated 2004-11-14, later Bulletin of the Institute of Combinatorics and Its Applications 47 (2006), 37–42. Author-hosted manuscript: https://math.hmc.edu/benjamin/wp-content/uploads/sites/5/2019/06/Combinatorial-Interpretations-of-Spanning-Tree-Identities.pdf.
3. G. Aalipour, A. M. Duval, W. Kook, K.-J. Lee, and J. L. Martin, *A weighted cellular matrix-tree theorem, with applications to complete colorful and cubical complexes*, arXiv:1510.00033 (first public version 2015-09-30). Background on the wider weighted matrix-tree framework; no wheel-specific Walsh classification is claimed from this source.
