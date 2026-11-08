# The Frobenius incenter of every hollow symmetric Monge simplex is Toeplitz and tends to quadratic cost

## Finding
For each integer \(n\ge3\), let \(\mathcal H_n\) consist of real, symmetric, entrywise-nonnegative \(n\)-by-\(n\) matrices \(C\) with \(C_{ii}=0\), \(\sum_{i,j=1}^n C_{ij}=1\), and the Monge inequalities
\[
C_{ij}+C_{k\ell}\le C_{i\ell}+C_{kj}\qquad(i<k,\ j<\ell).
\]
Distances and balls are measured in the intrinsic Frobenius metric on this affine space. Set
\[
N=\binom n2,\qquad
\alpha_n=\sqrt{3-\frac1N},\qquad
\beta_n=\sqrt{1-\frac1N},
\]
\[
D_n=2\binom n4+\alpha_n\binom n3+\beta_n\binom{n+1}3.
\]
Then **the largest inscribed Euclidean ball has exactly one center** \(C^{(n)}\), and its radius is
\[
\boxed{\rho_n=\frac{1}{\sqrt2\,D_n}.}
\]
The center is a symmetric **Toeplitz** matrix: \(C^{(n)}_{ii}=0\) and, for \(d=|i-j|\in\{1,\ldots,n-1\}\),
\[
\boxed{
C^{(n)}_{ij}=\frac{(d-1)(d-2)_++\alpha_n(d-1)+\beta_n d}{2D_n},
\qquad (z)_+=\max\{z,0\}.}
\]
Thus the center has a strictly superadditive distance profile: for all \(1\le i<j<k\le n\),
\[
C^{(n)}_{ik}>C^{(n)}_{ij}+C^{(n)}_{jk}.
\]
In particular the center is a strictly nonmetric Monge transportation cost, although a distinguished boundary face of this simplex consists of metric cost matrices.

The asymptotic statements are sharp:
\[
\boxed{\lim_{n\to\infty}n^4\rho_n=6\sqrt2,\qquad
\lim_{n\to\infty}\max_{1\le i,j\le n}
\left|n^2 C^{(n)}_{ij}-6\left(\frac{i-j}{n}\right)^2\right|=0.}
\]
Accordingly, the intrinsic Euclidean incenter selects the continuum squared-distance cost kernel \(6(s-t)^2\), with its normalization \(\int_0^1\int_0^1 6(s-t)^2\,ds\,dt=1\).

## Assumptions and scope
The **hollow symmetric** condition, the normalization \(\sum C_{ij}=1\), and the inherited Frobenius metric \(\|C\|_F=(\sum C_{ij}^2)^{1/2}\) are essential. The affine dimension is \(N-1\). The body is a genuine simplex for \(n\ge3\); for \(n=2\) it consists of a single point, so the positive-dimensional inradius statement is not asserted. Every quantity above is intrinsic to the hollow symmetric affine subspace, not to all \(n\)-by-\(n\) matrices. No nonsymmetric or general non-hollow claim is made.

## Proof
**Step 1: an explicit simplex parametrization.** Use the triangular index set
\[
\mathcal T_n=\{(a,b):a,b\ge1,\ a+b\le n\},\qquad |\mathcal T_n|=N.
\]
For \((a,b)\in\mathcal T_n\), define \(V_{ab}\) by placing the value \(1/(2ab)\) in each entry of the upper-right \(a\)-by-\(b\) rectangle and the transposed lower-left rectangle, and zero elsewhere. Both rectangles are disjoint from the diagonal. These are nonnegative normalized symmetric Monge matrices: each rectangle indicator is a product of oppositely monotone row and column indicators and therefore satisfies each two-by-two Monge inequality. This vertex family and its simpliciality are also proved in Erickson--Kretschmann, Proposition 4.1--4.2.

For the strictly upper-triangular coordinates write \(y_{ab}=C_{a,n-b+1}\), \((a,b)\in\mathcal T_n\), setting \(y_{ab}=0\) when \(a+b>n\). In particular the affine sum constraint is \(2\sum_{\mathcal T_n}y_{ab}=1\), and the squared Frobenius length of a displacement is \(2\sum_{\mathcal T_n}(\delta y_{ab})^2\). The unique barycentric coefficients in the vertex basis satisfy
\[
y_{ab}=\sum_{\substack{u\ge a,\ v\ge b\\u+v\le n}}
\frac{\lambda_{uv}}{2uv},\qquad
\boxed{\lambda_{ab}=2ab\left(y_{ab}-y_{a+1,b}-y_{a,b+1}+y_{a+1,b+1}\right).}
\]
To justify the inverse, subtract adjacent cumulative sums in the two indices. The components for \(a+b=n-1\) use a zero diagonal boundary value; those for \(a+b=n\) reduce to \(\lambda_{ab}=2ab y_{ab}\). Each inverse inequality \(\lambda_{ab}\ge0\) follows from the relevant upper-right adjacent Monge inequality, including the boundary inequalities with a diagonal zero. Conversely, nonnegative coefficients with sum one reconstruct \(C\) as a convex combination of the \(V_{ab}\). Thus the simplex has **precisely the facet inequalities** \(\lambda_{ab}\ge0\) and \(\sum\lambda_{ab}=1\).

**Step 2: three exact gradient types.** Fix \((a,b)\in\mathcal T_n\), and take the gradient of \(\lambda_{ab}\), restricted to the affine tangent plane \(\sum y_{uv}=0\). If \(a+b\le n-2\), its coefficient vector in the \(y\)-coordinates has four entries with signs \((+,-,-,+)\), sum zero and squared norm four. If \(a+b=n-1\), its three coefficients have signs \((+,-,-)\), sum minus one and squared norm three. If \(a+b=n\), only one plus coefficient survives. Orthogonal projection to the sum-zero hyperplane subtracts the average component. Moreover, the Frobenius metric contributes a factor \(1/2\) to squared dual norms. Therefore the intrinsic gradient norms are exactly
\[
\boxed{
 g_{ab}=\|\nabla_{\mathrm{aff}}\lambda_{ab}\|_F=
\sqrt2\,ab\begin{cases}
2,&a+b\le n-2,\\
\sqrt{3-1/N},&a+b=n-1,\\
\sqrt{1-1/N},&a+b=n.
\end{cases}}
\]
All gradients are nonzero because \(N\ge3\).

**Step 3: radius and uniqueness.** For any interior point with barycentric coordinates \(\lambda_{ab}\), the perpendicular distance to facet \(\lambda_{ab}=0\) is \(\lambda_{ab}/g_{ab}\). A radius-\(r\) ball is contained in the simplex exactly when \(\lambda_{ab}\ge r g_{ab}\) for every index. Summing the constraints gives \(1\ge r\sum g_{ab}\). Equality is attained by choosing \(\lambda_{ab}=\rho_n g_{ab}\) for every index and \(\rho_n=(\sum g_{ab})^{-1}\); equality forces every coordinate and hence the center uniquely. The elementary triangular identity
\[
\sum_{a=1}^{m-1}a(m-a)=\binom{m+1}3
\]
and the hockey-stick sum over \(2\le m\le n-2\) give
\[
\sum_{\mathcal T_n}g_{ab}
=\sqrt2\left[2\binom n4+\alpha_n\binom n3+\beta_n\binom{n+1}3\right]=\sqrt2 D_n,
\]
which proves the radius formula and the exact barycentric weights.

**Step 4: Toeplitz structure.** The normalized barycentric weight divided by the rectangular vertex weight is
\[
\frac{\lambda_{ab}}{2ab}=
\frac1{2D_n}\begin{cases}
2,&a+b\le n-2,\\
\alpha_n,&a+b=n-1,\\
\beta_n,&a+b=n.
\end{cases}
\]
Consequently \(y_{ab}\) is the sum over all upper-right rectangles containing \((a,b)\). Writing \(d=n+1-a-b\), there are \(m-a-b+1\) such rectangles with index sum \(m\). Their weighted sum is
\[
2\sum_{\ell=1}^{d-2}\ell+(d-1)\alpha_n+d\beta_n
=(d-1)(d-2)_++(d-1)\alpha_n+d\beta_n.
\]
As \(d=(n-b+1)-a\), the result depends only on the distance between the original matrix indices, proving the exact Toeplitz formula.

**Step 5: strict reversal of the triangle inequality.** Put \(h(d)=(d-1)(d-2)_+\) for positive integer \(d\). Its successive increments are nonnegative and nondecreasing, starting at zero, hence it is superadditive. For positive integers \(p,q\), the numerator \(Q(d)=h(d)+\alpha_n(d-1)+\beta_n d\) obeys
\[
Q(p+q)-Q(p)-Q(q)
=\bigl[h(p+q)-h(p)-h(q)\bigr]+\alpha_n\ge\alpha_n>0.
\]
Dividing by \(2D_n\) proves the strict inequality for every ordered triple.

**Step 6: asymptotics, including uniformity.** Since \(D_n=n^4/12+O(n^3)\), we have \(n^4\rho_n\to6\sqrt2\). Uniformly for integers \(1\le d<n\), the numerator \(Q(d)=d^2+O(n)\), with the implied constant independent of \(d\) and \(n\); also \(2D_n=n^4/6+O(n^3)\). Thus
\[
\sup_{1\le d<n}\left|n^2\frac{Q(d)}{2D_n}-6(d/n)^2\right|=O(n^{-1}).
\]
The diagonal entries are identically zero, so the same estimate holds over all matrix entries. This proves the uniform continuum profile.

## Verification
The standalone script `verification/verify_hollow_monge.py` constructs the vertex matrix in independent upper-triangular coordinates, **inverts that matrix numerically independently** of the finite-difference formulas, projects all facet gradients into the correct affine Frobenius tangent space, and solves an independent linear program for the Chebyshev radius. It verifies every formula, the Toeplitz entries, the unique-radius equalities, and strict anti-metric inequalities for \(3\le n\le10\). It also reports asymptotic scaled radii and uniform errors at several larger dimensions. The script's independent matrix-inverse and LP checks agree with the theorem within stated floating-point tolerances. The all-dimensional proof is analytical; these checks are finite corroboration.

## Relationship to prior work
Erickson and Kretschmann's *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522 (first posted 2023-11-13), defines the hollow symmetric Monge simplex, determines its vertices, and identifies its metric face (Propositions 4.1, 4.2, 4.6). Their full relevant Sections 2--5 were inspected. Their volume and face-lattice results do not give the **Frobenius inradius, the unique Toeplitz incenter, or the quadratic continuum limit**.

The published published-finding corpus note *An affine \((n-1)\)-cube of Euclidean incenters for square Monge polytopes* (2026-10-11) gives the exact inball of the **nonsymmetric** normalized square Monge polytope, whose ambient dimension is \(n^2-1\) and which has nonunique centers. Its proof and theorem were inspected. Taking the hollow symmetric slice does not transport its radius or incenter classification, since that slice is lower-dimensional and its intrinsic facet norms change. That published nonsymmetric inradius is asymptotic to \(6n^{-4}\), whereas the hollow symmetric radius here is asymptotic to \(6\sqrt2\,n^{-4}\). The strict squared-cost continuum profile and its anti-metric property are further statements not implied by that prior result.

Rudolf and Woeginger (1995) characterize extreme rays of the nonnegative Monge cone but do not, in the available descriptions, address this intrinsic Euclidean center. No equivalence with a previously published Chebyshev-center or discrete-cost result was identified in the searches listed in the audit; absence of an identified result is not proof of publication priority.

## Limitations
The theorem does not extend automatically to all symmetric (non-hollow), nonsymmetric, rectangular, or differently normalized Monge polytopes. The Euclidean metric is specifically Frobenius, not an arbitrary affine-invariant metric. The comparison with the nonsymmetric case does not assert an exact finite-size radius ratio. No independent mathematical audit or comprehensive exhaustive historical-priority certification has been performed. Earlier work on Monge cone extremal rays was available principally through bibliographic descriptions, rather than a fully inspected original article.

## References
- W. Q. Erickson and J. Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522v2, first public posting 2023-11-13; especially Propositions 4.1--4.2, Section 4.3 and Proposition 4.6. Full-text preprint also available from the authors' ResearchGate upload, 2023-11-20.
- R. Rudolf and G. J. Woeginger, *The cone of Monge matrices: Extremal rays and applications*, Mathematical Methods of Operations Research 42 (1995), 161--168; DOI:10.1007/BF01415751.
- *An affine \((n-1)\)-cube of Euclidean incenters for square Monge polytopes*, published mathematical research record, published-finding corpus (2026-10-11), full `RESULT.md` inspected.
