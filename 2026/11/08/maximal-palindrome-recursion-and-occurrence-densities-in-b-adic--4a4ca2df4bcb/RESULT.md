# Maximal-palindrome recursion and occurrence densities in \(b\)-adic period-doubling words

## Finding

For every integer \(b\ge 2\), define the infinite binary word \(x_b=x_b(0)x_b(1)\cdots\) by
\[
x_b(n)=\nu_b(n+1)\bmod 2,\qquad n\ge0,
\]
where \(\nu_b(t)=\max\{j\ge0:b^j\mid t\}\). Divisibility by powers is meant literally, so the definition also covers composite bases. Equivalently, \(x_b\) is the fixed point beginning in \(0\) of
\[
0\longmapsto 0^{b-1}1,\qquad 1\longmapsto 0^b.
\]
A nonempty factor \(P\) is **maximal palindromic as a factor** if \(P=P^{\mathrm R}\) and neither \(0P0\) nor \(1P1\) is a factor of \(x_b\). This is language-level maximality, not maximality of a chosen occurrence.

Define a map on finite binary words by
\[
\mathcal F_b(c_1\cdots c_m)
=0^{b-1}\overline{c_1}0^{b-1}\overline{c_2}\cdots
0^{b-1}\overline{c_m}0^{b-1},
\]
where \(\overline{0}=1\) and \(\overline{1}=0\). Define \(M_{b,0}=0^{2b-2}\) and \(M_{b,k+1}=\mathcal F_b(M_{b,k})\) for every \(k\ge0\).

**Theorem.** For every integer \(b\ge2\), the full set of maximal palindromic factors of \(x_b\) is exactly
\[
\{M_{b,k}: k\ge0\}.
\]
Each such factor is unique at its length, and
\[
|M_{b,k}|=(2b-1)b^k-1.
\]
Its *complete zero-based starting-position set* is
\[
\operatorname{Occ}(M_{b,k})
=\big\{b^k(b^2v-b+\varepsilon):v\ge1,\ 
\nu_b(v)\equiv0\pmod2,\ \varepsilon\in\{0,1\}\big\}.
\]
In particular, the natural density of starting positions exists and equals
\[
\operatorname{dens}\operatorname{Occ}(M_{b,k})
=\frac{2}{b^{k+1}(b+1)}.
\]
The assertions hold simultaneously for all bases and all recursion levels; no finite cutoff is assumed.

## Assumptions and scope

All indices in \(x_b\) start at zero; in the proof, \(y_b(t)=x_b(t-1)=\nu_b(t)\bmod2\) is defined for positive integers \(t\). The letter \(1\) can occur only when \(b\mid t\). Every finite factor has occurrences arbitrarily far to the right: for any fixed positive index bound \(T\), choose \(K\) with \(b^K>T\). For \(1\le t\le T\) and every integer \(q\ge1\), the identity \(\nu_b(qb^K+t)=\nu_b(t)\) repeats the initial block \(y_b(1)\cdots y_b(T)\) arbitrarily far away. Thus any factor can be considered with letters available on both sides.

The theorem treats the precise **nonextendibility in the factor language**, a notion different from merely being a palindromic factor or being a maximal occurrence at a chosen center. Density refers to the limit of the number of permitted starts below \(N\), divided by \(N\), as \(N\) tends to infinity.

## Proof

**1. Sparse-block identity and zero runs.** For every integer \(u\ge1\),
\[
y_b(bu)=1-y_b(u),\qquad y_b(t)=0\quad(b\nmid t).
\]
In any two consecutive positive integers, at least one is not divisible by \(b\); hence at least one of the corresponding positions \(bu\) and \(b(u+1)\) carries a \(1\). Consequently a run of consecutive zeros cannot have length greater than \(2b-1\). A run of precisely this length occurs between \(b(u-1)\) and \(b(u+1)\) exactly when \(b\mid u\) and \(y_b(bu)=0\). Write \(u=bv\); this is equivalent to \(\nu_b(v)\) even. Such a run has middle coordinate \(b^2v\), and its positions are \(b^2v-b+1,\ldots,b^2v+b-1\). There is also a shorter initial zero run, which cannot contribute a length-\(2b-2\) occurrence.

The only maximal all-zero palindrome is \(M_{b,0}=0^{2b-2}\). Indeed, every shorter positive zero block extends as \(0P0\) inside a length-\(2b-1\) zero run; a block of length \(2b-1\) extends as \(1P1\) between two neighboring ones at distance \(2b\). Length \(2b-2\) cannot extend as \(0P0\), because there are no length-\(2b\) zero runs. Nor can it extend as \(1P1\), because the two ones would be separated by \(2b-1\), a number not divisible by \(b\). Its two starts in each maximal zero run yield exactly
\[
\operatorname{Occ}(M_{b,0})
=\{b^2v-b+\varepsilon: v\ge1,\ \nu_b(v)\equiv0\pmod2,\ \varepsilon\in\{0,1\}\}.
\]

**2. Reflection forces the base lattice.** Let \(P\) be a palindromic factor containing at least one \(1\), occurring in \(y_b\) at positive coordinates \([a,c]\). Its reflection axis is determined by the sum \(S=a+c\). Every \(1\) lies at a multiple of \(b\); a \(1\) at a noncentral position has its reflected \(1\) at another multiple of \(b\), and hence \(b\mid S\). If there is only a central \(1\), its coordinate is a multiple of \(b\) and once again \(b\mid S\). Therefore the reflection maps multiples of \(b\) onto multiples of \(b\), and nonmultiples onto nonmultiples.

If the outer coordinates \(a-1\) and \(c+1\) are not multiples of \(b\), both contain \(0\). Using a sufficiently far-right occurrence, \(P\) then extends as \(0P0\). Thus a maximal palindrome containing a \(1\) necessarily has both outer coordinates divisible by \(b\). Its occurrence interval has the form
\[
[a,c]=[bu-b+1,bv+b-1]
\]
for integers \(1\le u\le v\). Applying the sparse-block identity at the internal multiples \(bu,\ldots,bv\) shows that \(P=\mathcal F_b(Q)\), where \(Q=y_b(u)\cdots y_b(v)\). Reflection and \(b\mid S\) imply that \(Q\) is a palindrome.

**3. Maximality descends, and the construction ascends.** If \(Q\) from step 2 were extendible as \(dQd\), then the corresponding occurrence of \(\mathcal F_b(Q)\) would extend at the outer multiples of \(b\) as \(\overline d\mathcal F_b(Q)\overline d\). Hence any nonzero maximal palindromic factor descends to a strictly shorter maximal palindrome.

Conversely, suppose \(Q\) is a maximal palindrome with at least one zero. Then \(P=\mathcal F_b(Q)\) is a palindrome and occurs at every lifted occurrence of \(Q\); it contains at least one \(1\). Any occurrence of \(P\) has the same phase modulo \(b\), because its \(1\)-positions must occupy multiples of \(b\). Therefore any palindromic extension of \(P\) must use the two external multiples of \(b\), and would project to an extension of \(Q\), impossible. Thus \(P\) is maximal. The word \(M_{b,0}\) contains zeros, and every subsequent \(\mathcal F_b\)-image contains zeros because \(b\ge2\). Induction proves that all \(M_{b,k}\) are maximal. Descending a maximal palindrome strictly reduces length, and step 1 shows that the only terminal maximal palindrome is \(M_{b,0}\). This proves completeness and uniqueness. Since \(|\mathcal F_b(Q)|=b(|Q|+1)-1\), the length formula follows.

**4. Exact occurrence dilation.** If a word \(Q\) has a zero, the \(1\)-positions in \(\mathcal F_b(Q)\) force the phase modulo \(b\) of each occurrence. Consequently there is a bijection between occurrences of \(Q\) starting at zero-based position \(n\) and occurrences of \(\mathcal F_b(Q)\) starting at position \(bn\). (The correspondence is obtained by inserting \(b-1\) zeros before every complemented symbol and at the end.) Applying this bijection repeatedly to the two-start description in step 1 gives the claimed exact occurrence set.

**5. Natural density.** Among positive integers \(v\), those with even \(b\)-adic valuation have density
\[
\sum_{j\ge0}\frac{b-1}{b^{2j+1}}=\frac b{b+1}.
\]
There are two distinct starts per qualifying \(v\), scaled by a factor \(b^{k+2}\). The claimed density \(2/[b^{k+1}(b+1)]\) follows. In particular, the density proof is an infinite exact count, not an extrapolation from finite prefixes. \(\square\)

## Verification

Run the standalone script `verify_maximal_palindromes.py` with a standard Python 3 interpreter. The script constructs \(x_b\) directly by valuation parity and checks the symbolic recursion, predicted occurrence starts and factor-level maximality on finite prefixes for bases \(2\) through \(8\). It reports:

`VERIFY_OK bases=2..8 lengths_per_base=1..150 length_cases=1050 palindrome_window_tests=27910468 occurrence_checks=23293`

These exhaustive *finite-prefix window checks* are diagnostic; they do not establish the all-base or all-length theorem. The proof above supplies the unbounded arguments and the exact occurrence and density formulas. No external computational certificate is required.

## Relationship to prior work

Schaeffer and Shallit, *Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences* (2015), Theorem 3(d), identify the maximal-palindrome **lengths** \(3\cdot2^k-1\) in the ordinary binary period-doubling word. That is exactly the \(b=2\) length specialization of the present theorem, and is not claimed as new. Their theorem does not state the all-base recursive words, their exact occurrence sets or their densities. The new classification is about the valuation-parity word for every positional base \(b\), not about increasing the alphabet size.

Frid, Laborde and Peltomäki, *On prefix palindromic length of automatic words* (first publicly posted 2020-09-07), study minimum numbers of palindromes in prefixes and include the classical period-doubling word; prefix-factorization length is a different statistic from the complete language of nonextendible palindromes. Allouche, Baake, Cassaigne and Damanik, *Palindrome complexity* (2001), Theorem 9, provide a general class-P substitution mechanism for deriving palindrome-count recurrences; their lifting formula includes the operation of adjoining a common palindrome block. Thus the existence of a palindromic substitution lift is **not** a novel component here. Their theorem concerns counts of all palindromes, not the complete language-maximal list, exact starting positions, or asymptotic densities for every positional base. The present claim isolates these latter assertions and proves them directly.

Fici and Shallit, *Properties of a Class of Toeplitz Words* (first posted 2021-12-22), classify palindromes of Stewart words generated by ternary patterns; these sequences are not the present base-\(b\) valuation-parity family. Barro, Kaboré and Bognini, *On the palindromic zl-factorization and c-factorization of the generalized period-doubling sequences* (2022), use a two-uniform substitution with an alphabet of size \(q\) and analyze factorization properties. Their use of “generalized period-doubling” should not be confused with varying the positional base \(b\) of the present binary word.

## Limitations

The result concerns ordinary reversal palindromes and language-level symmetric nonextendibility only. It is not a statement about palindromic factorization lengths, arbitrary palindromic occurrences, pseudopalindromes or other automatic families. The ordinary base-two length specialization is known. Unindexed equivalent all-base results cannot be ruled out by bibliographic search alone. Independent examination of the new proof and literature comparison remains outstanding.

## References

1. A. E. Frid, E. Laborde, J. Peltomäki, *On prefix palindromic length of automatic words*, arXiv:2009.02934 (first posted 2020-09-07). https://arxiv.org/abs/2009.02934
2. L. Schaeffer, J. Shallit, *Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences*, arXiv:1508.02074 (2015), Theorem 3(d). https://arxiv.org/abs/1508.02074
3. G. Fici, J. Shallit, *Properties of a Class of Toeplitz Words*, arXiv:2112.12125 (first posted 2021-12-22), Section 6. https://arxiv.org/abs/2112.12125
4. M. Barro, I. Kaboré, K. E. Bognini, *On the palindromic zl-factorization and c-factorization of the generalized period-doubling sequences*, Australas. J. Combin. 83 (2022), 435–447, Sections 2–3. https://ajc.maths.uq.edu.au/pdf/83/ajc_v83_p435.pdf
5. J.-P. Allouche, M. Baake, J. Cassaigne, D. Damanik, *Palindrome complexity*, arXiv:math/0106121 (2001), Sections 4.2 and 6, Theorem 9. https://arxiv.org/abs/math/0106121
