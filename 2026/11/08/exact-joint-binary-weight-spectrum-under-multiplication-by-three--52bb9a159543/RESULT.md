# Exact joint binary-weight spectrum under multiplication by three

## Finding
For a nonnegative integer \(n\), write \(s_2(n)\) for its binary digit sum and put \(s_2(0)=0\). For every integer \(r\ge1\), set
\[S_r=\{(s_2(n),s_2(3n)):0\le n<2^r\}.\]
The complete support, including all endpoints, is
\[
S_r=\{(0,0)\}\ \cup\ \{(a,2a):1\le a\le\lfloor(r+1)/2\rfloor\}
\ \cup\ \left\{\left(\frac{b+t}{2},b\right):2\le b,t\le r,\ b\equiv t\pmod 2\right\}.
\]
The three displayed sets are disjoint, and their total cardinality is
\[\boxed{|S_r|=\binom r2+2}\qquad(r\ge1).\]
The theorem also gives the *shortest binary-length witness* for every achievable pair. Writing \(a=s_2(n)\), \(b=s_2(3n)\), and \(t=2a-b\), the shortest positive integer witness has bit length \(2a-1\) if \(t=0\), and \(\max(b,t)\) if \(t\ge2\). The corresponding binary strings are exhibited in the proof. Every pair is also attained by infinitely many integers (multiply a witness by arbitrary powers of two).

By Legendre's formula, \(\nu_2\binom{2n}{n}=s_2(n)\), so the same theorem is an exact joint valuation-support theorem for the two central binomial coefficients \(\binom{2n}{n}\) and \(\binom{6n}{3n}\).

## Assumptions and scope
All quantities are over ordinary nonnegative integers. A binary word has no leading zeros when measuring shortest positive bit length, although multiplying by a power of two preserves both digit sums. The range is *exactly* \(0\le n<2^r\), with \(r\ge1\); no limiting probability statement is assumed. The word \((10)^h\) means a concatenation of \(h\) copies of the two-bit block \(10\), while \(1^h\) and \((01)^h\) likewise mean repeated literal bits.

## Proof
**1. Carry identity and forbidden single carry.** Add \(n\) to \(2n\) in base two. Every carry decreases the total number of nonzero summand digits by exactly one. Therefore if \(a=s_2(n)\) and \(b=s_2(3n)\), the number \(t\) of carries is exactly
\[t=2a-b.\]
If \(n<2^r\), no carry occurs in the units column and all possible carry-producing columns are numbered \(1,\ldots,r\); hence \(0\le t\le r\). If the first carry occurs in column \(j\), the two contributing original digits in positions \(j\) and \(j-1\) must both be ones. The next column necessarily receives both the newly created carry and the shifted one from position \(j\), so it also produces a carry. Consequently \(t=1\) never occurs. For \(t=0\), no two ones in \(n\)'s binary expansion can be adjacent; conversely, nonadjacent ones cause no carry. Such a word with \(a\ge1\) ones requires at least \(2a-1\) bit positions, and \((10)^{a-1}1\) attains this lower bound. Its two digit sums are \((a,2a)\).

**2. The second coordinate is bounded when carries occur.** If \(n>0\), then \(3n\) is not a power of two, so \(b\ge2\). Suppose \(3n<3\cdot2^r\) has more than \(r\) ones. Its binary length is at most \(r+2\). If its leading one is at position at most \(r\), this forces \(3n=2^{r+1}-1\). If its leading one is at position \(r+1\), the smallest possible number with at least \(r+1\) ones is \(3\cdot2^r-1\): one must retain the leading bit and \(r\) of the \(r+1\) lower bits, minimizing by deleting the bit in position \(r\). But \(3n\le3\cdot2^r-3\), a contradiction. Hence \(b>r\) forces \(3n=2^{r+1}-1\). Divisibility by three then requires \(r+1\) even, and \(n=(2^{r+1}-1)/3\) has alternating binary ones, giving \(t=0\). Thus \(t\ge2\) implies \(2\le b\le r\), and together with the carry bound we obtain \(2\le b,t\le r\). The identity \(2a=b+t\) forces matching parity. These are all necessary restrictions.

**3. Sharp constructions when \(t\ge2\).** Fix arbitrary integers \(b,t\ge2\) of the same parity, and define \(a=(b+t)/2\). If \(t\ge b\), put \(h=(t-b)/2=a-b\) and let \(n\) have binary word \((10)^h1^b\), of length \(t\) and weight \(a\). Its exact value satisfies
\[3n=2^{b+2h+1}+2^b-3.\]
Because \(2^b-3\) has exactly \(b-1\) ones for every \(b\ge2\), these disjoint blocks show \(s_2(3n)=b\). If \(b\ge t\), put \(h=(b-t)/2=a-t\) and take the word \(1^t(01)^h\), of length \(b\) and weight \(a\). In this case
\[3n=(3\cdot2^t-3)2^{2h}+(2^{2h}-1).\]
The first parenthesized integer has digit sum \(t\) and the second has digit sum \(2h\), with no overlapping bit positions; hence \(s_2(3n)=t+2h=b\). In both cases the exhibited length \(\max(b,t)\) meets the two lower bounds from Steps 1–2, making the length optimal. Multiplication by powers of two gives arbitrarily large witnesses without changing their weight pair.

**4. Cardinality.** For \(t\ge2\), the map \((b,t)\mapsto((b+t)/2,b)\) is injective. Among the integers \(2,\ldots,r\), let \(E\) and \(O\) be the numbers of even and odd members. Exactly \(E^2+O^2\) ordered pairs \((b,t)\) have matching parity. The nonzero carry-free pairs contribute \(\lfloor(r+1)/2\rfloor\), and \(n=0\) contributes one. Thus
\[|S_r|=1+\lfloor(r+1)/2\rfloor+E^2+O^2.\]
For even \(r=2m\), \((E,O)=(m,m-1)\); for odd \(r=2m+1\), \((E,O)=(m,m)\). In either case this simplifies to \(\binom r2+2\), including \(r=1\).

**5. Central-binomial interpretation.** Legendre's identity \(\nu_2(n!)=n-s_2(n)\) implies \(\nu_2\binom{2n}{n}=s_2(n)\). Substituting \(3n\) for \(n\) gives the claimed simultaneous valuation interpretation. This completes the proof.

## Verification
Run `python3 verify.py` in a directory containing the standalone verifier. Its independent enumeration compares the complete support, for every level \(1\le r\le15\), with direct integer bit counts for all \(0\le n<2^r\). It also tests the explicit minimal-length constructors across many \((a,b)\) values, and checks the closed cardinality. The verifier uses integer arithmetic and does not assume the theorem to generate the enumerated actual supports. No finite test is being used as a proof for arbitrary \(r\).

## Relationship to prior work
Morgenbesser, Shallit, and Stoll (2010) study the binary digit sum on multiples, especially the parity of \(s_2(kn)\) and bounds for the least odd-parity witness. Their results do not state this two-coordinate support or shortest-witness profile. Clokie, Lidbetter, Molina Lovett, Shallit, and Witzman (2020) analyze the predicate \(s_2(3n)<s_2(n)\) and equality via automata, including asymptotic counts. Those predicates and their aggregate frequencies do not, alone, specify every attainable ordered weight pair or its optimal length. Kaneko and Stoll (2021 preprint, 2022 article) study products with prescribed small binary weights, yielding bounds in selected low-weight regimes rather than this uniform simultaneous image. OEIS A036555 and A180054 give, respectively, one-coordinate values \(s_2(3n)\) and the 3-flimsy inequality, not the full joint support. The numerical cardinality sequence coincides with the elementary sequence \(\binom r2+2\), but a coincidence of numbers is not an arithmetic classification.

## Limitations
This theorem classifies *support* and shortest bit lengths, not the multiplicity or asymptotic density of each weight pair, and says nothing about other odd multipliers. The all-level proof is self-contained. Priority comparisons were made against available source material; a historically unlocated equivalent statement remains possible. The full text of Kaneko–Stoll's related small-weight paper could not be retrieved in this investigation, so that comparison relies on its accessible scholarly abstract and explicitly remains a residual priority risk. Independent mathematical audit has not been performed.

## References
- J. F. Morgenbesser, J. Shallit, and T. Stoll, *Thue-Morse at Multiples of an Integer*, arXiv:1009.5357v1, first public September 27, 2010 (MSC 11N25, 11A63). https://arxiv.org/abs/1009.5357
- T. Clokie, T. F. Lidbetter, A. Molina Lovett, J. Shallit, and L. Witzman, *Computational Aspects of Sturdy and Flimsy Numbers*, arXiv:2002.02731v1, February 7, 2020. https://arxiv.org/abs/2002.02731
- H. Kaneko and T. Stoll, *Products of Integers with Few Nonzero Digits*, arXiv:2112.03077v1 (2021), *Uniform Distribution Theory* 17 (2022), 11–28. https://arxiv.org/abs/2112.03077
- OEIS A036555 and A180054, https://oeis.org/A036555 and https://oeis.org/A180054.
