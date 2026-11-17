# An equivariant representation sphere for the diagonal-avoiding multiway relational product

## Finding

For integers \(n\ge2\) and \(r\ge3\), define the \(r\)-way relation
\[
R_{n,r}=[n]^r\setminus\{(i,\ldots,i):i\in[n]\}.
\]
Let \(\mathcal D(R_{n,r})\) be its **relational prod-complex**: the cell \(\sigma_1\times\cdots\times\sigma_r\) is present exactly when all \(\sigma_j\) are nonempty subsets of \([n]\) and their Cartesian product lies in \(R_{n,r}\). Its realization \(X_{n,r}\) has a natural action of \(S_n\times S_r\) by simultaneous relabeling and by permuting factors.

**Theorem.** There is an explicit \(S_n\times S_r\)-equivariant homeomorphism
\[
X_{n,r}\ \cong\ S(U_n\otimes U_r),
\qquad U_k=\ker\bigl(\mathbb R^k\xrightarrow{\mathrm{sum}}\mathbb R\bigr).
\]
Consequently \(X_{n,r}\) is a sphere of dimension \((n-1)(r-1)-1\), and its top integral homology is \(\mathbb Z\) with character
\[
(\sigma,\tau)\longmapsto
(\operatorname{sgn}\sigma)^{r-1}(\operatorname{sgn}\tau)^{n-1}.
\]
For every subgroup \(H\le S_n\times S_r\), let \(o_n,o_r,o_{nr}\) be the numbers of orbits on \([n]\), on \([r]\), and on \([n]\times[r]\). Define
\[
e(H)=o_{nr}-o_n-o_r+1.
\]
Then \(e(H)\ge0\) and
\[
X_{n,r}^{H}\cong
\begin{cases}
\varnothing,&e(H)=0,\\
S^{e(H)-1},&e(H)>0.
\end{cases}
\]
These are genuine geometric fixed spaces, not just the invariant part of homology. For instance \(X_{2,3}\cong S^1\), \(X_{3,3}\cong S^3\), and \(X_{3,4}\cong S^5\); the full symmetry group has an empty fixed-point space in every case.

## Assumptions and scope

The dimensions \(n\) and \(r\) are integers with \(n\ge2\) and \(r\ge3\). The target is the *symmetric relational prod-complex* of the displayed relation, not a one-factor simplicial Dowker quotient. A point in \(X_{n,r}\) consists of \(r\) probability vectors \(x_j=(x_{j1},\ldots,x_{jn})\) with \(x_{ji}\ge0\), \(\sum_i x_{ji}=1\), and \(\min_j x_{ji}=0\) for every column \(i\). Indeed, a point belongs to some allowed product cell precisely when its row-support sets have empty total intersection. All group actions are on actual realizations; tensor factors and indices may be interchanged by a fixed coordinate identification.

## Proof

**1. Linear representation and a positive gauge.** Identify the real tensor product \(U_r\otimes U_n\) with
\[
W=\left\{z\in\mathbb R^{r\times n}:\sum_i z_{ji}=0\ (1\le j\le r),\ \sum_jz_{ji}=0\ (1\le i\le n)\right\}.
\]
It has dimension \(d=(r-1)(n-1)\). Relabeling columns and rows gives the stated \(S_n\times S_r\)-representation. On \(W\) define
\[
F(z)=-\sum_{i=1}^{n}\min_{1\le j\le r}z_{ji}.
\]
Because the sum of every column is zero, each column minimum is nonpositive. If \(F(z)=0\), every entry in every column is nonnegative, and the column sums force every entry to vanish. Thus \(F(z)>0\) whenever \(z\ne0\). The function is continuous, invariant under both permutation groups, positively homogeneous, and convex because it is a sum of maxima of linear forms. More explicitly,
\[
F(z)=\max_{(j_1,\ldots,j_n)\in[r]^n}\left(-\sum_{i=1}^nz_{j_i i}\right).
\]
Therefore \(B=\{z\in W:F(z)\le1\}\) is a compact full-dimensional convex polytope containing zero in its interior, and its boundary is \(F^{-1}(1)\). Compactness follows also directly because \(F\) has a strictly positive minimum on the Euclidean unit sphere of \(W\).

**2. Exact inverse maps.** For \(x\in X_{n,r}\), form its column averages and double-centering
\[
\bar x_i=\frac1r\sum_{j=1}^{r}x_{ji},\qquad
z_{ji}=x_{ji}-\bar x_i.
\]
Each column of \(z\) sums to zero. Also each row of \(z\) sums to \(1-r^{-1}\sum_{j',i}x_{j'i}=0\), hence \(z\in W\). Because each column of \(x\) has minimum zero,
\[
\min_j z_{ji}=-\bar x_i,
\qquad F(z)=\sum_i\bar x_i=1.
\]
This defines a continuous equivariant map \(T:X_{n,r}\to\partial B\).

Conversely, given \(z\in\partial B\), set
\[
x_{ji}=z_{ji}-\min_{1\le k\le r}z_{ki}.
\]
All entries are nonnegative and every column contains a zero. Moreover each row sums to \(-\sum_i\min_kz_{ki}=F(z)=1\), since every row of \(z\) sums to zero. Thus \(x\in X_{n,r}\). Its column average is \(-\min_kz_{ki}\), since each column of \(z\) sums to zero, so double-centering recovers \(z\). Conversely, applying this formula to the image of \(x\) recovers \(x\) because every column of \(x\) has minimum zero. The maps are continuous and commute with both permutation actions. Hence \(X_{n,r}\cong\partial B\) **equivariantly and homeomorphically**.

**3. Round sphere and integral orientation.** Positive homogeneity and positivity of \(F\) give mutually inverse equivariant radial maps \(\partial B\longleftrightarrow S(W)\), by \(z\mapsto z/\lVert z\rVert_2\) and \(w\mapsto w/F(w)\). Thus \(X_{n,r}\) is a representation sphere, not merely homotopy equivalent to one. The determinant identity for a Kronecker product gives
\[
\det(g\mid W)=\det(\sigma\mid U_n)^{r-1}\det(\tau\mid U_r)^{n-1}
=(\operatorname{sgn}\sigma)^{r-1}(\operatorname{sgn}\tau)^{n-1}.
\]
This determinant is the degree of the induced self-homeomorphism on \(S(W)\), proving the integral top-homology action. No other reduced integral homology occurs.

**4. Arbitrary subgroup fixed spaces.** Since the homeomorphism is equivariant, \(X_{n,r}^{H}\cong S(W)^H=S(W^H)\), with the latter empty exactly when \(W^H=0\). The permutation representation on matrix entries splits naturally over \(\mathbb R\) as
\[
\mathbb R^{[n]\times[r]}\cong
\mathbb R\ \oplus\ U_n\ \oplus\ U_r\ \oplus\ (U_n\otimes U_r).
\]
Taking \(H\)-invariants is exact over \(\mathbb R\). The invariant dimension of a permutation module equals the number of orbits of \(H\) on its underlying basis. Hence
\[
\dim W^H=o_{nr}-o_n-o_r+1=e(H).
\]
This proves both the nonnegativity and every claimed fixed-space dimension and completes the proof.

## Verification

The included independent finite checker `verification/check.py` directly enumerates every product cell by empty total support intersection, builds its cellular boundary matrices over \(\mathbb F_2\), and computes reduced Betti numbers in eight configurations (including the classical two-factor boundary cases). There are 3,660 enumerated product cells overall. Additional exact rational arithmetic reconstructs the gauge homeomorphism; determinant calculations test 16 symmetry generators; and 28 independently generated subgroup tests compare matrix-kernel dimensions against the orbit-count formula. The output is recorded in `verification/check_output.txt` and ends in `DIAGONAL_DOWKER_CHECK_PASS`. The code uses Python and SymPy. These finite computations are checks only: the preceding exact proof establishes all integers and integral claims.

## Relationship to prior work

De Silva, Giusti, Itskov, Robinson, Sazdanovic, Schonsheck, Vaupel and Yoon introduce multiway Dowker relational prod-complexes and prove a general homotopy equivalence with the associated quotients (Theorem 4.3.2 of their work). That general equivalence is taken as the framework, not claimed as a discovery. It neither gives this diagonal-complement relation's explicit representation-sphere homeomorphism nor determines integral orientation and **all** subgroup fixed spaces. In the two-factor case, deleted-product sphere phenomena are classical; the new claim concerns three or more factors and the complete symmetry geometry. The corresponding Tverberg literature often uses *pairwise disjoint* supports, a strictly different condition from empty *total* support intersection. Prior-work checks found no demonstrated theorem implying all the statements here; alternate indexing or terminology could still conceal overlap.

## Limitations

The conclusion concerns the relation obtained by excluding exactly the constant tuples from a full Cartesian power. It does not apply to arbitrary higher-order relations, nor to the pairwise-deleted-product subspace. It does not classify quotient-space integral torsion or actions on arbitrary one-factor Dowker quotient models. Independent mathematical validation has not been performed; finite experiments are not an infinite proof, and negative literature searches cannot guarantee novelty.

## References

- V. de Silva, C. Giusti, V. Itskov, M. Robinson, R. Sazdanovic, N. Schonsheck, M. Vaupel and I. H. R. Yoon, *Dowker's theorem for higher-order relations*, arXiv:2506.10909, first submitted June 12, 2025; *Journal of Applied and Computational Topology* **10**, article 11 (2026), https://doi.org/10.1007/s41468-026-00239-x. Full open-access text, especially Sections 3–6 and Theorem 4.3.2.
- P.-S. Simon, *Topological Tverberg Theorems for Products of Polytopes*, arXiv:2608.02979 (2026). Compared as literature on pairwise-deleted products; its condition differs from empty total support intersection.
