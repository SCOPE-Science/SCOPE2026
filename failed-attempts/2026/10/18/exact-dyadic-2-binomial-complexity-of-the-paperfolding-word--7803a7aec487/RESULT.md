# Exact dyadic 2-binomial complexity of the paperfolding word

## Finding

Let \(p=p_1p_2\cdots\) be the binary sequence with \(p_i=1\) when the odd part of \(i\) is congruent to \(1\pmod4\), and \(p_i=0\) otherwise. It is the bitwise complement of the standard ordinary paperfolding sequence. Write \(b_2(n)\) for the number of equivalence classes of length-\(n\) factors of \(p\) under equality of the counts of *all scattered subsequences* of length at most two. For every integer \(k\ge2\), with \(n=2^k\),

\[
b_2(n)=2n+k+1.
\]

More precisely, if \(c\) denotes the number of ones, the three and only three possible values are \(n/2-1,n/2,n/2+1\). Each outer value of \(c\) supports exactly \(n\) distinct 2-binomial signatures; the central value supports exactly \(k+1\). Within each outer layer, \(n/2\) signatures occur at even starting positions and \(n/2\) at odd starting positions, without overlap. Every central signature occurs at both starting parities. For the central layer the distinct positional sums of ones are precisely

\[
\left\{\frac{n(n-1-k)}4+j\frac n2:0\le j\le k\right\}.
\]

For comparison, the paperfolding word has ordinary factor complexity \(4n\) at all \(n\ge7\); thus along powers of two its 2-binomial complexity is asymptotically half the ordinary factor complexity, even though its abelian complexity at these lengths is only three.

## Assumptions and scope

The index \(i\) begins at one. The *odd part* of a positive integer is the result of dividing it by its largest power of two. A factor of length \(n\) beginning at \(s\ge1\) is \(p_sp_{s+1}\cdots p_{s+n-1}\). Equal factors are automatically assigned equal signatures, so counting distinct signatures among all starts is equivalent to counting the 2-binomial factor-complexity classes. This result concerns the one-sided infinite ordinary paperfolding sequence and powers-of-two factor lengths; it does not concern prefixes alone, contiguous pair counts, or higher binomial levels.

For a binary word \(w=w_0\cdots w_{n-1}\), define \(c(w)=\sum_{j=0}^{n-1}w_j\) and \(\omega(w)=\sum_{j=0}^{n-1}j w_j\). The number of scattered \(01\) subsequences is \(\omega(w)-\binom{c(w)}2\). The remaining pair counts are \(\binom{n-c(w)}2\), \(\binom{c(w)}2\), and \(c(w)(n-c(w))-[01](w)\), for \(00\), \(11\), and \(10\), respectively. Thus two equal-length binary words are 2-binomially equivalent if and only if their ordered pairs \((c,\omega)\) agree. Bit complementation preserves the number of equivalence classes, though it changes the numerical positional sums.

## Proof

**1. Dyadic interleaving.** The sequence obeys \(p_{2i}=p_i\), \(p_{4i+1}=1\), and \(p_{4i+3}=0\) for nonnegative indices wherever positive. Let \(m=2^{k-1}\), let \((c,\omega)\) be the signature of a length-\(m\) factor beginning at \(t\), and let \(b\in\{0,1\}\) be the parity of \(t\). Interleaving the original symbols at even indices with the alternating symbols at odd indices gives the following *exact* transformations into length-\(2m\) factors:

\[
E_b(c,\omega)=\left(c+\frac m2,\;2\omega+\frac{m(m-1)}2+bm\right)
\]

for the factor beginning at \(2t\), and

\[
O_b(c,\omega)=\left(c+\frac m2,\;2\omega+c+
\begin{cases}m^2/2,&b=0,\\m(m-2)/2,&b=1\end{cases}\right)
\]

for the factor beginning at \(2t-1\). Both maps are onto the respective possible sets because every positive starting position is of one of these forms with \(t\ge1\). To verify the positional constants, in the even-start case the inserted ones occupy odd local positions \(1,5,\dots\) when \(t\) is even and \(3,7,\dots\) when \(t\) is odd. In the odd-start case they occupy local even positions, while the inherited ones at odd positions contribute \(2\omega+c\).

**2. Base case.** At length two, both starting-position parities realize the signatures \(\{(0,0),(1,0),(1,1),(2,1)\}\); all four binary length-two words occur at both parities. Applying the maps with \(m=2\) gives, at length four:

\[
\begin{array}{c|cc}
 c &\text{even-start values of }\omega&\text{odd-start values of }\omega\\\hline
1&\{1,3\}&\{0,2\}\\
2&\{1,3,5\}&\{1,3,5\}\\
3&\{3,5\}&\{4,6\}.
\end{array}
\]

This verifies the theorem for \(k=2\), including the parity distinctions.

**3. Outer layers.** Suppose the complete statement, including starting parities and the stated central progression, holds at length \(m=2^{k-1}\), with \(k\ge3\). In either outer layer at length \(m\), the count \(c=m/2\pm1\) is odd; each starting parity contributes exactly \(m/2\) signatures and their \(\omega\) values have opposite parities (the claim is explicit at \(m=4\)). The transforms \(E_b\) preserve distinctness for each fixed \(b\) and give all even \(\omega\) at the new length, whereas \(O_b\) give all odd \(\omega\), because their extra term \(c\) is odd. For any one transform type, the images from \(b=0\) and \(b=1\) are distinct modulo four: \(m\) is divisible by four, the two lower-start parity classes have opposite \(\omega\)-parities, and the fixed additive constants agree modulo four between \(b=0\) and \(b=1\) for each transform type. Consequently each new start parity contributes \(m\) outer signatures, and the two new start-parity sets are disjoint. The new outer layer therefore has \(2m=n\) signatures. Its parity property persists.

**4. Central layer.** The central predecessor count is \(c=m/2\), and by induction each predecessor start parity realizes the identical progression

\[
\omega_j=\frac{m(m-k)}4+j\frac m2,\qquad 0\le j\le k-1.
\]

Under \(E_0\) these become \(\frac{n(n-1-k)}4+jm\) and under \(E_1\) the same progression translated by \(m\). Their union is one progression with indices \(0\le j\le k\), step \(m=n/2\). Similarly, \(O_1\) supplies the unshifted progression and \(O_0\) its translate by \(m\). Hence each new starting parity has exactly the same \(k+1\) central signatures, and their union remains \(k+1\).

**5. Exhaustion and count.** Every length-\(n\) starting position is covered by the two interleavings, and no other counts of ones occur: the predecessor counts are \(m/2-1,m/2,m/2+1\), shifted by \(m/2\). The three count layers are disjoint. Summing their signature numbers gives \(n+(k+1)+n=2n+k+1\). The induction proves all assertions simultaneously for every integer \(k\ge2\). The claimed complexity comparison follows from the established ordinary factor-complexity formula and the three abelian layers above.

## Verification

The bundled standalone Python program `check.py` implements the exact interleaving recurrences with integer sets and, independently, directly scans factors from a length-\(131072\) prefix generated by odd-part arithmetic. It compares the *entire conditional signature sets*, not just their sizes, for lengths \(2,4,8,\ldots,512\). The recurrence is additionally checked through length \(2048\), including each layer cardinality, the central progression, and all starting-parity disjointness statements. Its terminal success marker is `PAPERFOLDING_DYADIC_2_BINOMIAL_ALL_CHECKS_PASSED`. Finite checks corroborate but do not replace the induction proof.

## Relationship to prior work

Rigo, Stipulanti, and Whiteland (2022) provide the precise binomial-complexity framework and structural results for other infinite words, including bounded-complexity morphisms and Thue–Morse-related families; the inspected full text does not give the present paperfolding dyadic formula. Lü, Chen, Wen, and Wu (2021) compute 2-binomial complexity for generalized Thue–Morse words, not paperfolding words. Madill and Rampersad (2012) establish 2-regularity of the *abelian* complexity of the ordinary paperfolding word; this is the level-one quotient and does not determine the level-two signatures. In particular, an ordinary factor-complexity formula cannot imply a precise number of 2-binomial classes without further analysis. The present dyadic classification is a distinct exact refinement. These comparisons are based on the relevant inspected full texts and specific mathematical implications; searches cannot prove absolute novelty.

## Limitations

No formula is claimed for lengths that are not powers of two, for scattered subsequences of length at least three, or for general paperfolding instruction sequences. The arithmetic central progression is stated for the explicitly defined complemented orientation; the total complexity and tier counts are unchanged by complement. An equivalent characterization outside indexed and inspected literature remains a risk. The result has received no independent external mathematical audit.

## References

1. M. Rigo, M. Stipulanti, M. A. Whiteland, *Characterizations of families of morphisms and words via binomial complexities*, 2022, arXiv:2201.04603v1, https://arxiv.org/abs/2201.04603 (first public 2022-01-12; MSC 68R15).
2. X.-T. Lü, J. Chen, Z. Wen, W. Wu, *On the 2-binomial complexity of the generalized Thue-Morse words*, 2021, arXiv:2112.05347v1, https://arxiv.org/abs/2112.05347 (first public 2021-12-10).
3. B. Madill, N. Rampersad, *The abelian complexity of the paperfolding word*, 2012, arXiv:1208.2856, https://arxiv.org/abs/1208.2856.
