# Sharp outermost coverage covariance for all sequentially deposited \(k\)-mers

## Finding

In one-dimensional random sequential covering (RSC) by length-\(k\) intervals, \(k\ge3\), let \(C_x(t)\) be the number of **accepted** intervals covering lattice site \(x\) by time \(t\), where each interval start has its own independent unit-rate Poisson attempt clock. The stationary-in-space field \((C_x(t))_{x\in\mathbb Z}\) is \(3(k-1)\)-dependent. This range is sharp at every \(t>0\): its covariance at the last possibly dependent separation, \(d=3k-3\), is **strictly positive** and is explicitly
\[
\operatorname{Cov}(C_0(t),C_{3k-3}(t))
=2\left[\frac{J_k(t)-J_{k+1}(t)}{k(k-1)}
-\frac{J_{2k-1}(t)-J_{2k}(t)}{k-1}
+\frac{J_{2k}(t)-J_{2k+1}(t)}{k}\right]
-\left[J_k(t)-J_{k+1}(t)\right]^2>0,
\]
where \(J_a(t)=(1-e^{-at})/a\). For every \(d\ge3k-2\), the variables \(C_0(t)\) and \(C_d(t)\) are independent, not merely uncorrelated.

At complete coverage (\(t=\infty\)), the last nonzero spatial covariance has the rational expression
\[
\boxed{\operatorname{Cov}(C_0(\infty),C_{3k-3}(\infty))
=\frac{5k+2}{k^2(k+1)^2(2k-1)(2k+1)}
=\frac{5}{4k^5}+O(k^{-6}).}
\]
For example the values for trimers and tetramers are \(17/5040\) and \(11/12600\). Thus the span of dependence grows linearly with interval length, but the correlation at its outermost edge decays as the fifth power of that length.

## Assumptions and scope

The substrate is the initially empty infinite integer lattice. An interval beginning at \(i\in\mathbb Z\) covers exactly \(\{i,\ldots,i+k-1\}\). At each \(i\) an independent, homogeneous, unit-rate Poisson process proposes deposits. A proposal is accepted if and only if at least one of its \(k\) sites is not yet covered; otherwise it is discarded. Previously covered sites remain covered permanently, but may be covered again by accepted intervals. Accepted intervals contribute one each to multiplicity \(C_x(t)\), which lies in \(\{0,1,\ldots,k\}\). Time is in units of the per-start attempt rate. The statement holds for each integer \(k\ge3\) and each \(t\in(0,\infty]\); the proof also establishes the formulas for \(k=2\), whose complete spatial covariance profile was separately recorded previously.

## Proof

**First-attempt representation.** For each interval start \(j\), write \(U_j\) for its first proposal time. These variables are independent \(\operatorname{Exp}(1)\) clocks. Once a first proposal at \(j\) is rejected, all its sites are covered, so no later proposal at the same start can be accepted. For every site \(x\), the first proposal among the \(k\) intervals covering \(x\) must be accepted, since \(x\) was uncovered. Consequently the indicator that the interval at \(j\) is accepted by time \(t\) is exactly
\[
A_j(t)=\mathbf1\!\left\{U_j\le t,\ \exists x\in\{j,\ldots,j+k-1\}:
U_j=\min_{x-k+1\le h\le x}U_h\right\},
\qquad C_x(t)=\sum_{j=x-k+1}^{x}A_j(t).
\]
All minima are unique almost surely. This identity is not a truncation or an independent-acceptance approximation.

**Finite dependence.** Determining \(A_j(t)\) requires only \(U_{j-k+1},\ldots,U_{j+k-1}\). Therefore \(C_x(t)\) is measurable with respect to the independent clocks
\[
\{U_{x-2k+2},\ldots,U_{x+k-1}\}.
\]
Two sets of site multiplicities separated by at least \(3k-2\) lattice steps use disjoint clock families, hence are independent. In particular, all covariances vanish at those separations.

**The single shared clock at the last separation.** Put \(d=3k-3\). The determining clock windows for \(C_0(t)\) and \(C_d(t)\) intersect in exactly \(U_{k-1}\), and otherwise use disjoint independent clocks. Conditional on \(U_{k-1}=u\), the two site multiplicities are independent. Spatial reflection \(x\mapsto d-x\) maps an interval start \(j\) to \(d-j-k+1\) and fixes the shared start \(k-1\); hence their conditional means coincide. Let this common mean be \(f_t(u)\).

Only the acceptance of the interval starting at \(0\) among the \(k\) intervals covering site \(0\) can depend on \(U_{k-1}\). To determine the dependence, suppose \(U_0=s\le t\). The interval at \(0\) becomes accepted when the shared clock is moved from \(0\) to a value \(u>s\), but would not have been accepted otherwise, **if and only if** the clocks \(U_1,\ldots,U_{k-2}\) are all greater than \(s\), while \(U_{-1}<s\). Indeed, all sites \(0,\ldots,k-2\) are then already covered by time \(s\): the earlier proposal at start \(-1\) either covers them or finds them already covered. The site \(k-1\) is first reached from start \(0\) precisely when the remaining right-hand clocks are later than \(s\). Conversely, if \(U_{-1}>s\), site \(k-2\) already certifies acceptance independently of the shared clock. All other clock values are immaterial for this pivotal event.

Integrating over \(U_0=s\), whose density is \(e^{-s}\), gives
\[
 f_t(u)-f_t(0)=g_k(\min\{u,t\}),\qquad
 g_k(v)=\int_0^v\big(e^{-(k-1)s}-e^{-ks}\big)\,ds
=\frac{1-e^{-(k-1)v}}{k-1}-\frac{1-e^{-kv}}k.
\]
(The value \(f_t(0)\) denotes the continuous conditional-mean extension at the boundary.) By the conditional covariance identity,
\[
\operatorname{Cov}(C_0(t),C_d(t))
=\operatorname{Var}\big[g_k(\min\{U,t\})\big],
\qquad U\sim\operatorname{Exp}(1).
\]
This representation proves strict positivity for every \(t>0\), because \(g_k'(v)=e^{-(k-1)v}(1-e^{-v})>0\) for \(v>0\) and \(\min(U,t)\) is nondegenerate. It also proves that no shorter finite-dependence range is possible.

**Exact covariance and large-length law.** Define \(J_a(t)=(1-e^{-at})/a\). For \(U\sim\operatorname{Exp}(1)\), the fundamental theorem of calculus and Tonelli's theorem give
\[
\mathbb E\,g_k(U\wedge t)=J_k(t)-J_{k+1}(t),
\]
\[
\mathbb E\,g_k(U\wedge t)^2
=2\left[\frac{J_k-J_{k+1}}{k(k-1)}
-\frac{J_{2k-1}-J_{2k}}{k-1}
+\frac{J_{2k}-J_{2k+1}}{k}\right],
\]
where all \(J\) terms in the second formula have argument \(t\). Subtraction of the squared mean yields the displayed finite-time expression. Sending \(t\to\infty\), all \(J_a\to1/a\), and elementary simplification gives
\[
\operatorname{Var}g_k(U)=\frac{5k+2}{k^2(k+1)^2(2k-1)(2k+1)}.
\]
Multiplying by \(k^5\) and taking \(k\to\infty\) gives \(5/4\). These identities prove every asserted time, length and boundary case.

## Verification

The complete standalone file `VERIFY.py` checks the saturated rational identity with independent exact-fraction moment calculations for \(2\le k\le2000\), and separately enumerates all \(24\) and \(5040\) local first-arrival orderings for \(k=2,3\), respectively. Those enumerations reconstruct the conditional expected coverage polynomial directly from the original interval-acceptance rule, confirming the crucial pivotal-clock dependence and the exact variances \(1/45\) and \(17/5040\). Thirty independent exponential-integral quadrature checks compare the all-time formula at six lengths and five times. The program uses Python 3 standard-library modules only:

```text
python3 VERIFY.py
```

The exhaustive finite checks test the specific computations but do not serve as proof for arbitrarily large \(k\) or continuous \(t\); those claims follow from the general first-clock and conditional-independence arguments above.

## Relationship to prior work

Krapivsky, *Random Sequential Covering* (arXiv:2209.03992), introduces the accepted-if-new-coverage process and develops one-site and aggregate observables. Viot and Krapivsky, *Random sequential covering of a one-dimensional lattice by \(k\)-mers* (arXiv:2410.12373, initially public October 16, 2024), solve one-site occupation densities for small \(k\), demonstrate finite closure, and explicitly identify two-point correlations as an interesting separate direction. An earlier exact result for dimer multiplicity already gives a three-step finite covariance profile and its outermost correlation \(1/45\); the present claim therefore asserts a new all-length formula for \(k\ge3\), not dimer novelty. A separate trimer-specific result treats covariance and Gaussian fluctuations of the **indicator of triple coverage** at full deposition, not the full site multiplicity \(C_x(t)\) or a formula valid for all \(k\) and \(t\). The general local-clock method is shared, but the exact positive farthest-distance covariance and its \(k^{-5}\) law are not statements of those inspected works. Complete historical priority against unindexed work remains unverified.

## Limitations

The theorem concerns the infinite, homogeneous, one-dimensional RSC process and multiplicity counts. It makes no claim about the signs at intermediate separations, correlations of individual multiple-coverage indicators, inhomogeneous deposition rates, higher-dimensional substrates, or finite systems with boundary conditions. A closed formula at the final dependent lag does not determine the full spatial covariance spectrum or its integrated variance. The separate trimer paper establishes relevant limited-range structure for another observable; an implicit broader all-length formula in unindexed work cannot be ruled out without independent expert inspection.

## References

1. P. L. Krapivsky, *Random Sequential Covering*, arXiv:2209.03992 (first public September 8, 2022), https://arxiv.org/abs/2209.03992.
2. P. Viot and P. L. Krapivsky, *Random sequential covering of a one-dimensional lattice by \(k\)-mers*, arXiv:2410.12373 (first public October 16, 2024), https://arxiv.org/abs/2410.12373; DOI 10.1088/1742-5468/ad930b.
3. *Oscillating spatial correlations and exact Gaussian fluctuations in trimer sequential covering*, public mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-oscillating-spatial-correlations-and-exact-gaussian-fluctuations--27b43bfd218a.
