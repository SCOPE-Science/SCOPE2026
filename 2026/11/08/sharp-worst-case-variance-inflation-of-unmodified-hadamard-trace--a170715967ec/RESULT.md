# Sharp worst-case variance inflation of unmodified Hadamard trace probes

## Finding

For a real symmetric matrix of dyadic order, uniformly sampling a few unmodified Walsh--Hadamard rows to estimate its trace may have **larger**, not smaller, variance than using the same number of independent Rademacher probes. The exact worst-case variance inflation over all non-diagonal symmetric matrices is

\[
\boxed{\frac{n(n-k)}{2(n-1)}}\quad(1\le k<n,\quad n=2^m).
\]

The sharp bound holds within positive-definite matrices of condition number arbitrarily close to one. Equality holds exactly when, for every nonzero binary offset, all off-diagonal entries on the associated binary-XOR perfect matching are equal. For every \(n\ge4\) and \(1\le k\le n-2\), that worst-case factor exceeds one; for \(k=n-1\) it is below one, and at \(k=n\) the entire Hadamard trace is exact.

Using **one shared, independently sampled Rademacher diagonal sign matrix** before choosing the same distinct Hadamard rows instead yields the exact universal identity

\[
\operatorname{Var}(\widehat\tau_{\mathrm{signed},k})
=\frac{n-k}{n-1}\operatorname{Var}(\widehat\tau_{\mathrm{iid},k}),
\]

so the known random-sign modification removes the adverse variance inflation. This last construction is established in earlier hierarchical probing; the new assessment concerns the exact sharp worst-case envelope, its equality geometry, and the query-budget reversal.

## Assumptions and scope

Let \(m\ge1\), \(n=2^m\), and identify indices with \(\mathbb F_2^m\). Let \(A\) be an arbitrary deterministic real symmetric \(n\)-by-\(n\) matrix. Define the Sylvester--Walsh row vectors by

\[
h_r(j)=(-1)^{r\cdot j},\qquad r,j\in\mathbb F_2^m.
\]

Choose a uniform \(k\)-element subset \(S\) of all \(n\) row indices without replacement and form \(\widehat\tau_{H,k}=k^{-1}\sum_{r\in S}h_r^T A h_r\). Compare with \(\widehat\tau_{\mathrm{iid},k}\), the average of \(k\) independent quadratic forms \(z^T A z\), where each coordinate of each \(z\) is an independent fair sign. Both estimators use \(k\) products with \(A\), are unbiased, and are considered only when \(\sum_{i<j}A_{ij}^2>0\) in the variance ratio. At \(k=n\) the Hadamard estimator has zero variance. To obtain \(\widehat\tau_{\mathrm{signed},k}\), draw one independent fair-sign vector \(\varepsilon\), multiply every selected Hadamard row coordinatewise by this **shared** vector, and average their quadratic forms; the same sampled subset is used throughout this definition.

## Proof

For each nonzero \(s\in\mathbb F_2^m\), write

\[
c_s=\sum_{j\in\mathbb F_2^m}A_{j,j\oplus s}
=2\sum_{\{i,j\}:i\oplus j=s}A_{ij}.
\]

The second sum runs over the \(n/2\) edges of the perfect matching with XOR difference \(s\). Expanding each quadratic form and grouping the Walsh characters yields the exact character identity

\[
h_r^T A h_r=\operatorname{tr}A+\sum_{s\ne0}c_s(-1)^{r\cdot s}.
\]

Orthogonality of the \(n\) Walsh characters implies \(n^{-1}\sum_r h_r^T A h_r=\operatorname{tr}A\) and, by Parseval, the population variance of the \(n\) row values equals \(\sum_{s\ne0}c_s^2\). The ordinary finite-population identity for a uniform size-\(k\) subset without replacement gives

\[
\operatorname{Var}(\widehat\tau_{H,k})
=\frac{n-k}{k(n-1)}\sum_{s\ne0}c_s^2.

\]

Independence of Rademacher coordinates, together with symmetry, gives the classical identity

\[
\operatorname{Var}(\widehat\tau_{\mathrm{iid},k})
=\frac4k\sum_{i<j}A_{ij}^2.

\]

Each unordered pair \(\{i,j\}\) belongs to exactly one nonzero XOR matching. Cauchy--Schwarz on each matching yields

\[
c_s^2=4\left(\sum_{\{i,j\}:i\oplus j=s}A_{ij}\right)^2
\le 2n\sum_{\{i,j\}:i\oplus j=s}A_{ij}^2.
\]

Summing in \(s\) and combining (1)--(2) proves the announced sharp ratio. Equality in every Cauchy--Schwarz inequality is necessary and sufficient: the coefficients must be constant along each nonzero XOR matching. This permits zero coefficients on an entire matching and imposes no restriction on the diagonal.

For sharpness in the positive-definite cone, fix \(s\ne0\), let \(P_s\) be the symmetric permutation matrix \((P_s)_{ij}=\mathbf1_{\{j=i\oplus s\}}\), and set \(A=I+\epsilon P_s\) for any \(0<\epsilon<1\). Since \(P_s^2=I\) and \(P_s\) has eigenvalues \(\pm1\), this matrix is positive definite with condition number \((1+\epsilon)/(1-\epsilon)\) and saturates the bound. Letting \(\epsilon\downarrow0\) makes the condition number tend to one without changing the variance ratio. Elementary evaluation of the bound gives the strict adverse and favorable query-budget regions in the finding; for \(n=2,k=1\) equality rather than strict advantage holds.

For shared random signs, write \(D=\operatorname{diag}(\varepsilon_j)\) and \(A'=DAD\). Conditionally on \(D\), formula (1) applies to \(A'\) and the conditional mean remains exactly \(\operatorname{tr}A\). Now

\[
c_s(D)=2\sum_{\{i,j\}:i\oplus j=s}A_{ij}\varepsilon_i\varepsilon_j.
\]

Distinct unordered pairs induce distinct degree-two sign monomials, which are pairwise orthogonal in expectation. Consequently

\[
\mathbb E_D[c_s(D)^2]=4\sum_{\{i,j\}:i\oplus j=s}A_{ij}^2.
\]

Apply conditional total variance, sum these identities over nonzero \(s\), and use (2) to obtain the exact shared-sign variance factor \((n-k)/(n-1)\). No assumption of independently re-randomizing signs between rows is made.

## Verification

A standalone exact-arithmetic Python checker evaluates the Walsh character formula, all sample-without-replacement choices in representative dyadic sizes, exhaustive shared-sign patterns, the sharp permutation-matching positive-definite examples, and independent Rademacher comparisons. Running `python verify_hadamard.py` prints `PASS 3151 exact variance and equality assertions`. The proof of the all-size statement uses Walsh orthogonality and Cauchy--Schwarz rather than extrapolation from this finite verification. For \(n=8,k=3\), the exact worst-case inflation is \(20/7\), while the shared-sign factor is \(5/7\).

## Relationship to prior work

Frommer, Rinelli, and Schweitzer (2023) establish variance formulas for stochastic probing with graph-color partitions and give the motivating numerical trace-estimation setting. Their inspected results concern independent sign probes on partition classes, rather than the uniform unmodified Hadamard-row sampling variance envelope and its sharp XOR-matching equality class. Stathopoulos, Laeuchli, and Orginos (2013) developed hierarchical probing with Hadamard construction and **already proposed a shared initial random-sign vector** to restore unbiasedness; no priority is claimed for that sign randomization. Laeuchli and Stathopoulos (2020) analyze extended graph-color/Hadamard probing rather than this query-budget extremum. Fika and Koukouvinos studied Hadamard-based trace estimation, but their relevant full text could not be inspected; an explicit specialist-priority uncertainty therefore remains.

## Limitations

The unmodified-row result assumes uniform random subsampling from **all** rows of a Sylvester matrix, not the prescribed hierarchical ordering, independently chosen random diagonal signs, an arbitrary orthogonal system, or Gaussian sketches. The upper ratio is not a guarantee of superiority on every input; it describes a sharp worst case. The shared-sign result evaluates variance averaged over the shared signs and the sampled subset. These results concern trace-estimation variance, not computation of matrix-vector products, matrix-function approximation errors, or unbiasedness under an arbitrary fixed nonrandom row selection. Uninspected specialist literature may contain equivalent results. Independent external validation has not been carried out.

## References

1. A. Frommer, M. Rinelli, M. Schweitzer, *Analysis of stochastic probing methods for estimating the trace of functions of sparse symmetric matrices*, arXiv:2308.07722v1, first posted 2023-08-15. https://arxiv.org/abs/2308.07722
2. A. Stathopoulos, J. Laeuchli, K. Orginos, *Hierarchical probing for estimating the trace of the matrix inverse on toroidal lattices*, arXiv:1302.4018, first posted 2013-02-17. https://arxiv.org/abs/1302.4018
3. J. Laeuchli and A. Stathopoulos, *Extending Hierarchical Probing for Computing the Trace of Matrix Inverses*, SIAM J. Sci. Comput. (2020). https://doi.org/10.1137/18M1176427
4. P. Fika and C. Koukouvinos, *Stochastic estimates for the trace of functions of matrices via Hadamard matrices*, Communications in Statistics - Simulation and Computation, DOI:10.1080/03610918.2015.1096373. Full text not inspected.
