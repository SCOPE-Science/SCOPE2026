# Two-patch collapse of fixed-area habitat capacity under area-elastic dispersal

## Finding
Let a finite landscape have at least two potential habitat sites and a symmetric, nonnegative dispersal-affinity matrix with zero diagonal and at least one positive edge. For every area elasticity \(\gamma\geq1\), allocating a fixed positive total habitat area to maximize the Perron root of the kernel \(M_{ij}=w_{ij}(A_iA_j)^\gamma\) leads **exactly** to two occupied sites. They must be the endpoints of an edge of maximum affinity and must each receive half the total area. The optimal value is \(w_{\max}(B^2/4)^\gamma\). There are no other maximizers.

This universal conclusion is not exponent-insensitive: at elasticity \(\gamma=1/2\), three equally connected sites with equal area achieve capacity \(2B/3\), strictly exceeding the best two-site capacity \(B/2\). More generally, in that three-site example, the equal three-site design beats every two-site design whenever \(0<\gamma<\log(2)/\log(9/4)\). This last inequality is a sufficient witness to failure of two-site optimality, not a complete optimization classification for intermediate exponents.

## Assumptions and scope
Take any integer \(n\geq2\), \(B>0\), and \(\gamma\geq1\). Fix a real symmetric matrix \(W=(w_{ij})_{1\leq i,j\leq n}\) satisfying \(w_{ii}=0\), \(w_{ij}\geq0\), and \(w_{\max}=\max_{i\ne j}w_{ij}>0\). Choose areas \(A_i\geq0\) subject only to \(\sum_{i=1}^{n}A_i=B\). Define \(M_{ii}=0\) and \(M_{ij}=w_{ij}(A_iA_j)^\gamma\) for distinct sites. Capacity means the largest eigenvalue \(\lambda_{\max}(M)\), equivalently the Perron root of this nonnegative symmetric matrix.

This is an explicitly specified **area-elastic spectral surrogate**, motivated by metapopulation capacity. The original incidence-function and other metapopulation models can use different powers, extinction dependencies and self-terms; the theorem is not asserted for those other kernels. Area can be reassigned without changing the fixed affinities, and removing a patch (zero area) is allowed. This matters: if every area must be strictly positive and \(n>2\), the stated maximum is generally only a supremum, not an attained optimum.

## Proof
Write \(C=w_{\max}(B^2/4)^\gamma\). For each site \(i\), the nonnegative row sum \(R_i\) satisfies
\[
R_i=\sum_{j\ne i}w_{ij}A_i^\gamma A_j^\gamma
\leq w_{\max}A_i^\gamma\sum_{j\ne i}A_j^\gamma
\leq w_{\max}\bigl(A_i(B-A_i)\bigr)^\gamma
\leq C.
\]
The middle inequality follows from \(\sum_j x_j^\gamma\leq(\sum_jx_j)^\gamma\) for nonnegative numbers and \(\gamma\geq1\). The last inequality is \(A_i(B-A_i)\leq B^2/4\). The induced infinity norm, or equivalently the Perron row-sum bound, gives \(\lambda_{\max}(M)\leq C\).

Select an edge \(\{p,q\}\) with \(w_{pq}=w_{\max}\), assign \(A_p=A_q=B/2\), and put zero area elsewhere. Its only nonzero spectral block is the \(2\)-by-\(2\) matrix with off-diagonal value \(C\), so \(\lambda_{\max}(M)=C\). The bound is sharp.

For completeness, suppose equality holds in the spectral bound. The positive Perron eigenvalue is attained on an irreducible connected component of the graph of nonzero entries of \(M\), with at least two vertices. On that component the positive left Perron vector shows that, if every row sum is at most \(C\) and the Perron root is \(C\), **every** component row sum equals \(C\): multiplying the row-sum inequalities by that vector and summing forces equality termwise. Therefore every vertex \(i\) of this component realizes equality in \(A_i(B-A_i)\leq B^2/4\) and hence \(A_i=B/2\). Because total area is \(B\), the component has exactly two vertices, these exhaust the entire budget, and equality in the first row-sum bound forces their connecting affinity to be \(w_{\max}\). Thus the listed designs are the only global maximizers, even if \(W\) is reducible.

To check the boundary's substantive dependence on the area exponent, consider three sites with \(w_{ij}=1\) for all distinct \(i,j\) and areas \(A_1=A_2=A_3=B/3\). The matrix is a constant off-diagonal matrix of value \((B^2/9)^\gamma\), with eigenvalues \(2(B^2/9)^\gamma\) and twice \(-(B^2/9)^\gamma\). Any allocation supported on at most two sites has Perron root at most \((B^2/4)^\gamma\), by the arithmetic-geometric mean inequality. Their strict comparison is
\[
2(B^2/9)^\gamma>(B^2/4)^\gamma
\quad\Longleftrightarrow\quad
\gamma<\frac{\log2}{\log(9/4)}.
\]
At \(\gamma=1/2\), this becomes \(2B/3>B/2\). This proves the stated counterexample without making any claim about a globally sharp critical exponent for every landscape when \(\gamma<1\).

## Verification
The standalone `checker.py` runs exact rational checks for the normalized three-site specializations and an exact expression for the comparison exponent, then uses independently generated symmetric nonnegative matrices and area vectors to compare eigenvalues against the analytic bound and test two-patch sharpness. It passed 8,103 assertions in the packaged environment. These finite checks are diagnostics only; the preceding row-sum and equality arguments prove the infinite families for all dimensions, allowed affinities, budgets and exponents.

Run `python checker.py` with Python 3.10 or newer and NumPy. No network or external data are needed.

## Relationship to prior work
Hanski and Ovaskainen (2000) introduced leading-eigenvalue metapopulation capacity to compare patch networks; the present statement instead optimizes the explicitly defined area-elastic kernel over *all* nonnegative area allocations under one conserved total. Etienne and Heesterbeek (2000), Etienne (2004), and Nicol and Possingham (2010) study reserve size, allocation, and persistence in different stochastic or demographic specifications; no equivalence with this universally weighted spectral allocation problem was established from the accessible text. Bertuzzo, Rodriguez-Iturbe, and Rinaldo (2015) inspect full landscape spectral capacities, use row-sum estimates, and vary river-network topology rather than independently reallocating area under an arbitrary fixed weighted adjacency matrix. Thus the general inequality in the proof uses familiar Perron mathematics, but the parameter-uniform habitat-allocation classification and strict two-site support consequence are not identified in the inspected comparisons. Priority remains provisional: several potentially relevant older papers were only available in abstract or metadata form.

## Limitations
A capacity proxy need not order actual stochastic extinction times, ecological richness, redundancy or spatial feasibility. Real habitat patch positions and areas interact; keeping affinities fixed while reallocating all area may be physically infeasible. If a minimum area at all sites, multiple-species constraints, asymmetric transfer, nonzero diagonal terms, nonlinear crowding, or area-dependent patch-extinction rates are imposed, the optimal allocation can change. The theorem proves no global threshold below \(\gamma=1\), no robustness to parameter estimation error and no field management recommendation. The novelty comparison is limited to inspected evidence and requires independent historical checking.

## References
1. Hanski, I., and Ovaskainen, O. (2000), *The metapopulation capacity of a fragmented landscape*, Nature 404, 755–758, first published 13 April 2000, https://doi.org/10.1038/35008063 .
2. Etienne, R. S., and Heesterbeek, J. A. P. (2000), *On optimal size and number of reserves for metapopulation persistence*, Journal of Theoretical Biology 203, 33–50, https://doi.org/10.1006/jtbi.1999.1060 .
3. Etienne, R. S. (2004), *On optimal choices in increase of patch area and reduction of interpatch distance for metapopulation persistence*, Ecological Modelling 179, 77–90, https://doi.org/10.1016/j.ecolmodel.2004.05.003 .
4. Nicol, S. C., and Possingham, H. P. (2010), *Should metapopulation restoration strategies increase patch area or number of patches?*, Ecological Applications 20, 566–581, https://doi.org/10.1890/08-2216.1 .
5. Bertuzzo, E., Rodriguez-Iturbe, I., and Rinaldo, A. (2015), *Metapopulation capacity of evolving fluvial landscapes*, Water Resources Research 51, 2696–2706, https://doi.org/10.1002/2015WR016946 .
