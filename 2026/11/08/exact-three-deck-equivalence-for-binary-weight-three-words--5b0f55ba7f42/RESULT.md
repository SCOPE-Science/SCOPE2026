# Exact three-deck equivalence for binary weight-three words

## Finding
For every integer \(n\ge 3\), two distinct binary words of length \(n\) with precisely three ones have equal multiplicity-weighted length-three subsequence decks if and only if their four zero-gap vectors form the pair
\[
(x,z+3d,z,v+d)\quad\text{and}\quad(x+d,z,z+3d,v),
\]
where \(x,z,v\ge0\) and \(d\ge1\) are integers satisfying \(n=3+x+2z+v+4d\). Each equivalence class has one or two members, and each two-member class has exactly one such parametrization (up to ordering the two members). Consequently, if \(D_{3,3}(n)\) counts distinct length-three decks of binary length-\(n\), weight-three words, then
\[
\sum_{n\ge0}D_{3,3}(n)u^n=\frac{u^3}{(1-u)^4}-\frac{u^7}{(1-u)^2(1-u^2)(1-u^4)},
\]
where \(D_{3,3}(n)=0\) for \(n<3\). This establishes the generating-function assertion proposed as Conjecture 1 of Chrisnata et al.

## Assumptions and scope
A subsequence is selected by an increasing triple of indexed positions, with repeated resulting words counted with their multiplicities. The length-three deck records the numbers of occurrences of all eight patterns in \(\{0,1\}^3\). Words are indexed, with no identification under reversal, rotation, or bit complementation. The alphabet is binary and the word contains exactly three ones. Define the unique gap encoding
\[
 w=0^x1\,0^y1\,0^z1\,0^t,\qquad x,y,z,t\in\mathbb Z_{\ge0},\quad x+y+z+t=n-3.
\]

## Proof
Write \(N=x+y+z+t\) and let \(P_{abc}\) denote the subsequence count of the pattern \(abc\). Directly choosing the two one-positions and one zero-position gives
\[
 P_{011}=3x+y=:A,\qquad P_{110}=z+3t=:B,
 \qquad P_{101}=2(y+z).
\]
Equal decks for two weight-three words force identical \(N,A,B\). The integer solutions of this linear system lie along the primitive kernel vector \((1,-3,3,-1)\): if one gap vector is \((x,y,z,t)\), the other is necessarily
\[
 (x+s,y-3s,z+3s,t-s),\qquad s\in\mathbb Z,
\]
with nonnegative entries. The last assertion follows because the first coordinate difference is integral and uniquely determines the other three differences. In particular \(y+z\) stays fixed, so \(P_{101}\) stays fixed as well.

The count of \(001\) is
\[
 F(x,y,z,t)=\binom{x}{2}+\binom{x+y}{2}+\binom{x+y+z}{2}.
\]
Substituting the candidate vector, expanding the three quadratic polynomials, and canceling yields the exact identity
\[
 F(x+s,y-3s,z+3s,t-s)-F(x,y,z,t)=s(z-y+3s).
\]
Thus identical decks require \(s=0\) or \(s=(y-z)/3\). The first means the same word. For the second, a distinct partner exists precisely when \(y-z\) is a nonzero multiple of three and the four transformed entries are nonnegative.

Conversely, suppose the second value of \(s\) is integral and yields a nonnegative gap vector. Then \(N,A,B\) and \(P_{001}\) are unchanged. The complementary pattern satisfies
\[
 P_{100}=\binom{y+z+t}{2}+\binom{z+t}{2}+\binom{t}{2},
\]
whose change under the same transformation is also \(s(z-y+3s)=0\). The all-zero and all-one counts are respectively \(\binom N3\) and \(1\), both unchanged. Finally
\[
 P_{001}+P_{010}+P_{100}=3\binom N2,
\]
since the left side counts every selection of two zeros and one of the three ones exactly once. This fixes \(P_{010}\). Therefore all eight length-three pattern multiplicities agree. No other distinct partner is possible, proving that every deck class has size at most two.

For a unique orientation of a distinct pair, take the word with \(y>z\). Write \(y=z+3d\), with \(d\ge1\). The partner has terminal gap \(t-d\ge0\), so write \(t=v+d\); the remaining gaps \(x,z,v\) are nonnegative. These choices yield exactly the displayed pair, and its total number of zeros is \(x+2z+v+4d\). Conversely, every such quadruple produces a valid distinct deck-equivalent pair. The orientation and the gap encoding are unique.

The set of all weight-three length-\(n\) words has size \(\binom n3\), with ordinary generating function \(u^3/(1-u)^4\). Each two-member deck class reduces the number of distinct decks by exactly one. Their generating function is
\[
 \sum_{d\ge1}\sum_{x,z,v\ge0}u^{3+x+2z+v+4d}
 =\frac{u^7}{(1-u)^2(1-u^2)(1-u^4)}.
\]
Subtracting proves the asserted formula for all \(n\), including the zero-count boundary \(n<3\). \(\square\)

## Verification
The accompanying standalone Python program `verify_three_deck.py` enumerates all length-\(n\) weight-three words for \(3\le n\le30\). It obtains all subsequence counts of lengths one through three by dynamic programming independent of the gap formula, groups words by signature, checks that no class exceeds two members, checks the exact gap-partner involution, and compares every length's number of pairs and decks with the symbolic count. Executing `python3 verify_three_deck.py 30` yields `VERIFY_OK n=3..30 words=31465 pairs=2933`. In addition, direct symbolic expansion verifies the two key quadratic difference identities. The infinite result rests on the preceding algebraic argument, not on finite verification.

## Relationship to prior work
Chrisnata et al., *On the Number of Distinct k-Decks: Enumeration and Bounds*, explicitly pose this very rational generating function as their Conjecture 1 and record finite evidence. They identify the linear kernel direction but do not give the quadratic gap-rigidity and exhaustive collision-pair enumeration established here. Freydenberger et al., *Testing k-Binomial Equivalence*, develop the decision problem for k-binomial equivalence; Lejeune et al., *On the k-Binomial Equivalence of Words*, study the general equivalence relation, emphasizing different classifications. The result here proves the precisely stated weight-three, length-three deck conjecture; it is not a proof for arbitrary weights or deck lengths.

## Limitations
The proof is restricted to binary words with exactly three ones and decks of subsequences of length three. It neither determines all \(D_{k,s}(n)\) nor provides complexity results for general k-binomial equivalence. Earlier unindexed sources may contain equivalent results; no independent expert audit has been performed.

## References
- Chrisnata, Kiah, Karingula, Vardy, Yaakobi and Yao, *On the Number of Distinct k-Decks: Enumeration and Bounds*, Conjecture 1, DOI: https://doi.org/10.3934/amc.2021032; full text: https://yaakobi.net.technion.ac.il/files/2022/08/60_k_Decks_Disc_Math21.pdf.
- *Testing k-Binomial Equivalence*, arXiv:1509.00622, first version September 2, 2015, https://arxiv.org/abs/1509.00622.
- *On the k-Binomial Equivalence of Words*, arXiv:2001.11732, https://arxiv.org/abs/2001.11732.
- *Reconstruction of Words with Fixed Hamming Weight from Subsequence Decks*, arXiv:2610.41110, https://arxiv.org/abs/2610.41110 (different parameter regime).
