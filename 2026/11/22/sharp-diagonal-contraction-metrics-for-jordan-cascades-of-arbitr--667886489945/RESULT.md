# Sharp diagonal contraction metrics for Jordan cascades of arbitrary length

## Finding
For every integer \(n\ge5\), consider the stable nonnormal generator
\[
G=-aI_n+cN_n,\qquad a,c>0,\qquad (N_n)_{i,i+1}=1\quad(1\le i<n),
\]
with all other entries of \(N_n\) zero. For each positive diagonal matrix \(P=\operatorname{diag}(p_1,\ldots,p_n)\), write \(\kappa(P)=\max_i p_i/\min_i p_i\), \(\|x\|_P^2=x^*Px\), and
\[
\mu_P(G)=\lambda_{\max}\!\left(\frac{P^{1/2}GP^{-1/2}+P^{-1/2}G^*P^{1/2}}2\right).
\]
For **every** budget \(K\ge 2^{n-3}\), the sharp optimal weighted logarithmic norm is
\[
\boxed{\min_{\substack{P>0\ \mathrm{diagonal}\\\kappa(P)\le K}}\mu_P(G)
=-a+c(4K)^{-1/[2(n-1)]}.}
\]
The unique optimal diagonal metric up to a common positive factor is \(P_*(K)=\operatorname{diag}(p_1,\ldots,p_n)\) with
\[
q=(4K)^{-1/[2(n-1)]},\qquad p_1=1,\qquad
p_i=\frac{1}{2q^{2(i-1)}}\ (2\le i\le n-1),\qquad p_n=K.
\]
At the sharp onset \(K=2^{n-3}\), its first and last adjacent coordinates coincide; for all larger \(K\), every adjacent coordinate is strictly increasing.

More generally, for **every** \(K\ge1\), the lower bound
\[
\boxed{\inf_{\kappa(P)\le K}\mu_P(G)\ge-a+c(4K)^{-1/[2(n-1)]}}
\]
is sharp **if and only if** \(K\ge2^{n-3}\). Thus the exact high-budget formula has a sharp natural feasibility threshold, without claiming to solve the lower-budget optimization.

In particular, whenever the coupling-to-damping ratio satisfies \(c/a\ge\sqrt2\), the *least* condition-number budget admitting a positive diagonal Hilbert norm in which the entire semigroup \(e^{tG}\) is contractive is
\[
\boxed{K_{\mathrm{contr}}=\frac14\left(\frac ca\right)^{2(n-1)}.}
\]
At the boundary the displayed metric yields \(\|e^{tG}\|_{P_*}\le1\) for every \(t\ge0\), and no metric with smaller diagonal condition number does. For example, the five-stage chain \(G=-I_5+2N_5\) has the exact least contractivity budget \(64\), attained by \(P=\operatorname{diag}(1,2,8,32,64)\).

## Assumptions and scope
The state space is \(\mathbb C^n\) (equally valid over \(\mathbb R^n\)). The generator is the uniform-rate, one-way nilpotent Jordan cascade specified above. Its eigenvalues all equal \(-a\), so it is exponentially stable, but it can exhibit substantial short-time norm growth. The quadratic metrics are **positive diagonal only**. Condition numbers are those of the metrics \(P\), not of \(P^{1/2}\). The statement addresses logarithmic norms and all-time induced-norm contractivity, not the sharp Euclidean peak transient.

The high-budget theorem is for \(n\ge5\), \(K\ge2^{n-3}\) and arbitrary \(a,c>0\). The least-budget contractivity theorem additionally requires \(c/a\ge\sqrt2\). The lower bound and its sharpness criterion hold for every \(K\ge1\). These ranges are exact, including equality at their boundaries.

## Proof
**1. Reduction to a weighted path.** Put \(x_i=(p_i/p_{i+1})^{1/2}>0\), for \(1\le i<n\). The Hermitian part of \(P^{1/2}GP^{-1/2}\) is \(-aI_n+(c/2)T(x)\), where \(T(x)\) is the symmetric tridiagonal matrix with zero diagonal and \(T_{i,i+1}=T_{i+1,i}=x_i\). Since this weighted path is irreducible and nonnegative,
\[
\mu_P(G)=-a+\frac c2\rho(T(x)),
\]
where \(\rho\) is its positive Perron eigenvalue. The telescoping product identity is
\[
\prod_{i=1}^{n-1}x_i=\sqrt{p_1/p_n}\ge K^{-1/2},
\]
because \(p_n/p_1\le\kappa(P)\le K\), even when the coordinates of \(P\) are not monotone.

**2. Sharp universal edge-product inequality.** Choose the positive test vector
\[
u=(1,\sqrt2,\ldots,\sqrt2,1)^\mathsf T.
\]
For \(n\ge3\), \(\|u\|_2^2=2(n-1)\), and the product of adjacent coordinate products is
\[
\prod_{i=1}^{n-1}u_i u_{i+1}=2^{n-2}.
\]
The Rayleigh principle and the arithmetic–geometric mean inequality give
\[
\begin{aligned}
\rho(T(x))&\ge\frac{u^\mathsf TT(x)u}{u^\mathsf Tu}
=\frac{\sum_{i=1}^{n-1}x_i u_i u_{i+1}}{n-1}\\
&\ge\left(\prod_{i=1}^{n-1}x_i u_i u_{i+1}\right)^{1/(n-1)}
\ge 2(4K)^{-1/[2(n-1)]}.
\end{aligned}
\]
Both inequalities have rigid equality cases. Equality in the arithmetic–geometric mean requires all edge terms \(x_i u_i u_{i+1}\) to coincide; hence, with \(q=(4K)^{-1/[2(n-1)]}\),
\[
x_1=x_{n-1}=\sqrt2\,q,\qquad x_2=\cdots=x_{n-2}=q.
\]
Equality in the final product bound requires \(p_n/p_1=K\). For exactly these weights, direct multiplication shows \(T(x)u=2qu\); Perron–Frobenius implies \(\rho(T(x))=2q\). Conversely, no other positive edge vector can realize equality; all the metric ratios are fixed.

**3. Feasibility, unique optimizer, and the cutoff.** Normalize \(p_1=1\). Reconstructing \(P\) from the forced adjacent ratios produces
\[
p_i=\frac1{2q^{2(i-1)}}\quad(2\le i\le n-1),
\qquad p_n=\frac1{4q^{2(n-1)}}=K.
\]
The internal ratios \(p_{i+1}/p_i=q^{-2}>1\). The first and last ratios are \(p_2/p_1=p_n/p_{n-1}=(2q^2)^{-1}\). Consequently all entries lie in \([1,K]\), as required for condition number \(K\), **precisely when** \(q\le1/\sqrt2\), equivalently \(K\ge2^{n-3}\). At equality the first and last ratios are one; above it they exceed one. For smaller \(K\) the forced endpoint ratios are less than one, making \(p_1\) not a minimum or \(p_n\) not a maximum and violating \(\kappa(P)\le K\). After normalizing \(\min p_i=1\), the feasible set is a compact subset of \([1,K]^n\) and \(\mu_P(G)\) is continuous. Therefore the unattainable lower bound is **strictly** below the true minimum when \(1\le K<2^{n-3}\). In the feasible range, the equality conditions determine every entry up to an overall scalar; this proves sharpness and uniqueness.

**4. Exact all-time contractivity frontier.** For a finite matrix and induced Hilbert norm,
\[
\|e^{tG}\|_P\le1\quad\text{for every }t\ge0
\quad\Longleftrightarrow\quad \mu_P(G)\le0.
\]
The forward implication follows by differentiating \(\|e^{tG}v\|_P^2\) at \(t=0^+\) for all vectors \(v\); the reverse follows by dissipativity of the Hermitian part and the energy derivative. Let \(c/a\ge\sqrt2\) and write
\[
K_{\mathrm{contr}}=\frac14(c/a)^{2(n-1)}\ge2^{n-3}.
\]
At this budget, \(q=a/c\) and the optimal metric has \(\mu_{P_*}(G)=0\). At any smaller budget \(K\), the universal bound gives \(\mu_P(G)\ge-a+c(4K)^{-1/[2(n-1)]}>0\) for every diagonal \(P\), which excludes all-time contractivity. At the threshold, the explicit optimal metric gives contractivity, proving necessity and sufficiency.

**5. A five-stage exact boundary.** For \(G=-I_5+2N_5\), the formula yields \(K_{\mathrm{contr}}=64\), \(q=1/2\) and \(P=\operatorname{diag}(1,2,8,32,64)\). Its symmetric weighted generator has top eigenvalue zero and positive Perron vector \((1,\sqrt2,\sqrt2,\sqrt2,1)^\mathsf T\). The preceding argument rules out every smaller diagonal budget.

## Verification
The standard-library script `verify.py` reconstructs the proposed metrics in dimensions \(5,6,7,8,11\), checks the exact edge profiles and boundary example, and compares computed Perron eigenvalues against the closed form and against deterministic feasible random metrics. Its expected output is `CASCADE_DIAGONAL_METRIC_DIAGNOSTIC_OK 3288`. These finite checks establish numerical consistency only: the all-dimension theorem and equality rigidity follow from the explicit Rayleigh, arithmetic–geometric-mean and Perron proof above. The script requires only Python 3.

## Relationship to prior work
Perelmuter (2026, arXiv:2611.15455, primary MSC 47D06) distinguishes semigroup boundedness from contractivity in the context of complex-time continuation; that distinction motivates asking for a **sharp real-time contractivity metric**, without implying its diagonal budget. Mehrmann and Reis (2026, arXiv:2611.05063) discuss dissipative Hamiltonian representations and Lyapunov methods, giving qualitative context, not a sharp Jordan-chain diagonal condition-number optimum.

An earlier published four-stage calculation, *Sharp metric-conditioning phase transition for a four-stage positive cascade* (12 October 2026), proves the exact complete four-dimensional budget tradeoff, including a large-budget branch consistent with the specialization \(n=4\) of the present expression. **That four-stage result is credited and is not claimed as new.** The present theorem concerns **all chain lengths \(n\ge5\)**, proves a universal path-edge lower bound with its sharp all-dimensional feasibility threshold, identifies the unique general-dimensional metric, and gives a dimension-dependent exact exponential conditioning law. None of these all-length conclusions follows by substituting a parameter into the stated four-stage theorem.

Standard Perron–Frobenius theory, logarithmic-norm contractivity, and the arithmetic–geometric-mean inequality are established tools. General positive-system diagonal stability, upper-triangular contractive matrix characterizations, and graph Perron-root bounds have different objectives or hypotheses. The paper by Renard (2025, arXiv:2506.15444) studies spectral-norm contractions with prescribed triangular diagonals and superdiagonals; its fully inspected Theorem 1.1 and proof address a distinct fixed-entry, discrete contraction problem rather than this all-time, fixed-condition-budget semigroup metric formula. Targeted literature and published-record comparisons revealed no implication-equivalent all-length statement. This is not a claim that a search proves novelty.

## Limitations
The lower-budget optimum for \(K<2^{n-3}\) is **not** computed; only its strict separation from the displayed universal lower bound is proved. The least-budget contractivity formula requires \(c/a\ge\sqrt2\). No claim is made for nondiagonal metrics, uneven coupling, heterogeneous decay rates, stochastic switching, or external disturbances. A contractive weighted norm controls the semigroup in that norm, not the exact peak of its Euclidean transient; the conversion \(\|e^{tG}\|_2\le\sqrt{\kappa(P)}\) need not be sharp.

The derivation uses simple classical inequalities, and some general spectral-radius or diagonal-scaling literature could contain this fact in an equivalent form; the bibliographic originality assessment remains qualified pending wider independent scrutiny. In particular, the full text of every potentially relevant older scaling article was not accessible. No independent mathematical audit has been performed.

## References
1. M. A. Perelmuter, *Semigroups with periodic complex-time boundedness and holomorphy regions*, arXiv:2611.15455v1, first posted 11 November 2026, https://arxiv.org/abs/2611.15455.
2. V. Mehrmann and T. Reis, *Dissipative Hamiltonian representations of linear evolution equations*, arXiv:2611.05063v1, first posted 3 November 2026, https://arxiv.org/abs/2611.05063.
3. *Sharp metric-conditioning phase transition for a four-stage positive cascade*, published 12 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-sharp-metric-conditioning-phase-transition-for-a-four-stage-posi--2d808ba1bdde.
4. A. Renard, *Contractive upper triangular matrices with prescribed diagonals and superdiagonals*, arXiv:2506.15444, first posted 18 June 2025, https://arxiv.org/abs/2506.15444.
5. O. Mason and R. Shorten, *On the simultaneous diagonal stability of a pair of positive linear systems*, Linear Algebra and its Applications 413 (2006), 13–23, DOI 10.1016/j.laa.2005.07.019.
