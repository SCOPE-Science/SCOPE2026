# Three angular phases of power-weighted lecture-hall simplices

## Finding
For a positive weight vector \(s=(s_1,\ldots,s_n)\), let
\[
P_n(s)=\left\{x\in\mathbb R^n:0\le x_1/s_1\le\cdots\le x_n/s_n\le1\right\}.
\]
Write \(v_{n,k}=(0,\ldots,0,s_{k+1},\ldots,s_n)\) for \(0\le k\le n\); thus \(v_{n,0}=(s_1,\ldots,s_n)\) and \(v_{n,n}=0\). Let \(J_n\in\{0,\ldots,n\}\) be the index of the vertex exposed by a uniformly random direction on the Euclidean unit sphere. Equivalently, \(\mathbb P(J_n=k)\) is the normalized spherical solid angle of its outward normal cone.

**Exact finite angle factorization.** For arbitrary strictly positive real weights and every \(0\le k\le n\), with independent standard Gaussian variables \(G_i\),
\[
\begin{aligned}
\mathbb P(J_n=k)&=L_{n,k}R_{n,k},\\
L_{n,k}&=\mathbb P\left(\sum_{i=k-r+1}^{k}s_iG_i<0\ \text{for every }1\le r\le k\right),\\
R_{n,k}&=\mathbb P\left(\sum_{i=k+1}^{k+r}s_iG_i>0\ \text{for every }1\le r\le n-k\right),
\end{aligned}
\]
where an empty event has probability one. In particular, for equal weights, the full exact angular spectrum is
\[
\mathbb P(J_n=k)=4^{-n}\binom{2k}{k}\binom{2n-2k}{n-k}.
\]

**Three-phase angular classification.** Fix any real \(\alpha\), take \(s_i=i^\alpha\), and let \(U\) have the classical arcsine distribution \(\operatorname{Beta}(1/2,1/2)\).

* If \(\alpha>-1/2\), then
  \[
  J_n/n\ \xrightarrow{\mathrm d}\ U^{1/(2\alpha+1)},\qquad
  \lim_{n\to\infty}\mathbb P(J_n/n\le t)
  =\frac2\pi\arcsin\left(t^{\alpha+1/2}\right)
  \quad(0\le t\le1).
  \]
  In particular, the limiting angular-index density is
  \[
  f_\alpha(t)=\frac{(2\alpha+1)t^{\alpha-1/2}}{\pi\sqrt{1-t^{2\alpha+1}}},\qquad 0<t<1,
  \]
  and the limiting mean rank is
  \[
  \lim_{n\to\infty}\mathbb E(J_n/n)
  =\frac{\Gamma(\frac12+\frac1{2\alpha+1})}{\sqrt\pi\,\Gamma(1+\frac1{2\alpha+1})}.
  \]
  This mean is strictly increasing in \(\alpha\); the classical linear-weight sequence \(s_i=i\) has limiting mean approximately \(0.7131741278\), rather than \(1/2\).
* If \(\alpha=-1/2\), there is no nondegenerate linear-rank limit. Instead,
  \[
  \frac{\log(J_n+1)}{\log n}\ \xrightarrow{\mathrm d}\ U.
  \]
  In particular, for each \(0<t<1\), the limiting angular mass of the first \(n^t\) indexed vertices is \(2\arcsin(\sqrt t)/\pi\).
* If \(\alpha<-1/2\), then on the natural infinite Gaussian coupling there is an almost surely finite random index \(J_\infty\) such that \(J_n=J_\infty\) for all sufficiently large \(n\). In addition, \(0<\mathbb P(J_\infty=0)\le1/2\). Thus angular mass remains on finitely indexed vertices, in contrast to both preceding regimes.

This is a statement about Euclidean spherical normal-cone measure and not about uniform sampling of vertices. For nonintegral weights, the objects are positive-weight Euclidean staircase simplices rather than lattice polytopes.

## Assumptions and scope
Throughout, \(n\ge2\), all weights are positive, coordinates carry the standard Euclidean metric, and the normal cones are **outward**. We label the \(n+1\) vertices by the number \(k\) of coordinates removed from the *beginning* of the full-suffix vertex; it is not an index measured from the origin. A centered Gaussian and a uniform random spherical direction expose the same vertex because multiplying the objective by a positive scalar does not change its maximizer. Gaussian ties have probability zero.

In the power family, \(\alpha\) is fixed independently of \(n\). The statements do not assert uniformity as \(\alpha\) approaches \(-1/2\) with \(n\), local asymptotics for individual angles, or an explicit distribution for the finite subcritical index \(J_\infty\).

## Proof
**1. Vertices and Gaussian support.** Set \(y_i=x_i/s_i\). The inequalities become \(0\le y_1\le\cdots\le y_n\le1\), whose vertices are exactly the indicator vectors of suffixes, including the zero suffix. The diagonal coordinate map \(y_i\mapsto s_i y_i\) is nonsingular. Thus the stated \(v_{n,k}\) are all vertices. For \(S_0=0\) and \(S_j=\sum_{i=1}^{j}s_iG_i\),
\[
\langle G,v_{n,k}\rangle=\sum_{i=k+1}^{n}s_iG_i=S_n-S_k.
\]
Maximizing this objective is precisely minimizing \(S_k\) over \(k=0,\ldots,n\). All differences \(S_k-S_j\) for \(k\ne j\) are nondegenerate centered Gaussians. The minimum is unique almost surely.

**2. Independent left/right persistence.** Fix \(k\). The event \(S_k<S_j\) for every \(j<k\) is the event that all \(k\) backward sums \(S_k-S_{k-r}\) are negative. The event \(S_k<S_j\) for every \(j>k\) is that all \(n-k\) forward sums \(S_{k+r}-S_k\) are positive. The former uses only \(G_1,\ldots,G_k\), the latter only \(G_{k+1},\ldots,G_n\); hence their probabilities multiply, giving the exact factorization. When the weights are constant, the Sparre Andersen theorem for continuous symmetric independent and identically distributed increments gives either \(m\)-step survival probability \(\binom{2m}{m}/4^m\), proving the displayed finite law.

**3. Gaussian variance clock.** Set \(A_0=0\), \(A_j=\sum_{i=1}^ji^{2\alpha}\). The Gaussian partial sums \((S_j)\) have the same joint law as Brownian motion \((B(A_j))\), since the independent increments have precisely these variances. For any \(n\) this identification is exact, not an invariance approximation. Let \(T_n=A_n\) and \(t_{n,j}=A_j/A_n\). Normalizing Brownian time and height shows that the law of \(J_n\) equals the index minimizing a standard Brownian motion sampled at the deterministic clock points \(t_{n,j}\in[0,1]\).

**4. Diffuse clocks.** For \(\alpha\ge-1/2\), \(A_n\to\infty\) and
\[
\max_{1\le j\le n}(t_{n,j}-t_{n,j-1})
=\frac{\max_{j\le n}j^{2\alpha}}{A_n}\longrightarrow0.
\]
Therefore the minimum among sampled Brownian values converges, in its *Brownian time coordinate*, to the almost surely unique minimizer \(U\) over \([0,1]\). Indeed, continuity and uniqueness separate the true minimizer from the complement of any fixed neighborhood by a strictly positive random gap; sufficiently fine grids enter that neighborhood. Lévy's arcsine theorem gives \(U\sim\operatorname{Beta}(1/2,1/2)\).

For \(\alpha>-1/2\), elementary power-sum asymptotics and monotonicity yield the uniform clock approximation
\[
\max_{0\le j\le n}\left|\frac{A_j}{A_n}-(j/n)^{2\alpha+1}\right|\longrightarrow0.
\]
The limiting clock is a strictly increasing homeomorphism of \([0,1]\). Inverting it at the unique Brownian minimizer gives \(J_n/n\Rightarrow U^{1/(2\alpha+1)}\). Transforming the beta density gives the stated CDF and density. Bounded convergence for the normalized index gives the mean formula from the standard beta moment. Coupling every exponent with the same nondegenerate \(U\in(0,1)\) proves strict increase of the limiting mean.

For \(\alpha=-1/2\), \(A_j=H_j=\sum_{i=1}^j1/i\). Uniformly over \(0\le j\le n\),
\[
\frac{H_j}{H_n}-\frac{\log(j+1)}{\log n}\longrightarrow0,
\]
where \(H_0=0\). (Use \(H_j=\log(j+1)+O(1)\) and \(H_n=\log n+O(1)\).) Hence the Brownian-time minimizer converges to \(U\) and the logarithmic-index minimizer differs from it by a uniformly vanishing amount, proving the critical law. This also implies \(J_n/n\to0\) in probability at criticality: for every fixed \(\varepsilon>0\), \(\log(\varepsilon n+1)/\log n\to1\), while \(U<1\) almost surely.

**5. Summable clocks.** Suppose \(\alpha<-1/2\). Since \(\sum_{i\ge1}i^{2\alpha}<\infty\), the independent centered Gaussian series \(S_j=\sum_{i\le j}i^\alpha G_i\) converges almost surely and in \(L^2\) to a finite \(S_\infty\). Define tails \(R_j=S_\infty-S_j\). The event that \(R_j\ge0\) for all sufficiently large \(j\) belongs to the tail sigma-algebra, so by the zero-one law has probability zero or one. By symmetry it has the same probability as the analogous eventual nonpositivity event. The two events are disjoint almost surely (all tails cannot be identically zero), so each has probability zero. Thus almost surely the tails have both signs arbitrarily late. In particular, some finite \(j\) satisfies \(S_j<S_\infty\). Since \(S_j\to S_\infty\), the global discrete minimum is attained among finitely many indices. It is unique almost surely, as every pairwise difference is a nondegenerate Gaussian. Denoting its index by \(J_\infty\), eventual equality \(J_n=J_\infty\) follows immediately.

Finally, \(\mathbb P(J_\infty=0)>0\): choose a sufficiently large finite \(K\) such that the Gaussian tail partial-sum supremum \(\sup_{j\ge K}|S_j-S_K|\) is less than a fixed positive \(\delta\) with positive probability (Doob's \(L^2\) maximal inequality). Independently, the finite-prefix event \(S_1,\ldots,S_K>2\delta\) has positive probability by the positive Gaussian density. On their intersection, \(S_j>0\) for every \(j\ge1\), so the unique minimizer is \(0\). Conversely \(\mathbb P(J_\infty=0)\le\mathbb P(S_1>0)=1/2\). This completes all three regimes.

## Verification
The standalone file `verify_exposure.py` uses independently generated Gaussian objectives to check the vertex-objective identity (5,200 samples), an exact analytic three-angle formula in dimension two for five exponents, and the exact Sparre Andersen spectrum for nine increments. It also reports direct high-dimensional CDF diagnostics for the positive, zero, and critical exponents, and subcritical finite-index stability under a coupled 30,000-increment sample. Running `python3 verify_exposure.py` produced `POWER_STAIRCASE_EXPOSURE_PASS`. These finite checks are corroboration only: the infinite-dimensional statements rest on the proof above.

In dimension two the exact probabilities, writing \(b=2^\alpha\), are
\[
\begin{aligned}
\mathbb P(J_2=0)&=\tfrac14+\tfrac1{2\pi}\arcsin\bigl((1+b^2)^{-1/2}\bigr),\\
\mathbb P(J_2=1)&=\tfrac14,\\
\mathbb P(J_2=2)&=\tfrac14+\tfrac1{2\pi}\arcsin\bigl(b(1+b^2)^{-1/2}\bigr).
\end{aligned}
\]
They sum to one and give an independent normalization check of the factorization.

## Relationship to prior work
The lecture-hall simplex and its suffix vertices are established objects in the work on lecture-hall polytopes by Kohl and Olsen, and in Olsen's geometric survey. Earlier work by Beck and collaborators studies Ehrhart and triangulation properties of the classical lecture-hall cone and simplex. Those results provide the polyhedral definition and context, not the index of a uniformly Gaussian-exposed vertex. Lévy's arcsine theorem and the Sparre Andersen survival formula are classical probabilistic inputs; neither is claimed as new. The present claim is the geometric normal-cone factorization and the three-scale classification for power Euclidean weights, including the logarithmic threshold and almost-sure finite-index condensation. Related geometric notes treat a single terminal spike in the weights or Euclidean curvature spectra of power-weighted simplices, rather than this complete angular rank phase diagram.

## Limitations
The weights \(i^\alpha\) cease to be integral for many exponents, and for \(\alpha<0\) are decreasing; the result therefore concerns a natural Euclidean extension of the lattice-polytope family. The Brownian arcsine identity itself is classical and the proof uses its standard time-change mechanism. There is no claim of a local limit for any single angular mass at growing ranks, any uniform-in-exponent approximation, or an explicit law for \(J_\infty\). Historical originality remains subject to independent review, especially for results indexed as inhomogeneous Gaussian random-walk minima rather than lecture-hall geometry.

## References
1. F. Kohl and M. Olsen, *Level algebras and s-lecture hall polytopes*, first arXiv version 2017-10-30, https://arxiv.org/abs/1710.10892.
2. M. Olsen, *Polyhedral geometry for lecture hall partitions*, arXiv first version 2018-08-18, https://arxiv.org/abs/1808.06131.
3. P. Brändén and L. Solus, *Some algebraic properties of lecture hall polytopes*, arXiv first version 2019-11-27, https://arxiv.org/abs/1911.12459.
4. M. Beck, B. Braun, M. Köppe, C. Savage and Z. Zafeirakopoulos, *Generating functions and triangulations for lecture hall cones*, arXiv:1508.04619, https://arxiv.org/abs/1508.04619.
5. D. Denisov, A. Sakhanenko and V. Wachtel, *First-passage times for random walks with nonidentically distributed increments*, Annals of Probability 46 (2018), 3313–3350, https://doi.org/10.1214/17-AOP1248.
6. Classical probability facts used: Lévy's Brownian arcsine law; Sparre Andersen's symmetric continuous-increment survival formula; Kolmogorov's zero-one law.
