# Sharp polynomial growth of distinct \(k\)-decks for every alphabet and fixed read length

## Finding

Let \(q\ge2\) and \(k\ge1\) be fixed integers, and let \(D_{q,k}(n)\) be the number of distinct vectors of length-\(k\) scattered-subsequence multiplicities realized by words of length \(n\) over a \(q\)-letter alphabet. Write
\[
L_q(j)=\frac1j\sum_{d\mid j}\mu(d)q^{j/d},\qquad
E_q(k)=\sum_{j=1}^{k}jL_q(j)-1,
\]
where \(\mu\) is the Möbius function. Then
\[
\boxed{D_{q,k}(n)=\Theta_{q,k}\bigl(n^{E_q(k)}\bigr).}
\]
More precisely, there is an explicit positive integer \(C_{q,k}\), depending only on \(q,k\), such that for every positive integer \(R\) there are at least \(2^{R E_q(k)}\) distinct \(k\)-decks of words of the common length \(C_{q,k}(2^R-1)\). These words are obtained from finite positive-word pairs by a constructive rational-linear-algebra selection and a base-\(2^j\) digit encoding at each homogeneous level \(j\).

This supplies the matching lower bound asked for in Conjecture 8.1 of Nilforoushan and Parvaresh (2026). The matching upper bound is their Theorem 5.1, not reproved here.

## Assumptions and scope

The alphabet is \(\Sigma=\{0,1,\ldots,q-1\}\). For words \(w,u\) let \(\binom wu\) denote the number of increasing choices of positions spelling \(u\) in \(w\); the empty pattern occurs once. The \(k\)-deck of \(w\), for \(|w|\ge k\), is \((\binom wv)_{v\in\Sigma^k}\). The quantity \(L_q(j)\) is also the rational dimension of the homogeneous degree-\(j\) piece \(\mathfrak L_j\) of the free Lie algebra on the letters \(X_a\), by the classical Witt formula. All implicit constants may depend on the fixed values of \(q,k\), not on \(n\). Only finite words and ordinary scattered subsequences are considered.

Calculations take place in the truncated associative algebra \(\mathcal A_k=\mathbb Q\langle X_0,\ldots,X_{q-1}\rangle/(\text{monomials of degree greater than }k)\), where \(\mathfrak L_j\) embeds as Lie polynomials under commutator \([P,Q]=PQ-QP\).

## Proof

**1. Subsequence signatures and low-degree differences.** Define
\[
S(w)=\prod_{t=1}^{|w|}(1+X_{w_t})
=\sum_{|v|\le k}\binom wv X_v\quad\text{in }\mathcal A_k.
\]
The product is in word order. In particular, \(S(uv)=S(u)S(v)\). A pair of words \((U,V)\) of the same length is a *degree-\(j\) difference pair* if \(S(U)-S(V)\) has no terms of degree below \(j\) and its degree-\(j\) part \(P(U,V)\) is nonzero. Throughout, the pairs constructed for \(j\ge2\) have equal letter counts.

**2. Producing a basis of difference pairs at every degree.** At degree one take
\[
(U_{1,a},V_{1,a})=(a,q-1),\qquad 0\le a<q-1.
\]
Their leading polynomials \(X_a-X_{q-1}\) form a basis of the \((q-1)\)-dimensional zero-sum linear subspace, exactly the degree-one freedom at fixed total word length.

At degree two take \((U_{2,a,b},V_{2,a,b})=(ab,ba)\) for \(a<b\). Their leading polynomials \([X_a,X_b]\) are a basis of \(\mathfrak L_2\).

For \(j\ge2\), suppose equal-length pairs \((U_i,V_i)\) have equal signatures below degree \(j\), and their degree-\(j\) differences \(P_i\) form a basis of \(\mathfrak L_j\). For each letter \(a\), consider
\[
(U_i a V_i,\; V_i a U_i).
\]
Writing \(B=S(V_i)\), \(\Delta=S(U_i)-S(V_i)\) and \(C_i=\sum_b|U_i|_bX_b\), the difference of the new signatures is exactly
\[
\Delta(1+X_a)B-B(1+X_a)\Delta.
\]
Its terms through degree \(j\) vanish, while the degree-\((j+1)\) term is
\[
[P_i,X_a+C_i].
\]
For fixed \(i\), the \(q\) vectors \(X_a+C_i\) span \(\mathfrak L_1\): their coefficient matrix is \(I+c_i\mathbf1^{\mathsf T}\), whose determinant is \(1+\sum_b|U_i|_b=1+|U_i|>0\). Since \(\mathfrak L_{j+1}=[\mathfrak L_j,\mathfrak L_1]\), by generation in degree one and the Jacobi identity, the candidate leading differences span the entire \(\mathfrak L_{j+1}\). Choosing a rational-linearly independent subfamily therefore gives precisely \(L_q(j+1)\) required pairs. The construction is deterministic after fixing an order and selecting each candidate that increases rational rank. Equal word lengths and equality of all lower signatures are preserved at every step. This induction covers every fixed degree up to \(k\).

Let \(m_1=q-1\) and \(m_j=L_q(j)\) for \(j\ge2\), and enumerate these pairs as \((U_{j,i},V_{j,i})\), \(1\le i\le m_j\). The leading differences \(P_{j,i}\) are linearly independent at every level. Put
\[
C_{q,k}=\sum_{j=1}^k(2^j-1)\sum_{i=1}^{m_j}|U_{j,i}|>0.
\]

**3. Uniform expansion gives weighted independent digits.** For an integer \(m\ge1\), let \(\phi_m\) replace each letter by \(m\) copies of itself. Under the signature map, this is the algebra substitution \(X_a\mapsto(1+X_a)^m-1\). If the leading difference of a pair is \(P\) of degree \(j\), expansion preserves all lower equalities and changes the degree-\(j\) difference to \(m^jP\); higher-degree terms cannot contribute to that homogeneous degree.

Fix \(R\ge1\). For each pair \((j,i)\) and each \(0\le r<R\), define \(U_r=\phi_{2^r}(U_{j,i})\), \(V_r=\phi_{2^r}(V_{j,i})\), and \(b_j=2^j-1\). Choose a digit \(d_{j,i,r}\in\{0,1,\ldots,b_j\}\), and form a block
\[
V_r^{\,d_{j,i,r}}U_r^{\,b_j-d_{j,i,r}}.
\]
Concatenate all blocks in an arbitrary but fixed order first by \(j\), then \(i\), then \(r\). The resulting word has length \(C_{q,k}(2^R-1)\), independently of the digits. Replacing the zero digit by \(d\) changes its block signature first in degree \(j\), with leading term \(-d\,2^{rj}P_{j,i}\). This follows by telescoping the difference of the two products: all factors have constant term one, and the individual \(V_r-U_r\) signature difference starts in degree \(j\).

Suppose two assignments of all digits produced the same truncated signature. Let \(j\) be the smallest level at which their digits differ. At every smaller level the blocks are identical; at every larger level the block differences begin strictly above degree \(j\). Multiplicativity of signatures therefore makes the degree-\(j\) difference equal exactly
\[
-\sum_{i=1}^{m_j}\left(\sum_{r=0}^{R-1}
(d_{j,i,r}-d'_{j,i,r})2^{rj}\right)P_{j,i}.
\]
Linear independence of the \(P_{j,i}\) forces each coefficient to vanish. But the digits are in \(\{0,\ldots,2^j-1\}\), so uniqueness of base-\(2^j\) expansion forces \(d_{j,i,r}=d'_{j,i,r}\) for every \(i,r\), a contradiction. Hence the assignment-to-signature map is injective. The number of assignments is
\[
\prod_{j=1}^{k}(2^j)^{Rm_j}
=2^{R((q-1)+\sum_{j=2}^k jL_q(j))}
=2^{R E_q(k)}.
\]

**4. From truncated signatures to the actual length-\(k\) decks.** For a word \(w\) of length \(n\ge k\) and a pattern \(u\) of length \(j\le k\), double-counting nested choices of indices gives the exact identity
\[
\sum_{v\in\Sigma^k}\binom wv\binom vu
=\binom{n-j}{k-j}\binom wu.
\]
The binomial multiplier is positive. Thus the actual length-\(k\) deck determines all shorter decks, and two different truncated signatures of equal-length words necessarily have different \(k\)-decks.

For arbitrary sufficiently large \(n\), choose the largest \(R\) for which \(N_R=C_{q,k}(2^R-1)\le n\), and append the same suffix \(0^{n-N_R}\) to every constructed word. Multiplication by the signature \(S(0^{n-N_R})\), whose constant term is one, is invertible in the truncated algebra; it preserves signature distinctness. Maximality of \(R\) gives
\[
2^R>\frac{n/C_{q,k}+1}{2},
\]
so the number of distinct \(k\)-decks is at least \((n/(2C_{q,k}))^{E_q(k)}\). This proves the required \(\Omega_{q,k}(n^{E_q(k)})\) lower bound. The same argument covers \(k=1\), using just the degree-one pairs.

**5. Upper bound.** Nilforoushan and Parvaresh, Theorem 5.1 (2026), already prove \(D_{q,k}(n)=O_{q,k}(n^{E_q(k)})\) for \(k\ge2\). For \(k=1\), the elementary exact count \(D_{q,1}(n)=\binom{n+q-1}{q-1}\) has the required upper order. Combining these gives the claimed \(\Theta\)-law. \(\square\)

## Verification

The accompanying dependency-free Python program `verify.py` reconstructs all selected finite word-pair bases by exact rational row reduction, checks equal lengths and exact lower-degree cancellation, and checks the degree-\(j\) scaling identity for expansion factors two and three. It verifies the Witt ranks for \((q,k)=(2,2),(2,3),(3,2),(3,3),(2,4),(4,3)\). Direct enumeration confirms that all \(64\), \(512\), and \(256\) constructed words have *distinct actual length-\(k\) decks* for \((q,k,R)=(2,2,2),(2,3,1),(3,2,1)\), respectively, and verifies the nested-deck identity on sample codewords. The first-level constants for \((q,k)=(3,3),(2,4),(4,3)\) are also computed, but their exponentially large codebooks are not exhaustively enumerated. The full output is in `verification_output.txt`.

These tests corroborate the constructive proof; finite verification alone would not establish its all-parameter claims.

## Relationship to prior work

Nilforoushan and Parvaresh (arXiv:2609.23106, first posted September 19, 2026) prove the universal upper bound in Theorem 5.1 and establish matching lower bounds in the cases \(k\le2\) and \((q,k)=(2,3)\). Their Conjecture 8.1 asks for the full matching \(\Theta\)-law and Section 8 explicitly leaves the general lower bound unproved. The present result constructs the missing lower bound simultaneously for all fixed \(q,k\).

Lejeune, Rigo and Rosenfeld (arXiv:2001.11732, 2020, particularly Section 4) study \(k\)-binomial classes and obtain the exact growth order for \(k=2\), alongside a general coarser upper bound. Chrisnata and collaborators (2019/2023) provide earlier finite data and weaker general asymptotic bounds for the binary alphabet. Free Lie homogeneous dimensions and the Witt formula are classical; they are used, not claimed as new.

The new part is the finite recursive construction of positive-word difference pairs spanning each homogeneous Lie degree, together with a shared-length digital scaling and an all-level injection argument. The result is mathematically distinct from the existing upper bound and its previously known small-parameter lower-bound cases.

## Limitations

The statement gives the exact *polynomial growth exponent*, not a leading asymptotic coefficient or an exact count at each finite length. The explicit construction has constants that can grow rapidly with \(q,k\); no efficient encoding/decoding complexity is claimed. It assumes a fixed finite alphabet, fixed \(k\), and the usual subsequence multiplicities, not substring decks or growing \(k\). The upper bound is taken from the cited 2026 paper. The conclusion has not undergone independent mathematical validation, and priority relative to all unindexed literature remains to be established.

## References

1. A. Nilforoushan and F. Parvaresh, *Improved upper bound on the number of distinct k-decks for any k and alphabet size by counting the independent parameters*, arXiv:2609.23106 (initial version September 19, 2026), especially Theorem 5.1 and Conjecture 8.1. https://arxiv.org/abs/2609.23106
2. M. Lejeune, M. Rigo and M. Rosenfeld, *On the binomial equivalence classes of finite words*, arXiv:2001.11732 (January 31, 2020), Section 4; subsequently *International Journal of Algebra and Computation* 30 (2020), 1375–1397. https://arxiv.org/abs/2001.11732
3. J. Chrisnata, H. M. Kiah, S. R. Karingula, A. Vardy, E. Yaakobi and H. Yao, *On the number of distinct k-decks: Enumeration and bounds*, *Advances in Mathematics of Communications* 17 (2023), 960–978. https://doi.org/10.3934/amc.2021032
4. C. Reutenauer, *Free Lie Algebras*, Oxford University Press (1993), for the classical Witt dimension formula and free Lie algebra structure.
