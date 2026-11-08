# A palindromic square-root law for perfect binary path-pattern evolution algebras

## Finding
For every integer \(n\ge2\), let \(E_{n,\mathbf d}\) be the evolution algebra over \(\mathbb F_2\) with natural basis \(e_1,\ldots,e_n\) and products
\[
e_i e_j=0\quad(i\ne j),\qquad e_i^2=e_{i-1}+d_i e_i+e_{i+1},
\]
where \(d_i\in\mathbb F_2\) and nonexistent endpoint terms are omitted. Denote by \(\mathcal P_n\) the set of these algebras with \(E_{n,\mathbf d}^2=E_{n,\mathbf d}\) (equivalently, invertible structure matrix). Define
\[
a_n=\frac{2^{n+1}+(-1)^n}{3},\quad b_n=a_{\lfloor n/2\rfloor}.
\]
Then exactly \(a_n\) diagonal strings define perfect algebras. Of these, precisely \(b_n\) have a nonidentity \(\mathbb F_2\)-algebra automorphism, which is necessarily reflection of the natural basis, so their ordinary automorphism group is \(C_2\); all other members have trivial automorphism group. Two perfect members are isomorphic exactly when their diagonal strings agree or are reversals. Hence the exact number of unrestricted algebra-isomorphism classes occurring in \(\mathcal P_n\) is
\[
\boxed{\frac{a_n+b_n}{2}},
\]
and the proportion of uniformly selected perfect members with nontrivial automorphism group is
\[
\boxed{\frac{b_n}{a_n}=2^{-\lceil n/2\rceil}\left(1+O(2^{-\lfloor n/2\rfloor})\right)}.
\]
In particular, reflection-symmetric perfect members are exponentially rare on the half-dimension scale.

## Assumptions and scope
The coefficient field is exactly \(\mathbb F_2\). The underlying *off-diagonal support* is the undirected path on \(n\) labeled vertices, with the two adjacent entries equal to one; diagonal loops are independently allowed or absent. All isomorphisms and automorphisms are unrestricted \(\mathbb F_2\)-linear algebra isomorphisms, not merely graph maps preserving a chosen natural basis. The conclusion is about perfect members (invertible structure matrix) only. We do not assert the same formula over larger fields or for arbitrary graph-supported evolution algebras.

## Proof
Write \(T_n(\mathbf d)\) for the symmetric tridiagonal structure matrix and \(D_n(\mathbf d)=\det T_n(\mathbf d)\in\mathbb F_2\). With \(D_0=1\) and \(D_{-1}=0\), Laplace expansion gives the continuant recursion
\[
D_j=d_jD_{j-1}+D_{j-2},\qquad j\ge1,
\]
where the relevant prefix of \(\mathbf d\) is implicit. Since the consecutive state \((D_j,D_{j-1})\) is never \((0,0)\), write \(u_j,v_j,w_j\) for the numbers of length-\(j\) strings with respective states \((1,0),(1,1),(0,1)\). Appending a free bit gives
\[
(u_{j+1},v_{j+1},w_{j+1})=(2w_j,u_j+v_j,u_j+v_j).
\]
The initial counts are \((u_1,v_1,w_1)=(0,1,1)\). Thus \(a_j=u_j+v_j\) obeys \(a_{j+1}=a_j+2a_{j-1}\), with \(a_0=a_1=1\), and solving gives \(a_j=(2^{j+1}+(-1)^j)/3\). This counts exactly those diagonal strings for which \(D_j=1\).

Next consider a reflection-palindromic diagonal string. Let \(L_j\) be the continuant of its first \(j\) entries. The standard concatenation identity for continuants, obtained by multiplying the two by two transfer matrices or expanding at the join, gives in characteristic two:
\[
D_{2m}(d_1,\ldots,d_m,d_m,\ldots,d_1)=L_m^2+L_{m-1}^2=(L_m+L_{m-1})^2,
\]
\[
D_{2m+1}(d_1,\ldots,d_m,c,d_m,\ldots,d_1)=cL_m^2.
\]
For even length, \(L_m+L_{m-1}\) is the determinant of the length-\(m\) tridiagonal matrix with its last diagonal bit toggled. Toggling is a bijection on all \(m\)-bit strings. For odd length, the determinant is nonzero exactly when \(c=1\) and \(L_m=1\). Thus in both parity cases the number of invertible palindromic diagonal strings is exactly \(a_m\), where \(m=\lfloor n/2\rfloor\).

Finally, an isomorphism between two perfect evolution algebras sends a natural basis to nonzero scalar multiples of a permuted natural basis. This is the established monomial-isomorphism theorem for nonsingular evolution algebras (Wei--Zou, citing Elduque--Labra). Over \(\mathbb F_2\), all nonzero scalars equal one, so any isomorphism is an ordinary basis permutation. Each structure matrix has nonzero off-diagonal entries precisely at pairs of adjacent path vertices, and a permutation preserving this support is either the identity or reversal. The identity can identify two matrices only when their diagonal strings coincide; reversal identifies them when the strings are reversed. Reversal fixes one matrix exactly when its diagonal string is a palindrome. There are no other possible automorphisms. Burnside's two-element orbit formula gives \((a_n+a_{\lfloor n/2\rfloor})/2\) classes, and the ratio of the palindrome count to the total yields the stated asymptotic by the explicit formula for \(a_j\).

## Verification
The accompanying standalone Python checker enumerates all \(2^n\) binary diagonal strings for every \(2\le n\le12\), recomputes the continuant determinant and the palindrome count, and verifies the exact formulas. For all perfect members at dimensions \(2\le n\le6\), it also enumerates *every* permutation of the natural basis, checks the entire multiplication table, and confirms that the automorphism group has order two exactly for palindromes and order one otherwise. Its output ends in `VERIFY_OK`. These finite checks supplement, but cannot replace, the proof for all dimensions.

## Relationship to prior work
Wei and Zou (first public preprint October 18, 2023, arXiv:2310.12368v1) established the monomial action and general Burnside framework for *all* perfect finite-field evolution algebras and computed unrestricted isomorphism-class totals through dimension four. We use their structural theorem without claiming it as new. Their inspected full preprint does not give the path-supported exact class numbers, the parity-dependent palindrome determinant identities or the half-dimension automorphism-rarity law. General graph-based automorphism results supply a conceptual antecedent but do not by themselves count invertible path patterns. The new object here is the exact **joint** perfection/isomorphism/automorphism census for this path-loop family.

## Limitations
The field \(\mathbb F_2\), off-diagonal path support and unit edge entries are essential to the stated formula. This work does not classify nonperfect members, arbitrary sparse patterns, larger finite fields, or automorphism group schemes. No independent validation or complete universal literature-priority guarantee is claimed. Finite enumeration is not a proof for unbounded \(n\).

## References
- Yangjiang Wei and Yi Ming Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368v1, first public October 18, 2023, https://arxiv.org/pdf/2310.12368 . Theorem 1.1, Corollary 1.1, and Section 2.
- Alberto Elduque and Alicia Labra, *On the automorphism group of an evolution algebra*, cited in Wei--Zou's Theorem 1.1, for the general monomial-isomorphism criterion.
