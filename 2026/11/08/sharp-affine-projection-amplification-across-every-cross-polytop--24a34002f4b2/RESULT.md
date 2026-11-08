# Sharp affine-projection amplification across every cross-polytope face skeleton

## Finding

Let \(d\ge2\) be an integer and \(C_d=\{x\in\mathbb R^d:\sum_{i=1}^d|x_i|\le1\}\). For \(1\le s\le d\), let \(\mu_{d,s}\) be the probability obtained by choosing one \((s-1)\)-dimensional face of \(C_d\) uniformly, then choosing a uniformly distributed point of that face with respect to its intrinsic volume. This is uniform counting probability on the \(2d\) vertices when \(s=1\), and normalized boundary surface probability when \(s=d\). Let \(P_{d,s}\) be the real \(L^2(\mu_{d,s})\)-orthogonal projection onto all restrictions of affine functions, with the projected function evaluated on the entire polytope using its unique affine extension.

The exact \(L^\infty\)-operator norm is
\[
\boxed{\|P_{d,s}\|=1+\frac{s+1}{2}\left(1-\frac{2}{d(s+1)}\right)^s.}
\]
All and only the \(2d\) vertices \(\{\pm e_i:1\le i\le d\}\) are norming evaluation locations. At each vertex \(v\), input data attaining the norm are precisely the positive or negative sign of the reproducing kernel \(1+\frac{d(s+1)}2 v\cdot y\), modulo sets of measure zero.

If \(P_{d,\mathrm{vol}}\) denotes the analogous projector for normalized \(d\)-dimensional Lebesgue measure on \(C_d\), then
\[
\boxed{\|P_{d,\mathrm{vol}}\|=1+\frac{d+2}{2}\left(1-\frac{2}{(d+1)(d+2)}\right)^{d+1}.}
\]
Its norming evaluation locations are again exactly the vertices. The complete strict hierarchy is
\[
\boxed{\|P_{d,1}\|<\|P_{d,2}\|<\cdots<\|P_{d,d}\|<\|P_{d,\mathrm{vol}}\|.}
\]
Moreover, writing \(L_{d,s}=\|P_{d,s}\|\), uniformly in \(1\le s\le d\),
\[
0\le L_{d,s}-\left(\frac{s+3}{2}-\frac{s}{d}\right)<\frac1d,
\qquad
\sup_{1\le s<d}\left|L_{d,s+1}-L_{d,s}-\frac12\right|\le\frac2d,
\]
and
\[
\boxed{\lim_{d\to\infty}\bigl(\|P_{d,\mathrm{vol}}\|-\|P_{d,d}\|\bigr)=\frac12.}
\]

## Assumptions and scope

All dimensions and face ranks are integers with \(d\ge2\) and \(1\le s\le d\). Every face of fixed rank is selected with equal probability, and intrinsic uniform face measure is normalized to probability. In this regular cross-polytope all faces of the same dimension have equal intrinsic volume, so the measure is also normalized intrinsic Hausdorff measure on the corresponding skeleton. The domain and codomain norms are \(L^\infty\) on the observation support; affine output has a unique representative and can also be evaluated on \(C_d\), which gives the same supremum. The projection includes the constant function. The real scalar field is essential for the sign-kernel extremizer formulation.

The random sampling description is equivalent to choosing a uniformly random support \(S\subset\{1,\dots,d\}\) of cardinality \(s\), independent uniformly random signs on \(S\), and a Dirichlet\((1,\ldots,1)\) vector \((U_i)_{i\in S}\), then setting \(Y_i=\operatorname{sign}_i U_i\) for \(i\in S\) and \(Y_i=0\) otherwise. For \(s=1\), the one-coordinate Dirichlet variable equals one.

## Proof

**1. Kernel and covariance.** Coordinate sign symmetry gives \(\mathbb E Y_i=0\) and \(\mathbb E Y_iY_j=0\) for distinct coordinates. For a Dirichlet\((1,\dots,1)\) distribution on \(s\) coordinates, \(\mathbb E U_i^2=2/[s(s+1)]\). Since each coordinate is selected with probability \(s/d\),
\[
\mathbb E Y_i^2=\frac{s}{d}\frac2{s(s+1)}=\frac2{d(s+1)}.
\]
Thus the affine Gram matrix in basis \(1,y_1,\ldots,y_d\) is diagonal with strictly positive diagonal, and its reproducing kernel is
\[
K_{d,s}(x,y)=1+\alpha_{d,s} x\cdot y,\qquad
\alpha_{d,s}=\frac{d(s+1)}2.
\]
The operator norm is \(\max_{x\in C_d}\int|K_{d,s}(x,y)|\,d\mu_{d,s}(y)\). The maximum over \(C_d\) equals the essential supremum over the sampling support because the norming vertices belong to the closure of that support.

**2. Exact integral.** The evaluation-row norm is convex in \(x\), so it is at most its maximum over vertices. By signed-permutation symmetry, all vertices have the same row norm. At \(x=e_1\), symmetry and \(\int K(e_1,y)\,d\mu_{d,s}=1\) imply
\[
\int|K(e_1,y)|\,d\mu_{d,s}(y)
=1+\frac{s}{d}\mathbb E(\alpha_{d,s}U-1)_+,
\]
where \(U\) is Beta\((1,s-1)\) for \(s\ge2\), and equals one for \(s=1\). Its survival function is \(\mathbb P(U>u)=(1-u)^{s-1}\) for \(0\le u<1\), with the \(s=1\) case read as the constant survival function one. Because \(\alpha_{d,s}>1\), integration of the survival function gives
\[
\mathbb E(\alpha_{d,s}U-1)_+
=\alpha_{d,s}\int_{1/\alpha_{d,s}}^1(1-u)^{s-1}\,du
=\frac{\alpha_{d,s}}s(1-\alpha_{d,s}^{-1})^s.
\]
Substitution yields the asserted closed skeleton norm.

**3. Strict norming-location classification.** Let \(v\ne w\) be any two vertices. An observation \(y\) sufficiently close to \(-v\) within one of the sampled faces that contains \(-v\) satisfies \(K(v,y)<0<K(w,y)\), since \(\alpha_{d,s}>1\) and \(w\cdot(-v)\) is zero or one. This sign disagreement holds on positive \(\mu_{d,s}\)-measure (an atom when \(s=1\)). For any nonvertex \(x\in C_d\), choose a convex decomposition involving at least two distinct vertices with positive weights. The triangle inequality in the representation \(K(x,y)=\sum_v\lambda_v K(v,y)\) is then strict after integration, because a pair of these kernels has opposite signs on a positive-measure observation set. Hence every nonvertex row norm is strictly less than the common vertex row norm. Equality in the dual \(L^\infty\)-to-\(\mathbb R\) integral bound forces input signs to match \(K(v,\cdot)\) almost everywhere, or their simultaneous reversal. For \(s\ge2\), the zero set of this affine kernel has zero skeleton measure; for \(s=1\), it is nonzero at all observation vertices. This proves the complete norming and input equality cases.

**4. Strict skeleton hierarchy.** Write \(c=2/d\), and for real \(t\ge2\) define \(g(t)=t(1-c/t)^{t-1}\). Its logarithmic derivative is
\[
\frac{g'(t)}{g(t)}=\frac1t+\log(1-c/t)+\frac{(t-1)c}{t(t-c)}.
\]
For \(0<u<1\), the strict elementary bound \(\log(1-u)>-u/(1-u)\) yields
\[
\frac{g'(t)}{g(t)}>\frac{t-2c}{t(t-c)}\ge0
\qquad(t\ge2,\ 0<c\le1).
\]
Therefore \(g\) is strictly increasing. Since \(L_{d,s}=1+\frac12g(s+1)\), all successive skeleton inequalities are strict.

**5. Solid-volume formula and strict final inequality.** A uniform point \(X\) of \(C_d\) can be written \(X=RZ\), where \(Z\sim\mu_{d,d}\), \(R\) is independent with density \(d r^{d-1}\) on \([0,1]\), and \(\mathbb E R^2=d/(d+2)\). Hence \(\mathbb E X_i^2=2/[(d+1)(d+2)]\), and the volume projection kernel is \(1+\frac{(d+1)(d+2)}2 x\cdot y\). The magnitude of a coordinate of a uniform volume point is Beta\((1,d)\), so the same tail integration with selection probability one gives the displayed volume norm. The strict vertex-classification argument of Step 3 also applies, using open sets of positive volume near the negative vertices.

For strict volume versus boundary comparison, fix a vertex \(v\), put \(a=d(d+1)/2\) and \(b=\mathbb E R^2=d/(d+2)\), and let \(W=|v\cdot Z|\). By independent sign symmetry, the surface row norm equals \(\mathbb E\max(1,aW)\), whereas the volume row norm equals \(\mathbb E\max(1,(a/b)RW)\). For each fixed \(W\), convexity in \(R\) gives a lower bound \(\max(1,(a/b)(\mathbb E R)W)\). Since \(\mathbb E R=d/(d+1)>b\), this lower bound strictly exceeds \(\max(1,aW)\) whenever \(aW>1\). That event has positive probability. Therefore \(\|P_{d,\mathrm{vol}}\|>\|P_{d,d}\|\), completing the hierarchy.

**6. Uniform and asymptotic consequences.** Put \(a=2/[d(s+1)]\). Bernoulli's inequality and the second-order Taylor remainder bound for \((1-a)^s\) give
\[
0\le (1-a)^s-(1-sa)\le\binom{s}{2}a^2.
\]
Multiplying by \((s+1)/2\) yields
\[
0\le L_{d,s}-\left(\frac{s+3}{2}-\frac{s}{d}\right)
\le\frac{s(s-1)}{d^2(s+1)}<\frac1d.
\]
Taking neighboring differences proves the stated uniform \(2/d\) bound. The boundary and volume closed forms, expanded to first order with the same controlled remainder, give respectively \(\|P_{d,d}\|=(d+1)/2+O(1/d)\) and \(\|P_{d,\mathrm{vol}}\|=(d+2)/2+O(1/d)\); their difference converges to \(1/2\).

## Verification

The accompanying standalone `checker.py` computes the vertex-row norm independently by exactly integrating the binomial expansion of the Beta density, with rational arithmetic for every \(2\le d\le34\) and \(1\le s\le d\). It additionally checks coordinate covariances, the zero-skeleton kernel directly by finite summation, sampled strict comparisons and the radial-volume moment identity. These are finite corroborations only: Steps 1–6 above prove the statements for all allowed dimensions and ranks without relying on the finite range of tests.

Run `python3 checker.py` with Python 3.9 or later; the checker uses only Python's standard library.

## Relationship to prior work

The boundedness and max-norm stability of orthogonal least-squares projectors are classical themes. Oswald's 2006 counterexample studies unbounded projection norms for piecewise-linear spline spaces on highly graded simplicial triangulations; its approximation spaces and measures differ from a single global affine space observed on a fixed cross-polytope's faces. Hangelbroek, Narcowich, Sun and Ward's 2010 paper proves stability of projectors onto spaces generated by positive-definite kernels on smooth manifolds under quasiuniform sampling hypotheses; it does not give these face-skeleton exact constants.

The published exact simplex-affine projector calculation is for uniform solid-simplex sampling, not the \(\ell_1\)-cross-polytope or its ranked skeleta. A separate universal comparison for centrally symmetric bodies proves that cone-boundary affine projection is more stable than solid-volume projection; it does not imply the face-rank formulas, the strict intermediate skeleton hierarchy, or the uniform half-step law. The present result concerns a regular cross-polytope, hence includes a complete family of mutually distinct observation supports and strictly increasing amplification constants.

## Limitations

This is not a general theorem for arbitrary simplicial polytopes, weighted faces, nonuniform face probabilities, or higher-degree polynomial approximation. It uses equal-probability sampling of all same-rank faces, intrinsic uniform face measures and affine projection. The numerical checker supplies corroboration, not an infinite-dimensional or computer-assisted proof. Literature indexing is incomplete; a mathematically equivalent earlier treatment of ranked cross-polytope skeleton sampling could exist beyond the inspected sources.

## References

1. P. Oswald, *A counterexample concerning the \(L^2\)-projector onto linear spline spaces*, arXiv:math/0611573, first posted November 19, 2006; especially Sections 1–3 and Theorem 1. https://arxiv.org/abs/math/0611573
2. T. Hangelbroek, F. J. Narcowich, X. Sun and J. D. Ward, *Kernel Approximation on Manifolds II: The \(L^\infty\)-norm of the \(L^2\)-projector*, arXiv:1005.2424, first posted May 13, 2010; especially Section 5 and Theorem 5.1. https://arxiv.org/abs/1005.2424
