# Exact Poisson-binomial conditioning for heterogeneous Fourier sampling on coordinate hyperplanes

## Finding

Let \(n\ge2\) and let \(A_1,\ldots,A_n\) be arbitrary finite abelian groups of orders \(q_j\ge2\), which need not coincide. Fix one marked symbol \(a_j\in A_j\) per coordinate. Give \(X=\prod_{j=1}^n A_j\) uniform probability measure, and let \(\mathcal H_{\le r}\) be the span of product Fourier characters nontrivial in at most \(r\) coordinates, where \(1\le r<n\). Sample on the **union of coordinate hyperplanes**
\[
S=\{x\in X:\text{at least one }x_j=a_j\}.
\]
For \(R:\mathcal H_{\le r}\to L^2(X)\) defined by \(Rf=\mathbf1_S f\), write \(D=\dim\mathcal H_{\le r}=\sum_{|U|\le r}\prod_{j\in U}(q_j-1)\). Let \(Z_j\) be independent Bernoulli variables with \(\Pr(Z_j=1)=1/q_j\), and, for \(T\subseteq[n]\), define
\[
\beta_T=\Pr\left(\sum_{j\notin T} Z_j\le r-|T|\right),\qquad m_T=\prod_{j\in T}(q_j-2).
\]
The **complete squared-singular-value spectrum** of \(R\), including multiplicities, is
\[
\boxed{1-\beta_T\quad(m_T\text{ times}),\quad |T|\le r;\qquad
1\quad\left(D-\sum_{|T|\le r}m_T\text{ times}\right).}
\]
Zero-multiplicity terms are omitted and coincident values are merged. In particular, every sampled Fourier band is injective, the largest singular value is exactly \(1\), and the least singular value is **simple**, with
\[
\boxed{\sigma_{\min}(R)^2=\Pr\left(\sum_{j=1}^nZ_j\ge r+1\right),\qquad
\kappa_2(R)=\Pr\left(\sum_{j=1}^nZ_j\ge r+1\right)^{-1/2}.}
\]
The unique least-stable coefficient direction, up to scalar, is the Fourier polynomial
\[
\boxed{f_*(x)=\sum_{\substack{U\subseteq[n]\\|U|\le r}}\ \prod_{j\in U}\frac{1-q_j\mathbf1_{\{x_j=a_j\}}}{q_j-1}.}
\]
The same spectrum applies to the normalized sampled Fourier matrix whose entry at sampled point \(x\) and band character \(\chi\) is \(\chi(x)/\sqrt{|X|}\). In general the value \(1\) appears with positive multiplicity when \(r\ge1\).

## Assumptions and scope

All groups are finite and abelian; no cyclicity, equal alphabet size, field structure, or special choice of marked symbols is assumed. The Fourier characters are orthonormal under uniform probability measure on \(X\). On the range the inherited ambient norm is used: there is **no renormalization by \(|S|\)**. Every \(q_j\ge2\) and \(1\le r<n\); these hypotheses ensure the Poisson-binomial upper tail in the denominator is strictly positive. Empty products equal one. The condition number is the spectral \(\ell^2\) condition number of the injective restriction operator.

## Proof

**Coordinate decomposition.** On coordinate \(A_j\), let \(\epsilon_j=1/q_j\), \(e_j=\mathbf1_{\{a_j\}}\), and
\[
u_j=(q_j e_j-1)/\sqrt{q_j-1}.
\]
Then \(1,u_j\) are orthonormal; the orthocomplement \(W_j\) of their span consists precisely of the \((q_j-2)\)-dimensional functions that vanish at \(a_j\) and sum to zero over \(A_j\). The one-coordinate nonconstant Fourier-character space is \(\mathbb C u_j\oplus W_j\). Both \(u_j\) and every vector in \(W_j\) have Fourier interaction degree one.

**Tensor-product mask.** The unobserved set is the rectangular puncture \(B=X\setminus S=\prod_j(A_j\setminus\{a_j\})\). Multiplication by its indicator is the tensor product of the coordinate projections \(M_j=M_{\mathbf1_{A_j\setminus\{a_j\}}}\). The operator \(M_j\) acts as identity on \(W_j\), and its restriction to \(\operatorname{span}\{1,u_j\}\) is the orthogonal rank-one projection \(|g_j\rangle\langle g_j|\), where
\[
g_j=\sqrt{1-\epsilon_j}\,1-\sqrt{\epsilon_j}\,u_j.
\]
Indeed \(g_j\) is the normalized function that is zero at \(a_j\) and constant on the remaining \(q_j-1\) points.

**Entire block spectrum.** The interaction-degree projector commutes with the mutually orthogonal decomposition by the set \(T\) of coordinates in \(W_j\). Fix such a set with \(|T|=s\le r\), and fix one of the \(m_T\) tensor-product contrast vectors on its coordinates. On all other coordinates, the band consists of squarefree products of the modes \(u_j\) on subsets of size at most \(r-s\). Its puncture compression is the rank-one operator formed from the orthogonal projection of \(\bigotimes_{j\notin T}g_j\) to that band. The squared norm of this projection is
\[
\sum_{\substack{U\subseteq[n]\setminus T\\|U|\le r-s}}
\prod_{j\in U}\epsilon_j\prod_{j\notin U\cup T}(1-\epsilon_j)
=\beta_T.
\]
Consequently the puncture compression has one eigenvalue \(\beta_T\) for each of the \(m_T\) contrast vectors and all its other eigenvalues zero. On the complete degree-\(r\) Fourier band it has precisely those nonzero levels; the sampled compression \(R^*R=I-P_{\le r}M_{\mathbf1_B}P_{\le r}\) has the displayed spectrum.

**Strict extreme level.** For any nonempty \(T\) with \(|T|\le r\), the event \(\{\sum_{j\notin T}Z_j\le r-|T|\}\) is contained in \(\{\sum_{j=1}^nZ_j\le r\}\). The containment is strict with positive probability: choose exactly \(r-|T|+1\) successes outside \(T\) and zero successes inside \(T\). There are enough outside coordinates since \(r<n\). Thus \(\beta_T<\beta_\varnothing\). As \(m_\varnothing=1\), the smallest eigenvalue \(1-\beta_\varnothing\) has multiplicity one and equals the Poisson-binomial tail stated above. The upper tail is positive since every \(\epsilon_j>0\) and \(r<n\). Finally \(D-\sum_Tm_T\ge\sum_j[(q_j-1)-(q_j-2)]=n>0\), so the largest eigenvalue is \(1\).

**Extremizer and asymptotic limits.** The top puncture eigenmode is the degree-\(r\) projection of \(\prod_jg_j\), equivalently of \(\mathbf1_B\). Because
\[
\mathbf1_{A_j\setminus\{a_j\}}=(1-\epsilon_j)\left[1+\frac{1-q_j\mathbf1_{\{a_j\}}}{q_j-1}\right],
\]
its truncation is the explicit \(f_*\). If \(\lambda_n=\sum_j\epsilon_j\) along a triangular sequence, then (a) when \(\max_j\epsilon_j\to0\) and \(\lambda_n\to\lambda\in(0,\infty)\), the exact condition number tends to \(\left[1-e^{-\lambda}\sum_{k=0}^r\lambda^k/k!\right]^{-1/2}\) for fixed \(r\); (b) when \(\lambda_n\to0\), the tail is asymptotic to the elementary symmetric sum \(e_{r+1}(\epsilon_1,\ldots,\epsilon_n)\), provided \(n\ge r+1\), because \((1-\lambda_n)e_{r+1}\le\Pr(\sum Z_j\ge r+1)\le e_{r+1}\); (c) when \(\lambda_n\to\infty\), Chebyshev's inequality and \(\operatorname{Var}(\sum Z_j)\le\lambda_n\) show the condition number tends to \(1\). These are additional consequences of the exact identity, with no assumption of equal alphabets.

## Verification

The independent implementation `artifacts/verify.py` constructs actual complex Fourier character matrices for twelve cyclic test products with unequal factor orders and various nonzero marked symbols, independently forms the sampled Gram operators, and compares all squared singular values (with multiplicity) and sharp condition numbers to the Poisson-binomial formulas. The maximum numerical spectral discrepancy is below \(4\times10^{-15}\); the checker prints `HETEROGENEOUS_PUNCTURE_SPECTRUM_PASS cases=12`. Execute `python artifacts/verify.py` from the package root with Python 3 and NumPy. The all-dimensional proof is the block calculation above; finite numerical experiments are corroboration, not an infinite certificate.

For example, for factor sizes \((2,3,4,5)\) and \(r=2\), the tail probability is exactly \(11/120\). The restriction has \(46\) Fourier columns, \(96\) sampled points, and sharp condition number \(\sqrt{120/11}\).

## Relationship to prior work

Filmus [1] establishes a harmonic framework for homogeneous binary Hamming slices. Vasil'eva [2] studies reconstruction of individual eigenspaces from homogeneous \(q\)-ary Hamming spheres. Related published formulas for the complete mixed Fourier-band spectrum on a **single homogeneous Hamming sphere** [3], and first-band sampling on a homogeneous sphere [4], do not state the tensor-product spectral law for a **union of coordinate hyperplanes with unequal alphabet sizes**. Previous homogeneous first-band Hamming-ball work treats a different domain, while classical tensor-product Fourier theory supplies the individual coordinate decomposition used in our proof. The claim of contribution is limited to the complete heterogeneous band spectrum, sharp Poisson-binomial conditioning and explicit unique least-stable direction; the elementary rank-one tensor identity is not itself claimed to be new.

## Limitations

The observation set must be the union of the specified coordinate hyperplanes, and only the interaction-degree-band Fourier subspace is analyzed. Arbitrary coordinate-dependent missing-point masks that are not rectangular in the complement and nonlinear feature spaces are not covered. The normalizations are essential; sampling-row renormalization scales all singular values but does not alter the condition number. Exact spectral information does not address noisy statistical estimation beyond linear worst-case stability. A sufficiently general unpublished or historical tensor-compression theorem could imply the specialization; priority review is bounded and independent mathematical validation has not been performed.

## References

[1] Y. Filmus, *An orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142 (first public version 2014-06-01), https://arxiv.org/abs/1406.0142.

[2] A. Vasil'eva, *Reconstruction of Eigenfunctions of q-ary n-dimensional Hypercube*, arXiv:1412.3622 (first public version 2014-12-11), https://arxiv.org/abs/1412.3622.

[3] *An all-degree spectral law for Fourier sampling on q-ary Hamming spheres*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-all-degree-spectral-law-for-fourier-sampling-on-q-ary-hamming--f3d01cadaa90.

[4] *Exact q-ary Hamming-shell Fourier concentration and the arithmetic tightness criterion*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-q-ary-hamming-shell-fourier-concentration-and-the-arithmet--89a15e26e594.
