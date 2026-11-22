# Sharp dimension-optimal boundary jets for planar harmonic Fourier bands

## Finding

Fix integers \(L\ge0\), \(k\ge0\), and \(M\ge1\). Let \(\mathcal H_{\le L}\) be the complex vector space of planar harmonic polynomials of total degree at most \(L\), of dimension \(2L+1\). At the \(M\) equally spaced points on any circle of positive radius, observe the *complete harmonic jet of order \(k\)*: function value and all partial derivatives of total order at most \(k\). There are exactly \(2k+1\) independent complex data channels at each point.

**Sharp node theorem.** These observations determine every member of \(\mathcal H_{\le L}\) uniquely if and only if
\[
M\ge \left\lceil\frac{2L+1}{2k+1}\right\rceil.
\]
No configuration of fewer points, whether or not on a circle, can determine every such harmonic polynomial using jets of order at most \(k\). Thus equally spaced boundary points attain the universal information-theoretic minimum for every bandwidth and every jet order.

**Complete undersampling rank theorem.** For each residue \(r\in\{0,\ldots,M-1\}\), set
\[
p_r=\#\{n\in\{1,\ldots,L\}:n\equiv r\pmod M\},\quad
q_r=\#\{n\in\{1,\ldots,L\}:-n\equiv r\pmod M\},
\]
and \(c_r=1\) for \(r=0\), otherwise \(c_r=0\). Define \(\epsilon_r=1\) if \(c_r=1\), or \(p_r>k\), or \(q_r>k\); otherwise \(\epsilon_r=0\). Then the **exact complex rank** of the boundary-jet sampling operator is
\[
\boxed{\operatorname{rank}J_{L,k,M}=\sum_{r=0}^{M-1}\left[\min(p_r,k)+\min(q_r,k)+\epsilon_r\right].}
\]
Consequently its nullity is precisely \(2L+1-\operatorname{rank}J_{L,k,M}\), at every undersampling rate as well as above the uniqueness threshold. A residue-class discrete Fourier transform and small one-sided confluent Vandermonde solves give a constructive reconstruction algorithm.

**Comparison at the same differential order.** Sampling only the boundary trace and its tangential derivatives through order \(k\) at an equally spaced grid requires and suffices with \(\lceil(2L+1)/(k+1)\rceil\) nodes, whereas access to the complete harmonic \(k\)-jet lowers the exact optimum to \(\lceil(2L+1)/(2k+1)\rceil\). In particular first-jet value-and-gradient samples require \(\lceil(2L+1)/3\rceil\) points, versus \(L+1\) for value plus first tangential derivative at equispaced points.

## Assumptions and scope

A planar harmonic polynomial means a complex-valued polynomial in Cartesian real coordinates satisfying \(\Delta f=0\). With \(z=x+iy\), every such polynomial of degree at most \(L\) is uniquely
\[
f(z)=a_0+\sum_{n=1}^{L}\left(a_nz^n+b_n\overline z^{\,n}\right).
\]
The sampling points are \(z_t=R\exp(i(\phi+2\pi t/M))\), with arbitrary \(R>0\), \(\phi\in\mathbb R\), and \(0\le t<M\). Complete order-\(k\) jets may equivalently be specified by
\[
f(z_t),\quad\partial_z^{\,j}f(z_t),\quad\partial_{\overline z}^{\,j}f(z_t),\qquad1\le j\le k,
\]
because every mixed complex partial derivative containing both \(\partial_z\) and \(\partial_{\overline z}\) is zero for harmonic functions; the transformations between these and Cartesian derivatives are invertible within the harmonic-jet space. Derivatives are exact and noiseless. The theorem is an injectivity/rank statement, not a claim of uniform numerical conditioning or stability under noise. Real-valued harmonic polynomials obey the same node threshold by complexification.

## Proof

**1. Fourier reduction.** Scaling \(R\) and rotating \(\phi\) change coefficients and jet rows by invertible diagonal transformations, so rank is independent of both. Work on the unit circle without rotation. Write \(f(\rho e^{i\theta})=\sum_{n=-L}^{L}c_n\rho^{|n|}e^{in\theta}\). At each point \(z_t=e^{2\pi it/M}\), multiply the \(j\)-th holomorphic jet by \(z_t^j\), and its antiholomorphic counterpart by \(\overline z_t^{\,j}\). The resulting channels are
\[
\sum_{n=-L}^{L}c_n z_t^n,\qquad
\sum_{n=1}^{L}(n)_{\underline j}c_n z_t^n,\qquad
\sum_{n=-L}^{-1}(-n)_{\underline j}c_n z_t^n,
\]
where \((u)_{\underline j}=u(u-1)\cdots(u-j+1)\), with \((u)_{\underline0}=1\) and \((u)_{\underline j}=0\) for integer \(0\le u<j\). Applying the \(M\)-point DFT splits all measurements into independent residue classes \(n\pmod M\), with one block for each \(r\).

**2. Exact block rank.** For one residue class there are \(p\) positive frequencies, \(q\) negative frequencies, and possibly the zero frequency \(c\). The positive derivative rows form the evaluation matrix of \((t)_{\underline j}\), \(1\le j\le k\), on distinct positive integers. Its rank is \(\min(p,k)\): every leading \(p\)-by-\(p\) minor for \(p\le k\) is a product of the positive nodes and a nonzero Vandermonde difference product. The negative block similarly has rank \(\min(q,k)\).

The remaining value row adds one dimension precisely when a constant coefficient is present, or when either sign class has more than \(k\) frequencies. To prove the latter, suppose the value row on at least \(k+1\) distinct positive integers lay in the span of the order-one-through-\(k\) falling-factorial rows. A polynomial of degree at most \(k\) and with zero constant term would then equal one at at least \(k+1\) distinct positive points. Subtracting one would give at least \(k+1\) roots but a nonzero value at zero, impossible. The same argument holds for the negative class. If there is no zero frequency and both sign classes contain at most \(k\) frequencies, their derivative rows already span their entire coefficient columns, so the value row adds nothing. This proves exactly the block rank \(\min(p,k)+\min(q,k)+\epsilon\), hence the stated sum.

**3. Sharp universal node count.** The space \(\mathcal H_{\le L}\) has complex dimension \(2L+1\), while every order-\(k\) harmonic jet has complex dimension at most \(2k+1\). For any points, injectivity therefore requires \(M(2k+1)\ge2L+1\).

Conversely suppose this bound holds and use the regular \(M\)-gon. Then \(L/M<k+1/2\). In residue zero the number of positive and negative frequencies is \(\lfloor L/M\rfloor\le k\), and the constant supplies the value row, so that block has full column rank. In any other residue, there are at most \(k+1\) positive and at most \(k+1\) negative frequencies; moreover the whole arithmetic progression in \([-L,L]\) has at most \(\lfloor 2L/M\rfloor+1\le2k+1\) frequencies. Hence either both sign counts are at most \(k\), or exactly one is \(k+1\) and the other is at most \(k\). The block-rank formula in both cases equals its number of columns. All blocks have full column rank, completing sufficiency. The DFT and Vandermonde reductions are also an explicit inverse algorithm.

**4. Tangential-only comparison.** For the trace \(\sum_{n=-L}^{L}c_ne^{in\theta}\), derivatives of orders \(0,\ldots,k\) yield, after the DFT, standard polynomial Vandermonde blocks in the distinct integer frequencies, with at most \(k+1\) rows per residue. Every such block has full column rank exactly when its frequency count is at most \(k+1\). For a consecutive integer band this is equivalent to \(M(k+1)\ge2L+1\), proving the comparison.

## Verification

The included Python standard-library checker constructs every integer residue block, compares its exact rational row rank with the closed formula, and verifies the universal threshold for \(0\le k\le4\), \(0\le L\le16\), \(1\le M\le14\). It additionally constructs independently the unreduced complex boundary-jet matrix and compares numerical ranks to the block formula for \(0\le k\le3\), \(0\le L\le8\), \(1\le M\le11\). All 10,514 assertions passed. These checks do not constitute an infinite proof; Steps 1–4 do.

For a square first-jet example, \(L=4\), \(k=1\), \(M=3\), the residue frequency sets are \(\{-3,0,3\}\), \(\{-2,1,4\}\), and \(\{-4,-1,2\}\). Their three-by-three jet blocks have nonzero determinant magnitudes \(9\), \(6\), and \(6\), respectively. Thus nine complex measurements at three points recover all nine Fourier coefficients.

Reproduce by running `python checker.py` from the directory containing this file and the checker; no third-party Python library is required.

## Relationship to prior work

Berriochoa, Cachafeiro, García Rábade, and García-Amor (2021) treat Hermite interpolation on unit-circle node arrays for Laurent polynomials and convergence. Cachafeiro and collaborators (2014) give explicit equispaced Laurent-polynomial interpolation from values and the first two derivatives of the Laurent trace. These are tangential/Laurent derivative data, not the complete harmonic interior jet with independent holomorphic and antiholomorphic directions in the present theorem. The sharp distinction is the order-\(k\) local harmonic data dimension \(2k+1\), compared with \(k+1\) for tangential derivatives of the same order.

Bojanov and Xu (2000) prove poised Hermite interpolation for all bivariate polynomials on concentric circles from consecutive radial derivatives at specified equidistant node counts. That ambient polynomial space and its radial-only measurements are different: the present theorem proves the universal minimal node count and exact undersampling rank for the harmonic subspace under complete spatial jets. Chandrasekaran, Gorman, and Mhaskar (2017) study derivative-data interpolation on manifolds in a general Sobolev setting; the present result instead supplies a finite Fourier exact-rank classification. These distinctions do not rule out an equivalent theorem in other literature.

## Limitations

No uniform frame bounds, noise resilience, statistical efficiency, reconstruction stability under node perturbations, or extension to higher spatial dimensions is asserted. The rank formula depends on all equispaced measurements being available and on complete jets rather than an arbitrary subset of derivatives. Historical priority is based on the examined primary literature and catalog comparisons and is not a proof of first discovery.

## References

1. E. Berriochoa, A. Cachafeiro, H. García Rábade, and J. M. García-Amor, *Mechanical Models for Hermite Interpolation on the Unit Circle*, Mathematics 9 (2021), 1043. First available May 6, 2021. https://doi.org/10.3390/math9091043
2. A. Cachafeiro et al., *Hermite Interpolation on the Unit Circle Considering up to the Second Derivative*, 2014. https://doi.org/10.1155/2014/808519
3. B. Bojanov and Y. Xu, *On a Hermite Interpolation by Polynomials of Two Variables*, SIAM J. Numer. Anal. (2000). Open full-text: https://homepage.divms.uiowa.edu/~atkinson/Seminar/BoXu1.pdf
4. S. Chandrasekaran, C. H. Gorman, and H. N. Mhaskar, *Minimum Sobolev Norm Interpolation of Derivative Data*, 2017. https://arxiv.org/abs/1710.01419
