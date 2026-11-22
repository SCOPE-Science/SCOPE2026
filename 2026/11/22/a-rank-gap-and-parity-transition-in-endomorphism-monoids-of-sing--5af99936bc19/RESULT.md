# A rank gap and parity transition in endomorphism monoids of singular Cayley evolution algebras

## Finding
Let \(k\) be **any field of characteristic two** and \(n\ge3\). Define the commutative, generally nonassociative evolution algebra \(E_n(k)\), with basis \(e_i\) indexed by \(\mathbb Z/n\mathbb Z\), by
\[
e_i e_j=0\ (i\ne j),\qquad e_i^2=e_i+e_{i+1}.
\]
Write \(w=\sum_i e_i\), \(\rho_r(e_i)=e_{i+r}\), and \(\psi_a(e_i)=a w\). Then the **complete set of unrestricted algebra endomorphisms** is
\[
\boxed{\operatorname{End}_{k\text{-alg}}(E_n)=\{\rho_r:r\in\mathbb Z/n\mathbb Z\}\ \sqcup\ \{\psi_a:a\in k\}.}
\]
The union is disjoint, with \(\psi_0=0\). In particular, \(\operatorname{Aut}(E_n)\cong C_n\), and every nonzero noninvertible endomorphism has rank one: ranks \(2,\ldots,n-1\) never occur. Over \(k=\mathbb F_q\), \(q\) a power of two, the exact rank polynomial and total count are
\[
\boxed{\sum_{F\in\operatorname{End}(E_n)}T^{\operatorname{rank}F}=1+(q-1)T+nT^n,\qquad |\operatorname{End}(E_n)|=q+n.}
\]
The multiplication of the endomorphism monoid, understood as composition, is determined by
\[
\rho_r\rho_s=\rho_{r+s},\quad \rho_r\psi_a=\psi_a\rho_r=\psi_a,\quad
\psi_a\psi_b=\begin{cases}\psi_{ab},&n\text{ odd},\\0,&n\text{ even}.\end{cases}
\]
The **algebra ideals** of \(E_n\) are exactly \(0\), \(E_n^2\), and \(E_n\), where \(\dim_k E_n^2=n-1\). The extension by the zero-multiplication quotient,
\[
0\longrightarrow E_n^2\longrightarrow E_n\longrightarrow k_0\longrightarrow0,
\]
splits as an extension of \(k\)-algebras exactly for odd \(n\). Hence its complete algebra-retraction list is \(\{0,\operatorname{id},\psi_1\}\) for odd \(n\), and \(\{0,\operatorname{id}\}\) for even \(n\).

## Assumptions and scope
Here \(k_0\) is the one-dimensional algebra with zero multiplication. An algebra endomorphism is any \(k\)-linear multiplicative map, **not** necessarily unital, invertible, natural-basis preserving, or a graph map. The algebra is nonunital and nonperfect; the field may be infinite or imperfect as long as its characteristic is two. The finite-field census requires \(q=2^f\). There are no claims for \(n=1,2\) or for fields of other characteristics. Multiplication of operators means composition, not pointwise addition; the set of multiplicative maps need not be a vector space.

This is a cyclic-group instance of the Cayley evolution algebra construction of Costoya--Muñoz--Tocino--Viruel: take the group algebra \(k[C_n]\), generator \(g\), and support-weight function \(f(1)=f(g)=1\), all other weights zero. Then \(e_i^2=e_i+e_{i+1}\). It is **singular** because the structure matrix is \(I+S\) in characteristic two.

## Proof
**1. Structure matrix and annihilation criterion.** Identify \(E_n\) with \(k^n\) and let \(S\) be the cyclic shift \(S e_i=e_{i+1}\). Then
\[
xy=(I+S)(x\circ y),
\]
where \(\circ\) denotes the coordinatewise (Hadamard) product. Since \((I+S)v=0\) exactly when all coordinates of \(v\) agree, \(\ker(I+S)=k w\) and \(\operatorname{rank}(I+S)=n-1\). In particular \(w^2=(I+S)w=0\). For any multiplicative map \(F\), writing \(v_i=F(e_i)\), the defining conditions are **equivalent** to
\[
(I+S)(v_i\circ v_j)=0\quad(i\ne j),\qquad
(I+S)(v_i\circ v_i)=v_i+v_{i+1}\quad(\forall i).
\tag{1}
\]
Equivalence follows by bilinearity from the basis multiplication table.

**2. Vanishing propagates; dense intersections force rank one.** If \(v_i=0\), the second condition in (1) gives \(v_{i+1}=0\), and cycling forces \(F=0\). Hence a nonzero endomorphism has every \(v_i\ne0\). Suppose there exist distinct \(i,j\) such that \(v_i\circ v_j\ne0\). The first condition in (1) implies \(v_i\circ v_j=cw\) with \(c\ne0\); both vectors have every coordinate nonzero. For each \(\ell\ne i\), \(v_i\circ v_\ell=c_\ell w\); because \(v_i\) is coordinatewise invertible and \(v_\ell\ne0\), \(c_\ell\ne0\), so
\[
v_\ell=c_\ell v_i^{\circ(-1)}.
\]
As \(n\ge3\), choose distinct \(j,\ell\ne i\). Then \(v_j\circ v_\ell\in kw\), and its nonzero coefficient forces the coordinatewise square of \(v_i^{\circ(-1)}\) to be constant. In any field of characteristic two, the squaring map is injective; therefore \(v_i\) itself is constant across coordinates. All \(v_\ell\), including \(v_i\), are nonzero scalar multiples of \(w\). Write \(v_i=a_iw\); the second equation in (1) becomes \(0=(a_i+a_{i+1})w\). Thus every \(a_i\) is the same nonzero \(a\), giving \(F=\psi_a\).

**3. Disjoint supports force cyclic rotations.** Otherwise, every distinct pair has \(v_i\circ v_j=0\), i.e. the \(n\) nonempty coordinate supports are pairwise disjoint subsets of an \(n\)-element set. Each is therefore a singleton and together they partition all coordinates. Hence \(v_i=a_i e_{\pi(i)}\) for some permutation \(\pi\) and \(a_i\in k^\times\). Substitution into the second equation of (1) gives
\[
a_i^2(e_{\pi(i)}+e_{\pi(i)+1})
=a_i e_{\pi(i)}+a_{i+1}e_{\pi(i+1)}.
\]
The two basis positions on the right are distinct, as are those on the left, and \(\pi(i)\) occurs on both sides. Therefore \(\pi(i+1)=\pi(i)+1\) for all \(i\), so \(\pi\) is a rotation. Comparing coefficients yields \(a_i^2=a_i\), hence \(a_i=1\). Thus \(F=\rho_r\). Conversely, rotations preserve all defining products, and each \(\psi_a\) preserves them because \(w^2=0\) and \(\psi_a(e_i+e_{i+1})=0\). The two classes exhaust all endomorphisms. Their ranks and finite-field counts follow immediately.

**4. Composition, idempotents and the parity obstruction.** Clearly rotations fix \(w\), giving \(\rho_r\psi_a=\psi_a\rho_r=\psi_a\). Also \(\psi_a(w)=na w\), where the scalar \(n\in k\) equals one if \(n\) is odd and zero if \(n\) is even. Thus \(\psi_a\psi_b(e_i)=nabw\), establishing the full monoid multiplication. A composition-idempotent rotation is only \(\rho_0\). The equation \(\psi_a^2=\psi_a\) has the additional nonzero solution \(a=1\) exactly for odd \(n\).

**5. Ideal lattice and splitting.** The span of all products is \(E_n^2=(I+S)E_n\), a codimension-one ideal; it consists exactly of vectors whose coordinate sum is zero. If a nonzero ideal \(J\) contains \(x\) with \(i\)-th coordinate nonzero, then \(e_i x=x_i e_i^2\in J\), so \(e_i^2\in J\). Multiplying this by \(e_{i+1}\) yields \(e_{i+1}^2\in J\), and cycling proves \(E_n^2\subset J\). Codimension one leaves only \(J=E_n^2\) or \(J=E_n\). Finally \(u^2=0\) if and only if \(u_i^2\) is constant for all \(i\); injectivity of squaring implies \(u\in kw\). A section of \(E_n\twoheadrightarrow k_0\) exists precisely when it has a square-zero representative outside \(E_n^2\), i.e. when \(w\notin E_n^2\). Since the coordinate sum of \(w\) is the parity of \(n\), this occurs exactly for odd \(n\). The retraction assertion also follows from the complete monoid classification in Step 4.

## Verification
The standalone file `verify_cayley_loop_endomorphisms.py` tests the **original multiplication identity** for every linear map on \(E_3(\mathbb F_2)\) (512 maps), \(E_4(\mathbb F_2)\) (65,536 maps) and \(E_3(\mathbb F_4)\) (262,144 maps, with explicit arithmetic in \(\mathbb F_4\)). It compares each exhaustive solution set to the stated normal forms and finds respectively 5, 6 and 7 endomorphisms. Separate direct composition tests cover dimensions 3 through 6 over \(\mathbb F_2\). Run `python3 verify_cayley_loop_endomorphisms.py`; successful output ends with `CYCLIC_CAYLEY_ENDOMORPHISMS_VERIFIED`. The program is a finite cross-check only. The unrestricted-field and all-dimension result rests on the proof above, not on interpolation from tests.

## Relationship to prior work
Costoya, Muñoz, Tocino and Viruel introduced Cayley evolution algebras in arXiv:2207.01335v1 (July 4, 2022). Their automorphism-group theorem (Proposition 4.4) imposes **regularity/perfectness** of the structure matrix; the matrix \(I+S\) here is singular, so that theorem cannot directly determine its automorphisms or its noninvertible endomorphisms. Boudi, Cabrera Casado and Siles Molina (arXiv:2006.14460, especially Theorem 2.4 and Corollary 2.7) already established general natural-basis criteria including pairwise independent squares. Their monomial-rigidity criterion applies here and is **not** claimed to be new. The 2024 study of hereditary graph subsets and ideals (doi:10.1007/s13348-024-00435-x, Proposition 3.9) provides general maximal-ideal structure, but not the complete endomorphism monoid or the parity-dependent algebra-splitting assertion of this family.

The published complete endomorphism census for *nilpotent chain* evolution algebras treats \(e_i^2=e_{i+1}\) and a final zero square, rather than \(e_i^2=e_i+e_{i+1}\) with all vertices looped. That census admits intermediate ranks, unlike the gap established here. General permutation-cycle evolution algebras have **invertible** monomial structure matrices; the present singular two-support cyclic matrices are not contained in that class. Published asymptotic rigidity for random singular evolution algebras describes random matrices and does not determine this exact deterministic monoid. These are implication comparisons, not a global claim of publication priority.

## Limitations
The hypotheses \(n\ge3\) and characteristic two are essential to the proof: the dense-support argument uses three distinct columns and injectivity of squaring, and the kernel is the constant line specifically in characteristic two. The statement does not classify analogous looped-cycle algebras in odd characteristic, nor their full endomorphism schemes with infinitesimal structure. The finite-field rank count applies only to fields of order a power of two. A specialized earlier treatment of the same singular weighted cycle may have escaped bibliographic and indexed searches; originality is a best-knowledge conclusion, not independently certified.

## References
1. C. Costoya, V. Muñoz, A. Tocino and A. Viruel, *Automorphism groups of Cayley evolution algebras*, arXiv:2207.01335v1 (2022-07-04), https://arxiv.org/abs/2207.01335.
2. N. Boudi, Y. Cabrera Casado and M. Siles Molina, *Natural families in evolution algebras*, arXiv:2006.14460v1 (2020-06-25), https://arxiv.org/abs/2006.14460.
3. Y. Cabrera Casado, D. Martín Barquero, C. Martín González and A. Tocino, *Connecting ideals in evolution algebras with hereditary subsets of its associated graph*, first published 2024-03-14, https://doi.org/10.1007/s13348-024-00435-x.
4. D. Fernández-Ternero, V. M. Gómez-Sousa and J. Núñez-Valdés, *Evolution algebras whose evolution operator is a homomorphism*, 2021-09-30, https://doi.org/10.1002/cmm4.1200.
5. C. Costoya, P. Mayorga and A. Viruel, *Permutation Representations and Automorphisms of Evolution Algebras*, 2025-07-29, https://doi.org/10.1007/s00009-025-02924-0.
6. *Endomorphism monoid and reduced endomorphism variety of chain evolution algebras*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-endomorphism-monoid-and-reduced-endomorphism-variety-of-chain-ev--bb8c934f4813.
7. *Random singular evolution algebras are asymptotically rigid over every finite field*, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-random-singular-evolution-algebras-are-asymptotically-rigid-over--6c834a318056.
