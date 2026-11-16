# Linear Fourier-condition growth for uniform Möbius-ladder spanning-tree sampling

## Finding
Let \(M_n\), for every integer \(n\geq3\), consist of a cycle on \(2n\) vertices together with the \(n\) edges joining antipodal vertices. Sample a spanning tree of \(M_n\) uniformly. The covariance of its \(3n\) edge-occupation indicators has precisely one zero eigenvalue, all other eigenvalues are positive, and its **complete finite Fourier spectrum** is given explicitly below. Its intrinsic squared sampling condition number satisfies
\[
\boxed{\displaystyle\frac{\kappa_n}{n}\longrightarrow\frac{\sqrt3}{2}}.
\]
More precisely, its least positive eigenvalue is \(1/(3n)+O(n^{-2})\), and its largest is \(1/(2\sqrt3)+O(n^{-1})\). The statements concern the covariance (one fourth of the centered \(\pm1\) Walsh-character Gram matrix); uniform rescaling does not change \(\kappa_n\).

## Assumptions and scope
Label vertices by \(\mathbb Z/(2n)\), rim edges by \(r_i=\{i,i+1\}\) for \(i\in\mathbb Z/(2n)\), and antipodal edges by \(s_j=\{j,j+n\}\) for \(j\in\mathbb Z/n\). Write \(X_e\) for the indicator of edge \(e\) in a uniformly selected spanning tree. Define \(C_n=(\operatorname{Cov}(X_e,X_f))_{e,f}\), and \(\kappa_n=\lambda_{\max}(C_n)/\lambda_{\min}^+(C_n)\), with \(\lambda_{\min}^+\) the smallest strictly positive eigenvalue. The graph is simple and connected for \(n\ge3\).

For a completely finite specification let
\[
\alpha=2-\sqrt3,\quad s=\frac1{4\sqrt3},\qquad
O_d=s\frac{\alpha^d-\alpha^{n-d}}{1+\alpha^n}\quad(0\le d<n),
\]
where \(O_{d+n}=-O_d\) and \(O\) is extended periodically with period \(2n\). On the same group let \(H_d=\mathbf1_{d=0}-1/(2n)-2O_d\) and \(T_d=2(O_d-O_{d+1})\). Define
\[
\begin{aligned}
a_k&=H_0-\sum_{d=0}^{2n-1}H_d^2 e^{-2\pi i k d/(2n)},\quad 0\le k<2n,\\
c_l&=4O_0-16\sum_{d=0}^{n-1}O_d^2e^{-2\pi i ld/n},\\
b_l&=-\sqrt2\sum_{d=0}^{n-1}T_d^2e^{-2\pi i ld/n},\quad0\le l<n.
\end{aligned}
\]
All \(a_k\) and \(c_l\) are real. The complete eigenvalue multiset of \(C_n\) consists of the \(n\) scalars \(a_k\) for odd \(k\in\{1,3,\ldots,2n-1\}\), together with, for each \(0\le l<n\), the two eigenvalues
\[
\boxed{\lambda_{l,\pm}=\tfrac12\left(a_{2l}+c_l\pm\sqrt{(a_{2l}-c_l)^2+4|b_l|^2}\right).}
\]
These are \(3n\) eigenvalues counted with multiplicity. The only zero is \(\lambda_{0,-}=0\).

## Proof
**1. Transfer-current covariance and exact kernels.** Let \(B\) be the oriented vertex-edge incidence matrix and \(L=BB^*\). The uniform-spanning-tree transfer-current identity gives, for \(P=B^*L^+B\),
\[
\operatorname{Cov}(X_e,X_f)=P_{ee}\mathbf1_{e=f}-|P_{ef}|^2.
\]
The vertex Laplacian has Fourier eigenvalue \(3-2\cos(\pi k/n)-(-1)^k\) at \(k\in\mathbb Z/(2n)\), the zero mode being excluded from its pseudoinverse. Separate even and odd Fourier indices. On the odd sector, the inverse Green kernel is precisely \(O_d\): it solves the antiperiodic massive recurrence with characteristic roots \(2\pm\sqrt3\), yielding the stated formula. The even sector supplies the cycle derivative kernel \((\mathbf1_{d\equiv0\pmod n}-1/n)/2\). A first difference for rim-to-antipodal currents, and a second difference for rim-to-rim currents, therefore give
\[
P_{r_0,r_d}=H_d,\quad P_{s_0,s_d}=4O_d,\quad
|P_{r_d,s_0}|^2=T_d^2.
\]
The last formula is independent of the orientation chosen for antipodal edges. Hence
\[
\begin{aligned}
(C_n)_{r_i,r_j}&=H_0\mathbf1_{i=j}-H_{i-j}^2,\\
(C_n)_{s_i,s_j}&=4O_0\mathbf1_{i=j}-16O_{i-j}^2,\\
(C_n)_{r_i,s_j}&=-T_{i-j}^2.
\end{aligned}
\]
Because \(T_{d+n}^2=T_d^2\), the rim-to-chord coupling vanishes on odd rim Fourier modes. Normalized even rim modes couple to the matching chord frequencies, with the normalization factor \(\sqrt2\). Thus Fourier transformation gives exactly the scalar modes \(a_k\) and Hermitian blocks \(\begin{psmallmatrix}a_{2l}&b_l\\\overline b_l&c_l\end{psmallmatrix}\). This proves the finite-spectrum formula.

**2. Rank.** Every spanning tree has exactly \(2n-1\) edges, so the all-ones edge vector is in the covariance kernel. Conversely, if a real edge-cost array has constant cost over all spanning trees, its costs agree along any cycle: for two edges in one cycle, extend the remainder of the cycle to a spanning tree and exchange one edge for the other. The four-cycles \(r_i,s_{i+1},r_{i+n},s_i\), with indices modulo \(n\), form a chain through all chord and rim edges, hence all costs are equal. The graph's cycle matroid is connected. Complex costs follow by considering real and imaginary parts. Therefore the covariance kernel is exactly the constant line, and all other eigenvalues are positive.

**3. Limiting symbol.** Put \(A=1/(2\sqrt3)\), \(D(\theta)=1-2\alpha^2\cos\theta+\alpha^4\), and
\[
\begin{aligned}
a(\theta)&=2s-\frac{8s^2(1-\alpha^4)}{D(\theta)},\\
b(\theta)&=-\frac{4\sqrt2s^2(1-\alpha)^2(1-\alpha^2)(1+e^{i\theta})}{D(\theta)}.
\end{aligned}
\]
The infinite-length limiting even-frequency covariance symbol is
\[M(\theta)=\begin{pmatrix}a(\theta)&b(\theta)\\\overline{b(\theta)}&2a(\theta)\end{pmatrix}.\]
Direct simplification using \(\alpha=2-\sqrt3\) gives \(|b(\theta)|^2=(A-a(\theta))(A-2a(\theta))\). Therefore the eigenvalues of \(M(\theta)\) are **exactly** \(A\) and \(L(\theta)=3a(\theta)-A\), not just numerical approximations. On \([0,\pi]\), the function \(a\) increases strictly from \(A/3\) to \(A/2\). In particular \(L\ge0\), with a unique zero at \(\theta=0\) modulo \(2\pi\), and \(L(\theta)=O(\theta^2)\) there.

The geometric formula for \(O_d\) and the finite geometric-series identity yield, **uniformly over all nonzero even frequencies** \(\theta_l=2\pi l/n\),
\[
\begin{pmatrix}a_{2l}&b_l\\\overline b_l&c_l\end{pmatrix}
=M(\theta_l)+\frac1{2n}\begin{pmatrix}1&0\\0&0\end{pmatrix}+O(n\alpha^n)
\]
in operator norm. The exceptional \(l=0\) block has its exact zero eigenvalue and its other eigenvalue tends to \(A\). Odd rim modes have the exact expression
\[
a_k=2O_0+\frac1{2n}\left(1-\frac4{4-2\cos(\pi k/n)}\right)\quad(k\text{ odd}),
\]
and thus converge uniformly to \(A\).

**4. Sharp least eigenvalue.** The spectral gap of \(M(\theta)\) is \(A-L(\theta)\ge A/2\), uniformly. The squared rim-coordinate of a unit eigenvector for its lower eigenvalue is
\[
p(\theta)=\frac{A-a(\theta)}{2A-3a(\theta)}\ge\frac23,
\]
with equality only at \(\theta=0\). Uniform two-dimensional Hermitian perturbation theory applied to the last displayed matrix gives
\[
\lambda_{l,-}=L(\theta_l)+\frac{p(\theta_l)}{2n}+O(n^{-2}+n\alpha^n)
\]
uniformly over \(1\le l<n\). Since \(L\ge0\) and \(p\ge2/3\), all these eigenvalues are at least \(1/(3n)-O(n^{-2})\). Taking \(l=1\) gives the reverse inequality because \(L(2\pi/n)=O(n^{-2})\) and \(p(2\pi/n)=2/3+O(n^{-2})\). All remaining eigenvalues are bounded away from zero for sufficiently large \(n\). Hence \(\lambda_{\min}^+(C_n)=1/(3n)+O(n^{-2})\).

**5. Sharp largest eigenvalue.** The two branches of \(M(\theta)\) are bounded above by \(A\); the perturbation and odd-rim formulas give \(\lambda_{\max}(C_n)\le A+O(n^{-1})\). The nonzero mode in the zero-frequency block, or any fixed nonzero odd rim mode, gives the reverse limit \(A\). Therefore \(\lambda_{\max}(C_n)=A+O(n^{-1})\), and the claimed condition-ratio limit follows.

## Verification
The standalone `check_mobius.py` independently constructs the covariance from the Moore–Penrose Laplacian inverse and compares it with the displayed finite geometric kernels and their Fourier eigenvalues for every \(3\le n\le30\). It also enumerates all spanning trees directly for \(3\le n\le6\) (respectively 81, 392, 1815, 8112 trees), comparing exact uniform moments with the spectral model. Additional larger-order checks compare the finite ratios to the proved asymptotic constant. All tests passed. The proof of the infinite-family limit is the uniform-symbol argument above, not the finite checks.

## Relationship to prior work
Azimi and Farrokhi (first publicly available June 18, 2023) gave incidence/Laplacian pseudoinverses, resistances, and tree counts for Möbius ladders (Theorem 5.1, Corollary 5.4); these ingredients are credited. The classical spanning-tree determinantal/transfer-current theorem supplies the edge covariance identity. Neither source asserts the two-branch **edge-occupation covariance** spectrum or its sharp \(\sqrt3/2\) linear condition coefficient. A publicly indexed wheel-graph spanning-tree covariance result has a different graph and quadratic, rather than linear, growth; its result does not imply the Möbius-ladder coefficient. This is a priority comparison, not a claim that the historical literature has been exhaustively searched.

## Limitations
The Fourier eigenvalues are explicit finite sums, not simplified finite-dimensional extrema for each individual \(n\); only the asymptotic extrema and coefficient are classified. The covariance measures first-order linear observability of edge indicators, not higher-degree Walsh characters or reconstruction of individual trees. The cited pseudoinverse formulas make the finite kernels algorithmically computable, so priority attaches especially to the harmonic block structure and sharp asymptotic, not to the general transfer-current identity. An undiscovered equivalent dimer/tree structure-factor treatment remains possible. Independent audit has not been performed.

## References
- A. Azimi and M. Farrokhi D. G., *Explicit formulas for matrices associated to ladder, circular ladder, and Mobius ladder graphs*, arXiv:2306.10497, v1 June 18, 2023, especially Section 5, Theorem 5.1 and Corollary 5.4, https://arxiv.org/abs/2306.10497.
- A. Kassel and W. Wu, *Transfer current and pattern fields in spanning trees*, Probability Theory and Related Fields 163 (2015), 89–121, https://doi.org/10.1007/s00440-014-0588-2.
- *Uniform Spanning Trees*, DPPy documentation, transfer-current projection-determinantal formulation, https://dppy.readthedocs.io/en/reduce-deps/exotic_dpps/ust.html.
