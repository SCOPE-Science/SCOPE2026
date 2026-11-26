# Coordinate-scaled homomorphisms and pointed-transformation spectra of finite regular \(L\)-algebras

## Finding

Every homomorphism between finite regular \(L\)-algebras has a coordinate normal form in the finite Young-diagram representation of Dietzel, Menchón, and Vendramin. After reversing the signs of the negative-cone coordinates, these algebras are finite, nonempty, coordinatewise downward-closed sets \(D\subseteq\mathbb N^m\), with logical unit \(\mathbf0\) and operation
\[
 a\mathbin{\bullet}b=((b_i-a_i)^+)_{i=1}^{m},\qquad t^+=\max(0,t).
\]
Here and below the coordinate systems are reduced by removing coordinates identically zero on the whole diagram.

**Coordinate normal-form theorem.** If \(D\subseteq\mathbb N^m\) and \(E\subseteq\mathbb N^s\) are any such finite diagrams, then a map \(f:D\to E\) is an \(L\)-homomorphism if and only if, for each output coordinate \(j\), either \(f(a)_j=0\) for every \(a\in D\), or there are a source coordinate \(i= i(j)\) and an integer \(k_j\ge1\) such that
\[
 f(a)_j=k_j a_i\quad(a\in D),
\]
with the combined coordinate map taking every element of \(D\) into \(E\). A finite inclusion test is enough: the image lies in \(E\) if and only if the image of **every maximal vector of \(D\)** lies in \(E\).

**Shape-independent rectangular-target census.** Write \(r_i=\max_{a\in D}a_i\ge1\). If \(E\) is the full integer box \(\prod_{j=1}^s\{0,\ldots,t_j\}\), where \(t_j\ge1\), then
\[
 \boxed{\left|\operatorname{Hom}(D,E)\right|=\prod_{j=1}^{s}\left(1+\sum_{i=1}^{m}\left\lfloor\frac{t_j}{r_i}\right\rfloor\right).}
\]
In particular, this cardinality depends only on the coordinate maxima of \(D\): filling all missing corners of \(D\) up to its bounding box changes neither its hom-set cardinality nor the available coordinate-choice patterns for a box target.

**Pointed-transformation and retract spectra.** For integers \(r,m\ge1\), let \(Q_{r,m}=\{0,\ldots,r\}^m\) with the operation above. Its endomorphism monoid is anti-isomorphic to the full transformation monoid on \(\{0,1,\ldots,m\}\) fixing \(0\). Let \(\left\{\begin{smallmatrix}u\\v\end{smallmatrix}\right\}\) denote a Stirling number of the second kind and \(B_u\) a Bell number. Then
\[
 \boxed{\left|\operatorname{End}(Q_{r,m})\right|=(m+1)^m,\qquad
 \operatorname{Aut}(Q_{r,m})\cong S_m.}
\]
The complete rank spectra of all endomorphisms, idempotent endomorphisms, and distinct embedded retract images are respectively
\[
 \boxed{\sum_{e\in\operatorname{End}(Q_{r,m})}z^{|e(Q_{r,m})|}
 =\sum_{k=0}^{m}\binom mk k!\left\{\begin{smallmatrix}m+1\\k+1\end{smallmatrix}\right\}z^{(r+1)^k},}
\]
\[
 \boxed{\sum_{e^2=e}z^{|e(Q_{r,m})|}
 =\sum_{k=0}^{m}\binom mk(k+1)^{m-k}z^{(r+1)^k},}
\]
\[
 \boxed{\sum_{\text{distinct retract }R\subseteq Q_{r,m}}z^{|R|}
 =\sum_{k=0}^{m}\left\{\begin{smallmatrix}m+1\\k+1\end{smallmatrix}\right\}z^{(r+1)^k}.}
\]
In particular, there are exactly \(B_{m+1}\) distinct embedded retracts. For \(m=3\), the endomorphism, idempotent, and retract totals are respectively \(64\), \(23\), and \(15\), independent of \(r\ge1\), even though the algebra has \((r+1)^3\) elements.

## Assumptions and scope

The classification is for **finite regular \(L\)-algebras**, not arbitrary \(L\)-algebras and not general \(\ell\)-groups. In the published representation [1, Theorem 5.9], every finite regular \(L\)-algebra is represented, uniquely up to coordinate permutations, by a finite upward-closed subset of the negative cone of a finitely generated free abelian lattice-ordered group. Replacing each negative coordinate \(x_i\) by \(a_i=-x_i\) gives precisely the finite downsets and positive-difference operation used here. The regularity hypothesis is structural: nothing here asserts that every finite \(L\)-algebra has such a normal form.

Allowing an empty list of active source coordinates covers the one-element diagram \(D=\{\mathbf0\}\): there is then exactly one homomorphism to any \(E\), the zero map. An empty list of active target coordinates similarly gives the one-element codomain and its unique constant-zero homomorphism. The rectangular formulas and pointed-transformation statement assume strictly positive side lengths as specified.

The rank of an endomorphism is its **image cardinality**, not vector-space rank. Retracts are counted as different **embedded subsets**, not only as abstract isomorphism types. The Stirling formulas count finite set partitions; the index containing the distinguished zero is essential.

## Proof

**1. Reduction to integer downsets.** In the negative cone of \(\mathbb Z^m\) the operation of [1, Section 5] is \(x\cdot y=\min(0,y-x)\) coordinatewise. On writing \(x=-a\), \(y=-b\), negating its value gives \((b-a)^+\). An upward-closed set in the negative cone becomes a downward-closed set in \(\mathbb N^m\). A downset is closed under positive-difference because \((b-a)^+\le b\). Thus the sign change is an isomorphism of the relevant binary-operation structures, and all subsequent calculations are performed in their concrete downset form.

**2. Homomorphisms into one coordinate.** Let \(h:D\to\mathbb N\) be the \(j\)-th coordinate of a homomorphism into a diagram \(E\). For every \(a\in D\), \(a\bullet a=\mathbf0\) and \(h(a)\bullet h(a)=0\), so \(h(\mathbf0)=0\). Since the source coordinate \(i\) is active, its unit vector \(\mathbf e_i\) belongs to \(D\); set \(c_i=h(\mathbf e_i)\ge0\).

For distinct \(i,j\) we have \(\mathbf e_i\bullet\mathbf e_j=\mathbf e_j\). After applying \(h\),
\[
 c_j=(c_j-c_i)^+.
\]
If \(c_j>0\), this forces \(c_i=0\). Therefore **at most one** of the integers \(c_i\) can be positive.

For any \(a\in D\) with \(a_i\ge1\), downward closure gives \(a-\mathbf e_i\in D\), and direct calculation gives
\[
 a\bullet(a-\mathbf e_i)=\mathbf0,
 \qquad(a-\mathbf e_i)\bullet a=\mathbf e_i.
\]
The first equality, under \(h\), implies \(h(a-\mathbf e_i)\le h(a)\). The second implies
\[
 h(a)-h(a-\mathbf e_i)=c_i.
\]
Iterating these exact increments from \(\mathbf0\) along any coordinatewise path to \(a\),
\[
 h(a)=\sum_{i=1}^{m}c_i a_i.
\]
Since at most one coefficient is positive, \(h\) is either zero or a positive integer multiple of one coordinate. This proves the necessity part simultaneously for all output coordinates.

**3. Converse and maximal-vector criterion.** Each map \(a\mapsto k a_i\) preserves positive differences because, for \(k\ge1\),
\[
 k(b_i-a_i)^+=(kb_i-ka_i)^+.
\]
The zero map also preserves them. Therefore any assembled output-coordinate choices preserving the condition \(f(D)\subseteq E\) define an \(L\)-homomorphism. Such maps are coordinatewise monotone. Every element of finite \(D\) is below some maximal element. Since \(E\) is a downset, checking inclusion of only those maximal-element images is both necessary and sufficient. This proves the full hom-set normal form, including arbitrary nonrectangular targets.

**4. Rectangular target and shape invariance.** For a given output coordinate with bound \(t_j\), the zero choice is available. If it uses source coordinate \(i\) with coefficient \(k\ge1\), then every value lies in the target range precisely when \(kr_i\le t_j\). Necessity follows since \(r_i\mathbf e_i\in D\): it lies below a vector attaining the coordinate maximum. Sufficiency follows from \(a_i\le r_i\) for all \(a\in D\). Thus there are exactly \(\lfloor t_j/r_i\rfloor\) choices involving source coordinate \(i\), in addition to zero. These choices are mutually distinct since the vectors \(\mathbf e_i\) are present. As the target is a **full** product, the choices across output coordinates are independent; multiplication gives the formula. Note that the full-product assumption belongs only to the target: the source need not be a box.

**5. Homogeneous boxes as pointed transformation monoids.** If every source and target side bound equals \(r\), the inequality \(kr\le r\) allows only the coefficient \(k=1\). Thus each output coordinate is either zero or a selected input coordinate. Adjoin a formal coordinate \(a_0=0\). Every endomorphism is uniquely
\[
 f_\tau(a)_j=a_{\tau(j)},\qquad \tau:\{0,\ldots,m\}\to\{0,\ldots,m\},\quad\tau(0)=0.
\]
Direct composition gives \(f_\sigma\circ f_\tau=f_{\tau\circ\sigma}\), hence the asserted anti-isomorphism. Bijective such maps are precisely the permutations of the \(m\) nonzero coordinate indices, giving \(\operatorname{Aut}\cong S_m\).

If exactly \(k\) distinct nonzero input indices occur among the selected outputs, then the image contains exactly \((r+1)^k\) vectors. First choose the \(k\) input indices in \(\binom mk\) ways. Conditional on their being used, the \(m\) output labels map onto all \(k\) selected indices, with optional zero. Adjoining a distinguished extra output fixed at zero identifies these assignments with partitions of \(m+1\) points into \(k+1\) blocks, whose \(k\) nonzero blocks are labeled. There are \(k!\left\{\begin{smallmatrix}m+1\\k+1\end{smallmatrix}\right\}\) such choices. This proves the complete endomorphism rank polynomial.

An endomorphism is idempotent precisely when every nonzero index selected by some output is itself a fixed coordinate: \(\tau(\tau(j))=\tau(j)\). Choose \(k\) fixed indices. Each of the other \(m-k\) outputs may choose any fixed index or zero, in \((k+1)^{m-k}\) ways. Its image again has size \((r+1)^k\), giving the idempotent rank polynomial.

Finally an idempotent image is a set of vectors whose coordinates are zero on one distinguished block (which contains the formal index \(0\)) and equal within each of the other blocks, the values of different blocks varying independently in \(\{0,\ldots,r\}\). Every partition of \(\{0,\ldots,m\}\) arises: choose one coordinate in each nonzero block as a fixed representative and copy it to that block's other coordinates. Distinct partitions yield distinct image subsets because \(r\ge1\). A partition with \(k+1\) blocks has image size \((r+1)^k\). This yields the retract rank polynomial and the total \(B_{m+1}\).

## Verification

The self-contained standard-library program `verify.py`, included alongside this result, constructs finite coordinate downsets, independently exhausts all possible maps in small cases, compares the survivors to the predicted coordinate maps, checks \(1{,}444\) source–target rectangular pairs, and checks endomorphism, idempotent, and retract-image rank spectra of homogeneous boxes through four coordinates (several side lengths). Its completed replay returned:

`VERIFY_OK 2593 independent exact comparisons; 11064 scalar maps; 9033 small downset-pair maps; 1444 rectangular pairs; homogeneous endomorphism/retract spectra m<=4`

The script checks the operation on every ordered argument pair for each enumerated candidate map. Its small-case enumeration is deliberately independent of the proof's coordinate arguments. These tests supplement, but do not replace, the general proof above.

## Relationship to prior work

Dietzel–Menchón–Vendramin [1, Theorem 5.9] establish the Young-diagram representation and classification of **isomorphism types** for all finite regular \(L\)-algebras. Section 2 defines homomorphisms; Section 5 derives the representation and the coordinate-permutation criterion for isomorphisms, but does not furnish the above classification of arbitrary noninjective homomorphisms, the shape-independent rectangular-target hom-set formula, or the pointed-transformation and rank/retract polynomials. Those are the additional claims proved here. Rump [2] supplies the underlying lattice-ordered-group structural machinery; his full text was not available for comprehensive comparison, so an implicit antecedent there remains possible.

Related general literature on operators on \(L\)-algebras [3] studies closure and other operators but, in its accessible abstract, does not assert a coordinate normal form for every map between finite regular examples. The named formulas are also distinct from the earlier Bell-number enumeration of **linear** \(L\)-algebra isomorphism classes [1, Section 4]: here the Bell number counts **embedded retracts of a fixed homogeneous regular algebra**, a different invariant and class.

## Limitations

This is an exact theorem with an elementary proof once the published finite Young-diagram representation is granted; it is **not** a new representation theorem and does not apply to all finite \(L\)-algebras. The box target is essential for the independent-product cardinality formula. For nonrectangular targets one must impose the joint maximal-vector membership test, rather than multiply individual output-coordinate counts. The finite verifier does not establish the theorem in all sizes. The originality search cannot rule out unindexed finite-algebra folklore or an implicit consequence of Rump's unavailable full text. Independent mathematical audit has not yet been performed.

## References

[1] C. Dietzel, P. Menchón, L. Vendramin, *On the enumeration of finite \(L\)-algebras*, arXiv:2206.04955, initial public version 2022-06-10; *Mathematics of Computation* **92** (2023), 1363–1381. https://arxiv.org/abs/2206.04955 ; https://arxiv.org/html/2206.04955v4 ; DOI:10.1090/mcom/3814. Published 2020 MSC primary 03G25.

[2] W. Rump, *\(L\)-algebras, self-similarity, and \(\ell\)-groups*, *Journal of Algebra* **320** (2008), 2328–2348, DOI:10.1016/j.jalgebra.2008.05.033. Structural background cited by [1]; full paper not inspected.

[3] Q. Zhan, A. Borumand Saeid, B. Davvaz, *Operators on \(L\)-algebras*, *Journal of Intelligent & Fuzzy Systems* **46** (2024), DOI:10.3233/JIFS-234370; accessible abstract consulted. https://journals.sagepub.com/doi/abs/10.3233/JIFS-234370 .
