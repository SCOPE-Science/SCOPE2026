# Unimodular hub actuation on unweighted spider trees

## Finding

Let \(S(\ell_1,\ldots,\ell_k)\) be the unweighted spider whose hub is joined to \(k\ge3\) internally disjoint paths of positive integer edge lengths \(\ell_1,\ldots,\ell_k\). Put \(n=1+\sum_i\ell_i\), let \(L\) be its combinatorial Laplacian, and let \(e\) be the unit vector at the hub. The square single-input Kalman matrix

\[
\mathcal K=[e,(-L)e,(-L)^2e,\ldots,(-L)^{n-1}e]
\]

satisfies the exact **zero-or-unit determinant law**

\[
\boxed{\quad |\det\mathcal K|=\begin{cases}1,&\gcd(2\ell_i+1,2\ell_j+1)=1\ \text{for every }i<j,\\0,&\text{otherwise}.\end{cases}\quad}
\]

This includes arbitrarily many genuinely branched trees. In the controllable cases the columns of \(\mathcal K\) form a basis of the integer lattice \(\mathbb Z^n\), not merely a basis over the reals. Thus, for the discrete-time integer system \(x_{t+1}=(I-L)x_t+eu_t\) started at zero, **every integer target state is reachable in exactly \(n\) steps using integer inputs**. If the gcd condition fails, there are real targets not reachable by any length of input sequence.

For example, arms \((1,2,3)\) have odd labels \((3,5,7)\) and \(|\det\mathcal K|=1\); arms \((1,2,4)\) have labels \((3,5,9)\) and determinant zero. The qualitative reachability criterion is consistent with prior starlike spectral methods; the asserted unit-lattice index is the substantive additional conclusion.

## Assumptions and scope

All graph edges have weight one; arm lengths count *edges* from the hub to an arm's leaf. The vertex order begins with the hub and then lists each arm outward. Reordering vertices changes only the determinant's sign. The positive integers \(\ell_i\) can differ arbitrarily, and \(k\ge3\) is fixed or arbitrary. The condition is pairwise coprimality of the **odd integers** \(2\ell_i+1\), not of the arm lengths themselves. The matrix \(-L\) is used for continuous-time linear controllability, while \(I-L\) supplies an integer discrete-time realization; neither discrete-time stochasticity nor stability is assumed.

## Proof

**1. Reducing hub controllability to disjoint grounded arms.** Write \(N=n-1\) and let \(D_\ell\) be the \(\ell\times\ell\) grounded path Laplacian with diagonal \((2,\ldots,2,1)\) and off-diagonal \(-1\); for \(\ell=1\), its only entry is \(1\). Under the prescribed ordering,

\[
-L=\begin{pmatrix}-k&u^{\mathsf T}\\u&B\end{pmatrix},\qquad B=\operatorname{diag}(-D_{\ell_1},\ldots,-D_{\ell_k}),
\]

where \(u\) is the direct sum of the first coordinate unit vectors of each arm. Let \(z_j\) be the lower \(N\) entries of \((-L)^je\). Then \(z_1=u\), and block multiplication gives \(z_{j+1}=Bz_j+u h_j\), where \(h_j\) is the hub entry of \((-L)^je\). Induction shows \(z_j=B^{j-1}u\) plus a linear combination of \(u,Bu,\ldots,B^{j-2}u\). Consequently, the first column of \(\mathcal K\) is \(e\), and triangular column operations of determinant one give

\[
|\det\mathcal K|=|\det[u,Bu,\ldots,B^{N-1}u]|.
\]

**2. Integer resultant factorization.** On a single arm, the matrix \([e_1,(-D_\ell)e_1,\ldots,(-D_\ell)^{\ell-1}e_1]\) is triangular with every diagonal entry one, hence has determinant one. Let \(P_\ell(x)=\det(xI-D_\ell)\), so \(P_0=1\), \(P_1=x-1\), and \(P_\ell=(x-2)P_{\ell-1}-P_{\ell-2}\) for \(\ell\ge2\). The monic polynomial remainder map

\[
\mathbb Z[x]_{<N}\longrightarrow\bigoplus_{i=1}^k\mathbb Z[x]/(P_{\ell_i}),\qquad f\longmapsto(f\bmod P_{\ell_i})_i
\]

has an integer matrix of determinant, up to sign, \(\prod_{i<j}\operatorname{Res}(P_{\ell_i},P_{\ell_j})\). This is the standard Sylvester-resultant determinant identity (for two factors, eliminate the division remainders; iterating gives the stated product). The cyclic arm bases just established transform this remainder map to the block Krylov matrix using only unimodular row transformations. Replacing \(D_\ell\) by \(-D_\ell\) affects only signs. Therefore

\[
\boxed{|\det\mathcal K|=\prod_{i<j}|\operatorname{Res}(P_{\ell_i},P_{\ell_j})|.}
\]

This identity is valid even when the factors share roots, in which case both sides vanish.

**3. Exact pairwise resultants.** The roots of \(P_a\), with \(A=2a+1\), are the simple numbers

\[
\lambda_j=2-2\cos\theta_j,\qquad\theta_j=(2j-1)\pi/A,\quad j=1,\ldots,a.
\]

The same tridiagonal recurrence (or the identity \(P_b(2-z-z^{-1})=(-1)^bz^{-b}(z^{2b+1}+1)/(z+1)\)) gives

\[
P_b(\lambda_j)=(-1)^b\frac{\cos((2b+1)\theta_j/2)}{\cos(\theta_j/2)}.
\]

If \(g=\gcd(A,2b+1)>1\), then \(\theta=\pi/g\) is a common root angle, since \(A/g\) and \((2b+1)/g\) are odd and \(g\ge3\). Thus the resultant vanishes. If \(g=1\), multiplication by the odd integer \(2b+1\) permutes the odd residue classes modulo \(2A\). Up to sign, the classes \(1,3,\ldots,A-2\) represent every pair of odd residues \(\{s,-s\}\) except the single fixed class \(A\), which multiplication by \(2b+1\) preserves. Because \(|\cos(\pi s/(2A))|\) is unchanged by \(s\mapsto-s\) modulo \(2A\), the product of the numerator cosines has the same absolute value as that of the denominator cosines. Hence \(|\operatorname{Res}(P_a,P_b)|=1\) for coprime \(A,2b+1\). Substitution in the product proves the exact determinant law.

**4. Integral finite-step reachability.** If \(A_0=-L\) and \(A_1=I-L=I+A_0\), the power binomial identities show that the two Krylov matrices differ by an upper triangular integer change of basis with diagonal ones; hence their determinants agree up to sign. At time \(n\), the map from \((u_0,\ldots,u_{n-1})\) to \(x_n\) is the column-reversed Krylov matrix of \((A_1,e)\). It maps \(\mathbb Z^n\) bijectively to \(\mathbb Z^n\) precisely when the determinant has absolute value one. When the determinant is zero, the Kalman rank condition prevents full real reachability. This proves both assertions.

**5. Finite-horizon volume corollary.** In the coprime case, \(L\) has distinct eigenvalues \(\lambda_1,\ldots,\lambda_n\). For any \(T>0\) and \(\mu\ge0\), define \(C_{ij}=\int_0^T e^{-(\lambda_i+\lambda_j+2\mu)t}\,dt\), and the controllability Gramian \(W(T,\mu)=\int_0^T e^{-(L+\mu I)t}ee^{\mathsf T}e^{-(L+\mu I)t}\,dt\). Eigenbasis factorization of \(W\) and the Kalman Vandermonde formula yield

\[
\boxed{\det W(T,\mu)=\frac{\det C}{\prod_{i<j}(\lambda_j-\lambda_i)^2}>0.}
\]

The strict inequality follows from linear independence of distinct exponentials on \([0,T]\). This is a direct consequence, not a claim of optimal hub placement among all vertices.

## Verification

Run `python check.py` with Python 3 and SymPy. The checker constructs exact integer Laplacians and exact Krylov determinants for 91 three- and four-arm length profiles, verifies 120 polynomial pair resultants, checks representative discrete-time determinant invariance, and confirms the inverse of a fully controllable integer Krylov matrix is integral. It reports 218 exact assertions. The analytical argument, not this finite enumeration, establishes the result for all arm counts and all positive arm lengths. No external symbolic certificate or independent audit is claimed.

## Relationship to prior work

Parlangeli and Notarstefano (2011) gave Laplacian controllability criteria for paths and cycles using grounded-path spectra, not the higher-degree spider lattice determinant. Parlangeli (2025) provided a complete qualitative spectral/node-selection procedure for starlike Laplacian controllability; its framework covers the hub's real reachability classification and must not be interpreted as leaving that qualitative question open. The present claim concerns the stronger exact integer Kalman determinant and the associated full-integer-target reachability property. The arithmetic use of Chebyshev-type resultant identities is also related to established resultant theory, including Louboutin (2013); no general resultant novelty is claimed.

## Limitations

The theorem covers only equal unit conductances, a single input placed at the hub, and full \(n\)-step integer dynamics. Arbitrary positive edge weights, nonhub inputs, actuator optimization, bounded or positive inputs, and prescribed stable/stochastic discretizations are not classified. A unimodular integer reachability matrix can still be poorly conditioned and can demand very large inputs. The Gramian identity is exact but does not provide a uniform numerical condition-number bound. The stated novelty depends on comparisons with accessible published sources; independent publication-priority checking remains outstanding.

## References

1. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556 (first posted 2011-09-16), https://arxiv.org/html/1109.3556v1 .
2. G. Parlangeli, *Laplacian Controllability and Observability of Multi-Agent Systems: Recent Advances in Tree Graphs*, Algorithms 18 (2025), 239, https://doi.org/10.3390/a18050239 .
3. S. R. Louboutin, *Resultants of Chebyshev Polynomials: A Short Proof*, Canadian Mathematical Bulletin 56 (2013), 602–605, first electronically published 2012-03-05, https://doi.org/10.4153/CMB-2012-002-1 .
