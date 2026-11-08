# Sharp higher-moment control bounds and convex state-clock geometry for finite passage networks

## Finding

Let \(T\) be the first arrival at an absorbing target in a finite, continuous-time Markov jump network, started at a transient state, with absorption almost surely and all permitted transition rates strictly positive. For every integer \(m\geq 1\), set \(U_m=\mathbb E[T^m]>0\). The following conclusions hold without reversibility or detailed balance.

**Sharp one-source control law.** For an edge \(e\), or any nonempty group of edges sharing one source state, multiply all rates in that group by \(t>0\), keeping other rates fixed. Then

\[
-m\leq\frac{\partial\log U_m(t)}{\partial\log t}\leq m.
\]

The universal constant \(m\) is optimal on both sides. Consequently, for every \(c\geq1\),

\[
c^{-m}\leq\frac{U_m(ct)}{U_m(t)}\leq c^m.
\]

If \(k_e\) ranges over all original individual transition-rate parameters, the global control-budget identity is

\[
\sum_e \frac{\partial\log U_m}{\partial\log k_e}=-m.
\]

**Convex state-clock law.** Independently speed up all jumps leaving each transient state \(i\) by \(e^{\theta_i}\). Then \(F_m(\theta)=\log U_m(e^\theta)\) is globally convex on \(\mathbb R^n\). More precisely, there is an explicitly defined finite probability distribution \(\mathsf P_\theta\) on nonnegative integer occupancy-count vectors \(N\) satisfying \(\sum_i N_i=m\), for which

\[
\frac{\partial F_m}{\partial\theta_i}=-\mathbb E_\theta N_i,
\qquad
\frac{\partial^2 F_m}{\partial\theta_i\partial\theta_j}
=\operatorname{Cov}_\theta(N_i,N_j).
\]

Thus each state-clock sensitivity lies in \([-m,0]\), the state-clock sensitivities sum to \(-m\), and their Hessian is positive semidefinite with the all-ones vector in its nullspace.

## Assumptions and scope

Take a finite directed continuous-time Markov chain with a nonempty absorbing target set \(B\) and a finite set of transient states \(S=\{1,\ldots,n\}\). The killed transition generator \(Q\) is the \(S\)-by-\(S\) restriction of the full generator, with off-diagonal entries equal to nonnegative jump rates and diagonal entries equal to minus the total rate of leaving each state, including target-bound transitions. Each permitted jump has a strictly positive finite rate. From every state in \(S\) there is a positive-rate directed path to \(B\); equivalently the finite killed chain is transient and its first hitting time is almost surely finite. Multiple absorbing states, different edge channels, and directed cycles are allowed; self-transitions are not treated as jumps. The starting state \(a\) belongs to \(S\). The moment order \(m\) is an arbitrary fixed positive integer.

One-source controls can comprise one transition or several transitions with the same source, including a jump into \(B\). Rates are multiplied by a common positive factor, so the permitted-edge graph never changes. For state-clock controls every outgoing transition from transient state \(i\), including absorbing jumps, receives factor \(e^{\theta_i}\).

## Proof

**1. Moment representation and positivity.** Let \(M=-Q\), \(G=M^{-1}\), and \(\mathbf 1\) be the all-ones column. Since the killed chain is transient, \(G=\int_0^\infty e^{Qt}\,dt\) exists entrywise and is nonnegative; \(M\) is a nonsingular \(M\)-matrix with \(\det M>0\). Integration of the survival function (or backward moment equations) gives, for every integer \(m\geq1\),

\[
U_m=m!\,e_a^\mathsf T G^m\mathbf1.
\]

The value is strictly positive and finite, since the initial holding time is positive almost surely and finite transience gives an exponential tail. This identity does not rely on reversibility.

**2. Positive-affine inverse lemma.** Fix a nonempty group of edges having source \(u\) and multiply their rates by \(t>0\). Only row \(u\) of \(M(t)\) changes, and that row is affine in \(t\). By determinant multilinearity, \(\det M(t)=c+dt\). Because \(M(t)\) is a nonsingular \(M\)-matrix for *every* \(t>0\), its determinant is positive throughout the positive half-line. Letting \(t\downarrow0\) and \(t\to\infty\) shows \(c,d\geq0\). Similarly Cramer's rule implies that every inverse entry has the form

\[
G_{ij}(t)=\frac{a_{ij}+b_{ij}t}{c+dt}.
\]

For every \(t>0\), \(G_{ij}(t)\geq0\); hence the affine cofactor numerator \(a_{ij}+b_{ij}t\) is nonnegative for every positive \(t\), and therefore \(a_{ij},b_{ij}\geq0\). If both numerator coefficients vanish, that entry is identically zero and can be omitted from subsequent products. For each positive entry,

\[
\frac{d\log G_{ij}(t)}{d\log t}
=\frac{b_{ij}t}{a_{ij}+b_{ij}t}-\frac{dt}{c+dt}\in[-1,1],
\]

because each fraction lies in \([0,1]\). This is the key lemma: arbitrary cycles do not spoil the one-source bound because a common-source perturbation changes just one matrix row.

**3. Moment control bound and finite changes.** Expand \(e_a^\mathsf T G(t)^m\mathbf1\) as the finite sum over \(i_1,\ldots,i_m\in S\) of nonnegative products

\[
\prod_{q=1}^m G_{i_{q-1},i_q}(t),\qquad i_0=a.
\]

Each positive product has logarithmic derivative in \([-m,m]\) by Step 2. The logarithmic derivative of their positive sum is a convex combination of these derivatives, so it also lies in \([-m,m]\). Integrate over \(\log t\) to obtain the two finite-change bounds. If every original jump rate is multiplied by a common factor \(c\), the complete sample path is a deterministic time change \(T\mapsto T/c\). Therefore \(U_m\mapsto c^{-m}U_m\), and differentiating at \(c=1\) proves the sum over **individual** original edge-rate elasticities equals \(-m\).

**4. Sharpness at both endpoints.** For the single-step chain \(A\xrightarrow{t}B\), \(T\) is exponential with mean \(1/t\), so \(U_m=m!t^{-m}\) and the lower elasticity is exactly \(-m\). For the chain \(A\xrightarrow{a}B\), \(A\xrightarrow{t}C\), \(C\xrightarrow{b}A\), with \(a,b>0\), start at \(A\) and absorb at \(B\). Its transient inverse is

\[
G(t)=\frac1{ab}\begin{pmatrix}b&t\\b&a+t\end{pmatrix}.
\]

As \(t\to\infty\), \(G(t)/t\) converges to \((ab)^{-1}\begin{pmatrix}0&1\\0&1\end{pmatrix}\), an idempotent rank-one matrix; hence \(U_m(t)\sim m!t^m/(ab)^m\). The positive-side logarithmic elasticity tends to \(+m\). No smaller architecture-independent absolute bound is possible.

**5. Joint state-clock geometry.** Write \(M_0\) for the uncontrolled matrix and \(W=M_0^{-1}\). Under state-clock factors \(e^{\theta_i}\),

\[
M(\theta)=\operatorname{diag}(e^{\theta_i})M_0,
\qquad
G(\theta)=W\operatorname{diag}(e^{-\theta_i}).
\]

Expanding Step 1 gives

\[
\frac{U_m(\theta)}{m!}
=\sum_{(i_1,\ldots,i_m)\in S^m}
\left[\prod_{q=1}^m W_{i_{q-1},i_q}\right]
\exp\left(-\sum_{q=1}^m\theta_{i_q}\right),\qquad i_0=a.
\]

Every bracketed coefficient is nonnegative and their total is positive. Normalize the summands to a probability law \(\mathsf P_\theta\) on index sequences, and let \(N_i\) count the number of occurrences of state \(i\) among \(i_1,\ldots,i_m\). Differentiation of this finite positive exponential sum yields the displayed gradient and covariance Hessian. Convexity follows, while \(\sum_iN_i=m\) gives the sum rule and Hessian null direction. This completes the proof.

## Verification

`verify_moment_controls.py` independently evaluates killed-generator matrix powers and derivative formulas with NumPy, compares local derivatives against centered finite differences, tests finite-change bounds, checks the explicit state-clock coefficient distribution and covariance Hessian, and verifies the two-state sharpness mechanism symbolically with SymPy. Run `python verify_moment_controls.py` with the versions indicated in `requirements.txt`. The script reports 6 exact moment-order sharpness checks, 864 local derivative tests, 864 finite-change tests, 576 state-clock Hessian tests, on 144 generated networks. These finite experiments corroborate algebraic identities and detect implementation errors; the universal claims follow from Steps 1–5 rather than from the sampling.

## Relationship to prior work

Liang and Bao (2026) prove the \([-1,1]\) edge bound and \(-1\) sum identity for **mean** first-passage time and analyze grouped kinetic controls. Their paper explicitly identifies whether the local bound extends to **higher moments** as an unresolved question in its Discussion. This theorem answers that precise question for all integer raw moments with a sharp order-dependent constant, identifies tight positive/negative examples, and adds the joint convex state-clock landscape; it does not claim the already-known mean case as new.

Nam and Gunawardena (2025, 2026) provide general positive rational expressions for first-passage moments through spanning forests and graph operators. Those moment formulas are stronger for **computing** moments on a specified network; they are not themselves the sharp rate-uniform moment control bounds or the covariance Hessian representation stated here. Caswell (2011) derives general perturbation and elasticity formulas for absorbing-chain moments. The present scope is the universal *inequalities and joint convexity*, not the existence of moment derivatives or their matrix calculus formulas. The full Caswell article was not available for detailed comparison; see limitations. The elementary generator and inverse identities employed in the proof are standard.

## Limitations

The bounds require a finite time-homogeneous Markov jump model, positive-rate graph-preserving perturbations, certain absorption, an integer **raw** moment, and **one common source** for an arbitrary scaled edge group. They do not claim the same \(m\)-bound for arbitrary multi-source groups, general semi-Markov waiting times, first-passage quantiles, variance or normalized shape statistics, or networks with positive nonabsorption probability. Positive convexity is asserted for **state-clock logarithmic coordinates**, not for arbitrary edge-rate coordinates. The positive sharpness constant is reached as a parameter limit, not necessarily at finite rates. Earlier generalized sensitivity theory, notably Caswell (2011), introduces a residual publication-priority risk because its complete article text could not be examined. Independent expert review and independent audit have not been performed.

## References

1. Shiling Liang and Ruicheng Bao, *A Universal Control Budget for First-Passage Kinetics*, arXiv:2608.06368, first posted 2026-08-06. https://arxiv.org/abs/2608.06368
2. Kee-Myoung Nam and Jeremy Gunawardena, *Algebraic formulas for first-passage times of Markov processes in the linear framework*, *Bulletin of Mathematical Biology* 87, 161 (2025). https://doi.org/10.1007/s11538-025-01524-z
3. Kee-Myoung Nam and Jeremy Gunawardena, *Algebraic formulas for first-passage times of Markov processes in the linear framework: generalising the work of Hill and Kac*, arXiv:2608.08375 (2026). https://arxiv.org/abs/2608.08375
4. Hal Caswell, *Perturbation analysis of continuous-time absorbing Markov chains*, *Numerical Linear Algebra with Applications* 18, 901–917 (2011). https://doi.org/10.1002/nla.791
