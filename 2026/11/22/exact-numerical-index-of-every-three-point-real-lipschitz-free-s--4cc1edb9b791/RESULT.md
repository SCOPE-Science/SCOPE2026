# Rank-one attainment of the numerical index on real hexagonal planes

## Finding

Every real Lipschitz-free space over a strict three-point metric triangle has a norm-one **rank-one** operator attaining its numerical index. Equivalently, the rank-one numerical index \(n_1(X)\) equals the ordinary numerical index \(n(X)\) for every real normed plane with a centrally symmetric hexagonal unit ball. On the edge-slope model there is a separate rank-one witness for each of the three sharp nonincident vertex-coordinate bounds, not just for the one that determines the ordinary index.

The ordinary numerical index for arbitrary three-point metrics, including the value \(1\) at triangle equality, was computed by Cobollo, Guirao and Montesinos [1]. The rank-one equality on the reflection-symmetric hexagon family associated with isosceles triangles was established by Chica and Merí [2]. The contribution here is the universal rank-one attainment and the per-coordinate witness construction.

## Assumptions and scope

For a real Banach space \(X\), the numerical radius of \(T\) is
\[
v(T)=\sup\{|x^*(Tx)|:\ \|x\|=\|x^*\|=x^*(x)=1\}.
\]
The ordinary numerical index infimizes \(v(T)\) over norm-one operators; the rank-one index restricts that infimum to rank-one operators. The theorem concerns real planes, not complex scalars or arbitrary polygonal unit balls. A strict triangle has positive side lengths \(w_1,w_2,w_3\), each strictly smaller than the sum of the other two.

## Proof

**Slope model and norming pairs.** In the dual of the free space, write a pointed Lipschitz potential in the coordinates of its oriented slopes on the cyclic edges. Summing the oriented increments gives
\[
X_w=\{z\in\mathbb R^3:\ \textstyle\sum_i w_i z_i=0\},\qquad \|z\|=\max_i|z_i|.
\]
Conversely the equation ensures the slopes integrate to a unique pointed potential. For each \(i\), let \(v_i\) be one of the two opposite vertices where the two other coordinates are saturated. Strictness gives exactly six vertices \(\pm v_i\): the two saturated coordinates have opposite signs (equal signs would force the third to have absolute value greater than one), and the missing coordinate has absolute value less than one. Write \(\phi_k(z)=z_k\). At each vertex the extreme normers are the two active signed coordinate functionals. For a fixed supporting functional the maximizing input may be taken at a vertex of its norming face, and then the maximizing normer may be taken extreme at that vertex. Thus
\[
\|T\|=\max_{i,k}|\phi_k(Tv_i)|,\qquad v(T)=\max_{i\ne k}|\phi_k(Tv_i)|.
\]

**Sharp nonincident bounds.** Fix \(i\), and let \(j,k\) be the other indices. The weighted-zero equation gives \(|\phi_i(Tv_i)|\le A_i v(T)\) for \(A_i=(w_j+w_k)/w_i\). Write \(v_i=\alpha v_j+\beta v_k\) and put \(B_i=|\alpha|+|\beta|\). Then \(|\phi_i(Tv_i)|\le B_i v(T)\), since both \(\phi_i(Tv_j)\) and \(\phi_i(Tv_k)\) are norming entries, up to sign. The scalar \(B_i\) does not depend on the choices of vertex signs. For example with \((w_1,w_2,w_3)=(a,b,c)\) choose
\[
v_1=(d,1,-1),\quad v_2=(-1,e,1),\quad v_3=(1,-1,(b-a)/c),\qquad d=(c-b)/a,\quad e=(a-c)/b.
\]
The first two coordinates give \(\alpha=(1+d)/(e-1)\) and \(\beta=(1+ed)/(e-1)\), both negative. Therefore \(B_1=1+(1+d)(1+e)/(1-e)\); cyclic relabeling gives
\[
B_i=1+\frac{(w_i+w_j-w_k)(w_i+w_k-w_j)}{w_i(w_j+w_k-w_i)}.
\]
Set \(R_i=\min(A_i,B_i)>1\). We have proved \(|\phi_i(Tv_i)|\le R_i v(T)\) for every \(T\) and \(\|T\|\le (\max_iR_i)v(T)\).

**Rank-one witnesses.** Define \(\eta\) on the basis \(v_j,v_k\) by
\[
\eta(v_j)=(R_i/B_i)\operatorname{sgn}(\alpha),\qquad
\eta(v_k)=(R_i/B_i)\operatorname{sgn}(\beta).
\]
Then \(\eta(v_i)=R_i\) and its absolute values on the other two vertices are at most one. Let \(u_i=1\) and \(u_j=u_k=-w_i/(w_j+w_k)\), so that \(u\in X_w\) and \(\|u\|=1\). The rank-one map \(Tz=\eta(z)u\) has all norming entries at \(v_j,v_k\) bounded in absolute value by one. The norming entries at \(v_i\) are bounded by \(R_i/A_i\le1\). Since \(\phi_i(Tv_i)=R_i\), the two bounds already established imply \(v(T)=1\). Its norm is \(R_i\), because the norm of \(\eta\) equals its maximum absolute value on the vertices. At a maximizing index, \(T/R_i\) is therefore a norm-one rank-one minimizer of the unrestricted numerical radius. Adjoint operators preserve norm, rank and numerical radius under finite-dimensional duality, proving the assertion for the free space.

**Equivalence with hexagonal planes.** For any real hexagonal unit ball, take the three distinct pairs of opposite facet functionals, normalized so the facets have values \(\pm1\). The norm is the maximum of the three absolute values, and two distinct functionals are linearly independent. The unique linear relation among all three therefore has nonzero coefficients. Reverse signs of individual coordinates to make the coefficients \(w_i\) positive. None of the bounds \(|z_i|\le1\) is redundant; hence \(w_i<w_j+w_k\), because the plane equation and the other two bounds would otherwise imply \(|z_i|\le1\). This identifies the plane isometrically with a model \(X_w\) as above. The triangle-equality case is not a hexagon; it is the known \(\ell_1^2\) free-space example of index one, where every norm-one rank-one operator trivially attains the index.

## Verification

The proof gives the complete two-dimensional witnesses and verifies their numerical radii and norms for every strict metric triangle, without approximation. The formulas for \(v_i\), \(\eta\) and \(u\) suffice for exact reproduction for rational metric data. The source package's rational witness diagnostic is supplementary to this analytic proof.

## Relationship to prior work

The formula \(1/\max_i R_i\) derived as part of this construction is an equivalent form of [1, Theorem 1.1], not a new ordinary index formula. Indeed sort the sides as \(p\ge q\ge r\). Write \(p=y+z,q=x+z,r=x+y\), where \(0<x\le y\le z\). Then \(B_r\le B_q\le B_p\) and \(A_r\ge A_q\ge A_p\). Also \(B_r\le A_q\) by \(x^2\le yz\), and \(A_p\le B_q\) by \(xy\le z^2\). Thus \(R_q\) maximizes the three ratios. The two branches of \(1/R_q\) are \(q/(p+r)\) and
\[
\frac{q(p+r-q)}{q(p+r-q)+(q+r-p)(p+q-r)}
=\frac{q(p+r-q)}{p(q+r-p)+r(p+q-r)},
\]
the two earlier branches. The attaining operators constructed in [1, Propositions 4.3–4.4] do not supply the rank-one refinement: on their two basis images, two of the evaluations are equal negative values on one image but positive and negative respectively on the other image. The images are consequently not collinear. This does not exclude additional minimizers. Chica and Merí [2, Theorem 1] give rank-one equality on a one-parameter reflection-symmetric subfamily; see [1, Corollaries 5.4–5.5] for its connection with the isosceles metrics. The separate sharp rank-one witnesses here require no such symmetry.

## Limitations

The construction establishes existence, not uniqueness or a classification of all extremizing operators. It is not an assertion about polygonal planes with more than six facets, where equality of the ordinary and rank-one indices can fail. The comparison is to the cited inspected literature and does not exclude unindexed equivalent work.

## References

1. C. Cobollo, A. J. Guirao and V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces*, arXiv:2304.13183, https://arxiv.org/abs/2304.13183.
2. M. Chica and J. Merí, *Rank-1 numerical index of some families of norms on the plane*, Linear and Multilinear Algebra 63 (2015), 1817–1828, https://doi.org/10.1080/03081087.2014.975670; author-hosted text: https://www.ugr.es/~jmeri/archivos/curriculum/pre-ChicaMeri-Rank1NumericalIndex.pdf.
