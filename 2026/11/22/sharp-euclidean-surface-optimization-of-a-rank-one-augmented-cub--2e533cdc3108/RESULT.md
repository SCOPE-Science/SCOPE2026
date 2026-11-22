# Sharp Euclidean surface optimization of a rank-one augmented cube

## Finding
For every integer \(n\ge2\) and real \(t>0\), define the standard Euclidean rank-one-augmented cube
\[
P_n(t)=[0,1]^n+t\Delta_n,\qquad \Delta_n=\operatorname{conv}\{0,e_1,\ldots,e_n\}.
\]
This is the independence polytope of the submodular rank function \(r_t(\varnothing)=0\), \(r_t(S)=|S|+t\) for nonempty \(S\subseteq[n]\). Its exact volume and ordinary Euclidean surface area are
\[
V_n(t)=\sum_{k=0}^n\binom nk\frac{t^k}{k!},\qquad
S_n(t)=nV_{n-1}(t)+\sum_{k=1}^n\binom nk\frac{\sqrt{k}\,t^{k-1}}{(k-1)!}.
\]
Its complete facet system consists of \(n\) coordinate facets, each of area \(V_{n-1}(t)\), and \(\binom nk\) subset facets of size \(k\), each of area \(\sqrt{k}t^{k-1}/(k-1)!\). The total number is \(2^n+n-1\).

**Sharp three-dimensional metric consequence.** Among all positive dilations of the bodies \(P_3(t)\), with arbitrary \(t\ge0\), and with volume fixed to one, there is exactly **one** minimizing shape parameter \(t=t_*\), with
\[
t_*=0.428630637733420\ldots,\qquad
\frac{S_3(t_*)}{V_3(t_*)^{2/3}}=5.762637024562116\ldots .
\]
Exactly, \(t_*\) is the unique positive root of
\[
\begin{aligned}
F(t)={}&9(\sqrt2-2)+(-9+3\sqrt3+9\sqrt2)t\\
&+(3+6\sqrt3-\tfrac92\sqrt2)t^2
+\tfrac32(1+\sqrt3-\sqrt2)t^3.
\end{aligned}
\]
The surface-area inequality \(S_3(t)/V_3(t)^{2/3}\ge S_3(t_*)/V_3(t_*)^{2/3}\) is strict except at \(t=t_*\). This supplies a sharp, nontrivial interpolation optimum between the cube at \(t=0\) and the simplex limit \(t\to\infty\).

## Assumptions and scope
All volumes are standard ambient \(n\)-dimensional Lebesgue volumes, all facet areas are \((n-1)\)-dimensional Euclidean Hausdorff measures, and \(n\ge2\). Facet formulas require \(t>0\); at \(t=0\), some subset inequalities coalesce and only the cube remains, although the volume and surface-area formulas continue by limits. For the three-dimensional minimization, every body is homothetically rescaled to unit volume, so only its shape parameter \(t\) varies. No assertion is made about all convex bodies, all Minkowski combinations, or the location of the surface-minimizing parameter in higher dimensions.

## Proof
**1. Exact irredundant inequalities.** For any nonnegative vector \(x\), set \((a)_+=\max(a,0)\). Splitting each coordinate into the unit-cube part \(\min(x_i,1)\) and simplex part \((x_i-1)_+\) proves the exact identity
\[
P_n(t)=\{x\in\mathbb R^n:x_i\ge0\ \forall i,\ \sum_i(x_i-1)_+\le t\}.
\]
Because \(\sum_i(x_i-1)_+=\max_{S\subseteq[n]}\sum_{i\in S}(x_i-1)\), an equivalent linear description is \(x_i\ge0\) together with \(\sum_{i\in S}x_i\le |S|+t\) for each nonempty \(S\subseteq[n]\). All are facets when \(t>0\): the face \(x_i=0\) is a copy of \(P_{n-1}(t)\), and the exposed face for a subset \(S\) of size \(k\) is
\[
\bigl(\mathbf1_S+t\operatorname{conv}\{e_i:i\in S\}\bigr)\times[0,1]^{[n]\setminus S},
\]
with coordinates understood in their respective orthogonal subspaces. Indeed, equality for \(S\) forces each \(x_i\ge1\) on \(S\), by the inequalities for \(S\setminus\{i\}\), and forces \(x_j\le1\) off \(S\), by the inequality for \(S\cup\{j\}\). Each listed face has dimension \(n-1\), establishing irredundancy and exhaustion.

**2. Exact Euclidean measures.** Partition \(P_n(t)\), up to measure-zero coordinate walls, according to the support \(T=\{i:x_i>1\}\). When \(|T|=k\), the excess coordinates form a nonnegative \(k\)-simplex of volume \(t^k/k!\), while all other coordinates range independently over intervals of length one. Summing over supports gives \(V_n(t)\). Each lower coordinate facet has \((n-1)\)-area \(V_{n-1}(t)\). For a nonempty subset \(S\) of size \(k\), the simplex \(t\operatorname{conv}\{e_i:i\in S\}\) has \((k-1)\)-area \(\sqrt{k}t^{k-1}/(k-1)!\), since the Gram matrix of its edge vectors is \(t^2(I_{k-1}+\mathbf1\mathbf1^{\mathsf T})\) and has determinant \(kt^{2k-2}\). Its Cartesian product with an orthogonal unit cube of dimension \(n-k\) preserves this area. Counting and adding gives the stated spectrum and \(S_n(t)\).

**3. Sharp three-dimensional optimization.** Substituting \(n=3\) yields
\[
V_3(t)=1+3t+\tfrac32t^2+\tfrac16t^3,\qquad
S_3(t)=6+(6+3\sqrt2)t+\tfrac12(3+\sqrt3)t^2.
\]
The surface of the volume-one representative is \(Q(t)=S_3(t)/V_3(t)^{2/3}\). Because \(V_3(t)>0\), the derivative \(Q'(t)\) has the sign of \(3S'_3(t)V_3(t)-2S_3(t)V'_3(t)=F(t)\). Its constant coefficient \(9(\sqrt2-2)\) is strictly negative, while all three remaining coefficients in the displayed formula for \(F\) are strictly positive. Descartes' rule of signs gives at most one positive root, and the change from negative at zero to positive at infinity gives at least one. Hence \(Q\) strictly decreases to that root and strictly increases afterwards, proving existence, uniqueness, and the sharp equality statement. The numerical values result from the displayed cubic, not from finite experiments used as proofs.

## Verification
The standalone \(\texttt{verify.py}\) enumerates vertices as sums of cube and simplex vertices and independently invokes the Euclidean convex-hull algorithm in dimensions \(2,3,4,5\), at three positive parameter values. It compares the hull volume and boundary area with the claimed closed formulas. It also checks every proposed subset-facet supporting inequality and full affine facet rank through dimension five. Symbolic computation checks the derivative cubic and its coefficient signs, while bracketed numerical root-finding checks the displayed optimizer and surface quotient. These finite checks support the algebra; the general proof is Steps 1–3, not the finite tests.

## Relationship to prior work
Castillo, Doolittle, Goeckner, Ross, and Ying, *Minkowski summands of cubes* (arXiv:2009.07252, first public September 15, 2020), study type cones and the Minkowski-summand classification of products of simplices. This does not determine ordinary Euclidean boundary area of the **sum** of a cube and a simplex, nor the sharp mixed-shape isoperimetric optimizer; a summand of a cube has only cube edge directions, whereas this sum develops simplex edge directions. Richter and Saorín Gómez, *On the Monotonicity of the Isoperimetric Quotient for Parallel Bodies* (2021), study monotonicity for Euclidean ball parallel bodies and relative-gauge area, not ordinary Euclidean area along cube-plus-simplex interpolation. A published cube-plus-crosspolytope boundary-spectrum theorem (2026) gives closely analogous subset-simplex Gram factors and a square-root facet-rank limit; these **are credited as antecedents** and are not asserted as the novelty here. Its centrally symmetric all-sign body has no persistent \(n\)-coordinate-facet family and does not yield this three-dimensional isoperimetric optimum through a parameter substitution. The finite volume polynomial itself is an elementary mixed-volume identity and is likewise not claimed as historically new. The proposed new contribution is the exact *ordinary-Euclidean* full facet-area accounting for the asymmetric rank-one augmented cube and, centrally, its sharp **unique** fixed-volume surface optimizer in dimension three.

## Limitations
The uniqueness theorem is proved only in dimension three, not all dimensions, and only within this one-parameter homothety family, not over arbitrary polyhedra. Some components of the exact boundary derivation are elementary and resemble known crosspolytope calculations; novelty is therefore focused on the combined asymmetric boundary accounting and the sharp surface optimizer, not on the underlying simplex Gram determinant, volume polynomial, or general local central-limit method. The literature comparison lowers but cannot eliminate the possibility of a pre-existing equivalent cube-plus-simplex isoperimetric optimization in the unindexed literature. No independent mathematical audit has been performed.

## References
1. F. Castillo, J. Doolittle, B. Goeckner, M. S. Ross, and L. Ying, *Minkowski summands of cubes*, arXiv:2009.07252 (first public 2020-09-15), especially Theorem A and the type-cone introduction. https://arxiv.org/abs/2009.07252
2. C. Richter and E. Saorín Gómez, *On the Monotonicity of the Isoperimetric Quotient for Parallel Bodies*, *Journal of Geometric Analysis* 32 (2022), Article 15, first online 2021-12-08. https://doi.org/10.1007/s12220-021-00766-2
3. *Square-root boundary-area condensation and a Gaussian facet-rank law for cube–crosspolytope sums*, published research record (2026), full RESULT inspected for its exact all-sign area spectrum. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-square-root-boundary-area-condensation-and-a-gaussian-facet-rank--4ae7f8d398dc
