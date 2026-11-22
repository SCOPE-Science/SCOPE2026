# A noncentral-to-Gaussian transition for simplicial depth near the center of a circle

## Finding

Let \(X_1,\ldots,X_n\) be independent uniform-arclength points on the unit circle, \(n\ge3\). For \(0\le r<1\), let \(T_n(r)\) count unordered triples whose convex hull contains \((r,0)\). Write \(p(r)=\mathbb E[T_n(r)]/\binom n3\), and let \(G_{kc},G_{ks}\), for odd positive \(k\), be mutually independent standard normal random variables. Set \(\lambda_k=-1/(\pi^2k^2)\) at odd \(k\).

For every fixed \(c\ge0\), as \(n\to\infty\),
\[
\frac{T_n(c/\sqrt n)-\tfrac14\binom n3}{n^2}\Longrightarrow Z_c
=\frac{\lambda_1}{2}\bigl((G_{1c}-c/\sqrt2)^2+G_{1s}^2-2\bigr)
+\frac12\sum_{\substack{k\ge3\\k\ \mathrm{odd}}}\lambda_k(G_{kc}^2+G_{ks}^2-2).
\]
The series converges in \(L^2\) and has the explicit moments
\[
\mathbb EZ_c=-\frac{c^2}{4\pi^2},\qquad \operatorname{Var}(Z_c)=\frac1{96}+\frac{c^2}{2\pi^4}.
\]
Thus the critical drift of the query point perturbs exactly **one** Fourier mode of the known central depth limit, producing a noncentral Gaussian-chaos law.

The transition scale is sharp. For any deterministic \(r_n\to0\), if \(\sqrt n\,r_n\to0\), the first displayed limit holds with \(c=0\). If instead \(\sqrt n\,r_n\to\infty\), then
\[
\frac{T_n(r_n)-\binom n3p(r_n)}{r_nn^{5/2}}\Longrightarrow N\!\left(0,\frac1{2\pi^4}\right).
\]
The *population* depth itself has the exact integral law
\[
p(r)=\frac14-\frac{3}{2\pi^3}\int_0^{2\pi}\arcsin^2(r\sin\theta)\,d\theta
=\frac14-\frac{3r^2}{2\pi^2}+O(r^4),\quad r\downarrow0.
\]
The new claim is the explicit moving-query transition and its sharp constants, **not** the classical central \(c=0\) distribution.

## Assumptions and scope

The sample is independent, exactly uniform by arclength on the full unit circle. The target lies strictly inside the disk and moves radially toward its center. Rotation shows that the orientation of the moving target is irrelevant. All boundary events have probability zero. The critical limit concerns fixed \(c\) and sufficiently large \(n\) so that \(c/\sqrt n<1\). The outer Gaussian result requires both \(r_n\to0\) and \(\sqrt n\,r_n\to\infty\), rather than a fixed noncentral location. The primary classification is the first-order weak-limit law with a precisely specified normalization; it does not assert a uniform Berry–Esseen rate or a functional limit over all target points.

## Proof

**1. Reduction to an angular triangular array.** For each point of the circle, write \(\Theta=\arg(X-(r,0))\in[0,2\pi)\). Since \((r,0)\) lies inside the unit disk, the map from circle position to viewing direction is a smooth, orientation-preserving bijection. Its angular density relative to normalized Lebesgue measure \(d\theta/(2\pi)\) is
\[
w_r(\theta)=1-\frac{r\cos\theta}{\sqrt{1-r^2\sin^2\theta}}
=1-r\cos\theta+O(r^3)
\]
uniformly in \(\theta\) for sufficiently small \(r\). For \(r=c/\sqrt n\), the joint sample law is contiguous to the uniform-direction sample: \(\mathbb E_0[(dP_r^n/dP_0^n)^2]=(\mathbb E_0w_r^2)^n\le\exp(O(nr^2))\), bounded for fixed \(c\). For \(\sqrt n r_n\to0\), the same likelihoods converge to one in \(L^2\).

**2. Exact population mean.** Write \(a_r(\theta)=\arcsin(r\sin\theta)\). Then \(w_r=1-a_r'\). The probability mass of a clockwise semicircle \((\theta,\theta+\pi)\) under \(P_r\) is \(h_r(\theta)=1/2+a_r(\theta)/\pi\). A triangle misses the origin precisely when all three directions lie within some open semicircle, which is uniquely indexed by its clockwise first point; therefore its failure probability equals \(3\int h_r^2\,dP_r\). Periodic integration by parts gives \(\int a_r\,dP_r=0\) and \(\int a_r^2\,dP_r=\int_0^{2\pi}a_r^2\,d\theta/(2\pi)\). Hence
\[
p(r)=1-3\int h_r^2\,dP_r
=\frac14-\frac{3}{2\pi^3}\int_0^{2\pi}a_r(\theta)^2\,d\theta.
\]
Since \(a_r(\theta)=r\sin\theta+O(r^3)\), the stated quadratic expansion follows, with a uniform \(O(r^4)\) remainder.

**3. Central Hoeffding kernel.** Let \(H(\theta_1,\theta_2,\theta_3)\) indicate origin containment by three rays. Under uniform directions, \(\mathbb EH=1/4\), and \(\mathbb E[H\mid\Theta_1=\theta]=1/4\). If two fixed directions have minor circular separation \(s\in[0,1/2]\), in units of a full revolution, then the allowed third directions occupy precisely a fraction \(s\) of the circle. Thus
\[
h_2(\theta,\phi)=\mathbb E[H\mid\theta,\phi]-\frac14=s(\theta,\phi)-\frac14.
\]
For \(u_{kc}(\theta)=\sqrt2\cos(k\theta)\) and \(u_{ks}(\theta)=\sqrt2\sin(k\theta)\), its real Fourier decomposition in \(L^2(P_0\otimes P_0)\) is
\[
h_2(\theta,\phi)=\sum_{k\ge1}\lambda_k\bigl[u_{kc}(\theta)u_{kc}(\phi)+u_{ks}(\theta)u_{ks}(\phi)\bigr],
\quad\lambda_k=2\int_0^{1/2}s\cos(2\pi ks)\,ds
=\frac{(-1)^k-1}{2\pi^2k^2}.
\]
In particular even modes vanish, odd modes are \(-1/(\pi^2k^2)\), and \(2\sum_{k\ge1}\lambda_k^2=1/48\).

The **exact** canonical decomposition of the unnormalized count is
\[
T_n(r)-\tfrac14\binom n3=(n-2)\sum_{i<j}h_2(\Theta_i,\Theta_j)+\sum_{i<j<k}h_3(\Theta_i,\Theta_j,\Theta_k),
\]
where \(h_3=H-1/4-h_2(\theta_i,\theta_j)-h_2(\theta_i,\theta_k)-h_2(\theta_j,\theta_k)\) is a bounded, fully canonical third-order kernel under \(P_0\). Under \(P_0\), the final sum has variance \(O(n^3)\). Therefore it vanishes after \(n^{-2}\) scaling under \(P_0\), and by the contiguity estimate of step 1 under every fixed critical \(c\) as well. The same transfer applies to truncating the Fourier expansion, because the uniform \(L^2\) error is bounded by a constant times \(\sum_{k>K}\lambda_k^2\).

**4. Critical noncentral limit.** Under \(r=c/\sqrt n\), the triangular-array multivariate central limit theorem gives, for each fixed collection of frequencies,
\[
\frac1{\sqrt n}\sum_i u_{1c}(\Theta_i)\Longrightarrow G_{1c}-\frac{c}{\sqrt2},
\]
whereas all other sine and cosine coordinates tend to independent centered standard Gaussians. Moreover \(n^{-1}\sum_i u_{kj}(\Theta_i)^2\to1\) in probability. The identity \(\sum_{i<j}u_i u_j=\frac12[(\sum_i u_i)^2-\sum_i u_i^2]\), multiplied by \((n-2)/n^2\), gives the finite-frequency noncentral quadratic series. Step 3 allows its extension to all frequencies by an \(L^2\)-truncation argument under \(P_0\) plus contiguity. Its variance is
\[
\sum_{k\ \mathrm{odd}}\lambda_k^2+\lambda_1^2\,c^2/2
=\frac1{96}+\frac{c^2}{2\pi^4},
\]
since \(\sum_{k\ \mathrm{odd}}k^{-4}=\pi^4/96\); its mean is \(\lambda_1c^2/4=-c^2/(4\pi^2)\). The standard central limit follows from the stronger convergence of the likelihood ratio to one when \(\sqrt n r_n\to0\).

**5. Gaussian outer window.** For each fixed \(r\), take the exact order-three Hoeffding decomposition under \(P_r\), with first canonical projection \(g_r(\theta)=\mathbb E_r[H(\theta,\Theta_2,\Theta_3)]-p(r)\). Differentiation at \(r=0\) of its bounded integrals, using step 3, yields uniformly
\[
g_r(\theta)=-2r\int h_2(\theta,\phi)\cos\phi\,dP_0(\phi)+O(r^2)
=\frac{2r}{\pi^2}\cos\theta+O(r^2).
\]
Consequently \(\operatorname{Var}_{P_r}(g_r)=2r^2/\pi^4+O(r^3)\). The linear term in the **unnormalized** \(T_n(r)\) is \(\binom{n-1}{2}\sum_i g_r(\Theta_i)\); its variance is \(n^5r^2/(2\pi^4)(1+o(1))\). For sufficiently small \(r\), all order-two and order-three canonical kernels are uniformly bounded, and their variances contribute \(O(n^4)\) and \(O(n^3)\), respectively. If \(r_n\sqrt n\to\infty\), these remainders are negligible at scale \(r_nn^{5/2}\). The triangular-array central limit theorem for bounded centered \(g_{r_n}/r_n\) then gives \(N(0,1/(2\pi^4))\).

## Verification

The supplied standalone `verify.py` (Python 3, no nonstandard packages) tests exact Fourier coefficients; the spectral variance identity; the overlap-derived central finite variance; independent brute-force angular-triple enumeration versus a semicircle sweep algorithm; geometric Jacobians of the displaced viewing direction; the small-displacement quadratic depth; and the limiting moment formulas. The checker reports 924 passed assertions. These tests corroborate the formulas only; the all-parameter and infinite-limit assertions are established by the analytic argument above.

## Relationship to prior work

Liu (1988) introduced simplicial depth, the exact object counted here, and established its role in location statistics. Killeen and Hettmansperger (2020 online/2021) derive the **central** count's exact finite null law and asymptotic null law; that known result is expressly not represented as new. Jentsch, Nagy and Wendler (2026) establish the fixed-query dichotomy of degenerate central versus nondegenerate off-center simplicial depth; the fixed-query theorem alone does not supply the explicit **shrinking-location**, mixed noncentral Fourier limit or the sharp variance coefficient proved above. Müller, Nagy and Trippler (2026) study bivariate sign-depth constructions and their distribution-free null testing, not this explicit moving-target limit. Koroleva and Nikitin (arXiv version first made public 7 January 2013) study geometric extremes in circle-sampled random polygons; their perimeter/area extremal asymptotics are not coverage of the present depth statistic.

The closest directly related earlier published research result on circular triangles above an angle threshold identifies the **right-angle** endpoint as a classical, previously solved central-depth law, and addresses fixed thresholds strictly above a right angle. The displaced query point here retains the right-angle criterion after a nonuniform change of viewing directions and is a different triangular-array limit. General noncentral U-statistic principles alone do not provide its explicit first-frequency shift and constants. This work does not claim novelty for classical Hoeffding theory, the null central spectrum, or the generic qualitative dichotomy. Historical priority is subject to the access limitations below.

## Limitations

The result requires exact uniform arclength sampling on the unit circle and a deterministic moving target that approaches the center. It does not cover a general elliptical density, arbitrary support, high dimensions, a random target, or a fixed nonzero target's explicitly normalized Gaussian law beyond its vanishing-radius frontier. The central \(c=0\) spectral limit is classical. Full text of Killeen–Hettmansperger (2020/2021) and of Jentsch–Nagy–Wendler (2026) could not be inspected through the available open textual representations. Their abstracts and published descriptions indicate null and fixed-query results respectively, but an unrecognized local-alternative section remains a concrete priority risk. No independent mathematical validation has been performed.

## References

1. R. Y. Liu, *On a notion of simplicial depth*, Proc. Natl. Acad. Sci. USA 85 (1988), 1732–1734, https://doi.org/10.1073/pnas.85.6.1732 (public author-uploaded full text inspected).
2. T. J. Killeen and T. P. Hettmansperger, *A bivariate test for location based on simplicial depth*, Commun. Statist. Theory Methods 50 (2021), 3954–3971, first online 2 March 2020, https://doi.org/10.1080/03610926.2019.1710205 (abstract inspected).
3. C. Jentsch, S. Nagy and M. Wendler, *Resampling simplicial depth*, arXiv:2608.11131, submitted 11 August 2026, https://arxiv.org/abs/2608.11131 (abstract inspected).
4. C. H. Müller, S. Nagy and S. Trippler, *Bivariate and multivariate sign depth and related distribution-free tests for model fit*, Metrika (2026), https://doi.org/10.1007/s00184-026-01041-6 (open-access HTML full article inspected).
5. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360v1, first public 7 January 2013, https://arxiv.org/html/1301.1360v1 (open-access HTML full article inspected).
6. W. Hoeffding, *A class of statistics with asymptotically normal distribution*, Ann. Math. Statist. 19 (1948), 293–325 (classical canonical decomposition).
