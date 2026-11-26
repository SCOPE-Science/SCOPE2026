# Veronese centralizer strata in the cubic free associative truncation

## Finding
Let \(k=\mathbb F_q\) be any finite field, and let \(A=k\langle x,y\rangle/(x,y)^4\), the unital associative algebra with the fifteen words of lengths zero through three as a basis. For \(a\in A\), let \(r(a)=\operatorname{rank}_k(b\mapsto ab-ba)\). Then the only ranks are \(0,1,2,4\), with generating polynomial
\[
\sum_{a\in A}t^{r(a)}=q^9\bigl(1+(q^2-1)t+(q^4-q^2)t^2\bigr)+q^{13}(q^2-1)t^4.
\]
The exact element-commuting probability is
\[
\Pr_{a,b\in A}(ab=ba)=\frac{2q^3+q^2-q-1}{q^7}.
\]
The geometric loci of ranks at most zero, one, and two are respectively an affine nine-space, a product of that affine nine-space with the affine cone over a smooth projective conic, and an affine thirteen-space. The nontrivial middle cone is the degree-two Veronese image of \(\mathbb P^1\) in the projective space of noncommutative quadratics. Its singular locus is precisely the affine nine-space of central elements. These statements hold over an algebraic closure in arbitrary characteristic, including characteristic two.

## Assumptions and scope
The augmentation ideal \(J=(x,y)/(x,y)^4\) satisfies \(J^4=0\). There is a grading \(A=A_0\oplus A_1\oplus A_2\oplus A_3\), where \(\dim A_i=2^i\). In particular, \(\dim A=15\). The statements concern ordinary associative commutators and the reduced rank loci, not a possibly nonreduced determinantal scheme structure. The finite-field parameter \(q\) can be any prime power; the geometric claims refer to an arbitrary algebraically closed base field.

Every element has a unique decomposition \(a=c+u+v+w\) with \(c\in A_0\), \(u\in A_1\), \(v\in A_2\), and \(w\in A_3\). The degree-three part and scalars are central. Write
\[
v=\alpha x^2+\beta xy+\gamma yx+\delta y^2.
\]

## Proof
First suppose \(u\ne0\). An invertible linear change of the free generators reduces \(u\) to \(x\) without changing ranks. The commutator map \(A_2\to A_3\), \(h\mapsto[x,h]\), has kernel precisely \(kx^2\): its images on \(xy,yx,y^2\) are
\[
x^2y-xyx,\quad xyx-yx^2,\quad xy^2-y^2x,
\]
which are linearly independent in the word basis, in every characteristic. Hence the degree-three image has dimension three. On \(A_1\), the degree-two image is spanned by \([x,y]=xy-yx\). The only linear combination of degree-one inputs with vanishing degree-two image lies in \(kx\); its image under \(\operatorname{ad}_a\) is \([v,x]=-[x,v]\), already in the degree-three image. Thus \(r(a)=3+1=4\), regardless of \(v,w,c\).

Now suppose \(u=0\). The commutator map vanishes outside \(A_1\) and is \(\ell\mapsto[v,\ell]\) into \(A_3\). If \(v=0\), its rank is zero. For \(v\ne0\), the rank drops from two to one exactly when some nonzero \(\ell\in A_1\) commutes with \(v\). After changing generators to \(\ell=x\), the displayed independent word coefficients in \([x,v]\) force \(\beta=\gamma=\delta=0\). Therefore the rank-one condition is exactly \(v=\lambda\ell^2\) for \(\lambda\in k^\times\) and \(\ell\in A_1\setminus0\). This implication and its converse hold over every field.

The projective squares \([\ell^2]\), for lines \([\ell]\in\mathbb P(A_1)\), form the Veronese conic. In coordinates \((\alpha,\beta,\gamma,\delta)\), its affine cone is
\[
\beta=\gamma,\qquad \alpha\delta=\beta^2.
\]
The second equation remains a reduced irreducible quadric after imposing the first linear equation, in every characteristic. Its gradient, restricted to the quadric, vanishes only at the cone vertex; hence the cone is smooth away from the origin and singular at the origin. The cone has dimension two, and adjoining the unrestricted central coordinates \(c,w\) adds nine dimensions. The rank-at-most-two locus is given by \(u=0\), hence has dimension thirteen; the rank-zero locus is \(c+w\), hence has dimension nine. This gives all the asserted geometric strata and singular loci.

Over \(\mathbb F_q\), the conic has \(q+1\) rational projective points. Each such point contributes \(q-1\) nonzero affine points, giving \(q^2-1\) nonzero quadratic forms with rank one. There are \(q^4-q^2\) forms of rank two and one of rank zero. The independent central coordinates give a factor \(q^9\). For \(u\ne0\), there are \((q^2-1)q^4q^9=q^{13}(q^2-1)\) rank-four elements. These counts sum to \(q^{15}\) and give the polynomial.

For each \(a\), its element centralizer has \(q^{15-r(a)}\) elements. Summing this quantity across the four ranks and dividing by \(q^{30}\) simplifies to the displayed commuting probability.

## Verification
The accompanying standalone `verify.py` independently constructs the multiplication and all fifteen-by-fifteen commutator matrices using concatenated word bases. It exhaustively checks the six relevant noncentral coordinates for \(q=2,3,5,7\), finding the predicted rank histograms in every case. Since the nine central coordinates do not influence the commutator, these are exhaustive checks of distinct commutator maps over the listed prime fields, not samples. The proof, rather than the finite checks, establishes all finite prime powers and the geometric claims.

To replay, run `python verify.py` in a directory containing this file and the verifier; no nonstandard packages are needed.

## Relationship to prior work
Boyarchenko, *Representations of unipotent groups over local fields and Gutkin's conjecture* (first arXiv release 2010-03-13), Section 3.2, introduces free associative nilpotent algebras of this type in the study of commutators of algebra groups. The inspected Sections 1 and 3.1–3.3 establish group-commutator structural properties rather than the complete element-centralizer rank distribution here. Bergman's centralizer theorem concerns full free associative algebras; it does not give the finite-truncation rank counts. In particular, the present low-rank geometry arises from commuting **modulo degree four**, not merely in the untruncated algebra.

Published results concerning commutator fibers in Kronecker path algebras, maximal-class filiform Lie algebras, and the classification of two-generated algebras with radical cube zero concern different algebra structures or different invariants. Their stated formulas do not imply the above Veronese rank locus for the free class-three associative truncation. An unlocated specialized study of centralizers in this exact quotient remains an originality risk.

## Limitations
This is an exact classification for the two-generator truncation through word length three only; higher degrees or more generators are not classified. The scheme-theoretic multiplicities of determinantal rank loci are not addressed. Finite tests do not independently establish characteristic-uniform correctness. No independent mathematical audit has been performed.

## References
1. M. Boyarchenko, *Representations of unipotent groups over local fields and Gutkin's conjecture*, arXiv:1003.2742 (initial submission 13 March 2010), particularly Section 3.2; https://arxiv.org/abs/1003.2742.
2. G. M. Bergman, *Centralizers in free associative algebras*, Transactions of the American Mathematical Society **137** (1969), 327–344, doi:10.2307/1994807.
3. P. M. Cohn, *Free Associative Algebras*, Bulletin of the London Mathematical Society **1** (1969), 1–39, doi:10.1112/blms/1.1.1.
