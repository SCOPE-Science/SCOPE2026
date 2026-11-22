# Sharp graph-local positivity horizons and an SSP-equality motif for second-order Markov Runge–Kutta

## Finding

Let \(Q\) be a finite continuous-time Markov generator in row convention: \(Q_{ij}=a_{ij}\ge0\) for \(i\ne j\), \(Q_{ii}=-\lambda_i\), and \(\lambda_i=\sum_{j\ne i}a_{ij}\). For distinct vertices put
\[
\tau_{ij}=\sum_{k\notin\{i,j\}}a_{ik}a_{kj},\qquad
\Delta_{ij}=(\lambda_i+\lambda_j)a_{ij}-\tau_{ij}.
\]
For the completed two-stage, second-order explicit Runge–Kutta map
\[
P(h)=I+hQ+\frac{h^2}{2}Q^2,
\]
if \(Q\ne0\) define
\[
H(Q)=\min_{\substack{i\ne j,\ a_{ij}>0\\\Delta_{ij}>0}}\frac{2a_{ij}}{\Delta_{ij}}.
\]
The minimum is over a nonempty finite collection, and the **entire** entrywise-nonnegative set is exactly \(\{h\ge0:P(h)\ge0\}=[0,H(Q)]\). In particular no later positivity recovery occurs. When \(Q=0\), every \(h\ge0\) is admissible.

With \(M=\max_i\lambda_i>0\), the sharp universal comparison is
\[
\frac1M\le H(Q)\le\frac2M.
\]
The familiar forward-Euler/SSP bound is **exactly** sharp, \(H(Q)=1/M\), if and only if there is a directed edge \(i\to j\) of positive rate joining two maximal-exit vertices (\(\lambda_i=\lambda_j=M\)) with **no positive directed two-step alternative** from \(i\) to \(j\) (\(\tau_{ij}=0\)). Thus a purely local graph motif characterizes when the completed second-order step *strictly* improves on its general SSP bound. The factor two is globally sharp: on the unit-rate undirected star with \(m\ge2\) leaves, \(H(Q)=2/(m+1)\) and \(M H(Q)=2m/(m+1)\to2\).

For an unweighted \(d\)-regular undirected graph, writing \(t\) for the minimum number of common neighbors across an edge, the formula reduces to \(H(Q)=2/(2d-t)\); in particular, strict improvement occurs precisely when every edge is in a triangle. This regular-graph specialization is explanatory, not the novelty claim in isolation.

## Assumptions and scope

The state set is any finite nonempty set. Edge rates are fixed finite real nonnegative numbers, with zero diagonal in \(a\); no irreducibility, reversibility, regularity, symmetry or connectedness is assumed. The property concerns the **completed** endpoint map on every nonnegative initial row distribution, not the intermediate Runge–Kutta stage. Matrix inequalities are entrywise. Steps \(h\) are real and nonnegative. The sharpness statements compare actual completed-step positivity, not order accuracy or total variation. The result includes absorbing states and zero-rate links; when all rates vanish the horizon is infinite.

## Proof

**Exact entry decomposition.** Since \(Q_{ii}=-\lambda_i\), direct matrix multiplication gives, for \(i\ne j\),
\[
(Q^2)_{ij}=-\lambda_i a_{ij}-\lambda_j a_{ij}+\tau_{ij}=-\Delta_{ij}.
\]
Consequently
\[
P_{ij}(h)=h a_{ij}-\frac{h^2}{2}\Delta_{ij}.
\]
If \(a_{ij}=0\), then \(\Delta_{ij}=-\tau_{ij}\le0\) and \(P_{ij}=h^2\tau_{ij}/2\ge0\) for all \(h\). If \(a_{ij}>0\) and \(\Delta_{ij}\le0\), the entry is nonnegative for every \(h\). If both are positive, the entry is nonnegative precisely when \(0\le h\le2a_{ij}/\Delta_{ij}\), and is strictly negative for *all* larger \(h\).

The diagonal entries are never the first obstruction. Indeed
\[
(Q^2)_{ii}=\lambda_i^2+\sum_{k\ne i}a_{ik}a_{ki},\quad
P_{ii}(h)=1-h\lambda_i+\frac{h^2}{2}\left(\lambda_i^2+\sum_{k\ne i}a_{ik}a_{ki}\right)
\ge\frac12+\frac12(1-h\lambda_i)^2\ge\frac12.
\]
Also \(Q\mathbf1=0\), so every row of \(P(h)\) sums to one. For \(Q\ne0\), choose \(i\) with \(\lambda_i=M>0\). If \(h>2/M\), then \(P_{ii}(h)>1\), forcing an offdiagonal entry in that row to be negative. Hence some positive-rate edge has \(\Delta_{ij}>0\) and the displayed finite minimum exists. Taking the minimum of the exact offdiagonal thresholds proves the interval characterization, including endpoint equality and absence of recovery.

**Universal bounds and equality.** Rewrite
\[
P(h)=\tfrac12 I+\tfrac12(I+hQ)^2.
\]
The forward-Euler matrix \(I+hQ\) is nonnegative and stochastic when \(0\le h\le1/M\). Hence \(H(Q)\ge1/M\). The previous maximal-exit diagonal argument gives \(H(Q)\le2/M\). For every edge with \(\Delta_{ij}>0\),
\[
\frac{2a_{ij}}{\Delta_{ij}}=
\frac{2}{\lambda_i+\lambda_j-\tau_{ij}/a_{ij}}\ge\frac1M.
\]
Equality occurs exactly when \(\lambda_i=\lambda_j=M\) and \(\tau_{ij}=0\). Since a nonempty finite minimum is attained, \(H(Q)=1/M\) if and only if at least one such edge exists. In an undirected positively weighted support, \(\tau_{ij}>0\) exactly when the edge belongs to at least one support triangle.

**Extremal examples.** On an undirected unit-rate star with \(m\) leaves, every edge has \(\tau_{ij}=0\), the center exit rate is \(m\), and the leaf exit rate is \(1\). Thus all edge thresholds are \(2/(m+1)\), and \(M=m\), establishing the sharp limiting factor two. For an unweighted \(d\)-regular graph, \(\tau_{ij}\) is the common-neighbor count \(c_{ij}\), so each edge threshold is \(2/(2d-c_{ij})\); the minimum is determined by \(t=\min c_{ij}\). This proves every assertion.

## Verification

Run `python3 verify.py` from the same directory (Python 3 standard library only). This independently computes the generator, quadratic propagator and exact rational threshold for directed weighted matrices on two through four states; checks stochastic row sums, the diagonal lower bound, endpoint nonnegativity, negativity beyond the calculated horizon, and the maximal-exit motif criterion; and tests stars with two through fifty leaves. It uses exact `fractions.Fraction` arithmetic and checks the polynomial both directly and through the Euler-square representation. The run returned `VERIFY_OK exact_assertion_groups= 39240`. These finite assertions corroborate the algebra but are not the proof of the all-size theorem.

## Relationship to prior work

The classic strong-stability-preserving Runge–Kutta literature establishes the sufficient forward-Euler step-size bound by convex stage decompositions. The inspected arXiv full text of Gottlieb, Grant and Higgs (2014), Section 2, explicitly gives the two-stage second-order SSP method with coefficient one; it does not derive a sharp fixed-generator endpoint horizon or the maximal-exit two-hop equality criterion. Lóczi and Ketcheson (2013) analyze absolute-monotonicity radii of stability functions, not this generator-dependent criterion. Horváth's 2005 work concerns positivity thresholds for general positive IVP classes; its full text was not available for inspection, creating a priority risk for general generator-specialized formulations.

Two directly relevant earlier published technical results were checked by their complete available result texts. “A triangle-count law for positive two-stage Euler supersteps on regular graphs” analyzes \((I-h_2L)(I-h_1L)\) with arbitrary **nonnegative real** substeps. Those products have quadratic coefficient \(h_1h_2\le(h_1+h_2)^2/4\); they cannot reproduce the second-order Runge–Kutta coefficient \(h^2/2\) at the same total time \(h\). Its formula for regular unweighted matrix entries is related and credited, but its extremal superstep result does not imply the present directed weighted characterization. “A path-parity certificate for sharp positivity loss in Taylor diffusion” gives a **sufficient** walk-gap criterion for a constant-rate graph to have its Euler bound sharp; it does not classify arbitrary weighted, directed, nonregular generators or characterize the strict-improvement cases. The common foundational polynomial expansion is not claimed as new in isolation.

## Limitations

The result is an exact endpoint-positivity and graph-motif classification for **second-order** explicit Runge–Kutta only. It does not imply intermediate-stage positivity for steps beyond \(1/M\), small numerical error near \(H(Q)\), or analogous behavior at higher order or for time-varying generators. The regular-graph common-neighbor identity and the SSP sufficient interval are known ingredients. Historical exact-step positivity treatments that cannot be examined in full, especially Horváth (2005), might cover some or all of the directed weighted statement; bibliographic priority remains subject to independent research. No independent mathematical audit has been carried out.

## References

1. L. Lóczi and D. I. Ketcheson, “Rational functions with maximal radius of absolute monotonicity,” arXiv:1303.6651, first public 2013-03-26, https://arxiv.org/abs/1303.6651 . Primary MSC 65L06.
2. S. Gottlieb, Z. J. Grant and D. Higgs, “Optimal Explicit Strong Stability Preserving Runge–Kutta Methods with High Linear Order and optimal Nonlinear Order,” arXiv:1403.6519v1, first public 2014-03-25, https://arxiv.org/html/1403.6519v1 .
3. Z. Horváth, “On the positivity step size threshold of Runge–Kutta methods,” *Applied Numerical Mathematics* **53** (2005), 341–356, https://doi.org/10.1016/j.apnum.2004.08.026 . Full text not inspected.
4. “A triangle-count law for positive two-stage Euler supersteps on regular graphs,” public technical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-triangle-count-law-for-positive-two-stage-euler-supersteps-on--395a6d422888 . Complete `RESULT.md` inspected.
5. “A path-parity certificate for sharp positivity loss in Taylor diffusion,” public technical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-path-parity-certificate-for-sharp-positivity-loss-in-taylor-di--2c9867ce7a18 . Complete `RESULT.md` inspected.
