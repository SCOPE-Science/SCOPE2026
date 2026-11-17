# Strict unimodality is exactly the stability-design law for weighted affine regression on a path

## Finding

For arbitrary ordered real abscissae \(t_0<\cdots<t_{n-1}\), \(n\ge2\), and strictly positive edge-variation weights \(w_1,\ldots,w_{n-1}\), consider the weighted least-squares projector \(P_\mu\) onto affine data \((a+bt_i)_i\), using any positive observation masses \(\mu_0,\ldots,\mu_{n-1}\). Put
\[
V_w(f)=\sum_{k=1}^{n-1}w_k|f_k-f_{k-1}|,
\qquad W=\sum_{k=1}^{n-1}w_k(t_k-t_{k-1}).
\]
There exists a **strictly positive observation-mass design** with \(V_w(P_\mu f)\le V_w(f)\) for every real data vector \(f\) **if and only if** the sequence \((w_k)\) is strictly increasing followed by strictly decreasing, allowing at most one equality between adjacent weights at their peak. Either increasing or decreasing portion may be empty. Equivalently, the consecutive differences \(w_k-w_{k+1}\) consist of negatives, then at most one zero, then positives. This characterization holds on every nonuniform grid and includes the one-edge case vacuously.

More precisely, for each positive \(\mu\), let
\[
m=\frac{\sum_i\mu_it_i}{\sum_i\mu_i},\qquad S=\sum_i\mu_i(t_i-m)^2,\qquad c_k=\frac{\sum_{i=k}^{n-1}\mu_i(t_i-m)}S.
\]
Then \(c_k>0\), and the exact, attained **two-input** operator seminorm is
\[
\operatorname{Lip}_{V_w}(P_\mu)=W\max_{1\le k<n}\frac{c_k}{w_k}\ge1.
\]
Every maximizing jump datum \(f_i={\bf1}_{\{i\ge k\}}\) attains this constant. Equality \(\operatorname{Lip}_{V_w}(P_\mu)=1\) holds precisely when \(c_k=w_k/W\) for all \(k\). Every nonexpansive observation-mass design is parameterized explicitly in the proof.

## Assumptions and scope

All signals and weights are real, all abscissae strictly increase, and every \(\mu_i,w_k\) is strictly positive. Only the finite path's adjacent-edge variation is considered; there is no absolute-value or mean term in the seminorm, whose nullspace consists of constants. \(P_\mu\) is the unique minimizer of \(\sum_i\mu_i(f_i-a-bt_i)^2\) evaluated on the input abscissae. Constants and affine data are exactly reproduced.

For \(n\ge3\), an admissible edge-weight profile has a strict rise and then a strict fall, with at most one flat step at the peak; a completely flat profile is admissible only for \(n=2,3\). Example: on \((t_0,t_1,t_2,t_3)=(0,1,2,3)\), edge weights \((1,2,1)\) and masses \((1,3,3,1)\) give the exact nonexpansive norm \(1\), while \((1,1,1)\) admits no strictly positive mass design with norm \(1\).

## Proof

**1. Linearization on single jumps.** Set \(s^{(k)}_i={\bf1}_{\{i\ge k\}}\). Weighted least squares gives the slope of the fitted line as
\[
B(f)=S^{-1}\sum_i\mu_i(t_i-m)f_i.
\]
Because \(B({\bf1})=0\), every data vector has the decomposition \(f=f_0{\bf1}+\sum_{k=1}^{n-1}(f_k-f_{k-1})s^{(k)}\) and hence
\[
B(f)=\sum_{k=1}^{n-1}c_k(f_k-f_{k-1}).
\]
For a strictly increasing grid the weighted covariance of \(t_i\) and \(s^{(k)}_i\) is strictly positive, so \(c_k>0\). One can check positivity directly: with \(M_L=\sum_{i<k}\mu_i>0\), \(M_R=\sum_{i\ge k}\mu_i>0\) and their conditional abscissa means \(m_L<m_R\), the numerator of \(c_k\) equals \(M_LM_R(m_R-m_L)/(M_L+M_R)>0\). Every fitted line has total weighted variation \(W|B(f)|\). The triangle inequality, followed by a single signed step at an index maximizing \(c_k/w_k\), proves the exact norm formula, its attainment, and its validity for differences of two arbitrary inputs.

**2. Rigidity at norm one.** Since \(P_\mu t=t\), using \(t_i-t_{i-1}>0\) in the slope decomposition yields
\[
1=\sum_{k=1}^{n-1}c_k(t_k-t_{k-1}).
\]
Set \(K=W\max_k(c_k/w_k)\). Then
\[
1\le(K/W)\sum_kw_k(t_k-t_{k-1})=K.
\]
Since all mesh gaps are positive, equality holds exactly when all ratios \(c_k/w_k\) are equal, hence \(c_k=w_k/W\).

**3. Necessary shape of edge weights.** Define \(c_0=0\) and \(c_n=0\). The centered-moment telescoping identity gives for all vertices
\[
c_i-c_{i+1}=\frac{\mu_i(t_i-m)}{S},\qquad 0\le i<n,
\]
where \(c_i\) on the left indexes edges after vertex \(i-1\) and the formula at the endpoints uses \(c_0=c_n=0\). In particular, for \(1\le i\le n-2\), if \(c_i=w_i/W\), then
\[
w_i-w_{i+1}=\frac{W\mu_i(t_i-m)}S.
\]
Thus successive edge-weight differences must be negative strictly to the left of \(m\), positive strictly to its right, and zero only at an interior vertex exactly equal to \(m\). Because distinct vertices cannot both equal \(m\), the allowed pattern has negatives followed by at most one zero followed by positives. This proves necessity.

**4. Explicit simultaneous design and completeness.** Suppose the stipulated difference-sign pattern holds. Choose \(m\in(t_0,t_{n-1})\) strictly between the last interior vertex with a negative difference and the first with a positive difference, with \(m=t_i\) if the unique zero difference occurs at vertex \(i\). When all signs have the same sign, choose \(m\) in the terminal gap on the appropriate side; such a choice always exists. Put
\[
\delta_0=-w_1,\quad \delta_i=w_i-w_{i+1}\ (1\le i\le n-2),\quad \delta_{n-1}=w_{n-1}.
\]
If \(\delta_i\ne0\), define \(\mu_i=\delta_i/(t_i-m)>0\); at the at most one interior index with \(\delta_i=0\), take an arbitrary \(\mu_i>0\) (necessarily \(m=t_i\)). Then telescoping yields
\[
\sum_i\mu_i(t_i-m)=\sum_i\delta_i=0,\qquad
\sum_i\mu_i(t_i-m)^2=\sum_i\delta_i(t_i-m)=W.
\]
Therefore this chosen \(m\) is indeed the weighted mean, \(S=W\), and \(c_k=\sum_{i\ge k}\delta_i/W=w_k/W\). It follows that the projector is variation-nonexpansive. Conversely, every positive nonexpansive design has this exact representation up to common positive scaling, with \(m\) equal to its weighted mean and the freely assignable mass allowed when an interior edge plateau occurs. This proves sufficiency and completeness.

## Verification

The accompanying standalone Python checker uses exact rational arithmetic. It exhaustively enumerates every positive integer edge-weight tuple with entries in \(\{1,2,3\}\) for path sizes two through seven, testing admissibility, all constructed masses, and the norm-one identities on a nonuniform rational grid (1,092 profiles). It also checks 3,000 independent irregular-grid rational instances for the derived coefficient, positivity, general norm bound and exact jump attainment. Executable reproduction: `python3 check_projection.py`. These checks corroborate, but do not replace, the all-size analytical argument.

## Relationship to prior work

Classical weighted least squares, including the locally weighted regression framework of Cleveland, provides the fitting operator; this result concerns a distinct, sharp path-variation norm and complete inverse mass/edge-weight design law. Steidl et al. investigate total-variation diffusion, wavelet shrinkage and regularization rather than the weighted affine regression projector. The published cyclic-order isotonic regression rigidity theorem deals with a nonlinear order-constrained map on a cyclic cover graph, not an affine orthogonal projector on an arbitrary weighted path. Previously known unweighted Whittaker–Henderson variation amplification concerns difference-penalty resolvents rather than this complete weighted projection design; its identity-fixed-space obstruction does not imply sufficiency for unimodal edge weights. No independence or historical novelty certificate is asserted.

## Limitations

The theorem classifies nonexpansivity, not the optimal coefficient when a prescribed edge-weight profile is inadmissible. It requires strictly positive observation and variation weights, and addresses the rank-two affine least-squares projector rather than all local regression smoothers, higher-degree polynomial projections, isotonic regression, or a finite-penalty Whittaker–Henderson smoother. Full-text access to Cleveland's original article was unavailable; older unindexed equivalent statements remain a historical-priority risk.

## References

1. W. S. Cleveland, *Robust Locally Weighted Regression and Smoothing Scatterplots*, Journal of the American Statistical Association **74** (1979), 829–836, DOI: https://doi.org/10.1080/01621459.1979.10481038. The original issue is dated December 1979; its day is not independently verified. A day-verified online publication event is April 5, 2012.
2. G. Steidl, J. Weickert, T. Brox, P. Mrázek, M. Welk, *On the Equivalence of Soft Wavelet Shrinkage, Total Variation Diffusion, Total Variation Regularization, and SIDEs*, Saarland University Preprint 94 (2003), https://lmb.informatik.uni-freiburg.de/people/brox/pub/steidl_pp94.pdf.
3. *Cyclic-cover rigidity of weighted variation stability for isotonic regression*, published finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-cyclic-cover-rigidity-of-weighted-variation-stability-for-isoton--c6a0693fe803.
4. *Only first-difference Whittaker–Henderson smoothing is universally range-preserving*, published finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-only-first-difference-whittaker-henderson-smoothing-is-universal--b1f399ec57e6.
