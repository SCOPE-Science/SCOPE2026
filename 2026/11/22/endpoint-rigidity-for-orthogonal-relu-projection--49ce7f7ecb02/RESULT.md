# Endpoint rigidity for orthogonal ReLU projection

## Finding

Let \(d\ge1\), let \(U\in\mathbb R^{d\times d}\) be orthogonal, and write \((v)_+=(\max\{v_i,0\})_{i=1}^d\). Define the Euclidean metric projector
\[
R_U(x)=U^{\mathsf T}(Ux)_+
=P_{\,U^{\mathsf T}\mathbb R_+^d}(x).
\]
For input and output both equipped with \(\|x\|_\infty=\max_i|x_i|\), the following are equivalent:

1. \(R_U\) is nonexpansive: \(\|R_U(x)-R_U(y)\|_\infty\le\|x-y\|_\infty\) for every \(x,y\in\mathbb R^d\).
2. Every orthogonal projector \(U^{\mathsf T}D U\), where \(D\) is a diagonal zero–one matrix, has induced maximum-row-sum norm at most one.
3. After independently permuting and changing signs of rows and columns, \(U\) is a block diagonal matrix with blocks of sizes one and two, all one-dimensional blocks equal to \(1\), and every two-dimensional block equal to
\[
H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]

In this case the optimal global coefficient is exactly \(\operatorname{Lip}_\infty(R_U)=1\). Otherwise it is strictly larger than one. Thus coordinatewise nonexpansivity permits arbitrary disjoint 45-degree pair mixing but forbids every other orthogonal mixing pattern.

A concrete expansive certificate is available from every row \(u\) of \(U\). Writing \(s=\|u\|_1\), one has
\[
\operatorname{Lip}_\infty(R_U)\ge
\max\left\{\|u\|_\infty s,\ \max_j\bigl(1+|u_j|s-2u_j^2\bigr)\right\}.
\]
For a flat row with \(k\ge3\) nonzero entries this gives \(\operatorname{Lip}_\infty(R_U)\ge2-2/k>1\).

## Assumptions and scope

All matrices and vectors are real; \(d\) is any positive integer, with no genericity assumption on the orthogonal matrix. The map is *Euclidean* nearest-point projection, while its stability is measured in the distinct coordinate maximum norm. The classification is of the entire class of square orthogonal ReLU-conjugated projectors, not of arbitrary tight frames, rectangular layers, or every proximal activation. Zero sign coordinates are included by continuity. Row/column sign and permutation operations in statement 3 describe matrices, not invariance of any chosen active chamber.

## Proof

**1. Projection formula and exact chamber reduction.** Since \(U\) is a Euclidean isometry and nearest-point projection onto the nonnegative orthant acts coordinatewise, the displayed formula is the unique Euclidean nearest-point projector onto \(U^{\mathsf T}\mathbb R_+^d\). For each \(S\subseteq\{1,\ldots,d\}\), put \(D_S=\operatorname{diag}(1_{i\in S})\). Every strict sign chamber \(\{x:(Ux)_i>0\ (i\in S),\ (Ux)_i<0\ (i\notin S)\}\) is nonempty because \(U\) is onto. On that chamber, \(R_U(x)=U^{\mathsf T}D_SUx\). On any segment the map is continuous and piecewise linear, so an upper bound by \(\max_S\|U^{\mathsf T}D_SU\|_{\infty\to\infty}\) follows by splitting the segment (or integrating the a.e. derivative). Conversely, inside any chamber, sufficiently small perturbations in an induced norming direction realize the corresponding operator norm as a finite-input quotient. Therefore
\[
\operatorname{Lip}_\infty(R_U)=\max_{S\subseteq[d]}\|U^{\mathsf T}D_SU\|_{\infty\to\infty},\qquad
\|A\|_{\infty\to\infty}=\max_j\sum_k|A_{jk}|.
\]
The all-active chamber gives coefficient at least one.

**2. Necessary row flatness and support size.** Let \(u\) be any row of \(U\) regarded as a unit column. Taking the singleton active mask gives the rank-one projector \(P=uu^{\mathsf T}\). Its row-sum norm is
\[
\|P\|_{\infty\to\infty}=\|u\|_\infty\|u\|_1\ge\sum_j|u_j|^2=1.
\]
If the assumed global coefficient is at most one, equality holds. Equality in this elementary weighted-maximum inequality means that every nonzero \(|u_j|\) equals the maximum magnitude. If there are \(k\) nonzeros, each has magnitude \(k^{-1/2}\).

Taking the complementary active mask gives \(I-P\). At any supported coordinate its absolute row sum is
\[
1-|u_j|^2+|u_j|\sum_{h\ne j}|u_h|
=1+|u_j|\|u\|_1-2|u_j|^2=2-\frac2k.
\]
Consequently \(2-2/k\le1\), forcing \(k\le2\). This also establishes the quantitative certificate in the finding: both rank-one and rank-one-complement masks actually occur as chamber Jacobians, and the row-sum expression remains valid without flatness.

**3. Orthogonality forces disjoint complete blocks.** If a row is supported on one coordinate, column normalization forces every other row to vanish on that coordinate. If a row has the two-coordinate support \(\{a,b\}\), its nonzero entries have equal magnitude \(1/\sqrt2\). Any other admissible row touching either coordinate cannot be a singleton and cannot have a different two-point support: in either case its inner product with the first row would be nonzero. The norm-one columns therefore require a second row, with exactly the same two-point support, which is its orthogonal partner. These two rows form a signed and permuted copy of \(H\). No other row touches this pair. Repeating over columns produces exactly the block decomposition in statement 3.

**4. Sufficiency.** On a one-dimensional block, every zero–one mask projector is either zero or identity. On a normalized two-dimensional Hadamard block, the four masks give zero, identity, or one of the two rank-one projectors \(\frac12\begin{pmatrix}1&\pm1\\\pm1&1\end{pmatrix}\), each of which has absolute row sum at most one. Signed permutations preserve these operator norms. Thus every chamber derivative has norm at most one; part 1 proves global nonexpansivity and the all-active chamber proves exact coefficient one. The contrapositive of parts 2–3 shows strict expansivity for every matrix outside the classified family. \(\square\)

## Verification

The analytic argument covers all dimensions, all orthogonal matrices, every chamber and all boundary inputs. `checker.py` is an independently executable supplementary check; it enumerates every sign mask in several low dimensions, tests exact block constructions to numerical tolerance, verifies a flat three-support row's rational \(4/3\) complementary projection norm, and tests random orthogonal matrices. Execute with `python checker.py` using NumPy. The checker output is not used as evidence that finitely many tests prove the universal theorem.

## Relationship to prior work

Hasannasab, Hertrich, Neumayer, Plonka, Setzer and Steidl (arXiv:1912.10480, first public December 19, 2019) establish Hilbert-norm nonexpansivity for a much larger proximal-network framework; their displayed stability statements concern the Hilbert norm and do not directly give the coordinate maximum-norm classification here. Anil, Lucas and Grosse (arXiv:1811.05381) examine Lipschitz-constrained orthogonal neural architectures and discuss the maximum-row-sum matrix norm, but their identified ReLU expressivity obstruction is a different statement. Randrianantoanina's survey (arXiv:math/0110171) documents classical norm-one projection theory and the relevant broader basis-theoretic setting. The present criterion is also an orthonormal-basis suppression-unconditionality criterion for \(\ell_\infty^d\). Classical sources could contain an equivalent formulation under that terminology; no exhaustive priority assertion is made.

## Limitations

This is not a result for rectangular Parseval frames or multiple nonlinear layers with possible cancellations, and it does not classify the exact coefficient when it exceeds one. The statement concerns single-layer Euclidean orthant projection evaluated in the real coordinate maximum norm, not general \(\ell_p\) metric projection. The literature comparison is bounded, and possible earlier equivalent unconditional-basis characterizations remain a priority risk. No independent mathematical audit has been performed.

## References

1. M. Hasannasab, J. Hertrich, S. Neumayer, G. Plonka, S. Setzer, G. Steidl, *Parseval Proximal Neural Networks*, arXiv:1912.10480, first posted December 19, 2019, https://arxiv.org/abs/1912.10480.
2. C. Anil, J. Lucas, R. Grosse, *Sorting Out Lipschitz Function Approximation*, arXiv:1811.05381, first posted November 13, 2018, https://arxiv.org/abs/1811.05381.
3. B. Randrianantoanina, *Norm One Projections in Banach Spaces*, arXiv:math/0110171, first posted October 16, 2001, https://arxiv.org/abs/math/0110171.
