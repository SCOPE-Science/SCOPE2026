# A sharp nonlinear-coupling window for two-probe trace estimation on a weighted five-cycle

## Finding

Let \(B\) be any real symmetric \(5\times5\) matrix whose only nonzero off-diagonal entries are the five edges of the cycle \(1\!\! -\!\!2\!\! -\!\!3\!\! -\!\!4\!\! -\!\!5\!\! -\!\!1\), with weights \(B_{12}=B_{23}=B_{34}=B_{45}=1\) and \(B_{51}=t>0\). The diagonal entries are arbitrary. Let \(Z,Z'\in\{-1,1\}^5\) each have the uniform Rademacher-vector distribution, but permit any joint coupling. Define the unbiased two-probe trace estimator

\[
H=\tfrac12\left(Z^{\mathsf T}BZ+{Z'}^{\mathsf T}BZ'\right).
\]

Its **minimum variance over all couplings with these marginals** is

\[
V_*(t)=\begin{cases}4t^2,&0<t\le1,\\
3+(t-2)^2,&1\le t\le3,\\
4,&t\ge3.\end{cases}
\]

If coupling is restricted to a deterministic componentwise sign flip, \(Z'=s\odot Z\) for a fixed \(s\in\{-1,1\}^5\), the optimal variance instead is \(V_{\rm flip}(t)=4\min\{1,t^2\}\). Hence **nonlinear coupling strictly improves every fixed sign-flip coupling precisely for \(1<t<3\)**. The maximum relative improvement within that interval is \(25\%\), uniquely at \(t=2\), where \(V_*=3\), \(V_{\rm flip}=4\), and two independent uniform probes have variance \(16\).

This is the first simple-cycle size at which such an advantage can occur: on any positively weighted triangle, an optimal fixed sign flip attains the overall coupling optimum; on any even cycle, a fixed checkerboard sign flip gives zero variance.

## Assumptions and scope

Every probe individually has mutually independent, equiprobable signs. **Independence between the two probes is explicitly *not* assumed.** Couplings may depend on the five off-diagonal weights and may have a nonlinear or nonlocal dependence on the first probe. Two separate quadratic forms are evaluated and averaged. The variance is with respect to the joint law of the probes, with \(B\) fixed. The diagonal of \(B\) need not be specified: under sign probes it contributes exactly \(\operatorname{tr}(B)\), so it does not affect variance. Adding a sufficiently large positive multiple of the identity yields the same conclusions for positive-definite matrices.

The optimization is over the coupling law, not over arbitrary unbiased trace estimators, probe distributions, deterministic matrix reconstructions, or matrix-query algorithms. The graph is the simple weighted cycle on five vertices, not an arbitrary sparsity pattern.

## Proof

**1. Parity reduction and the complete scalar distribution.** For indices understood modulo five, define \(\sigma_i=Z_iZ_{i+1}\) and

\[
S=\sigma_1+\sigma_2+\sigma_3+\sigma_4+t\sigma_5.
\]

Then \(Z^{\mathsf T}BZ=\operatorname{tr}(B)+2S\), so \(H-\operatorname{tr}(B)=S+S'\). The five edge signs obey \(\prod_{i=1}^5\sigma_i=1\). Conversely, each of the sixteen even-parity edge-sign patterns has exactly two vertex-sign preimages. Because \(Z\) is uniform, all sixteen edge-sign patterns are equiprobable. If \(k\in\{0,1,2,3,4\}\) is the number of minus signs among the first four edges, then \(\sigma_5=(-1)^k\) and \(S=4-2k+t(-1)^k\), with multiplicity \(\binom4k\). Thus its complete distribution consists of five affine levels:

| Level | Value | Multiplicity |
|---|---:|---:|
| \(A\) | \(4+t\) | 1 |
| \(B\) | \(2-t\) | 4 |
| \(C\) | \(t\) | 6 |
| \(D\) | \(-2-t\) | 4 |
| \(E\) | \(t-4\) | 1 |

In particular \(\mathbb ES=0\), hence \(\operatorname{Var}(H)=\mathbb E(S+S')^2\).

**2. Global coupling optimum is an attainable antitone pairing.** For any two real-valued variables with the same finite marginal, the rearrangement inequality (proved by swapping crossed pairs) minimizes \(\mathbb E[SS']\) by pairing the sorted values with the reverse-sorted values. For clarity, whenever \(a\le b\) and \(c\le d\), matching \((a,d),(b,c)\) instead of \((a,c),(b,d)\) changes the sum of products by \(-(b-a)(d-c)\le0\); repeated swaps establish global optimality. Because each scalar atom arises from whole equal-mass vertex-sign states, the reverse-sorted coupling is exactly realizable: order the sixteen even-parity edge patterns by \(S\), match them in reverse order, lift each pattern to either of its two vertex-sign preimages by an independently uniform overall sign, and use an independent overall sign for the second vector. Each marginal is precisely uniform on all \(32\) vertex-sign states, and the constructed coupling achieves the scalar lower bound.

For \(0<t<1\) the ascending level order is \(E,D,C,B,A\); the eight unordered reverse-position pairs comprise one \((A,E)\), four \((B,D)\), and three \((C,C)\). Every pair sum is \(\pm2t\), hence \(V_*(t)=4t^2\).

For \(1<t<3\) the order is \(D,E,B,C,A\); the eight pairs are one \((A,D)\), three \((C,D)\), one \((C,E)\), two \((B,C)\), and one \((B,B)\). Six pair sums have magnitude \(2\), and the remaining two are \(2t-4\) and \(4-2t\). Their average squared sum is \((24+2(2t-4)^2)/8=3+(t-2)^2\).

For \(t>3\) the order is \(D,B,E,C,A\); the eight pairs are one \((A,D)\), three \((C,D)\), three \((B,C)\), and one \((B,E)\), each having squared sum \(4\). Hence \(V_*(t)=4\). At \(t=1,3\) adjacent levels tie and the expressions agree continuously, establishing the non-strict boundaries as stated.

**3. Fixed sign-flip benchmark.** For \(Z'=s\odot Z\) write \(\eta_i=s_is_{i+1}\); then \(\prod_i\eta_i=1\) and \(S+S'=\sum_iw_i(1+\eta_i)\sigma_i\), with weights \((w_1,\ldots,w_5)=(1,1,1,1,t)\). Distinct edge signs on a simple cycle are pairwise uncorrelated, each with variance one, and consequently

\[
\operatorname{Var}(H)=4\sum_{i:\,\eta_i=1} w_i^2.
\]

Since the cycle has odd length, the number of positive \(\eta_i\) must be odd; it cannot be zero. Exactly one positive \(\eta_i\) is attainable at any chosen edge. With all weights positive, the optimum is thus \(4\min\{1,t^2\}\). Comparing with the three branches above gives strict improvement exactly on \((1,3)\), and in this interval

\[
\frac{V_{\rm flip}(t)-V_*(t)}{V_{\rm flip}(t)}
=\frac{(t-1)(3-t)}4 \le \frac14,
\]

with equality only at \(t=2\). Each individual quadratic form has variance \(4(4+t^2)\), so averaging two independent copies has variance \(2(4+t^2)\).

**4. Minimality among simple cycles.** On a positively weighted triangle, edge-sign parity gives four equiprobable values. If the positive weights are ordered \(a\ge b\ge c>0\), antitone pairing of these four values produces scalar pair sums \(2c,2c,-2c,-2c\), and the global minimum variance is \(4c^2\), already attained by a fixed sign flip preserving only the minimum-weight edge. On any even cycle, choosing alternating vertex signs makes \(\eta_i=-1\) on every edge, giving \(S+S'=0\) identically, the absolute lower bound. Thus triangles and four-cycles cannot show a nonlinear-coupling improvement, whereas the weighted five-cycle does.

## Verification

The accompanying standalone Python 3 verifier uses only exact integers and rational arithmetic. It checks all sixteen parity-state multiplicities, the affine level orders for all parameter regimes, the exact quadratic variance polynomials from reverse-order matching, the complete \(32\)-state vertex enumeration for thousands of rational \(t\) values, and the minimum over every fixed vertex-sign flip. All assertions must pass when run as `python3 verify.py`. Finite enumerations confirm, but do not replace, the analytic exchange argument and complete symbolic parameter partition above.

## Relationship to prior work

Cortinovis and Kressner (2020) analyze standard stochastic trace estimation using *independent* Rademacher or Gaussian probes, including indefinite matrices. Stathopoulos, Laeuchli, and Orginos (2013) construct graph-coloring and structured Hadamard probing schemes, including fixed patterns that cancel selected graph edges. Skorski (2020) develops concentration estimates for Hutchinson trace estimators, and Frommer, Nasr Khalil, and Ramirez-Hidalgo (2021) analyze multilevel variance reduction. Those results motivate two-probe variance analysis but do not, in the inspected statements and relevant sections, resolve this exact arbitrary-coupling, weighted-five-cycle variance classification. The rearrangement inequality used here is classical and is **not** claimed as a new principle; the contribution is the exact graph-specific optimum, thresholds, sharp improvement, and minimum-cycle distinction.

## Limitations

The improvement requires coupling that depends on the weights and generally is not a fixed sign flip; it is not a claim of computational speedup or practical superiority over algorithms using additional matrix information. It is only an exact finite-dimensional benchmark, not a new general trace-estimation complexity bound. The joint law is permitted to be arbitrarily dependent, although each probe marginal remains uniform; conclusions may change under restrictions such as joint coordinatewise independence, fixed linear transformations, or unknown weights. Equivalent prior specialist enumeration or couplings may exist; originality is assessed against the literature inspected, not independently certified.

## References

1. Alice Cortinovis and Daniel Kressner, *On randomized trace estimates for indefinite matrices with an application to determinants*, first public arXiv version 20 May 2020, https://arxiv.org/abs/2005.10009.
2. Andreas Stathopoulos, Jesse Laeuchli, and Kostas Orginos, *Hierarchical probing for estimating the trace of the matrix inverse on toroidal lattices*, arXiv 17 February 2013, https://arxiv.org/abs/1302.4018.
3. Maciej Skorski, *A Modern Analysis of Hutchinson's Trace Estimator*, arXiv 23 December 2020, https://arxiv.org/abs/2012.12895.
4. Andreas Frommer, Mostafa Nasr Khalil, and Gustavo Ramirez-Hidalgo, *A Multilevel Approach to Variance Reduction in the Stochastic Estimation of the Trace of a Matrix*, arXiv 25 August 2021, https://arxiv.org/abs/2108.11281.
