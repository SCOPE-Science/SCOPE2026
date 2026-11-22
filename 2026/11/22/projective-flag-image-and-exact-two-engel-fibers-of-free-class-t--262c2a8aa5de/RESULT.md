# Projective flag image and exact two-Engel fibers of free class-three Lie algebras

## Finding

Let \(q\) be any prime power and \(d\ge2\). Let \(L=\mathfrak f_{d,3}(\mathbb F_q)\) be the free nilpotent Lie algebra of class three on a \(d\)-dimensional generating space \(V\), with graded decomposition \(L=V\oplus L_2\oplus L_3\). Its dimension is
\[
D=d+\binom d2+\frac{d^3-d}{3}.
\]
For the *two-Engel Lie word map* \(E:L\times L\to L_3\), \(E(X,Y)=[X,[X,Y]]\), define for every one-dimensional subspace \(\ell=\langle x\rangle\) of \(V\) the subspace
\[
W_\ell=\{[x,[x,y]]:y\in V\}\subseteq L_3.
\]
Then \(W_\ell\) is independent of the choice of nonzero \(x\in\ell\), has dimension \(d-1\), and
\[
W_\ell\cap W_{\ell'}=\{0\}\quad(\ell\ne\ell').
\]
Thus \(\{W_\ell\}\) is a partial \((d-1)\)-spread in the degree-three free Lie component. The nonzero projective two-Engel values are in canonical bijection with incident point–line flags \(\ell\subset P\subset V\), where \(\dim\ell=1\) and \(\dim P=2\). In particular,
\[
\boxed{|\operatorname{im}E|=1+\frac{q^d-1}{q-1}(q^{d-1}-1).}
\]
Every prescribed target \(z\in L_3\) has one of exactly three possible fiber cardinalities:
\[
\boxed{
|E^{-1}(z)|=q^{2(D-d)}\begin{cases}
q^d+(q^d-1)q,&z=0,\\
q(q-1),&0\ne z\in\operatorname{im}E,\\
0,&z\notin\operatorname{im}E.
\end{cases}}
\]
The probability that two independently uniform elements satisfy the two-Engel identity is exactly
\[
\boxed{\Pr([X,[X,Y]]=0)=q^{1-d}+q^{-d}-q^{1-2d}.}
\]
When \(d=2\), the Engel word map is onto \(L_3\), and every nonzero target has the same fiber size. For \(d\ge3\) it has a proper image, supported on the flag-parametrized cone described above.

## Assumptions and scope

This is a theorem for the **free** class-three nilpotent Lie algebra over **every finite field**, including characteristics two and three. A free Lie algebra is understood as an alternating Lie algebra satisfying the universal mapping property, so it embeds in the tensor algebra with bracket \([u,v]=uv-vu\). There are no restrictions on the rank \(d\) except \(d\ge2\). The map takes ordered pairs of arbitrary elements of the entire algebra, not only generators, and the target is its central homogeneous degree-three layer. No assertion about Engel word maps on arbitrary nilpotent Lie algebras or groups is made.

The association \(\ell\mapsto W_\ell\) is well-defined since replacing \(x\) by \(a x\) with \(a\ne0\) multiplies all outputs by \(a^2\), leaving their linear span unchanged. A point–line flag here refers to a one-dimensional subspace inside a two-dimensional subspace of \(V\), irrespective of the ambient dimension.

## Proof

**1. Reduction to generating coordinates.** Since \(L\) has nilpotence class three, any bracket involving at least four homogeneous generators vanishes. Writing \(X=x+X_{\ge2}\), \(Y=y+Y_{\ge2}\) with \(x,y\in V\) immediately gives
\[
[X,[X,Y]]=[x,[x,y]].
\]
Consequently, any fixed fiber of the word map on \(V\times V\) has exactly \(q^{2(D-d)}\) lifts to \(L\times L\). It suffices to analyze \(F(x,y)=[x,[x,y]]\).

**2. Rank for a fixed nonzero first argument.** The free Lie algebra embeds into the tensor algebra \(T(V)\) over any field. In its degree-three piece the value has the exact tensor representation
\[
F(x,y)=x\otimes x\otimes y-2x\otimes y\otimes x+y\otimes x\otimes x.
\]
For \(x=e_1\), \(F(e_1,e_1)=0\) and the elements
\[
F(e_1,e_j),\qquad 2\le j\le d,
\]
are nonzero and linearly independent: their distinct multidegrees are \(2e_1+e_j\), and the coefficient of \(e_1\otimes e_1\otimes e_j\) is one, in every characteristic. The degree-three Lie component embeds in the degree-three tensor component, so no extra kernel is hidden. An invertible linear change of generators sends any nonzero \(x\) to \(e_1\). Therefore the linear map \(y\mapsto F(x,y)\) has kernel \(\langle x\rangle\), rank \(d-1\), and every output has exactly \(q\) preimages \(y\).

**3. Unique projective first argument.** Let \(\ell\ne\ell'\) and choose line representatives \(x,x'\) which are independent. An invertible linear change of generators sends them to \(e_1,e_2\). The first image subspace \(W_{\langle e_1\rangle}\) has an independent homogeneous spanning set with multidegrees \(2e_1+e_j\) for \(j\ne1\); the second has multidegrees \(2e_2+e_j\) for \(j\ne2\). These two multidegree sets are disjoint, including the potentially confusing pair \(2e_1+e_2\) versus \(e_1+2e_2\). The multigrading of \(L_3\) is a direct sum, so the subspaces have zero intersection. Equivariance under \(\mathrm{GL}(V)\) proves the assertion for all distinct lines. In particular every nonzero image element has a uniquely determined line \(\ell=\langle x\rangle\).

**4. Flag parametrization.** Given \(x\ne0\), the map \(V/\langle x\rangle\to W_{\langle x\rangle}\) induced by \(y\mapsto F(x,y)\) is an isomorphism. A one-dimensional subspace of the quotient corresponds bijectively to a two-dimensional subspace \(P\) of \(V\) containing \(\ell\). The disjointness established in step 3 makes the resulting correspondence between nonzero projective image points and flags globally injective and surjective. There are \((q^d-1)/(q-1)\) possibilities for \(\ell\) and \((q^{d-1}-1)/(q-1)\) for \(P\) containing it, giving \((q^d-1)(q^{d-1}-1)/(q-1)^2\) projective image points. Each has \(q-1\) nonzero affine representatives, proving the image-cardinality formula.

**5. Prescribed fibers.** If \(z\ne0\) is in the image, step 3 gives the unique projective first argument. It has \(q-1\) nonzero vector representatives \(x\); for each representative, step 2 gives exactly \(q\) solutions \(y\). Hence its fiber in \(V\times V\) has cardinality \(q(q-1)\). For \(z=0\), the \(q^d\) pairs with \(x=0\) all vanish; each of the remaining \(q^d-1\) choices of \(x\) has exactly \(q\) solutions \(y\) in its kernel. All other fibers are empty. Multiplication by the higher-layer lifting factor proves the full formula.

Finally, divide the zero-fiber cardinality by \(q^{2D}\), giving \(q^{-2d}(q^d+(q^d-1)q)=q^{1-d}+q^{-d}-q^{1-2d}\). When \(d=2\), the Witt dimension formula gives \(\dim L_3=2\), and the image formula gives \(q^2\) values, so the map is onto. For \(d\ge3\), \(\dim L_3=(d^3-d)/3\) and the image has fewer than \(q^{\dim L_3}\) values, since its size cannot exceed the \(q^{2d}\) pairs in \(V\times V\) and \(\dim L_3=(d^3-d)/3>2d\) for every \(d\ge3\) (e.g., for \(d=3\), it has \(1+(q^2+q+1)(q^2-1)\) rather than \(q^8\)); thus it is proper. This completes the proof.

## Verification

The independently implemented script `verify.py` evaluates the displayed tensor-cube expression directly over prime fields \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) and the nonprime field \(\mathbb F_4\). It exhaustively enumerates all \(q^{2d}\) pairs in \(V\times V\) for eight small configurations, compares exact zero and nonzero fiber sizes and total image cardinalities, and constructs all projectively normalized first arguments to check each image subspace's size and pairwise zero intersection. The full recorded output is `verify_output.txt`. These checks are finite consistency tests, not substitutes for the free-Lie/tensor proof for arbitrary \(d,q\).

## Relationship to prior work

Benito and de-la-Concepción [1] discuss free nilpotent Lie algebras of type two, including the rank-two class-three algebra, within classification problems for Lie algebra extensions. Their full preprint concerns structural extensions, derivations and automorphisms over the complex field, not prescribed finite-field two-Engel fibers. Their later survey [2] describes the Hall/Witt structure of free nilpotent Lie algebras, but is set in characteristic zero, so the characteristic-two and characteristic-three assertions here are proved independently from tensor embeddings.

Mann and Martínez [3] study general finite-Lie-algebra thresholds for nearly Engel identities. Those threshold statements do not give the image or all prescribed value fibers of this free nilpotent family. Related Engel word-map literature treats triangular matrix groups or semisimple groups, not this precise Lie word map with its flag-parametrized fibers. Another result on star-graph class-three Lie algebras [4] gives square-adjoint rank spectra and zero-value probabilities for a **different nonfree Lie algebra**, without the claimed free-Lie image or nonzero fiber classification.

The present assertion does not claim novelty for the existence of Hall bases, the universal embedding of free Lie algebras into tensor algebras, the known dimension formula, or prior general Engel identity bounds. Its additional result is the geometric description of all nonzero word values and the exact uniform nonzero-target fibers for the whole free class-three family.

## Limitations

Searches and full-text comparisons do not prove absolute historical uniqueness. An unindexed treatment of degree-three Lie word values, free Lie polynomial images, or the geometry of the degree-three Schur functor could imply this theorem indirectly. The closest general Engel-probability paper [3] was not verified page-by-page in full; its accessible abstract and theorem excerpts were compared. Further historical-priority review of that literature would be useful before asserting first discovery. No independent mathematical audit has been performed. The proof concerns the free class-three Lie algebra only and does not extend automatically to quotients or to group Engel word maps.

## References

[1] Pilar Benito and Daniel de-la-Concepción, *A note on extensions of nilpotent Lie algebras of type 2*, arXiv:1307.8419v1, first public 2013-07-31, sections 2–5. https://arxiv.org/html/1307.8419v1

[2] Pilar Benito and Daniel de-la-Concepción, *An overview of free nilpotent Lie algebras*, Comment. Math. Univ. Carolin. 55 (2014), 325–339, in particular its model for the free class-three algebra and its Hall/Witt dimension discussion. https://dml.cz/bitstream/handle/10338.dmlcz/143811/CommentatMathUnivCarolRetro_55-2014-3_5.pdf

[3] Avinoam Mann and Consuelo Martínez, *Groups nearly of prime exponent and nearly Engel Lie algebras*, Archiv der Mathematik 71 (1998), 5–11, DOI:10.1007/s000130050227. https://doi.org/10.1007/s000130050227

[4] *Exact two-Engel probabilities and square-adjoint rank spectra of star-graph Lie algebras*, public result dated 2026-11-08. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-two-engel-probabilities-and-square-adjoint-rank-spectra-of--fce13813ee56/RESULT.md
