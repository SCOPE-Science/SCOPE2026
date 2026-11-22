# Reentrant optimal single-pin conditioning on a four-vertex weighted path

## Finding

Let \(P_4\) have vertices \(1,2,3,4\) in path order and consecutive edge conductances \((1,25,5)\). For \(g>0\) and any vertex \(v\), put \(A_v(g)=L+g e_ve_v^\top\), where \(L\) is the weighted graph Laplacian, and define the spectral condition number \(\kappa_v(g)=\lambda_{\max}(A_v(g))/\lambda_{\min}(A_v(g))\).

**Theorem.** Among all four possible sites, the unique minimizer of \(\kappa_v(g)\) is \(v=2\) at \(g=10\), \(v=4\) at \(g=50\), and \(v=2\) again at \(g=500\). Consequently, as the common finite pinning gain varies continuously, the identity of an optimal single pin undergoes at least two distinct changes, including a return to a previously optimal vertex. Furthermore, vertex \(2\) is uniquely optimal for **all sufficiently large** \(g\), not merely at the displayed value \(500\). The three strict finite-gain winner identities hold for every sufficiently small simultaneous perturbation of the three positive edge conductances and the three tested gains.

## Assumptions and scope

The graph is undirected, simple and connected, its four vertices are labelled along the path, and exactly one positive diagonal pin is installed. The three conductances are held fixed at \((1,25,5)\), while the common gain \(g\) is an externally specified positive scalar; there is no optimization over edge weights, the magnitude of \(g\), or the number of pins. The matrix is

\[
L=\begin{pmatrix}1&-1&0&0\\-1&26&-25&0\\0&-25&30&-5\\0&0&-5&5\end{pmatrix}.
\]

The condition number is the Euclidean operator-norm condition number of the symmetric positive-definite pinned matrix, not an inverse-trace, convergence-rate, or ordinary unpinned-Laplacian eigenratio objective.

## Proof

For \(x\in\mathbb R^4\),

\[
x^\top A_v(g)x=(x_1-x_2)^2+25(x_2-x_3)^2+5(x_3-x_4)^2+g x_v^2.
\]

If this quadratic form vanishes, the three differences and the pinned coordinate vanish, hence \(x=0\). Thus all four eigenvalues are strictly positive for each \(v\) and each \(g>0\).

For each of the twelve choices \((g,v)\) with \(g\in\{10,50,500\}\) and \(v\in\{1,2,3,4\}\), the accompanying `check.py` stores four disjoint rational intervals of width \(10^{-6}\), and verifies exactly that the characteristic polynomial \(\det(A_v(g)-\lambda I)\) changes sign between the two endpoints of each interval. This polynomial has degree four, so four disjoint sign changes prove that every interval contains exactly one eigenvalue and together they enclose the entire spectrum. No numerical eigensolver is part of this certificate.

If \(\lambda_{\min}\in[a,b]\) and \(\lambda_{\max}\in[c,d]\), with \(0<a<b<c<d\), then \(c/b<\kappa_v(g)<d/a\), with exact rational endpoints. The same verifier proves that, at each gain, the certified *upper* condition-number bound of the stated winner is strictly below the certified *lower* bound for each of the other three sites. It checks nine rational inequalities in total. The following decimal table is solely for orientation; the rational brackets in `check.py` provide the proof.

| Gain \(g\) | \(\kappa_1\) | \(\kappa_2\) | \(\kappa_3\) | \(\kappa_4\) | Unique best vertex |
|---|---:|---:|---:|---:|---:|
| 10 | 183.234 | 66.708 | 70.436 | 84.152 | 2 |
| 50 | 170.519 | 88.897 | 95.868 | 80.349 | 4 |
| 500 | 1568.455 | 528.321 | 554.539 | 681.539 | 2 |

A separate structural argument certifies the entire large-gain tail. Write \(L_{\bar v}\) for the \(3\times3\) principal submatrix of \(L\) with row and column \(v\) deleted. By the min–max principle (or by compactness of unit Rayleigh minimizers as the penalty grows),

\[
\lim_{g\to\infty}\lambda_{\min}(A_v(g))=\lambda_{\min}(L_{\bar v}),\qquad
\lim_{g\to\infty}\frac{\lambda_{\max}(A_v(g))}{g}=1.
\]

For vertex \(2\), \(L_{\bar 2}\) is a direct sum of \([1]\) and \(\begin{psmallmatrix}30&-5\\-5&5\end{psmallmatrix}\). The latter block minus the identity is positive definite, since its leading diagonal entry is \(29>0\) and its determinant is \(91>0\); hence \(\lambda_{\min}(L_{\bar 2})=1\). For each other site, a Rayleigh test vector with coordinate \(v\) zero gives a quotient below \(1\): choose \((0,1,1,1)\) for \(v=1\), giving \(1/3\); choose \((1,1/26,0,0)\) for \(v=3\), giving a quotient below \(25/26\); and choose \((1,1/4,1/5,0)\) for \(v=4\), giving a quotient below \(33/40\). Thus

\[
\lim_{g\to\infty}\frac{\kappa_2(g)}g=1
<\lim_{g\to\infty}\frac{\kappa_v(g)}g
\quad(v\in\{1,3,4\}),
\]

so \(v=2\) is the unique minimizing pin for all sufficiently large gains. This identifies the eventual winner without numerical asymptotics or a fully solved finite-gain phase diagram.

For fixed edge weights, the four positive eigenvalues of \(A_v(g)\), and hence their extreme ratio, vary continuously in \(g>0\). Between the first and second gains, the optimal site must cease to be 2; between the second and third, site 4 must cease to be optimal. The associated winner-change points lie in disjoint gain intervals. Strict winner gaps and continuous eigenvalues also preserve the three winner identities under sufficiently small perturbations of weights and gains.

## Verification

With Python 3 and the standard library, run `python check.py` from the directory containing this file. The program evaluates a tridiagonal continuant exactly using `fractions.Fraction`, validates forty-eight rational sign-changing eigenvalue brackets, and compares nine exact rational condition-number bounds. It ends with `PASS: 48 disjoint exact-rational eigenvalue sign brackets; 9 strict optimality inequalities` on a successful run. No floating point is used in any proof assertion; displayed decimal ratios are diagnostic only.

## Relationship to prior work

Jalili, Askari Sichani and Yu (2015) introduced the same augmented-Laplacian eigenratio as a pinning-control placement criterion and studied optimized driver placement through evolutionary computation; they did not derive the present finite weighted-path return of a unique optimal site under a fixed changing gain. Orouskhani, Jalili and Yu (2016) studied separate and joint optimization of pin locations, feedback gains, and link weights; in particular they discuss that optimizing gains can change which locations are chosen, so qualitative dependence on gain is **not** claimed as new. The new assertion is the three-stage, exact-rational, robust *return* of the optimal site on one fixed small weighted path.

Jafarizadeh (2024) analytically optimizes the eigenratio on weighted networks including a singly pinned path, but permits link weights and feedback parameters themselves to be optimized; that design freedom does not imply the winner ordering when all three conductances and each tested gain are fixed as here. Shafi, Arcak and El Ghaoui (2010) optimize node and edge weights against Laplacian spectral constraints, again a different feasible set. Exact sign-changing characteristic-polynomial root isolation is classical and is not presented as a new method.

## Limitations

The theorem provides certified comparisons at three gains and an eventual large-gain winner, not a complete phase diagram or exact switching gains. It does not show that four vertices are minimal for reentrance, that there are exactly two switches, or that the specific observed return is generic among all weighted paths. Nor does it imply that minimizing spectral condition number is the same as optimizing every dynamical stability metric. The literature comparison supports priority only to the extent of the inspected open texts and indexed records; an unindexed equivalent example remains possible. There has been no independent mathematical validation.

## References

1. M. Jalili, O. Askari Sichani and X. Yu, *Optimal pinning controllability of complex networks: Dependence on network structure*, Physical Review E **91** (2015), 012803, published 2015-01-05. https://doi.org/10.1103/PhysRevE.91.012803
2. Y. Orouskhani, M. Jalili and X. Yu, *Optimizing Dynamical Network Structure for Pinning Control*, Scientific Reports **6** (2016), 24252, published 2016-04-12. https://pmc.ncbi.nlm.nih.gov/articles/PMC4828652/
3. S. Jafarizadeh, *Achieving Network Stability via Optimal Pinning Control in Weighted Complex Networks*, IEEE Access **12** (2024), 195256–195278. https://doi.org/10.1109/ACCESS.2024.3520735
4. S. Y. Shafi, M. Arcak and L. El Ghaoui, *Designing Node and Edge Weights of a Graph to Meet Laplacian Eigenvalue Constraints* (2010). https://people.eecs.berkeley.edu/~elghaoui/Pubs/SAE_Allerton_2010.pdf
