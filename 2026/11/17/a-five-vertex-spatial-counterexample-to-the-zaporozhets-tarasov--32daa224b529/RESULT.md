# A five-vertex spatial counterexample to the Zaporozhets–Tarasov mean-distance inequality

## Finding

There is a three-dimensional convex polytope with only **five vertices**, all six facets triangular, for which the mean Euclidean distance between two independent volume-uniform points exceeds that between two independent surface-area-uniform points. An explicit choice is the convex hull \(K\) of
\[
(0,0,\varepsilon),\quad(0,0,-\varepsilon),\quad (L,-1,\varepsilon/3),\quad(L,1,\varepsilon/3),\quad(L,0,-\varepsilon/3),
\]
where \(L=1000\) and \(\varepsilon=1/100\). Writing \(\Delta(K)\) and \(\theta(K)\) for the two respective mean distances, the entirely rational certificate below proves
\[
\boxed{\Delta(K)-\theta(K)>\frac{31158}{4375}>7.12.}
\]
The previous explicit construction in the motivating source has six vertices. This assertion reduces that exhibited vertex count without claiming that five is the theoretical minimum among all counterexamples.

## Assumptions and scope

Distances are ambient Euclidean distances in \(\mathbb R^3\). Interior points are independent draws from normalized three-dimensional Lebesgue measure on \(K\); boundary points are independent draws from normalized two-dimensional Hausdorff measure on \(\partial K\), including all six triangular facets. Edges and vertices have zero surface probability. The five stated vertices are distinct and form a full-dimensional compact convex body. The result is an explicit counterexample, not a classification of all five-vertex polytopes, and it makes no assertion about tetrahedra.

## Proof

Write \(t=x_1/L\in[0,1]\), with transverse coordinates \((x_2,x_3)\). At \(t=0\) the section is the segment \(E=\{(0,z):|z|\le\varepsilon\}\); at \(t=1\) it is the triangle \(T=\operatorname{conv}\{(-1,\varepsilon/3),(1,\varepsilon/3),(0,-\varepsilon/3)\}\). Convexity makes every intermediate section exactly \((1-t)E+tT\). Its area is
\[
A(t)=4\varepsilon t(1-t)+\frac{2\varepsilon}{3}t^2=4\varepsilon t-\frac{10\varepsilon}{3}t^2.
\]
Integration over \([0,1]\) gives \(\int_0^1 A(t)\,dt=8\varepsilon/9\), so the normalized axial volume density and distribution function are
\[
p_I(t)=\frac92t-\frac{15}{4}t^2,\qquad F_I(t)=\frac94t^2-\frac54t^3.
\]
For any probability law on \([0,1]\) with distribution function \(F\), two independent draws satisfy the Gini identity \(\mathbb E|T_1-T_2|=2\int_0^1F(t)(1-F(t))\,dt\), including laws with endpoint atoms. Direct integration gives
\[
g_I=\mathbb E|T_1-T_2|=\frac{39}{140}.
\]

The following six triples of vertex indices, in the order displayed above beginning at index zero, are precisely the facets:
\[
(0,1,2),\ (0,1,3),\ (0,2,3),\ (1,2,4),\ (1,3,4),\ (2,3,4).
\]
For every triple, the other two vertices lie strictly on the same side of its plane (the exact determinant test is reproduced in `CHECK.py`). There are six distinct supporting triangular faces. A three-polytope with five vertices has at most \(2\cdot5-4=6\) facets, so these exhaust the boundary and all five points are extreme.

The two faces with two \(t=0\) vertices have aggregate area
\[
A_0=2\varepsilon\sqrt{L^2+1}.
\]
Their normalized axial density is \(2(1-t)\). The three faces with two \(t=1\) vertices have aggregate area
\[
A_1=\sqrt{L^2+4\varepsilon^2/9}+\sqrt{L^2(1+4\varepsilon^2/9)+4\varepsilon^2/9}.
\]
Their normalized axial density is \(2t\). The remaining triangular end face has area \(A_2=2\varepsilon/3\), producing a point mass at \(t=1\). Put \(S=A_0+A_1+A_2\), \(\alpha=2A_0/S\), and \(\beta=(A_1-A_0)/S\). The boundary axial CDF is therefore
\[
F_B(t)=\alpha t+\beta t^2\quad (0\le t<1),
\]
and the same Gini identity gives
\[
g_B=\alpha+\frac23\beta-\frac23\alpha^2-\alpha\beta-\frac25\beta^2.
\]

For \(L=1000\) and \(\varepsilon=1/100\), each of the three positive square roots appearing in \(A_0,A_1\) lies strictly between \(1000\) and \(1001\). This yields \(20<A_0<1001/50\), \(2000<A_1<2002\), and \(A_2=1/150\), hence the rational interval bounds
\[
\frac{19}{1000}<\alpha<\frac{21}{1000},\qquad \frac{979}{1000}<\beta<\frac{982}{1000}.
\]
Throughout this rectangle both partial derivatives of \(g(\alpha,\beta)\) are negative: \(1-4\alpha/3-\beta<0\) and \(2/3-\alpha-4\beta/5<0\). Consequently,
\[
g_B<g\left(\frac{19}{1000},\frac{979}{1000}\right)=\frac{1347243}{5000000}.
\]

Finally, every point has transverse coordinates inside \([-1,1]\times[-\varepsilon,\varepsilon]\), so their diameter is at most \(D=2\sqrt{1+\varepsilon^2}<2001/1000\). Projection onto the first coordinate and the Euclidean triangle inequality show, for any two independent points of either distribution,
\[
L\mathbb E|T_1-T_2|\le\mathbb E|Z_1-Z_2|\le L\mathbb E|T_1-T_2|+D.
\]
Thus
\[
\frac{\Delta(K)-\theta(K)}{L}>\frac{39}{140}-\frac{1347243}{5000000}-\frac{2001}{1000000}=\frac{15579}{2187500}>0.
\]
Multiplying by \(L=1000\) establishes the claimed strict rational margin. No numerical approximation is required for the proof.

## Verification

The standalone Python 3 script `CHECK.py` uses only the standard library and exact rational arithmetic. It checks noncoplanarity and all supporting-plane determinant signs for the six facets, the six doubled-area identities, the interior density normalization and Gini integral, the rational square-root bounds, the permissible \((\alpha,\beta)\) rectangle, monotonicity, and the final rational gap. Run `python3 CHECK.py`. Its successful result is `PASS` and the certified positive margin \(31158/4375\). The check is independent of Monte Carlo approximation, though it does not claim a formal proof assistant or independent human certification.

## Relationship to prior work

Eric Shen, *The Zaporozhets–Tarasov Conjecture on Mean Distances*, arXiv:2608.06470 (first posted 2026-08-06), proves the planar conjecture and gives an explicit **six-vertex** three-dimensional counterexample. The Gini identity and axial-stretch comparison employed here follow the approach in that paper (in particular its section 4); they are not claimed as new. The displayed five-vertex convex hull, its triangular-facet surface law, and its rational strict reversal certificate constitute the refinement. Existence of some counterexample in three dimensions was already settled, and is not claimed as new. Lotnikov's arXiv:2608.14848 treats centrally symmetric counterexamples (a full-dimensional centrally symmetric three-polytope cannot have five vertices); Tokmachev's arXiv:2607.08869 proves positive inequalities under additional centroid or tangency hypotheses. Neither statement directly gives the present explicitly certified five-vertex example.

## Limitations

This proof does not establish vertex-count minimality: whether a tetrahedron could reverse the first-moment inequality is not settled here. The construction uses an extremely stretched shape and yields a certified lower bound, not an exact closed form for either three-dimensional mean distance. A specialized earlier five-vertex example may exist outside the searched published and indexed literature. The originality assessment is provisional, and independent mathematical audit has not been performed.

## References

1. E. Shen, *The Zaporozhets–Tarasov Conjecture on Mean Distances*, arXiv:2608.06470, submitted 2026-08-06, https://arxiv.org/abs/2608.06470 ; full HTML https://arxiv.org/html/2608.06470v4 .
2. A. S. Lotnikov, *Mean distance between points inside and on the boundary of a convex body*, arXiv:2608.14848, 2026, https://arxiv.org/abs/2608.14848 .
3. A. S. Tokmachev, *Inequalities for convex functions of random points inside and on the boundary of convex bodies*, arXiv:2607.08869, 2026, https://arxiv.org/abs/2607.08869 .
