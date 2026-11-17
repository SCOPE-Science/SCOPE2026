# Outer-sphere contact transitions in shifted right-angle and Kozlov polytopes

## Finding

Fix integers \(n\ge2\) and \(r\ge1\), positive real numbers \(a_1,\ldots,a_n\), and nonnegative integer degree offsets \(d_1,\ldots,d_r\). Write
\[
v_k=(a_1,\ldots,a_k,0,\ldots,0)\in\mathbb R^n\quad(1\le k\le n),\qquad
S(a)=\operatorname{conv}\{v_1,\ldots,v_n\}.
\]
For \(d\ge0\), let \(\sigma^d\) prepend \(d\) zeros and pad all vectors to the same length \(N=n+\max_i d_i\). Consider the Euclidean Minkowski-sum polytope
\[
P(a;d_1,\ldots,d_r)=\sum_{i=1}^r\sigma^{d_i}S(a)\subseteq\mathbb R^N.
\]
Set \(L=\sum_i\sigma^{d_i}v_1\), \(U=\sum_i\sigma^{d_i}v_n\), and, for each \(i\), the integer-coordinate interval \(I_i=\{d_i+2,\ldots,d_i+n\}\). Form the overlap graph on \(\{1,\ldots,r\}\), joining indices whose intervals intersect. Its \(c\) connected components \(C_1,\ldots,C_c\) have corresponding interval unions \(J_\alpha=\bigcup_{i\in C_\alpha} I_i\), each a contiguous integer interval. Put \(\ell_\alpha=|J_\alpha|=n-1+\max_{i\in C_\alpha}d_i-\min_{i\in C_\alpha}d_i\).

**Theorem.** In the inherited Euclidean metric:

1. The exact diameter and the **unique** smallest enclosing ball are
\[
\operatorname{diam}(P)=\|U-L\|_2,
\qquad B_{\min}(P)=\overline B\left(\frac{L+U}{2},\frac{\|U-L\|_2}{2}\right).
\]
Equivalently, writing \(w_t=\sum_{i:\,2\le t-d_i\le n}a_{t-d_i}\),
\[
\operatorname{diam}(P)^2=\sum_{t=1}^{N}w_t^2.
\]
2. The enclosing sphere meets \(P\) at precisely
\[
\boxed{\prod_{\alpha=1}^{c}(\ell_\alpha+1)}
\]
vertices. They are exactly the coordinatewise corners of the box \([L,U]\) whose high/low assignments, restricted to each \(J_\alpha\), are a nonincreasing binary step sequence in increasing coordinate order.
3. The number of **unordered diametral vertex pairs** is exactly
\[
\boxed{2^{c-1}}.
\]
Their endpoints are those box corners whose assignments are constant on every \(J_\alpha\), paired with their complementary assignments. The contact and diametral-pair counts depend only on overlap of the shifted variable supports, not on the positive leg lengths.

For the Kozlov leg vector \(a_j=\binom nj\), these statements apply to the standard all-rank Kozlov-polytope realization, up to an isometric translation induced by the fixed degree-zero entries. With \(\binom uv=0\) for integers \(v<0\) or \(v>u\), define
\[
C_n(h)=\binom{2n}{n+h}-\binom nh-n\binom n{h+1}\qquad(h\ge0).
\]
Then its squared Euclidean diameter has the additional closed formula
\[
\boxed{\operatorname{diam}(P)^2=\sum_{i,j=1}^r C_n(|d_i-d_j|).}
\]
For two summands with degree gap \(s\), there is one diametral pair and \(n+s\) enclosing-sphere contact vertices when \(0\le s\le n-2\). At \(s\ge n-1\), there are **two** diametral pairs and \(n^2\) contact vertices. The contact count thus changes sharply at the precise disjointness threshold for the variable supports.

## Assumptions and scope

The metric is the ordinary Euclidean norm of the displayed coordinates, **not** a graph-edge metric, a lattice-invariant norm, or one obtained after normalizing the coordinates by the leg lengths. Every \(a_j\) is strictly positive; zero legs can collapse the variable support and invalidate the stated contact counts. Offsets are integer coordinate shifts and may repeat. The polytope need not be full-dimensional in \(\mathbb R^N\); its smallest enclosing ball is the ordinary ambient Euclidean ball, whose unique center lies in the affine hull.

The underlying right-angle simplices and their shifted Minkowski sums are the constructions of Snellman (2026), Definitions 36--37. The representation of Kozlov's \(f\)-vector simplex originates in Kozlov (1997); the identification of all-rank shifted sums with Kozlov polytopes is Snellman's Theorem 39. These representations are inputs, **not** new claims here.

## Proof

**Coordinatewise box.** Each \(v_k\) has \(v_1\le v_k\le v_n\) in every coordinate. This remains true for every point of \(S(a)\), and therefore
\[
L_t\le x_t\le U_t\qquad\text{for every }x\in P\text{ and }1\le t\le N.
\]
Both \(L\) and \(U\) belong to \(P\). Consequently any pair \(x,y\in P\) obeys
\[
\|x-y\|_2^2\le\sum_t(U_t-L_t)^2=\|U-L\|_2^2,
\]
with equality for \((L,U)\). Thus the diameter is exact.

**Minimum enclosing ball and its equality case.** For every \(x\in[L,U]\), the coordinate identity
\[
\left(x_t-\frac{L_t+U_t}{2}\right)^2
=\frac{(U_t-L_t)^2}{4}-(x_t-L_t)(U_t-x_t)
\]
gives containment in the ball centered at \((L+U)/2\) with radius \(\|U-L\|_2/2\). Because that ball contains the diametral points \(L,U\), no smaller ball is possible. Any radius-minimizing ball must have its center within distance \(\|U-L\|_2/2\) of both \(L\) and \(U\); the two closed balls of that radius meet only at their midpoint, giving uniqueness. Equality in the displayed coordinate identity after summing holds exactly when every coordinate with \(L_t<U_t\) equals either \(L_t\) or \(U_t\). Therefore contacts are precisely the box corners that lie in \(P\).

**Box-corner characterization.** Express a contact point as a sum \(x=\sum_i x^{(i)}\), with \(x^{(i)}\in\sigma^{d_i}S(a)\). At a coordinate \(t\) where the total equals its box minimum, each contributing summand must individually attain its minimum; likewise for the maximum. Since \(a_j>0\), the normalized variable coordinates of each summand on \(I_i\) are consequently all \(0\) or \(1\). On that interval a point of \(S(a)\) has normalized coordinate sequence
\[
(\lambda_2+\cdots+\lambda_n,\ \lambda_3+\cdots+\lambda_n,\ldots,\lambda_n),
\qquad \lambda_k\ge0,\quad\sum_{k=1}^n\lambda_k=1.
\]
This is nonincreasing. If it is binary, it must consist of an initial run of ones followed by zeros, which forces it to be a single vertex \(v_k\). If intervals overlap, a coordinate shared by two summands must have the same high/low status for both; by chaining the nonincreasing inequalities across overlapping intervals, the binary assignment is nonincreasing throughout their entire union \(J_\alpha\). Conversely, any nonincreasing binary assignment on each \(J_\alpha\) restricts to one of the allowed step patterns on every \(I_i\), hence can be realized by choosing an appropriate vertex in every summand. An integer interval of \(\ell\) coordinates admits precisely \(\ell+1\) such step sequences, and the components are independent. Hence the contact count is \(\prod_\alpha(\ell_\alpha+1)\). A box corner lying in a polytope is automatically a vertex because a nontrivial convex combination cannot preserve all its endpoint coordinates.

**Diameter multiplicity.** Equality in the coordinatewise diameter bound requires that in every nonconstant coordinate the two endpoints take opposite box values. Each endpoint must therefore be one of the just-classified contacts, and one contact's binary assignment is the coordinatewise complement of the other's. Both a binary sequence and its complement can be nonincreasing on \(J_\alpha\) only when that sequence is constant. There are two constant choices per overlap component and therefore \(2^c\) oriented endpoint assignments, paired into \(2^{c-1}\) unordered pairs.

**Kozlov autocorrelation.** For \(a_j=\binom nj\), the squared diameter expands as
\[
\sum_t\left(\sum_i\mathbf1_{2\le t-d_i\le n}\binom n{t-d_i}\right)^2
=\sum_{i,j}\sum_{k=2}^{n-|d_i-d_j|}\binom nk\binom n{k+|d_i-d_j|}.
\]
Vandermonde's identity evaluates the unrestricted \(k\ge0\) inner sum as \(\binom{2n}{n+h}\) for \(h=|d_i-d_j|\); removing the \(k=0\) and \(k=1\) terms subtracts \(\binom nh+n\binom n{h+1}\). This proves the displayed exact closed formula, including gaps beyond the support (where the result is zero). For two summands, the supports intersect exactly when \(s\le n-2\). If they intersect, their union is one interval of \(n-1+s\) coordinates. Otherwise they are two components, each of length \(n-1\), establishing the stated transition.

## Verification

The accompanying standalone file `verify_outer_shell.py` uses exact integer arithmetic. It separately enumerates **1,245** finite shifted Minkowski sums across dimensions \(2\le n\le6\), ranks \(1\le r\le3\), and three leg-vector families, and tests sphere containment, exact diameter, contact counts, pair multiplicities, and the coordinate-width formula. It also checks the binomial autocorrelation identity in every tested range through \(n=79\). The executed result was **11,278 exact assertions passed**. The finite tests are corroboration; the proof above establishes the theorem for all stated parameters.

## Relationship to prior work

Kozlov (1997, Theorem 4.1 and Section 5) determines the convex hull of simplicial-complex \(f\)-vectors by complete skeleta and a coordinate-normalized chain. Snellman (2026, Sections 5, 8 and 9) introduces general right-angle sums, identifies the shifted Kozlov polytopes, and studies their vertices/facets, resolving the rank-two vertex case while leaving more general finer structure open. Snellman's companion paper (2026) counts achievable Hilbert functions rather than the geometric contacts of their convex hull. The basic box-diameter bound and midpoint-ball argument are elementary and are not being claimed as new; the result here is the complete overlap-controlled classification of **all** outer-sphere contacts and diametral pairs for **all ranks**, together with the exact Kozlov autocorrelation diameter formula and its sharp support-disjointness transition.

## Limitations

No assertion is made about the full vertex or facet structure, inradius, or lattice points of these Minkowski sums. Only ordinary Euclidean diameter and smallest-enclosing-sphere geometry are classified. An earlier equivalent result in general orthoscheme or box-polytope language cannot be ruled out by the presently inspected literature; historical priority remains provisional. No independent mathematical audit has occurred.

## References

1. Jan Snellman, *Hilbert functions over the exterior algebra and f-vectors in higher rank I: Amata-Crupi monomial modules, Kozlov polytopes, and r-vectors of simplicial complexes*, arXiv:2609.23605, first public September 20, 2026. Sections 5, 8--10. https://arxiv.org/abs/2609.23605
2. Jan Snellman, *Hilbert functions over the exterior algebra and f-vectors in higher rank II: Generalizing Linusson's count to sumsets of f-vectors*, arXiv:2610.14985, first public October 10, 2026. https://arxiv.org/abs/2610.14985
3. Dmitry N. Kozlov, *Convex Hulls of f- and β-Vectors*, Discrete & Computational Geometry 18 (1997), 421--431, especially Sections 4--5. DOI:10.1007/PL00009326.
