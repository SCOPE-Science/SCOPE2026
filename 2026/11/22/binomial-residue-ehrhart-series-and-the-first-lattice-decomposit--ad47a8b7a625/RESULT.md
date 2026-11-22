# Binomial-residue Ehrhart series and the first lattice-decomposition hole of uniformly weighted odd-cycle simplices

## Finding

For every odd integer \(n\ge3\) and integer \(w\ge2\), consider the lattice polytope
\[
P_{n,w}=\operatorname{conv}\{e_i+w e_{i+1}:i\in\mathbb Z/n\mathbb Z\}
\subset\mathbb R^n,
\]
where coordinate indices are cyclic. It is an \((n-1)\)-simplex in the affine hyperplane \(\sum_i x_i=w+1\). With respect to the induced ambient integer lattice in that hyperplane, its Ehrhart numerator is
\[
h^*_{P_{n,w}}(t)=1+\sum_{\substack{n\le s\le nw\\s\equiv0\pmod{w+1}}}
[z^s](z+z^2+\cdots+z^w)^n\,t^{s/(w+1)}.
\tag{1}
\]
In particular, its normalized lattice volume equals \((w^n+1)/(w+1)\). Every nonconstant coefficient at degrees \(\lceil n/(w+1)\rceil\) through \(n-\lceil n/(w+1)\rceil\) is positive; all other nonconstant coefficients vanish. The positive-degree coefficients are symmetric under \(j\mapsto n-j\).

If additionally \(2\le w\le n-2\), set \(q=\lceil n/(w+1)\rceil\ge2\). The only integer points of \(P_{n,w}\) are its \(n\) vertices. For every integer \(1\le m<q\), every integer point in \(mP_{n,w}\) decomposes as a sum of \(m\) integer points of \(P_{n,w}\). In degree \(q\) such a decomposition fails, and hence \(q\) is the exact first nondecomposable dilation. For the fixed weight \(w=2\), this first-failure degree is \(\lceil n/3\rceil\), unbounded as odd \(n\to\infty\).

## Assumptions and scope

All lattice points refer to \(\mathbb Z^n\); dilations take place in the hyperplanes \(\sum_i x_i=m(w+1)\). Let \(S\) be the cyclic shift \(Se_i=e_{i+1}\), and let \(A=I+wS\), so its columns are the vertices. For odd \(n\),
\[
\det A=1+w^n>0,\qquad
A^{-1}=\frac{1}{1+w^n}\sum_{j=0}^{n-1}(-wS)^j.
\tag{2}
\]
The Ehrhart series convention is \(\sum_{m\ge0}|mP_{n,w}\cap\mathbb Z^n|t^m=h^*_{P_{n,w}}(t)/(1-t)^n\). A degree-\(m\) decomposition is an equality \(z=z_1+\cdots+z_m\) with each \(z_i\in P_{n,w}\cap\mathbb Z^n\).

## Proof

**Step 1: fundamental-parallelepiped representatives.** For each \(b=(b_1,\ldots,b_n)\in\{1,\ldots,w\}^n\), define \(\alpha=A^{-1}b\). Formula (2) gives
\[
(1+w^n)\alpha_i=\sum_{j=0}^{n-1}(-w)^j b_{i-j}.
\]
Because \(n\) is odd, the even exponents have positive signs and the odd exponents have negative signs. The minimum over \(1\le b_i\le w\) is \(\sum_{j\ \mathrm{even}}w^j-w\sum_{j\ \mathrm{odd}}w^j=1\), and the maximum is \(w\sum_{j\ \mathrm{even}}w^j-\sum_{j\ \mathrm{odd}}w^j=w^n\). Thus
\[
\frac1{1+w^n}\le\alpha_i\le\frac{w^n}{1+w^n}<1
\tag{3}
\]
for every coordinate. Distinct integer vectors \(b\) give distinct fractional vectors \(\alpha\). Along with \(\alpha=0\), this produces \(w^n+1=|\det A|\) distinct points in \([0,1)^n\) having integer image under \(A\). Since this is exactly the index of \(A\mathbb Z^n\) in \(\mathbb Z^n\), these are *all* such representatives.

**Step 2: impose the affine lattice and obtain the full numerator.** The affine lattice of the simplex is the lattice \(\{z\in\mathbb Z^n:\sum_i z_i\equiv0\pmod{w+1}\}\) in the integer-coordinate cone, graded by \(\sum_i z_i/(w+1)\). Since every column of \(A\) has coordinate sum \(w+1\), the fundamental representative for \(b=A\alpha\) belongs to this graded lattice exactly when \(\sum_i b_i\) is divisible by \(w+1\). Its degree is then
\[
\sum_i\alpha_i=\frac{\sum_i b_i}{w+1}.
\]
The half-open simplicial-cone parallelepiped decomposition is disjoint and unique: each cone lattice point is precisely a representative plus a nonnegative integer combination of the \(n\) generator columns. Accordingly its lattice-point generating series has denominator \((1-t)^n\) and numerator (1), including the origin. Counting the selected representatives also gives \([\mathbb Z^n:A\mathbb Z^n]/[\mathbb Z^n:L]= (1+w^n)/(w+1)\), where \(L=\{z\in\mathbb Z^n:\sum_i z_i\equiv0\pmod{w+1}\}\), proving the normalized-volume formula. All available integer sums of \(n\) entries between \(1\) and \(w\) occur, proving the support interval. The involution \(b_i\mapsto w+1-b_i\) takes the integer degree \(j\) to \(n-j\), proving positive-degree symmetry.

**Step 3: sharp first failure.** Under \(w\le n-2\), the least positive degree among nonzero representatives is \(q\ge2\). Because \(h_1^*=|P_{n,w}\cap\mathbb Z^n|-n\), there are no nonvertex lattice points in the simplex. Let \(1\le m<q\) and \(z\in mP_{n,w}\cap\mathbb Z^n\). Uniquely write \(z=A\lambda\), \(\lambda_i\ge0\), \(\sum_i\lambda_i=m\). Its integer and fractional parts satisfy \(A\{\lambda\}\in\mathbb Z^n\), with \(\sum_i\{\lambda_i\}\) a nonnegative integer at most \(m\). If that sum were positive it would be at least \(q\) by Step 2, contradiction. Hence \(\lambda\in\mathbb Z_{\ge0}^n\), and \(z\) decomposes into \(m\) simplex vertices. At degree \(q\), choose any \(b\in\{1,\ldots,w\}^n\) whose sum equals \(q(w+1)\), which exists by the support interval. Then \(b=A\alpha\in qP_{n,w}\cap\mathbb Z^n\) with all \(0<\alpha_i<1\) by (3); the unique barycentric representation is not a nonnegative integer combination of vertices, so no \(q\)-term lattice-point decomposition exists. This establishes the exact threshold.

## Verification

The standalone standard-library program `verify_cycle.py` computes (1) by bounded compositions, independently enumerates all lattice points in small dilates by the inequalities \(A^{-1}z\ge0\), and compares Ehrhart counts using the binomial-basis expansion. It also verifies the strict coordinate bounds (3), the volume index and the coefficient symmetry. Seven sample parameter pairs \((n,w)\) comprise \((3,2),(3,4),(5,2),(5,3),(5,4),(7,2),(7,3)\), with \(3686\) bounded-composition vectors and \(32\) direct dilation counts. To rerun: `python3 verify_cycle.py` in the directory containing the file. These finite checks test the proof but do not substitute for its general argument.

## Relationship to prior work

Biermann, Lin and O'Keefe define the corresponding weighted oriented graph edge polytope. Their Proposition 3.10 identifies nonvertex integer points in the original simplex, and their Theorem 4.5 proves that a naturally oriented cycle with weights greater than one fails the integer decomposition property (for their stated cycle-size range). **These earlier results are not claimed as new.** The contribution here is the explicit binomial-residue Ehrhart numerator across all odd cycle sizes and uniform weights, together with the exact smallest failing dilation in the empty-simplex regime. Doolittle, Katthän, Nill and Santos investigate cyclic and circulant empty simplices; their general lattice constructions are a relevant background, but the inspected material does not explicitly give this family's coefficient formula or sharp decomposition threshold. The oriented-cycle **root** polytopes in separate literature use edge differences rather than positive weighted exponent vectors; a published root-polytope Ehrhart classification therefore does not imply (1).

## Limitations

The argument is restricted to odd \(n\) and integral uniform weights \(w\ge2\); its first-failure claim further assumes \(w\le n-2\). It does not assert optimality among all empty simplices, nor classify first nonnormality for even cycles or for the nonempty regime. A literature search cannot establish global priority, and unindexed computations or alternative terminology may contain overlapping enumerations. No independent audit has been performed.

## References

1. J. Biermann, K.-N. Lin, A. O'Keefe, *Integer Decomposition Property of Edge Polytopes of Weighted Oriented Graphs* (2026), arXiv:2611.17047v1, Proposition 3.10 and Theorem 4.5. https://arxiv.org/abs/2611.17047
2. J. Doolittle, L. Katthän, B. Nill, F. Santos, *Empty simplices of large width*, *Forum of Mathematics, Sigma* (open access), particularly cyclic and circulant constructions. https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/empty-simplices-of-large-width/08EB9BD3CDF8AE894DF9B9491623CE28
3. *Exact Ehrhart polynomials of oriented cycle root polytopes*, published mathematical record, different root-polytope construction. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-ehrhart-polynomials-of-oriented-cycle-root-polytopes--e32575b66377
