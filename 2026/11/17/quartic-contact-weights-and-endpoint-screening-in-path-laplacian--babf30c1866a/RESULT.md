# Quartic contact weights and endpoint screening in path Laplacian simplices

## Finding
For every integer \(n\ge4\), take the path on vertex set \(\{1,\ldots,n\}\), with its unweighted symmetric graph Laplacian \(L_n\). In the ordinary Euclidean metric on the hyperplane \(H_n=\{x\in\mathbb R^n:\sum_i x_i=0\}\), form the **canonical Laplacian simplex**
\[
Q_n=\operatorname{conv}\{L_ne_1,\ldots,L_ne_n\}\subset H_n.
\]
The unique smallest closed Euclidean ball containing \(Q_n\) has squared radius
\[
\boxed{R_n^2=6-\frac{6}{\binom{n+2}{5}}=6-\frac{720}{(n-2)(n-1)n(n+1)(n+2)}.}
\]
Its center \(c_n=(c_{n,1},\ldots,c_{n,n})\) has the **quadratic coordinate profile**
\[
\boxed{c_{n,i}=\frac{-6i^2+6(n+1)i-(n+1)(n+2)}{2\binom{n+2}{5}},\qquad 1\le i\le n.}
\]
For \(n\ge5\), exactly the \(n-2\) columns indexed by \(2,\ldots,n-1\) lie on the minimum enclosing sphere. Both endpoint columns lie strictly inside it, at squared-distance clearance
\[
\boxed{R_n^2-\|L_ne_1-c_n\|^2=R_n^2-\|L_ne_n-c_n\|^2=4-\frac{6n}{\binom{n+2}{5}}>0.}
\]
At the sharp boundary \(n=4\), **all four** vertices lie on the minimum sphere. The center has the following positive barycentric certificate on the interior columns:
\[
\boxed{c_n=\sum_{i=2}^{n-1}\lambda_{n,i}L_ne_i,
\qquad\lambda_{n,i}=\frac{\binom{i}{2}\binom{n-i+1}{2}}{\binom{n+2}{5}}>0,
\qquad\sum_{i=2}^{n-1}\lambda_{n,i}=1.}
\]
The radius approaches the constant interior-vertex norm \(\sqrt6\) with the exact fifth-order deficit \(6-R_n^2\sim720n^{-5}\).

For the exceptional three-vertex path, the center is \((-2/9,4/9,-2/9)\), \(R_3^2=98/27\), and all three vertices touch.

## Assumptions and scope
The path graph is finite, simple, undirected, unweighted, and consecutively labelled; the Euclidean metric is the inherited metric on \(H_n\), **not** the metric after an arbitrary unimodular reduction of the Laplacian matrix. The simplex is \((n-1)\)-dimensional because \(L_n\) has kernel \(\operatorname{span}\{\mathbf1\}\) and rank \(n-1\). A minimum enclosing ball covers the entire convex hull, equivalently every displayed vertex. The all-size formula is valid for integers \(n\ge4\), with the separate \(n=3\) case above. A sphere through all vertices need not be the **smallest enclosing sphere**; this distinction matters here.

## Proof
Write \(v_i=L_ne_i\), \(B=\binom{n+2}{5}\), and let \(w\in\mathbb R^n\) be the vector with endpoints zero and interior entries \(w_i=\binom{i}{2}\binom{n-i+1}{2}/B\). All interior weights are strictly positive. Set \(m=n-2\), \(j=i-1\), and
\[
F(j)=j(j+1)(m+1-j)(m+2-j).
\]
Then \(w_{j+1}=F(j)/(4B)\). The polynomial \(F\) has zeros at \(j=-1,0,m+1,m+2\), and the Vandermonde convolution gives
\[
\sum_{j=1}^{m}F(j)=4\binom{m+4}{5}=4B.
\]
Thus \(\sum_iw_i=1\).

The interior principal block \(K\) of the Gram matrix \(L_n^2\), indexed by \(2,\ldots,n-1\), is Toeplitz with diagonal \(6\), first off-diagonal \(-4\), and second off-diagonal \(1\). Since \(F\) is a monic quartic,
\[
F(j-2)-4F(j-1)+6F(j)-4F(j+1)+F(j+2)=24.
\]
The four endpoint zeros allow this identity also at the first two and last two rows of \(K\), with the omitted terms interpreted as zero. Consequently
\[
Kw_{\mathrm{int}}=\alpha\mathbf1,\qquad\alpha=6/B.
\]
Let \(c=L_nw\). Directly,
\[
\|c\|^2=w_{\mathrm{int}}^{\mathsf T}Kw_{\mathrm{int}}=\alpha,
\qquad
\langle v_i,c\rangle=\alpha\quad(2\le i\le n-1).
\]
Every interior column has squared norm \(6\), so
\[
\|v_i-c\|^2=6-2\alpha+\alpha=6-\alpha=R_n^2
\qquad(2\le i\le n-1).
\]
At an endpoint, \(\|v_1\|^2=2\) and
\[
\langle v_1,c\rangle=-3w_2+w_3=-3(n-2)/B,
\]
with the reflected identity at the other endpoint. Hence the endpoint squared distance is \(2+6(n-1)/B\), and the stated clearance is \(4-6n/B\). It is zero at \(n=4\), and strictly positive for every \(n\ge5\): indeed, \(B/n=(n-2)(n-1)(n+1)(n+2)/120\) is strictly increasing for \(n\ge4\) and equals \(3/2\) at \(n=4\).

**Sharpness and uniqueness for arbitrary ball centers.** For any \(y\in H_n\), the weighted contact-point identity gives
\[
\sum_{i=2}^{n-1}w_i\|v_i-y\|^2
=\sum_{i=2}^{n-1}w_i\|v_i-c\|^2+\|y-c\|^2
=R_n^2+\|y-c\|^2.
\]
Therefore the maximum distance from \(y\) to the vertices is at least \(R_n\), with strict inequality if \(y\ne c\). The constructed center attains \(R_n\), since the endpoint distances are no larger; this proves minimality, uniqueness, the exact contact set, and the barycentric certificate.

Finally, \(w_i\) is a quartic in \(i\); taking its negative second difference \(c_i=2w_i-w_{i-1}-w_{i+1}\), with \(w_1=w_n=0\), gives the displayed quadratic center formula. The asymptotic follows from \(B\sim n^5/120\).

For \(n=3\), direct calculation with the three Laplacian columns yields the strictly positive optimal weights \((7/27,13/27,7/27)\), their center \((-2/9,4/9,-2/9)\), and common squared distance \(98/27\). The same weighted identity certifies the optimum and uniqueness.

## Verification
The standalone `check_path_ball.py` requires only the Python 3 standard library. It reconstructs the **full path Laplacian columns**, computes the proposed centers and all squared distances with exact rational arithmetic for every \(3\le n\le80\), verifies positivity and normalization of the weights, checks the exceptional \(n=3,4\) contact behavior, and confirms the exact endpoint clearance and quadratic center coordinates. It separately checks the integer quartic recurrence and its normalization for every \(4\le n\le1000\). Reproduce with `python check_path_ball.py`; the expected success tag is `PATH_LAPLACIAN_BALL_EXACT_PASS`. This finite replay supports but does not substitute for the unrestricted polynomial and weighted-distance proof above.

## Relationship to prior work
Braun and Meyer introduced Laplacian simplices, including the explicit path Laplacian matrix, and proved lattice-unimodular equivalence of all tree Laplacian simplices of fixed order (Proposition 4.1). Their focus is lattice/Ehrhart properties rather than the minimum Euclidean enclosing ball in the canonical embedding. Meyer and Pllaha extend their study through coding theory. Existing public analyses of canonical tree Laplacian simplices determine **inradii** and asymptotic normal-cone probabilities of endpoints, and an analysis of complete-bipartite Laplacian simplices determines a different two-class enclosing-ball transition. None of those inspected statements implies the evaluated path formula, the quartic positive support weights, or the all-order \(n=4\) endpoint-contact threshold. General simplex minimum-ball theory supplies the weighted optimality principle but not these path-specific values. See the references.

## Limitations
The theorem concerns unweighted paths only, in the canonical full-column Euclidean embedding. It does not classify minimum enclosing spheres for arbitrary trees, weighted paths, or alternative nonisometric embeddings. Historical priority under a different graph-Laplacian or discrete-biharmonic terminology is provisional; searches do not establish absolute novelty. The checker examines only finite orders, while the proof is algebraic for all orders. No independent mathematical audit has been performed.

## References
1. Benjamin Braun and Marie Meyer, *Laplacian Simplices*, arXiv:1706.07085v1, first public 2017-06-21, particularly Section 4 and Proposition 4.1.
2. Marie Meyer and Tefjol Pllaha, *Laplacian Simplices II: A Coding Theoretic Approach*, arXiv:1809.02960v1, first public 2018-09-09.
3. Andrew Vince, *A Simplex Contained in a Sphere*, *Journal of Geometry* (2008), DOI 10.1007/s00022-008-1907-5, for the general distinction between a vertex circumsphere and a minimum enclosing ball.
4. *Tree Laplacian simplices exhibit sharp, lattice-invisible Euclidean inradius exponents*, published mathematical research note, identifier `e122ee1ddbbf` (2026).
5. *Cubic suppression of endpoint normal cones in path Laplacian simplices*, published mathematical research note, identifier `3a5a32d6aa7c` (2026).
6. *Sharp vertex-contact transition for complete-bipartite Laplacian simplices*, published mathematical research note, identifier `ac6d13296de7` (2026).
