# The sharp simplex-angle law for paired first-band spherical Fourier estimation

## Finding

Let \(d\ge3\) and \(m\ge1\). On the unit sphere \(\mathbb S^{d-1}\subset\mathbb R^d\), use normalized area measure \(\sigma\) and the real spherical Fourier subspace \(\mathcal H_1=\operatorname{span}_{\mathbb R}\{1,\sqrt d\,x_1,\ldots,\sqrt d\,x_d\}\). Its reproducing kernel is \(K(z,x)=1+d\langle z,x\rangle\). Let \((X_j,Y_j)\), \(1\le j\le m\), be independent, identically distributed pairs with **each marginal exactly** \(\sigma\); their joint coupling may otherwise be arbitrary. Define the unbiased random Fourier estimator
\[
 \widehat f_m(z)=\frac1{2m}\sum_{j=1}^m\bigl(f(X_j)K(z,X_j)+f(Y_j)K(z,Y_j)\bigr),\quad f\in\mathcal H_1.
\]
Then the sharp worst-case normalized squared \(L^2\) error over every such pair coupling is
\[
\boxed{\inf_\pi\ \sup_{\substack{f\in\mathcal H_1\\\|f\|_2=1}}m\,\mathbb E_\pi\|\widehat f_m-f\|_2^2=\frac{d-1}{2}.}
\]
**The complete equality classification** is: a coupling with uniform marginals is optimal if and only if \(\langle X,Y\rangle=-1/d\) almost surely. Such couplings exist in every dimension: sample \(X\) uniformly and take \(Y=-X/d+\sqrt{1-d^{-2}}Z\), where conditionally \(Z\) is uniform on the unit sphere orthogonal to \(X\). Independent sampling instead has worst-case value \(d/2\); antipodal pairing \(Y=-X\) has worst-case value \(d-1\). Thus the optimal pair is neither independent nor antipodal.

## Assumptions and scope

The norm \(\|\cdot\|_2\) is the \(L^2(\sigma)\) norm. Only real, degree-at-most-one spherical harmonics are considered. The estimator weights are fixed at \(1/(2m)\); the pairs are independent of one another and identically distributed, with uniform individual marginals, but dependence within each pair is unrestricted. The claim concerns **worst-case expected integrated squared error**, not almost-sure approximation, higher-degree harmonics, statistical least squares, or arbitrary nonuniform sampling marginals.

## Proof

1. The functions \(1\) and \(\sqrt d\,x_i\), \(1\le i\le d\), are orthonormal in \(L^2(\sigma)\); therefore \(K(z,x)=1+d\langle z,x\rangle\), \(\|K(\cdot,x)\|_2^2=d+1\), and \(\int f(x)K(\cdot,x)\,d\sigma(x)=f\) for \(f\in\mathcal H_1\). Each pair is unbiased. Independence of the \(m\) pairs divides the single-pair mean square error by \(m\).

2. Writing \(H_X=f(X)K(\cdot,X)\) and \(S=(H_X+H_Y)/2\), polarization and reproducing give, for every coupling with uniform marginals,
\[
\mathbb E\|S-f\|_2^2=\frac{d-1}{2}\|f\|_2^2+\frac12\mathbb E\bigl[f(X)f(Y)(1+d\langle X,Y\rangle)\bigr].\tag{1}
\]
Indeed \(\mathbb E\|H_X\|_2^2=(d+1)\|f\|_2^2\), \(\mathbb E S=f\), and \(\langle H_X,H_Y\rangle=f(X)f(Y)K(X,Y)\). At the fixed angle \(\langle X,Y\rangle=-1/d\), the cross term vanishes **pointwise for every input**, and (1) equals \((d-1)\|f\|_2^2/2\).

3. To prove global optimality, rotate an arbitrary coupling by a common independent Haar-uniform \(R\in O(d)\). Its input error quadratic form is the average of orthogonal conjugates of the original error form; hence its largest eigenvalue cannot increase. This averaging preserves uniform marginals and preserves the distribution of the pair inner product \(T=\langle X,Y\rangle\). Thus it suffices to analyze rotationally invariant joint laws, and their inner-product distributions retain information needed for equality.

4. Set \(u=\mathbb ET\) and \(v=\mathbb ET^2\). For a rotationally invariant pair, write \(f(x)=a+\sqrt d\,b\cdot x\). The conditional identity \(\mathbb E(Y\mid X,T)=TX\), together with \(\mathbb E X_iX_j=\delta_{ij}/d\), implies \(\mathbb E(f(X)f(Y)\mid T)=a^2+T\|b\|^2\). Substitution in (1) gives the **exact two-level input-error spectrum**:
\[
 A_d(u)=\frac d2(1+u)\quad\text{(one constant direction)},\qquad B_d(u,v)=\frac{d-1+u+dv}{2}\quad\text{(\(d\) linear directions)}.\tag{2}
\]
The worst-case value is \(\max\{A_d(u),B_d(u,v)\}\).

5. Since \(v\ge u^2\), the worst case is at least \(\max\{A_d(u),B_d(u,u^2)\}\). The difference factors as
\[
A_d(u)-B_d(u,u^2)=\frac{(1-u)(1+du)}2.\tag{3}
\]
For \(u>-1/d\), the increasing \(A_d(u)\) exceeds \((d-1)/2\). For \(u<-1/d\), \(B_d(u,u^2)>(d-1)/2\): the quadratic \(B_d(u,u^2)\) strictly decreases as \(u\) increases throughout \([-1,-1/d]\). At \(u=-1/d\), both equal \((d-1)/2\). Equality in the Jensen step requires \(v=u^2\), hence \(T=-1/d\) almost surely. Rotation averaging implies **every original** global minimizer has this same constant inner product. Conversely, step 2 proves every uniform-marginal coupling at that inner product attains the optimum. Independent coupling has \(u=0\), \(v=1/d\) and spectrum \(d/2,d/2\); the antipodal coupling has \(u=-1,v=1\), spectrum \(0,d-1\).

## Verification

The standalone Python script `checker.py` verifies factorization (3), optimal-angle equality, and independent/antipodal formulas by exact symbolic algebra. It also directly builds paired random-sampling error matrices for \(d=3,4,5,8\) and five angles per dimension, comparing all empirical eigenvalues to (2). Each case uses 24,000 independent pairs, with a deliberately loose stochastic tolerance of 0.32. These numerical checks corroborate (2), but do not prove the all-dimension or all-coupling theorem, which follows from the preceding algebra and rotation argument. Run `python checker.py` with NumPy and SymPy.

## Relationship to prior work

Brauchart, Grabner, Sloan and Womersley (first public preprint July 26, 2022) study spherical Fourier/needlet approximation with cubature that is not required to be polynomial-exact. Their Theorem 4.1 bounds multiscale generalized-needlet errors under deterministic quadrature assumptions; it does not optimize dependence between two uniformly sampled nodes. Earlier QMC-design work treats deterministic equal-weight Sobolev quadrature and optimal *rates*, rather than minimax variance of this degree-one reproducing-kernel estimator under arbitrary pair couplings. Subsequent Monte Carlo spherical quasi-interpolation literature uses different zonal kernels and multilevel methods. The present precise estimator and coupling class are essential; a generic antithetic-variance theorem is not asserted to be new.

## Limitations

The proof does not claim a new general spherical cubature theorem, higher-degree optimality, universality for noisy observations, or improvement over specially designed deterministic quadratures. Historical priority remains provisional: an older generic covariance-optimal coupling or spherical-design result might imply the conclusion after specialization. The symmetry argument requires \(O(d)\)-invariant surface measure and the stated uniform marginals. Pair independence, real-valued \(f\), fixed equal weights, and the first harmonic band are essential assumptions.

## References

1. J. S. Brauchart, P. J. Grabner, I. H. Sloan, R. S. Womersley, *Needlets Liberated*, arXiv:2207.12838, first version July 26, 2022, MSC2020 primary 42C10. https://arxiv.org/abs/2207.12838
2. J. S. Brauchart, E. B. Saff, I. H. Sloan, R. S. Womersley, *QMC designs: optimal order Quasi Monte Carlo Integration schemes on the sphere*, arXiv:1208.3267 (2012). https://arxiv.org/abs/1208.3267
3. Z. Sun, M. Lv, X. Sun, *Monte Carlo quasi-interpolation of spherical data*, arXiv:2510.12027 (2025), for later-context comparison only. https://arxiv.org/abs/2510.12027
