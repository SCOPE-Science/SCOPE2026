# Commuting-degree rigidity and orbit spectra for rank-two retracts of odd square-zero monomial complete intersections

## Finding

Let \(k=\mathbb F_q\) be a finite field of **odd** order and let \(d\ge2\). Put
\[
A_d=k[x_1,\ldots,x_d]/(x_1^2,\ldots,x_d^2),\qquad
\mathfrak m=(x_1,\ldots,x_d).
\]
All endomorphisms are unital \(k\)-algebra homomorphisms. Let \(\mathcal E_d\) denote the composition-idempotent endomorphisms \(e\) satisfying \(\dim_k e(A_d)=2\), and let \(\Gamma_d\) be the simple undirected graph with vertex set \(\mathcal E_d\), where distinct vertices are adjacent exactly when their endomorphisms commute under composition.

**Theorem (complete rank-two retract and commuting-degree classification).** Write
\[
C=2^{d-1}-1,\qquad B=C+d-1=2^{d-1}+d-2.
\]
Every \(e\in\mathcal E_d\) has a **unique** pivot \(i\in\{1,\ldots,d\}\), normalized element \(z=x_i u\), with \(u\in k[x_j:j\ne i]/(x_j^2:j\ne i)\) of constant coefficient \(1\), and scalar vector \(v=(v_1,\ldots,v_d)\in k^d\), with \(v_i=1\), such that
\[
e(x_j)=v_jz\qquad (1\le j\le d).
\]
Conversely every such datum produces an element of \(\mathcal E_d\). In particular, \(|\mathcal E_d|=d q^B\). Exactly \(d q^C\) image subalgebras occur, and each is the image of precisely \(q^{d-1}\) different retractions.

There are exactly \(d\) conjugacy classes under the **full** automorphism group \(\operatorname{Aut}_k(A_d)\). They are indexed by \(s\in\{0,\ldots,d-1\}\), the number of nonzero off-pivot coefficients \(v_j\) for \(j\ne i\). Every member of class \(s\) is conjugate to
\[
e_s(x_1)=x_1,\qquad e_s(x_j)=\begin{cases}x_1,&2\le j\le s+1,\\0,&s+2\le j\le d.\end{cases}
\]
Its orbit has cardinality
\[
\boxed{O_s=d\binom{d-1}{s}(q-1)^s q^C.}
\]

For distinct retractions \(e=(i,z,v)\) and \(f=(h,t,w)\), composition commutes **if and only if** \(i\ne h\), \(v_h=0\), and \(w_i=0\). In particular, the degree of the vertex \(e\) is
\[
\boxed{\deg_{\Gamma_d}(e)=(d-1-s)q^{B-1}.}
\]
Thus **the ordinary commuting-graph degree determines the complete automorphism-conjugacy class**. The degree enumerator and number of ordered commuting pairs (including diagonal pairs) are respectively
\[
\boxed{\mathcal D_{d,q}(Y)=d q^C\sum_{t=0}^{d-1}\binom{d-1}{t}(q-1)^{d-1-t}Y^{tq^{B-1}},}
\]
\[
\boxed{N_{\mathrm{comm}}=d q^B+d(d-1)q^{2B-2}.}
\]
The graph has exactly \(\tfrac12 d(d-1)q^{2B-2}\) edges, precisely \(d(q-1)^{d-1}q^C\) isolated vertices, and clique number exactly \(d\).

## Assumptions and scope

The theorem holds for every finite field of odd characteristic, including nonsplit extensions of its prime field; the field size is \(q\), and \(d\) is arbitrary at least two. The algebra is a local, commutative, nonreduced, \(2^d\)-dimensional complete intersection; its basis consists of squarefree monomials \(x_S\) indexed by \(S\subseteq[d]\). Image dimension \(2\) refers to \(k\)-linear dimension, not to the rank of the induced tangent map. No homomorphism is assumed graded. The graph excludes self-loops even though each retraction commutes with itself; diagonal pairs are explicitly retained only in the ordered-pair count.

## Proof

**1. The image must be dual numbers with a nonzero tangent direction.** Every subalgebra of the local algebra \(A_d\) which is the image of a retraction is local, since it is a retract of a local algebra and a subalgebra with no nontrivial idempotents. A two-dimensional such image is \(k\oplus kz\) with \(z\ne0\), \(z^2=0\): its maximal ideal is one-dimensional and nilpotent. As every \(x_j\) is nilpotent, \(e(x_j)\in kz\). Also the line \(kz\) cannot lie in \(\mathfrak m^2\), because then \(e(\mathfrak m^2)\subseteq(kz)^2=0\) while \(e(z)=z\ne0\). Consequently \(z\) has a nonzero linear term modulo \(\mathfrak m^2\).

**2. Square-zero normal form.** Write the degree-one part of \(z\) as \(\sum_j a_j x_j\). Since the characteristic is not two, the degree-two part of \(z^2=0\) is \(2\sum_{j<h}a_ja_h x_jx_h\). Distinct squarefree monomials are linearly independent, so at most one \(a_j\) is nonzero. Let this unique index be \(i\), and rescale \(z\) to make \(a_i=1\). Using the direct sum decomposition \(A_d=A'\oplus x_i A'\), where \(A'=k[x_j:j\ne i]/(x_j^2:j\ne i)\), write \(z=x_i u+b\) with \(u,b\in A'\), \(u\) of constant coefficient one, and \(b\in\mathfrak m_{A'}^2\). Squaring gives \(z^2=b^2+2x_iub\); the two summands lie in distinct direct summands, hence \(ub=0\). The element \(u\) is a unit, so \(b=0\). Thus \(z=x_i u\), as claimed. Expressing \(u\) in the squarefree monomial basis of \(A'\) proves there are exactly \(q^{2^{d-1}-1}=q^C\) normalized choices of \(z\) for a fixed pivot.

**3. All retractions.** Since \(e(x_j)\in kz\), put \(e(x_j)=v_jz\). From the coefficient of \(x_i\) in \(e(z)=z\), necessarily \(v_i=1\). Conversely choose an index \(i\), any normalized \(z=x_i u\) as above, and any scalars \(v_j\) with \(v_i=1\). The substitution \(x_j\mapsto v_jz\) respects \(x_j^2=0\), hence extends uniquely to a unital algebra homomorphism \(e\). Since the positive-degree nonlinear terms of \(z\) are products of two or more images and \(z^2=0\), evaluating \(z\) under \(e\) gives \(e(z)=v_i z=z\). Therefore \(e^2=e\) and its image is \(k\oplus kz\), of dimension two. Uniqueness of the pivot, normalized \(z\), and scalars \(v\) follows from the unique linear term and \(e(x_i)=z\). There are \(d q^C q^{d-1}=d q^B\) maps. Distinct normalized \(z\)'s yield distinct image subalgebras because two nonzero square-zero generators of the same two-dimensional algebra differ only by a nonzero scalar; normalization fixes that scalar. Thus each of the \(d q^C\) images has \(q^{d-1}\) retractions.

**4. Conjugacy.** The substitution \(\theta(x_i)=z\) and \(\theta(x_j)=x_j\) for \(j\ne i\) is an automorphism: replacing \(x_i\) by \(x_i u\) with \(u\) a unit has an invertible tangent linear part, and the images satisfy all square relations. It intertwines \(e\) with the linear normal form \(e_{i,v}\) sending \(x_j\mapsto v_jx_i\), because \(e(z)=z\). Therefore every retraction is conjugate to a map with no nonlinear tail.

For any automorphism \(\psi\), the nonzero tangent linear part of each \(\psi(x_j)\) must lie on a single coordinate axis by the square-zero argument of Step 2. Since the tangent map is invertible, these axes are pairwise distinct. Thus its tangent matrix is monomial (a permutation times a nonzero diagonal matrix). Conjugation of \(e_{i,v}\) by a monomial tangent matrix preserves the number \(s\) of nonzero entries of its unique nonzero row outside the pivot. Conversely, coordinate permutations and nonzero rescalings send any pair of such linear projections having the same \(s\) to one another. Hence exactly \(d\) orbits occur. For a given \(s\), there are \(d\) choices of pivot, \(\binom{d-1}{s}\) choices of off-pivot support, \((q-1)^s\) choices of its nonzero coefficients, and \(q^C\) choices of \(z\). Their product proves \(O_s\).

**5. Exact commutation and graph degree.** For \(e=(i,z,v)\) and \(f=(h,t,w)\), the square-zero nature of \(z\) and \(t\) implies \(e(t)=v_hz\) and \(f(z)=w_it\). Therefore, for each generator \(x_j\),
\[
(e\circ f)(x_j)=w_jv_hz,\qquad (f\circ e)(x_j)=v_jw_it.
\]
If \(i=h\), evaluating \(j=i\) shows \(z=t\), after which all \(v_j=w_j\), so the maps are equal. If \(i\ne h\), the linear parts of \(z\) and \(t\) are independent; equality for all \(j\) is equivalent to \(v_h=w_i=0\). Conversely those two vanishing conditions make both compositions equal to the augmentation map. This proves the criterion.

A vertex with exactly \(t\) zero entries among its \(d-1\) off-pivot coefficients can commute with vertices of exactly those \(t\) other pivot types. Each permitted pivot type has \(q^C q^{d-2}=q^{B-1}\) choices, because its scalar coefficient at the original pivot must vanish. Therefore its graph degree is \(tq^{B-1}\). Since \(s=d-1-t\), degree uniquely determines \(s\). The number of vertices with that degree is \(d\binom{d-1}{t}(q-1)^{d-1-t}q^C\), yielding \(\mathcal D_{d,q}\). Summing degrees gives \(d(d-1)q^{2B-2}\) and halving counts edges. Adding the \(d q^B\) diagonal pairs gives \(N_{\mathrm{comm}}\). For \(t=0\), the degree formula yields \(d(q-1)^{d-1}q^C\) isolated vertices. A clique contains at most one vertex per pivot, hence at most \(d\) vertices. Taking, for each pivot \(i\), the coordinate projection sending all \(x_j\) with \(j\ne i\) to zero realizes a commuting clique of size \(d\). \(\square\)

## Verification

The standalone Python program `verify_retractions.py` uses exact prime-field arithmetic and a squarefree-monomial multiplication table. It exhaustively constructs **all** algebra endomorphisms in dimensions \(d=2\), for \(q=3\) and \(q=5\), tests their defining square relations and composition idempotence, then computes their actual image dimensions. It finds, respectively, \(18\) and \(50\) image-dimension-two retractions, exactly the predicted parameter sets; all other idempotents have image dimensions one or four. For \(d=2\), \(q=3,5\) and \(d=3\), \(q=3\), it generates every predicted rank-two retraction, evaluates \(e^2=e\), tests image rank two, explicitly checks the coordinate-normalizing automorphism intertwining identities, and compares **all ordered pairs** by direct substitution against the commutation criterion. The outputs are:

| \((d,q)\) | Rank-two retractions | Orbit sizes by \(s\) | Ordered commuting pairs |
|---|---:|---|---:|
| \((2,3)\) | 18 | 6, 12 | 36 |
| \((2,5)\) | 50 | 10, 40 | 100 |
| \((3,3)\) | 729 | 81, 324, 324 | 40,095 |

These finite computations are independent corroboration for the specified prime-field cases, not proof for arbitrary \(q\) or \(d\). The general theorem is proved in Steps 1–5. Run `python3 verify_retractions.py` with standard Python 3, without external dependencies.

## Relationship to prior work

Díaz, Liendo, Manzano-Flores and Regeta (arXiv:2408.02197; first public 2024-08-05) study automorphism groups of zero-dimensional monomial algebras in characteristic zero. In particular, Example 4.25 analyzes the automorphism group of \(k[x,y]/(x^2,y^2)\); their theorem concerns **automorphisms**, not the present all-dimension idempotent retraction or commuting-graph classification. The full accessible HTML treatment of their work was examined, including the stated characteristic-zero scope and Example 4.25.

The public result *Automorphism orbits and rank counts of characteristic-two square-zero-variable algebra retractions* (2026-10-12, published-finding corpus identifier ending `256249efd1a0`) already proves **all-rank** retraction orbit and rank counts when the characteristic equals two. Its `RESULT.md` was read. That result does not cover odd characteristic and has, in particular, only one orbit of rank-two retracts; the \(d\) distinct odd-characteristic orbits and degree-rigidity law here are not its corollaries. The public result *An exact prime-power symmetry jump for modular monomial complete intersections* (2026-11-02, identifier ending `bac767308614`) proves an automorphism tangent-group jump for exponents \(p^e\) and \(p^e+1\); its `RESULT.md` was read. For odd \(p\) this does not include the exponent-two retraction problem and does not count commuting retractions.

Epstein and Nguyen, *Algebra retracts and Stanley–Reisner rings* (arXiv:1301.3967, 2013), prove structural results on **graded** monomial algebra retracts, notably Theorem 6.4 for irreducible monomial ideals as cited by the characteristic-two result. Their graded retract framework does not by itself provide a classification of all non-graded endomorphisms, the precise orbit sizes, or the commuting-graph degree spectrum here. Their abstract and bibliographic record were checked, but their complete article was not independently inspected in this work. The present theorem does not claim to originate the notions of dual-number tensor powers, algebra retracts, or monomial automorphisms.

## Limitations

The claim concerns only retractions with two-dimensional image, not all image ranks. The formulas assume odd characteristic; extension-field verification rests on the general algebraic proof rather than a computational enumeration of nonprime fields. The automorphism-group classification is at the level of \(k\)-rational points and composition conjugacy, not group schemes. Originality comparisons rely on accessed primary and public material and cannot exclude equivalently phrased unpublished results or inaccessible historical literature. No independent mathematical audit is claimed.

## References

1. R. Díaz, A. Liendo, G. Manzano-Flores, A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197v1, first posted 2024-08-05. https://arxiv.org/abs/2408.02197
2. *Automorphism orbits and rank counts of characteristic-two square-zero-variable algebra retractions*, 2026-10-12. https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-automorphism-orbits-and-rank-counts-of-characteristic-two-square--256249efd1a0
3. *An exact prime-power symmetry jump for modular monomial complete intersections*, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-an-exact-prime-power-symmetry-jump-for-modular-monomial-complete--bac767308614
4. N. Epstein, H. D. Nguyen, *Algebra retracts and Stanley–Reisner rings*, arXiv:1301.3967v2, 2013; J. Pure Appl. Algebra 218 (2014), 1665–1682. https://arxiv.org/abs/1301.3967
