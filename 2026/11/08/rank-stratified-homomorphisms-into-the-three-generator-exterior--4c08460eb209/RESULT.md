# Rank-stratified homomorphisms into the three-generator exterior algebra

## Finding

Let \(k\) be a field, \(m\geq1\), and \(E_d(k)=\bigwedge_k(k^d)\), considered as a **unital associative algebra** (homomorphisms need not preserve the exterior grading). Every homomorphism \(E_m(k)\to E_3(k)\) has a linear-part map \(V:k^m\to k^3\), induced on augmentation ideals modulo their squares. Write \(r=\operatorname{rank}(V)\).

**Theorem.** In characteristic different from two, the rank-\(r\) locus of the reduced homomorphism variety is a vector bundle of rank
\[
 m(4-r)+\binom r2
\]
over the smooth irreducible variety of rank-\(r\) matrices in \(\operatorname{Hom}_k(k^m,k^3)\), for \(0\leq r\leq \min(m,3)\). It has dimension
\[
 d_r=4m+\frac{5r-r^2}{2}.
\]
Consequently, if \(m\geq3\), the reduced variety has dimension \(4m+3\) and **at least two distinct irreducible components of that maximal dimension**, the closures of the rank-two and rank-three loci. No assertion is made here that those are all components.

For \(k=\mathbb F_q\) of odd characteristic, the exact number with linear rank \(r\) is
\[
 H_{m,q}(r)=q^{m(4-r)+\binom r2}
 \frac{\prod_{i=0}^{r-1}(q^3-q^i)(q^m-q^i)}
 {\prod_{i=0}^{r-1}(q^r-q^i)},
\quad 0\leq r\leq\min(m,3).
\]
Empty products equal one. Summing over \(r\) gives the number of all unital homomorphisms, including non-surjective maps. For \(m\geq3\), surjections are exactly the rank-three maps; their number is
\[
 q^{m+3}\prod_{i=0}^{2}(q^m-q^i).
\]
In particular, at \(m=3\) the rank-three count is \(|\operatorname{GL}_3(q)|q^6\), the classical automorphism count.

In characteristic two the full homomorphism variety is the affine space \(\mathbb A_k^{7m}\): for \(\mathbb F_q\), its number of points is exactly \(q^{7m}\). This change in geometry and total count is genuine; the odd-characteristic formula must not be specialized to even \(q\).

## Assumptions and scope

The source and target are ordinary unital exterior algebras, not superalgebras with parity-preserving morphisms. The target dimension is fixed at three generators, while source rank \(m\) is arbitrary. The finite-field formula concerns individual labeled maps, not maps modulo automorphisms or isomorphism of images. For geometric assertions, the underlying reduced finite-type variety is meant; no claim about a possibly nonreduced homomorphism scheme at the lower-rank boundary is made.

## Proof

Let \(W=k^3\) and choose an oriented volume element \(\Omega\in\bigwedge^3W\). Each source generator is nilpotent; its image under a unital homomorphism must therefore have zero scalar part. Accordingly every possible generator image has a unique expression
\[
 u_i=v_i+w_i+t_i\Omega,\quad v_i\in W,\quad w_i\in\bigwedge^2W,\quad t_i\in k
\]
for \(1\leq i\leq m\). Set \(V(e_i)=v_i\). The volume form identifies \(\bigwedge^2W\) with \(W^*\), with \(w_i\leftrightarrow\phi_i\) defined by \(v\wedge w_i=\phi_i(v)\Omega\). Assemble \(\phi_i\) as the rows of \(\Phi:W\to(k^m)^*\).

Assume \(\operatorname{char}k\ne2\). The exterior multiplication rules give
\[
 u_i^2=2\phi_i(v_i)\Omega,\qquad
 u_i u_j+u_j u_i=2\bigl(\phi_i(v_j)+\phi_j(v_i)\bigr)\Omega\quad(i<j).
\]
All omitted products vanish by degree (any product involving \(\Omega\), except multiplication by a scalar, vanishes; likewise products of two degree-two terms). The universal defining relations of \(E_m(k)\) are precisely \(u_i^2=0\) and \(u_iu_j+u_ju_i=0\). Thus the images define a homomorphism **if and only if** the \(m\times m\) matrix \(\Phi V\) is alternating: \((\Phi V)_{ii}=0\) and \((\Phi V)_{ij}=-(\Phi V)_{ji}\). The \(m\) coefficients \(t_i\) are completely free.

Fix \(V:S=k^m\to W\) of rank \(r\), and let \(K=\ker V\). If \(A=\Phi V\) is alternating, then \(K\) is in its right radical and hence also its left radical. Therefore \(A\) uniquely descends to an alternating bilinear form on \(S/K\), of dimension \(r\). Conversely, each alternating form on \(S/K\) determines an \(A\) with \(K\subseteq\ker A\). The equation \(\Phi V=A\) then specifies \(\Phi\) uniquely on \(\operatorname{im}V\), and there are \(m(3-r)\) freely chosen coefficients for its extension to \(W\). Since alternating forms on an \(r\)-space form a vector space of dimension \(\binom r2\), the fiber in \((\Phi,(t_i))\) is an affine space of dimension \(m(3-r)+\binom r2+m\). The construction is algebraic in \(V\) and gives a vector bundle over the constant-rank matrix stratum (locally split using an invertible minor).

A rank-\(r\) \(3\times m\) matrix stratum is smooth irreducible of dimension \(r(3+m-r)\). Adding fiber dimension yields
\[
 r(3+m-r)+m(4-r)+\binom r2
 =4m+\frac{5r-r^2}{2}.
\]
The rank-two and rank-three strata (for \(m\geq3\)) each have dimension \(4m+3\), larger than ranks zero and one. Both are irreducible, so their closures are irreducible components of maximal dimension. The rank-two closure is contained in the closed determinantal locus \(\operatorname{rank}V\leq2\), whereas the rank-three closure meets \(\operatorname{rank}V=3\), making them distinct. This proves the claimed geometric conclusion without attempting a complete component classification.

Over \(\mathbb F_q\), the number of rank-\(r\) matrices \(V\) equals
\[
 \frac{\prod_{i=0}^{r-1}(q^3-q^i)(q^m-q^i)}
 {\prod_{i=0}^{r-1}(q^r-q^i)}.
\]
Multiplying by the affine-fiber count \(q^{m(4-r)+\binom r2}\) gives \(H_{m,q}(r)\). A homomorphism is surjective precisely when its induced map on augmentation ideals modulo their squares is surjective: the forward implication is clear, and the reverse follows by lifting generators through the nilpotent augmentation filtration (or Nakayama's lemma). Hence the rank-three formula.

Finally, in characteristic two \(E_3(k)\) is the commutative algebra \(k[x,y,z]/(x^2,y^2,z^2)\). Every element of its seven-dimensional augmentation ideal squares to zero. Thus **any** ordered \(m\)-tuple in that ideal satisfies the source exterior relations and gives a unique homomorphism. The parameter space is exactly \(\mathbb A^{7m}\).

## Verification

The accompanying `check_exterior_hom.py` checks the homomorphism relations by literal multiplication in the eight-dimensional exterior basis, using the signs of disjoint-subset products. It does not call the alternating-matrix criterion for the decision of whether a tuple is valid. For \(m=1,2\) over \(\mathbb F_3\), and \(m=1\) over \(\mathbb F_5\), it enumerates every linear/quadratic image pair, counts by linear rank, and compares with the formula (all cubic coefficients are independently free). It also enumerates the binary \(m=2\) case, and exhausts all quadratic possibilities above canonical representative linear maps of ranks zero through three for \(m=3\) over \(\mathbb F_3\). Every comparison passes. The recorded output is in `check_output.txt` and is reproducible with `python check_exterior_hom.py`.

Over \(\mathbb F_3\) for \(m=3\), the four rank counts are respectively \(531441\), \(6652854\), \(17740944\), and \(8188128\), totalling \(33113367\). Over \(\mathbb F_2\), \(m=3\) gives \(2^{21}=2097152\) maps (the latter count follows algebraically and was not exhaustively enumerated).

## Relationship to prior work

Djoković (1978) and Bavula (first public arXiv version 2007-03-12) determine important structures of derivations and **automorphism groups** of exterior algebras. In particular, Bavula's explicit description of \(\operatorname{Aut}(E_3)\) supplies the rank-three, \(m=3\) special case; it is prior work, not a novel corollary here. The statement assessed here treats **all** unital homomorphisms into \(E_3\), including every deficient-linear-rank stratum and its exact point count, and proves the coexistence of two maximal-dimensional reduced components. Those assertions do not follow from an automorphism-group order alone. Bruns and Conca (2007 preprint) study the closure of the map taking an ordinary linear transformation to its exterior power, a different parameter space from arbitrary algebra homomorphisms \(E_m\to E_3\).

## Limitations

The result does not determine every irreducible component, scheme-theoretic nilpotents, singularities, orbit classes, or homomorphism varieties into exterior algebras on more than three generators. Its originality assessment is a finite comparison against inspected references and searches, not a certification of absolute historical priority. General counting theories of quadratic algebras or homomorphism schemes could contain an equivalent formula not identified here. The computational checks are finite and do not replace the proof for all \(m\) and fields.

## References

- D. Ž. Djoković, *Derivations and automorphisms of exterior algebras*, Canadian Journal of Mathematics **30** (1978), 1336–1344, https://doi.org/10.4153/CJM-1978-111-5 (full nine-page text inspected; original first-public day not independently verified).
- V. V. Bavula, *The Jacobian map, the Jacobian group and the group of automorphisms of the Grassmann algebra*, arXiv:math/0703352v1, first publicly posted 2007-03-12, https://arxiv.org/abs/math/0703352 (full HTML text inspected, including the \(n=3\) automorphism decomposition and its monoid discussion).
- W. Bruns and A. Conca, *The variety of exterior powers of linear maps*, arXiv:0705.3399v1, first publicly posted 2007-05-23, https://arxiv.org/abs/0705.3399 (HTML text inspected; distinguished from algebra-homomorphism varieties).
