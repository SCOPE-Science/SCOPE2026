# Quadratic Fourier Gram spectral splitting at rational angles of geometric circle orbits

## Finding

Let \(L\ge2\) and \(1\le a<L\) be coprime integers. Let \(0<p<1\), \(\theta_0=2\pi a/L\), and \(1\le K\le L\). Put \(N=L+K\). Define the infinite, probability-weighted Fourier sampling operator
\[
(A_N(\theta)c)_s=\sqrt{(1-p)p^s}\sum_{j=0}^{N-1}c_j e^{ijs\theta},\qquad s=0,1,\ldots,
\]
from \(\mathbb C^N\) into \(\ell^2(\mathbb N_0)\), and its positive semidefinite Gram matrix \(G_N(\theta)=A_N(\theta)^*A_N(\theta)\). Explicitly,
\[
(G_N(\theta))_{jk}=\frac{1-p}{1-p e^{i(k-j)\theta}},\qquad 0\le j,k<N.
\]
Define \(\zeta=e^{2\pi ia/L}\), the positive residue masses
\[
W_r=\frac{(1-p)p^r}{1-p^L},\quad 0\le r<L,
\]
and the positive definite \(K\)-by-\(K\) moment matrix
\[
(H_K)_{jk}=\sum_{r=0}^{L-1}W_r\zeta^{(k-j)r}=\frac{1-p}{1-p\zeta^{k-j}},\qquad 0\le j,k<K.
\]
Write the eigenvalues of each Hermitian matrix in increasing order and put
\[
C_{L,p}=\frac{L^4p^L}{2(1-p^L)^2}.
\]
**Theorem (all soft branches).** The matrix \(G_N(\theta_0)\) has nullity exactly \(K\). For each \(1\le j\le K\), as real \(\varepsilon\to0\),
\[
\boxed{\lambda_j\bigl(G_N(\theta_0+\varepsilon)\bigr)
=C_{L,p}\lambda_j(H_K)\varepsilon^2+O_{L,K,a,p}(|\varepsilon|^3).}
\]
Thus all \(K\) zero eigenvalues open *quadratically*, with individually sharp, positive, explicitly computable constants. At \(K=2\), the two constants are \(C_{L,p}(1\pm (1-p)/|1-p\zeta|)\).

**Theorem (full doubled band).** At \(K=L\), the \(L\) nonzero eigenvalues at \(\theta_0\) are precisely \(2LW_r\), and the \(L\) soft quadratic coefficients are precisely \(C_{L,p}LW_r\), as multisets indexed by \(0\le r<L\). Their corresponding coefficient ratios are all \(C_{L,p}/2\). Consequently, the condition number of the infinite-row sampling operator obeys the sharp law
\[
\boxed{\operatorname{cond}_2 A_{2L}(\theta_0+\varepsilon)
\sim\frac{2(1-p^L)}{L^2p^{L-1/2}}\frac1{|\varepsilon|}.}
\]
This is a complete leading spectral description for the first \(L\) extra Fourier modes beyond a rational orbit's support, not merely a determinant or a bound on the least eigenvalue.

## Assumptions and scope

All limits are for fixed \(L,K,a,p\) as above, with the angular perturbation \(\varepsilon\in\mathbb R\). Eigenvalues include multiplicity. The coefficient norm is ordinary Euclidean \(\ell^2\), while observations carry the probability weights \((1-p)p^s\). The angular variable is in radians. No uniform claim is made when \(L\) grows, \(p\) tends to \(0\) or \(1\), or \(K>L\). In a sufficiently small punctured neighborhood of \(\theta_0\), the sampling operator is injective: rational angles with support size less than \(N\) form a finite set, and no such angle other than \(\theta_0\) occurs sufficiently near it.

## Proof

**1. The resonant kernel.** Put \(\omega_s=(1-p)p^s\). The operator \(A_N(\theta)\) is analytic from a real neighborhood of \(\theta_0\) into bounded operators \(\mathbb C^N\to\ell^2\): every fixed derivative is bounded by a polynomial in \(s\) times \(\sqrt{\omega_s}\), hence summable. At \(\theta_0\), after factoring out the positive row weights \(\sqrt{\omega_s}\), the evaluations depend on \(s\) only through \(r=s\bmod L\). Thus the range consists exactly of sequences \(\sqrt{\omega_s}F(s\bmod L)\): degree-less-than-\(L\) polynomials interpolate arbitrary values \(F(r)\) at the \(L\) roots \(\zeta^r\). Therefore its rank is \(L\). Its coefficient-space kernel is
\[
E=\{(z^L-1)R(z):\deg R<K\},\qquad\dim E=K.
\]
When \(R(z)=\sum_{j=0}^{K-1}b_jz^j\), the two coefficient blocks of \((z^L-1)R\) have disjoint support because \(K\le L\), and
\[
\|(z^L-1)R\|_{\ell^2(\mathrm{coeff})}^2=2\sum_{j=0}^{K-1}|b_j|^2.
\]

**2. A finite-dimensional singular-cluster perturbation lemma.** Suppose \(B(\varepsilon)=B_0+\varepsilon B_1+O(\varepsilon^2)\) analytically maps a finite-dimensional Hilbert space into any Hilbert space. Let \(E=\ker B_0\), let \(Y=\operatorname{ran}B_0\), and let \(P_Y\) be the orthogonal projection onto \(Y\). Then the eigenvalues of \(B(\varepsilon)^*B(\varepsilon)\) converging to zero have quadratic leading coefficients equal, with multiplicity, to the eigenvalues on \(E\) of
\[
T=\bigl((I-P_Y)B_1|_E\bigr)^*\bigl((I-P_Y)B_1|_E\bigr).
\]
Indeed decompose the domain as \(E\oplus E^\perp\). The latter's \(B_0\)-Gram block is invertible, the off-diagonal Gram blocks are order \(\varepsilon\), and the \(E\)-block is \(\varepsilon^2 (B_1|_E)^*(B_1|_E)+O(\varepsilon^3)\). Taking the Schur complement of the invertible block gives \(\varepsilon^2 T+O(\varepsilon^3)\). For eigenvalue parameter \(\lambda=O(\varepsilon^2)\), replacing that block by its \(\lambda\)-shift changes the Schur complement only in order \(O(|\varepsilon|^3)\), so the ordered small eigenvalues equal \(\varepsilon^2\lambda_j(T)+O(|\varepsilon|^3)\). This also covers repeated leading eigenvalues by the Hermitian eigenvalue perturbation bound. The lemma does not assert that every leading coefficient is nonzero; that is checked below.

**3. Conditional variance determines the entire soft spectrum.** For \(P(z)=(z^L-1)R(z)\in E\), differentiate the sampled values at \(\theta_0\):
\[
\frac{d}{d\theta}P(e^{is\theta})\big|_{\theta_0}
=is\zeta^sP'(\zeta^s)=iLsR(\zeta^r),\qquad r=s\bmod L.
\]
After identifying the row-weighted output \(\ell^2\) with \(L^2(\{\omega_s\})\) by dividing each sequence entry by \(\sqrt{\omega_s}\), the range projection \(P_Y\) is conditional expectation with respect to \(r\). The conditional distribution of \(s\) given \(r\) is \(s=r+Lt\), where \(t\ge0\) has geometric distribution \((1-p^L)(p^L)^t\), independent of \(r\). Hence
\[
\operatorname{Var}(s\mid r)=\frac{L^2p^L}{(1-p^L)^2},\qquad
\| (I-P_Y)A_N'(\theta_0)P\|^2
=\frac{L^4p^L}{(1-p^L)^2}\sum_{r=0}^{L-1}W_r|R(\zeta^r)|^2.
\]
Divide by the coefficient-space factor \(2\) from Step 1. The resulting quadratic form on \(b\in\mathbb C^K\) is exactly \(C_{L,p}\,b^*H_Kb\). Since \(K\le L\), a polynomial of degree less than \(K\) vanishing at all \(L\) distinct roots must be zero. Thus \(H_K\) is positive definite. Apply Step 2 to prove all quadratic spectral expansions and their positive constants.

**4. Complete doubled-band spectrum.** For \(K=L\), the \(L\)-point Fourier matrix \((\zeta^{rj})_{0\le r,j<L}\) is unitary up to factor \(\sqrt L\). Consequently the eigenvalues of \(H_L\) are \(LW_r\). At \(\theta_0\), the two consecutive length-\(L\) monomial blocks coincide at every root; in that decomposition the Gram matrix is
\[
G_{2L}(\theta_0)=\begin{pmatrix}H_L&H_L\\H_L&H_L\end{pmatrix}.
\]
Its hard eigenvalues are \(2LW_r\). The leading soft eigenvalues follow from Step 3. Because \(W_0\) is the largest and \(W_{L-1}\) the smallest residue weight, the top hard eigenvalue is \(2LW_0\) and the least soft eigenvalue is \(C_{L,p}LW_{L-1}\varepsilon^2+O(|\varepsilon|^3)\). Taking the square root of their quotient yields the displayed condition-number constant. This also gives the claimed coefficient-ratio equality for the matched spectral multisets.

## Verification

The standalone `VERIFY.py` checks exact rational identities for the two-residue weights and modal constants. It independently forms the full Hermitian moment Gram matrices directly from \((1-p)/(1-p e^{i(k-j)\theta})\), compares every soft eigenvalue against the predicted matrix spectrum for coprime angles, tests exact resonant rank and hard eigenvalues, and checks the sharp condition-number coefficient. Tested dimensions are \(2\le L\le5\) and every allowed \(1\le K\le L\), with several geometric weights and small positive and negative angular perturbations. Run `python VERIFY.py` with Python 3 and NumPy; the recorded replay yields `PASS: 768 assertions`. These are finite stress tests; the proof for all parameters is the four-step argument above.

## Relationship to prior work

Zhedanov's 2020 wrapped-geometric OPUC construction gives the moment formula, explicit orthogonal polynomials, their norms, and the periodic support at root-of-unity angles (arXiv:2010.10321, Sections 2–3). His norm identity already implies a special determinant/product collapse, but it does not state the entire family of soft eigenvalue coefficients, their \(K\)-dependent moment-matrix spectrum, or the doubled-band pairing and sharp sampling condition number. In particular, a determinant alone cannot identify individual soft eigenvalues for \(K>1\).

Batenkov, Diederichs, Goldman, and Yomdin study singular-value *orders and bounds* for finite clustered-node Vandermonde matrices (arXiv:1909.01927, Theorems 2.2–2.3). Kunis and Nagel likewise give bounds for finite Fourier Vandermonde matrices with near-colliding nodes (DOI:10.1007/s11075-020-00974-x). Those hypotheses concern finite varying node configurations, not the infinitely supported geometric-orbit observation measure here; neither examined theorem supplies this exact all-branch weighted moment-matrix limit. The general singular-cluster Schur complement used here is elementary perturbation theory, not itself claimed as new.

## Limitations

The result is a finite-band, fixed-weight, local angular asymptotic. It does not give a uniform estimate for varying bandlimit or geometric parameter, and does not address the hierarchy beyond \(K=L\), where further orders of vanishing may appear. A complete literature-priority determination, especially against unindexed OPUC perturbation results, remains open. No claim of independently audited correctness is made.

## References

1. A. Zhedanov, *An Explicit Example of Polynomials Orthogonal on the Unit Circle with a Dense Point Spectrum Generated by a Geometric Distribution*, SIGMA **16** (2020), 140, arXiv:2010.10321 (first submitted 20 October 2020); https://sigma-journal.com/2020/140/ and https://arxiv.org/abs/2010.10321.
2. D. Batenkov, B. Diederichs, G. Goldman and Y. Yomdin, *The Spectral Properties of Vandermonde Matrices with Clustered Nodes*, Linear Algebra and Its Applications **609** (2021), 37–72, arXiv:1909.01927 (first submitted 4 September 2019); https://arxiv.org/abs/1909.01927.
3. S. Kunis and D. Nagel, *On the Condition Number of Vandermonde Matrices with Pairs of Nearly-Colliding Nodes*, Numerical Algorithms **87** (2021), 473–496 (online 21 July 2020); https://doi.org/10.1007/s11075-020-00974-x.
