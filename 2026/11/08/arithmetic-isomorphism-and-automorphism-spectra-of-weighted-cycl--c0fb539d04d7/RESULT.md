# Arithmetic isomorphism and automorphism spectra of weighted cyclic evolution algebras

## Finding
For an integer \(n\geq 2\) and a prime power \(q\), consider the evolution algebra \(E(\boldsymbol a)\) over \(\mathbb F_q\) with natural basis \(e_0,\ldots,e_{n-1}\) and multiplication
\[
e_i e_j=0\quad(i\ne j),\qquad e_i^2=a_i e_{i+1\pmod n},\qquad a_i\in\mathbb F_q^\times.
\]
Every such algebra is perfect and simple. Put \(N=2^n-1\), \(g=\gcd(q-1,N)\), and let \(c(\boldsymbol a)=\prod_{i=0}^{n-1}a_i^{2^{n-1-i}}\). The multiplicative quotient \(\mathbb F_q^\times/(\mathbb F_q^\times)^N\) is cyclic of order \(g\), written additively as \(\mathbb Z/g\mathbb Z\). Two such algebras are isomorphic if and only if their classes \([c(\boldsymbol a)]\) belong to the same orbit under \([c]\mapsto[c]^2\). This includes isomorphisms not required to respect the displayed natural bases.

For \(a\in\mathbb Z/g\mathbb Z\), let \(d(a)\) be the least positive integer such that \(2^{d(a)}a=a\) in that group. Then \(d(a)\mid n\), and the full algebra automorphism group has order
\[
|\operatorname{Aut}_{\mathbb F_q}(E_a)|=\frac{gn}{d(a)}.
\]
For each \(d\mid n\), the number of isomorphism classes with \(d(a)=d\) is
\[
\boxed{\quad C_{n,q}(d)=\frac1d\sum_{h\mid d}\mu(d/h)\gcd(g,2^h-1).\quad}
\]
In particular, the total number of classes is \(\sum_{d\mid n}C_{n,q}(d)\); these formulas give both the complete class census and automorphism-*order* spectrum. The order alone is not asserted to determine the abstract automorphism group in general.

A sharper conclusion holds for \(\mathbb F_4\). Fix \(\omega\in\mathbb F_4\) with \(\omega^2+\omega+1=0\). If \(n\) is odd, all these weighted cycles are isomorphic and their automorphism group is cyclic of order \(n\). If \(n\) is even, there are exactly **two** isomorphism classes: the untwisted cycle \(U_n\), with all \(a_i=1\), and the twisted cycle \(T_n\), with \(a_0=\cdots=a_{n-2}=1\) and \(a_{n-1}=\omega\). Their abstract automorphism groups are respectively
\[
\boxed{\quad\operatorname{Aut}(U_n)\cong C_3\rtimes C_n\quad\text{(inversion action)},\qquad\operatorname{Aut}(T_n)\cong C_{3n/2}.\quad}
\]
The natural exact sequence for the twisted algebra
\[
1\longrightarrow C_3\longrightarrow\operatorname{Aut}(T_n)\longrightarrow C_{n/2}\longrightarrow1
\]
is nonsplit precisely when \(3\mid n/2\). Thus every dimension \(n=6k\), \(k\ge1\), provides a **simple** evolution algebra over \(\mathbb F_4\) with nonsplit diagonal-to-permutation automorphism extension and cyclic automorphism group \(C_{9k}\). The existence of nonsplit extensions for other evolution-algebra families is prior work; the assertion here concerns this explicit infinite simple weighted-cycle family.

## Assumptions and scope
The base field is exactly \(\mathbb F_q\), with \(q\) any prime power. Linear isomorphisms and automorphisms are \(\mathbb F_q\)-linear algebra maps; semilinear/Frobenius automorphisms are excluded. All \(n\) cyclic weights are nonzero. The cycle has distinct labeled vertices, and the claimed classifications disregard labels by allowing all algebra isomorphisms. The exponent invariant is an element of the specified quotient, not a choice of representative in the field. The \(\mathbb F_4\) conclusions hold for every positive even \(n\ge2\), and the nonsplitting assertion is for \(n\) divisible by six.

## Proof
**1. Simplicity and monomial rigidity.** The structure matrix is an invertible weighted permutation matrix, so \(E^2=E\). If an ideal contains \(0\ne v=\sum_i v_i e_i\), choose \(i\) with \(v_i\ne0\); multiplication by \(e_i\) yields \(v_i a_i e_{i+1}\ne0\), and repeated squaring propagates round the cycle. Hence the ideal is the full algebra. For perfect evolution algebras, the established monomial-isomorphism theorem (Elduque--Labra, as reproduced by Wei--Zou, Theorem 1.1) says that an algebra isomorphism sends every natural-basis vector to a nonzero scalar multiple of a natural-basis vector. The directed support cycle forces the induced permutation \(i\mapsto i+s\pmod n\): if \(\varphi(e_i)=u_i e'_{\sigma(i)}\), then comparison of squares gives \(\sigma(i+1)=\sigma(i)+1\pmod n\). Therefore all isomorphisms are combinations of cyclic shifts and nonzero diagonal rescalings.

**2. The complete arithmetic invariant.** Under a diagonal change \(e'_i=u_i e_i\), the new displayed weight at position \(i\) is \(a_i u_i^2/u_{i+1}\), subscripts modulo \(n\). Set \(c(\boldsymbol a)=\prod_i a_i^{2^{n-1-i}}\). Multiplication of these transformed weights to the same powers telescopes, leaving \(c(\boldsymbol a')=c(\boldsymbol a)u_0^{2^n-1}\). Conversely, for any target weights with this relation, the recursion \(u_{i+1}=u_i^2a_i/a'_i\) determines nonzero scalars and its final consistency condition is exactly \(u_0^N=c(\boldsymbol a')/c(\boldsymbol a)\). Hence diagonal orbits correspond bijectively to \(\mathbb F_q^\times/(\mathbb F_q^\times)^N\), of size \(g\). Rotating weights by one position changes \(c\) to \(c^2\) modulo \(N\)-th powers: the quotient of the two expressions is an \(N\)-th power of a single weight. Thus full isomorphism classes are exactly the doubling orbits on \(C_g\).

**3. Automorphism orders and orbit multiplicities.** A diagonal automorphism requires \(u_{i+1}=u_i^2\), hence \(u_i=u_0^{2^i}\) and \(u_0^N=1\). This kernel has \(g\) elements. The image of the permutation map from \(\operatorname{Aut}(E_a)\) into the cyclic rotation group consists exactly of rotations fixing the class \(a\); its cardinality is \(n/d(a)\). The order formula follows by the kernel--image theorem. Since \(g\mid2^n-1\), doubling has order dividing \(n\) on \(C_g\), so \(d(a)\mid n\). The fixed points of its \(h\)-th iterate solve \((2^h-1)a=0\), of which there are \(\gcd(g,2^h-1)\). Möbius inversion extracts points of least period \(d\); dividing by \(d\) gives \(C_{n,q}(d)\).

**4. Groups over \(\mathbb F_4\).** Here \(q-1=3\). If \(n\) is odd, \(g=1\), so the full automorphism group projects isomorphically onto the rotations, giving \(C_n\). If \(n\) is even, \(g=3\) and doubling on \(C_3\) fixes zero and swaps its two nonzero classes. This proves there are exactly two classes, represented by \(U_n\) and \(T_n\). The full automorphisms of \(U_n\) consist of \(e_i\mapsto t^{2^i}e_i\), \(t^3=1\), and the pure cyclic shift \(e_i\mapsto e_{i+1}\). Conjugation by the shift interchanges \(t\) and \(t^{-1}\), proving \(C_3\rtimes C_n\) with the indicated action.

For \(T_n\), define \(F\) explicitly by
\[
F(e_i)=e_{i+2}\ (0\le i\le n-3),\quad
F(e_{n-2})=\omega e_0,\quad F(e_{n-1})=\omega^2e_1.
\]
(The first range is empty for \(n=2\).) Checking squares at ordinary and exceptional indices shows \(F(e_i)^2=F(e_i^2)\), so \(F\) is an algebra automorphism. Its permutation is a two-step rotation; direct iteration gives \(F^{n/2}(e_i)=\omega e_i\) for even \(i\), and \(\omega^2e_i\) for odd \(i\). This is a nontrivial diagonal automorphism of order \(3\). The permutation of \(F\) has order \(n/2\), and therefore \(F\) has order \(3n/2\). Since the automorphism count from step 3 also equals \(3n/2\), \(F\) generates the full group. In a cyclic group of order \(3m\), the subgroup of order \(3\) has a cyclic complement of order \(m\) if and only if \(\gcd(3,m)=1\); put \(m=n/2\). This proves the nonsplitting criterion and the family \(n=6k\).

## Verification
Run \(\texttt{python verify.py}\) using Python 3 standard libraries. The standalone checker represents multiplicative weights by exponents in the cyclic group \(\mathbb F_q^\times\), enumerates full orbits under each independent elementary diagonal rescaling and one-position rotation, and compares their stabilizer-order multisets against the formula for small \(n\) and cyclic-group orders. It also directly tests all invertible \(2\times2\) matrices over \(\mathbb F_4\) as possible algebra isomorphisms between the nine labeled two-dimensional weighted cycles, checking the two isomorphism classes and their automorphism orders without assuming monomiality. It separately validates the explicit twisted \(\mathbb F_4\) automorphism's multiplicative identities and order for every even \(n\) up to \(100\). Successful execution prints \(\texttt{VERIFY_OK}\). This is finite corroboration of the proof, not an exhaustive check of the universal theorem; the computed group actions depend only on a cyclic multiplicative group and are also meaningful for formal cyclic-group orders that do not arise from finite fields.

## Relationship to prior work
Sriwongsa and Zou (2022, arXiv:2202.01333, Section 4) study the maximal diagonal automorphism subgroup and prove the untwisted cyclic semidirect-product classification over algebraically closed characteristic-zero fields; the nontrivial finite-field twists and nonsplit extensions treated here are not a consequence of that field-specific conclusion. Wei and Zou (2023, arXiv:2310.12368, first posted 2023-10-18) establish the general monomial-isomorphism criterion, an orbit formula over finite fields, and general low-dimensional counts. Those are relied upon here; their general results do not explicitly give the all-dimensional weighted-cycle arithmetic orbit sizes or the \(\mathbb F_4\) automorphism-group extension classification. Khudoyberdiyev, Omirov and Qaralleh (2013, arXiv:1307.0993) discuss permutation-type evolution algebras in a characteristic-zero setting with additional root-extraction assumptions; that normalization need not hold over finite fields. Alshatnawi, Costoya and Viruel (2026, arXiv:2607.15154) explicitly recognize weighted cyclic components and normalized representative weights and discuss normalization over algebraically closed fields; the present cyclic finite-field quotient, exact order spectrum, and infinite nonsplit group identification require additional arithmetic and group arguments. Kaygorodov, Martin González and Viruel (2026, arXiv:2610.22248, Proposition 21) describe a different six-dimensional evolution-algebra example with nonsplit diagonal extension and explicitly ask for splitting criteria in their Question 33; nonsplitting in evolution algebras itself is **not** claimed as new. The additional conclusion is an exact splitting criterion throughout a natural simple directed-cycle family in every even dimension over the four-element field, together with complete finite-field cycle isomorphism and automorphism-order formulas. This resolves the splitting question on that family, not in general. Relevant abstract research-index matches concern other algebra families or distinct invariants; no decisive equivalent was found in the inspected sources.

## Limitations
The result is confined to nonzero weights on one directed cycle. It does not classify arbitrary evolution algebras, disjoint unions of cycles, zero-weight degenerations, or semilinear automorphisms. The general theorem determines automorphism-group **orders** and orbit counts, not the isomorphism types of all automorphism groups for arbitrary finite fields. The abstract-group identification is proved specifically over \(\mathbb F_4\). The first-posting date governs the motivating source only and does not establish priority. Broader unlocated results specializing the general monomial-isomorphism theorem may subsume part of the arithmetic enumeration; an independent literature audit remains outstanding.

## References
- S. Sriwongsa and Y. M. Zou, *On Automorphism Groups of Idempotent Evolution Algebras*, arXiv:2202.01333 (2022), https://arxiv.org/abs/2202.01333 .
- Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368 (first posted 2023-10-18), https://arxiv.org/abs/2310.12368 .
- A. Khudoyberdiyev, B. Omirov, I. Qaralleh, *Few remarks on evolution algebras*, arXiv:1307.0993 (2013), https://arxiv.org/abs/1307.0993 .
- Alshatnawi, Costoya and Viruel, *On Grothendieck Ring of Finite-Dimensional Non-Degenerate Evolution Algebras*, arXiv:2607.15154 (2026), https://arxiv.org/abs/2607.15154 .
- Kaygorodov, Martin González and Viruel, *Evolution algebras: a survey*, arXiv:2610.22248 (2026), https://arxiv.org/abs/2610.22248 .
