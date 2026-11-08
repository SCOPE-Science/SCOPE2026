# A sharp sample-size phase transition for positive Jacobi moment quadrature

## Finding
Let \(\mu_\alpha\) be the symmetric Jacobi probability measure with density proportional to \((1-x^2)^\alpha\) on \([-1,1]\), where \(\alpha>-1\). Draw \(m\ge2\) independent nodes uniformly from \([-1,1]\). Let \(P_m(\alpha)\) be the probability that **some nonnegative weights** on these prescribed nodes integrate every polynomial of degree at most two exactly against \(\mu_\alpha\). Put
\[
\tau=\frac{1}{2\alpha+3},\qquad r=\sqrt\tau,\qquad
B_{\rm out}=\frac{1+\tau}{2},\qquad B_{\rm in}=1-r.
\]
For every \(m\ge2\) and every \(0<\tau<1\), the exact finite-sample law is
\[
P_m(\alpha)=\frac{m}{2^m}\int_\tau^1
\left[(1+u)^{m-1}+(1-u)^{m-1}
 -(u+\tau/u)^{m-1}-(2-u-\tau/u)^{m-1}\right]du.
\tag{1}
\]
In particular,
\[
P_2(\alpha)=0,\qquad
P_3(\alpha)=\frac{3\tau}{2}\left(\log\frac1\tau-1+\tau\right),
\qquad P_4(\alpha)=2P_3(\alpha).
\tag{2}
\]
For fixed \(\alpha>-1\), the failure probability has a sharp, nonuniform-in-\(\alpha\) transition:
\[
1-P_m(\alpha)\sim
\begin{cases}
\displaystyle \frac{2}{1-\tau}\left(\frac{1+\tau}{2}\right)^m,
 & -1<\alpha<\sqrt2,\\[6pt]
\displaystyle \sqrt{\frac{\pi r}{2(1-r)}}\,\sqrt m\,(1-r)^m,
 & \alpha\ge\sqrt2.
\end{cases}
\tag{3}
\]
At \(\alpha=\sqrt2\), both exponential bases coincide at \(2-\sqrt2\), but the second mechanism dominates by a \(\sqrt m\) factor. At the uniform target \(\alpha=0\), the exact three-node success probability is \(\frac12\log3-\frac13\), and \(1-P_m(0)\sim3(2/3)^m\). For \(m\ge3\), the event in (1) is, with probability one, also the event that **all** prescribed nodes can be assigned strictly positive weights satisfying the moments, although a positive rule with at most three nodes always exists on the success event.

## Assumptions and scope
The target measure is \(d\mu_\alpha(x)=c_\alpha(1-x^2)^\alpha dx\) on \([-1,1]\), where \(c_\alpha=1/B(1/2,\alpha+1)\); independently, the candidate nodes \(X_1,\ldots,X_m\) are sampled from the **uniform** law on the same interval, not from the Jacobi target law or an importance/Lewis law. Exactness means there are weights \(w_i\ge0\) with
\[
\sum_{i=1}^m w_i=1,\qquad
\sum_{i=1}^m w_iX_i=0,\qquad
\sum_{i=1}^m w_iX_i^2=\tau.
\]
The expression for \(\tau\) follows by the beta-integral ratio \(\mathbb E_{\mu_\alpha}X^2=B(3/2,\alpha+1)/B(1/2,\alpha+1)\). The result concerns feasibility of positive weights, not the output of any particular least-squares estimator and not conditioning of the weights. All asymptotics hold with \(\alpha\) fixed.

## Proof
**1. Convex-hull certificate.** Map each node to \((x,x^2)\in\mathbb R^2\). The moment equations have a nonnegative solution precisely when \((0,\tau)\) belongs to the convex hull of these points. If one sign is absent, this is impossible almost surely. Otherwise let \(u_-\) and \(u_+\) be the smallest and largest absolute negative nodes, and \(v_-\), \(v_+\) the smallest and largest positive nodes. Since the parabola is strictly convex, the lower boundary of its sampled convex hull at horizontal coordinate zero is the chord joining the nearest opposite-sign nodes, at height \(u_-v_-\). The upper boundary is the chord joining the two extreme opposite-sign nodes, at height \(u_+v_+\). Hence the necessary and sufficient criterion is
\[
\boxed{u_-v_-\le\tau\le u_+v_+.}\tag{4}
\]
The conditions are strict almost surely whenever they hold. Then \((0,\tau)\) lies in the interior of the convex hull, which permits a strictly positive coefficient on every node: subtract a sufficiently small positive multiple of the nodes' average from the target and represent the remaining interior point convexly. Carathéodory's theorem provides an alternative representation using at most three nonnegative coefficients.

**2. Two extremal-pair densities.** For \(0<u,v<1\), the joint density of the largest opposite-sign magnitudes \((u_+,v_+)\), including the requirement of both signs, is
\[
f_+(u,v)=\frac{m(m-1)}{2^m}(u+v)^{m-2}.
\]
This follows by selecting two distinct extreme sample indices and forcing each of the remaining \(m-2\) samples into \([-u,v]\). Analogously, the density of the smallest opposite-sign magnitudes \((u_-,v_-)\) is
\[
f_-(u,v)=\frac{m(m-1)}{2^m}(2-u-v)^{m-2},
\]
because the other samples must avoid \((-u,v)\). On the event of both signs, \(u_-v_-\le u_+v_+\). Therefore the success event in (4) has probability
\[
P_m=\int_{uv\ge\tau}(f_+(u,v)-f_-(u,v))\,du\,dv,
\]
where both integrations range over the unit square. Integrate first in \(v\), between \(\tau/u\) and \(1\), then in \(u\), between \(\tau\) and \(1\), to obtain (1). Direct integration at \(m=2,3,4\) yields (2).

**3. Exact failure decomposition.** Let \(F_{\rm out}\) be the probability of no opposite-sign pair with product at least \(\tau\), including samples of one sign; let \(F_{\rm in}\) be the probability that the nearest opposite-sign product exceeds \(\tau\). These events are disjoint by (4) and
\[
1-P_m=F_{\rm out}+F_{\rm in}.
\]
Their exact, nonnegative integral representations are
\[
F_{\rm out}=2^{1-m}+\frac{m(m-1)}{2^m}
 \int_{\substack{0<u,v<1\\uv<\tau}}(u+v)^{m-2}\,du\,dv,
\tag{5}
\]
\[
F_{\rm in}=\frac{m(m-1)}{2^m}
 \int_{\substack{0<u,v<1\\uv>\tau}}(2-u-v)^{m-2}\,du\,dv.
\tag{6}
\]
Each corresponds to a distinct, geometrically identifiable failure mechanism (insufficient outer spread or an overly wide central gap).

**4. Sharp outer-spread asymptotic.** On the compact region \(uv\le\tau\) inside \([0,1]^2\), the function \(u+v\) has exactly two maximizers, \((1,\tau)\) and \((\tau,1)\), with maximum \(1+\tau\). Near the first, set \(u=1-s\) and \(v=\tau/(1-s)-t\), with \(s,t\ge0\). Then
\[
u+v=(1+\tau)-(1-\tau)s-t+O(s^2).
\]
The change of coordinates has Jacobian one. Two-dimensional boundary Laplace integration gives one contribution asymptotic to \((1+\tau)^m/[m^2(1-\tau)]\) to the unnormalized integral in (5). The second maximizer gives the same amount. Away from fixed neighborhoods of these maximizers the integrand is exponentially smaller. The factor \(m(m-1)/2^m\) gives
\[
F_{\rm out}\sim\frac{2}{1-\tau}\left(\frac{1+\tau}{2}\right)^m;
\]
the one-sign term \(2^{1-m}\) is smaller because \(\tau>0\).

**5. Sharp central-gap asymptotic.** Integrating (6) first in \(v\) yields
\[
F_{\rm in}=\frac m{2^m}\int_\tau^1
\big[(2-u-\tau/u)^{m-1}-(1-u)^{m-1}\big]du.
\tag{7}
\]
The second term is exponentially smaller than the first's maximum because \(1-\tau<2(1-\sqrt\tau)\). The strictly concave phase function \(2-u-\tau/u\) near its unique maximum at \(u=r=\sqrt\tau\) obeys
\[
2-u-\tau/u=2(1-r)-\frac{(u-r)^2}{r}+O(|u-r|^3).
\]
The one-dimensional Gaussian Laplace formula applied to (7) yields
\[
F_{\rm in}\sim \sqrt{\frac{\pi r}{2(1-r)}}\sqrt m\,(1-r)^m.
\]
The error outside a fixed neighborhood of \(r\) is exponentially smaller, so this is a full sharp equivalent, not merely a logarithmic rate.

**6. Crossover.** The two exponential bases are equal exactly when \((1+r^2)/2=1-r\), or \(r=\sqrt2-1\), i.e. \(\tau=3-2\sqrt2\). Substituting \(\tau=1/(2\alpha+3)\) gives \(\alpha=\sqrt2\). Above that value the central-gap base is larger; below it the outer-spread base is larger. At equality the extra \(\sqrt m\) central-gap prefactor wins. Equations (5)–(7) give (3).

## Verification
The accompanying standalone `verify.py` uses exact rational arithmetic to compare (4) against direct three-node moment-solvability witnesses across randomly generated sets. It additionally compares the finite-sample one-dimensional integral against the separately derived two-term failure decomposition, verifies the elementary \(m=3,4\) identities, and checks the large-sample prefactors numerically at the crossover and on each side. Running `python verify.py` under Python 3 using only the standard library passes **2,222** tested cases/groups. These are checks of the analytic calculations; numerical integration, sampled configurations, and observed asymptotic ratios do not prove the infinite-parameter theorem.

## Relationship to prior work
Bělík, Narayan and Turnage (arXiv:2609.09506, first posted September 8, 2026) develop randomized least-squares constructions, stability conditions, and positive-weight existence with high probability. Neumayer, Schäfer and Ullrich (arXiv:2610.32699, first posted October 23, 2026) establish positive exact quadrature from randomly sampled nodes under Lewis-density domination with a general sample-size guarantee. Both provide motivating existence theory and neither inspected full text supplied (1)–(3) for **uniformly sampled prescribed nodes**, **quadratic Jacobi moments**, or the specific \(\alpha=\sqrt2\) competition. Hayakawa, Lyons and Oberhauser (arXiv:2101.04250) establish general random-convex-hull probability inequalities and sample-size estimates; Hayakawa, Oberhauser and Lyons (arXiv:2210.05787) treat polynomial cubature sample complexity using hypercontractivity. Those works already cover the convex-hull framework, but their inspected main theorems do not supply the stated exact quadratic Jacobi law. Van den Bos and collaborators (arXiv:1809.09842) give sample-based positive quadrature algorithms, rather than an exact probability for uniform candidate nodes and a mismatched Jacobi target. The underlying convex-hull and moment-matching equivalence is classical and is not presented as new. The mathematical contribution here is the exact sampling law and its sharp two-mechanism asymptotics. Prior work on arbitrary-sample positive quadrature and convex moment curves remains relevant to a full historical-priority assessment.

## Limitations
The nodes must be iid uniform on \([-1,1]\), the moment space must be exactly \(\operatorname{span}\{1,x,x^2\}\), and the target must be the symmetric Jacobi law. The sharp equivalents are pointwise in fixed \(\alpha\), not uniform in a joint \(m,\alpha\) regime. The theorem asserts existence and does not identify a unique all-positive weight vector or bound conditioning, stability under finite precision, or performance of a prescribed construction algorithm. The exact integrals may suffer floating-point cancellation for extreme parameters and large sample counts; the separate positive failure integrals (5)–(7) are preferable for numerical evaluation. Independent mathematical validation has not been performed.

## References
1. F. Bělík, A. Narayan, J. Turnage, *Constructive Tchakaloff results and well-conditioned quadrature through randomized least squares*, arXiv:2609.09506v1 (2026-09-08), https://arxiv.org/abs/2609.09506.
2. S. Neumayer, M. Schäfer, T. Ullrich, *Random nodes with positive weights: Richter–Tchakaloff rules and optimal positive quadrature*, arXiv:2610.32699v1 (2026-10-23), https://arxiv.org/abs/2610.32699.
3. Classical convex-hull criterion for positive moment matching and Carathéodory's theorem (used as standard background, not novelty claimed).
4. S. Hayakawa, T. Lyons, H. Oberhauser, *Estimating the probability that a given vector is in the convex hull of a random sample*, arXiv:2101.04250v1 (2021-01-12), https://arxiv.org/abs/2101.04250.
5. S. Hayakawa, H. Oberhauser, T. Lyons, *Hypercontractivity Meets Random Convex Hulls: Analysis of Randomized Multivariate Cubatures*, arXiv:2210.05787v1 (2022-10-11), https://arxiv.org/abs/2210.05787.
6. L. M. M. van den Bos, B. Sanderse, W. Bierbooms, G. van Bussel, *Generating nested quadrature rules with positive weights based on arbitrary sample sets*, arXiv:1809.09842 (2018-09-26), https://arxiv.org/abs/1809.09842.
