# Sharp three-state threshold and threefold noise inflation for stochastic rounding of scalar contractions

## Finding

Fix a real target \(u\in(0,1)\). Define unbiased integer stochastic rounding \(\mathcal R\) by rounding \(y\) to \(\lfloor y\rfloor\) and \(\lceil y\rceil\) with respective probabilities \(1-\{y\}\) and \(\{y\}\); an integer is returned unchanged. All rounding draws are conditionally independent. Consider the one-rounding-per-iteration process, from any deterministic \(X_0\in\mathbb Z\),
\[
 X_{n+1}=\mathcal R\bigl(u+a(X_n-u)\bigr),\qquad -\tfrac12\le a<1.
\]
For every such \(a,u\), the process has exactly one stationary law and its distribution converges to that law from every integer start. Its mean at finite time is \(\mathbb E X_n=u+a^n(X_0-u)\).

When \(0\le a<1\), the stationary law is Bernoulli on \(\{0,1\}\), with masses \(1-u,u\) and variance \(u(1-u)\). When \(-\tfrac12\le a<0\), set \(r=-a\), \(t=\min(u,1-u)\), and \(b=(1+r)t\). For \(t\ge r/(1+r)\), the same Bernoulli law is stationary. For \(0<t<r/(1+r)\), it instead has exactly three occupied integer states. If \(u=t\le\tfrac12\), they are \(-1,0,1\), with
\[
 p_1=\frac{t}{1-r+b},\qquad p_{-1}=(r-b)p_1,\qquad p_0=1-p_1-p_{-1}.
\]
If \(u>\tfrac12\), the masses are reflected by sending the integer \(j\) to \(1-j\), so the states are \(0,1,2\). In either case the stationary variance is
\[
 V_r(u)=u(1-u)+\frac{2t\,[r-(1+r)t]}{1-r+(1+r)t}\quad\text{if }t<\frac r{1+r},
\]
with \(V_r(u)=u(1-u)\) otherwise. Consequently,
\[
 1\le\frac{V_r(u)}{u(1-u)}<3.
\]
The bound \(3\) is the sharp unattained supremum over \(0<r\le\tfrac12\) and \(0<u<1\), approached as \(r=\tfrac12\) and \(u\downarrow0\). For each fixed \(r>0\), the ratio falls strictly from \((1+r)/(1-r)\) to \(1\) as \(t\) increases from zero to \(r/(1+r)\).

## Assumptions and scope

The real affine argument is evaluated exactly, and **only the final result** is stochastically rounded to the unit integer lattice. The model does not include other finite-precision errors. Conditional rounding draws are independent at successive iterations and have the specified distance-proportional probabilities. The multiplier interval corresponds to gradient descent on the scalar quadratic \(f(x)=\tfrac{\lambda}{2}(x-u)^2\), with \(a=1-\eta\lambda\): the three-state phenomenon occurs for overshooting but deterministically stable stepsizes \(1<\eta\lambda\le\tfrac32\). The starting state is any deterministic integer, not restricted to the finite recurrent class.

## Proof

**Unbiasedness and the mean.** For every real \(y\), \(\mathbb E[\mathcal R(y)]=y\). Iterated expectations give \(\mathbb E[X_{n+1}-u]=a\,\mathbb E[X_n-u]\), which proves the finite-time mean formula.

**Positive multipliers.** If \(0\le a<1\), the set \(\{0,1\}\) is invariant, since both affine images are strictly inside \((0,1)\). From an integer above \(1\), every step is nonincreasing, and at each fixed integer above \(1\) there is a strictly positive probability of moving lower; the analogous statement holds below \(0\). Thus the chain reaches \(\{0,1\}\) in finite time almost surely. It is irreducible and aperiodic there, with positive self-loop probabilities. Its stationary mean must be \(u\), hence the stationary masses on \(\{0,1\}\) are \(1-u,u\).

**A finite trapping set for negative multipliers.** Write \(a=-r\), where \(0<r\le1/2\). Since \(|\mathcal R(y)-y|<1\) except when it is zero, every sample path satisfies
\[
 |X_n-u|\le r^n|X_0-u|+\frac{1-r^n}{1-r}.
\]
For any \(0<\delta<\min(u,1-u)\), the right side is eventually below \(2+\delta\). The only integers in that interval about \(u\) belong to \(S=\{-1,0,1,2\}\). Direct substitution into \(u-r(x-u)\) shows \(S\) is invariant for \(r\le1/2\). Therefore the chain reaches \(S\) deterministically after a finite index and never leaves it.

**Classes and exact probabilities.** The dynamics are invariant under reflection \((u,X)\mapsto(1-u,1-X)\), so assume \(0<u\le1/2\). Put \(b=(1+r)u\). If \(b\ge r\), the images of \(0,1\) are respectively \(b\in(0,1)\), \(b-r\in[0,1)\); hence \(\{0,1\}\) is the sole closed irreducible class. Indeed, from \(-1\) and \(2\) there are positive-probability paths into it, so these other states are transient. Its unique stationary law is Bernoulli with mean \(u\). If \(b<r\), the class \(\{-1,0,1\}\) is closed, irreducible and aperiodic (state \(0\) has a self-loop); state \(2\) is transient. In this case the transition \(1\to-1\) has probability \(r-b\). Stationary mass balance at \(-1\) gives \(p_{-1}=(r-b)p_1\). Stationary mean balance gives \(u=p_1-p_{-1}=p_1(1-r+b)\), whence the displayed three masses. The zero self-loop and connectivity imply convergence in law from every start. For \(u>1/2\), apply reflection.

**Variance and sharpness.** In the three-point class, \(\mathbb E[X^2]=p_1+p_{-1}\), so \(\operatorname{Var}(X)-u(1-u)=\mathbb E[X^2]-u=2u(r-b)/(1-r+b)\). Reflection preserves variance. For any integer-valued variable of mean \(u\in(0,1)\), the pointwise inequality \(j(j-1)\ge0\) gives \(\operatorname{Var}(X)\ge u(1-u)\), with equality exactly on \(\{0,1\}\). In the extra-variance regime, writing \(R(t)=V_r(u)/[u(1-u)]\), direct differentiation yields
\[
 R(t)=1+\frac{2[r-(1+r)t]}{(1-t)[1-r+(1+r)t]},\qquad
 R'(t)=-\frac{2\{[\,(1+r)t-r\,]^2+1\}}{(1-t)^2[1-r+(1+r)t]^2}<0.
\]
Thus \(1<R(t)<(1+r)/(1-r)\le3\). The limit as \(t\downarrow0\) is \((1+r)/(1-r)\), which increases to \(3\) at \(r=1/2\), proving the sharp strict bound.

## Verification

Run `python3 verify.py` with Python 3 and no third-party packages. The exact-rational verifier constructs the finite transition kernel for \(75\) parameter pairs, checks positivity, stationarity, support, normalization, means, variances, the trapping-set transitions, reachability and the sharp-constant approach, and reports \(911\) passed rational assertions. In the example \(r=2/5\), \(u=1/10\), it checks \((p_{-1},p_0,p_1)=(13/370,307/370,5/37)\), variance \(593/3700\), and inflation ratio \(593/333\). The finite tests do not establish the all-parameter theorem: that follows from the analytic classification and inequality above.

## Relationship to prior work

Li et al. (2017), Theorem 5 and its proof in Section 5 and Appendix F, analyze the small-learning-rate limit of quantized neural-network training with noisy stochastic-gradient laws; their assumptions include positive gradient-noise mass in both directions. They do not give the exact oscillatory fixed-slope, deterministic-gradient chain classified here. Connolly, Higham and Mary (2020/2021) establish mean-independent stochastic-rounding errors and probabilistic backward-error analysis rather than stationary laws for gradient iterations. Croci et al. (2022) survey implementation and stochastic-rounding error analysis. Xia, Massei and Hochstenbach (2025) analyze gradient-descent rounding errors under a Polyak–Łojasiewicz condition, with descent-oriented small-step hypotheses not covering the present overshooting range. A published result on **deterministic floor-quantized** negative-slope affine contractions concerns orbit basins and two-cycles, not the unbiased stochastic transition probabilities or stationary variance studied here. The three-state calculations are elementary once the correct trapping set is identified, so unindexed equivalent Markov-chain results remain a genuine originality risk.

## Limitations

The theorem is for one-dimensional exact affine arithmetic followed by a single independent unbiased integer rounding operation. It does not imply corresponding limits for rounded gradients, multiple rounding sites, arbitrary floating-point grids, nonlinear targets, higher dimensions, or overshoot multipliers less than \(-1/2\). The sharp constant is a supremum, not an attained example. The finite rational tests sample parameter values; they cannot replace the global proof. No independent scientific audit has been performed.

## References

- H. Li, S. De, Z. Xu, C. Studer, H. Samet, and T. Goldstein, *Training Quantized Nets: A Deeper Understanding*, arXiv:1706.02379 (initial public posting June 7, 2017), Section 5, Theorem 5 and Appendix F. https://arxiv.org/abs/1706.02379
- M. P. Connolly, N. J. Higham, and T. Mary, *Stochastic Rounding and Its Probabilistic Backward Error Analysis*, initial preprint April 28, 2020; SIAM Journal on Scientific Computing 43 (2021), A566–A585. https://doi.org/10.1137/20M1334796 ; preprint https://eprints.maths.manchester.ac.uk/2763/
- M. Croci, M. Fasi, N. J. Higham, T. Mary, and M. Mikaitis, *Stochastic rounding: implementation, error analysis and applications*, Royal Society Open Science 9 (2022), 211631. https://doi.org/10.1098/rsos.211631
- L. Xia, S. Massei, and M. E. Hochstenbach, *On the convergence of the gradient descent method with stochastic fixed-point rounding errors under the Polyak–Łojasiewicz inequality*, Computational Optimization and Applications (2025). https://doi.org/10.1007/s10589-025-00656-1
