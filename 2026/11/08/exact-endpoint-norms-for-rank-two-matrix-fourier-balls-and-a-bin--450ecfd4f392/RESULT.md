# Exact endpoint norms for rank-two matrix Fourier balls and a binary-square sign transition

## Finding
Let \(q\ge2\) be a prime power and \(3\le m\le n\). Write \(G=M_{m,n}(\mathbb F_q)\) for the additive matrix group, \(D=\{A\in G:\operatorname{rank}A\le2\}\), and \(P_D\) for the Fourier multiplier \(\mathbf1_D\) after the canonical identification of \(G\) with its character group. Thus \(P_Df=K_D*f\), with normalized kernel \(K_D(X)=q^{-mn}\sum_{A\in D}\psi(\sum_{ij}A_{ij}X_{ij})\).

For integers \(t,r\), let \({t\brack r}_q=\prod_{i=0}^{r-1}(q^{t-i}-1)/(q^{r-i}-1)\) be the Gaussian coefficient, and set it to zero when \(r>t\) or \(r<0\). Define
\[
F_k=q^{2n}{k\brack2}_q-q^{n+1}{m-2\brack1}_q{k\brack1}_q+q^3{m-1\brack2}_q\quad(0\le k\le m),
\]
and \(N_{m,n}(s)=\prod_{i=0}^{s-1}(q^m-q^i)(q^n-q^i)/(q^s-q^i)\), with the empty product equal to one. Then the **exact sharp endpoint norm** is
\[
\boxed{\|P_D\|_{\ell^1\to\ell^1}=\|P_D\|_{\ell^\infty\to\ell^\infty}=1+\frac{2}{q^{mn}}\bigg[-F_1N_{m,n}(m-1)+\mathbf1_{\{q=2,\,n=m\ge5\}}(-F_2)N_{m,n}(m-2)\bigg].}
\]
In particular, the Fourier transform \(\widehat{\mathbf1_D}(X)\) is **strictly negative** exactly when \(\operatorname{rank}X=m-1\), together with the additional shell \(\operatorname{rank}X=m-2\) precisely for \(q=2\), \(n=m\ge5\). All other coefficients are positive, and none vanishes.

## Assumptions and scope
The result holds for every finite field, including nonprime fields, every \(m\ge3\), and every \(n\ge m\). Fourier coefficients are *unnormalized*: \(\widehat h(X)=\sum_{A\in G}h(A)\overline{\chi_X(A)}\), where \(\chi_X(A)=\psi(\sum_{ij}X_{ij}A_{ij})\) and \(\psi\) is any fixed nontrivial additive character. The kernel is normalized by \(|G|=q^{mn}\). The rank convention for \(X\) is the ordinary rank over \(\mathbb F_q\). The two endpoint operator norms use counting-measure \(\ell^p\); their values are unchanged by a constant renormalization of that measure.

## Proof
**Step 1: subspace-incidence decomposition.** For \(U\le\mathbb F_q^m\), let \(L_U=\{A\in M_{m,n}(\mathbb F_q):\operatorname{im}A\subseteq U\}\). Put \(R={m-2\brack1}_q\) and \(T={m-1\brack2}_q\). One has the pointwise identity
\[
\mathbf1_D(A)=\sum_{\dim U=2}\mathbf1_{L_U}(A)-qR\sum_{\dim U=1}\mathbf1_{L_U}(A)+q^3T\mathbf1_{\{0\}}(A).
\]
Indeed the right-hand side is one on matrices of rank two, because their column space is the unique two-dimensional \(U\) containing it; for rank one, the coefficient is \({m-1\brack1}_q-qR=1\), since \({m-1\brack1}_q=1+qR\); for rank zero it equals \({m\brack2}_q-qR{m\brack1}_q+q^3T=1\) by the Gaussian-binomial identities. For rank at least three it vanishes.

**Step 2: Fourier transform without character tables.** Since \(L_U\) has \(q^{n\dim U}\) elements, orthogonality of additive characters gives
\[
\sum_{A\in L_U}\overline{\chi_X(A)}=q^{n\dim U}\mathbf1_{\{U\subseteq\ker X^{\mathsf T}\}}.
\]
The kernel of the linear map \(X^{\mathsf T}:\mathbb F_q^m\to\mathbb F_q^n\) has dimension \(k=m-\operatorname{rank}X\). Counting its \(j\)-subspaces gives \(\widehat{\mathbf1_D}(X)=F_k\). This also shows the transform is real, independent of the additive character chosen, and constant on rank orbits.

**Step 3: exact sign classification.** For \(k=0\), \(F_0=q^3T>0\). For \(k=1\), use \(T=R{m-1\brack1}_q/(q+1)\) to write
\[
F_1=R\big(q^3{m-1\brack1}_q/(q+1)-q^{n+1}\big)<0,
\]
because \({m-1\brack1}_q<(q+1)q^{m-2}\) for every \(q\ge2\), and \(n\ge m\).

For \(k\ge3\), the ratio identity \({k\brack2}_q/{k\brack1}_q={k-1\brack1}_q/(q+1)\) shows that the first two terms of \(F_k\) have positive sum: \(q^{n-1}{k-1\brack1}_q/((q+1)R)\ge q^{n-1}/R>1\). The remaining term is positive, so \(F_k>0\).

For \(k=2\),
\[
F_2=q^{2n}-q^{n+1}(q+1)R+q^3T.
\]
The ratio of the magnitude of the middle term to the first is smaller than \((q+1)/(q^{n-m+1}(q-1))\). This is at most \(2/3\) for \(q\ge3\), \(n\ge m\), and at most \(3/4\) for \(q=2\), \(n\ge m+1\). Hence \(F_2>0\) in these ranges. In the remaining binary-square case, put \(z=2^{m-2}\); the exact simplification is
\[
F_2=\frac83(-z^2+6z+1).
\]
For the permissible powers \(z=2,4,8,\dots\), this is positive at \(m=3,4\) and negative exactly when \(m\ge5\). Thus no Fourier coefficient vanishes, and the claimed negative rank shells are exhaustive.

**Step 4: endpoint norm from negative mass.** Fourier inversion gives \(\sum_{X\in G}\widehat{\mathbf1_D}(X)=q^{mn}\) because \(0\in D\). The number of rank-\(s\) matrices is the standard exact count \(N_{m,n}(s)\) obtained by counting factorizations of rank \(s\) modulo \(\operatorname{GL}_s(\mathbb F_q)\). Hence
\[
q^{-mn}\sum_X|\widehat{\mathbf1_D}(X)|=1+2q^{-mn}\sum_{\widehat{\mathbf1_D}(X)<0}(-\widehat{\mathbf1_D}(X)),
\]
which, after inserting the classified negative shells, yields the boxed formula. Convolution on a finite group has sharp \(\ell^1\) norm equal to the kernel \(\ell^1\) norm (test a delta mass), and sharp \(\ell^\infty\) norm equal to the same number (test the pointwise conjugate kernel phase at one output). This completes the proof.

## Verification
The standalone file `verify.py` checks the Gaussian and matrix-rank orbit formulas over an exact integer grid with \(q=2,3,4,5,7,8,9\), \(3\le m\le17\), and \(n\in\{m,m+1,m+3\}\). For the prime fields \(q=2,3\), it independently constructs complete finite Fourier transforms over the \(3\times3\) spaces and the binary \(4\times4\) space; it verifies every Fourier coefficient and the sharp norm, not just a few samples. An independent direct rank-at-most-two enumeration over binary \(5\times5\) and \(5\times6\) matrices verifies the exceptional sign change without enumerating their ambient matrix spaces. The checker requires Python 3 and NumPy for full transforms; all other checks use the standard library. Run `python verify.py`. The expected final marker is `ALL_RANK_TWO_BALL_CHECKS_PASS`.

## Relationship to prior work
Delsarte [1] established the bilinear-forms association scheme and generalized Krawtchouk character table; the present rank-ball transform can also be obtained by summing its first three radial eigenvalues. Gavrilyuk and Koolen [2] study combinatorial characterization of the binary square bilinear-forms graphs, not endpoint Fourier-projection norms. Cioabă and Gupta [3] prove sign and magnitude results for **single-distance** (exact rank) graphs, with a distinct graph eigenvalue extremization; their Theorem 4.7 does not evaluate the Fourier-algebra norm of the rank-at-most-two ball or identify its two-negative-shell binary-square exception. The present contribution is the complete closed endpoint norm, direct incidence proof, and exact rank-shell transition, not the underlying association-scheme eigenmatrix.

## Limitations
This theorem addresses radius two only, with matrix height at least three. It does not claim all-radius analogues, classify nonendpoint \(\ell^p\) norms, or establish an independent priority certificate. The older general character-table theorem provides a way to derive all finite coefficients; the novelty assessment concerns the sharp absolute-mass summation and uniform sign transition. The 1978 source was inspected in authorized full text, but other obscure historical work could have anticipated this specialization. Independent mathematical validation has not been performed.

## References
[1] Ph. Delsarte, “Bilinear forms over a finite field, with applications to coding theory,” *Journal of Combinatorial Theory, Series A* **25** (1978), 226–241; DOI `10.1016/0097-3165(78)90015-8`, especially Section 3 and Appendix Theorem A2.

[2] A. L. Gavrilyuk and J. H. Koolen, “A characterization of the graphs of bilinear \((d\times d)\)-forms over \(\mathbb F_2\),” arXiv:1511.09435, first posted 2015-11-30 UTC; introductory discussion and main Theorem 1.3.

[3] S. M. Cioabă and H. Gupta, “On the eigenvalues of Grassmann graphs, Bilinear forms graphs and Hermitian forms graphs,” arXiv:2102.10155, first posted 2021-02-19 UTC; Section 1.2, Theorem 4.7.
