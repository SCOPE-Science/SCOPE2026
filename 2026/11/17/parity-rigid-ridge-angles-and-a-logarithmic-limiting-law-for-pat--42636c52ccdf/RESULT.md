# Parity-rigid ridge angles and a logarithmic limiting law for path-edge simplices

## Finding

Let \(Q_m\) be the unsigned edge polytope of the path on \(m+1\) vertices with its inherited Euclidean metric. Its exterior ridge-angle cosines have an exact rational Gram representation. Their signs alternate rigidly with the parity of facet indices, except for a single right angle when the number of path edges is odd. A uniformly chosen ridge has an explicit nonuniform limiting angle distribution, governed by the ratio of the two-point Dirichlet Green kernel.

Writing \(T=m+1\) and using the definitions in the next section, the exact answer is
\[
\boxed{\cos\phi_{ij}=\frac{H_{ij}}{\sqrt{H_{ii}H_{jj}}},\qquad 1\le i<j\le m.}
\]
For \(m=2k\), the numbers of acute, obtuse and right **exterior** angles are \(k(k-1),\ k^2,\ 0\). For \(m=2k+1\) they are \(k^2-1,\ k(k+1),\ 1\), with the only right angle between the two endpoint-labeled facets. Interior angles are the supplements of these exterior normal angles, so acute and obtuse counts reverse for interior angles.

If \(\Phi_m\) is a uniformly sampled exterior angle and \(Z\) denotes its limiting cosine, then \(Z=\varepsilon R\), where \(\varepsilon\) is a fair sign independent of \(R\), and
\[
\boxed{\Pr(R\le r)=\frac{2r^2[-\log(r^2)-1+r^2]}{(1-r^2)^2},\qquad 0<r<1.}
\]
The continuous extensions are \(0\) at \(r=0\) and \(1\) at \(r=1\). For instance \(\Pr(|Z|\le 1/2)=\frac{8}{9}(\log4-3/4)\approx0.56559\), different from the corresponding probability \(1/2\) for a uniform cosine.

## Assumptions and scope

Fix an integer \(m\ge3\). Let \(e_1,\ldots,e_{m+1}\) be the standard orthonormal basis of \(\mathbb R^{m+1}\), and let
\[
Q_m=\operatorname{conv}\{v_1,\ldots,v_m\},\qquad v_i=e_i+e_{i+1}.
\]
This is the *ordinary unsigned edge polytope*, not the centrally symmetric root polytope or the Laplacian simplex. Distances and angles are computed in its \((m-1)\)-dimensional affine hull using the metric inherited from \(\mathbb R^{m+1}\). Write \(F_i=\operatorname{conv}\{v_j:j\ne i\}\); each pair \(F_i,F_j\) meets in a ridge. The **exterior dihedral angle** \(\phi_{ij}\) is the ordinary angle between outward unit normals to their supporting hyperplanes inside this affine hull.

Define the following exact \(m\)-by-\(m\) matrix and vector, with \(T=m+1\):
\[
A_{ij}=(-1)^{i+j}\frac{\min(i,j)(T-\max(i,j))}{T},
\]
\[
b_i=\begin{cases}
1/2,&m\text{ odd and }i\text{ odd},\\
0,&m\text{ odd and }i\text{ even},\\
(T-i)/(2T),&m\text{ even and }i\text{ odd},\\
i/(2T),&m\text{ even and }i\text{ even},
\end{cases}
\qquad
 t=\begin{cases}T/4,&m\text{ odd},\\m(m+2)/(4T),&m\text{ even},\end{cases}
\]
and \(H_{ij}=A_{ij}-b_i b_j/t\). The formula in the finding specifies the cosine of every exterior angle, including repetitions if two indexed pairs have equal values.

## Proof

**The affine simplex and its normal Gram matrix.** The \((m+1)\)-by-\(m\) unsigned incidence matrix \(B\), with columns \(v_i\), has full column rank: a vanishing linear combination gives the first coefficient zero from row one and then all others recursively. Consequently the \(m\) vectors \(v_i\) are affinely independent. The vertex Gram matrix is
\[
G=B^{\mathsf T}B=\begin{pmatrix}
2&1&&\\1&2&\ddots&\\&\ddots&\ddots&1\\&&1&2
\end{pmatrix}.
\]
Conjugating \(G\) by the alternating sign diagonal gives the usual positive path Dirichlet tridiagonal matrix. Solving its second-difference boundary problem gives
\[
(G^{-1})_{ij}=(-1)^{i+j}\frac{\min(i,j)(m+1-\max(i,j))}{m+1}=A_{ij}.
\]
Set \(b=G^{-1}\mathbf1\), \(t=\mathbf1^{\mathsf T}G^{-1}\mathbf1\). The recurrence \(b_{i-1}+2b_i+b_{i+1}=1\) with \(b_0=b_{m+1}=0\) gives exactly the displayed formulas for \(b_i,t\).

The affine barycentric coordinate \(\lambda_i\) on \(\operatorname{aff}Q_m\) is characterized by \(\lambda_i(v_j)=\delta_{ij}\) and \(\sum_i\lambda_i=1\). Its tangent gradient can be chosen as
\[
g_i=BG^{-1}\left(e_i-\frac{b_i}{t}\mathbf1\right).
\]
For any tangent displacement \(B\delta\) with \(\mathbf1^{\mathsf T}\delta=0\), this satisfies \(\langle g_i,B\delta\rangle=\delta_i\), while \(g_i\) lies in the tangent space (it is orthogonal to \(BG^{-1}\mathbf1\)). Thus \(-g_i\) is an outward facet normal. Direct multiplication gives \(\langle g_i,g_j\rangle=A_{ij}-b_i b_j/t=H_{ij}\). The positive diagonal entries are squared norms of genuine nonzero facet gradients, proving the exact cosine formula.

**Sign classification.** Whenever \(i<j\) have opposite parity, \(A_{ij}<0\) and \(b_i b_j\ge0\), so \(H_{ij}<0\). For equal parity, \(A_{ij}>0\). If \(m\) is odd, the even-even cases have \(b_i=b_j=0\), while for odd-odd pairs
\[
H_{ij}=\frac{i(m+1-j)-1}{m+1},
\]
which is nonnegative and equals zero for distinct indices precisely at \((i,j)=(1,m)\). If \(m\) is even, for odd-odd pairs
\[
H_{ij}=\frac{(m+1-j)(i(m+1)-1)}{m(m+2)}>0,
\]
and for even-even pairs
\[
H_{ij}=\frac{i(m(m+2)-j(m+1))}{m(m+2)}>0.
\]
These signs classify every ridge. Counting equal- and opposite-parity unordered pairs gives the two formulas in the finding, after subtracting the one exceptional zero in odd \(m\).

**Scaling limit.** For indices \(i/m\to x\), \(j/m\to y\) with \(0<x<y<1\), the inverse Gram kernel and its diagonal satisfy
\[
A_{ij}=(-1)^{i+j}m x(1-y)+o(m),\quad
A_{ii}=m x(1-x)+o(m),\quad A_{jj}=m y(1-y)+o(m).
\]
Uniformly in \(i\), we have \(0\le b_i\le1/2\) and \(t\sim m/4\), so \(b_i b_j/t=O(m^{-1})\). Therefore, uniformly on compact subsets of the open triangle \(0<x<y<1\),
\[
\cos\phi_{ij}=(-1)^{i+j}
\sqrt{\frac{x(1-y)}{y(1-x)}}+o(1).
\]
As an unordered pair of distinct facet indices is sampled uniformly, \((i/m,j/m)\) converges to the ordered pair \((X,Y)\) of two independent \(\operatorname{Uniform}(0,1)\) variables. Each parity combination contributes asymptotically one quarter of all ordered index pairs; consequently \((-1)^{i+j}\) becomes an independent fair sign. Since the angle cosines are bounded, deleting arbitrarily narrow strips near the triangle boundary and diagonal does not affect weak convergence. It follows that
\[
\cos\Phi_m\xrightarrow{\mathrm d}\varepsilon
\sqrt{\frac{X(1-Y)}{Y(1-X)}}.
\]

**Closed distribution function.** Put \(a=r^2\in(0,1)\). On \(0<X<Y<1\), the inequality \(X(1-Y)\le aY(1-X)\) is exactly
\[
0<X\le\frac{aY}{1-(1-a)Y}.
\]
The joint density of ordered independent uniforms is \(2\) on this triangle. Hence
\[
\Pr(R\le r)=2\int_0^1\frac{a y}{1-(1-a)y}\,dy
=\frac{2a[-\log a-1+a]}{(1-a)^2},
\]
as asserted. The formula has the given continuous endpoint limits. This finishes the all-dimensional and asymptotic proofs.

## Verification

Run `python verify_path_angles.py` using Python, SymPy and NumPy. For every \(3\le m\le15\), the checker constructs the unsigned-incidence vertices and independently forms the affine difference-vertex Gram matrix, inverts it exactly, and compares its barycentric-gradient Gram to the closed formula. It tests every ridge sign and the precise parity count: 559 ridges across thirteen dimensions. At \(m=650\) it also compares finite angle-cosine distributions and the Dirichlet-kernel Riemann limit against five evaluations of the logarithmic CDF. This last check is numerical corroboration, not a convergence proof; the proof above is analytic. No indefinite certification is asserted.

## Relationship to prior work

Tran and Ziegler [1] define ordinary graph edge polytopes and explicitly note that tree edge polytopes are simplices; their results concern face structure, extremal face counts and combinatorial properties, not inherited Euclidean dihedral angles. Nagaoka and Tsuchiya [2] study the same edge-polytope realization, proving reflexive embedding and normality results; their dimension formula confirms the ambient setting but does not imply the angle spectrum or limit law. The classical inverse of a tridiagonal Dirichlet matrix is used as a proof ingredient, not claimed to be new.

For comparison, the ordinary unsigned edge simplex of an **odd cycle** has a known complete angle spectrum and a sine-law angle limit (uniform cosine). Those statements do not cover the **path** simplex: a path has one fewer edge and one additional independent affine constraint, and its limiting exterior cosine is the nonuniform signed kernel-ratio law derived here. A Laplacian simplex, a symmetric edge polytope, and a Schläfli orthoscheme use different Euclidean vertex realizations; a combinatorial or unimodular equivalence alone does not preserve dihedral angles. Targeted overlap searches did not locate a stronger result implying this indexed path formula. Historical priority remains subject to unindexed literature.

## Limitations

The formula concerns unsigned, unit-weight **paths** with at least three edges and angles in the inherited metric, uniformly sampled by unordered ridge rather than weighted by ridge measure. It does not claim a universal theorem for other trees, nonuniform edge weights, intrinsic volumes, an area-weighted angle law, or a quantitative rate of weak convergence. The asymptotic sign law and closed CDF are analytically proved; finite computations alone would not establish them. The literature comparison cannot guarantee historical novelty beyond inspected material.

## References

[1] T. Tran and G. M. Ziegler, *Extremal Edge Polytopes*, Electronic Journal of Combinatorics 21 (2014), P2.57; arXiv:1307.6708 (first public 2013-07-25), especially the introduction, Example 3, and the incidence-matrix dimension discussion. https://arxiv.org/abs/1307.6708

[2] T. Nagaoka and A. Tsuchiya, *Reflexive Polytopes Arising from Edge Polytopes*, Linear Algebra and its Applications 557 (2018), 438–454; arXiv:1712.06078v1 (first public 2017-12-17), especially §1 and the introduction. https://arxiv.org/abs/1712.06078

[3] Classical finite Dirichlet path Green-function inversion for the tridiagonal matrix with diagonal \(2\) and nearest-neighbor entries \(-1\) (rederived explicitly in the proof).
