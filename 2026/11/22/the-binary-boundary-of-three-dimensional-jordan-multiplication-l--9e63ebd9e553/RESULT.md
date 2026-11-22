# The binary boundary of three-dimensional Jordan multiplication laws

## Finding

Let \(V=\mathbb F_2^3\). A *pointwise Jordan law* on \(V\) is a commutative bilinear product satisfying
\[
(x^2)(xy)=x(x^2y)\quad\text{for every }x,y\in V.
\]
Such a law is *extension-stable* if the same identity holds on \(V\otimes_{\mathbb F_2}K\) for every field extension \(K/\mathbb F_2\). Neither associativity nor an identity element is assumed.

**Theorem.** The exact counts of labelled products and isomorphism classes are:

| Property | Labelled multiplication laws | Isomorphism classes |
|---|---:|---:|
| Pointwise Jordan identity | 2,858 | 47 |
| Extension-stable Jordan identity | 1,898 | 32 |
| Associativity | 988 | 16 |

Consequently there are **15** pointwise Jordan isomorphism classes which are not extension-stable, and all 15 are nonassociative. The complete, canonical list of 47 representatives, their orbit sizes and automorphism-group orders is `representatives.tsv`; the independent finite enumerator is `check_jordan_f2.cpp`.

The distinction is witnessed by the multiplication
\[
e_1^2=e_1+e_3,\qquad e_1e_2=e_1,\qquad e_2^2=e_2,
\]
with all other basis products zero. This law satisfies the Jordan identity on \(\mathbb F_2^3\), but for \(\omega\in\mathbb F_4\) with \(\omega^2+\omega+1=0\), the Jordan defect at \(x=e_1+\omega e_2\), \(y=e_1\) equals \(e_3\ne0\).

## Assumptions and scope

The word *pointwise* makes the definition over the two-element field unambiguous: only the eight field-valued vectors are tested. *Extension-stable* means an identity of polynomial functions on every scalar extension. This does not assert any classification of quadratic Jordan algebras, which carry additional structure in characteristic two.

Write the six unordered basis pairs in this fixed order:
\[
(1,1),(1,2),(1,3),(2,2),(2,3),(3,3).
\]
Encode each output vector as an integer from 0 through 7, with bits for \(e_1,e_2,e_3\). If the six outputs have codes \(b_0,\ldots,b_5\), encode the multiplication by
\[
c=\sum_{p=0}^{5}2^{3p}b_p,\qquad 0\le c<2^{18}.
\]
The first column of `representatives.tsv` uses this encoding. Its representative is the *least numerical code* in the corresponding \(\operatorname{GL}_3(\mathbb F_2)\)-orbit. The columns `associative` and `strict` are 0–1 indicators; `zero_square_vectors` includes zero, while `nonzero_idempotents` excludes zero.

## Proof

**1. Exhaustion of multiplication laws.** Commutativity and bilinearity determine a product uniquely from the six unordered pairs of basis vectors. Each pair has one of eight possible outputs. Hence there are exactly \(8^6=2^{18}=262{,}144\) such products. The implementation `multiplication` constructs all 64 pairwise products from a six-output code using bilinearity. `jordan_over_F2` evaluates the defining identity for all 64 ordered pairs \((x,y)\in V^2\). No polynomial genericity assumptions enter this finite-field check.

**2. Isomorphism orbits.** An isomorphism of two such algebras is exactly an invertible \(\mathbb F_2\)-linear map preserving products. Every invertible map is determined by an ordered basis, yielding
\[
|\operatorname{GL}_3(\mathbb F_2)|=(8-1)(8-2)(8-4)=168.
\]
`all_GL3_F2` constructs these maps from all independent triples, and `change_basis` computes the induced action on multiplication codes using inverse coordinates. Every code admitted by the Jordan test is assigned to the orbit of its least representative. The partition is verified by an independent visited-code check and by the orbit–stabilizer identity. The 47 classes have orbit-size frequency
\[
1^1,\ 7^2,\ 8^1,\ 14^1,\ 21^3,\ 28^{10},\ 42^5,\ 56^3,\ 84^{17},\ 168^4,
\]
where the exponent denotes the number of orbits of that size. The weighted sum is 2,858.

**3. Extension-stability criterion.** In characteristic two,
\[
x=\sum_i t_i e_i\quad\Longrightarrow\quad x^2=\sum_i t_i^2e_i^2.
\]
Thus every coefficient of the Jordan defect is a polynomial, linear in the coordinates of \(y\), whose monomials in the coordinates of \(x\) are exactly of the form \(t_i^2t_j\). Its coefficient at \(t_i^2t_jy_k\) is
\[
e_i^2(e_je_k)-e_j(e_i^2e_k).
\]
Distinct ordered pairs \((i,j)\) give distinct formal monomials (including \(i=j\)); hence the polynomial vanishes over every scalar extension if and only if all 27 such vector coefficients vanish. This is the test `jordan_formal`. As a separate validation, `jordan_over_F4` directly evaluates the defect on all 64 vectors \(x\in\mathbb F_4^3\) and on the three basis vectors \(y\). The two tests agree on every pointwise Jordan multiplication law. They are equivalent because each coordinate degree is at most three, strictly below \(|\mathbb F_4|=4\), so a polynomial vanishing at all of \(\mathbb F_4^3\) is zero. Hence this is a rigorous all-extensions criterion, not an extrapolation from small samples.

**4. Exact output and independent count identities.** The exhaustive loops yield 2,858 pointwise laws, of which 1,898 satisfy the formal criterion and 988 are associative; their respective orbit counts are 47, 32 and 16. Independently, counting fixed laws across every linear change of basis gives Burnside fixed-point sums 7,896, 5,376 and 2,688, which divided by 168 reproduce the three orbit counts. Moreover the sums of orbit sizes for the extension-stable and associative representatives reproduce the corresponding labelled counts. These finite computations *exhaust the complete finite search space*, rather than sample it, and the standalone source and full representative table make the certificate reproducible.

**5. A genuinely binary-only example.** For the displayed product, writing \(x=ae_1+be_2+ce_3\) and \(y=ue_1+ve_2+we_3\) over any characteristic-two extension yields the explicit defect
\[
(x^2)(xy)-x(x^2y)=ab(a+b)u\,e_3.
\]
This is zero for all \(a,b\in\mathbb F_2\), because \(ab(a+b)=0\), but setting \(a=1,b=\omega,u=1\) in \(\mathbb F_4\) gives \(\omega(1+\omega)e_3=e_3\), proving that not every pointwise law is extension-stable.

## Verification

Build and run with any C++17 compiler:

```sh
c++ -std=c++17 -O2 check_jordan_f2.cpp -o check_jordan_f2
./check_jordan_f2 representatives.tsv
```

The program regenerates the complete 47-row table and exits with an error if the table census, formal-versus-\(\mathbb F_4\) comparison, orbit coverage, stratum preservation or Burnside consistency fails. Its success marker is `F2_3D_JORDAN_CENSUS_OK`. One may compare the generated table against the accompanying copy byte-for-byte. No external algebra packages are needed.

## Relationship to prior work

Hernández, Martin, Rodrigues and Silva (2026), arXiv:2611.00315v1, classify Jordan algebras of dimension at most three over fields with *more than two elements*, explicitly excluding \(\mathbb F_2\) (their Section 2); one of their characteristic-two steps selects a scalar outside \(\{0,1\}\) (Section 4.3). Their algebraically closed characteristic-two geometric classification does not itself give the complete rational-point orbit census over \(\mathbb F_2\). The present theorem closes that exact finite-field endpoint and distinguishes pointwise from extension-stable identities.

Hegazi and Abdelwahab (2013) classify the *nilpotent* three-dimensional Jordan subclass, including five characteristic-two isomorphism classes, but do not enumerate all nonnilpotent products. Cedilnik and Jerman (2020) classify *zeropotent* algebras (all squares zero); Cedilnik (2023) classifies *isopotent* algebras (each square proportional to its input). These are significant proper subclasses and are not competing full binary Jordan orbit enumerations. Prior classifications can contain some of the 47 representatives without implying the total count or the 15-class extension-stability boundary.

## Limitations

The theorem is specific to dimension three and the base field \(\mathbb F_2\). It counts isomorphism classes of commutative bilinear multiplication laws, **not** equivalence classes of quadratic Jordan structures and not isomorphism classes after extension of scalars. Exhaustion is finite and fully reproducible, but does not establish a closed dimension-dependent formula. Historical priority cannot be guaranteed against unindexed classifications or unpublished enumerations. Independent mathematical audit has not been performed.

## References

1. I. Hernández, M. E. Martin, R. L. Rodrigues and C. A. G. Silva, *Isomorphism classes and geometric classification of three-dimensional Jordan algebras and the length function*, arXiv:2611.00315v1 (first public 2026-10-30). https://arxiv.org/html/2611.00315v1
2. A. S. Hegazi and H. Abdelwahab, *Construction of Nilpotent Jordan Algebras Over any Arbitrary Fields*, arXiv:1301.6349v4 (2013), especially Theorem 34. https://arxiv.org/pdf/1301.6349
3. A. Cedilnik and M. Jerman, *Classification of three-dimensional zeropotent algebras*, International Electronic Journal of Algebra 27 (2020), 127–146. https://www.ieja.net/files/papers/volume-27/9-V27-2020.pdf
4. A. Cedilnik, *Classification of three-dimensional isopotent algebras*, International Electronic Journal of Algebra 33 (2023), 226–246. https://www.ieja.net/files/papers/volume-33/14-IEJA-3322.pdf
