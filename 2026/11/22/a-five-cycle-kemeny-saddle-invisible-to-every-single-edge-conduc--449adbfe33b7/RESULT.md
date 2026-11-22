# A five-cycle Kemeny saddle invisible to every single-edge conductance scan

## Finding

**Theorem (sharp cycle-size obstruction to coordinatewise conductance design).** Let \(C_n\), \(n\ge3\), have positive edge conductances \(w_0,\ldots,w_{n-1}\). The discrete-time, loopless, reversible random walk crosses edge \(\{i,i+1\}\) with probability proportional to its conductance. Denote the zero-target Kemeny constant by \(K_n(w)\). Scaling all conductances by the same positive factor does not change \(K_n\).

For **every** \(n\ge3\), holding all but one conductance at one and allowing the remaining conductance \(t>0\), the homogeneous walk is the **unique** minimizer along that one-edge family:
\[
\boxed{K_n(1,\ldots,1,t)-K_n(1,\ldots,1)
=\frac{(n-1)(n-2)^2(t-1)^2}{6(n-1+t)((n-1)t+1)}.}
\tag{1}
\]
Nevertheless, the uniform conductance vector is a **strict saddle** of the full, fixed-total-conductance Kemeny-design problem already on \(C_5\). For every real \(\epsilon\) with \(0<|\epsilon|<1\), the feasible five-edge profile
\[
(w_0,w_1,w_2,w_3,w_4)=(1+\epsilon,1+\epsilon,1,1-\epsilon,1-\epsilon)
\]
keeps the budget \(\sum_iw_i=5\) and satisfies the exact improvement
\[
\boxed{K_5(w)=4-\frac{2\epsilon^2}{5(5-\epsilon^2)}<4=K_5(1,1,1,1,1).}
\tag{2}
\]
The threshold at five vertices is sharp: on \(C_3\), equal conductances uniquely minimize \(K_3\) over **all** positive assignments; on \(C_4\), the global minimum \(5/2\) is attained exactly when \(w_0w_2=w_1w_3\), and includes the uniform conductances. Thus no cycle with fewer than five vertices can exhibit the uniform-design failure in (2).

## Assumptions and scope

All vertices are labelled modulo \(n\); edge \(i\) joins \(i\) to \(i+1\). Each \(w_i\) is a strictly positive real number. Set \(d_i=w_{i-1}+w_i\) and \(M=\sum_iw_i\). The transition probabilities are \(P_{i,i+1}=w_i/d_i\) and \(P_{i,i-1}=w_{i-1}/d_i\), with \(P_{ii}=0\). The stationary distribution is \(\pi_i=d_i/(2M)\).

Here \(K_n=\sum_{\lambda\ne1}(1-\lambda)^{-1}=\sum_j\pi_j\mathbb E_i T_j\), with \(T_i=0\) if the sampled target equals the starting vertex. This is well-defined for every irreducible finite chain, including the periodic even cycles. It is **not** the Kirchhoff index (the unweighted sum of resistances), the worst-case mixing rate, or the expected commute time under uniformly selected endpoints. No assertion of a globally optimal five-cycle profile is made: equation (2) supplies a strict improvement, not a full global minimization.

The fixed-budget design set is \(\{w_i>0:\sum_iw_i=n\}\); scale invariance allows every positive vector to be compared after such normalization. A one-edge scan in (1) changes the raw budget but is equivalent to its normalized fixed-budget scan because simultaneous scaling leaves \(P\) unchanged.

## Proof

**1. Weighted resistance representation.** Let \(R_{ij}\) be effective electrical resistance between vertices \(i,j\) when each edge has resistance \(1/w_i\). The standard commute-time identity for this reversible walk gives \(\mathbb E_i T_j+\mathbb E_j T_i=2MR_{ij}\). Because the random-target hitting-time mean does not depend on its starting vertex, averaging over two independent stationary endpoints and pairing both orientations yields
\[
\boxed{K_n(w)=\frac{1}{2M}\sum_{0\le i<j<n}d_i d_jR_{ij}.}
\tag{3}
\]
For a cycle, two arcs of total resistances \(s\) and \(T-s\) connect any pair in parallel, where \(T=\sum_i1/w_i\). Hence
\[
 R_{ij}=\frac{s(T-s)}T,\qquad s=\sum_{k=i}^{j-1}\frac1{w_k}\quad (i<j).
\tag{4}
\]
These identities hold for every positive weight vector, including for odd and even cycles.

**2. One-edge exact identity for every length.** Put \(m=n-1\), place the exceptional edge of weight \(t>0\) between vertices \(0,m\), and give the other \(m\) path edges weight one. Then \(M=m+t\), both path endpoints have degree \(1+t\), and all \(m-1\) interior vertices have degree two. For two vertices separated by \(k\) edges of the unit path, the series/parallel formula gives
\[
R(k)=\frac{k[1+t(m-k)]}{1+mt},\qquad 1\le k\le m.
\]
In the numerator of (3), group the endpoint pair, the endpoint-to-interior pairs, and the interior-to-interior pairs. Their sum, multiplied by \(1+mt\), is exactly
\[
 m(1+t)^2+4(1+t)\sum_{k=1}^{m-1}k[1+t(m-k)]
 +4\sum_{k=1}^{m-2}(m-1-k)k[1+t(m-k)].
\]
Using the standard sums of first, second and third integer powers, this simplifies to
\[
\frac m3\left[(2m^2+1)(t^2+1)+m(m^2+5)t\right].
\]
Therefore
\[
K_n(1,\ldots,1,t)=\frac{m[(2m^2+1)(t^2+1)+m(m^2+5)t]}{6(m+t)(mt+1)}.
\tag{5}
\]
At \(t=1\), this is \(((m+1)^2-1)/6=(n^2-1)/6\). Subtracting and factoring the numerator gives precisely (1). Since \(n\ge3\), its coefficient is positive and both denominator factors are positive; equality holds if and only if \(t=1\). Every edge is equivalent by cycle rotation. This also proves the asserted fixed-budget coordinatewise statement by homogeneity.

**3. A fixed-budget descent on five vertices.** For the vector in (2), \(M=5\), the degrees in vertex order are \((2,2+2\epsilon,2+\epsilon,2-\epsilon,2-2\epsilon)\). The total arc resistance is \(T=(5-\epsilon^2)/(1-\epsilon^2)\). Substitute these quantities into (3)--(4), and group the ten unordered vertex pairs into the five adjacent and five nonadjacent pairs. Direct rational simplification gives respectively
\[
 \sum_{i=0}^4 d_i d_{i+1}R_{i,i+1}=16,
 \qquad
 \sum_{i=0}^4 d_i d_{i+2}R_{i,i+2}=\frac{4(30-7\epsilon^2)}{5-\epsilon^2},
\]
with indices understood modulo five. Dividing the combined sum by \(2M=10\) gives (2). Its denominator is strictly positive for \(|\epsilon|<1\); every nonzero such perturbation reduces \(K_5\). Along this budget-preserving direction the second derivative at zero is \(-4/25<0\), while (1) gives strictly increasing one-coordinate deviations (after normalization). Therefore the homogeneous allocation is stationary and is a genuine saddle, not a local minimum, in the four-dimensional budget simplex. Stationarity follows also from permutation of the five edge coordinates under the cycle automorphism group, which fixes the homogeneous vector and acts transitively on edges; the gradient on the fixed-sum tangent space must vanish.

**4. Sharp exclusion of smaller cycles.** On \(C_3\), the reversible transition matrix has three real eigenvalues \(1,\lambda_2,\lambda_3\). Its diagonal vanishes, so \(\lambda_2+\lambda_3=-1\). Strict convexity of \(u\mapsto(1-u)^{-1}\) on \((\!-\infty,1)\) gives
\[
K_3=\frac1{1-\lambda_2}+\frac1{1-\lambda_3}\ge\frac43,
\]
with equality precisely when both nonconstant eigenvalues equal \(-1/2\). In that equality case the simple eigenvalue-one projector is \(\mathbf1\pi^\top\), so \(P=-I/2+3\mathbf1\pi^\top/2\). Since \(P_{ii}=0\), all three \(\pi_i=1/3\), giving \(P_{ij}=1/2\) for distinct vertices. The three conductances must consequently be equal. Conversely uniform conductances attain \(4/3\).

On \(C_4\), bipartition the vertices into \(\{0,2\}\) and \(\{1,3\}\). Reversibility and bipartiteness give transition eigenvalues \(1,-1,\rho,-\rho\) with \(0\le\rho<1\), and the two off-diagonal blocks have determinant product
\[
\rho^2=\frac{(w_0w_2-w_1w_3)^2}{d_0d_1d_2d_3}.
\]
Consequently
\[
K_4=\frac12+\frac1{1-\rho}+\frac1{1+\rho}
=\frac52+\frac{2\rho^2}{1-\rho^2}\ge\frac52.
\]
Equality is equivalent to \(w_0w_2=w_1w_3\). Uniform conductances satisfy this criterion. The triangle and four-cycle results make the five-cycle counterexample minimal among simple cycles.

## Verification

The standalone `verify.py` uses only the Python standard library and runs with `python3 verify.py`. Its first implementation computes exact \(K_n\) from the parallel-resistance sum (3)--(4). An **independent** implementation constructs the transition matrix and solves rational linear systems for the mean hitting time from vertex zero to each other target. All computations are exact `fractions.Fraction` arithmetic. The script verifies the one-edge formula on \(3\le n\le23\) at eight rational conductances, the five-cycle formula at eleven rational perturbations, and the triangle/four-cycle classifications on rational examples. It completed **631 exact-rational comparisons**. These tests do not replace the all-parameter algebraic arguments above.

For one illustrative value, \(\epsilon=1/2\) gives \(K_5=378/95\), strictly below the homogeneous value four while each possible isolated edge change increases it.

## Relationship to prior work

The eigenvalue formula and global network-design motivation are classical. Zhang, Sheng, Hu and Chen (2012) study which **unweighted network topologies** minimize Kemeny's constant and develop exact spectra for sparse scale-free/fractal networks; they do not optimize positive conductances on one fixed cycle. Kirkland and Zeng (2016) develop forest formulas and Kemeny--Braess **edge addition on trees**, not simultaneous positive conductance retuning on a fixed five-cycle. The first two pages and abstract of their accessible article were inspected; its complete publisher text was unavailable in this source access.

The weighted electrical representation (3) is itself standard and is not claimed as new. A separate published research record concerning adding an **unweighted chord** to a cycle determines a different intervention (new graph topology, rather than fixed-topology allocation). Another published record studies **weighted-cycle last-coverage laws**, not the stationary-target mean hitting time. A five-cycle **continuous-time spectral-gap** design result optimizes a distinct objective and does not imply the discrete-time normalized-walk Kemeny counterexample. The new contribution is the **joint** all-length coordinatewise optimality identity, explicit strictly descending five-cycle budget direction, and proof that five vertices are the first possible cycle size.

## Limitations

No assertion is made that the displayed five-cycle family contains a global minimizer, that every nonuniform five-cycle improves Kemeny's constant, or that the effect extends without change to continuous-time generators or to arbitrary graphs. The strict descent is of quadratic order near equal weights and can be numerically small. This result is based on exact algebra and the inspected accessible literature; older or unindexed treatments of Kemeny optimization on weighted cycles may contain an equivalent statement. Independent mathematical validation has not been performed.

## References

1. Z. Zhang, Y. Sheng, Z. Hu and G. Chen, *Optimal and suboptimal networks for efficient navigation measured by mean-first passage time of random walks*, arXiv:1211.4295, first public 2012-11-19. https://arxiv.org/abs/1211.4295
2. S. Kirkland and Z. Zeng, *Kemeny's Constant and an Analogue of Braess' Paradox for Trees*, Electronic Journal of Linear Algebra 31 (2016), 444--464. https://doi.org/10.13001/1081-3810.3222
3. X. Wang, J. L. A. Dubbeldam and P. Van Mieghem, *Kemeny's constant and the effective graph resistance*, Linear Algebra and Its Applications 535 (2017), 231--244. https://doi.org/10.1016/j.laa.2017.09.003
4. *A single antipodal shortcut optimally reduces Kemeny transport on cycles*, publicly accessible research record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-single-antipodal-shortcut-optimally-reduces-kemeny-transport-o--8c80d7a9cb1e
5. *Hidden one-dimensional fairness in reversible weighted cycle cover tours*, publicly accessible research record. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-hidden-one-dimensional-fairness-in-reversible-weighted-cycle-cov--65056ab3b0c0
6. *Exact active-edge allocation on a five-cycle with one priced link*, publicly accessible research record. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-active-edge-allocation-on-a-five-cycle-with-one-priced-lin--ccfd8e9d0e03
