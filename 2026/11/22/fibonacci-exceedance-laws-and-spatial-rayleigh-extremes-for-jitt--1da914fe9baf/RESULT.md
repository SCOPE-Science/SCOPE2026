# Spatial near-maximum gap process for jittered interval samples

## Finding

Take independent \(U_1,\ldots,U_n\) uniform on \((0,1)\), and put \(X_i=(i-1+U_i)/n\) for \(1\le i\le n\). These are the ordered sites of the equal-stratum, one-site-per-stratum design. For internal gaps write
\[
G_{n,i}=n(X_{i+1}-X_i),\qquad T_{n,i}=\sqrt n(2-G_{n,i}),\qquad 1\le i<n.
\]
The location–deficit process satisfies
\[
\Xi_n=\sum_{i=1}^{n-1}\delta_{(i/n,T_{n,i})}\;\Longrightarrow\;\operatorname{PPP}(ds\,t\,dt)
\]
in the vague topology of locally finite point measures on \([0,1]\times[0,\infty)\).

In particular the spatial coordinate of the largest internal gap converges jointly with its scaled deficit to an independent uniform location and Rayleigh mark. For any fixed rank \(k\) (largest gaps first), the corresponding scaled deficit has limiting survival
\[
e^{-t^2/2}\sum_{j=0}^{k-1}\frac{(t^2/2)^j}{j!},\qquad t\ge0.
\]
The two boundary gaps, from 0 to \(X_1\) and from \(X_n\) to 1, do not change the limiting largest gap. The contribution is the joint spatial marked process for this design, not a new hard-core polynomial identity or a new general theorem for dependent maxima.

## Proof

**Geometry.** Since \(G_{n,i}=1+U_{i+1}-U_i\), for \(0\le\delta\le1/2\) the event \(G_{n,i}>2-\delta\) is \(U_{i+1}>1-\delta+U_i\), which has probability \(q=\delta^2/2\) by integrating the triangle. Two neighboring exceedances are incompatible: the first requires the shared jitter to be greater than \(1-\delta\), while the second requires it to be less than \(\delta\). At nonneighboring indices the gaps use disjoint uniforms. Thus for any fixed \(L\) and all \(n\) with \(L/\sqrt n\le1/2\), the law of a deficit mark on \([0,L]\) has density \(t/n\) and adjacent indices cannot both have marks in that window. Endpoint equalities have probability zero.

**Marked convergence.** For a nonnegative continuous test function \(f\) supported in \([0,1]\times[0,L]\), put \(h_i=\mathbb E[1-e^{-f(i/n,T_{n,i})}]=n^{-1}\int_0^L(1-e^{-f(i/n,t)})t\,dt\). Expanding the expectation of the product \(\prod_i e^{-f(i/n,T_{n,i})}\), the subsets containing a neighboring pair contribute zero by exclusion, and each other subset contributes \(\prod_{i\in S}(-h_i)\) by independence. Including the omitted terms gives \(\prod_i(1-h_i)\). The total absolute weight of those terms is at most
\[
e^{\sum_i h_i}\sum_{i=1}^{n-2}h_i h_{i+1}=O_L(n^{-1}),
\]
by charging every omitted subset to an adjacent pair it contains and summing over the other included indices. Since \(0\le h_i\le L^2/(2n)\), the logarithm of the product is \(-\sum_i h_i+O_L(n^{-1})\). Passing to the spatial Riemann sum gives the Laplace functional
\[
\exp\left(-\int_0^1\int_0^L(1-e^{-f(s,t)})t\,dt\,ds\right),
\]
which is that of the claimed Poisson point process. Convergence of these Laplace functionals is the vague point-process convergence criterion.

**Ranks and endpoints.** On each bounded window with no limit point on the cutoff, the point ordering by deficit is continuous whenever the relevant ranks exist and have no ties. The Poisson intensity is diffuse in the mark and the probability of fewer than \(k\) points in \([0,1]\times[0,L]\) tends to zero as \(L\to\infty\). The mean below \(t\) is \(t^2/2\), so a Poisson count of fewer than \(k\) gives the displayed survival. The factorized intensity gives independent uniform spatial coordinates conditional on the ordered marks. The boundary gaps are at most \(1/n\); independent gaps made from \(\lfloor n/2\rfloor\) disjoint uniform pairs each satisfy \(\Pr(G_{n,i}>1)=1/2\), so the chance that a boundary gap attains the overall maximum is at most \(2^{-\lfloor n/2\rfloor}\).

## Context: the finite count law and the univariate maximum

Let \(N_n(\delta)\) count internal gaps above \((2-\delta)/n\), and let \(M_n\) be the maximum including boundaries. The geometry realizes a one-dependent hard-core process with marginal \(q\) on the path of \(n-1\) indices. Its standard independent-set expansion [2, Lemmas 23–24] specializes to
\[
\mathbb E[z^{N_n(\delta)}]=\sum_{k=0}^{\lfloor n/2\rfloor}\binom{n-k}{k}q^k(z-1)^k,\qquad
\Pr(nM_n\le2-\delta)=\sum_{k=0}^{\lfloor n/2\rfloor}\binom{n-k}{k}(-q)^k,
\]
for \(n\ge2\) and \(0\le\delta\le1/2\). Indeed the mixed inclusion probability vanishes on any subset with neighbors and is \(q^k\) on an independent subset of size \(k\). There are \(\binom{n-k}{k}\) such subsets; the boundary gaps are below the threshold. Summing variances of the indicators and covariances of adjacent pairs yields \((n-1)q-(3n-5)q^2\). At \(\delta=0\) the count is zero. This finite law is a model-specific use of the prior hard-core identity, not a separate originality claim.

The univariate Rayleigh law alone also follows from Watson's dependent-maxima theorem in the form quoted in [3, §2]. The sequence \((2-G_{n,i})^{-1}\) is the restriction of a stationary 1-dependent sequence with upper tail \(1/(2y^2)\) for \(y\ge2\) and no adjacent exceedances at such a level. Using \(y=\sqrt n/t\), for fixed \(t>0\), yields \(\Pr(\sqrt n(2-nM_n)>t)\to e^{-t^2/2}\) by the endpoint bound. That theorem does not give the location–deficit process above.

## Verification and limitations

The supplied `checker.py` checks finite exceedance coefficients, variance, selected transfer-integral calculations and the univariate limit numerically; it does not prove the marked convergence. The analytic Laplace functional proof covers all fixed compact mark windows and ranks. The sample model assumes equal one-dimensional strata and independent uniform jitter. The finite polynomial applies only through \(\delta=1/2\). The marked convergence does not quantify gaps with macroscopic deficits. Indexed analogues on unstratified uniform spacings [3,5] use a different tail and Gumbel normalization; discrepancy for this very design [1] is a different statistic. Unindexed perturbed-lattice or scan-statistic precedents cannot be excluded.

## References

1. F. Pausinger and S. Steinerberger, *On the Discrepancy of Jittered Sampling*, §1, https://arxiv.org/abs/1510.00251.
2. A. E. Holroyd and T. M. Liggett, *Finitely dependent coloring*, §9, Lemmas 23–24 and Eq. (24), https://arxiv.org/abs/1403.2448.
3. A. Mijatović and V. Vysotsky, *On the Weak Limit Law of the Maximal Uniform k-Spacing*, Theorem 1 and §2, https://arxiv.org/abs/1508.00944.
4. G. S. Watson, *Extreme Values in Samples from m-Dependent Stationary Stochastic Processes*, Annals of Mathematical Statistics 25 (1954), 798–800.
5. *Independent spatial extreme fields for finitely many maximal uniform spacings*, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-independent-spatial-extreme-fields-for-finitely-many-maximal-uni--a7482687ed1b/RESULT.md.
