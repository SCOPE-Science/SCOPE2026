# A uniform rational enumerator for one-base-loop complementary stem avoidance

## Finding

Let \(\Sigma\) be any alphabet of even size \(q\ge2\), with a fixed-point-free involution \(a\mapsto\bar a\). Let \(a_q(n)\) count indexed linear words of length \(n\) containing **no** factor of the form \(ab c\bar b\bar a\), where \(a,b,c\) range independently over \(\Sigma\). Thus the forbidden factors consist of two complementary, reversed two-letter stems separated by precisely one arbitrary letter. The empty word is included.

Put
\[
D_q(z)=1-qz+z^2-z^3+(q-2)z^4+(q-1)z^5
\]
and
\[
N_q(z)=q^4-q^3z+q^2z^2-q^3(q-1)z^3-q^2(q^2-q+1)z^4.
\]
Then **for every even \(q\ge2\) and every \(n\ge0\)** the complete exact enumerator is
\[
\boxed{\sum_{n\ge0}a_q(n)z^n=1+qz+q^2z^2+q^3z^3+\frac{z^4N_q(z)}{D_q(z)}.}
\]
Equivalently, for every \(n\ge9\),
\[
a_q(n)=q a_q(n-1)-a_q(n-2)+a_q(n-3)
 -(q-2)a_q(n-4)-(q-1)a_q(n-5),
\]
with the starting values supplied exactly by the rational function. In particular,
\[
(a_4(0),\ldots,a_4(9))=(1,4,16,64,256,960,3600,13504,50656,190032).
\]
For the four-base DNA alphabet, the exponential growth constant is the Perron eigenvalue \(\lambda_4=3.75146484123868\ldots\), the largest positive root of
\[
\lambda^5-4\lambda^4+\lambda^3-\lambda^2+2\lambda+3=0.
\]
Accordingly the formal constraint capacity is \(\log_2\lambda_4=1.90745403735\ldots\) bits per base. This is a mathematical counting capacity, not a claim that a one-letter-loop stem is biochemically stable.

## Assumptions and scope

Words are oriented and indexed, not identified under rotation or reverse complementation. Every choice of the middle letter \(c\) is forbidden when the two length-two stems match by Watson–Crick reverse complement. Only **exactly one** intervening letter is considered. Longer separated stems, other loop sizes, global secondary structures, and substitution/deletion correction are not constrained. The involution has no fixed symbols and can otherwise be any pairing. Formal power series are over the integers after substituting even \(q\).

## Proof

**1. A finite universal complement-pattern system.** A word of length four can be canonicalized under symbol permutations commuting with the fixed-point-free complement: scan left to right; when a previously unseen complementary pair occurs, assign it the next pair number and designate its first encountered symbol as the even member; its complement is the odd member. This gives exactly \(49\) possible canonical four-letter states, distributed according to their number \(k\) of different complementary pairs as \((8,28,12,1)\) for \(k=1,2,3,4\).

For a canonical state \(w=(w_0,w_1,w_2,w_3)\) using \(k\) pairs, append either one of its \(2k\) already represented letters (multiplicity one) or the first member of a fresh pair (multiplicity \(q-2k\)). Omit an append \(x\) exactly when \(w_0=\bar x\) and \(w_1=\bar w_3\); this is precisely the condition that the new five-letter suffix has form \(ab c\bar b\bar a\). Canonicalize the resulting four-letter suffix. These steps define a fully explicit \(49\times49\) transition matrix \(T_q\) with entries in \(\mathbb Z[q]\), and work even when fewer than four complementary pairs exist because then the relevant fresh-pair multiplicity vanishes.

The number of actual length-four words represented by a state with \(k\) pairs is
\[
v_q(w)=\prod_{j=0}^{k-1}(q-2j).
\]
Writing \(\mathbf 1\) for the all-ones column, the combinatorial bijection between paths and admissible continuations proves
\[
a_q(4+t)=v_q T_q^t\mathbf 1\qquad(t\ge0).
\]
No approximation or asymptotic argument enters this identity.

**2. Finite symbolic annihilator.** Directly applying the transition rule to each of the \(49\) canonical states gives the identity in the free \(\mathbb Z[q]\)-module of length \(49\):
\[
\bigl[T_q^5-qT_q^4+T_q^3-T_q^2+(q-2)T_q+(q-1)I\bigr]\mathbf1=\mathbf0.
\]
This is a finite polynomial identity, not a numerical extrapolation from finitely many word lengths or alphabet sizes. `VERIFY.py` constructs the complete canonical-state list, constructs every transition polynomial from the preceding definition, and asserts **every coefficient** of all \(49\) components is zero with ordinary integer polynomial arithmetic. The same program checks the five initial polynomial identities
\[
\sum_{j=0}^{i}[z^j]D_q(z)\,a_q(4+i-j)=[z^i]N_q(z),\qquad 0\le i\le4.
\]

**3. Completion of the infinite enumerator.** Multiplying the annihilator by \(v_qT_q^t\) for every integer \(t\ge0\) proves the homogeneous fifth-order recurrence for the entire infinite tail. The initial polynomial identities fix its rational generating function to be \(N_q/D_q\) from length four onward. Adding the unconstrained lengths zero to three gives the displayed formula, with no further cases.

**4. The DNA rate.** For \(q=4\), the ordinary \(256\)-vertex graph on length-four suffixes has an edge for each admissible appended nucleotide. Directed reachability checks in both the graph and its transpose visit all \(256\) vertices, and the constant four-letter vertex has a self-loop. Hence the adjacency matrix is primitive. Perron–Frobenius gives a unique dominant positive eigenvalue contributing nontrivially to the positive count sequence. The rational recurrence and a root check identify it as \(3.75146484123868\ldots\), proving the stated exponential capacity.

## Verification

Execute `python3 VERIFY.py` using the packaged code. It relies only on the Python standard library. It verifies the \(49\)-state matrix polynomial identity and initial numerator equations **symbolically**, with exact integer coefficients, and independently compares the resulting enumeration with ordinary four-letter-suffix dynamic programs for \(q=2,4,6,8\). It also exhaustively tests literal words through lengths \(16,9,7,5\) respectively, and checks strong connectivity and aperiodicity of the DNA suffix graph. The literal tests are checks; the exact \(49\)-state polynomial identity and path bijection carry the all-alphabet/all-length proof.

## Relationship to prior work

Chu, Wang and Zhang (arXiv:2304.11403v1, first posted 22 April 2023) develop capacity analysis for DNA secondary-structure avoidance with two **arbitrarily separated**, non-overlapping reverse-complement substrings. That is a more restrictive *global* language, with rate \(1.1679\) bits/base for stem length two, and its results do not imply this exact one-letter-loop **local** count. Zhang and Wu (29 November 2023, DOI:10.1016/j.csbj.2023.11.035) introduce a loop-length-aware avoidance framework with stems growing with word length and loop separation at least four; their source definitions motivate distinguishing gap lengths, but they do not enumerate this fixed-gap length-five language.

An independently available calculation of *local reverse-complement duplication irreducibility* for length-two blocks excludes the **four-letter** factors \(ab\bar b\bar a\) and has a cubic rational denominator. Our excluded words are the distinct **five-letter** factors \(ab c\bar b\bar a\), with a fifth-order denominator. Neither prohibition implies the other: e.g., the length-five word \(a b c\bar b\bar a\) is always excluded here, but can avoid all four-letter reverse-complement palindromes, and a four-letter reverse-complement palindrome is allowed here because it has no length-five factor. No new statement about the previously published length-four system is claimed.

## Limitations

The result is a complete counting theorem for one sharply defined local forbidden-factor language, not a global DNA secondary-structure avoidance theorem, nor a claim of practical physical hairpin suppression. The shortest one-base loop is a mathematical baseline rather than the clinically or biochemically typical loop size. The symbolic finite-state proof has not been independently audited. The literature comparison is best knowledge: unindexed generalized-palindrome avoidance identities and implicit transfer-matrix formulations may coincide, so priority requires further independent historical checking.

## References

1. H. Chu, C. Wang, Y. Zhang, *Improved constructions of secondary structure avoidance codes for DNA sequences*, arXiv:2304.11403v1, 22 April 2023, https://arxiv.org/abs/2304.11403.
2. R. Zhang and H. Wu, *On secondary structure avoidance of codes for DNA storage*, Computational and Structural Biotechnology Journal, published online 29 November 2023, DOI:10.1016/j.csbj.2023.11.035, https://pmc.ncbi.nlm.nih.gov/articles/PMC10749251/.
3. *Rational enumeration and entropy of locally irreducible reverse-complement length-two words*, open result record, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-rational-enumeration-and-entropy-of-locally-irreducible-reverse--0f04deff31c7/RESULT.md (different local forbidden-factor family; consulted for mathematical overlap only).
