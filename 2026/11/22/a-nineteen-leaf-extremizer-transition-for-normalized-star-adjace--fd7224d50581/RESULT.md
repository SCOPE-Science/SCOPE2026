# A nineteen-leaf extremizer transition for normalized star adjacency

## Finding

Fix an integer \(m\ge1\) and a lower conductance bound \(a>0\). Let \(G_w\) be the undirected weighted star with hub \(0\), leaves \(1,\ldots,m\), and positive hub–leaf conductances \(w=(w_1,\ldots,w_m)\in[a,\infty)^m\). Write \(A_w\) for its weighted adjacency matrix and \(D_w\) for its degree matrix. Its symmetric degree-normalized adjacency operator is
\[
N(w)=D_w^{-1/2}A_wD_w^{-1/2}.
\]
Give conductance vectors the coordinate supremum norm and matrices the maximum absolute entry norm, both denoted \(\|\cdot\|_{\max}\). Define the optimal global two-input coefficient
\[
L_m(a)=\sup_{\substack{w,v\in[a,\infty)^m\\w\ne v}}
\frac{\|N(w)-N(v)\|_{\max}}{\|w-v\|_{\max}}.
\]
Then \(L_1(a)=0\). For every \(m\ge2\), the exact answer is
\[
\boxed{L_m(a)=\begin{cases}
\dfrac{m-1}{a\,m^{3/2}},&2\le m\le18,\\[5pt]
\dfrac{(m-1)(1+r_m)}{2a\sqrt{r_m}\,(r_m+m-1)^{3/2}},&m\ge19,
\end{cases}}
\qquad
r_m=\frac{m-5+\sqrt{m^2-18m+33}}4.
\]
The sharp derivative is approached near the uniform lower-bound conductance vector for \(2\le m\le18\). Starting at exactly \(m=19\), its optimizing conductance profile has one exceptional spoke of weight \(a r_m>a\) and all other spokes at \(a\). In every case the lower-bound coordinates can be approached from the interior, so this derivative optimization supplies the sharp global two-input coefficient. Moreover,
\[
\boxed{\lim_{m\to\infty}aL_m(a)=\frac1{3\sqrt3}},
\qquad \lim_{m\to\infty}\frac{r_m}{m}=\frac12.
\]
Thus degree-normalized star adjacency retains nonvanishing maximum-entry sensitivity as its degree grows, if one spoke may be asymptotically half as strong as the total baseline conductance of the other spokes. The comparison is for fixed labelled stars, not graphs compared modulo vertex relabelling.

## Assumptions and scope

The graph has exactly \(m+1\) vertices and no loops or leaf–leaf edges; every conductance is an independently variable real number bounded below by \(a>0\), with no upper bound. All degrees are therefore positive. The output is the entire real symmetric normalized adjacency matrix, not a filtered signal or an eigenvector. Both input and output deviations use unweighted entrywise maximum norms. The coefficient is a global two-input supremum; it need not be attained by a pair of distinct conductance vectors. The first-public motivating work is Levie–Isufi–Kutyniok, arXiv:1901.10524, first submitted 2019-01-29.

## Proof

**1. Exact normalized representation.** Put \(W=\sum_{j=1}^m w_j\), and \(u_i=\sqrt{w_i/W}\). Because the hub degree is \(W\) and the \(i\)-th leaf degree is \(w_i\), the only nonzero entries of \(N(w)\) are \(N(w)_{0i}=N(w)_{i0}=u_i\). Hence its maximum-entry difference norm equals \(\max_i|u_i(w)-u_i(v)|\). When \(m=1\), \(u_1\equiv1\).

**2. Exact Jacobian norm.** For \(m\ge2\), direct differentiation yields
\[
\frac{\partial u_i}{\partial w_i}=\frac{W-w_i}{2\sqrt{w_i}\,W^{3/2}},\qquad
\frac{\partial u_i}{\partial w_j}=-\frac{\sqrt{w_i}}{2W^{3/2}}\quad(j\ne i).
\]
The induced maximum-to-maximum norm is the largest absolute row sum. Thus
\[
\|DN(w)\|_{\max\to\max}=
\max_i\frac{W+(m-2)w_i}{2\sqrt{w_i}\,W^{3/2}}.
\]
For fixed \(x=w_i>0\), write \(S=\sum_{j\ne i}w_j\). The row sum is \([S+(m-1)x]/[2\sqrt{x}(x+S)^{3/2}]\). Its derivative in \(S\) has the sign of \((5-3m)x-S\), which is strictly negative for every \(m\ge2\). Consequently, all other weights may be set to their minimum \(a\) in searching for the supremum. With \(z=x/a\ge1\), the problem is exactly
\[
L_m(a)=\frac1a\max_{z\ge1}g_m(z),\qquad
 g_m(z)=\frac{(m-1)(z+1)}{2\sqrt z\,(z+m-1)^{3/2}}.
\]
For completeness, the equality between the global two-input coefficient and the supremum of the Jacobian norm follows by integrating the derivative along every segment in the convex domain, then recovering each row sum as a directional derivative at interior points. Every boundary candidate has interior approximants; sign choices of the conductance direction attain each absolute Jacobian row sum in the interior limit.

**3. Sharp integer boundary.** Define \(F_m(z)=g_m(z)/g_m(1)\). Since \(g_m(1)=(m-1)/m^{3/2}\),
\[
F_m(z)^2=\frac{m^3(z+1)^2}{4z(z+m-1)^3},\qquad
\frac{\partial}{\partial m}\log F_m(z)=\frac32\left(\frac1m-\frac1{z+m-1}\right)\ge0
\]
for \(z\ge1\). At \(m=18\), the comparison with one is certified by the exact factorization
\[
4z(z+17)^3-18^3(z+1)^2
=4(z-1)\bigl(z^3+52z^2-539z+1458\bigr).
\]
The cubic is strictly positive on \(z\ge1\), as shown by the identity
\[
z^3+52z^2-539z+1458
=(z-19/4)^2(z+123/2)+(363/16)z+2253/32.
\]
Thus \(F_{18}(z)\le1\) for all \(z\ge1\); monotonicity in \(m\) gives \(F_m(z)\le1\) for every integer \(2\le m\le18\).

At \(m=19\), choosing \(z=4\) reverses this inequality: exactly
\[
4\cdot4\cdot(4+18)^3-19^3(4+1)^2=-1107<0,
\]
so \(F_{19}(4)>1\). Strict monotonicity of \(F_m(4)\) in \(m\) proves \(F_m(4)>1\) for all \(m\ge19\). For these integers, logarithmic differentiation gives
\[
\frac{g_m'(z)}{g_m(z)}
=-\frac{2z^2+(5-m)z+(m-1)}{2z(z+1)(z+m-1)}.
\]
The two roots of the numerator lie strictly above one, and the larger is \(r_m\). Therefore the only possible global maximizers on \([1,\infty)\) are \(1\) and \(r_m\). The strict witness \(F_m(4)>1\) excludes \(1\), so \(r_m\) is the unique maximizer for \(m\ge19\). This proves both branches of the sharp formula.

**4. Large-star limit.** The radical expression gives \(r_m/m\to1/2\). Substitute this scaling into the exact second branch to obtain \(aL_m(a)\to(3\sqrt3)^{-1}\). This limit is positive: replacing the exceptional spoke by a uniformly bounded one would miss the asymptotically sharp regime.

## Verification

Run the accompanying standalone script from the same directory with `python3 check_normalized_star.py`. It checks the exact rational \(m=18\) certificate and the \(m=19\) strict witness, numerical maximizer profiles, random differential row-sum bounds, finite-difference derivatives and global finite-pair Lipschitz inequalities. On its reference execution the script printed `PASS 14202 supplementary checks`. These finite computations support implementation accuracy and examples; the universal quantifiers, threshold, and limit rely on the proof above.

## Relationship to prior work

Levie–Isufi–Kutyniok (2019) studies stability of spectral graph filters under a perturbation of their graph shift matrices, including normalized Laplacians (their Theorem 2 and normalized ChebNet discussion). Gama–Bruna–Ribeiro (2019) gives filter perturbation inequalities in spectral norms and describes absolute versus relative perturbations (Theorem 1 and Appendix B). These works motivate graph-shift robustness but do not yield the exact conductance-to-normalized-adjacency coefficient or the change of optimizer at nineteen leaves. Geisler–Kosmala–Herbst–Günnemann, *Spatio-Spectral Graph Neural Networks* (NeurIPS 2024), discusses Lipschitz degree normalization under simultaneously upper- and lower-bounded degrees, whereas the present class permits an unbounded hub degree and computes a sharp endpoint coefficient; only the relevant extracted text, not a complete visual inspection, was available for this third comparison. Closely ranked published findings about heat gradients, Hodge projections and star conductance optimization concern different operators or norm/perturbation variables. Such distinctions are by actual claim implication, not merely terminology.

## Limitations

This is a result for a star's degree-normalized adjacency matrix. It does not give a sharp coefficient for arbitrary graphs, for arbitrary functional-calculus filters of this matrix, or for the combinatorial Laplacian. Edge weights must have a strictly positive common floor; the result does not extend uniformly to conductances approaching zero. The sharp constant is a supremum, established by local derivatives, not a claim that a finite nonzero perturbation pair attains it. Similar formulas in unindexed specialized normalization literature cannot be categorically ruled out without external priority assessment. Independent mathematical audit has not been performed.

## References

1. R. Levie, E. Isufi, and G. Kutyniok, *On the Transferability of Spectral Graph Filters*, arXiv:1901.10524, initially posted 2019-01-29. https://arxiv.org/abs/1901.10524
2. F. Gama, J. Bruna, and A. Ribeiro, *Stability Properties of Graph Neural Networks*, arXiv:1905.04497, initially posted 2019-05-11. https://arxiv.org/abs/1905.04497
3. S. Geisler, A. Kosmala, D. Herbst, and S. Günnemann, *Spatio-Spectral Graph Neural Networks*, NeurIPS 2024. https://openreview.net/pdf/3a46231cf042909d550605fa8da48926f0cf53e3.pdf
