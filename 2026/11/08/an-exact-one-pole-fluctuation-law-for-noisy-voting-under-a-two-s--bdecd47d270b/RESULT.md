# An exact one-pole fluctuation law for noisy voting under a two-state environment

## Finding

Consider finite-population noisy voting with two externally switched spontaneous-flip rates. Even though its full stationary distribution can undergo nontrivial changes of shape, its exact finite-population **stationary variance** is a rational function with a single pole in the environment-switching speed. It decreases strictly with that speed whenever herding is present and the two noise intensities differ.

Write \(V_\lambda=\operatorname{Var}_\lambda(i)\), where \(i\) is the number of agents with the first opinion. For every integer \(N\ge2\), all \(a_0,a_1,h,r_0,r_1,\lambda>0\), set
\[
\begin{gathered}
\pi_0=\frac{r_1}{r_0+r_1},\qquad \pi_1=\frac{r_0}{r_0+r_1},\\
 c_\sigma=4a_\sigma+\frac{2h}{N},\qquad
 b_\sigma=N\left(a_\sigma+\frac h2\right),\\
 \bar c=\pi_0c_0+\pi_1c_1,\qquad
 \bar b=\pi_0b_0+\pi_1b_1.
\end{gathered}
\]
Then the unique stationary law satisfies \(\mathbb E[i]=N/2\) and
\[
\boxed{V_\lambda=
\frac{\bar b}{\bar c}+
\frac{8h(N-1)\pi_0\pi_1(a_1-a_0)^2}
{\bar c\left[c_0c_1+\lambda(r_0+r_1)\bar c\right]}.}
\]
For \(a_0\ne a_1\), the map \(\lambda\mapsto V_\lambda\) is strictly decreasing and strictly convex; for \(a_0=a_1\) it is constant. Define \(V_\infty=\bar b/\bar c\), \(V_0=\pi_0b_0/c_0+\pi_1b_1/c_1\), and
\[\lambda_*=\frac{c_0c_1}{(r_0+r_1)\bar c}.\]
Whenever \(a_0\ne a_1\), the exact interpolation law is
\[
\frac{V_\lambda-V_\infty}{V_0-V_\infty}=\frac1{1+\lambda/\lambda_*}.
\]
The limiting symbol \(V_0\) means \(\lambda\downarrow0\), not an assertion of a unique stationary law at exactly \(\lambda=0\).

## Assumptions and scope

There are \(N\ge2\) exchangeable agents with two opinions and continuous-time count \(i\in\{0,\ldots,N\}\). An independent environment \(\sigma\in\{0,1\}\) changes from \(\sigma\) to \(1-\sigma\) at rate \(\lambda r_\sigma\), where \(\lambda,r_0,r_1>0\). Conditional on \(\sigma\), the population transitions are
\[
T^+_{i,\sigma}=(N-i)\left(a_\sigma+\frac{hi}{N}\right),\qquad
T^-_{i,\sigma}=i\left(a_\sigma+\frac{h(N-i)}{N}\right),
\]
with \(a_0,a_1,h>0\). Rates at forbidden boundary jumps are zero. No detailed-balance assertion is made for the joint process; only the finite chain's stationary law is used. The model is mean-field/all-to-all; it is not a theorem for arbitrary contact networks or for a state-dependent environment.

## Proof

**Existence, symmetry.** Positive spontaneous-flip rates make all adjacent count transitions possible, and positive environmental rates allow state switching. The \(2(N+1)\)-state continuous-time Markov chain is irreducible, hence has a unique stationary law. The involution \((i,\sigma)\mapsto(N-i,\sigma)\) preserves all rates. Therefore stationarity is invariant under that involution and \(\mathbb E[i]=N/2\).

**Exact conditional second-moment closure.** Let \(m=i-N/2\) and let \(\mathcal L_\sigma\) denote only the population component of the generator. Directly from the jump rates,
\[
T^+_{i,\sigma}-T^-_{i,\sigma}=-2a_\sigma m,
\qquad
T^+_{i,\sigma}+T^-_{i,\sigma}
=N\left(a_\sigma+\frac h2\right)-\frac{2h}{N}m^2.
\]
Each jump changes \(m^2\) by \(\pm2m+1\); thus
\[
\mathcal L_\sigma(m^2)=2m(T^+_{i,\sigma}-T^-_{i,\sigma})+T^+_{i,\sigma}+T^-_{i,\sigma}
=b_\sigma-c_\sigma m^2.
\]
The environment is autonomous, so its stationary marginal is \(\pi_0=r_1/(r_0+r_1)\) and \(\pi_1=r_0/(r_0+r_1)\). Put \(u_\sigma=\mathbb E[m^2\mathbf1_{\{\text{environment}=\sigma\}}]\). Applying the full stationary generator to \(m^2\mathbf1_{\{\text{environment}=\sigma\}}\) gives the **exact** system
\[
\begin{pmatrix}
c_0+\lambda r_0&-\lambda r_1\\
-\lambda r_0&c_1+\lambda r_1
\end{pmatrix}
\begin{pmatrix}u_0\\u_1\end{pmatrix}
=\begin{pmatrix}\pi_0 b_0\\\pi_1 b_1\end{pmatrix}.
\]
Its determinant is \(\Delta=c_0c_1+\lambda(r_0+r_1)\bar c>0\). Solving and summing yields
\[
V_\lambda=u_0+u_1=
\frac{\pi_0b_0c_1+\pi_1b_1c_0+\lambda(r_0+r_1)\bar b}
{c_0c_1+\lambda(r_0+r_1)\bar c}.
\]
There is no approximation in this calculation.

**Factorization and monotonicity.** Subtracting \(\bar b/\bar c\) produces
\[
V_\lambda-\frac{\bar b}{\bar c}=
\frac{\pi_0\pi_1(c_1-c_0)(b_0c_1-b_1c_0)}
{\bar c\,[c_0c_1+\lambda(r_0+r_1)\bar c]}.
\]
The two factors simplify to
\[
c_1-c_0=4(a_1-a_0),\qquad
b_0c_1-b_1c_0=2h(N-1)(a_1-a_0),
\]
which proves the stated nonnegative excess with strictly positive numerator precisely when \(a_0\ne a_1\) under the assumptions. Writing its positive numerator divided by \(\bar c\) as \(K\), differentiation gives \(V_\lambda'=-K(r_0+r_1)\bar c/\Delta^2<0\) and \(V_\lambda''=2K[(r_0+r_1)\bar c]^2/\Delta^3>0\). Taking both limits and factoring \(\Delta=c_0c_1(1+\lambda/\lambda_*)\) proves the interpolation identity.

**Observable interpretation.** Sample two distinct agents uniformly at stationarity. Conditional on \(i\), their chance of agreeing is
\[
\frac{i(i-1)+(N-i)(N-i-1)}{N(N-1)}.
\]
Averaging and using \(\mathbb E i=N/2\) gives
\[
\Pr_\lambda(\text{the sampled pair agrees})
=\frac{N-2}{2(N-1)}+\frac{2V_\lambda}{N(N-1)},
\]
so this sociologically interpretable pairwise measure decreases with environmental speed under the same strict conditions. The opinion-fraction variance is \(V_\lambda/N^2\).

## Verification

The accompanying self-contained `verify.py` uses Python standard-library rational arithmetic to (i) construct the full exact \(2(N+1)\)-state joint generator, (ii) solve its stationary linear equations independently of the conditional-moment argument, and (iii) compare the exact variance to the formula. It tests \(N=2,\ldots,7\) across five parameter sets including the equal-noise and zero-herding degeneracies, and additionally tests strict monotonicity for \(N=2,\ldots,19\). Running `python verify.py` prints `PASS: 84 exact rational identities / monotonicity inequalities`. These finite checks do **not** establish the universal theorem; the generator calculation above does.

## Relationship to prior work

Caligiuri and Galla [1], Section IV, specify exactly the count jump rates above (their Eq. 22), analyze the limits of slow and fast environmental switching, and simulate the intermediate regime to examine changes between unimodal, bimodal, and trimodal distributions. Their Section IV.4 does not provide an all-finite-size stationary variance law or establish strict monotonicity of stationary pairwise agreement for arbitrary positive, possibly unequal environmental switching rates. The present claim concerns an exactly solvable **second moment**, not the harder problem of explicitly recovering the full distribution or classifying all its modes.

Hufton, Lin, Galla and McKane [2] develop PDMP and linear-noise methods for general switching-environment population processes. Those approximations do not directly yield the stated exact finite-\(N\) voter variance or its strict all-\(\lambda\) law. Herrerías-Azcué and Galla [3] derive stationary distributions of a time-homogeneous multistate noisy voter model, rather than this two-environment Markov-modulated finite-\(N\) observable. Carro, Toral and San Miguel [4] analyze noisy voters on static complex graphs, without environmental switching. Standard second-moment generator methods are known; the contribution is the explicit exact temporal-switching formula and its sharp qualitative implication for this specific model.

## Limitations

The formula does not prove that every functional of the stationary distribution becomes less polarized, does not locate its modes, and does not address absorption times, nonlinear networks or three-or-more environmental states. Equal-noise (and, beyond the strict assumptions, zero-herding) degeneracies have no strict speed effect. All novelty assertions are limited to the literature examined; a differently expressed or unindexed result may exist. No independent external mathematical audit has been performed.

## References

1. A. Caligiuri and T. Galla, *Noisy voter models in switching environments*, arXiv:2305.19096 (first submitted 2023-05-30), https://arxiv.org/html/2305.19096v2 ; *Physical Review E* **108**, 044301 (2023), https://doi.org/10.1103/PhysRevE.108.044301 . Specifically Section IV, Eq. (22), Sections IV.2–IV.4.
2. P. G. Hufton, Y. T. Lin, T. Galla and A. J. McKane, *Intrinsic noise in systems with switching environments*, arXiv:1512.00785, https://arxiv.org/html/1512.00785v2 , especially Sections II–IV.
3. F. Herrerías-Azcué and T. Galla, *Consensus and diversity in multi-state noisy voter models*, arXiv:1903.09198, https://arxiv.org/abs/1903.09198 .
4. A. Carro, R. Toral and M. San Miguel, *The noisy voter model on complex networks*, *Scientific Reports* **6**, 24775 (2016), https://doi.org/10.1038/srep24775 .
