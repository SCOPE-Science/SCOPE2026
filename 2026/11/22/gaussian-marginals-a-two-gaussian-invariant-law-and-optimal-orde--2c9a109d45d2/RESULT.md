# The exact stationary cost of updating the noisier coordinate last

## Finding

For \(0<c<1\), minimize \(f(x)=\tfrac12(x_1^2+x_2^2+2cx_1x_2)\). At each call use a unit coordinate step with fresh independent centered Gaussian oracle noise, of variance \(u>0\) for coordinate 1 and \(v>0\) for coordinate 2. Thus an update replaces \(x_i\) by \(-cx_{3-i}-\xi_i\). In each epoch use exactly two updates, one per coordinate, choosing order \(12\) with probability \(p\in[0,1]\) and \(21\) otherwise, independently of the past and of all oracle noise. Compare the expected objective at stationarity, measured after the two updates in an epoch. Then
\[
L(p)=\frac{u+v+2c^2\big((1-p)u+pv\big)}{2(1+c^2)}.
\]
If \(u\ne v\), the unique optimum among these order probabilities puts the noisier coordinate first every epoch. Its exact improvement over any \(p\) is
\[
L(p)-\min_{q\in[0,1]}L(q)
=\frac{c^2|u-v|}{1+c^2}\Pr_p(\text{the noisier coordinate is updated last}).
\]
In particular a uniformly sampled order pays half the penalty of the worse fixed order. If \(u=v\) every \(p\) has the same risk. The order effect comes from dependence between the coordinates, not their individual variances.

## Proof

Write \(H=\begin{pmatrix}1&c\\c&1\end{pmatrix}\) and \(\|h\|_H^2=h^{\mathsf T}Hh\). Drive two trajectories with the same noise and order. Their difference evolves as \((-ch_2,c^2h_2)\) for order \(12\), or \((c^2h_1,-ch_1)\) for order \(21\). The squared \(H\)-norm values are \(c^2(1-c^2)h_2^2\) and \(c^2(1-c^2)h_1^2\), respectively. They are bounded by \(c^2\|h\|_H^2\), by completing the square. The epoch transition is therefore a strict contraction in quadratic Wasserstein distance for this norm. It preserves finite second moments and has a unique invariant probability law in that space, reached from each independent initial law of finite second moment. In fact no other invariant probability laws exist: synchronous coupling reduces the distance of any two finite-valued initial states by \(c^k\) after \(k\) epochs, and bounded Lipschitz test functions and dominated convergence then show that any two invariant laws agree.

Put
\[
a=\frac{u+c^2v}{1-c^4},\qquad d=\frac{v+c^2u}{1-c^4}.
\]
These are the positive solutions to \(a=c^2d+u\), \(d=c^2a+v\). Starting with coordinate second moments \(a,d\), each single coordinate update keeps both second moments fixed: for the updated coordinate use independence and centering of fresh noise, and the other coordinate does not change. In particular every epoch preserves the two second moments, regardless of order. Starting from, for example, independent centered Gaussians of these variances and using convergence in quadratic Wasserstein distance shows that the stationary second moments are \(a,d\).

For order \(12\), complete the square at the last coordinate:
\[
f(X')=\tfrac12(1-c^2)(X'_1)^2+\tfrac12(X'_2+cX'_1)^2
=\tfrac12(1-c^2)(X'_1)^2+\tfrac12\xi_2^2.
\]
The order is independent of the incoming state, so the conditional expected cost is \(L_{12}=((1-c^2)a+v)/2\). Similarly \(L_{21}=((1-c^2)d+u)/2\). As \(a-d=(u-v)/(1+c^2)\), the difference \(L_{21}-L_{12}=c^2(u-v)/(1+c^2)\) has the sign of \(u-v\). Averaging these conditional costs over the order gives the exact expression and all equality cases.

## Relation to earlier work

These updates are also bivariate Gaussian conditional replacement kernels. When \(u\ne v\) the two replacements are incompatible: the conditional log densities have mixed derivatives \(-c/u\) and \(-c/v\), whereas those derivatives must agree for corresponding positive joint conditionals. Different fixed-scan laws with the same marginals and mixtures of such laws are established ideas in incompatible Gibbs sampling [1–3], not originality claims here. In this model the fixed-scan output laws are determined by the shared Gaussian marginals and the last replacement. A single-site random scan choosing coordinate 1 with probability \(1-p\) has the same stationary mixture as these full epochs: the replacement at 1 gives the fixed-scan law with 1 last, and the replacement at 2 gives the other. Thus changing the schedule need not give a new family of distributions. The result here instead evaluates the loss for the specified stochastic optimization problem: the last update contributes its noise variance directly to the completed square, but the first contributes through the smaller weighted marginal term. This leads to the exact heteroscedastic ordering criterion and regret under the stated epoch-boundary quadratic objective.

Noiseless coordinate-descent permutation rates [4] and finite-epoch finite-sum shuffling rates [5] optimize or bound different quantities. The closer stationary ordering result [6] has a scalar noninterpolating finite-sum recursion with deterministic component gradients, not this independent noisy coordinate oracle. The full text of [1] was not available for comparison; precise historical priority is not certified.

## Verification and scope

For \(c=1/2,u=9,v=4\), the fixed variances are \((a,d)=(32/3,20/3)\); the completed-square formula gives \(L_{12}=6\), \(L_{21}=7\) and \(L(1/2)=6.5\). The frozen companion `verify.py` (Python, NumPy, SymPy) also contains symbolic objective and derivative checks and a seeded simulation at another parameter setting. Finite arithmetic and simulation do not establish the all-parameter theorem. The result concerns independent order choices, fresh Gaussian oracle noise, and this two-dimensional unit-diagonal quadratic at epoch boundaries. It is not a statement about adaptive ordering, transient iteration counts or general dimension.

## References

1. S.-H. Chen and E. H. Ip, *Behaviour of the Gibbs sampler when conditional distributions are potentially incompatible*, Journal of Statistical Computation and Simulation 85 (2015), 3266–3275, https://doi.org/10.1080/00949655.2014.968159.
2. S.-H. Chen, E. H. Ip and Y. J. Wang, *Gibbs Ensembles for Nearly Compatible and Incompatible Conditional Models*, Computational Statistics & Data Analysis 55 (2011), 1760–1769, https://doi.org/10.1016/j.csda.2010.11.006, §5.
3. K.-L. Kuo and Y. J. Wang, *The Gibbs Sampler Revisited from the Perspective of Conditional Modeling*, arXiv:2410.09559, §2.3, https://arxiv.org/abs/2410.09559.
4. M. Gürbüzbalaban, A. Ozdaglar, N. D. Vanli and S. J. Wright, *Randomness and Permutations in Coordinate Descent Methods*, arXiv:1803.08200, https://arxiv.org/abs/1803.08200.
5. I. Safran and O. Shamir, *Random Shuffling Beats SGD Only After Many Epochs on Ill-Conditioned Problems*, arXiv:2106.06880, https://arxiv.org/abs/2106.06880.
6. *Sharp randomized-to-deterministic ordering transition for two-component quadratic reshuffling*, public research note, https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-sharp-randomized-to-deterministic-ordering-transition-for-two-co--0dcf8057d8e5.
