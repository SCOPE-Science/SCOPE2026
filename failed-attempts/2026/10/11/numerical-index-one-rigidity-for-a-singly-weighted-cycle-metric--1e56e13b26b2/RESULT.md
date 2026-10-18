# Numerical-index-one rigidity for a singly weighted cycle metric

## Finding
Let \(n\ge3\) be an integer. On the edges of a cyclic graph with vertices \(v_0,\ldots,v_{n-1}\), assign length \(1\) to \(n-1\) consecutive edges and length \(w>0\) to the remaining edge. Give the vertex set \(M_{n,w}\) the shortest-path metric. For the **real** Lipschitz-free space \(X_{n,w}=\mathcal F(M_{n,w})\), its numerical index satisfies the sharp dichotomy
\[
\boxed{\;n(X_{n,w})=1\quad\Longleftrightarrow\quad w\ge n-1\quad\text{or}\quad(n\text{ is even and }w=1).\;}
\]
Whenever \(0<w<n-1\) and either \(n\) is odd or \(w\ne1\), one has the **strict** inequality \(n(X_{n,w})<1\). Thus every nonzero perturbation of the single edge away from \(1\) sufficiently close to \(1\) destroys numerical-index one on an even cycle, although the underlying graph stays bipartite. Numerical-index one reappears when the distinguished edge becomes metrically redundant at \(w=n-1\).

## Assumptions and scope
All scalars are real; the graph contains exactly the displayed \(n\) vertices, and its metric is the minimum weighted length of connecting paths. The numerical index of a real normed space \(X\) is
\[
n(X)=\inf_{\|T\|=1}\;\sup\bigl\{|x^*(Tx)|:\ x\in S_X,\ x^*\in S_{X^*},\ x^*(x)=1\bigr\}.
\]
The free space \(\mathcal F(M)\) is the canonical predual of real Lipschitz functions vanishing at a chosen base vertex. The conclusion decides only whether the numerical index equals its maximal value \(1\); it does not compute its value below \(1\).

## Proof
**1. The redundant-edge regime.** If \(w\ge n-1\), a path using the distinguished edge never improves a distance between cycle vertices relative to the path along the \(n-1\) unit edges: replacing that edge by the unit-edge chain costs no more. Hence the metric is exactly the path metric on \(n\) points. On that path the map sending a zero-based Lipschitz function to its \(n-1\) unit-edge increments is a linear isometry from \(\operatorname{Lip}_0(M_{n,w})\) onto \(\ell_\infty^{n-1}\); dualizing gives \(X_{n,w}\cong\ell_1^{n-1}\). The real space \(\ell_1^{n-1}\) has numerical index \(1\): every extreme point of its unit ball is a signed coordinate vector and every extreme functional is a coordinate sign vector, so every extreme pairing has absolute value \(1\).

**2. Edge-coordinate geometry in the strict-cycle regime.** Assume \(0<w<n-1\). Orient the cycle consistently; write \(l_1=\cdots=l_{n-1}=1\) and \(l_n=w\). Each edge length is strictly smaller than the length of its complementary route (for a unit edge the complementary route has length \(n-2+w>1\); for the distinguished edge it has length \(n-1>w\)). Its endpoints therefore have distance exactly \(l_i\). Let
\[
m_i=\frac{\delta_{v_{i-1}}-\delta_{v_i}}{l_i},
\qquad i=1,\ldots,n,
\]
with vertices read cyclically. Every difference between two vertices is a signed telescoping sum of the edge differences along a shortest path, so its normalized molecule lies in \(\operatorname{conv}\{\pm m_i:1\le i\le n\}\). Conversely all \(m_i\) are unit molecules; consequently
\[
B_{X_{n,w}}=\operatorname{conv}\{\pm m_1,\ldots,\pm m_n\}.
\]
Each \(m_i\) is exposed. Indeed, fix \(i\) and put \(L=\sum_{j\ne i}l_j>l_i\). Prescribe the oriented edge increment of a potential \(f\) to be \(l_i\) on edge \(i\) and \(-l_i l_j/L\) on each other edge \(j\). They sum to zero, so they integrate to a function on the cycle; the normalized slopes are \(1\) on edge \(i\) and \(-l_i/L\), strictly between \(-1\) and \(1\), on every other edge. Thus the corresponding norm-one functional exposes \(m_i\) in the displayed finite convex hull. Exactly the \(2n\) vectors \(\pm m_i\) are the extreme points of \(B_X\).

For any dual unit-ball element \(f\), put \(\theta_i=(f(v_{i-1})-f(v_i))/l_i\). The edge inequalities alone characterize the Lipschitz norm for the shortest-path metric, and increments integrate to a potential exactly when they close around the cycle. Hence
\[
B_{X_{n,w}^*}\cong H_l:=\left\{\theta\in[-1,1]^n:\ \sum_{i=1}^n l_i\theta_i=0\right\},
\qquad f(m_i)=\theta_i.
\]
A point of \(H_l\) is extreme if and only if at least \(n-1\) coordinates attain \(\pm1\). With two strictly interior coordinates, a small nonzero perturbation proportional to their opposite edge lengths preserves the single linear equation and the cube, proving nonextremality. Conversely, \(n-1\) saturated coordinate constraints and the single positive-weight linear equation uniquely determine the point, proving extremality.

**3. The numerical-index-one test.** McGregor's finite-dimensional real criterion states that \(n(X)=1\) if and only if \(|f(x)|=1\) for every extreme \(x\in B_X\) and every extreme \(f\in B_{X^*}\). In the present coordinates, by Step 2, this is precisely
\[
\text{every vertex of }H_l\text{ has }|\theta_i|=1\text{ for all }i.
\]
If \(n\) is odd, assign \(n-1\) unit-edge coordinates equally many \(+1\) and \(-1\), and set \(\theta_n=0\). This is a vertex of \(H_l\) with an interior coordinate, so \(n(X_{n,w})<1\) for every \(0<w<n-1\).

If \(n\) is even and \(1<w<n-1\), assign the \(n-1\) unit-edge coordinates signs summing to \(+1\), and set \(\theta_n=-1/w\). This lies strictly inside the last coordinate interval and is a vertex of \(H_l\), so \(n(X_{n,w})<1\).

If \(n\) is even and \(0<w<1\), assign \(\theta_n=+1\), assign \(n-2\) unit-edge coordinates an equal number of \(+1\) and \(-1\), and assign the final unit-edge coordinate \(-w\). Again exactly one coordinate is interior at a vertex of \(H_l\), proving \(n(X_{n,w})<1\).

Finally suppose \(n\) is even and \(w=1\). At every vertex of \(H_l\), at least \(n-1\) coordinates are signs. If exactly one coordinate were interior, the sum of the other \(n-1\) signs would be an odd integer, so its negative, required for the remaining coordinate, could lie in \([-1,1]\) only if it were \(+1\) or \(-1\), a contradiction. Therefore every dual vertex has all coordinates at \(\pm1\). The McGregor criterion gives \(n(X_{n,1})=1\). Combining the cases completes the proof.

## Verification
The argument is an exact symbolic proof for every integer \(n\ge3\) and real \(w>0\). The boundary \(w=n-1\) was handled separately via metric redundancy; neither a limiting argument nor an unverified strict inequality was used there. In the strict regime the primal extreme molecules are exposed by explicit 1-Lipschitz functionals, and dual extremality follows from a complete hyperplane-section vertex criterion. All four parity/weight regimes are settled constructively, using McGregor's proved finite-dimensional characterization. No numerical enumeration or software run is claimed as a proof.

## Relationship to prior work
McGregor's finite-dimensional characterization supplies the numerical-index-one criterion; it does not classify the present metric family. Godard's tree-metric work motivates the \(\ell_1\) behavior when the distinguished edge becomes redundant. Cobollo, Guirao, and Montesinos treat the two-dimensional Lipschitz-free case, covering the three-vertex specialization but not the entire cycle family. Published higher-cycle parity calculations determine the index for **unit-edge cycles**, and a published bipartiteness criterion concerns only **unweighted** shortest-path metrics. These cover the \(w=1\) case but do not imply the sharp strict inequality for the weighted regime \(w\ne1\). In particular, subdividing a rationally weighted edge changes the finite vertex set and produces a different Lipschitz-free space; numerical-index-one is not automatically inherited by arbitrary subspaces. General weighted graph-metric literature identifies cycle relations, without a covering numerical-index classification for this one-edge perturbation.

## Limitations
Only the real scalar field and a positive single-edge perturbation of an otherwise unit cycle are treated. The theorem is an exact threshold classification, not a formula for numerical-index values in the failing regions. Known unweighted results cover the \(w=1\) slice and existing two-dimensional results cover the three-vertex specialization; novelty concerns the uniform weighted parameter regimes, the instability of the even-cycle index-one property, and the exact redundancy threshold. A historical equivalent formula in weighted hyperplane-quotient or polyhedral terminology might exist outside the inspected literature; this is a residual bibliographic risk. No claim of independent validation is made.

## References
1. C. M. McGregor, *Finite-Dimensional Normed Linear Spaces with Numerical Index 1*, J. London Math. Soc. (1971), DOI 10.1112/jlms/s2-3.4.717.
2. A. Godard, *Tree metrics and their Lipschitz-free spaces*, arXiv:0904.3178v1, first public 2009-04-21.
3. C. Cobollo, A. J. Guirao, V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces*, arXiv:2304.13183v1, first public 2023-04-25.
4. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814v1.
5. *Bipartiteness exactly characterizes numerical index one for finite graph metrics*, published research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-bipartiteness-exactly-characterizes-numerical-index-one-for-fini--1ca1185831c4 .
6. *Numerical-index parity law for Lipschitz-free spaces over cycles*, published research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-numerical-index-parity-law-for-lipschitz-free-spaces-over-cycles--06885f9d5f05 .
