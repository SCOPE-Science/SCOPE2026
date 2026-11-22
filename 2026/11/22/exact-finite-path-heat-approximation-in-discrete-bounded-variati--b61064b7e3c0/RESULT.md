# Exact finite-path heat approximation in discrete bounded variation, with central-cut rigidity

## Finding

Let \(N\ge2\), let \(L_N\) be the combinatorial Laplacian of the unit-edge path on vertices \(1,\ldots,N\), and set \(H_t=e^{-tL_N}\). For \(f\in\mathbb R^N\), set \(\operatorname{TV}(f)=\sum_{i=1}^{N-1}|f_{i+1}-f_i|\). For every \(t>0\), the exact best approximation coefficient is
\[
\begin{aligned}
C_N(t)&=\sup_{\operatorname{TV}(f)>0}\frac{\|H_tf-f\|_{\ell^1}}{\operatorname{TV}(f)}\\
&=\frac4N\sum_{r=1}^{N-1}\frac{1-e^{-4t\sin^2(\pi r/(2N))}}{4\sin^2(\pi r/(2N))}\sin^2\!\left(\frac{\pi r\lfloor N/2\rfloor}{N}\right).
\end{aligned}
\]
The only maximizing signals, modulo additive constants and multiplication by nonzero real scalars, are unit steps \(f_i=\mathbf1_{\{i>k\}}\) at the central edge indices \(k\in\{\lfloor N/2\rfloor,\lceil N/2\rceil\}\cap\{1,\ldots,N-1\}\). For even \(N\) there is one such edge and for odd \(N\) there are two. The coefficient is strictly increasing and strictly concave in \(t>0\), with
\[
C_N(0)=0,\qquad C_N'(0)=2,\qquad
\lim_{t\to\infty}C_N(t)=\frac{2\lfloor N/2\rfloor\lceil N/2\rceil}{N}.
\]
For each fixed \(\tau>0\), its diffusive continuum limit is
\[
\lim_{N\to\infty}\frac{C_N(N^2\tau)}{N}
=\frac4{\pi^2}\sum_{j=0}^{\infty}\frac{1-e^{-(2j+1)^2\pi^2\tau}}{(2j+1)^2}.
\]
The finite-length, time-dependent sharp coefficient and the complete single-edge equality classification constitute the finding; the continuum series and the equilibrium coefficient are included as comparisons, not independent novelty claims.

## Assumptions and scope

The path has \(N\) distinct sites, unit conductance on each of the \(N-1\) edges, and counting measure in \(\ell^1\). The generator is the symmetric nearest-neighbor Laplacian, with diagonals \((1,2,\ldots,2,1)\) and off-diagonals \(-1\), with the obvious \(2\)-site interpretation. Thus \(H_t\) is strictly positive, symmetric and stochastic for every \(t>0\). No additional boundary variations are included in \(\operatorname{TV}\). Scalars are real. The supremum is over all nonconstant vectors and is attained at each finite positive time.

## Proof

**1. Decomposition into jumps and the cut error.** For \(k\in\{1,\ldots,N-1\}\), let \(u^{(k)}_i=\mathbf1_{\{i>k\}}\). Every vector has the exact decomposition \(f=f_1\mathbf1+\sum_{k=1}^{N-1}(f_{k+1}-f_k)u^{(k)}\). Since \(H_t\mathbf1=\mathbf1\), the triangle inequality yields
\[
\|H_tf-f\|_1\le\sum_k|f_{k+1}-f_k|\,\|H_tu^{(k)}-u^{(k)}\|_1.
\]
For \(i\le k\), \((H_tu^{(k)}-u^{(k)})_i>0\), and for \(i>k\) it is negative, because the kernel is strictly positive. Symmetric stochasticity therefore gives
\[
E_k(t):=\|H_tu^{(k)}-u^{(k)}\|_1
=2\sum_{i\le k<j}H_t(i,j).
\]
Consequently \(C_N(t)=\max_{1\le k<N}E_k(t)\) with single steps always attaining the maximal coefficient.

**2. The edge heat-kernel identity.** Let \(D\) be the forward difference matrix, \((Df)_k=f_{k+1}-f_k\). Then \(L_N=D^\top D\), and \(B_N=DD^\top\) is the Dirichlet tridiagonal Laplacian with diagonal \(2\) and off-diagonal \(-1\), acting on edges \(1,\ldots,N-1\). The intertwining identity
\[
D H_t=e^{-tB_N}D
\]
follows from the power series. Differentiating the flux across edge \(k\), using the path Laplacian and telescoping its rows, gives
\[
\frac12 E_k'(t)
= (H_tu^{(k)})_{k+1}-(H_tu^{(k)})_k
= (e^{-tB_N})_{kk}.
\]
In particular \(E_k(0)=0\) and \(E_k(t)=2\int_0^t(e^{-sB_N})_{kk}\,ds\). Diagonalizing \(B_N\) with orthonormal eigenvectors \(\sqrt{2/N}\sin(\pi rk/N)\) and eigenvalues \(\lambda_r=4\sin^2(\pi r/(2N))\), \(1\le r<N\), proves
\[
E_k(t)=\frac4N\sum_{r=1}^{N-1}\frac{1-e^{-\lambda_rt}}{\lambda_r}\sin^2\left(\frac{\pi rk}{N}\right).
\]

**3. Strict central-edge localization.** Let \(h_t(a)\) be the heat kernel of the nearest-neighbor walk on the cycle of length \(2N\), started at vertex zero. The odd-reflection image identity for the Dirichlet interval gives
\[
(e^{-tB_N})_{kk}=h_t(0)-h_t(2k).
\]
This is also immediate by comparing the cycle eigenfunction expansion with the displayed Dirichlet spectrum. The cycle heat kernel is symmetric, \(h_t(a)=h_t(2N-a)\), and strictly decreases as \(a\) runs from \(0\) to \(N\) for every \(t>0\). To prove strictness without assuming unimodality, set \(d_a(t)=h_t(a)-h_t(a+1)\) for \(0\le a<N\). The vector \(d(t)\) solves a cooperative tridiagonal linear system: its interior equations are \(d'_a=d_{a-1}-2d_a+d_{a+1}\), its boundary equations are \(d'_0=-3d_0+d_1\) and \(d'_{N-1}=d_{N-2}-3d_{N-1}\), and \(d(0)=(1,0,\ldots,0)\). Its irreducible Metzler matrix has a strictly positive exponential at every positive time, proving \(d_a(t)>0\). (For \(N=2\), the two boundary equations directly give the same conclusion.) As the cycle distance of \(2k\) from zero is \(2\min(k,N-k)\), the edge diagonal, and hence its time integral, increases strictly up to the middle and decreases symmetrically afterward. This proves exactly the claimed central maximizing indices.

**4. Complete equality classification.** The inequality in step 1 can be an equality only if every active jump index maximizes \(E_k\), and the triangle inequality is an equality at every output coordinate. If two distinct indices \(k<\ell\) have nonzero jump coefficients with the same sign, then their error vectors have opposite signs at any site \(k<i\le\ell\); if their coefficients have opposite signs, their errors have opposite signs at any site \(i\le k\). All such entries are nonzero for \(t>0\). Thus two nonzero jumps always cause strict triangle loss. Exactly one central jump is therefore necessary and sufficient.

**5. Time behavior and continuum scaling.** The expression \(C_N(t)=2\int_0^t(e^{-sB_N})_{kk}\,ds\) at a central index shows \(C_N'>0\) and \(C_N''<0\), since the diagonal spectral expansion has strictly positive coefficients at the first eigenmode and no zero eigenvalue. Its derivative at zero is two. Letting \(t\to\infty\) in the spectral formula, or using mass mixing in the cut formula, yields \(2k(N-k)/N\) at any edge, hence the central equilibrium limit.

For the diffusive limit divide the spectral formula by \(N\), put \(t=N^2\tau\) and \(k=\lfloor N/2\rfloor\), and view the finite sum as a sequence indexed by \(r\ge1\) with zero terms for \(r\ge N\). For each fixed \(r\), \(N^2\lambda_r\to\pi^2r^2\) and \(\sin^2(\pi rk/N)\to\mathbf1_{\{r\text{ odd}\}}\). The estimate \(\sin(\pi r/(2N))\ge r/N\) for \(1\le r<N\) gives the summable domination
\[
0\le\frac4{N^2}\frac{1-e^{-N^2\lambda_r\tau}}{\lambda_r}\sin^2\left(\frac{\pi rk}{N}\right)\le \frac1{r^2}.
\]
Dominated convergence for the series proves the stated limit. No general uniform error rate is asserted.

## Verification

Execute `python check.py` in a Python environment with NumPy and SciPy. The checker independently compares matrix-exponential step errors to the spectral formula on \(2\le N\le31\), checks central-edge maximization across five times, tests arbitrary signed vectors, checks exact integer closed-walk counts for Dirichlet edge heat kernels, and compares diffusive scaling numerically. The last reported line is `ALL_NEW_DISCRETE_REFLECTING_HEAT_CHECKS_PASS`. This is diagnostic finite evidence, not a substitute for the analytical arguments above.

## Relationship to prior work

Dowker (2012) explicitly derives the discrete path Neumann heat kernel and the Dirichlet and periodic kernels by eigenmodes and images. Those formulas imply the starting ingredients, but its result sections and conclusion do not formulate or optimize the exact norm of \(H_t-I\) from adjacent total variation into counting \(\ell^1\), or classify central single-step extremizers. Published work on stationary-barycenter envelopes for Lipschitz Markov heat on weighted paths optimizes \(\|H_t\|_{\mathrm{Lip}\to\mathrm{Lip}}\) over conductances and times, not \(\|H_t-I\|_{\mathrm{TV}\to\ell^1}\) at fixed unit conductance and finite time. Heat-semigroup BV characterizations on manifolds examine short-time limiting integrated oscillations, not this finite-path coefficient. A continuous reflecting-interval analogue shares the midpoint-jump geometry; its continuum coefficient is reproduced here only as a scaling limit, not claimed as new.

## Limitations

Only finite, unweighted, nonperiodic paths with symmetric unit conductances, counting \(\ell^1\), and real adjacent total variation are covered. Unequal edge weights, nonuniform vertex measures, arbitrary graphs, discrete-time approximations, and a quantitative uniform rate in the diffusive limit are not treated. Equivalent but unindexed older results cannot be excluded; the novelty comparison is substantive but not an independent historical-priority certification.

## References

1. J. S. Dowker, *Heat-kernels on the discrete circle and interval*, arXiv:1207.2096 (first publicly posted 2012-07-09), especially sections 7, 8 and 15, https://arxiv.org/abs/1207.2096.
2. P. Alonso Ruiz and F. Baudoin, *Yet another heat semigroup characterization of BV functions on Riemannian manifolds*, arXiv:2010.12131 (2020), https://arxiv.org/abs/2010.12131.
3. *Sharp stationary-barycenter envelope for Lipschitz Markov heat on weighted paths*, published research result (2026-10-27), https://github.com/published-finding corpus/2026/tree/main/2026/10/27/SCOPE-sharp-stationary-barycenter-envelope-for-lipschitz-markov-heat-o--e763059e9aa5.
