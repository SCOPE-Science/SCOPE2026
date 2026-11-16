# Sharp eightfold primitive triple-sum collisions in the symmetric dyadic Fourier spectrum

## Finding

Let \(S=\{0\}\cup\{\pm2^j:j\in\mathbb Z_{\ge0}\}\). An *unordered primitive triple* for an integer \(D\) is a three-element multiset \(\{a,b,c\}\) from \(S\) with \(a+b+c=D\) and \(a+b\ne0\), \(a+c\ne0\), \(b+c\ne0\). Denote the number of these multisets by \(R(D)\). Repetition of a nonzero member is permitted; at most one zero can occur.

**Theorem.** For the full infinite symmetric dyadic frequency set,

\[
R(0)=\infty,\qquad 0\le R(D)\le8\quad(D\ne0),\qquad
R(D)=8\iff D=\pm3\cdot2^v\ (v\ge1).
\]

The value seven is never attained. In fact, the following formula determines every nonzero fiber. For \(D>0\), write uniquely \(D=2^v m\), with \(v\ge0\) and \(m\) positive odd. Put

\[
\delta(k)=\mathbf1_{\{k\ge2\text{ is a power of }2\}},\quad p(m)=\delta(m-1)+\delta(m+1),\quad T(0)=0,
\]

and, for every positive integer \(n\),

\[
T(n)=\mathbf1_{\{\operatorname{popcount}(n)=2\ \text{or }(n\ge2\text{ is a power of }2)\}}+
\mathbf1_{\{\operatorname{oddpart}(n)+1\text{ is a power of }2\}}.
\]

Here \(\operatorname{popcount}\) is the count of ones in the ordinary binary expansion and \(\operatorname{oddpart}(n)=n/2^{\nu_2(n)}\). Then

\[
\boxed{R(2^v m)=T\!\left(\frac{m-1}{2}\right)+T\!\left(\frac{m+1}{2}\right)+p(m)+\mathbf1_{m=3}
+\mathbf1_{v\ge1}\bigl(p(m)+\mathbf1_{m=1}\bigr)+\mathbf1_{v\ge2}\mathbf1_{m=1}.}
\]

By sign symmetry \(R(-D)=R(D)\). The eight primitive triples at \(D=6\) are

\[
\begin{gathered}
\{0,2,4\},\ \{0,-2,8\},\ \{1,1,4\},\ \{-1,-1,8\},\\
\{2,2,2\},\ \{2,-4,8\},\ \{-2,4,4\},\ \{-2,-8,16\}.
\end{gathered}
\]

Multiplication by \(2^{v-1}\) gives the eight triples for every positive maximizer \(D=3\cdot2^v\), \(v\ge1\), and negation gives the negative maximizers.

## Assumptions and scope

All three frequencies belong to the *infinite* set \(S\), not to an implicitly fixed truncation. Primitive means precisely that there is **no pair summing to zero**; this also excludes two zeros but allows \(\{a,a,b\}\) when \(a\ne0\). Each multiset is counted once, independent of the number of orderings. This is a theorem about supports of cubic Fourier convolutions: for a finitely supported polynomial \(P(t)=\sum_{n\in S} c_n e^{int}\), there are at most eight distinct noncancelling unordered monomial types in the coefficient of \(e^{iDt}\) in \(P(t)^3\) for \(D\ne0\). Their ordering multiplicities need not be equal, and arbitrarily many *cancelling* terms may also contribute.

## Proof

**Step 1: two-term count.** Consider \(\{u,w\}\subset\{\pm2^j:j\ge1\}\) with \(u+w=n>0\) and \(u+w\ne0\). There is at most one all-positive representation: either the binary expansion of \(n\) has exactly two ones, or \(n=2^k\) with \(k\ge2\), in which case the terms are equal. There is at most one mixed-sign representation. Writing it as \(n=2^a-2^b\) with \(a>b\ge1\), we have \(n=2^b(2^{a-b}-1)\), so its existence is equivalent to \(\operatorname{oddpart}(n)=2^j-1\) for some \(j\ge1\). Since \(b=\nu_2(n)\) and \(j=a-b\) are forced, it is unique. Dividing both terms by two converts this count to \(T(n/2)\) whenever \(n\) is even, as used below. Equivalently, \(T(k)\) directly counts unordered signed nonzero dyadic pairs of exponent at least zero whose sum is \(k\). Thus \(0\le T(k)\le2\) for \(k>0\), and \(T(0)=0\) under the noncancelling restriction.

**Step 2: valuation classes.** It is enough to take \(D>0\) by symmetry. Write \(D=2^v m\) with \(m\) odd. Let \(e\) be the minimum exponent among the nonzero elements of a primitive triple. If exactly one entry has exponent \(e\), its parity after dividing by \(2^e\) forces \(e=v\). If exactly two entries have exponent \(e\), they must have the same sign, since opposite signs are forbidden. The third entry must be of strictly greater exponent or zero. If it is zero or of exponent at least \(e+2\), the sum has valuation \(e+1\), so \(e=v-1\). If the third has exponent \(e+1\), its sign agrees with or opposes the two equal entries: the resulting sum is respectively \(\pm2^{e+2}\) or zero. Thus the nonzero case has \(e=v-2\) and \(m=1\). Finally, if all three nonzero entries have exponent \(e\), all their signs must agree, and their sum is \(\pm3\cdot2^e\), so \(e=v\) and \(m=3\). These mutually exclusive cases exhaust all primitive triples.

**Step 3: exact fibers.** For the class with exactly one minimum exponent \(e=v\), the low term has sign \(\pm\), and the other two terms have exponents at least \(v+1\) (or are zeros subject to primitiveness). The cases with *two nonzero* higher terms contribute \(T((m-1)/2)+T((m+1)/2)\) by Step 1, while the case with one zero contributes \(p(m)\), since the other term must be a power of two in units of \(2^v\), with exponent at least one. For all three minimum exponent terms, Step 2 contributes \(\mathbf1_{m=3}\). For two minimum terms at \(e=v-1\), the third entry is either zero (possible exactly for \(m=1\)) or a signed power of two of exponent at least \(v+1\); these contribute \(\mathbf1_{v\ge1}(\mathbf1_{m=1}+p(m))\). The final \(e=v-2\) class gives \(\mathbf1_{v\ge2}\mathbf1_{m=1}\). Combining yields the formula.

**Step 4: sharpness and the gap.** For odd \(m\ge5\), at most one of \(m-1,m+1\) is a power of two at least two: both can be powers of two only when \(m=3\). Consequently \(p(m)\le1\) and the exact formula bounds \(R(2^vm)\le2+2+2=6\). For \(m=1\), it gives \(R(1)=2\), \(R(2)=4\), and \(R(2^v)=5\) for \(v\ge2\). For \(m=3\), \(T(1)=1\), \(T(2)=2\), \(p(3)=2\); the formula gives \(R(3)=6\) and \(R(3\cdot2^v)=8\) for every \(v\ge1\). Hence eight is the sharp maximum for nonzero targets, and seven never occurs. The listed eight triples supply constructive equality.

**Step 5: zero target.** A primitive triple summing to zero has exactly two entries at its minimal exponent \(e\) and one entry at exponent \(e+1\) of the opposite sign; all other valuation patterns cannot sum to zero. Thus precisely the multisets \(\{2^e,2^e,-2^{e+1}\}\) and their negatives, for each \(e\ge0\), yield \(R(0)=\infty\).

## Verification

Run `python check_a.py` and `python check_b.py`, independently and without third-party packages. The first enumerates primitive unordered triples and checks the exact equality set and forbidden value seven for every target \(1\le |D|\le4096\); the second independently enumerates every positive target through \(8192\) and compares its count to the closed formula. The search uses the rigorous finite cutoff \(\max(|a|,|b|,|c|)\le4|D|\): the largest term \(P\) cannot have an equal-magnitude opposite term, and the other two can offset \(P\) most closely only through the two next largest powers; unless the sum is zero, the remaining magnitude is at least \(P/4\). Finite verification is a check, not the proof of the infinite assertion, which follows from Steps 1–5.

## Relationship to prior work

Ciccone and Gonçalves, arXiv:2208.09441 (first public 2022-08-19), introduce the \(\mathrm P(3)\) arithmetic sparsity property and establish a sharp Fourier extension theorem under that property. Their Section 2.1 explicitly identifies the small-ratio dyadic case as outside their sufficient hypotheses; they do not enumerate its primitive triple fibers. Gonçalves and Ferreira, arXiv:2510.20934 (2025), extend a Fourier inequality to lacunary ratios greater than three and explain additional mixed cancellations below that threshold, but not the exact dyadic fiber function. The published symmetric ternary-lacunary threefold collision theorem (full proof compared) has sharp maximum three with a distinct saturation set; its balanced-ternary argument does not imply the dyadic result because binary carries have a different valuation structure. Hajnal's signed-binary numeral theorem (2024) concerns distinct exponents with strictly alternating signs, not unordered three-term multisets allowing repeated powers and zero. The present assertion is an arithmetic classification, not a proof of a sharp Fourier extension inequality.

## Limitations

This result deliberately excludes opposite cancelling pairs, which create unbounded numbers of representations for many targets; no assertion is made about all cubic Fourier coefficients without this restriction or about Fourier extension constants. No phase- or coefficient-weighted cancellation is estimated. The exact multiplicity eight is arithmetic, independent of analytic Bessel-integral estimates. The possible existence of an equivalent unindexed signed-digit combinatorics classification remains a historical-priority risk; no independent expert audit has been performed.

## References

1. V. Ciccone and F. Gonçalves, *Sharp Fourier Extension on the Circle Under Arithmetic Constraints*, arXiv:2208.09441v1 (2022), https://arxiv.org/abs/2208.09441 .
2. F. Gonçalves and J. P. Ferreira, *On a Sharp Fourier Extension Inequality on the Circle with Lacunary Spectrum*, arXiv:2510.20934v1 (2025), https://arxiv.org/html/2510.20934v1 .
3. P. Hajnal, *Binary Numeration System with Alternating Signed Digits and Its Graph Theoretical Relationship*, *Algorithms* 17 (2024), 55, https://doi.org/10.3390/a17020055 .
4. *Sharp threefold collision law for symmetric ternary lacunary spectra*, public full-text theorem and proof, https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-sharp-threefold-collision-law-for-symmetric-ternary-lacunary-spe--66a6b286e118/RESULT.md .
