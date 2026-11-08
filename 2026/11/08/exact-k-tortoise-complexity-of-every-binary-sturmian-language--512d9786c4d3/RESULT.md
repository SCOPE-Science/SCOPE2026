# Exact \(k\)-tortoise complexity of every binary Sturmian language

## Finding

Let \(0<\alpha<1\) be irrational, and let \(\mathcal L_\alpha(n)\) denote the set of distinct length-\(n\) factors of any binary Sturmian word of slope \(\alpha\), with \(1\) having frequency \(\alpha\). The *tortoise* map \(T\) removes the leftmost \(1\) of a finite binary word and appends it at the right; it fixes words without \(1\). Write
\[
\rho_{\alpha,k}(n)=\#\{T^k(w):w\in\mathcal L_\alpha(n)\}.
\]
For **every** pair of integers \(n,k\ge1\), put \(q=\lfloor k/\alpha\rfloor\). Then
\[
\boxed{\rho_{\alpha,k}(n)=2+\max\{0,n-1-q\}.}
\]
In particular, the exact longest initial interval on which \(k\)-tortoise equivalence agrees with Abelian equivalence is
\[
\boxed{\operatorname{abel}_{\alpha}(k)=\lfloor k/\alpha\rfloor+1.}
\]
The theorem also classifies all fibers: using the standard rotation parameter \(\beta\), two Sturmian factors have the same \(T^k\)-image if and only if their parameters lie in the same component after retaining the rotation-partition cuts indexed by \(0,n\), and by those \(j\in\{1,\ldots,n-1\}\) for which \(j>\lfloor k/\alpha\rfloor\). Each component is interpreted as a union of consecutive factor cells; factor endpoints follow their neighboring cell coding.

## Assumptions and scope

The alphabet is ordered \(0<1\). For any \(0\le\beta<1\), define the lower mechanical factor
\[
w_\beta(i)=\lfloor\beta+(i+1)\alpha\rfloor-\lfloor\beta+i\alpha\rfloor,\quad 0\le i<n.
\]
Irrationality of \(\alpha\) makes the intercept orbit dense, and all length-\(n\) factors of a Sturmian word of slope \(\alpha\) are precisely the distinct \(w_\beta(0)\cdots w_\beta(n-1)\). These are the standard \(n+1\) mechanical factors; neither the initial intercept nor an individual occurrence is part of the claimed count. Superscript \(T^k\) means exactly \(k\) iterations, not iteration to complete sorting. Every length \(n\) is positive, and \(k\) is a positive integer.

## Proof

**1. Rotation cells and their weights.** Set
\[
\beta_j=\{-j\alpha\}\quad(0\le j\le n),
\]
where braces mean fractional part, and \(\beta_0=0\). These \(n+1\) points are all distinct. Between consecutive points in their circular order, every digit of \(w_\beta\) is fixed. Different cells produce different factors (the standard Sturmian rotation partition). The total number of ones is
\[
\sum_{i=0}^{n-1}w_\beta(i)=\lfloor\beta+n\alpha\rfloor,
\]
since \(0\le\beta<1\). Thus the cuts \(\beta_0\) and \(\beta_n\) separate two arcs of different letter weights, \(\lfloor n\alpha\rfloor\) and \(\lceil n\alpha\rceil\). Tortoise iterations preserve weight, so cells in these different arcs cannot be equivalent.

**2. An interior cut is a single transposition.** For \(1\le j\le n-1\), crossing only \(\beta_j\) in the increasing-\(\beta\) direction increases \(\lfloor\beta+j\alpha\rfloor\) by one while leaving every other relevant integer part unchanged. Hence the two adjacent factors differ only at positions \(j-1,j\): their letters there are \(01\) and \(10\), respectively. Just before the crossing, the number of ones among positions strictly before \(j-1\) is
\[
\left\lfloor\beta_j+(j-1)\alpha\right\rfloor=\lceil j\alpha\rceil-1.
\]
Therefore the displaced \(1\) is the \(\lceil j\alpha\rceil\)-th one in either factor.

**3. Exactly the early cuts disappear.** On a binary word, \(T^k\) is precisely the operation of deleting its first \(\min(k,\#1)\) ones and appending that many ones. If \(j\le q=\lfloor k/\alpha\rfloor\), then \(\lceil j\alpha\rceil\le k\). At the cut \(\beta_j\), the transposed one is among those deleted, so the two adjacent factors have identical \(T^k\)-images. Consequently, every chain of factor cells in a single weight arc separated only by cuts with \(j\le q\) belongs to one equivalence class.

For the converse, take two distinct cells in the same weight arc whose intervening cuts include an index larger than \(q\). Let \(J\) be the **largest index** of any intervening interior cut. Then \(J>q\). At position \(J\), the two associated words differ: the contribution from the cut \(\beta_J\) changes this digit, while a second change at that digit would require crossing \(\beta_{J+1}\), which does not lie between the cells by maximality of \(J\). Each word has at least
\[
\lfloor J\alpha\rfloor\ge k
\]
ones in its first \(J\) positions, because \(J>\lfloor k/\alpha\rfloor\). Thus, in both words, all \(k\) removed ones lie strictly before position \(J\). The differing digit at position \(J\) survives at output position \(J-k\), proving that the two \(T^k\)-images differ. This also rules out any nonlocal collision of fibers across retained cuts.

**4. Counting and the exact threshold.** There are \(n+1\) original factor cells. Of the \(n-1\) interior cuts, exactly \(\min(q,n-1)\) are erased as equivalence-class separators; the two weight-separating boundary cuts remain. Hence
\[
\rho_{\alpha,k}(n)=(n+1)-\min(q,n-1)=2+\max(0,n-1-q).
\]
The Abelian factor complexity of every Sturmian word is \(2\) at each positive length. Our expression equals \(2\) exactly for \(n\le q+1\), and equals \(3\) at \(n=q+2\). This proves the stated exact abelianization threshold and completes the proof. \(\square\)

## Verification

The attached independent-factor-enumeration script `verify_tortoise_sturmian.py` constructs the full mechanical factor language from the \(n+1\) intercept cells, computes actual tortoise iterates, and checks the formula at 10 quadratic irrational slopes, for every \(1\le n\le70\) and \(1\le k\le16\). It passed **11,200** direct complexity comparisons. For lengths \(1\le n\le32\), the same factor languages were independently generated by long orbit prefixes; all **320** language comparisons matched, with **25,550** intercept cells checked in total. These finite tests are corroboration only; Step 3 establishes the infinite no-extra-collision assertion for all parameters.

To reproduce: run `python3 verify_tortoise_sturmian.py` in the directory containing the script. Python 3 standard library is sufficient. Calculations use 64-digit Decimal arithmetic for sampled quadratic irrational rotations; they are not interval-arithmetic certifications of all irrational slopes.

## Relationship to prior work

Defant and Kravitz introduced tortoise stack sorting for words [1]. Campbell and Rampersad introduced the \(k\)-tortoise factor complexity of infinite words and established formulas and bounds for paperfolding and Thue–Morse words [2, Sections 3–6]. Their Section 7 explicitly identifies Sturmian generalizations as a direction for investigation, without providing this all-slope, all-iterate formula. The familiar rotation interval description of light and heavy Sturmian factors is used in studies of Abelian periods [3] and supplies the geometric background, but does not itself count tortoise-equivalence classes. The result here uses the ranks of the transposed ones at individual rotation cuts and a rightmost surviving-digit argument to determine precisely which factor boundaries collapse.

## Limitations

The theorem applies to binary Sturmian **factor languages** with an irrational slope and the specified zero/one order, not arbitrary finite binary words, rational mechanical periodic words, nonbinary alphabets, or other partial-sorting maps. It does not provide the number of occurrences of individual factors or algorithms for arbitrary input texts. The mathematical proof is self-contained conditional only on the standard mechanical-word representation; finite checks do not establish its universal validity by themselves. Historical-priority searches and comparison with accessible primary sources cannot exclude unindexed equivalent formulations; independent mathematical audit has not been performed.

## References

[1] C. Defant and N. Kravitz, *Stack-sorting for Words*, arXiv:1809.09158, first public September 24, 2018. https://arxiv.org/abs/1809.09158

[2] J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811, first public April 28, 2026; v2 October 5, 2026. https://arxiv.org/html/2604.25811v2

[3] J. Peltomäki, *Abelian periods of factors of Sturmian words*, arXiv:1905.06138, first public May 15, 2019; Journal of Number Theory 214 (2020), 251–285. https://arxiv.org/abs/1905.06138
