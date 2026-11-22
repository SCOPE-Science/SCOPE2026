# Square-zero linear-space incidence in generalized dihedral group algebras

## Finding
Let \(H\) be any finite abelian group of **odd** order \(m\ge1\), let \(k=\mathbb F_q\) with \(q=2^f\) and \(f\ge1\), and let \(A=k[G]\), where \(G=H\rtimes C_2\) and the involution acts by inversion. The set of square-zero elements is \(X(k)=\{x\in A:x^2=0\}\). A *square-zero linear space* means a \(k\)-linear subspace contained in \(X(k)\), not merely a subspace of nilpotent elements of unbounded index.

Write \(\widehat H=\operatorname{Hom}(H,\overline k^*)\). The nontrivial characters are partitioned into unordered inversion pairs \(\{\chi,\chi^{-1}\}\). Let \(d_1,\dots,d_r\) denote the lengths of the orbits of \(\chi\mapsto\chi^q\) on these pairs, counted once per orbit. Consequently \(\sum_i d_i=(m-1)/2\); an empty list is allowed when \(m=1\).

**Theorem (maximal-space arrangement, geometry, and rank spectrum).** Every inclusion-maximal square-zero linear space has the same dimension \((m+1)/2\). Their exact number is
\[
\boxed{F_{H,q}=\prod_{i=1}^{r}(q^{d_i}+1).}
\]
There is a canonical parametrization, after choosing the simple-factor decomposition, by the product of projective lines \(\prod_i\mathbb P^1(\mathbb F_{q^{d_i}})\). For two maximal spaces with labels \((L_i)\) and \((L_i')\),
\[
\boxed{\dim_k(W_L\cap W_{L'})=1+\sum_{\{i:L_i=L_i'\}}d_i.}
\]
In particular, for any fixed maximal space and any proper subset \(S\subsetneq\{1,\dots,r\}\), exactly \(\prod_{i\notin S}q^{d_i}\) other maximal spaces agree with it in exactly the coordinates in \(S\). The same formula gives the complete pairwise intersection-dimension distribution, including coincident subset sums. For \(r=0\), there is one one-dimensional maximal space.

The *reduced* affine algebraic set of square-zero elements is geometrically irreducible of dimension \(m\), and over \(\overline k\) has form
\[
\boxed{X_{\mathrm{red},\overline k}\simeq\mathbb A^1\times\{(a,b,c):a^2+bc=0\}^{(m-1)/2}.}
\]
For \(m>1\), the displayed cone factors have singular vertices and the singular locus of the product is a union of codimension-two subvarieties. This is a statement about the **reduced** variety, not the possibly nonreduced equation scheme.

Let \(\rho(x)=\operatorname{rank}_k(L_x:A\to A)\) for left multiplication. Its full finite-field distribution is
\[
\boxed{\sum_{x\in A,\ x^2=0}z^{\rho(x)}
=(1+(q-1)z)\prod_{i=1}^{r}\left(1+(q^{2d_i}-1)z^{2d_i}\right).}
\]
In particular \(\#X(k)=q^m\), independent of the isomorphism type of \(H\), whereas the arrangement size \(F_{H,q}\) and the pair-intersection spectrum depend on the Frobenius/inversion orbit degrees. The largest possible rank is \(m\), attained by \((q-1)\prod_i(q^{2d_i}-1)\) elements when the product is interpreted as \(1\) for \(m=1\).

## Assumptions and scope
All spaces, ranks and counts are over \(k=\mathbb F_{2^f}\); the orbit degrees are positive integers and the group order \(m\) is odd. For \(m=1\), the algebra is \(k[C_2]\simeq k[\epsilon]/(\epsilon^2)\), and all formulas hold with empty products. The rank distribution counts **individual group-algebra elements**, not conjugacy classes or representations of the group. The linear-space incidence statements concern all inclusion-maximal \(k\)-linear subspaces of the square-zero set, not only spaces stabilized by the unit group. There are no hypotheses that \(H\) be cyclic or that the field contain all character values.

## Proof
**1. Character-orbit decomposition.** Because \(m\) is odd, the group algebra \(\overline k[H]\) is a product of \(m\) one-dimensional character algebras. Inversion fixes only the trivial character: if \(\chi=\chi^{-1}\), then \(\chi^2=1\), so \(\chi=1\) since \(H\) has odd order. The crossed product by the swapping involution on each nontrivial character pair is a full \(2\times2\) matrix algebra. On the trivial character factor it is \(\overline k[C_2]\simeq\overline k[\epsilon]/(\epsilon^2)\), with \(\epsilon=s+1\). The resulting decomposition descends along finite-field Frobenius orbits. Every central simple algebra over a finite field is split, so
\[
A\simeq k[\epsilon]/(\epsilon^2)\times\prod_{i=1}^r M_2(k_i),\qquad k_i=\mathbb F_{q^{d_i}}.
\]
Here \(2+4\sum_i d_i=2m\), verifying the ambient vector-space dimension. The semisimple factors and their degree arithmetic are classical; the new questions addressed below concern the complete square-zero arrangement, its rational incidence and its reduced geometry.

**2. Square-zero matrix geometry.** If \(K\) is any characteristic-two field, a matrix \(N\in M_2(K)\) has \(N^2=0\) exactly when it is zero or nonzero rank-one nilpotent. It then has trace zero and can be written \(\left(\begin{smallmatrix}a&b\\c&a\end{smallmatrix}\right)\) with \(a^2+bc=0\). Over \(K=\mathbb F_Q\), there are \(Q^2\) such matrices: the zero matrix and \(Q+1\) possible image/kernel lines, each yielding \(Q-1\) nonzero scalar multiples.

A key rigidity is that any \(k\)-linear subspace \(U\subset M_2(K)\) consisting entirely of square-zero matrices is contained in a *single one-dimensional \(K\)-linear nilpotent line*. Indeed, for nonzero \(N,M\in U\), the equality \((N+M)^2=0\) gives \(NM=MN\). If \(N\) and \(M\) had different image lines, their two rank-one products could be equal only if both vanished. Yet in dimension two each nonzero square-zero matrix has \(\operatorname{im}N=\ker N\), and the two zero-product conditions would force the image lines to agree. Thus their image lines coincide, and the space of square-zero maps with fixed image/kernel is one-dimensional over \(K\). This argument also covers \(q=2\): it uses only the sum of two elements, not a generic-scalar assumption.

**3. All maximal spaces and their incidences.** Project any square-zero \(k\)-linear subspace \(W\subset A\) onto the simple factors in Step 1. Its dual-number projection lies in \(k\epsilon\), and by Step 2 its projection to the \(i\)-th matrix factor lies in a nilpotent \(k_i\)-line, indexed by the projective image line \(L_i\in\mathbb P^1(k_i)\). Therefore \(W\) lies in
\[
W_{(L_i)}=k\epsilon\times\prod_i \{N\in M_2(k_i):\operatorname{im}N\subseteq L_i\subseteq\ker N\}.
\]
Every such product is itself a square-zero \(k\)-linear space, has dimension \(1+\sum_i d_i\), and is inclusion-maximal, since a further square-zero element cannot enlarge any of its projections. This proves that **all** inclusion-maximal spaces occur in this list. Distinct \(L_i\) give distinct matrix nilpotent lines, and each \(\mathbb P^1(k_i)\) has \(q^{d_i}+1\) points, giving \(F_{H,q}\). Two distinct nilpotent lines in the same matrix block intersect only in zero; identical lines intersect in dimension \(d_i\) over \(k\). The common dual-number line contributes one dimension in every intersection. The stated incidence and multiplicity formulas follow immediately by counting the \(q^{d_i}\) choices *different* from a chosen line at each mismatching coordinate.

**4. Geometry over the algebraic closure.** After extension to \(\overline k\), the \(i\)-th matrix block splits into \(d_i\) independent \(2\times2\) blocks; the reduced square-zero set is the product of \(\mathbb A^1\) from the dual-number factor with \(r_{\mathrm{geom}}=(m-1)/2\) quadratic cones \(C:\ a^2+bc=0\). The defining polynomial is irreducible over \(\overline k\), and its gradient vanishes on \(C\) only at the vertex. Consequently \(C\) is irreducible of dimension two and has a single singular point; products with affine space give a geometrically irreducible reduced variety of dimension \(1+2r_{\mathrm{geom}}=m\), with the stated singular-locus boundary.

**5. Full rank polynomial.** Left multiplication by \(b\epsilon\) on \(k[\epsilon]/(\epsilon^2)\) has rank zero when \(b=0\), and rank one otherwise. For \(M_2(k_i)\), left multiplication by a rank-one matrix has rank \(2\) over \(k_i\), hence \(2d_i\) over \(k\). Each matrix factor contributes one zero and \(q^{2d_i}-1\) nonzero square-zero elements. Ranks add under direct products, giving the displayed polynomial. At \(z=1\) this evaluates to \(q\prod_i q^{2d_i}=q^{1+2\sum_i d_i}=q^m\), whereas the all-nonzero factor choices give the top coefficient.

## Verification
The accompanying dependency-free Python 3 program `verify_generalized_dihedral_squarezero.py` constructs the **original** group-algebra multiplication table for \(H\rtimes C_2\), squares each candidate coefficient vector by convolution, and independently calculates the rank of left multiplication using finite-field elimination (including a primitive polynomial model for \(\mathbb F_4\)). It checks all \(2^{2m}\) elements for \(H=C_3,C_5,C_7,C_3^2\) over \(\mathbb F_2\), and all \(4^6\) elements for \(H=C_3\) over \(\mathbb F_4\). The computed rank polynomials match exactly. Additionally the checker enumerates **all** square-zero binary linear subspaces in the cases \(H=C_3,C_5,C_7\), verifies the inclusion-maximal-space count and dimension, and directly recomputes every pairwise intersection size. All tested configurations pass with `VERIFY_OK`, and their full output is embedded as `checker_output.txt`. These tests do not replace the general proof.

## Relationship to prior work
Kaur and Khan's 2012 preprint analyzes unit groups for \(\mathbb F_2[D_{2p}]\); their 2013 preprint provides the unit-group structure for \(\mathbb F_{2^f}[D_{2p^s}]\). Their character-orbit and matrix-factor methods supply indispensable known algebraic structure. In characteristic two, \(x^2=0\) implies \((1+x)^2=1\), so **the total square-zero cardinality for those cyclic prime-power specializations is already implicit in their unit-group classification and is not claimed independently as new**. The present claim is the maximal-linear-subspace classification and *complete intersection spectrum*, uniformly for arbitrary odd abelian \(H\), together with the refined left-multiplication-rank distribution and the reduced variety's geometry.

Published related research on generalized-dihedral group algebras determines ranks and image subspaces of **inner derivations**, not left-multiplication ranks of square-zero elements. Another study establishes a square-zero census for the order-sixteen dihedral, semidihedral and quaternion \(2\)-groups, which lie outside the odd-kernel family. A dicyclic odd-index study has different quaternionic principal blocks and does not classify the linear-space incidence arrangement here. These are statement-level boundaries, not merely title differences. The decomposition and individual matrix-cone facts are classical, and the new combined arrangement may conceivably be subsumed by a general theorem on nilpotent subspaces of finite product algebras; priority is not independently certified.

## Limitations
Oddness of \(|H|\) and characteristic two are essential to the displayed crossed-product decomposition. The theorem does not cover nonabelian odd kernels, even kernels, higher nilpotency exponents, or conjugacy orbit counts. The rank polynomial is for left multiplication in the regular algebra, not for the rank of the group action on a particular module. The claimed affine geometry is explicitly that of the **reduction** of the square-zero equation scheme. Full historical priority and independent verification remain open; the finite exhaustive examples are only checks of the universal proof.

## References
1. K. Kaur and M. Khan, *UNITS IN F2D2p*, arXiv:1209.0283v1, first public 2012-09-03, https://arxiv.org/abs/1209.0283.
2. K. Kaur and M. Khan, *Units in FD_{2p^m}*, arXiv:1307.0282v1, first public 2013-07-01, https://arxiv.org/abs/1307.0282.
3. J. Nan and S. Zhang, *On the Structure of the Units of Group Algebra of Dihedral Group*, *Communications in Mathematical Research* 30 (2014), 307–319, DOI: 10.13447/j.1674-5647.2014.04.04. Accessible abstract; full text not verified.
