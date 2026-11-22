# Sharp three-dimensional separation between one-step and annealed Kaczmarz sampling

## Finding

Let \(0<c<1\), and solve a consistent, nonsingular real three-equation system by ordinary unit-step randomized Kaczmarz. Its unit row normals are
\[
u_1=(1,0,0),\quad u_2=(c,\sqrt{1-c^2},0),\quad u_3=(0,0,1).
\]
At every step sample independently from one stationary law \(p=(p_1,p_2,p_3)\). Denote by \(F_1(p)\) the worst-unit-initial-error expected squared-error factor after **one** step, and by
\[
\Gamma(p)=\lim_{k\to\infty}\bigl[\sup_{\|e_0\|_2=1}\mathbb E_p\|e_k\|_2^2\bigr]^{1/k}
\]
the exact worst-initialization **annealed** exponential factor. The limit exists.

**The two unique unrestricted optimal laws differ.** The unique minimizer of \(F_1\) and the unique minimizer of \(\Gamma\) are respectively
\[
\boxed{p^{\rm one}=\left(\frac1{3-c},\frac1{3-c},\frac{1-c}{3-c}\right),\quad
\min_p F_1(p)=\frac2{3-c},}
\]
\[
\boxed{p^{\rm ann}=\left(\frac1{3-c^2},\frac1{3-c^2},\frac{1-c^2}{3-c^2}\right),\quad
\min_p\Gamma(p)=\frac2{3-c^2}.}
\]
These minima range over *all* three nonnegative row-selection probabilities, not only those satisfying symmetry. In particular, the exact asymptotic mean-square factor of the one-step-optimized sampler is
\[
\Gamma(p^{\rm one})=\frac2{3-c}>rac2{3-c^2}=\Gamma(p^{\rm ann}).
\]
The multiplicative loss and its sharp maximum are
\[
\boxed{\frac{\Gamma(p^{\rm one})}{\min_p\Gamma(p)}
=\frac{3-c^2}{3-c}\le6-2\sqrt6,}
\]
with equality exactly when \(c=3-\sqrt6\). At \(c=3/5\), the two laws are \((5/12,5/12,1/6)\) and \((25/66,25/66,8/33)\); their exact annealed factors are \(5/6\) and \(25/33\), a ratio of \(11/10\).

This is the smallest *real ambient dimension* in which the optimized worst-direction one-step law can differ from the optimized exact annealed-rate law: the previously established planar coincidence theorem covers arbitrary spanning real two-dimensional row pools (see References). Only the three-dimensional separation and sharp factor above are asserted as new.

## Assumptions and scope

The rows are unit-length and linearly independent; \(0<c<1\) is fixed. The linear system is consistent and noise-free, and the Kaczmarz update is the **unrelaxed** orthogonal projection \(e\mapsto Q_i e\) with \(Q_i=I-u_i u_i^{\mathsf T}\). Every row is sampled independently at each iteration with fixed probabilities \(p_i\ge0\) summing to one. Initial errors are deterministic. The annealed factor optimizes worst-initialization expected squared Euclidean error, not almost-sure/quenched decay, adaptive sampling, or the optimum for a prescribed finite iteration count. The formula is for three rows in \(\mathbb R^3\); the row system is invertible throughout the displayed open range.

## Proof

**1. Conditional one-step rate.** Set \(q=p_3\), \(s=p_1+p_2=1-q\), and \(M=\sum_i p_i u_i u_i^{\mathsf T}\). Orthogonality of each \(Q_i\) gives
\[
F_1(p)=1-\lambda_{\min}(M).
\]
The third coordinate has eigenvalue \(q\). The other two eigenvalues form a plane block with trace \(s\) and determinant \(p_1p_2(1-c^2)\). Its smaller eigenvalue is
\[
\frac{s-\sqrt{(p_1-p_2)^2+4c^2p_1p_2}}2\le\frac{s(1-c)}2.
\]
For \(s>0\), equality holds exactly when \(p_1=p_2=s/2\): the discriminant can be written \(c^2s^2+(1-c^2)(p_1-p_2)^2\). Thus
\[
F_1(p)\ge\max\{1-q,\ 1-(1-q)(1-c)/2\}.
\]
The first function strictly decreases in \(q\), the second strictly increases; they cross only at \(q=(1-c)/(3-c)\). At that point the row-pair equality is necessary, proving the unique global law and its claimed objective.

**2. Exact annealed spectral reduction.** On the real Hilbert space of symmetric \(3\times3\) matrices with the Frobenius inner product, define
\[
\Phi_p(X)=\sum_{i=1}^3p_iQ_iXQ_i.
\]
Independence gives \(\mathbb E[e_ke_k^{\mathsf T}]=\Phi_p^k(e_0e_0^{\mathsf T})\), so the squared-error expectation is its trace. The operator \(\Phi_p\) is self-adjoint and positive semidefinite as a *linear operator*: its quadratic form is \(\sum_i p_i\|Q_iXQ_i\|_F^2\ge0\). The decomposition of symmetric matrices into (i) the symmetric upper \(2\times2\) block, (ii) the two plane-to-third-coordinate cross entries, and (iii) the last diagonal entry is invariant.

On block (iii), the eigenvalue is \(s=1-q\). On block (ii), the operator identifies with \(p_1Q_1^{\rm pl}+p_2Q_2^{\rm pl}\), because \(Q_3\) kills cross entries; its eigenvalues lie in \([0,s]\). On block (i), \(Q_3\) is the identity and \(Q_1^{\rm pl},Q_2^{\rm pl}\) are rank-one projections. The latter two have Frobenius inner product \(c^2\), so the two nonzero eigenvalues of their rank-one superoperator are those of the Gram matrix
\[
\begin{pmatrix}p_1&c^2\sqrt{p_1p_2}\\c^2\sqrt{p_1p_2}&p_2\end{pmatrix}.
\]
Consequently the largest plane-block eigenvalue is
\[
q+\frac{s+\sqrt{(p_1-p_2)^2+4c^4p_1p_2}}2
\ge q+\frac{s(1+c^2)}2,
\]
with equality for \(s>0\) exactly when \(p_1=p_2\). The plane block and last diagonal block together dominate the cross block, hence the spectral radius is exactly the maximum of the plane-block expression and \(1-q\).

This spectral radius equals the stated *worst-initialization annealed exponential factor*. Indeed,
\[
\sup_{\|e_0\|=1}\mathbb E\|e_k\|^2=\lambda_{\max}(\Phi_p^k(I_3)).
\]
Every dominating block has a nonzero positive-semidefinite eigenmatrix: the last-diagonal projector on block (iii), and a nonnegative combination of plane rank-one projectors on block (i). Such an eigenmatrix has strictly positive trace, so \(I_3\) has nonzero projection onto a top eigenspace. Self-adjointness and the nonnegative spectrum imply that the displayed \(k\)-th root converges to \(\rho(\Phi_p)\), including boundary sampling laws.

**3. Global annealed optimization and uniqueness.** Every sampling law obeys
\[
\Gamma(p)\ge\max\{1-q,\ q+(1-q)(1+c^2)/2\}.
\]
Equality holds for \(p_1=p_2=(1-q)/2\). The first affine term strictly decreases and the second strictly increases with \(q\), intersecting uniquely at \(q=(1-c^2)/(3-c^2)\). This gives \(\Gamma_*=2/(3-c^2)\). Any \(q\) different from this raises the lower bound; at its unique optimizing \(q\), any imbalance \(p_1\ne p_2\) strictly raises the plane-block eigenvalue. Therefore the fully unrestricted annealed optimum is unique.

**4. Quantified separation and sharpness.** For \(0<c<1\), \(c^2<c\), hence the annealed-optimal third-row probability strictly exceeds the one-step-optimal one. At the latter probability the block (iii) eigenvalue dominates, so \(\Gamma(p^{\rm one})=1-q=2/(3-c)\). Differentiating the ratio \((3-c^2)/(3-c)\) gives derivative with the sign of \(c^2-6c+3\); its unique critical point in \((0,1)\) is \(c=3-\sqrt6\), which is the strict global maximum. Direct substitution gives \(6-2\sqrt6\). The rational example follows by substitution. Finally, the complete published planar theorem in References proves one-step and annealed minimizers coincide for arbitrary real planar frames; dimension one is immediate, so the present dimension-three example is minimal.

## Verification

Run `python verify.py` with Python 3, NumPy and SymPy. The checker builds the actual normalized row normals, the expected one-step matrix, and the full nine-dimensional Kronecker covariance operator; it checks 8,466 spectral inequalities across six correlations and a grid of all three probabilities, and verifies the exact rational example and sharp maximum. It prints `PASS: 8466 spectral inequalities checked; exact rational examples and maximum checked`. The mathematical assertions for all real \(c\) and all probability laws follow from the proof, not from finite testing.

## Relationship to prior work

Dai, Soltanalian and Pelckmans (2014) formulate optimized one-step Kaczmarz sampling as a smallest-eigenvalue semidefinite problem; the one-step objective and general optimization idea here are prior art. Agaskar, Wang and Lu (2014) formulate the exact annealed mean-square exponent via the lifted operator \(\sum_i p_iQ_i\otimes Q_i\) and optimize it by a general SDP; that lifted formulation, including its computational solvability, is also prior art. Their inspected 2014 paper includes numerical three-dimensional examples but does not state the displayed exact three-row family, the two optimizer laws, or the sharp gap. Needell, Srebro and Ward (2013 preprint) examine nonuniform sampling and convergence bounds, not this exact annealed-versus-one-step gap.

A published planar coincidence result proves equality of the two optimal probability sets for *every* spanning real plane row pool; the present theorem supplies an exact higher-dimensional separation and its smallest-dimensional sharp loss. A separate previously published result already solves **all nonsingular three-row one-step minmax sampling**, so no novelty is attributed to that special-case one-step formula. A published two-cluster Kaczmarz result studies more rows and the one-step criterion, not an exact annealed separation. The significant new mathematical information is precisely the explicit discrepancy between the **two criteria**, its unrestricted uniqueness, and the maximized relative penalty. Known general semidefinite programs can recover numerical values and are not claimed new.

## Limitations

The model has exactly two correlated orthogonal-projection rows and one orthogonal third row. It is not an arbitrary three-dimensional matrix classification. The result concerns iid stationary sampling, worst-initialization annealed MSE asymptotics and one-step mean-square factors, not exact finite-time expected error for every initialization, per-iteration computational costs, or almost-sure exponents. General SDP frameworks can derive these optimized values for individual matrices; the new assertion is their explicit analytic comparison for this natural parametric family, including the sharp loss. Priority against every unindexed paper is not proved and independent mathematical audit has not been performed.

## References

1. D. Needell, N. Srebro and R. Ward, *Stochastic Gradient Descent, Weighted Sampling, and the Randomized Kaczmarz Algorithm*, arXiv:1310.5715v1, first public 2013-10-21. https://arxiv.org/abs/1310.5715
2. L. Dai, M. Soltanalian and K. Pelckmans, *On the Randomized Kaczmarz Algorithm*, arXiv:1402.2863v1, first public 2014-02-12. https://arxiv.org/pdf/1402.2863
3. A. Agaskar, C. Wang and Y. M. Lu, *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities*, GlobalSIP 2014, DOI:10.1109/GlobalSIP.2014.7032145. Author-archived full text: https://dash.harvard.edu/server/api/core/bitstreams/7312037d-8b4a-6bd4-e053-0100007fdf3b/content
4. *Planar coincidence theorem for optimal randomized Kaczmarz sampling*, full text at https://github.com/published-finding corpus/2026/blob/main/2026/10/13/SCOPE-planar-coincidence-theorem-for-optimal-randomized-kaczmarz-sampl--54597ea58934/RESULT.md
5. *A signed-triangle formula for minimax three-row randomized Kaczmarz sampling*, full text at https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-a-signed-triangle-formula-for-minimax-three-row-randomized-kaczm--fc51ccf74dc5/RESULT.md
6. *Three-phase optimal sampling for two-cluster correlated Kaczmarz systems*, full text at https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-three-phase-optimal-sampling-for-two-cluster-correlated-kaczmarz--6e183c9f201f/RESULT.md
