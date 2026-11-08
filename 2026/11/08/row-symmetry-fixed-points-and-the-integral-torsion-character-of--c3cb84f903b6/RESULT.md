# Row-symmetry fixed points and the integral torsion character of a multiple chessboard family

## Finding

For every integer \(m\geq5\), let \(X_m\) be the simplicial complex whose vertices are rook positions \((r,j)\) with \(r\in\{1,2,3,4,5\}\) and \(j\in\{1,\ldots,m\}\). A set of positions is a face precisely when no column is used twice, each of the first four rows is used at most once, and the fifth row is used at most \(m-4\) times. Row permutations \(S_4\) on the first four rows and column permutations \(S_m\) act simplicially and commute.

**Theorem (integral torsion character and all proper row-symmetry fixed-point types).** The unique torsion subgroup in reduced integral homology is
\[
\operatorname{Tor}\widetilde H_{m-3}(X_m;\mathbb Z)\cong\mathbb Z/3,
\qquad (\rho,\sigma)\cdot z=\operatorname{sgn}(\rho)\operatorname{sgn}(\sigma)\,z.
\]
For every nonidentity subgroup \(H\leq S_4\), write \(k\in\{0,1,2\}\) for the number of rows of \(\{1,2,3,4\}\) fixed individually by all elements of \(H\). Then the *geometric* fixed-point space has homotopy type
\[
|X_m|^H\simeq\bigvee^{\beta_k(m)} S^{m-5+k},
\]
where
\[
\begin{aligned}
\beta_0(m)&=\binom{m-1}{3},\\
\beta_1(m)&=m\binom{m-2}{2}-\binom{m-1}{3},\\
\beta_2(m)&=m(m-3)+\binom{m-1}{3}.
\end{aligned}
\]
All displayed wedge multiplicities are positive. In particular, all nonidentity row-subgroup fixed spaces have torsion-free integral homology even though the ambient complex has three-torsion.

## Assumptions and scope

The columns have capacity one. The four distinguished unit-capacity rows are permuted by \(S_4\); the last row is fixed by this subgroup. For \(m=5\) all five row capacities happen to equal one, but the designated \(S_4\) subgroup is still well-defined. A *geometric* fixed point of \(H\) means a point of the polyhedron fixed by every group element, not merely a vertex in a fixed-vertex subcomplex. Reduced homology is with integral coefficients unless another ring is indicated. The theorem does not identify the full equivariant homotopy type of \(X_m\).

## Proof

**1. Fixed-point identification.** Let \(H\leq S_4\) be nonidentity. If a row \(r\) is moved by some \(h\in H\), the orbit of any rook vertex \((r,j)\) contains both \((r,j)\) and \((h(r),j)\). These two vertices occupy the same column, hence cannot belong to a common simplex. Any point in a geometric simplex fixed by \(H\) has a barycentric support that is an \(H\)-invariant face. Therefore its support contains no vertex in a moved row. Conversely every rook vertex in a row fixed individually by \(H\), or in row five, is fixed. Thus \(|X_m|^H\) is the geometric realization of the full subcomplex using precisely those \(k\) unit rows and the fifth row. It is \(Y_{m,k}=\Delta_{[m]}^{(1^k,m-4)}\). A nonidentity permutation of four letters fixes at most two letters, so \(k\in\{0,1,2\}\).

**2. Homotopy of fixed-point complexes.** Each maximal face of \(Y_{m,k}\) uses all \(k\) unit rows and \(m-4\) positions in the heavy row; this is achievable since \(k\leq2\). Indeed any smaller face can be extended until these capacities are saturated, as the total capacity \(m-4+k\) is at most \(m\). The complex is pure of dimension \(d=m-5+k\). The shellability theorem of Jojić–Vrećica–Živaljević (Theorem 4.4 in arXiv:1412.0386) applies since its condition for \(k+1\) rows reads
\[
m\geq(m-4+k)+(k+1)-1=m-4+2k,
\]
which holds for all \(k\leq2\). Therefore \(Y_{m,k}\) has the homotopy type of a wedge of \(d\)-spheres, including \(d=0\) in the case \(m=5,k=0\).

To compute the multiplicity without assuming a homology table, count faces of size \(j\):
\[
f_{j-1}(Y_{m,k})=\sum_{\substack{0\leq a\leq k\\0\leq j-a\leq m-4}}\binom ka(m)_a\binom{m-a}{j-a},\qquad (m)_a=\frac{m!}{(m-a)!},
\]
where \(f_{-1}=1\). Choosing \(a\) unit rows, placing their rooks injectively into columns, and choosing the heavy-row columns proves this equality. Alternating the count and using
\[
\sum_{b=0}^{m-4}(-1)^b\binom{m-a}{b}=(-1)^{m-4}\binom{m-a-1}{m-4}
\]
for \(0\leq a\leq2\) yields
\[
\beta_k(m)=(-1)^k\sum_{a=0}^{k}(-1)^a\binom ka(m)_a\binom{m-a-1}{m-4}.
\]
Substituting \(k=0,1,2\) simplifies to the three displayed formulas. Since the complexes are pure and shellable, reduced Euler characteristic determines the sphere count; this establishes the complete fixed-point homotopy classification and torsion-freeness.

**3. Torsion and its symmetry.** Theorem 5.7 of Limonchenko–Yu (arXiv:2610.37827, first posted October 27, 2026) proves that \(\operatorname{Tor}\widetilde H_{m-3}(X_m;\mathbb Z)\) is exactly cyclic of order three. We examine the naturality of the integral relative-chain presentation in its proof, rather than infer a group action from the abstract abelian-group isomorphism. Equations (5.10)–(5.11) reduce the relevant cokernel to two families \(r_D^{(2)}\) and \(r_D^{(3)}\), indexed by three-element column subsets \(D\), with incidence relations
\[
\sum_{\substack{D\supseteq T\\|D|=3}}r_D^{(a)}=0\quad (|T|=1,2;\ a=2,3),
\qquad \sum_D\bigl(r_D^{(2)}+r_D^{(3)}\bigr)=0.
\]
Each of the sums \(q^{(2)}=\sum_D r_D^{(2)}\) and \(q^{(3)}=\sum_D r_D^{(3)}\) is a class in the cokernel; the cited proof shows that \(q^{(2)}\) generates its unique order-three subgroup. The last relation is \(q^{(3)}=-q^{(2)}\). Swapping the second and third unit-capacity rows interchanges the two families *without changing column order*, and hence sends the order-three generator to its negative. Since the resulting action \(S_4\to\operatorname{Aut}(\mathbb Z/3)\cong C_2\) is a group homomorphism, and all transpositions of \(S_4\) are conjugate, the action of \(S_4\) is its sign character.

For the column group, choose the basis words used in (5.10)–(5.11) with exterior factors ordered increasingly by column. The representative \(R_{D,p}^{(2)}\) consists of one difference factor from *every* column (two of type \(x\), one of type \(y\), and \(m-3\) of type \(z\) in the notation of the cited proof). A permutation \(\sigma\in S_m\) carries it to \(\operatorname{sgn}(\sigma)R_{\sigma D,\sigma p}^{(2)}\) upon reordering all \(m\) exterior factors. The cokernel relations make the image of \(R_{D,p}^{(2)}\) independent of the chosen \(p\in D\). Consequently the symmetric sum \(q^{(2)}\) transforms by \(\operatorname{sgn}(\sigma)\). Combining the commuting row and column actions gives the stated product-sign representation. Every step is valid over \(\mathbb Z\), and the last sign is interpreted modulo three on the torsion class.

## Verification

The accompanying `verify.py` reconstructs the ordinary five-by-five chessboard case \(m=5\) from all \(1545\) nonempty faces as signed simplicial chains, performs exact linear algebra over \(\mathbb F_3\), and checks that exchanging either two rows or two columns acts as multiplication by negative one on its one-dimensional degree-two mod-three homology. (The test is a mod-three corroboration, not a substitute for the integral presentation above.) The program separately reconstructs every face of \(Y_{m,k}\) for \(m\in\{5,6,7\}\), \(k\in\{0,1,2\}\), and computes its reduced mod-two homology ranks; all nine cases match the wedge dimensions and multiplicities. A third check constructs the two-family modular quotient presentation and checks the torsion generator and its two sign actions for \(5\leq m\leq9\). `requirements.txt` gives the NumPy dependency. `verify_output.txt` contains the exact observed output. The infinite-family statements follow from the proof, not finite extrapolation.

## Relationship to prior work

Theorem 5.7 and equations (5.10)–(5.11) of Limonchenko–Yu establish the ambient three-torsion and provide its relative integral presentation; that torsion-existence result is not claimed here as new. Theorem 4.4 of Jojić–Vrećica–Živaljević proves shellability for small-capacity multiple chessboard complexes; shellability alone does not identify them as every row-subgroup geometric fixed-point space of this torsion family. Jonsson (2010, arXiv:1203.5644, page 11) already obtains a sign action for a specified symmetry subgroup in the ordinary five-by-five chessboard case; that special-case sign observation is not claimed as new. The 2015 symmetrized-chessboard paper of Jojić–Vrećica–Živaljević studies *unions* of row-permuted complexes and connectivity, not these pointwise fixed spaces. The present claim is their joint uniform equivariant refinement for all \(m\geq5\), including the explicit fixed-point homotopy profile for every nontrivial subgroup and the complete row-and-column torsion character.

## Limitations

The result does not classify the free integral homology representations, other row-capacity vectors, the full \(S_5\) action in the accidental all-unit-row case, or a fully equivariant wedge/Moore-space splitting. The fixed-point equivalences are ordinary (nonequivariant) homotopy equivalences of the fixed spaces, not a claimed coherent equivariant homotopy equivalence for the ambient action. The first theorem uses the publicly available 2026 torsion preprint as an input. Independent external validation has not been performed, and an equivalent unindexed statement remains an originality risk.

## References

1. I. Limonchenko and S. Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, arXiv:2610.37827v1 (first public October 27, 2026), Theorem 5.7 and equations (5.10)–(5.11), https://arxiv.org/abs/2610.37827.
2. D. Jojić, S. T. Vrećica and R. T. Živaljević, *Multiple chessboard complexes and the colored Tverberg problem*, arXiv:1412.0386, Theorem 4.4, https://arxiv.org/abs/1412.0386.
3. J. Jonsson, *On the 3-torsion Part of the Homology of the Chessboard Complex*, arXiv:1203.5644, page 11 (older journal publication, *Annals of Combinatorics* 14 (2010)), https://arxiv.org/abs/1203.5644.
4. D. Jojić, S. Vrećica and R. Živaljević, *Symmetric multiple chessboard complexes and a new theorem of Tverberg type*, arXiv:1502.05290, https://arxiv.org/abs/1502.05290.
