# The critical signed extension polytope of a finite metric path and its factorial volume law

## Finding
Let \(m\ge1\), let \(X=\{x_0,\ldots,x_m\}\) be a weighted metric path with consecutive edge lengths \(\ell_i>0\) for \(0\le i<m\), and write \(D=\sum_{i=0}^{m-1}\ell_i\). Add a point \(o\) at the same distance \(R\ge D/2\) from every path vertex. For real-linear extensions that preserve every input function on \(X\), the optimal Lipschitz operator norm is **one**, and the complete optimizer set at the smallest admissible radius \(R=D/2\) is the polytope described below.

Write the new-point rule as \((Ef)(o)=\sum_{j=0}^{m}w_jf(x_j)\), with real coefficients \(\sum_jw_j=1\), and define cumulative signed masses \(F_i=\sum_{j=0}^{i}w_j\) for \(0\le i<m\). At the critical attachment radius \(R=D/2\), the operator has norm one **if and only if**
\[
0\le F_i\le1\quad(0\le i<m),\qquad
\sum_{i=0}^{m-1}\ell_iF_i=D/2,
\qquad 2\sum_{i=0}^{j-1}\ell_iF_i\le\sum_{i=0}^{j-1}\ell_i\quad(1\le j<m).
\]
This polytope has affine dimension \(m-1\). It contains an operator with a **negative** coefficient exactly when \(m\ge3\), namely when the original path contains at least four vertices. For \(R>D/2\), the optimizer set has full dimension \(m\); for \(m\ge2\), it also contains negative-coefficient operators.

For unit edge lengths and \(m\ge2\), use the induced Euclidean \((m-1)\)-dimensional volume on the critical optimizer affine hull (either in signed coefficients or in cumulative coordinates). The exact volume **fraction** occupied by operators with all coefficients nonnegative is
\[
\boxed{\frac{1}{(m-1)!}}.
\]
In particular, for \(m\ge3\), the fraction of critical optimal operators with at least one negative coefficient is \(1-1/(m-1)!\). In cumulative coordinates the full critical polytope itself has volume
\[
\boxed{\frac{\sqrt m}{m!}\sum_{k=0}^{\lfloor m/2\rfloor}(-1)^k\binom{m}{k}\left(\frac m2-k\right)^{m-1}}.
\]
The standard central-cube-section factor in this last expression is classical; the stated contribution is its identification with the signed optimal-extension locus and the exact factorial comparison with positive optimizers.

## Assumptions and scope
The path distances are \(d(x_j,x_k)=\sum_{i=\min(j,k)}^{\max(j,k)-1}\ell_i\) for \(j\ne k\); all \(\ell_i\) are strictly positive. The enlarged metric satisfies \(d(o,x_j)=R\) for all \(j\), which is a metric exactly when \(R\ge D/2\). Linear operators are between the real spaces of Lipschitz functions with their Lipschitz seminorms, are required to extend the input at every original vertex, and therefore preserve constants. The same assertion holds after passing to Lipschitz spaces modulo constants. The words *signed* and *nonnegative* refer to the coefficients \(w_j\), not to values of the functions.

For \(R>D/2\), the exact complete optimizer set remains the finite system
\[
\sum_{j=0}^{m}w_j=1,\qquad
\sum_{i<j}\ell_i|F_i|+\sum_{i\ge j}\ell_i|F_i-1|\le R\quad (0\le j\le m),
\]
where sums over \(i\) always have \(0\le i<m\). For \(m=1\), negative coefficients occur in this supercritical set if and only if \(R>D\). No claim is made for other attachment metrics or non-scalar target spaces.

## Proof
**The signed path transport formula.** Every linear extension is represented by an affine coefficient vector \(w\): otherwise a constant input would have nonzero extension seminorm. The Lipschitz seminorm of its new-point coordinate relative to evaluation at \(x_j\) equals the Kantorovich--Rubinstein norm of \(\sum_rw_r\delta_{x_r}-\delta_{x_j}\). The differences along successive path edges are independent variables of modulus at most the edge length. Therefore this norm is *exactly*
\[
N_j(w)=\sum_{i<j}\ell_i|F_i|+\sum_{i\ge j}\ell_i|F_i-1|.
\]
Consequently \(\|E\|=\max\{1,\max_jN_j(w)/R\}\). The two endpoint evaluations differ by \(D\), so the triangle inequality implies \(\max_jN_j(w)\ge D/2\). The coefficient vector \(w_0=w_m=1/2\) and \(w_j=0\) for the other vertices attains \(N_j=D/2\) for **every** \(j\), proving the exact optimum and feasibility at all \(R\ge D/2\).

**Equality and full classification.** At \(R=D/2\), both \(N_0,N_m\) are at most \(D/2\). Their sum equals \(\sum_i\ell_i(|F_i|+|1-F_i|)\), which is at least \(D\). Thus equality holds edge-by-edge, giving \(0\le F_i\le1\) and \(\sum_i\ell_iF_i=D/2\). In that range the exact formula reduces to
\[
N_j(w)=D/2-\sum_{i<j}\ell_i+2\sum_{i<j}\ell_iF_i.
\]
The displayed weighted prefix inequalities are therefore both necessary and sufficient. For arbitrary \(R>D/2\), retaining the absolute-value inequalities gives the complete polytope. At the endpoint-average vector all such inequalities are strict, so the supercritical polytope has full affine dimension \(m\), and for \(m\ge2\) any sufficiently small perturbation making one interior coefficient negative remains feasible.

**Dimension and four-vertex threshold.** For \(m\ge2\), choose \(F_i=1/2+\epsilon(i-c)\), where \(c=(\sum_i i\ell_i)/D\). For sufficiently small \(\epsilon>0\) this lies strictly between zero and one, has weighted mean \(1/2\), and its proper weighted prefix averages are strictly below the overall weighted average. Hence the critical polytope has relative interior in its single weighted-sum hyperplane and dimension \(m-1\); the statement also holds for \(m=1\). If \(m\le2\), the cumulative coordinates are nondecreasing, forced by the prefix condition and weighted mean, so all coefficients are nonnegative. If \(m\ge3\), put \(F_0=1/2-\epsilon\ell_1/\ell_0\), \(F_1=1/2+\epsilon\), and \(F_i=1/2\) for \(2\le i<m\). For sufficiently small \(\epsilon>0\), this satisfies every displayed inequality but has \(w_2=F_2-F_1=-\epsilon<0\). This proves the exact threshold.

**Factorial volume law.** Let every \(\ell_i=1\) and set
\[
U_m=\{F\in[0,1]^m:\sum_iF_i=m/2\},\qquad
P_m=\{F\in U_m:\sum_{i<j}(F_i-1/2)\le0\text{ for }1\le j<m\}.
\]
Outside a measure-zero set, the \(m\) cyclic rotations of \(F_i-1/2\) have a unique rotation with all proper prefix sums nonpositive: start just after the unique maximum among the \(m\) successive partial sums. Since rotations preserve Euclidean measure on \(U_m\), \(\operatorname{vol}(P_m)=\operatorname{vol}(U_m)/m\).

The coefficient vector is nonnegative exactly when its cumulative coordinates are nondecreasing. Every nondecreasing vector in \(U_m\) belongs to \(P_m\), since a proper initial average cannot exceed the total mean \(1/2\). Coordinate permutation symmetry splits \(U_m\), up to measure-zero ties, into \(m!\) equal order regions. Its unique nondecreasing region therefore has volume \(\operatorname{vol}(U_m)/m!\). Dividing gives \(1/(m-1)!\). The affine invertible conversion between \(F\) and \(w\) has a constant Jacobian on the critical hyperplane, so the ratio is independent of the chosen induced Euclidean measure. Finally, applying inclusion-exclusion to the cumulative volume of \(\sum_iF_i\le s\) in the cube, and differentiating at \(s=m/2\), gives the standard central-section formula \(\operatorname{vol}(U_m)=\sqrt m\sum_{k=0}^{\lfloor m/2\rfloor}(-1)^k\binom{m}{k}(m/2-k)^{m-1}/(m-1)!\). Multiplication by \(1/m\) completes the claim.

## Verification
Running `python path_extension_check.py` with standard Python checks 11,715 exact-rational cumulative vectors for equivalence of the optimizer inequalities and the original signed transport norm, and 309 signed coefficient profiles against independently enumerated extremal edge-Lipschitz potentials. It also checks cyclic-ballot permutation counts for \(3\le m\le7\), the nonnegative-permutation count, and explicit critical negative-coefficient examples for three weighted paths. Expected final line: `WEIGHTED_PATH_SIGNED_OPTIMAL_EXTENSION_ALL_CHECKS_PASS`. These are finite reproducibility checks and are not the general proof, which is given above.

## Relationship to prior work
Bruè--Di Marino--Stra (arXiv:1801.07533, first posted 2018-01-23) give linear Lipschitz extensions from random projections with doubling-based estimates; their Theorem 4.1 is a general existence theorem rather than a classification of the signed critical optimizer set for path metrics. Ambrosio--Puglisi (arXiv:1609.01450, Theorems 2.14--2.15) link random projections to extension operators but do not state the factorial critical-optimizer volume fraction. Godard (arXiv:0904.3178, Theorem 3.2) provides the classical \(L_1\) structure of Lipschitz-free spaces on trees, from which the path norm formula is a familiar specialization. The central cube-section volume formula itself occurs in Marichal--Mossinghoff (arXiv:math/0607715, Theorem 4). The cyclic maximal-partial-sum argument is classical and is proved here directly; none of these ingredients is claimed as new in isolation.

The new assertion is the *joint* complete signed critical equality polytope for arbitrary weighted paths, its sharp signed four-vertex threshold, and the precise factorial proportion of positive versus signed optimal operators on unit paths. No implication from the inspected source theorems produces those statements without the separate equality and cyclic-order analyses.

## Limitations
The novelty conclusion is relative to the inspected sources and searched records, not a proof of historical uniqueness. In particular, the factorial volume law could occur in a differently titled study of continuous ballot polytopes or optimal Wasserstein centers. The volume fraction concerns the natural Lebesgue/Hausdorff measure on the affine optimizer locus, not the distribution of an unspecified sampling algorithm. No independent external mathematical audit has been performed.

## References
1. E. Bruè, S. Di Marino, F. Stra, *Linear Lipschitz and \(C^1\) extension operators through random projection*, arXiv:1801.07533 (first posted 2018-01-23), Theorem 4.1.
2. L. Ambrosio, D. Puglisi, *Linear extension operators between spaces of Lipschitz maps and optimal transport*, arXiv:1609.01450 (first posted 2016-09-06), Theorems 2.14--2.15.
3. A. Godard, *Tree metrics and their Lipschitz-free spaces*, arXiv:0904.3178 (first posted 2009-04-21), Theorem 3.2.
4. J.-L. Marichal, M. J. Mossinghoff, *Slices, slabs, and sections of the unit hypercube*, arXiv:math/0607715 (first posted 2006-07-27), Theorem 4.
