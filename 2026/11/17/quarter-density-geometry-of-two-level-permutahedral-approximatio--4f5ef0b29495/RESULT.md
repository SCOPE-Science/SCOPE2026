# Quarter-density geometry of two-level permutahedral approximation

## Finding
For integers \(n\geq3\) and \(1\leq k<n\), define the standard permutahedron
\[
P_n=\operatorname{conv}\{\sigma(1,2,\ldots,n):\sigma\in S_n\},
\]
and the two-level multipermutahedron
\[
Q_{n,k}=\operatorname{conv}\{\sigma(L^k,U^{n-k}):\sigma\in S_n\},\qquad L=(k+1)/2,\quad U=(n+k+1)/2.
\]
Here exponents on \(L\) and \(U\) denote multiplicities, not powers. Then \(Q_{n,k}\subset P_n\), and its defining inequalities inside the common sum hyperplane are \(L\le y_i\le U\).

Let \(\lambda\) be the unique real solution to
\[
\sum_{i=1}^n \operatorname{clip}(i+\lambda,L,U)=\frac{n(n+1)}2,
\qquad \operatorname{clip}(t,L,U)=\min\{U,\max\{L,t\}\}.
\]
Set \(y_i=\operatorname{clip}(i+\lambda,L,U)\), \(q_i=i-y_i\), and let \(r=\#\{i:i+\lambda<L\}\), \(s=\#\{i:i+\lambda>U\}\), \(m=n-r-s\). The **exact Euclidean Hausdorff distance** satisfies
\[
d_H(P_n,Q_{n,k})^2=\sum_{i=1}^n q_i^2.
\]
In particular this is a finite, fully rational formula: \(\lambda\) is found by solving a piecewise-linear equation with breakpoints \(L-i\) and \(U-i\).

The **entire set of farthest points** in \(P_n\) is the disjoint union of exactly \(n!/m!\) exposed faces, each an \((m-1)\)-dimensional standard permutahedron: choose coordinate positions for each of the labels \(1,\ldots,r\) and \(n-s+1,\ldots,n\), lock those labels there, and freely permute the consecutive middle labels \(r+1,\ldots,n-s\) over the remaining \(m\) positions. Every point of each face, including its nonvertex points when \(m\ge2\), is farthest; all other points are strictly closer to \(Q_{n,k}\). The nearest point to any point in one such face is uniquely its translation by the corresponding permuted vector \(-q\).

When \(k=k_n\) and \(k_n/n\to\alpha\in[0,1]\), put \(\beta=\min\{\alpha,1-\alpha\}\). Then
\[
\lim_{n\to\infty}\frac{d_H(P_n,Q_{n,k_n})^2}{n^3}=\Phi(\beta),\quad
\Phi(\beta)=\begin{cases}
\dfrac{(1-\sqrt\beta)^3(1+3\sqrt\beta)}{12},&0\le\beta\le1/4,\\[5pt]
\dfrac7{96}-\dfrac{\beta(1-\beta)}4,&1/4\le\beta\le1/2.
\end{cases}
\]
The function \(\Phi\) is twice continuously differentiable across \(\beta=1/4\), but its third derivative jumps from \(-2\) to \(0\). For \(0<\alpha<1\), the common dimension of the farthest faces, divided by \(n\), converges to \(\min\{\sqrt\beta,1/2\}\): at quarter density, both lower and upper clipping become active, and farthest-face dimensions saturate at half the ambient dimension.

## Assumptions and scope
The realization is **the unscaled, standard-coordinate Euclidean metric** on the common affine hyperplane of coordinate sum \(n(n+1)/2\), with the ambient Euclidean norm restricted to this hyperplane. The faces in the farthest locus are genuine faces of \(P_n\). The statement does not optimize over rotations or affine transformations. The parameter \(n\) is an integer at least three; \(k\) is an integer strictly between zero and \(n\). The ratio limit is for any admissible integer sequence \(k_n\). The first-public lead concerns multipermutahedra and their structure, not the claimed metric law.

## Proof
**1. Nested orbit polytopes.** Average the first \(k\) entries of \((1,\dots,n)\) and separately the remaining \(n-k\) entries. This produces the two-valued vector \((L^k,U^{n-k})\), itself a convex combination of permutations of \((1,\dots,n)\). Permutation invariance gives \(Q_{n,k}\subset P_n\). The elementary uniform-matroid/base-polytope identity gives
\[
Q_{n,k}=\{y\in[L,U]^n:\sum_i y_i=n(n+1)/2\}.
\]
Indeed, writing \(y=L\mathbf1+(U-L)z\) gives \(0\le z_i\le1\), \(\sum_i z_i=n-k\), whose vertices are the binary vectors with exactly \(n-k\) ones.

**2. Projection and uniqueness.** For \(x=(1,\dots,n)\), minimize \(\sum_i(x_i-y_i)^2\) on the displayed capped-sum section. The Euclidean projection optimality condition is \(\langle x-y,v-y\rangle\le0\) for all feasible \(v\). The clipped vector \(y_i=\operatorname{clip}(x_i+\lambda,L,U)\) satisfies it: when \(y_i=L\), \(x_i-y_i\le-\lambda\) and \(v_i-y_i\ge0\); when \(y_i=U\), \(x_i-y_i\ge-\lambda\) and \(v_i-y_i\le0\); for uncapped coordinates the residual equals \(-\lambda\). Hence \(\langle x-y,v-y\rangle\le-\lambda\sum_i(v_i-y_i)=0\). Strict convexity makes \(y\) unique. The function \(f(t)=\sum_i\operatorname{clip}(i+t,L,U)\) is continuous and nondecreasing, and its target lies strictly between \(nL\) and \(nU\). It has exactly one solution: a constant interval at the target would force every coordinate to be at one of the two caps, with a jump of length \(U-L=n/2>1\) between two consecutive input labels, impossible. Breakpoints are rational, so \(\lambda\), \(y\), and the squared distance are rational.

**3. Maximum distance.** The distance to a closed convex set is convex. Therefore its maximum over \(P_n\) is realized at some vertex. By coordinate-permutation symmetry, all \(n!\) vertices have the same projection distance, namely \(\|q\|\). Hence this is exactly the directed distance from \(P_n\) to \(Q_{n,k}\), and because \(Q_{n,k}\subset P_n\) it equals their symmetric Hausdorff distance.

**4. Full farthest-point locus.** For any vertex \(v\) write \(p_v=\Pi_{Q_{n,k}}(v)\), \(u_v=v-p_v\). All these residuals are permutations of \(q\) and have squared norm \(D^2\). For any convex combination \(z=\sum_v t_vv\in P_n\), the point \(\sum_vt_vp_v\) lies in \(Q_{n,k}\), and
\[
\operatorname{dist}(z,Q_{n,k})^2\le\left\|\sum_vt_vu_v\right\|^2
=D^2-\sum_vt_v\left\|u_v-\sum_wt_wu_w\right\|^2.
\]
Equality with \(D^2\) therefore requires every positive-weight vertex to have the same residual. The entries of \(q\) are strictly increasing over the lower-clipped indices, constant \(-\lambda\) over the \(m\) middle indices, and strictly increasing over the upper-clipped indices; the three groups are also strictly ordered. Thus a residual determines the coordinate positions of each of the \(r+s\) extreme labels uniquely and allows precisely the \(m!\) permutations of the middle labels. The corresponding convex hull is an exposed face of \(P_n\) by the rearrangement inequality, and distinct choices give disjoint faces. Conversely, on any such face every vertex has the same residual \(u\); its convex combinations satisfy the same normal inequality after translating by \(-u\). Thus each of its points has distance \(D\) and unique nearest point \(z-u\), proving the classification, count, and dimension.

**5. Continuous-density limit.** By reflection of labels, the squared distance and \(m\) are invariant under \(k\leftrightarrow n-k\); assume \(k_n/n\to\beta\in(0,1/2]\). Normalize coordinates by \(n\), and write \(h=\lim\lambda/n\). The limiting balance equation is
\[
\int_0^1\operatorname{clip}(t+h,\beta/2,(1+\beta)/2)\,dt=1/2.
\]
For \(0<\beta\le1/4\) its unique solution is \(h=(1-\sqrt\beta)^2/2\): only the upper cap is active, beginning at \(t=\sqrt\beta\). For \(1/4\le\beta\le1/2\) the solution is \(h=(1-2\beta)/4\): lower and upper clipping begin at \(t=\beta-1/4\) and \(t=\beta+1/4\). Riemann-sum convergence and strict monotonicity near the limiting root justify convergence of the discrete shifts and the clipping proportions. Integrating the squared residual gives respectively
\[
\sqrt\beta\,h^2+\int_{\sqrt\beta}^1(t-(1+\beta)/2)^2dt
=\frac{(1-\sqrt\beta)^3(1+3\sqrt\beta)}{12}
\]
and
\[
\int_0^{\beta-1/4}(t-\beta/2)^2dt+\frac12h^2
+\int_{\beta+1/4}^1(t-(1+\beta)/2)^2dt
=\frac7{96}-\frac{\beta(1-\beta)}4.
\]
The middle coordinate fraction is the length of the unclipped interval, \(\sqrt\beta\) in the first regime and \(1/2\) in the second. If \(\beta=0\), the capped-sum constraint forces the average squared deviation of every normalized feasible vector from the constant \(1/2\) vector to tend to zero, because the rank or corank fraction tends to zero. Consequently the normalized squared distance converges to \(\int_0^1(t-1/2)^2dt=1/12=\Phi(0)\). In this endpoint regime the normalized clipping shift approaches \(1/2\) from below and the free-coordinate fraction tends to zero; this follows from the same balance equation because any positive-measure free interval would leave a strict deficit below its maximal mean \(1/2\). This also supplies the endpoint face-dimension limit. Direct differentiation shows matching first two derivatives and one-sided third derivatives \(-2\) and \(0\) at \(1/4\).

## Verification
The included `verify.py` uses exact rational arithmetic for all 299 integer pairs with \(3\le n\le25\); it tests KKT inequalities against random hypersimplex vertices, and enumerates all permutation residual classes for 20 cases with \(3\le n\le7\). Its asymptotic formula test spans \(n=200,400,800\), and 35 independent SciPy SLSQP quadratic programs verify the exact squared distances numerically with maximum reported error below \(4\cdot10^{-14}\). The script can be run with `python verify.py` and requires Python, NumPy, and SciPy. These tests do not substitute for the all-dimensional proof.

## Relationship to prior work
Manecke, Sanyal, and So study the combinatorial and monotone-path realization of multipermutahedra; in particular, their Theorem 4.3 concerns monotone-path polytopes, not Euclidean approximation between orbit polytopes. Wang and Lu already give the general capped-simplex projection algorithm and KKT clipping structure; these ingredients, including the finite projection step here, are not claimed as new. Ardila, Castillo, Eur, and Postnikov develop Coxeter/generalized permutahedral deformation theory, without the specific Hausdorff or farthest-locus result. The contribution here is the complete farthest-point locus, exact all-parameter geometric gap for the canonical two-level coarsening, and its quarter-density curvature and face-dimension transition.

## Limitations
The comparison is for the designated standard Euclidean realization and two-valued coarsening, not arbitrary multipermutahedra, arbitrary metrics, or the best approximation over rescalings. General projection algorithms imply the clipping certificate, so that component alone is not a novelty claim. The bibliographic comparison does not prove absolute priority; specialist results under alternative permutahedral-orbit or majorization terminology could exist. The theorem is a direct mathematical argument supported by finite checks; no independent audit is claimed.

## References
1. S. Manecke, R. Sanyal, J. So, *\(S\)-hypersimplices, pulling triangulations, and monotone paths*, arXiv:1812.07491 (first public 2018-12-18), especially Proposition 2.4 and Theorem 4.3. https://arxiv.org/abs/1812.07491
2. W. Wang, C. Lu, *Projection onto the capped simplex*, arXiv:1503.01002 (2015), Sections 1–3. https://arxiv.org/abs/1503.01002
3. F. Ardila, F. Castillo, C. Eur, A. Postnikov, *Coxeter submodular functions and deformations of Coxeter permutahedra*, arXiv:1904.11029 (2019). https://arxiv.org/abs/1904.11029
