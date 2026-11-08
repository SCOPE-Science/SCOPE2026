# Longest-path localization for sharp Sobolev evaluation on parallel-path metric graphs

## Finding

Consider a metric graph formed by joining two distinct vertices with \(r\ge3\) internally disjoint metric paths of respective lengths \(\ell_1,\ldots,\ell_r>0\), with no further edges. Define
\[
L=\sum_{i=1}^r\ell_i,\qquad a=\max_i\ell_i,\qquad S_3=\sum_{i=1}^r\ell_i^3.
\]
For real, continuous, edgewise \(H^1\) functions with zero (unnormalized) arclength integral, the *exact* pointwise energy inequality is
\[
\boxed{\|f\|_{L^\infty(G)}^2\le K(G)\sum_{i=1}^r\int_0^{\ell_i}|f_i'(t)|^2\,dt,\quad
 K(G)=\frac{S_3}{12L^2}+\frac{a(L-a)}{4L}.}
\]
Every nonzero equality function is proportional to the centered Kirchhoff Green representer of evaluation at the midpoint of a longest path. Conversely each such representer realizes equality. There are exactly as many maximizing evaluation points as there are longest paths, with distinct midpoints for \(r\ge3\).

For fixed total length \(L\) and fixed number \(r\ge3\) of positive-length paths, the complete sharp shape range is
\[
\boxed{\frac{L(3r-2)}{12r^2}\le K(G)<\frac L{12}.}
\]
The lower bound is attained *only* when all lengths equal \(L/r\). The upper bound is a supremum not attained in the positive-length class; it is approached when \(r-2\) paths collapse to zero length, leaving two positive-length parallel paths. In the two-path case \(r=2\) the graph is a circle, all evaluation points maximize, and \(K(G)=L/12\).

## Assumptions and scope

Edges are one-dimensional segments of arbitrary positive lengths, connected only at their common two endpoints. Edgewise arclength, not vertex weights, defines the zero-mean condition and the \(L^\infty\) norm. There are no vertex atoms, no density weights, and no other attached components. The function space is
\[
\mathcal H(G)=\left\{f\in C(G):f_i\in H^1(0,\ell_i),\ \sum_i\int_0^{\ell_i}f_i(t)\,dt=0\right\}
\]
with energy inner product \(\langle f,h\rangle_E=\sum_i\int f_i'h_i'\). This is a Hilbert space because its only zero-energy functions are constants and the mean condition removes them. The norm of the embedding \(\mathcal H(G)\hookrightarrow C(G)\) is \(\sqrt{K(G)}\), not \(K(G)\).

## Proof

**Orthogonal splitting.** Orient each path from common vertex \(A\) to common vertex \(B\). For \(f\in\mathcal H(G)\), write \(d=f(B)-f(A)\), and uniquely express
\[
f_i(t)=u+\frac{dt}{\ell_i}+h_i(t),\qquad h_i\in H^1_0(0,\ell_i).
\]
Put \(C=\sum_j1/\ell_j\). Integration of the cross term using the zero boundary values of \(h_i\) yields
\[
\|f\|_E^2=Cd^2+\sum_j\|h_j'\|_2^2.
\]
The arclength mean of the affine part is \(u+d/2\), so the mean-zero evaluation functional at coordinate \(s\) on the \(i\)-th path is
\[
f_i(s)=d\left(\frac{s}{\ell_i}-\frac12\right)
 +h_i(s)-\frac1L\sum_j\int_0^{\ell_j}h_j(t)\,dt.
\]

**Evaluation representers.** On \(H^1_0(0,\ell_j)\) with derivative energy, the evaluation kernel is the Dirichlet Green function
\[
g_j(t,u)=\min(t,u)-\frac{tu}{\ell_j},
\quad g_j(s,s)=\frac{s(\ell_j-s)}{\ell_j}.
\]
The integral functional has representer \(q_j(t)=t(\ell_j-t)/2\), satisfying \(\|q_j\|_E^2=\ell_j^3/12\) and \(\langle g_j(\cdot,s),q_j\rangle_E=s(\ell_j-s)/2\). By the Pythagorean decomposition across the scalar \(d\) and the Dirichlet spaces, the squared norm of evaluation at \(s\in[0,\ell_i]\) is therefore exactly
\[
\begin{aligned}
K_i(s)&=\frac{S_3}{12L^2}
 +\frac{(s/\ell_i-1/2)^2}{C}
 +s(\ell_i-s)\left(\frac1{\ell_i}-\frac1L\right)\\
&=\frac{S_3}{12L^2}+\frac1{4C}
 +s(\ell_i-s)\left(\frac1{\ell_i}-\frac1L-\frac1{C\ell_i^2}\right).
\end{aligned}
\]
This is an identity for every point, including vertices and boundary values, not merely an upper bound.

**Strict localization and path-length comparison.** Write \(T_i=\sum_{j\ne i}1/\ell_j\). The coefficient of \(s(\ell_i-s)\) is
\[
\beta_i=\frac{(L-\ell_i)T_i-1}{L(1+\ell_i T_i)}.
\]
Cauchy--Schwarz yields \((L-\ell_i)T_i\ge(r-1)^2>1\). Thus \(\beta_i>0\) for \(r\ge3\): on each path its unique maximal point is the midpoint. Substitution cancels the conductance term:
\[
K_i(\ell_i/2)=\frac{S_3}{12L^2}+\frac{\ell_i(L-\ell_i)}{4L}.
\]
For distinct paths \(i,j\), their midpoint values differ by
\[
\frac{(\ell_i-\ell_j)(L-\ell_i-\ell_j)}{4L}.
\]
The second factor is strictly positive for \(r\ge3\); hence exactly the longest paths maximize. Boundedness and sharpness follow from Riesz representation and equality in Cauchy--Schwarz. Each nonzero optimizer is proportional to a representer at some maximizing evaluation point, with either sign allowed. Conversely every such representer attains the sharp inequality. For \(r=2\), \(\beta_i=0\) and the expression simplifies to \(L/12\) everywhere, as it must on a circle.

**Sharp optimization over lengths.** Put \(x=a/L\), where \(x\in[1/r,1)\). By strict convexity of the cube and Jensen's inequality,
\[
\frac{K(G)}L\ge\Phi_r(x):=\frac{x^3+(1-x)^3/(r-1)^2}{12}+\frac{x(1-x)}4,
\quad \Phi_r'(x)=\frac{r(r-2)(1-x)^2}{4(r-1)^2}>0.
\]
It follows that \(K(G)\ge L(3r-2)/(12r^2)\), and equality forces all path lengths to be \(L/r\). For the opposite direction, since at least two of the paths other than a longest one are positive,
\[
S_3<a^3+(L-a)^3;
\]
therefore
\[
12L^2K(G)<a^3+(L-a)^3+3La(L-a)=L^3.
\]
Collapsing all but two positive paths to length zero while holding total length fixed gives the stated sharp unattained supremum.

## Verification

The standalone Python file `theta_exact_check.py` uses only the standard-library exact rational type. It independently constructs the zero-mean solution of \(-g''=\delta_x-1/L\) with Kirchhoff conditions, compares \(g(x)\) to \(\int|g'|^2\) and the analytical kernel, checks arbitrary rational path-position examples, and verifies the shape and midpoint inequalities for finite families. Execute `python theta_exact_check.py` from a directory containing that file. The proof above, not any finite enumeration, establishes the theorem for all positive real lengths and all \(r\ge3\).

For a second direct reconstruction at a point \(s\) of path \(i\), set \(d=(s/\ell_i-1/2)/C\) and
\[
b_j=\frac d{\ell_j}-\frac{\ell_j}{2L}
 +\mathbf1_{j=i}\frac{\ell_i-s}{\ell_i},
\quad G_j(t)=A+b_jt+\frac{t^2}{2L}-\mathbf1_{j=i}(t-s)_+,
\]
where the unique scalar \(A\) makes the total arclength integral of \(G\) vanish. These functions meet at both common vertices, have zero total outgoing Kirchhoff derivative there, and satisfy the required distributional equation. Thus \(\int |G'|^2=G_i(s)=K_i(s)\). This independent differential construction matches the orthogonal decomposition.

## Relationship to prior work

Solomyak's work on metric-graph Sobolev approximation (arXiv:math/0206235, first posted 23 June 2002) establishes general graph approximation and embedding estimates using graph partitions, but does not state a length-resolved sharp point-evaluation constant or the longest-path localization on parallel-path graphs. Usman's *Sobolev type inequalities for compact metric graphs* (2018, DOI 10.1186/s13660-018-1872-y) develops isoperimetric Sobolev and Cheeger inequalities, rather than the exact mean-zero \(H^1\)-to-\(C\) embedding. Kennedy, Kurasov, Léna and Mugnolo's *A theory of spectral partitions of metric graphs* (2021, DOI 10.1007/s00526-021-01966-y) studies pumpkin graphs for Laplacian spectral-partition energies, a different functional. Standard Green-representer and Dirichlet interval identities are used, not presented as novel.

The distinct contribution is the exact all-length formula, strict midpoint-longest-path optimizer classification, and sharp fixed-total-length shape extrema. Full-text access to every potentially related pre-2016 result was not possible, so equivalent unindexed prior coverage remains a scientific originality risk.

## Limitations

No assertion is made for vertex-mass measures, unequal arclength densities, extra trees or loops, nonlinear \(p\)-energy, or higher-order Sobolev spaces. The formula is for mean-zero functions with *unnormalized derivative energy*: replacing energy by normalized arclength energy changes the numerical constant. For \(r=2\), every point is norming; the strict localization statement requires at least three positive-length paths. Finite verification is corroborative rather than an infinite proof.

## References

1. M. Solomyak, *On approximation of functions from Sobolev spaces on metric graphs*, arXiv:math/0206235v1, 23 June 2002, https://arxiv.org/abs/math/0206235.
2. M. Usman, *Sobolev type inequalities for compact metric graphs*, Journal of Inequalities and Applications 2018, article 271, https://doi.org/10.1186/s13660-018-1872-y.
3. J. B. Kennedy, P. Kurasov, C. Léna and D. Mugnolo, *A theory of spectral partitions of metric graphs*, Calculus of Variations and Partial Differential Equations 60 (2021), article 61, https://doi.org/10.1007/s00526-021-01966-y.
