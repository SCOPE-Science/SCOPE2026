# Exact cardinality spectra of equal-sum divisor partitions of \(3\cdot2^{m-1}\)

## Finding
For \(m\ge1\), put \(n_m=3\cdot2^{m-1}\). Let \(P_m(z)\) enumerate subsets of the positive divisors of \(n_m\) whose sum is half of the sum of all divisors, with each such subset carrying weight \(z^{|A|}\). Then
\[\sum_{m\ge1}P_m(z)t^m=\frac{t^2z(1+z^2)}{1-tz-t^2z(1+z^2)}.\]
In particular, if \(B_m\) is the number of **unordered** partitions into two classes of equal sum **and equal cardinality**, then \(B_m=[z^m]P_m(z)/2\). Explicitly, \(B_1=B_2=B_3=0\), and for every \(m\ge4\),
\[B_m=\frac12\sum_{r=0}^{\lfloor(m-4)/4\rfloor}\binom{m-3-2r}{2r+1}\binom{2r+2}{r+1}.\]
The first counts for \(m=1,\ldots,12\) are \(0,0,0,1,2,3,4,8,18,37,68,124\). The first qualifying integer is \(n_4=24\).

## Assumptions and scope
All statements hold for every integer \(m\ge1\). A partition is of the entire **set of distinct positive divisors**, not an integer partition with repeated parts. An oriented partition distinguishes the selected half, while an unordered partition identifies complementary halves. Both half-sums equal \(\sigma(n_m)/2\), and in a double Zumkeller partition both halves contain exactly \(m\) divisors among \(2m\) total divisors. No assumption of primality beyond the factor \(3\) is needed.

## Proof
The divisor set is precisely \(\{2^i,3\cdot2^i:0\le i<m\}\). Every selected half uniquely determines two binary integers \(u=\sum_i\alpha_i2^i\) and \(v=\sum_i\beta_i2^i\), with \(0\le u,v<2^m\), where \(\alpha_i,\beta_i\in\{0,1\}\). Put \(M=2^m-1\). Since the total divisor sum is \(4M\), the half-sum equation is
\[u+3v=2M,\qquad |A|=s_2(u)+s_2(v),\]
where \(s_2\) is binary Hamming weight.

To count solutions with their weights, add \(u+v+2v\) digit by digit in base two. At bit \(i\), the state is \( (b,c)\), where \(b\) is the previous digit of \(v\) and \(c\in\{0,1\}\) is the incoming carry. The states are ordered as \( (0,0),(0,1),(1,0),(1,1)\). The target \(2(2^m-1)\) has digit zero at index zero and digit one at indices \(1,\ldots,m\); its higher digits vanish. At the first index, the valid pairs of digits are \((0,0)\) and \((1,1)\), producing weighted initial vector
\[q(z)=(1,0,0,z^2).\]
At each of the following \(m-1\) ordinary digit positions with target digit one, direct enumeration of the four possible input-digit pairs gives the weighted transfer matrix
\[T(z)=\begin{pmatrix}z&0&z&0\\1&0&0&z^2\\1&0&0&z^2\\0&z&0&z\end{pmatrix}.\]
After both \(m\)-bit inputs end, the remaining target digit one is achieved without a further carry precisely in states \((0,1)\) and \((1,0)\), so the final column is \(e=(0,1,1,0)^{\mathsf T}\). Consequently
\[P_m(z)=q(z)T(z)^{m-1}e.\]
A finite matrix inversion (or direct multiplication) gives
\[\sum_{m\ge1}P_m(z)t^m=tq(z)(I-tT(z))^{-1}e=\frac{t^2z(1+z^2)}{1-tz-t^2z(1+z^2)}.\]
Thus \(P_1(z)=0\), \(P_2(z)=z+z^3\), and for \(m\ge3\),
\[P_m(z)=zP_{m-1}(z)+z(1+z^2)P_{m-2}(z).\]
Expansion by the number \(j\) of two-step terms yields, for \(m\ge2\),
\[P_m(z)=\sum_{0\le j\le\lfloor(m-2)/2\rfloor}\binom{m-2-j}{j}z^{m-1-j}(1+z^2)^{j+1}.\]
The \(z^m\)-coefficient requires \(2h=j+1\) in the expansion of \((1+z^2)^{j+1}\), hence \(j=2r+1\) and \(h=r+1\). This gives the stated binomial sum. Complementation exchanges selected sets of size \(m\) without fixed points; every unordered balanced partition is counted exactly twice. This completes the proof.

## Verification
Running `python3 checker.py` directly enumerates every possible pair \(u,v\) at \(m\le12\) and compares each full cardinality polynomial and its balanced coefficient with the transfer recurrence and closed binomial sum. The symbolic matrix calculation can be checked by multiplying \((I-tT)\) into the stated rational vector identity. The finite tests are confirmations; the matrix and coefficient arguments prove every \(m\).

## Relationship to prior work
Mahanta, Saikia and Yaqubi (2020) classify existence of equal-sum divisor partitions for two-prime-factor integers. Somu, Kukla and Tran (first public 2023-10-22) investigate additive properties of Zumkeller numbers. Existing exact count results for \(2^a p\) enumerate all unweighted Zumkeller partitions, whereas the present statement supplies a nontrivial *cardinality-weighted rational spectrum* and a closed formula for the strengthened equal-cardinality property. The named notion *double Zumkeller number* is already recorded in OEIS A347063, which includes the first example \(24\). The binomial formula counts its partitions rather than merely testing membership.

## Limitations
The result is restricted to the family \(3\cdot2^{m-1}\); it does not classify all double Zumkeller numbers. Stronger, as-yet-unindexed published enumerators could subsume this formula. A relevant published complete parametrization of unweighted partitions was discoverable by summary but its complete text was not accessible for comparison, so an implicit derivation there is an outstanding bibliographic risk. No independent mathematical audit has been performed.

## References
- P. J. Mahanta, M. P. Saikia, D. Yaqubi, *Some properties of Zumkeller numbers and k-layered numbers*, Journal of Number Theory **217** (2020), 218–236, DOI:10.1016/j.jnt.2020.05.003.
- S. T. Somu, A. Kukla, D. V. K. Tran, *Some Results on Zumkeller Numbers*, arXiv:2310.14149 (first public 2023-10-22), https://arxiv.org/abs/2310.14149.
- OEIS A347063, *Double Zumkeller numbers*, https://oeis.org/A347063.
- *Exact Zumkeller partition counts for the family \(2^a p\)*, published research record `2026/9/21/SCOPE-zumkeller-two-prime-partition-count--8a0ca297bd59`.
