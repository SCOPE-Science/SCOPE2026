# Universal cyclic-erasure designs for periodic Green-kernel quadrature

## Finding

Fix an integer \(n\ge2\), \(\kappa>0\), and \(s>0\). On the unit circle \(\mathbb T=\mathbb R/\mathbb Z\), let \(X\) be a centered real Gaussian field with periodic Green covariance
\[
 C(x,y)=s\sum_{m\in\mathbb Z}e^{-\kappa|x-y+m|}
 =s\frac{e^{-\kappa d}+e^{-\kappa(1-d)}}{1-e^{-\kappa}},
 \quad d=(x-y)\bmod1\in[0,1).
\]
For distinct nonadaptive sampling sites in cyclic order, write \(g_i>0\) for their successive cyclic gaps, with \(\sum_{i=0}^{n-1}g_i=1\). A randomly delivered subset \(S\) of the prescribed sites is known to the estimator and independent of \(X\). Assume **only** that the law of its index set is invariant under cyclic shifts; failures may be arbitrarily dependent. The target is the full-circle integral \(J=\int_0^1X(t)\,dt\), and the loss is the expected conditional variance of \(J\), equivalently the unconditional mean-squared error of its Gaussian conditional-mean estimator.

Set
\[
 f(\ell)=\frac{2s}{\kappa^2}\left[\kappa\ell-2\tanh\left(\frac{\kappa\ell}{2}\right)\right],\quad
 q_k=\Pr(0\in S,\ k\in S,\ 1,\ldots,k-1\notin S),\quad 1\le k<n,
\]
and \(p_j=\Pr(|S|=j)\) for \(j=0,1\). Then the **exact** expected posterior integral variance is
\[
 \boxed{R(g)=p_0\frac{2s}{\kappa}+p_1f(1)+\sum_{k=1}^{n-1}q_k
 \sum_{i=0}^{n-1}f\!\left(\sum_{j=0}^{k-1}g_{(i+j)\bmod n}\right).}
\]
Every equally spaced design \(g_i=1/n\) globally minimizes this risk, regardless of the dependence structure. Let \(K=\{k\in\{1,\ldots,n-1\}:q_k>0\}\) and define \(d=\gcd(n,K)\), with \(d=n\) if \(K\) is empty. **All** minimizers are exactly the positive gap vectors satisfying
\[
 \boxed{g_{i+d}=g_i\quad\text{for all indices modulo }n.}
\]
Consequently, equally spaced sites are the unique minimizers up to rotating the circle **if and only if** \(d=1\). In particular, a law delivering precisely the even or precisely the odd sites on a four-site circle, each with probability one half, admits the entire nonuniform optimal family \((a,\frac12-a,a,\frac12-a)\) for \(0<a<1/2\).

For independent deliveries of probability \(p\in(0,1)\), the uniform gaps are uniquely optimal and the minimum is
\[
 \boxed{R_n^*(p)=(1-p)^n\frac{2s}{\kappa}+np(1-p)^{n-1}f(1)
 +np^2\sum_{k=1}^{n-1}(1-p)^{k-1}f(k/n).}
\]
For \(p=1\), the minimum is \(n f(1/n)\). With \(p\in(0,1]\) and \(\kappa,s\) fixed, the sharp asymptotic loss of independent erasures is
\[
 \boxed{\lim_{n\to\infty}\frac{R_n^*(p)}{n f(1/n)}=1+\frac{6(1-p)}{p^2}.}
\]
Thus the same uniform design is optimal at every reliability, but the leading posterior integral variance is inflated by exactly a factor of \(13\) at delivery probability \(p=1/2\).

## Assumptions and scope

The unit circle has circumference one; integration uses normalized arc length. The kernel scale \(s\) is **not** called the marginal variance: \(C(x,x)=s\coth(\kappa/2)\). Both \(s\) and \(\kappa\) are fixed positive constants. Each successful site is observed without noise and at its original location. There are no sequential replacements after a failure. Erasure status is known, the delivery law is independent of the field and invariant under a one-step cyclic permutation of site labels, and sites are distinct with strictly positive cyclic gaps. Independence between deliveries is required only for the explicit Bernoulli formula and asymptotic factor. No estimator is required to be unbiased for deterministic integrands: the claimed risk is Gaussian Bayes risk under the displayed prior.

## Proof

**1. The kernel and the exact bridge cost.** The periodized exponential is positive definite because its circle Fourier coefficient at integer frequency \(m\) is \(2s\kappa/[\kappa^2+(2\pi m)^2]>0\). Its covariance operator is the inverse of
\[
 L=\frac{-\partial_t^2+\kappa^2}{2\kappa s}
\]
on periodic functions. This follows directly from the distributional identity \(( -\partial_t^2+\kappa^2)e^{-\kappa|t|}=2\kappa\delta_0\), summed over integer translates. The prior integral variance is \(\langle1,L^{-1}1\rangle=2s/\kappa\).

Condition on field values at a nonempty finite set of sites. The Gaussian Cameron–Martin quadratic energy is \(\langle u,Lu\rangle\); after fixing the endpoint values, residual functions vanish at every observed site. Their energy form splits as the direct sum of Dirichlet forms on the arcs between consecutive surviving sites. Thus their conditional covariance, and therefore the integral residual variance, is a sum over these arcs. For an arc of length \(\ell>0\), the function
\[
 u_\ell(t)=\frac{2s}{\kappa}\left[1-\frac{\cosh(\kappa(t-\ell/2))}{\cosh(\kappa\ell/2)}\right],\quad 0\le t\le\ell,
\]
is the unique Dirichlet solution to \(Lu_\ell=1\). Hence its contribution to the conditional variance of the integrated field is \(\int_0^\ell u_\ell(t)\,dt=f(\ell)\). The argument works when exactly one site survives: its two sides are the ends of the same length-one Dirichlet arc, so the conditional variance equals \(f(1)\). With no surviving site it is the prior value \(2s/\kappa\).

As an independent check of the normalization, the conditional mean between two successive surviving values is the hyperbolic interpolation
\[
 \mathbb E[X(t)\mid X(0),X(\ell)]
 =\frac{\sinh(\kappa(\ell-t))}{\sinh(\kappa\ell)}X(0)
 +\frac{\sinh(\kappa t)}{\sinh(\kappa\ell)}X(\ell),
\]
so a surviving site flanked by surviving-arc lengths \(a,b\) receives the strictly positive integral-estimation weight \([\tanh(\kappa a/2)+\tanh(\kappa b/2)]/\kappa\). These are posterior weights, not an assertion of exactness for arbitrary deterministic functions.

**2. Enumerating surviving arcs.** If at least two sites survive, every oriented arc between consecutive surviving sites has a uniquely determined starting index \(i\) and a length covering precisely \(k\) original gaps, for some \(1\le k<n\). This occurs exactly on the event that sites \(i\) and \(i+k\) survive and the intervening indices do not, with no restriction on other indices. Rotation invariance makes its probability \(q_k\), independent of \(i\). Linearity of expectation counts every such arc exactly once, yielding the displayed exact formula for \(R(g)\), including the separate empty- and singleton-survival terms.

**3. Convexity and the full optimizer face.** For \(\ell>0\), direct differentiation gives
\[
 f'(\ell)=\frac{2s}{\kappa}\tanh^2(\kappa\ell/2),\qquad
 f''(\ell)=2s\tanh(\kappa\ell/2)\operatorname{sech}^2(\kappa\ell/2)>0.
\]
Fix \(k\). Define the cyclic \(k\)-gap lengths \(L_i^{(k)}=\sum_{j=0}^{k-1}g_{(i+j)\bmod n}\). Each original gap appears exactly \(k\) times, so \(\frac1n\sum_iL_i^{(k)}=k/n\). Strict Jensen gives
\[
 \sum_i f(L_i^{(k)})\ge n f(k/n),
\]
with equality precisely when all \(L_i^{(k)}\) are equal. Since
\(L_{i+1}^{(k)}-L_i^{(k)}=g_{i+k}-g_i\), this is equivalent to \(g_{i+k}=g_i\) for every \(i\). All \(q_k\) are nonnegative. Hence \(R\) is minimized exactly when this periodicity relation holds for every \(k\in K\). The subgroup generated by \(K\) in \(\mathbb Z/n\mathbb Z\) is the subgroup generated by \(d=\gcd(n,K)\); simultaneous invariance is therefore equivalent to \(g_{i+d}=g_i\). Strict convexity rules out every other positive gap vector. The uniform vector always meets the relations. If \(d=1\), the gap sum forces \(g_i=1/n\). If \(d>1\), nonuniform positive periodic vectors with sum one exist; when \(K\) is empty every positive gap vector is optimal. This proves both necessity and sufficiency for uniqueness.

For the stated four-site correlated-erasure example, only the two-step arc event has positive probability, so \(K=\{2\}\) and \(d=2\). The displayed nonuniform family is exactly its full set of minimizing gaps. Rotational invariance of the erasure law is material: for a deterministic nonsymmetric delivery of only sites \(0\) and \(2\) on three candidate sites, the optimum requires those two locations to be antipodal, whereas uniform three-site spacing fails this condition.

**4. Bernoulli formula and its sharp limit.** Under independent Bernoulli successes of probability \(0<p<1\), the probabilities are
\[
 p_0=(1-p)^n,\quad p_1=np(1-p)^{n-1},\quad q_k=p^2(1-p)^{k-1}.
\]
In particular \(q_1=p^2>0\), so the uniform gap vector is uniquely minimizing. Substitution in Step 2 at that vector gives the finite formula. When \(p=1\), all sites survive and the risk is \(nf(1/n)\).

The expansion \(f(\ell)=s\kappa\ell^3/6+O_{s,\kappa}(\ell^5)\) holds at zero. For fixed \(p\in(0,1)\), the empty- and singleton-success terms decay exponentially in \(n\). Moreover \(f(k/n)\le C_{s,\kappa}(k/n)^3\) for \(1\le k<n\). Dominated convergence with the geometrically weighted cubic summands gives
\[
 \lim_{n\to\infty}n^2R_n^*(p)=\frac{s\kappa}{6}\,
 p^2\sum_{k=1}^{\infty}k^3(1-p)^{k-1}
 =\frac{s\kappa}{6}\frac{p^2-6p+6}{p^2}.
\]
The elementary cubic geometric-series identity used here is
\(\sum_{k\ge1}k^3q^{k-1}=(1+4q+q^2)/(1-q)^4\) for \(0\le q<1\). Since \(n^2\,[nf(1/n)]\to s\kappa/6\), division yields the claimed sharp factor. The same formula has value one at \(p=1\), handled directly. No limit allows the reliability \(p\) or range \(\kappa\) to vary with \(n\).

## Verification

The companion `verify_circular_ou.py` independently constructs finite covariance matrices from the periodized kernel, computes conditional integral variances by a Schur complement, and compares them with the Dirichlet-bridge gap decomposition. It separately checks the posterior integral weights, enumerates all Bernoulli observation patterns against the exact \(q_k\) expansion, tests random nonuniform designs against uniform ones, and verifies the nonuniform four-site optimizer family. Running `python verify_circular_ou.py` with Python 3 and NumPy executes 687 independently parameterized verification cases, with the printed success line documenting completion. The verifier checks finite examples only; the general statements depend on the exact Green-kernel decomposition, strict Jensen equality conditions, and the dominated-convergence argument.

## Relationship to prior work

Pronzato and Zhigljavsky (2018) provide the general Bayesian quadrature / kernel-energy viewpoint and discuss the nonperiodic exponential covariance on an interval; their general variational framework does not state the circular erasure-risk formula, the gcd classification, or the Bernoulli loss factor. Sikolya and Baran (2018) study a complex Ornstein–Uhlenbeck process and optimize integrated *pointwise prediction error* or observation entropy on an interval, different objectives from the variance of a single integrated circular field. Huang and Li (2022) derive the circular Matérn Green covariance and its Markov precision structure; those identities underlie Step 1, and are not claimed as new. The public note *Exact optimal nodes and stratification penalty for Ornstein–Uhlenbeck Bayesian quadrature* studies noiseless observations on a nonperiodic interval and establishes unequal terminal margins and a random-stratification penalty; its theorem does not imply the cyclic correlated-erasure optimizer face or this independent-erasure coefficient. The current theorem is a specialization of standard Gaussian-Markov conditioning and convexity tools, not a claim to discover those general tools.

## Limitations

The covariance must be the specified periodic order-one Green kernel, with a known mean and range. All successful observations are exact, and erasures are independent of field values. The broad optimality assertion requires cyclic invariance of the label-erasure distribution, not merely equal marginal survival probabilities. The gap classification assumes a positive-gap design; coincident or adaptively relocated sites are excluded. The asymptotic efficiency factor assumes a fixed positive per-site success probability. The result concerns posterior **integral** risk, not prediction of the whole sample path or field parameter estimation. A complete historical-priority review cannot be guaranteed, especially for older circular Gaussian-Markov sampling literature; the result has not undergone independent mathematical audit.

## References

1. K. Sikolya and S. Baran, *On the optimal designs for the prediction of complex Ornstein–Uhlenbeck processes*, arXiv:1808.03444v1, first public 2018-08-10, https://arxiv.org/abs/1808.03444.
2. L. Pronzato and A. Zhigljavsky, *Bayesian quadrature and energy minimization for space-filling design*, arXiv:1808.10722v1, first public 2018-08-31, https://arxiv.org/html/1808.10722v1.
3. C. Huang and A. Li, *The Circular Matérn Covariance Function and its Link to Markov Random Fields on the Circle*, arXiv:2201.12856v1, first public 2022-01-30, https://arxiv.org/html/2201.12856v1.
4. *Exact optimal nodes and stratification penalty for Ornstein–Uhlenbeck Bayesian quadrature*, publicly available mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-optimal-nodes-and-stratification-penalty-for-ornstein-uhle--971795799fba.
