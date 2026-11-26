# Exact Lie complexity of the period-doubling word

## Finding

Let \(p=0100010101000100\cdots\) be the right-infinite fixed point starting with \(0\) of the binary length-two morphism \(\mu(0)=01\), \(\mu(1)=00\). For a positive integer \(n\), let \(L_p(n)\) be the number of cyclic-rotation classes \([w]_{\rm cyc}\) of length-\(n\) binary words such that **every** cyclic rotation of \(w\) occurs as a contiguous factor of \(p\). Then

\[
L_p(n)=\begin{cases}
2,&n=2^a\text{ or }n=3\cdot2^a\text{ for some integer }a\ge0,\\
0,&\text{otherwise},
\end{cases}\qquad(n\ge1).
\]

In particular, \(L_p(2m)=L_p(m)\) for every positive integer \(m\), \(L_p(1)=L_p(3)=2\), and \(L_p(n)=0\) for odd \(n\ge5\). The accepted positive lengths have binary representations consisting of `1` followed by \(a\) zeros, or `11` followed by \(a\) zeros, for some integer \(a\ge0\). Their ordinary generating function is the lacunary formal series

\[
\sum_{n\ge1}L_p(n)z^n=2\sum_{a\ge0}\bigl(z^{2^a}+z^{3\cdot2^a}\bigr).
\]

The exact number of positive accepted lengths at most \(N\ge1\) is
\[
\lfloor\log_2 N\rfloor+1+\max\bigl(0,\lfloor\log_2(N/3)\rfloor+1\bigr).
\]

## Assumptions and scope

All indices of \(p\) are zero-based; a factor is a contiguous finite subword starting at a nonnegative index, not a scattered subsequence. A cyclic-rotation class identifies rotations, but not arbitrary permutations or reversals. Every member of a counted class must occur in \(p\); the weaker condition that *some* member occurs defines a different invariant, cyclic complexity. The domain of the theorem is every positive integer \(n\). Under the usual empty-word convention \(L_p(0)=1\), not included in the displayed series.

Write \(\rho_j(w)\) for the left cyclic rotation of a length-\(n\) word by \(j\) positions, with \(0\le j<n\). The class \([w]_{\rm cyc}\) is counted precisely when \(\rho_j(w)\) is a factor of \(p\) for every such \(j\).

## Proof

**(1) Alternating alignment and zero-run bound.** Since \(p=\mu(p)\), the morphism implies, for all \(i\ge0\),
\[
p_{2i}=0,\qquad p_{2i+1}=1-p_i.
\]
Thus every \(1\) in \(p\) lies at an odd index, and in particular \(11\) is not a factor. Moreover, a hypothetical occurrence of \(0000\), starting at either parity, would force both \(p_i=p_{i+1}=1\) for an appropriate \(i\), contradicting absence of \(11\). Hence \(0000\) is not a factor, and every length-\(n\) factor for \(n\ge4\) contains at least one \(1\).

**(2) Odd lengths.** Every factor of \(p\) has all occurrences of \(1\) in positions of a single parity relative to the start of that factor. Suppose a circular word \(w\) of odd length \(n\) has at least two occurrences of \(1\) and every rotation occurs in \(p\). Choose any two of its \(1\)-positions, whose forward circular distance is \(d\), with \(0<d<n\). Orienting the circular word first with one and then with the other position at its beginning makes these two \(1\)'s appear at linear distances \(d\) and \(n-d\), respectively. Both would have to be even, contradicting odd \(n\). Thus any counted class at odd length has at most one \(1\). For odd \(n\ge5\), either it is all zeroes or a rotation begins with at least \(n-1\ge4\) consecutive zeroes. Both alternatives would require the forbidden factor \(0000\). Hence \(L_p(n)=0\) for odd \(n\ge5\).

**(3) Doubling bijection.** Fix \(m\ge2\). We show that the map
\[
[w]_{\rm cyc}\longmapsto[\mu(w)]_{\rm cyc}
\]
is a bijection between counted length-\(m\) classes and counted length-\(2m\) classes.

If \([w]_{\rm cyc}\) is counted, every even rotation \(\rho_{2j}(\mu(w))=\mu(\rho_j(w))\) occurs in \(p\), aligned at an even position because \(p=\mu(p)\). Every such occurrence has the following symbol \(0\), since the first symbol of every morphism block is \(0\). Therefore the one-position left rotation of each aligned occurrence also occurs, giving every odd rotation of \(\mu(w)\). Hence its class is counted.

Conversely, let \([u]_{\rm cyc}\) be a counted class of length \(2m\ge4\). By step (1), \(u\) contains at least one \(1\). Since every rotation occurs in \(p\), all \(1\)-positions on the circle must have the same parity: in each individual rotation the relative \(1\)-positions have one parity, and for even circular length both directions between two \(1\)'s have the same parity. Rotate \(u\) so that its \(1\)'s occur only in odd positions. All even positions are then zero, so it is uniquely \(\mu(w)\) for some binary word \(w\) of length \(m\). Since \(\mu(w)\) contains a \(1\) in a relative odd position, any occurrence in \(p\) starts at an even absolute position. Reading aligned morphism blocks shows that \(w\) is a factor of \(p\). The same reasoning applied to every even rotation \(\mu(\rho_j(w))\) shows that every \(\rho_j(w)\) occurs: \([w]_{\rm cyc}\) is counted.

Finally, for \(m\ge2\), no factor \(w\) of length \(m\) consists entirely of \(1\)'s, since \(11\) is absent. Consequently \(\mu(w)\) contains at least one \(1\). A cyclic shift by an odd number cannot carry \(\mu(w)\) to another word of the form \(\mu(v)\) containing a \(1\), since it would move all its \(1\)'s from odd to even relative positions. An even shift of \(\mu(w)\) corresponds exactly to a shift of \(w\). The map is thus injective on counted classes as well as surjective. This proves \(L_p(2m)=L_p(m)\) for \(m\ge2\).

**(4) Base cases and conclusion.** At length one, both \(0\) and \(1\) occur, so \(L_p(1)=2\). At length two, the factors are \(00,01,10\), giving the two accepted classes \([00]_{\rm cyc}\) and \([01]_{\rm cyc}\); thus \(L_p(2)=2=L_p(1)\). At length three, exactly the classes \([000]_{\rm cyc}\) and \([001]_{\rm cyc}\) are counted: \(000,001,010,100\) all occur, while any other necklace contains \(11\). Hence \(L_p(3)=2\). Remove all factors of two from any positive \(n\) using the doubling recurrence. The remaining odd number is either \(1\), \(3\), or at least \(5\); steps (2) and (4) yield precisely the displayed formula. Its binary-language, generating-function, and support-count corollaries follow immediately from the disjoint sets of positive lengths \(\{2^a:a\ge0\}\) and \(\{3\cdot2^a:a\ge0\}\). \(\square\)

## Verification

The standalone file `verify.py` implements a direct substitution prefix and an independent arithmetic description using parity of the two-adic valuation of \(i+1\). It compares their first \(2^{17}\) symbols, computes every conjugacy class from independently enumerated length-\(n\) factor sets for \(1\le n\le120\), checks class-level desubstitution at all even lengths in that range, and checks all binary circular words for \(1\le n\le13\). Two independent prefix lengths are compared to detect finite truncation. The exact executable was run and returned `VERIFY_OK`. These are finite corroborations; the preceding proof handles arbitrarily long factors and does not depend on finite truncation.

Run with `python3 verify.py` from a directory containing the extracted file. No third-party Python packages are required.

## Relationship to prior work

Bell and Shallit [1] introduce Lie complexity, give an automaticity theorem, and compute it for the Thue–Morse, ternary variant, Cantor, Fibonacci, and Tribonacci words; the period-doubling example is not among the formulas in their Section 7. Cassaigne, Fici, Sciortino and Zamboni [2] prove that the *cyclic complexity* of the period-doubling word equals \(2\) at powers of two (Proposition 17 and Example 1). That weaker invariant counts a class when at least one rotation occurs, and thus does not imply the exact all-rotation class counts, especially their vanishing at every other length. Li [3] proves general structural bounds and automaticity for extensions of Lie complexity, and De Luca and Fici [4] compute Lie complexity for Sturmian words, not this non-Sturmian fixed point. The exact period-doubling formula here is not covered by the inspected statements.

## Limitations

The theorem concerns the exact period-doubling morphism specified above; it is not a classification for arbitrary uniform morphisms or for cyclic complexity. It does not estimate frequency of occurrences or address other complexity invariants. The originality assessment is conditional on the inspected literature and database comparisons; an unindexed equivalent result remains possible. The finite verifier alone does not prove the infinite statement or establish novelty. No independent external mathematical audit has been performed.

## References

[1] J. P. Bell and J. Shallit, *Lie complexity of words*, arXiv:2102.03821, first public version February 7, 2021, https://arxiv.org/abs/2102.03821, especially Theorem 1.4 and Section 7.

[2] J. Cassaigne, G. Fici, M. Sciortino and L. Q. Zamboni, *Cyclic complexity of words*, arXiv:1402.5843, first public version February 24, 2014, https://arxiv.org/abs/1402.5843, especially Proposition 17 and Example 1.

[3] S. Li, *A note on the Lie complexity and beyond*, arXiv:2207.05859, first public version July 12, 2022, https://arxiv.org/abs/2207.05859, especially Sections 3–6.

[4] A. De Luca and G. Fici, *On the Lie complexity of Sturmian words*, arXiv:2206.00995, 2022 preprint, https://arxiv.org/abs/2206.00995, especially Sections 2–3.
