# Exact palindromic language and sharp complexity of the generalized Cantor words

## Finding

Let \(b\ge3\) be an integer and let the binary generalized Cantor word \(c_b\) have a \(1\) precisely at those zero-based indices whose base-\(b\) digits belong to \(\{0,b-1\}\). For \(r\ge1\), write \(W_{b,r}=c_b[0:b^r]\), the palindrome consisting of the first \(b^r\) symbols, and for each \(t\ge0\) put
\[
T_{b,t}=0^{(b-2)b^{t+1}}W_{b,t+1}0^{(b-2)b^{t+1}},\quad
L_t=(b-2)b^t+2,\quad U_t=(2b-3)b^{t+1}.
\]

**Complete palindromic language.** Every nonempty palindromic factor of \(c_b\) is *exactly* one of the following:

1. \(0^n\), for any integer \(n\ge1\);
2. \(0^h10^h\), for an integer \(0\le h\le b-2\);
3. the uniquely centered factor of \(T_{b,t}\) of length \(n\), for integers \(t\ge0\), \(L_t\le n\le U_t\), and \(n\equiv b\pmod2\).

Every listed factor occurs; the three types are disjoint. Factors in type 3 for distinct \(t\) are distinct even at equal lengths. The complete set of *globally maximal palindromes*, meaning palindromic factors that possess neither a \(0\)-by-\(0\) nor \(1\)-by-\(1\) symmetric extension anywhere in \(c_b\), is precisely
\[
\{0^{b-2}10^{b-2}\}\ \cup\ \{T_{b,t}:t\ge0\}.
\]

Consequently, if \(P_b(n)\) is the number of distinct palindromic factors of length \(n\ge1\), then
\[
\boxed{P_b(n)=1+\mathbf1_{\{n\text{ odd},\ n\le2b-3\}}+
\mathbf1_{\{n\equiv b\pmod2\}}
\sum_{t\ge0}\mathbf1_{\{(b-2)b^t+2\le n\le(2b-3)b^{t+1}\}}.}
\]
The finite sum is actually at most two; for every \(b\ge3\) and \(n\ge1\), \(P_b(n)\le3\), with equality for infinitely many lengths. For the classical ternary word, \(P_3(1)=2\), \(P_3(n)=1\) for even \(n\), and \(P_3(n)=3\) for odd \(n\ge3\).

## Assumptions and scope

Indices are nonnegative and factors are finite contiguous subwords of the right-infinite word. The notation \(c_b[0:b^r]\) includes positions \(0,\ldots,b^r-1\). The word is also the fixed point starting in \(1\) of the \(b\)-uniform morphism \(1\mapsto10^{b-2}1\), \(0\mapsto0^b\). A globally maximal palindrome is nonextendible *anywhere in the infinite factor language*, not merely at a selected occurrence or finite-word boundary. The entire result applies to composite and prime integer bases alike; \(b=2\) is excluded because the digit restriction then gives the constant-one word.

## Proof

**1. All marker gaps.** Let \(a_b(k)\) be the position of the \((k+1)\)-st \(1\) (counting from \(k=0\)). If \(\epsilon_j(k)\in\{0,1\}\) are the binary digits of \(k\), then
\[
a_b(k)=(b-1)\sum_{j\ge0}\epsilon_j(k)b^j.
\]
If \(t=\nu_2(k+1)\), binary increment changes the trailing \(t\) ones of \(k\) into zeros and sets the next zero bit. Hence the successive-marker gap is
\[
a_b(k+1)-a_b(k)
=(b-1)b^t-(b-1)\sum_{j=0}^{t-1}b^j
=(b-2)b^t+1=:g_t.
\]
The numbers \(g_t\) are strictly increasing. In particular, adjacent gaps at any marker other than the first are \(g_{\nu_2(k)}\) and \(g_{\nu_2(k+1)}\), and exactly one has index zero. Thus their lengths are different and the smaller is \(g_0=b-1\).

**2. Zero-centered and one-centered palindromes.** All \(0^n\) occur since \(g_t\to\infty\). Every palindrome with an odd number of ones must center at a marker. If it contained three or more ones, its first neighboring marker on either side would have to be equidistant; this contradicts the unequal adjacent gaps from step 1. Therefore such a palindrome has exactly one \(1\); its maximum zero radius is \(g_0-1=b-2\), and this bound occurs at markers sufficiently far from the left boundary. All and only the type-2 factors occur. Moreover, \(0^{b-2}10^{b-2}\) cannot extend symmetrically because its two outward symbols at an occurrence are different (one is \(1\) at distance \(g_0\), the other \(0\)); no occurrence permits both symbols to agree.

**3. Symmetry about a central marker pair.** Every palindrome with at least two ones has an even number of them, and its center lies midway between two successive markers \(a_b(j)\), \(a_b(j+1)\). Write \(j+1=2^t(2q+1)\). The centered gap is \(g_t\). For each \(1\le h<2^t\), the gaps occurring symmetrically \(h\) steps to either side have the same valuation since
\[\nu_2(2^t(2q+1)-h)=\nu_2(h)=\nu_2(2^t(2q+1)+h).\]
Thus the block of \(2^{t+1}\) successive ones with binary support labels \(2^{t+1}q\) through \(2^{t+1}(q+1)-1\) is symmetric about the given pair. The gaps within this block and its intervening zero runs are independent of \(q\). Since the corresponding \(2^{t+1}\) markers occupy precisely the first \(b^{t+1}\) positions for \(q=0\), their block is the translate of \(W_{b,t+1}\). This block is a palindrome: reflecting every permitted base-\(b\) digit \(0\leftrightarrow b-1\) sends \(i\) to \(b^{t+1}-1-i\).

If \(q\ge1\), the two immediate exterior marker gaps of this block are
\[
g_{t+1+\nu_2(q)}\quad\text{and}\quad g_{t+1+\nu_2(q+1)}.
\]
One is exactly \(g_{t+1}\) while the other is strictly larger, because \(q\) and \(q+1\) have unequal valuations, one being zero. Therefore the common maximal extension of \(W_{b,t+1}\) by zeros is precisely \(g_{t+1}-1=(b-2)b^{t+1}\) symbols on each side, giving \(T_{b,t}\). Neither an extra symmetric pair of zeros nor of ones is possible at any occurrence. For the boundary case \(q=0\), a palindrome cannot extend to negative positions, and any such factor is still a centered factor of the longer word \(T_{b,t}\), which occurs at \(q\ge1\).

Any palindrome with at least two ones must contain its central two markers. Their gap \(g_t\) therefore forces the smallest possible length \(g_t+1=L_t\). Its parity agrees with \(g_t+1\), hence with \(b\), and its maximal length is \(U_t=|T_{b,t}|\). All intermediate admissible parity lengths arise as centered factors of an actual occurrence of \(T_{b,t}\). This proves the language classification and the complete list of maximal palindromes. Note that no \(0^n\) is globally maximal because longer all-zero runs occur.

**4. Exact counts.** At any fixed length, the all-zero factor contributes one; type 2 contributes one exactly for odd \(n\le2b-3\); type 3 contributes one for each admissible \(t\). Distinct type-3 indices yield distinct central gaps because \(g_t\) strictly increases, hence distinct factors. The formula follows. Nonadjacent type-3 index intervals cannot overlap, since
\[
L_{t+2}-U_t=(b-1)(b-3)b^{t+1}+2>0.
\]
Thus the sum contains at most two terms. When the one-centered contribution is possible, \(L_1>2b-3\), so at most one type-3 term is present. This gives \(P_b(n)\le3\). The intervals \([L_{t+1},U_t]\) contain lengths of the required parity for every \(t\ge0\); hence the bound is sharp infinitely often. At \(b=3\) these parity-compatible overlap intervals partition the odd lengths from \(3\) upward, apart from the one-centered initial exception, giving the stated special formula.

## Verification

A standalone Python 3 diagnostic \(\texttt{verify_cantor_palindromes.py}\) enumerates **actual factor strings**, compares their palindromicity and equality against the formula, for bases \(3\) through \(9\) and lengths \(1\) through \(160\). It checks all starts within finite prefixes of length \(\min(30000,b^9)\). Its expected-language construction is independent of the enumeration of observed factor strings. Successful output is \(\texttt{VERIFY_OK bases=3..9 lengths=1..160 total_cases=1120}\). This finite diagnostic is not an exhaustive infinite proof; steps 1–4 provide the infinite argument.

## Relationship to prior work

Chen, Lü and Wu investigated the original ternary Cantor word and proved \(k\)-Abelian complexity regularity; they did not supply the present all-base palindromic language or length-by-length formula. The earlier Cantor-like word paper considered permutation and ordinary factor complexity for the same family of substitutions. Schaeffer and Shallit developed automatic-logic methods for many classical infinite words, without an explicit generalized Cantor formula here. Allouche, Baake, Cassaigne and Damanik surveyed palindromic complexity and proved results for primitive constant-length class-\(P\) substitutions; the substitution here is nonprimitive. General methods for other invariants and sequences do not imply the claim by matching terminology alone.

## Limitations

This is a mathematical proof with finite computational diagnostics, not an independent proof-assistant certification. Novelty was evaluated against accessible primary work and mathematical records; an unindexed or inaccessible equivalent statement remains possible. No asymptotic claim about the full factor complexity or prefix-palindromic length is made. The base \(b=2\) and finite-prefix boundary-specific maximality are outside the theorem.

## References

- J. Chen, X. Lü and W. Wu, *On the \(k\)-Abelian Complexity of the Cantor Sequence*, first public 2017-03-12, https://arxiv.org/abs/1703.04063.
- *On the permutation complexity of the Cantor-like sequences*, *Theoretical Computer Science*, DOI https://doi.org/10.1016/j.tcs.2015.12.022.
- L. Schaeffer and J. Shallit, *Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences*, https://arxiv.org/abs/1508.02074.
- J.-P. Allouche, M. Baake, J. Cassaigne and D. Damanik, *Palindrome Complexity*, https://arxiv.org/abs/math/0106121.
