# Finite-time singular collapse and lag-filtered fluctuations in delayed tent dynamics

## Finding
For integers \(d>k\geq1\), consider the endpoint of the delayed Lozi family
\[
 F(x_1,\ldots,x_d)=(T(x_k),x_1,\ldots,x_{d-1}),\qquad T(t)=1-2|t|,
\]
on \(Q=[-1,1]^d\). This is the parameter choice \(a=2\) and \(\nu=1\) in the Bilal--Ramaswamy recurrence. The system has the following exact statistical description.

Define
\[
 M=\{x\in Q:x_j=T(x_{j+k})\text{ for }1\leq j\leq d-k\}.
\]
Let \(H:[-1,1]^k\to M\) assign the last \(k\) coordinates \(H(u)_{d-k+j}=u_j\), for \(1\leq j\leq k\), and assign every earlier coordinate recursively by \(H(u)_j=T(H(u)_{j+k})\). Write \(\lambda\) for uniform probability on \([-1,1]\) and put \(\mu=H_*(\lambda^{\otimes k})\). Then:

1. \(M\) is invariant, \(F|_M\) is conjugate under \(H\) to \(G(u_1,\ldots,u_k)=(T(u_k),u_1,\ldots,u_{k-1})\), and \(G^k=T^{\times k}\). The invariant probability \(\mu\) is mixing, is supported on a Lipschitz \(k\)-dimensional graph, and is singular relative to ambient \(d\)-dimensional volume.
2. The initial uniform ensemble collapses to its stationary probability **exactly** after \(d-k\) iterates:
\[
 F^{d-k}_*(\lambda^{\otimes d})=\mu.
\]
For every probability density on \(Q\), its pushforwards converge to \(\mu\) in total variation as time tends to infinity. The latter statement does not extend to arbitrary singular initial measures, because periodic orbit measures exist.
3. Under \(\mu\), let \(Z_n\) be the first coordinate of the \(n\)-th iterate and \(Y_n=Z_n^2-1/3\). The **linear** covariance \(\operatorname{Cov}(Z_0,Z_n)\) vanishes for all \(n\geq1\), whereas the centered quadratic observable has the exact lag-filtered covariance
\[
 \operatorname{Cov}(Y_0,Y_n)=
 \begin{cases}
 \frac4{45}\,4^{-n/k}, & k\mid n,\\
 0,&k\nmid n,
 \end{cases}\qquad n\geq0.
\]
Consequently, in the convention \(S_Y(\omega)=\sum_{n\in\mathbb Z}\operatorname{Cov}(Y_0,Y_n)e^{-in\omega}\),
\[
 S_Y(\omega)=\frac4{45}\frac{1-4^{-2}}{1+4^{-2}-2\cdot4^{-1}\cos(k\omega)}.
\]
The stationary sums satisfy, for every fixed \(d>k\ge1\),
\[
 \frac1{\sqrt N}\sum_{n=0}^{N-1}Y_n\ \Longrightarrow\ \mathcal N(0,4/27).
\]
The asymptotic variance is independent of both delay dimensions and is \(5/3\) times the independent-sampling variance \(4/45\).

## Assumptions and scope
All integers satisfy \(1\leq k<d\). The state space is the invariant cube \(Q\); the map is not asserted to control initial states outside this cube. The law \(\mu\) is the physical invariant probability for initial data absolutely continuous with respect to volume on \(Q\). It is not the only invariant probability among all Borel probability measures.

## Proof
**Graph conjugacy and finite-time collapse.** For \(1\leq j\leq d-k\), the constraints \(x_j=T(x_{j+k})\) determine the earlier coordinates backwards from the last \(k\). This makes \(H\) a homeomorphism onto \(M\), bi-Lipschitz because both \(T\) and the last-coordinate projection are Lipschitz. A direct coordinate check gives \(F\circ H=H\circ G\) and \(G^k=T^{\times k}\). Moreover the last \(k\) coordinates of \(F^{d-k}(x)\) are exactly \((x_1,\ldots,x_k)\), and all preceding coordinates are prescribed by \(H\), so
\[
 F^{d-k}(x)=H(x_1,\ldots,x_k)\quad(x\in Q).
\]
This identity proves the finite-time ensemble equality for product-uniform input without any limiting argument. It also shows \(M=F^{d-k}(Q)\), a Lipschitz graph with Hausdorff dimension exactly \(k\), since the inverse graph projection is Lipschitz.

**The physical measure.** The two inverse branches of \(T\) at \(s\in[-1,1]\) are \(\pm(1-s)/2\), both with absolute slope \(2\). Thus \(T_*\lambda=\lambda\). The full-branch tent map is exact: its inverse branches yield dyadic conditional averages, and the transfer-operator iterates converge in \(L^1\) to the mean for step functions, hence for all integrable densities by approximation and contractivity. Its \(k\)-fold product \(T^{\times k}\) is exact by the same product dyadic-partition argument. In particular it is mixing; so is \(G\), as \(G^k=T^{\times k}\). Therefore \(\lambda^{\otimes k}\) is \(G\)-invariant and mixing, and \(\mu\) is \(F\)-invariant and mixing. For any absolutely continuous initial probability on \(Q\), the first \(k\)-coordinate marginal is absolutely continuous; after \(d-k\) iterates this becomes \(H_*\) of that marginal. The exactness of \(G\) gives the claimed total-variation limit. Since \(k<d\), \(M\) has zero ambient volume.

**Covariances and spectrum.** From \(G^k=T^{\times k}\), the stationary first-coordinate process splits by time residues modulo \(k\) into \(k\) independent stationary \(T\)-orbits, each with uniform one-point law. Its linear transfer response vanishes after one step. Write \(b(t)=t^2-1/3\), and write \(P\) for the transfer operator of \(T\) against \(\lambda\):
\[
 (Pf)(s)=\tfrac12[f((1-s)/2)+f(-(1-s)/2)].
\]
Direct substitution gives \(Pt=0\) and \(Pb=\tfrac14b-\tfrac12t\), hence for every integer \(m\geq1\),
\[
 P^mb=4^{-m}b-\tfrac12\,4^{-(m-1)}t.
\]
Uniform-moment identities give \(\int b^2\,d\lambda=4/45\) and \(\int tb\,d\lambda=0\). The transfer duality \(\int b(b\circ T^m)\,d\lambda=\int b(P^mb)\,d\lambda\) proves the quadratic covariance at multiples of \(k\); independence of distinct residue strands gives zero otherwise. Summing the two-sided geometric covariance series produces the stated spectral density. The linear covariances vanish because \(Pt=0\).

**Central-limit law.** The transfer-series solution \(v=\sum_{m\geq1}P^mb=\tfrac13b-\tfrac23t\) is bounded. Put \(h=b+v\) and \(m=h-v\circ T\). Then \(Pm=0\) and \(b=m-v+v\circ T\). The stationary sequence \(m\circ T^j\) is a bounded reverse martingale-difference sequence, to which the ergodic martingale central limit theorem applies; the bounded coboundary has negligible normalized sum. The single-strand variance, computed either from the martingale difference or the summable covariances, is
\[
 \frac4{45}+2\sum_{j\geq1}\frac4{45}\,4^{-j}=\frac4{27}.
\]
For the interleaved \(k\) strands, each residue class contributes an independent stationary tent orbit with about \(N/k\) terms. Independence and the fixed-\(k\) central limit theorem give total variance \(k\cdot(1/k)\cdot4/27=4/27\), proving the claim.

## Verification
A standalone standard-library exact-rational checker (`CHECK.py`) verifies the graph/intertwining identities for a range of integer dimensions and rational points, the transfer-operator identities, the first eight nonzero quadratic covariances, the variance summation, and the spectral-density normalization. These finite checks are supplementary: the argument above, not the enumerated checks, establishes the theorem for all eligible dimensions and all times.

## Relationship to prior work
Bilal and Ramaswamy (2020), Sections II--III, introduce this delayed Lozi family and already observe that \(\nu=1\) gives a \(k\)-dimensional endomorphism and a degenerate Lyapunov spectrum. Those observations are acknowledged here, not claimed as discoveries. The present statement specializes further to the full-height \(a=2\) map and determines an explicit singular stationary law, exact finite-step uniform initialization, delayed nontrivial quadratic memory, its frequency spectrum, and a dimension-independent fluctuation variance. General skew-tent correlation and other delayed-map results concern related mechanisms; no inspected source established this combined statement for the displayed family. This is a best-knowledge literature assessment, not proof of global publication priority.

## Limitations
The result is at the distinguished parameter choice \(a=2,\nu=1\), not an open parameter neighborhood. Total-variation attraction requires an absolutely continuous initial probability; periodic atomic invariant measures remain. The spectral density and Gaussian limit are for the specified stationary centered squared-coordinate observable, with fixed \(k\) as \(N\to\infty\), and no quantitative uniform-in-\(k\) CLT rate is asserted. Closely related transfer-operator methods may imply parts of the result; inaccessible or unindexed literature leaves residual novelty risk.

## References
- S. Bilal and R. Ramaswamy, *A higher-dimensional generalization of the Lozi map: Bifurcations and dynamics*, arXiv:2005.01849v1 (first public 2020-05-04), https://arxiv.org/html/2005.01849v1 . In particular Eq. (3), Eq. (5), Sections II--III.
- P. Góra, A. Boyarsky and Z. Li, *Singular SRB measures for a non 1--1 map of the unit square*, arXiv:1607.01658 (2016), https://arxiv.org/abs/1607.01658 . Related memory maps, structurally distinct from the zero-coupling delay limit studied here.
