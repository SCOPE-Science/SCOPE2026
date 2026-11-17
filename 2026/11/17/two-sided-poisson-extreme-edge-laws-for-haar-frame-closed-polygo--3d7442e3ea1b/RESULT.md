# Two-sided Poisson extreme-edge laws for Haar-frame closed polygons

## Finding

Let \(n\ge 3\), and sample a closed polygon of total edge length \(2\) by the Haar-frame construction described below. Write \(m_n\) and \(M_n\) for the shortest and longest edge lengths. The following four limits hold as \(n\to\infty\), with **joint independence** between the two components in each row:

| Ensemble | Longest-edge statistic converging to standard Gumbel | Shortest-edge statistic and its limit |
| --- | --- | --- |
| Closed planar polygons | \(\frac n2 M_n-\log n\) | \(\frac{n^2}{2}m_n\to \operatorname{Exp}(1)\) |
| Closed spatial polygons | \(nM_n-\log n-\log\log n\) | \(n^{3/2}m_n\to R\), \(\Pr(R>t)=e^{-t^2/2}\) |

More precisely, with the edge-index mark \(i/n\), **both entire extreme-edge point processes converge jointly to independent marked Poisson point processes**. For planar polygons the short-edge intensity is \(ds\,dt\) on \([0,1]\times(0,\infty)\); for spatial polygons it is \(ds\,t\,dt\). In both cases the long-edge intensity is \(ds\,e^{-x}\,dx\) on \([0,1]\times\mathbb R\), with marks and rescalings as in the table. These are statements of weak convergence in the vague topology on locally finite point measures, not total-variation convergence of the original dependent edge lengths.

There is also a quantitative comparison to an **exact independent reference model**. Put
\[
F_{\mathrm{pl}}(z)=1-e^{-z/2},\qquad F_{\mathrm{sp}}(z)=1-(1+z)e^{-z},\qquad z\ge0.
\]
For \(0\le t\le R\), \(|x|\le R\), and sufficiently large \(n\), define
\[
(a_n,b_n)=\begin{cases}
(2t/n,\ 2(\log n+x)),&\text{plane},\\
(t/\sqrt n,\ \log n+\log\log n+x),&\text{space}.
\end{cases}
\]
If \(H_n(x,t)\) is the joint probability that the normalized longest-edge variable is at most \(x\) **and** the normalized shortest-edge variable exceeds \(t\), then, with the corresponding \(F\),
\[
\sup_{|x|\le R,\ 0\le t\le R}
\left|H_n(x,t)-[F(b_n)-F(a_n)]^n\right|
=O_R\!\left(\frac{(\log n)^{3/2}}{\sqrt n}\right).
\]
For the planar case the limiting joint probability is \(\exp(-e^{-x}-t)\); for the spatial case it is \(\exp(-e^{-x}-t^2/2)\). Thus the independent-edge estimate of the probability that **all** edges lie below a near-critical maximum threshold becomes asymptotically exact, despite the finite-\(n\) closure constraint.

## Assumptions and scope

For the planar ensemble take a Haar-distributed orthonormal two-frame \(U=(u,v)\in V_2(\mathbb R^n)\), and set the \(i\)-th planar edge to \((u_i^2-v_i^2,\ 2u_iv_i)\). For the spatial ensemble take \(U=(u,v)\in V_2(\mathbb C^n)\), and set the \(i\)-th spatial edge to \((|u_i|^2-|v_i|^2,\ 2\operatorname{Re}(u_i\overline v_i),\ 2\operatorname{Im}(u_i\overline v_i))\). Orthogonality forces each edge list to sum to zero; its Euclidean edge lengths are precisely
\[
\ell_i=|u_i|^2+|v_i|^2,\qquad \sum_{i=1}^n\ell_i=2.
\]
The polygons need not be simple, convex, equilateral, or unknotted. The planar and spatial ensembles are distinct; neither is sampling independent edge vectors conditioned on exact closure. The results concern the full Haar-induced probability measures, with the total perimeter held at \(2\). No assumption of independent edge lengths is made.

Define, for the planar case,
\[
\Xi_n^{\rm small}=\sum_{i=1}^n\delta_{(i/n,\,n^2\ell_i/2)},\quad
\Xi_n^{\rm large}=\sum_{i=1}^n\delta_{(i/n,\,n\ell_i/2-\log n)};
\]
for the spatial case replace the second coordinates by \(n^{3/2}\ell_i\) and \(n\ell_i-\log n-\log\log n\), respectively. The short processes are viewed on \([0,1]\times(0,\infty)\), with the harmless inclusion of \(0\) when testing the minimum; the long processes on \([0,1]\times\mathbb R\). Convergence means convergence of joint Laplace functionals for nonnegative continuous compactly supported test functions, together with the stated endpoint minimum laws (obtained directly from the joint minimum/maximum formula).

## Proof

**1. An exact Gaussian representation.** For each \(n\), let \(G\) be an \(n\times2\) matrix whose entries are independent standard real normals (plane), or independent standard circular complex normals satisfying \(\mathbb E|G_{ij}|^2=1\) (space). Set \(S_n=G^*G/n\) and
\[
U=G(G^*G)^{-1/2}=n^{-1/2}GS_n^{-1/2}.
\]
The density of \(G\) is invariant under left orthogonal or unitary multiplication, so \(U\) is exactly Haar on the appropriate Stiefel manifold; its two columns are orthonormal. The Hopf/square map in the assumptions proves the edge-length identity. If \(T_i=\|G_{i,:}\|_2^2\), then \(T_1,\ldots,T_n\) are independent with laws
\[
T_i\sim\chi^2_2\quad(\text{plane}),\qquad
T_i\sim\operatorname{Gamma}(2,1)\quad(\text{space}).
\]
Their respective distribution functions are \(F_{\mathrm{pl}}\) and \(F_{\mathrm{sp}}\).

**2. Uniform global coupling.** Because the frame dimension is fixed, elementary Gaussian Chernoff bounds for a fixed net of unit vectors imply absolute \(c,C>0\) such that
\[
\Pr\!\left(\|S_n-I_2\|_{\rm op}>h\right)\le C e^{-cnh^2}
\quad(0<h<1/2).
\]
Indeed for every fixed unit vector \(z\), \(z^*S_nz\) is the average of \(n\) independent squared normal or complex-normal magnitudes, whose moment-generating function exists near zero; a fixed \(1/4\)-net transfers the scalar tail to the operator norm. Taking \(h=C_0\sqrt{\log n/n}\) with sufficiently large fixed \(C_0\), the exceptional probability is at most \(n^{-3}\). On its complement, with \(\delta_n=2h\), every single edge satisfies the **same** inequalities
\[
(1-\delta_n)T_i\le n\ell_i=G_{i,:}S_n^{-1}G_{i,:}^*\le(1+\delta_n)T_i.
\]
The probability-free inequalities are simultaneous in all \(n\) rows and retain even the rarest short and longest edges. In particular, \(\max_i T_i=O_{\Pr}(\log n)\), while \(\min_i T_i=O_{\Pr}(n^{-1})\) in the plane and \(O_{\Pr}(n^{-1/2})\) in space. Hence the normalized maxima and minima of \(\ell_i\) differ by \(o_{\Pr}(1)\) from their independent-\(T_i\) counterparts on the stated scales.

**3. Exact independent joint tails.** The independent model has, whenever \(0\le a_n<b_n\),
\[
\Pr\{\min_iT_i>a_n,\ \max_iT_i\le b_n\}
=[F(b_n)-F(a_n)]^n.
\]
For the planar model, \(nF_{\rm pl}(2t/n)\to t\) and \(n[1-F_{\rm pl}(2(\log n+x))]\to e^{-x}\). For the spatial model, \(nF_{\rm sp}(t/\sqrt n)\to t^2/2\) and \(n[1-F_{\rm sp}(\log n+\log\log n+x)]\to e^{-x}\). Therefore the joint limits are respectively
\[
\exp(-t-e^{-x}),\qquad\exp(-t^2/2-e^{-x}).
\]
This proves both the marginal extreme laws and their asymptotic independence, by Step 2.

**4. Finite-sample quantitative comparison.** On the good covariance event, the Stiefel joint event lies between independent events obtained by replacing \((a_n,b_n)\) by
\[
\left(\frac{a_n}{1-\delta_n},\frac{b_n}{1+\delta_n}\right)
\quad\text{and}\quad
\left(\frac{a_n}{1+\delta_n},\frac{b_n}{1-\delta_n}\right).
\]
The difference of their probabilities is at most \(n\) times the \(F\)-mass in the two intervening narrow boundary intervals. Uniformly for bounded \(x,t\), direct differentiation of the displayed \(F\)'s gives
\[
n\,a_nF'(z)=O_R(1)\ \text{for }z\asymp a_n,\qquad
n\,b_nF'(z)=O_R(\log n)\ \text{for }z\asymp b_n.
\]
At \(t=0\) the first interval is empty; no derivative bound at zero is needed. The resulting error is \(O_R(\delta_n\log n)+O(n^{-3})=O_R((\log n)^{3/2}/\sqrt n)\), giving the quantitative formula. For \(n\) large enough \(a_n<b_n\) uniformly on every stated compact parameter set.

**5. Joint marked point processes.** Consider first independent \(T_i\)'s. For any bounded interval of short-edge marks, its single-row probability is \(n^{-1}\) times the integral of the asserted short intensity, plus \(o(n^{-1})\); similarly, for any bounded interval of long-edge marks the probability is \(n^{-1}\int e^{-x}dx+o(n^{-1})\). The two classes of mark intervals are disjoint in the original \(T\)-variable for all sufficiently large \(n\). Thus, multiplying the independent one-row Laplace transforms over the grid \(i/n\), the logarithm converges to the sum of the negative Laplace exponents of two independent spatially marked Poisson measures. This also gives asymptotically independent uniform index locations of a fixed number of extremal edges. By Step 2, for any compact short-mark set the multiplicative error in its marks is \(o_{\Pr}(1)\), and for any compact long-mark set the additive error is \(O_{\Pr}(\delta_n\log n)=o_{\Pr}(1)\). Poisson processes have no atoms at deterministic test-set boundaries, so the coupled Stiefel processes have the same vague limits. This completes the proof.

## Verification

The standalone `check_extremes.py` script checks the exact frame orthogonality, closure, perimeter and Hopf/square edge-length identities for both real and complex ensembles; it checks the deterministic simultaneous Gaussian coupling bound on generated samples; and it compares numerical joint-tail frequencies against the exact finite-\(n\) independent reference formula. Run `python check_extremes.py` with NumPy installed. Its final success marker is `STIEFEL_TWO_SIDED_EXTREMES_CHECKS_OK`. The proofs of the uniform tail bound, Poisson limit and rate are analytic; the finite simulations are diagnostics, not substitutes for infinite-dimensional convergence.

## Relationship to prior work

Cantarella, Deguchi and Shonkwiler (2012), *Probability Theory of Random Polygons from the Quaternionic Viewpoint*, establish the Haar-frame model, exact one-edge beta distributions and tail bounds. In their Section 11 (see also Figure 7), independent edge lengths are explicitly a **simplifying assumption** for estimating a rejection sampler's success probability, not a theorem. The present result supplies a joint two-sided extreme-edge limit, its marked Poisson version and a quantitative finite-size justification of that approximation. Their single-edge marginal tail estimates and the present joint point-process statement are logically distinct.

Kabluchko and Prochno (2021), *Large deviations for random matrices in the orthogonal group and Stiefel manifold with applications to random projections of product distributions*, establish large-deviation principles for related real random matrices and their projections. A large-deviation principle does not, by itself, give the present two-sided Poisson edge statistics, their complex-frame analogue, or the compact-parameter finite-size comparison. Generic asymptotic Gaussian/normal-frame approximations motivate the coupling step but are not cited as prior statements of this precise polygon theorem.

## Limitations

The results apply only to Haar-induced closed polygon ensembles with total perimeter \(2\), not to equilateral polygons, arbitrary exchangeable closed edge models, self-avoiding polygons, or polygons conditioned on a knot type. The quantitative \(O_R\) constant is not made explicit and the comparison is on compact threshold sets; it is not a uniform total-variation estimate on the complete edge vector. For spatial polygons the convenient \(\log n+\log\log n\) centering approaches its Gumbel limit slowly, although the finite-\(n\) independent formula remains usable. No claim is made that Gaussian frame normalization or classical independent extreme-value theory is new. Historical originality remains subject to further literature scrutiny and independent mathematical review.

## References

1. Jason Cantarella, Tetsuo Deguchi, Clayton Shonkwiler, *Probability Theory of Random Polygons from the Quaternionic Viewpoint*, arXiv:1206.3161v1, publicly posted 14 June 2012, especially Sections 5, 9, 11 and Figure 7. https://arxiv.org/abs/1206.3161
2. Zakhar Kabluchko, Joscha Prochno, *Large deviations for random matrices in the orthogonal group and Stiefel manifold with applications to random projections of product distributions*, arXiv:2110.12977v1, publicly posted 25 October 2021. https://arxiv.org/abs/2110.12977
3. Petros Drineas, Malik Magdon-Ismail, Michael W. Mahoney, David P. Woodruff, *Fast approximation of matrix coherence and statistical leverage*, arXiv:1109.3843 (related coherence terminology; no geometric extreme-edge statement claimed from this source). https://arxiv.org/abs/1109.3843
