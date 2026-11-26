# First repetition law for triadic-length factors of the Cantor word

## Finding
Let \(C=C_0C_1C_2\cdots\) be the binary Cantor word fixed by the length-three morphism \(\mu(1)=101\) and \(\mu(0)=000\), starting with \(1\). Define \(\operatorname{inr}_C(n)\) as the number of pairwise distinct consecutive length-\(n\) factors starting at positions \(0,1,\ldots\) before the first repetition: equivalently, the smallest position \(j\ge1\) for which the length-\(n\) factor beginning at \(j\) equals a factor beginning at some \(i<j\).

**Theorem.** For every integer \(k\ge1\), put \(m=3^{k-1}\) and \(n=3m=3^k\). The factors beginning at the \(5m\) positions \(0,1,\ldots,5m-1\) are pairwise distinct, and the factor at position \(5m\) is equal to the one at position \(m\). In particular,
\[
\operatorname{inr}_C(3^k)=5\cdot 3^{k-1}\qquad(k\ge1).
\]
At length one, \(\operatorname{inr}_C(1)=2\). The statement concerns the initial prefix of this particular fixed point, not arbitrary shifts of the same factor language.

## Assumptions and scope
Indices start at zero; factors are contiguous, their lengths are positive, and repeated factors are compared as literal binary strings. Set \(B=\mu^{k-1}(1)\), so \(|B|=m\). The word \(B\) begins and ends with \(1\) and contains exactly \(2^{k-1}\) ones. These facts follow inductively from \(\mu(1)=101\) and \(\mu(0)=000\). Writing \(U=\mu^k(1)\), one has \(U=B0^mB\), of length \(3m\). Because \(C\) begins with \(101\), the first three length-\(n\) substituted blocks of \(C\) are \(U,0^n,U\). All comparisons below are thus settled inside that finite prefix.

## Proof
Write \(n=3m\), \(b=2^{k-1}\), and let \(F_i=C_i\cdots C_{i+n-1}\). For \(0\le i\le n\), the initial three-block decomposition gives
\[
F_i=U[i:n]0^i,
\]
where \(U[i:n]\) denotes the suffix of \(U\) beginning at offset \(i\). For \(0\le r\le2m\), it likewise gives
\[
F_{n+r}=0^{n-r}U[0:r].
\]
The second formula at \(r=0\) is the same single factor \(F_n\) as the first formula at \(i=n\).

**No repetitions within either side.** For \(0\le i<n\), since \(U\) ends in \(1\), the rightmost one of \(F_i\) is at internal offset \(n-1-i\). These offsets are distinct; \(F_n\) is all zeros. For \(1\le r\le2m\), since \(U\) begins in \(1\), the leftmost one of \(F_{n+r}\) is at internal offset \(n-r\). These offsets are distinct, and none of these factors is all zeros.

**No earlier cross-side repetition.** Take \(0\le i<n\) and \(1\le r<2m\). If \(i<m\), the suffix \(U[i:n]\) contains all \(b\) ones from the final copy of \(B\) and at least one one from the first copy. Thus \(F_i\) has at least \(b+1\) ones, whereas \(F_{n+r}\), whose only possible ones come from \(U[0:r]\subseteq B0^m\), has at most \(b\). So they differ.

If instead \(m\le i<n\), the rightmost one of \(F_i\) lies at offset \(n-1-i\le2m-1\). For \(1\le r\le m\), every one of \(F_{n+r}\) lies at an offset at least \(n-r\ge2m\). For \(m<r<2m\), the rightmost one of \(F_{n+r}\) is the final one from \(B\), at offset \(n-r+m-1=4m-r-1\ge2m\). Again \(F_i\ne F_{n+r}\). The all-zero factor \(F_n\) cannot equal a nonzero \(F_i\), and it is not repeated among \(F_{n+r}\) with \(r\ge1\). Hence every factor beginning before \(n+2m=5m\) is distinct.

**The first collision.** At \(i=m\),
\[
F_m=0^mB0^m.
\]
At \(r=2m\), the other formula gives
\[
F_{n+2m}=0^mU[0:2m]=0^mB0^m=F_m.
\]
Therefore the first repeated starting position is exactly \(5m\), and its earlier matching position is \(m\). Since \(C\) begins \(101\), the first repeated length-one factor starts at position \(2\), completing the separate base case.

## Verification
The standalone file `verify.py` generates \(\mu^{k+1}(1)\), independently checks every generated bit against the ternary-digit criterion (a bit equals one iff the base-three representation of its index uses only digits zero and two), and searches every factor starting from position zero until the predicted first collision. For each \(1\le k\le8\), it checks that no earlier factor repeats, that the first repetition is at \(5\cdot3^{k-1}\) with prior occurrence \(3^{k-1}\), and that the three-block decomposition used above holds. Run `python3 verify.py` using Python 3 without external packages. The finite checks corroborate the calculations; the proof establishes the universal quantifier over all integers \(k\ge1\).

## Relationship to prior work
Nicholson and Rampersad introduced and studied initial non-repetitive complexity for infinite words and explicitly report formulas for Thue–Morse, Fibonacci, and Tribonacci words (arXiv:1507.08206, first public version 29 July 2015). The 2016 article on the permutation complexity of Cantor-like sequences gives the ordinary factor complexity of the classical Cantor word as \(p_C(n)=2n-1\) for \(n\ge2\), not its first-repetition location. In particular, the theorem and that previously known factor complexity give the asymptotic ratio
\[
\frac{\operatorname{inr}_C(3^k)}{p_C(3^k)}=\frac{5\cdot3^{k-1}}{2\cdot3^k-1}\longrightarrow\frac56.
\]
Ordinary factor complexity alone cannot determine initial non-repetitive complexity, since the latter depends on the chosen origin. Available summaries of the Nicholson–Rampersad article do not state a Cantor-word evaluation, but its complete text could not be examined; see limitations.

## Limitations
The theorem only evaluates initial non-repetitive complexity at positive powers of three (plus the length-one base case). It does not claim a formula at every length, a non-initial/worst-shift version, or a general formula for other Cantor-like morphisms. The directly relevant Nicholson–Rampersad full text was not accessible for detailed theorem-by-theorem comparison; an unindexed or unexamined equivalent Cantor specialization remains an originality risk. No external independent audit has been performed.

## References
1. J. Nicholson and N. Rampersad, *Initial non-repetitive complexity of infinite words*, arXiv:1507.08206 (first publicly posted 2015-07-29); *Discrete Applied Mathematics* 208 (2016), 114–122. https://arxiv.org/abs/1507.08206 ; https://doi.org/10.1016/j.dam.2016.03.010.
2. J. Chen, X. Lü, and W. Wu, *On the permutation complexity of the Cantor-like sequences*, *Theoretical Computer Science* 616 (2016), 100–110, https://doi.org/10.1016/j.tcs.2015.12.022. Section 3 includes the factor-complexity formula for the classical Cantor word.
