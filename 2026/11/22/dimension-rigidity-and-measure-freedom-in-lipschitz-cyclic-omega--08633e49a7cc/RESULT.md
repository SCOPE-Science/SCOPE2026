# Dimension rigidity and measure freedom in Lipschitz cyclic omega sections

## Finding
Let \(I=[0,1]\) and let \(F:I^2\to I^2\) be a **globally Lipschitz triangular map**,
\[
F(x,y)=(f(x),g(x,y)).
\]
Suppose the forward \(f\)-orbit of \(x_0\) has as its \(\omega\)-limit a cycle \(P=\{p_0,\ldots,p_{m-1}\}\) of least period \(m\ge1\), with \(f(p_i)=p_{i+1}\) (indices modulo \(m\)). There are nonempty compact sets \(M_i\subset I\) such that
\[
\omega_F(x_0,y_0)=\bigcup_{i=0}^{m-1}\{p_i\}\times M_i.
\]
**Rigidity:** for each of the four notions—Hausdorff dimension, lower box dimension, upper box dimension, and packing dimension—the value is independent of the fibre index \(i\). The four notions need not agree with one another in an arbitrary example; what is forced is equality from section to section, even when those sections are not mutually homeomorphic.

**Sharp simultaneous realization:** For every integer \(m\ge1\) and every \(d\in[0,1]\), there are such a globally Lipschitz map, an \(m\)-cycle of its base, and an orbit whose sections satisfy
\[
\dim_H M_i=\underline{\dim}_B M_i=\overline{\dim}_B M_i=\dim_P M_i=d
\quad(0\le i<m).
\]
They may all be chosen affine images of a single compact set. For \(0\le d<1\), that set may be an uncountable Cantor set on which the \(m\)-step return dynamics is a **minimal, equicontinuous binary adding machine**; in particular the dynamics restricted to the full \(\omega\)-limit set has topological entropy zero.

**Independent measure freedom:** If \(0<d\le1\), and \(q_0,\ldots,q_{m-1}>0\) are arbitrary, the realization may simultaneously be chosen with
\[
0<\mathcal H^d(M_i)<\infty,
\qquad \frac{\mathcal H^d(M_i)}{\mathcal H^d(M_j)}=\frac{q_i}{q_j}
\quad(0\le i,j<m).
\]
There is no claim about arbitrary absolute \(d\)-dimensional measures, nor about preserving a prescribed global Lipschitz constant. The case \(d=0\) is not included in the measure-ratio statement.

## Assumptions and scope
Hausdorff, packing and lower/upper Minkowski (box-counting) dimensions use the Euclidean metric on each fibre. Nonempty compact sets have nonnegative dimensions bounded by one. The \(\omega\)-limit is the set of subsequential limits of the forward orbit. A cyclic base orbit may be the base coordinate of the starting point itself; the realizations below take \(x_0=p_0\). The assertion applies to finite periodic base \(\omega\)-limits only, not arbitrary base minimal sets. The constructed global maps are Lipschitz, not necessarily invertible, differentiable or dynamically mixing on the entire square.

## Proof
**1. Rigidity.** Compactness and continuity give the standard identity \(F(\omega_F(z))=\omega_F(z)\). The periodic base fibres are pairwise distinct, and only \(p_i\) among the cycle points maps to \(p_{i+1}\). Therefore the restrictions \(u_i=g(p_i,\cdot)|_{M_i}\) are surjections \(M_i\to M_{i+1}\). They are Lipschitz because \(F\) is. A Lipschitz image cannot have greater Hausdorff, packing, upper box, or lower box dimension than its domain; for box dimensions this follows from \(N_{u_i(M_i)}(L\varepsilon)\le N_{M_i}(\varepsilon)\) for a finite Lipschitz constant \(L>0\). The resulting inequalities for each of the four dimensions, iterated around the cycle, force equality. This uses no assumed conjugacy or homeomorphism of the sections.

**2. A minimal Lipschitz Cantor model.** Choose a sequence \(0<r_k\le r_*<1/2\), and write \(\ell_0=1\), \(\ell_k=\prod_{j=1}^{k}r_j\). Form a Cantor set \(C\subset[0,1]\) by retaining, at stage \(k\), the two extreme subintervals of relative length \(r_k\) inside each stage-\((k-1)\) interval. It is canonically parametrized by binary sequences \(a=(a_1,a_2,\ldots)\), with \(a_k=0\) or \(1\) deciding the left or right child. If two sequences first disagree in position \(k\), their coded points have Euclidean separation satisfying
\[
(1-2r_k)\ell_{k-1}\le |E(a)-E(b)|\le\ell_{k-1}.
\]
Addition of one in the compact group of binary \(2\)-adic integers (least significant digit first) preserves the position of the first disagreement of any two sequences. Therefore its conjugate \(T:C\to C\) obeys
\[
|T(E(a))-T(E(b))|\le (1-2r_*)^{-1}|E(a)-E(b)|.
\]
Subtraction of one gives the same inequality for \(T^{-1}\). Thus \(T\) is bi-Lipschitz. For any code and any finite prefix, some positive integer iterate of addition by one has that prefix; every orbit is dense, \(T\) is minimal and equicontinuous (all iterates preserve the first-difference depth, giving uniform equicontinuity via the displayed separation). A minimal equicontinuous system has zero topological entropy; directly, each Bowen spanning number is bounded uniformly in time by the number of sufficiently long binary prefixes.

For \(0<d<1\), set \(r_k=r=2^{-1/d}<1/2\). The resulting two-branch strongly separated self-similar Cantor set \(C_d\) has \(\dim_H C_d=\underline{\dim}_B C_d=\overline{\dim}_B C_d=\dim_P C_d=d\) and \(0<\mathcal H^d(C_d)<\infty\). Indeed \(2^k\) level-\(k\) cylinders of length \(r^k\) provide the upper bound, while their uniform Bernoulli measure satisfies \(\mu(B(x,t))\le C_rt^d\) by the positive relative gaps, giving the lower Hausdorff bound. The same level counts give both box dimensions; the packing dimension lies between Hausdorff and upper box dimension.

For \(d=0\), use \(r_k=2^{-(k+2)}\). Then
\[
\ell_k=2^{-k(k+5)/2},\qquad \frac{\log 2^k}{-\log\ell_k}=\frac{2}{k+5}\longrightarrow0.
\]
When \(\ell_k\le\varepsilon<\ell_{k-1}\), at most \(2^k\) intervals of length \(\varepsilon\) cover the set. This proves upper box dimension zero, hence all four dimensions are zero, while the Cantor set remains uncountable and carries the same minimal bi-Lipschitz adding machine. Its total \(\mathcal H^0\)-measure is infinite, which explains why it is not used for the measure-ratio clause.

For \(d=1\), choose \(C_1=[0,1]\) with the full tent map \(T(y)=1-|2y-1|\). It is Lipschitz, topologically mixing, and has a point with dense forward orbit; its four dimensions equal one and \(\mathcal H^1(C_1)=1\). This last model is not claimed to be an adding machine.

**3. Realization by a global Lipschitz triangular map.** Fix any \(m\) distinct points \(p_i\in(0,1)\), indexed in temporal cyclic order. A piecewise linear interpolant of the data \(f(p_i)=p_{i+1}\), with arbitrary endpoint values in \(I\), is a Lipschitz self-map \(f:I\to I\) containing precisely the prescribed distinct points as a period-\(m\) orbit.

Let \(C_d\) and its distinguished map \(T\) be as above. Choose arbitrary \(s_i\in(0,1/2]\) and translations \(a_i\in[0,1-s_i]\), and put \(M_i=a_i+s_iC_d\) with affine coding \(A_i:C_d\to M_i\). Define, on each \(M_i\),
\[
u_i=A_{i+1}A_i^{-1}\quad (0\le i<m-1),
\qquad u_{m-1}=A_0TA_{m-1}^{-1}.
\]
Each map is Lipschitz and maps \(M_i\) onto \(M_{i+1}\). Extend \(u_i\) to a globally Lipschitz \(\widetilde u_i:I\to I\) by any real-valued Lipschitz extension followed by clipping to \(I\) (equivalently, the one-dimensional piecewise linear gap interpolation, which also preserves the Lipschitz bound). Interpolate \(\widetilde u_i(y)\) linearly in the base coordinate between the finitely many ordered knots \(p_i\), and use the endpoint functions outside the outermost knots. This gives a jointly Lipschitz \(g:I^2\to I\) with \(g(p_i,y)=\widetilde u_i(y)\). Consequently \(F=(f,g)\) is a globally Lipschitz triangular map.

Choose \(x_0=p_0\) and a \(y_0\in M_0\) with dense forward orbit under \(A_0TA_0^{-1}\); every \(y_0\) works for \(d<1\), and a dense tent-map orbit exists for \(d=1\). At times \(mk+i\) the orbit lies in \(\{p_i\}\times M_i\), and its fibre coordinate is an affine copy of \(T^k(A_0^{-1}y_0)\). Hence those subsequences have exactly \(\{p_i\}\times M_i\) as their accumulation sets and their union is the full \(\omega_F(x_0,y_0)\). The zero-entropy assertion for \(d<1\) follows because the restriction is a finite cyclic extension of the adding machine; its \(m\)-th iterate is the union of \(m\) conjugate adding machines.

**4. Arbitrary relative Hausdorff measures.** For \(0<d\le1\), set \(H_d=\mathcal H^d(C_d)\in(0,\infty)\). Given positive numbers \(q_i\), choose \(s>0\) so small that \(s_i=sq_i^{1/d}\le1/2\) for all \(i\). Use these scales in step 3. Similarity invariance yields
\[
\mathcal H^d(M_i)=s_i^dH_d=s^dq_iH_d,
\]
which gives every ratio. Scaling does not change any of the four dimensions or the return-map conjugacy. This completes all assertions.

## Verification
`verify.py` is a standalone exact-rational finite-level checker. It exhaustively compares first-disagreement depths before and after addition modulo \(2^n\) for several lengths and contraction schedules, verifies the asserted geometric Lipschitz bounds on every pair of finite code endpoints, checks the zero-dimensional cylinder-scale identity, and tests cyclic base interpolation and the finite cyclic extension. The infinite Cantor, dimension, density and extension arguments above are proofs independent of these finite experiments. Execute `python3 verify.py` with Python 3's standard library from the same directory.

## Relationship to prior work
García Guirao (2026), Theorem A and Corollary B, characterize continuous cyclic fibre realizations using continuous surjections and chain transitivity; the article gives examples of topologically nonhomeomorphic sections. In particular its cyclic surjection criterion implies that any Lipschitz restrictions must have nonincreasing metric dimensions. The **new combined assertion** is the complete equal-dimension spectrum for globally Lipschitz triangular realizations, with minimal equicontinuous fractal models at every dimension below one and independently prescribed Hausdorff-measure ratios. The existing continuous realization theorem does not ensure a Lipschitz ambient map or those quantitative measure controls.

Balka and Keleti (2023) study Lipschitz images and dimensions, including bilipschitz equivalence among certain self-similar sets. That work supplies metric context but neither periodic-base triangular omega-limits nor these simultaneous realizations. Pawelec (2024) studies recurrence under an adding machine on a self-similar Cantor set; adding-machine dynamics themselves are established background, not claimed as new. Jiménez López and Smítal (2001) study realizability of Peano continua and other sections by continuous triangular maps, not the Lipschitz quantitative spectrum. A related published construction of interval forests with cyclic omega-limit sections concerns continuous nonhomeomorphic sets with countably many interval components, rather than the present Lipschitz equidimensional Cantor families.

## Limitations
This is a **realizability spectrum**, not a characterization of every possible tuple of Lipschitz sections. Equality of dimensions is necessary but by itself need not be sufficient for prescribed non-affinely related compact sets. The constructed sets are affine images of one model; no upper bound on the Lipschitz constant is fixed. The base orbit starts exactly on the periodic cycle. There is no global attractivity, no differentiability conclusion, and no claim of independently performed audit. Earlier general results on cyclic surjections, Lipschitz dimension monotonicity and adding machines provide substantial ingredients; equivalent special constructions in other literature remain possible.

## References
1. J. L. García Guirao, *\(\omega\)-limit sets of triangular maps over periodic orbits of the base*, arXiv:2611.06889v1, first posted 2026-11-04, https://arxiv.org/abs/2611.06889 .
2. R. Balka and T. Keleti, *Lipschitz images and dimensions*, arXiv:2308.02639, first posted 2023-08-04, https://arxiv.org/abs/2308.02639 .
3. Ł. Pawelec, *Estimating the Hausdorff measure using recurrence*, Proceedings of the Edinburgh Mathematical Society, published 2024, https://www.cambridge.org/core/journals/proceedings-of-the-edinburgh-mathematical-society/article/estimating-the-hausdorff-measure-using-recurrence/840E4CA35494D29A2F2E24C49701133A .
4. V. Jiménez López and J. Smítal, *\(\omega\)-limit sets for triangular mappings*, Fundamenta Mathematicae 167 (2001), 1–15, DOI:10.4064/fm167-1-1, https://www.impan.pl/en/publishing-house/journals-and-series/fundamenta-mathematicae/all/167/1/89185/omega-limit-sets-for-triangular-mappings .
