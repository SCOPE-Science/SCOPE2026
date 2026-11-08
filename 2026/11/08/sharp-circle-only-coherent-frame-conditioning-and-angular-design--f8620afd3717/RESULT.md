# Sharp circle-only coherence-frame conditioning and angular-design rigidity

## Finding

Let \(n\geq1\) be an integer. In the standard Bargmann–Fock polynomial space \(\mathcal P_n=\operatorname{span}\{z^k/\sqrt{k!}:0\leq k\leq n\}\), take any finite collection of positively weighted, normalized coherent-state observations supported on a *single* circle \(|z|=R>0\). Let \(A\) and \(B\) denote its optimal lower and upper frame bounds; write \(B/A=+\infty\) if the family is not a frame. There is an **exact universal optimum over the circle radius, any number of observations, all angular positions and all positive observation weights**:

\[
\inf_{R>0,\,M\geq1,\,\theta_j,\,w_j>0}\frac BA
=\mathcal K_n
:=\max_{0\leq k\leq n}\frac{(n!)^{k/n}}{k!}.
\]

The infimum is attained. A finite weighted family attains it **if and only if**

\[
R^2=(n!)^{1/n},\qquad
\sum_{j=1}^M w_j e^{id\theta_j}=0\quad (d=1,\ldots,n).
\]

Every optimizer therefore has at least \(n+1\) distinct angular sites. With exactly \(n+1\) sites, **the only optimizers** are rotations of the regular \((n+1)\)-gon with all weights equal (up to an overall common positive factor). Conversely, any positive weighted angular design annihilating the first \(n\) nontrivial Fourier moments attains the optimum at the specified radius. For \(n\ge2\), \(\mathcal K_n>1\): no single-circle positive sampling can be tight, irrespective of redundancy. Moreover,

\[
\mathcal K_n=
\sqrt e\,(2\pi n)^{(1/e-1)/2}
\exp(n/e)\bigl(1+O((\log n)^2/n)\bigr)
\quad(n\to\infty).
\]

Thus the sharp optimal *frame-bound ratio* grows exponentially in polynomial degree; the corresponding analysis-operator condition number is \(\sqrt{\mathcal K_n}\).

## Assumptions and scope

The full Bargmann–Fock Hilbert space has inner product \(\langle f,g\rangle=\pi^{-1}\int_{\mathbb C}f(z)\overline{g(z)}e^{-|z|^2}\,dA(z)\), linear in its first entry. The degree-\(n\) subspace \(\mathcal P_n\) is endowed with the inherited norm. A sample at \(z_j=Re^{i\theta_j}\) measures \(\sqrt{w_j}\,e^{-R^2/2}f(z_j)\), where \(w_j>0\) and repetitions of a site are allowed (their weights can be combined). The associated quadratic form is

\[
\sum_{j=1}^M w_j e^{-R^2}|f(Re^{i\theta_j})|^2.
\]

All claims hold simultaneously for every integer \(n\ge1\), every number \(M\ge1\), and every positive finite weight array. No upper bound on the total weight is imposed, because it cancels from \(B/A\). The lower bound is zero when the measurements do not span \(\mathcal P_n\). The object is a finite-degree, one-radius design problem, not the full infinite-dimensional Fock sampling problem.

## Proof

**1. Universal spectral lower bound.** In the orthonormal basis \(e_k(z)=z^k/\sqrt{k!}\), set \(x=R^2\) and \(W=\sum_jw_j\). The frame matrix is

\[
S_{k\ell}=\frac{e^{-x}x^{(k+\ell)/2}}{\sqrt{k!\ell!}}\sum_{j=1}^M w_j e^{i(\ell-k)\theta_j},\qquad 0\le k,\ell\le n.
\]

In particular, its diagonal entries are \(D_k=We^{-x}x^k/k!\), independent of angular placement. The Rayleigh principle gives \(\lambda_{\max}(S)\ge\max_kD_k\) and \(\lambda_{\min}(S)\le\min_kD_k\). If the minimum eigenvalue vanishes the ratio is infinite. Otherwise

\[
\frac BA\ge Q_n(x):=
\frac{\max_{0\le k\le n}x^k/k!}{\min_{0\le k\le n}x^k/k!}.
\]

**2. Unique optimal radius.** The positive sequence \(x^k/k!\) is log-concave in \(k\), hence its minimum occurs at \(k=0\) or \(k=n\). These endpoint values are equal only at \(x_0=(n!)^{1/n}\). For \(0<x<x_0\), the minimum is \(x^n/n!\), and each quotient \((x^k/k!)/(x^n/n!)\), \(k<n\), is strictly decreasing in \(x\); the maximum of these finitely many strictly decreasing functions is strictly decreasing. For \(x>x_0\), the minimum is \(1\), and each \(x^k/k!\), \(k\ge1\), is strictly increasing; their maximum is strictly increasing. Thus the unique minimizing radius is \(R^2=x_0\), and \(Q_n(x_0)=\mathcal K_n\). At \(x_0\), the minimizing entries are exactly those at \(k=0,n\) (for \(n=1\) these exhaust the indices).

**3. Rigidity at equality.** If \(B/A=\mathcal K_n\), step 2 gives \(x=x_0\). Let \(d=We^{-x_0}\) be the diagonal value at \(k=0\), and let \(D=\mathcal K_n d\) be the largest diagonal. The spectral inequalities \(\lambda_{\min}\le d\), \(\lambda_{\max}\ge D\), together with their ratio \(\lambda_{\max}/\lambda_{\min}=D/d\), force \(\lambda_{\min}=d\) and \(\lambda_{\max}=D\). Since the unit vector \(e_0\) has Rayleigh quotient \(d\), it lies in the minimum eigenspace, so \(S_{0\ell}=0\) for every \(\ell>0\). The displayed formula for \(S\) yields \(\sum_jw_je^{i\ell\theta_j}=0\) for \(\ell=1,\ldots,n\) (up to complex conjugation). Conversely, those vanishing moments make \(S\) diagonal, giving equality at \(x_0\).

**4. Minimum cardinality and equality placements.** If the first \(n\) moments vanish, the \(M\times(n+1)\) angular Vandermonde matrix \(V_{jk}=\sqrt{w_j}e^{ik\theta_j}\) obeys \(V^*V=WI_{n+1}\). Consequently \(M\ge n+1\). When \(M=n+1\), the square matrix \(V/\sqrt W\) is unitary. The norm of each row yields \(w_j=W/(n+1)\). Orthogonality of distinct rows yields \(\sum_{k=0}^n e^{ik(\theta_j-\theta_\ell)}=0\), so \(e^{i(\theta_j-\theta_\ell)}\) is a nontrivial \((n+1)\)-st root of unity. All sites therefore form a rotated regular polygon. Equal weights on such a polygon annihilate the first \(n\) Fourier moments, proving sufficiency and attainment. The case of repeated sample angles cannot have \(n+1\) independent rows and so cannot attain the minimum cardinality.

**5. Exponential asymptotic.** Put \(x_0=(n!)^{1/n}\). The unimodal sequence \(x_0^k/k!\) peaks at an integer nearest the transition between \(k\le x_0\) and \(k\ge x_0\): specifically \(k=\lfloor x_0\rfloor\), with an additional tied mode only if \(x_0\) is an integer. Stirling's formula gives

\[
x_0=\frac ne+\frac{\log(2\pi n)}{2e}+O((\log n)^2/n)
\]

and the maximal term equals \(e^{x_0}/\sqrt{2\pi x_0}\,(1+O(1/n))\), by Stirling and the fact that the maximizing index differs from \(x_0\) by at most one. Substituting the first estimate into the second gives the claimed asymptotic with relative remainder \(O((\log n)^2/n)\).

## Verification

The standalone `CHECK.py` independently builds the coherent observation matrix for fixed integer degrees, compares its Gram eigenvalues to the diagonal formula for regular-polygon designs, checks the universal bound for positive random angular weights, tests uniqueness of the optimal radius against perturbed radii, and compares the finite-degree optimum with its Stirling approximation. It reports 400 checks. All numerical checks are finite; they are not used to establish the universal quantifiers or the Stirling estimate, which are proved above.

## Relationship to prior work

The motivating work of Bownik and Yu (arXiv:2603.10423, first public 2026-03-11) establishes existence of nearly tight discretizations of continuous frames on suitable metric measure spaces, including planar Gabor systems. It places no one-circle constraint on the coherent-state sampling locations. The present result gives a sharp *negative quantitative constraint* for a geometrically restricted finite-degree sampling class. There is no contradiction: varying radii removes the diagonal obstruction.

Escudero, Haimi and Romero study stable Fock sampling and derivative interpolation using planar density conditions, rather than exact finite-degree one-circle optimal ratios. Speckbacher establishes sampling on *collections of infinitely many concentric circles* for full short-time Fourier transforms; this is not a stability result for any single finite circle. Berman and Feuer study perfect conditioning of angular Fourier–Vandermonde matrices; their unweighted unit-circle results do not determine the factorial radial conditioning obstruction. Janszky–Domokos–Adam and Luo–Tang–Zhang consider superpositions of circular coherent states and quantum observables; their available descriptions do not state the present all-weight minimax frame result. Elementary Fourier orthogonality, Gaussian monomial norms and Stirling asymptotics are used as established facts, not claimed as novel ingredients.

## Limitations

Only positive scalar observation weights, point-value coherent measurements, the standard one-dimensional Fock monomial basis and a common positive sampling radius are covered. Arbitrary preconditioning that depends on polynomial degree, multiple radii, derivative sampling or signed/complex quadratic weights can avoid this conclusion. The extremal classification is not a claim of global priority: older coherent-state and Vandermonde literature may contain equivalent statements under other terminology, and the full 1993 circular-coherent-state paper and 2024 optimal-circular-state paper were not available for decisive complete-text exclusion. Independent review has not been performed.

## References

1. M. Bownik and P.-T. Yu, *Uniform discretization of continuous frames*, arXiv:2603.10423v1 (first public 2026-03-11), https://arxiv.org/html/2603.10423v1.
2. L. A. Escudero, A. Haimi and J. L. Romero, *Multiple Sampling and Interpolation in Weighted Fock Spaces of Entire Functions*, Complex Analysis and Operator Theory 15 (2021), article 35, https://pmc.ncbi.nlm.nih.gov/articles/PMC7886767/.
3. L. Berman and A. Feuer, *On perfect conditioning of Vandermonde matrices on the unit circle*, Electronic Journal of Linear Algebra 16 (2007), https://doi.org/10.13001/1081-3810.1190.
4. J. Janszky, P. Domokos and P. Adam, *Coherent states on a circle and quantum interference*, Physical Review A 48 (1993), 2213–2219, https://doi.org/10.1103/PhysRevA.48.2213.
5. S. Luo, S. Tang and Y. Zhang, *Optimal circular states*, Journal of Physics A 57 (2024), 465301, https://doi.org/10.1088/1751-8121/ad8792.

6. M. Speckbacher, *Sampling Trajectories for the Short-Time Fourier Transform*, Journal of Fourier Analysis and Applications 28 (2022), article 82, https://pmc.ncbi.nlm.nih.gov/articles/PMC9581872/.
