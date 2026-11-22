# A sharp cost–coherence allocation law for two-coordinate quadratic descent

## Finding

Let \(H\in\mathbb R^{2\times2}\) be symmetric positive definite, and consider exact randomized single-coordinate minimization of the quadratic \(f(x)=\tfrac12(x-x_\star)^\top H(x-x_\star)\). Updating coordinate \(i\) has fixed positive work price \(c_i\). Draw coordinate 1 with probability \(p\in[0,1]\), and coordinate 2 otherwise. Put
\[
 \rho=\frac{|H_{12}|}{\sqrt{H_{11}H_{22}}}\in[0,1),\qquad
 C(p)=pc_1+(1-p)c_2.
\]
For one update, define the **sharp worst-initialization fractional expected objective decrease per expected update work**
\[
 \mathcal R(p)=\frac1{C(p)}\inf_{x\ne x_\star}
 \frac{f(x)-\mathbb E_p f(x^+)}{f(x)}.
\]
Then \(\mathcal R\) has exactly one maximizer on the closed probability interval, given by
\[
 \boxed{p_\star=\frac{\sqrt{c_1c_2}+\rho c_2}{2\sqrt{c_1c_2}+\rho(c_1+c_2)},\qquad
 \max_p\mathcal R(p)=\frac{1-\rho^2}{c_1+c_2+2\rho\sqrt{c_1c_2}}.}
\]
Both coordinates are sampled with positive probability. Equal work prices or zero coupling each force \(p_\star=1/2\); otherwise the expensive coordinate receives strictly less than half the probability. As coupling increases to one from below, the optimal probability tends to \(\sqrt{c_2}/(\sqrt{c_1}+\sqrt{c_2})\), the inverse-square-root-cost allocation.

The sharp improvement of this cost-aware rule over the equal-probability rule is
\[
 \boxed{\frac{\mathcal R(p_\star)}{\mathcal R(1/2)}
 =\frac{(1+\rho)(c_1+c_2)}{c_1+c_2+2\rho\sqrt{c_1c_2}}.}
\]
It exceeds one if and only if \(\rho>0\) and \(c_1\ne c_2\), is always strictly below two, and has sharp supremum two over positive prices and positive-definite two-dimensional Hessians. For example, with \(H=\begin{psmallmatrix}1&3/5\\3/5&1\end{psmallmatrix}\) and \((c_1,c_2)=(9,1)\), the unique optimum is \(p_\star=3/10\), the per-work decrement is \(4/85\), and equal sampling gives \(1/25\); the exact improvement factor is \(20/17\).

## Assumptions and scope

The Hessian \(H\) is real, symmetric, positive definite and fixed. Each update exactly minimizes the quadratic along the selected coordinate, with no relaxation, additive gradient noise, or variable pricing. Coordinate choices are independent of the current iterate, but only the next update is optimized; no long-horizon or wall-clock rate optimality is claimed. Work prices \(c_1,c_2>0\) are externally specified units, not inferred from the Hessian. The normalization \(\mathcal R\) is a **ratio of an exact worst-direction expected objective decrement to the expected work of one update**, not the expectation of a random work-normalized decrement. The two-point probability simplex includes endpoints.

## Proof

**1. Exact projectors.** Write \(z=H^{1/2}(x-x_\star)\) and \(u_i=H^{1/2}e_i/\sqrt{H_{ii}}\). Since \(\|u_i\|_2=1\), exact minimization in coordinate \(i\) takes \(z\) to \((I-u_i u_i^\top)z\). Thus the expected fraction of objective removed, conditional on a nonzero \(z\), is
\[
 \frac{z^\top[p u_1u_1^\top+(1-p)u_2u_2^\top]z}{\|z\|_2^2},
\]
and its infimum over \(z\) equals the smallest eigenvalue of \(M(p)=p u_1u_1^\top+(1-p)u_2u_2^\top\). The Gram determinant is \(1-\rho^2>0\). In particular, no endpoint law can be optimal because its smallest eigenvalue is zero, whereas interior laws have a strictly positive one.

**2. Cost-normalized design variables.** Set \(q_1=p/C(p)\) and \(q_2=(1-p)/C(p)\); then \(q_i\ge0\), \(c_1q_1+c_2q_2=1\), and the map between \(p\) and such \(q\) is bijective. Homogeneity of the smallest eigenvalue yields
\[
 \mathcal R(p)=\lambda_{\min}(q_1u_1u_1^\top+q_2u_2u_2^\top).
\]
Changing the sign of \(u_2\) if needed, assume \(u_1^\top u_2=\rho\ge0\), without changing the projectors. Define
\[
 D=c_1+c_2+2\rho\sqrt{c_1c_2},\quad
 g=\frac{1-\rho^2}{D}.
\]
There is a unique unit vector \(w\in\mathbb R^2\) with
\[
 w^\top u_1=\sqrt{c_1g},\qquad
 w^\top u_2=-\sqrt{c_2g}.
\]
Indeed, taking the basis \(u_1=(1,0)^\top\) and \(u_2=(\rho,\sqrt{1-\rho^2})^\top\), this vector is
\[
 w=\sqrt{g}\left(\sqrt{c_1},
 -\frac{\sqrt{c_2}+\rho\sqrt{c_1}}{\sqrt{1-\rho^2}}\right)^\top,
\]
whose squared norm is \(gD/(1-\rho^2)=1\). Consequently, for **every** admissible \(q\),
\[
 w^\top(q_1u_1u_1^\top+q_2u_2u_2^\top)w
 =g(c_1q_1+c_2q_2)=g,
\]
so \(\mathcal R(p)\le g\). This fixed rank-one direction is a global upper-bound certificate independent of the sampling probability.

**3. Attainment.** Define
\[
 q_1^\star=\frac{1+\rho\sqrt{c_2/c_1}}D,
 \qquad q_2^\star=\frac{1+\rho\sqrt{c_1/c_2}}D.
\]
They are positive and \(c_1q_1^\star+c_2q_2^\star=1\). The equations
\[
 q_1^\star-\rho\sqrt{c_2/c_1}\,q_2^\star=g,
 \qquad q_2^\star-\rho\sqrt{c_1/c_2}\,q_1^\star=g
\]
show directly, by expanding in the independent basis \((u_1,u_2)\), that the corresponding matrix sends \(w\) to \(gw\). Its other eigenvalue is at least \(g\), because
\[
 q_1^\star+q_2^\star-2g
 =\frac{\rho\bigl(\sqrt{c_2/c_1}+\sqrt{c_1/c_2}+2\rho\bigr)}D\ge0.
\]
Therefore the smallest eigenvalue is exactly \(g\). Converting back using \(p=q_1/(q_1+q_2)\) gives the stated \(p_\star\).

**4. Uniqueness.** If any \(q\) attained \(g\), the fixed unit vector \(w\), whose Rayleigh quotient always equals \(g\), would be a smallest-eigenvalue eigenvector. The resulting coefficients of \(u_1\) and \(u_2\) in \(Mw=gw\) give exactly the two linear equations in Step 3. Their determinant is \(1-\rho^2>0\), hence their solution is uniquely \(q^\star\), even when \(\rho=0\). Thus the probability is unique on the entire simplex.

**5. Monotonicity and sharp gain.** The optimal probability may be written as \(p_\star=(k+\rho c_2)/(2k+\rho(c_1+c_2))\) where \(k=\sqrt{c_1c_2}\). Its derivative with respect to \(\rho\) is \(k(c_2-c_1)/(2k+\rho(c_1+c_2))^2\), giving the monotone interpolation and equality cases. Uniform sampling has \(\lambda_{\min}(M(1/2))=(1-\rho)/2\) and work \((c_1+c_2)/2\), proving the displayed gain. By the arithmetic-geometric mean inequality, the gain is above one precisely under the conditions stated and is less than \(1+\rho<2\). Taking \(\rho\uparrow1\) and \(c_1/c_2\to\infty\) proves that two is the sharp supremum. All claims hold for the full parameter domain, not merely for the rational test instances.

## Verification

The standalone Python program `verify.py` requires only Python 3's standard library. It verifies the exact cost-normalized eigenvalue and the rank-one dual certificate on rational Pythagorean-direction instances, including the stated \(20/17\) example; independently checks a dense numerical grid of sampling probabilities and the cost-imbalance limit; and reports its completed test count. Run `python3 verify.py` from the directory containing this file. Finite tests are supplementary: the global theorem and uniqueness are established analytically in the proof.

## Relationship to prior work

Rodomanov and Kropotov (first public 2019-04-09, arXiv:1904.04587) analyze volume-sampled randomized coordinate descent; for single-coordinate updates their sampling weights are proportional to coordinate Lipschitz constants. The present result instead optimizes an exact worst-direction expected decrease normalized by **priced per-coordinate work** and derives a sharp closed form even when the classical Lipschitz weights are equal. Csiba and Richtárik (2018, *Coordinate Descent Faceoff*) optimize an established separable **complexity upper bound** multiplied by expected iteration cost; their importance-sampling optimum does not imply the optimum of the exact two-dimensional spectral quotient here. These are different objective functions, not contradictory theorems.

The published *Planar coincidence theorem for optimal randomized Kaczmarz sampling* (2026) characterizes one-step and annealed sampling for unpriced planar rows; it yields equal probabilities in the two-independent-direction case but does not optimize a price-weighted quotient. The published *Sharp work-budget phase transition between one-step and asymptotic randomized two-row Kaczmarz* (2026) uses equal singleton costs, permits full-batch and no-op masks, and fixes a work budget; neither its feasible set nor its objective subsumes the unequal-priced, one-coordinate-only rule proved here. Generic E-optimal-design methods are also relevant to the underlying eigenvalue maximization, but the particular closed-form cost/coherence law and sharp twofold equal-sampling gap were not found in the inspected accessible primary results. Elfving (1952) describes optimal allocation for two-parameter regression and mentions heterogeneous observation costs; its full text could not be examined, so no determination of noncoverage or priority is made for that plausible source.

## Limitations

The claim does not address nonquadratic objectives, more than two coordinates, time-varying or data-dependent work costs, adaptive probabilities, numerical conditioning, estimator bias, long-run annealed exponents, physical clock time, or total iteration complexity to a tolerance. It optimizes a precisely specified single-step worst-direction progress-per-expected-cost metric; a larger value of this metric by itself is not a proof of faster wall-clock convergence in a particular implementation. Standard results about two-point E-optimal design may imply this formula in an unlocated specialized source, so independent novelty verification remains needed.

## References

1. A. Rodomanov and D. Kropotov, *A Randomized Coordinate Descent Method with Volume Sampling*, arXiv:1904.04587v1 (2019-04-09), https://arxiv.org/abs/1904.04587 .
2. D. Csiba and P. Richtárik, *Coordinate Descent Faceoff: Primal or Dual?*, Proceedings of ALT 2018, https://research.cs.cornell.edu/conferences/alt2018/A/csiba18.pdf .
3. *Planar coincidence theorem for optimal randomized Kaczmarz sampling*, published-finding corpus public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-planar-coincidence-theorem-for-optimal-randomized-kaczmarz-sampl--54597ea58934 .
4. *Sharp work-budget phase transition between one-step and asymptotic randomized two-row Kaczmarz*, published-finding corpus public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-work-budget-phase-transition-between-one-step-and-asymptot--10323bbfb631 .
5. W. L. Martinez and E. J. Wegman, *An alternative criterion useful for finding exact E-optimal designs*, Statistics & Probability Letters 47 (2000), DOI:10.1016/S0167-7152(99)00173-X, https://doi.org/10.1016/S0167-7152(99)00173-X .
6. G. Elfving, *Optimum Allocation in Linear Regression Theory*, Annals of Mathematical Statistics 23 (1952), 255–262, DOI:10.1214/aoms/1177729442, https://doi.org/10.1214/aoms/1177729442 .
