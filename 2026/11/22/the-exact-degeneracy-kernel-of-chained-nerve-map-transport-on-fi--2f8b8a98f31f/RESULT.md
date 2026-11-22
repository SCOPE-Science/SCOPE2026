# The exact degeneracy kernel of chained nerve-map transport on finite metrics

## Finding

For a finite metric space \((M,d)\) with \(n=|M|\ge2\), a scale \(0<r\le\operatorname{diam}M\), and the **strictly positive** probability simplex \(\mathcal P_+(M)\), McCabe and Perea's infimal-chain construction \(d_{\mathrm{ch}}^r\) has an exactly computable zero-equivalence relation.

Call \(x\in M\) *isolated at scale* \(r\) if its open radius-\(r\) ball is \(\{x\}\), and write
\[
I_r=\{x:d(x,y)\ge r\ \text{for every }y\ne x\},\qquad A_r=M\setminus I_r.
\]
Then, for all \(\mu,\nu\in\mathcal P_+(M)\),
\[
\boxed{d_{\mathrm{ch}}^r(\mu,\nu)=0\quad\Longleftrightarrow\quad
\mu(x)=\nu(x)\text{ for every }x\in A_r.}
\]
In particular, the chain pseudometric is a genuine metric on the whole positive simplex precisely when \(|I_r|\le1\). Define the nearest-neighbor distance \(\rho(x)=\min_{y\ne x}d(x,y)\), and list the values in nonincreasing order, including ties: \(\rho_{(1)}\ge\rho_{(2)}\ge\cdots\). The exact strict threshold is
\[
\boxed{d_{\mathrm{ch}}^r\text{ separates points on }\mathcal P_+(M)
\quad\Longleftrightarrow\quad r>\rho_{(2)}.}
\]
Equality at the threshold is on the nonseparating side. Moreover, whenever this criterion holds, there is an **explicit constant depending only on \((M,d,r)\)** bounding the chain metric below by the total variation norm, uniformly over all positive probability vectors.

## Assumptions and scope

Fix a finite strict metric space \((M,d)\), \(n\ge2\), and \(0<r\le\operatorname{diam}M\). Every \(\mu\in\mathcal P_+(M)\) has \(\mu(x)>0\) at every site and total mass one. All intermediate measures in chains must also lie in \(\mathcal P_+(M)\). The open radius-\(r\) balls include their centers but exclude points at distance exactly \(r\).

For each \(m,x\in M\), put \(k_m(x)=(r-d(m,x))_+\), and let \(S_m(\mu)=\sum_x k_m(x)\mu(x)\). Strict positivity implies \(S_m(\mu)\ge r\mu(m)>0\) at every site. The support of the weighted nerve map at \(m\) is exactly \(B_r(m)=\{x:d(m,x)<r\}\), independently of the positive measure. Thus the diameter appearing in the *pointwise* cost is the fixed quantity \(D_m=\operatorname{diam} B_r(m)\), with singleton diameter zero. The formula, with transport cost minimized over all couplings of \(\mu\) and \(\nu\), is
\[
\widetilde c_m(x,y)=\min\{k_m(x),k_m(y)\}\,d(x,y)
+D_m|k_m(x)-k_m(y)|,
\]
\[
T_{\widetilde c_m}(\mu,\nu)=
\min_{\pi\in\Pi(\mu,\nu)}\sum_{x,y\in M}\widetilde c_m(x,y)\pi(x,y),\quad
\Delta_L^r(\mu,\nu)=\max_{m\in M}
\frac{T_{\widetilde c_m}(\mu,\nu)}{\max\{S_m(\mu),S_m(\nu)\}}.
\]
As in McCabe--Perea, Appendix A, define
\[
d_{\mathrm{ch}}^r(\mu,\nu)=\inf\left\{
\sum_{j=0}^{N-1}\Delta_L^r(\mu_j,\mu_{j+1}):
N\ge1,\ \mu_0=\mu,\ \mu_N=\nu,\
\mu_j\in\mathcal P_+(M)\right\}.
\]
This is a symmetric pseudometric by finite-chain concatenation; it need not inherit the triangle inequality from \(\Delta_L^r\), which itself can fail that inequality.

## Proof

**1. A positive cost at each nonisolated site.** Fix \(x\in A_r\). Its ball contains \(x\) and some \(z\ne x\); therefore \(D_x>0\), and \(k_x(x)=r\). For any \(y\ne x\), the cost from \(x\) to \(y\) is
\[
\widetilde c_x(x,y)
=k_x(y)d(x,y)+D_x(r-k_x(y))>0.
\]
Indeed, if \(d(x,y)<r\), then \(k_x(y)>0\) and \(d(x,y)>0\); otherwise \(k_x(y)=0\) and the second term is \(D_xr>0\). Set
\[
a_x=\frac1r\min_{y\ne x}\widetilde c_x(x,y)>0.
\]
For any coupling \(\pi\) of \(\mu\) and \(\nu\), the amount transferred off the diagonal in the row or column of \(x\) is at least \(|\mu(x)-\nu(x)|\). Symmetry of \(\widetilde c_x\) yields
\[
T_{\widetilde c_x}(\mu,\nu)
\ge r a_x|\mu(x)-\nu(x)|.
\]
As \(S_x(\eta)\le r\) for every probability measure \(\eta\), we get \(\Delta_L^r(\mu,\nu)\ge a_x|\mu(x)-\nu(x)|\).

**2. The bound survives arbitrary chains.** Apply the last inequality to every link \((\mu_j,\mu_{j+1})\), then use the ordinary triangle inequality on its real coordinate \(x\). Every finite chain satisfies
\[
\sum_j\Delta_L^r(\mu_j,\mu_{j+1})
\ge a_x\sum_j|\mu_j(x)-\mu_{j+1}(x)|
\ge a_x|\mu(x)-\nu(x)|.
\]
Take the infimum over all finite positive chains, and then the maximum over \(x\in A_r\). Thus if the chain pseudometric vanishes, all nonisolated-site masses agree.

**3. Isolated-site mass is invisible.** If \(z\in I_r\), then \(z\) belongs to no open radius-\(r\) ball other than its own singleton ball. For a non-singleton ball at \(m\), both \(k_m(z)\) and \(\widetilde c_m(z,z')\) vanish for every pair \(z,z'\in I_r\); if \(B_r(m)\) is a singleton, \(D_m=0\) and \(\widetilde c_m\) is identically zero. If \(\mu\) and \(\nu\) agree on \(A_r\), their residual total masses on \(I_r\) agree. Couple all active-site mass diagonally, and couple the residual isolated-site masses arbitrarily among sites in \(I_r\). This coupling has zero \(\widetilde c_m\)-cost for every \(m\). Hence \(\Delta_L^r(\mu,\nu)=0\) and thus \(d_{\mathrm{ch}}^r(\mu,\nu)=0\). Together with Step 2, this proves the exact zero-equivalence relation. When \(I_r\) has at least two members, strictly positive measures of equal active-site coordinates but different isolated-site coordinates exist; so separation fails. With at most one isolated site, the probability-mass constraint makes equality on \(A_r\) equivalent to equality of the full measures, proving the metric criterion.

**4. Explicit total-variation coercivity.** When \(|I_r|\le1\), \(A_r\ne\varnothing\). Put \(a=\min_{x\in A_r}a_x>0\) and \(b=\max_{x\in A_r}|\mu(x)-\nu(x)|\). At most one site is outside \(A_r\). Because total signed mass is zero, the absolute difference at that outside site, if any, is at most the sum of the absolute differences at active sites. Hence
\[
\|\mu-\nu\|_1\le 2(n-1)b,
\quad d_{\mathrm{ch}}^r(\mu,\nu)\ge a b
\ge \frac{a}{2(n-1)}\|\mu-\nu\|_1.
\]
Finally, \(x\in I_r\) exactly when \(\rho(x)\ge r\). Thus having at most one isolated site is equivalent to the second-largest value \(\rho_{(2)}\) being strictly smaller than \(r\), including the case of tied nearest-neighbor distances. This proves the exact threshold.

## Verification

The supplied standalone Python script `nerve_chain_check.py` reconstructs the pointwise cost matrices and solves their finite transport linear programs using SciPy's HiGHS linear-programming solver. It reproduces McCabe--Perea's Appendix A three-point calculation exactly to numerical tolerance: the three pairwise pointwise estimates are \(3/4\), \(2/9\), and \(1/2\), demonstrating failure of the original pointwise triangle inequality. It also tests zero separation with two isolated sites, positive separation with a single isolated site, and 275 deterministic graph-shortest-path metric/scale pairs on three to six sites. In those cases it verifies the per-site coercive lower bound, including boundary scales exactly equal to metric distances. These finite computations check the definitions and examples but do not replace the universal proof above.

To replay: `python nerve_chain_check.py` with NumPy and SciPy installed. The script has no network dependency. All tested measures have strictly positive coordinates.

## Relationship to prior work

McCabe and Perea, *Wasserstein Stability of the Nerve Map* (arXiv:2611.15938v1; first public 11 November 2026), introduce the specific pointwise transport estimate, prove the broader **localized transport** distance is a genuine metric (Proposition 3.3), exhibit failure of the triangle inequality for the pointwise estimate (Appendix A, Example A.1), and introduce the infimal-chain pseudometric while expressly leaving its point-separation under additional hypotheses unresolved (Appendix A, final paragraph; Section 7). Their metric result does not resolve the present question: the pointwise estimate is bounded **above** by a normalized localized transport metric, which supplies no positive lower bound for the infimum over chains. The present classification provides such lower bounds on the positive simplex, identifies its entire zero kernel, and determines the sharp threshold in the scale parameter.

Jin, Mémoli, Smith, and Wan, *The Wasserstein Transform* (arXiv:1810.07793v2), consider normalized kernel-localized measures and prove Wasserstein **upper** stability estimates (Section 4.5.1, Theorem 27 and Lemma 48). They do not study McCabe--Perea's pointwise cost with its local support diameter, nor its finite-chain metricization. Adamaszek, Adams, and Frick's metric-thickening work supplies broader context but concerns Wasserstein geometry of simplicial thickenings rather than this chain distance.

## Limitations

The result treats a finite strict metric space, a fixed scale, strictly positive weights on **all** sites, and chains restricted to that same positive simplex. It does not establish point separation on arbitrary restricted support classes, on infinite compact metric spaces, or when chains may pass through zero-weight boundary measures. The explicit lower bound need not be the optimal Lipschitz constant, and the theorem gives no closed form for the nonzero values of the chain metric. Independent validation and comprehensive priority assessment have not been performed.

## References

1. Kenneth McCabe and Jose A. Perea. *Wasserstein Stability of the Nerve Map*. arXiv:2611.15938v1, 11 November 2026. https://arxiv.org/abs/2611.15938 . Relevant: Proposition 3.3, Theorem 3.4, Section 7, Appendix A.
2. Kun Jin, Facundo Mémoli, Zane Smith, and Zhengchao Wan. *The Wasserstein Transform*. arXiv:1810.07793v2 (12 April 2026 revision; original public 2018). https://arxiv.org/abs/1810.07793 . Relevant: Section 4.5.1, Theorem 27, Lemma 48.
3. Michał Adamaszek, Henry Adams, and Florian Frick. *Metric Reconstruction Via Optimal Transport*. SIAM Journal on Applied Algebra and Geometry **2** (2018), 597–619. https://doi.org/10.1137/17M1148025 . Context only.
