# Uniform oriented-edge sampling is minimax for two successive coordinate solves on regular graphs

## Finding

Let \(G\) be any finite connected, simple, undirected \(d\)-regular graph with \(n\ge2\) vertices, adjacency matrix \(A\), and \(0<c<1/d\). For the strictly convex quadratic with Hessian \(H=I-cA\), perform two *successive exact single-coordinate minimizations*, choosing their ordered coordinates by any fixed joint probability law (including repetition). The smallest possible worst-initial-error expected squared-\(H\)-energy retention is
\[
\boxed{\rho_*=1-\frac{(1-dc)(2+2c+c^2)}{n}.}
\]
It is attained by choosing a uniformly random **oriented graph edge** and minimizing its tail coordinate followed by its head coordinate. Every minimax law is supported on directed edges, although uniqueness of the edge-supported law is not claimed. For this uniform law the constant vector is, up to scalar, the unique worst initial direction.

Uniformly sampling an ordered pair of *distinct* vertices instead has sharp worst-direction expected energy reduction
\[
\Lambda_{\mathrm{distinct}}=\frac{1-dc}{n}\left(2+\frac{d}{n-1}(2c+c^2)\right).
\]
For noncomplete graphs this is strictly smaller than \(\Lambda_{\mathrm{edge}}=(1-dc)(2+2c+c^2)/n\). On a sequence of cycles of growing length, as \(c\uparrow1/2\), their progress ratio tends to \(13/8\). This is a comparison of one-pair worst-case *conditional expected energy decreases*, not a multistep rate or computational-time speedup.

## Assumptions and scope

All matrices and vectors are real. The graph is simple, connected and regular of degree \(d\ge1\); the Hessian is \(H=I-cA\), strictly positive definite because the spectrum of \(A\) lies in \([-d,d]\) and \(cd<1\). Translate the minimizer to the origin; the objective is \(F(x)=\frac12x^{\mathsf T}Hx\). Write \(P_i x=x-e_i(Hx)_i\), since the Hessian diagonal is one. A sampling rule is an arbitrary probability vector \(\pi_{ij}\ge0\), \(\sum_{i,j}\pi_{ij}=1\), independent of the current state. Its two-update map is \(P_jP_i\). Define
\[
\rho(\pi)=\sup_{x\ne0}\frac{\sum_{i,j}\pi_{ij}(P_jP_i x)^{\mathsf T}H(P_jP_i x)}{x^{\mathsf T}Hx}.
\]
The theorem optimizes this single-pair, worst-direction criterion, not any adaptive policy, wall-clock cost, or exact long-horizon convergence rate. A directed edge \((i,j)\) means \(A_{ij}=1\) and \(i\ne j\).

## Proof

**Energy identity.** For any vector \(x\), put \(a=Hx\). Exact minimization of coordinate \(i\) lowers its squared energy by \(a_i^2\). The residual at coordinate \(j\) after this first minimization is \(a_j-H_{ji}a_i\), so the total two-step squared-energy drop is exactly
\[
\Delta_{ij}(x)=a_i^2+(a_j-H_{ji}a_i)^2.
\]
For an edge with distinct endpoints, \(H_{ji}=-c\) and therefore \(\Delta_{ij}=a_i^2+(a_j+ca_i)^2\); for distinct nonneighbors it is \(a_i^2+a_j^2\). If \(i=j\), the second minimization is inert and \(\Delta_{ii}=a_i^2\).

**Universal obstruction, and necessary edge support.** Put \(\gamma=1-dc>0\), and test any joint law on \(x={\bf1}\). Then \(H{\bf1}=\gamma{\bf1}\), while \(\|{\bf1}\|_H^2=n\gamma\). The energy drops for a repeated vertex, a nonadjacent distinct pair, and a directed edge are, respectively,
\[
\gamma^2,\qquad 2\gamma^2,\qquad (2+2c+c^2)\gamma^2.
\]
Because \(c>0\), the last is strictly greatest. Thus no law can guarantee a worst-direction relative decrease exceeding \(\gamma(2+2c+c^2)/n\). Moreover, any law attaining the bound must assign zero probability to all repeats and distinct nonedges, since otherwise its constant-vector drop would fall strictly below the upper bound.

**Attainment by uniform edges.** The undirected graph has \(nd/2\) edges, hence \(nd\) oriented edges. Under the uniform oriented-edge law, each vertex occurs as a first or second coordinate with probability \(1/n\). Averaging the exact squared drop over the ordered edges gives
\[
\mathbb E\Delta(x)=\frac1n(Hx)^{\mathsf T}\left[(2+c^2)I+\frac{2c}{d}A\right](Hx).
\]
The Hessian \(H\) and the symmetric bracket are polynomials in \(A\), so they share orthonormal adjacency eigenvectors. For adjacency eigenvalue \(a\in[-d,d]\), the Rayleigh-normalized expected decrease equals \(f(a)/n\), where
\[
f(a)=(1-ca)\left(2+c^2+\frac{2c}{d}a\right).
\]
Its difference from the constant-mode value factors exactly as
\[
 f(a)-f(d)=\frac{c(d-a)}d\left[dc^2+2c(d+a)+2(d-1)\right].
\]
All factors in the bracket are nonnegative because \(a\ge-d\), and \(dc^2>0\); therefore \(f(a)>f(d)\) for every \(a<d\). Connectedness makes \(a=d\) a simple adjacency eigenvalue, carried by \({\bf1}\). Hence the sharp guaranteed relative drop is \(f(d)/n=\gamma(2+2c+c^2)/n\), matching the universal obstruction; both global minimax attainment and the unique worst direction follow.

**Uniform distinct-pair comparator.** Put \(\alpha=d/(n-1)\), the probability that a uniformly chosen ordered distinct pair is adjacent. The same calculation gives the expected-drop matrix \(H[(2+\alpha c^2)I+(2\alpha c/d)A]H/n\). Its eigenvalue function \(g(a)=(1-ca)(2+\alpha c^2+(2\alpha c/d)a)\) is concave on \([-d,d]\), so its minimum occurs at an endpoint. Direct subtraction gives \(g(-d)-g(d)=2c[d(2+\alpha c^2)-2\alpha]>0\) for \(d\ge1\), \(0<\alpha\le1\); thus \(a=d\) is again the worst direction. This proves the displayed \(\Lambda_{\mathrm{distinct}}\). A connected noncomplete regular graph has \(d<n-1\), so \(\alpha<1\) and its improvement by edge sampling is strict. Finally on cycles \(d=2\), \(n\to\infty\) gives \(\alpha\to0\); then \(c\uparrow1/2\) makes the ratio of the two sharp decreases tend to \((2+1+1/4)/2=13/8\).

## Verification

Run `python3 verify.py` using the accompanying standalone Python 3 file. It uses only standard-library exact rational arithmetic and checked 45 graph/coupling cases: cycles, complete graphs, a complete bipartite graph, a cube and the Petersen graph. It reconstructs the two-update matrices and exact energy losses for every ordered pair, checks the proposed average matrix, the constant-mode bound, strict edge equality, and the eigenvalue factorization at rational arguments. Output: `PASS: 45 graph/coupling cases, exact rational pair and matrix identities, spectra inequalities.` These finite tests do not establish the all-graph theorem; the preceding algebraic proof does.

## Relationship to prior work

Randomized block Gauss–Seidel and coordinate selection were developed by Tu et al. (2017), Rodomanov and Kropotov (2019), and Wright and Lee (2017). The cited papers' available full texts analyze simultaneous sampled blocks, volume sampling, or permutation epochs, rather than this exact two-successive-singleton minimax calculation over all joint laws on regular graphs. An accessible published result titled *Sharp optimal cyclic-block Gauss–Seidel contraction and a screened-Poisson crossover* gives a different exact one-step law for **simultaneously minimizing a contiguous cyclic block**; for two coordinates its cycle formula is \(2(1-2c)/(n(1-c))\), not the sequential pair value above. This distinction is about the update operator, not simply different notation. Standard quadratic energy identities, adjacency spectral bounds and regular-graph symmetry are acknowledged as known ingredients. No bibliographic exhaustiveness is claimed.

## Limitations

The guarantee is for a connected simple regular graph, normalized diagonal Hessian, strictly positive subcritical interaction \(0<c<1/d\), exact arithmetic, and an error-independent one-pair sampling distribution. At \(c=0\), the strict necessity of edge support disappears; at \(c=1/d\), the Hessian is singular and the stated SPD criterion changes. Nonregular or signed graphs, nonuniform diagonal scaling, noisy or relaxed coordinate updates, and adaptive or multistep-optimal laws are not analyzed. Other edge-supported laws might also be globally minimax. The sharp improvement is an expected energy-decrease ratio; it does not imply the same ratio for iteration counts or runtime. A broader, possibly older two-projection theorem could imply this result, so publication priority is not independently established.

## References

1. S. Tu, S. Venkataraman, A. C. Wilson, A. Gittens, M. I. Jordan, and B. Recht, *Breaking Locality Accelerates Block Gauss-Seidel*, arXiv:1701.03863, first public 2017-01-14, https://arxiv.org/abs/1701.03863.
2. A. Rodomanov and D. Kropotov, *A Randomized Coordinate Descent Method with Volume Sampling*, arXiv:1904.04587, first public 2019-04-09, https://arxiv.org/abs/1904.04587.
3. S. Wright and C.-P. Lee, *Analyzing Random Permutations for Cyclic Coordinate Descent*, arXiv:1706.00908, first public 2017-06-03, https://arxiv.org/abs/1706.00908.
4. *Sharp optimal cyclic-block Gauss–Seidel contraction and a screened-Poisson crossover*, published research record, https://github.com/published-finding corpus/2026.
