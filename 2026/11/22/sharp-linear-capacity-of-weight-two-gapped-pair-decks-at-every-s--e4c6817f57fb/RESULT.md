# Sharp linear capacity of weight-two gapped pair decks at every spacing

## Finding
Let \(s\ge2\) and \(n\ge2\) be integers. In each binary word of length \(n\) and Hamming weight exactly two, observe the multiplicities of its letters and all ordered pairs of letters at position separation at least \(s\). Let \(D_s(n)\) denote the number of different observations, equivalently the largest zero-error codebook that can be decoded uniquely from this observation among words of that fixed composition.

**Theorem.** For every \(s\ge2\) and \(n\ge3s-1\),
\[
D_s(n)=\begin{cases}
5n-15,&s=2,\\
(2s+2)n-3s^2-2s-3,&s\ge3.
\end{cases}
\]
The stated linear regime starts sharply: at the preceding length \(n=3s-2\), the corresponding linear expression is **one smaller** than the true number \(D_s(3s-2)\). The proof counts observation profiles in layers specified by whether the marker separation is at least \(s\) and by the aggregate boundary excess. The exact separation need not be identifiable: for \(n=10\) and \(s=3\), zero-based placements \((2,7)\) and \((3,6)\) have different separations but the same counts \((G_{00},G_{01},G_{10},G_{11})=(19,4,4,1)\). In particular, for fixed \(s\), the distinct observable profiles grow only linearly in \(n\), whereas the number of source words is \(\binom n2\).

## Assumptions and scope
Positions are indexed \(0,1,\ldots,n-1\). Each source word has exactly two ones at distinct positions \(a<b\); other entries are zero. The *complete \(s\)-gapped two-deck* records each single letter and each ordered pair \(w_iw_j\) with \(j-i\ge s\), with multiplicity. There is no cyclic wraparound. The gap integer \(s\) is an arbitrary model parameter, not a bit value; \(s=2\) is the usual one-skipped-position deck. The equality of codebook capacity and observation count is exact: one may pick any single representative from each inverse observation fibre, and a decoder cannot distinguish two representatives of the same fibre.

## Proof
Write \(r=s-1\), \(H=n-2s+1\), and \(\ell=n-s\). Throughout the main proof suppose \(n\ge3s-1\), hence \(H\ge r+1\). Let \(e\) indicate that the two ones are at least \(s\) positions apart. If \(G_{xy}\) counts observed ordered pairs \(xy\), direct counting gives
\[
\begin{aligned}
G_{11}&=e=\mathbf1_{\{b-a\ge s\}},\\
G_{01}&=(a-r)_++(b-r)_+-e,\\
G_{10}&=(\ell-a)_++(\ell-b)_+-e,\\
G_{00}&=\binom{n-s+1}{2}-G_{01}-G_{10}-G_{11},
\end{aligned}
\]
where \((t)_+=\max\{t,0\}\). The length and two singleton counts are already fixed; hence the observation is determined by, and determines, \((e,G_{01},G_{10})\).

For an index \(i\), define the *boundary excess*
\[
\delta(i)=(r-i)_++(i-\ell)_+.
\]
Every index is either left of \(r\), in the central interval \([r,\ell]\), or right of \(\ell\). The identity
\[
(i-r)_++(\ell-i)_+=H+\delta(i)
\]
shows that the observation determines
\[
j:=\delta(a)+\delta(b)=G_{01}+G_{10}+2e-2H.
\]
Here \(j\) is an integer between zero and \(2r\), and \(G_{01}\) together with \((e,j)\) determines \(G_{10}\). Thus distinct profiles are counted by the number \(N_{e,j}\) of attainable \(G_{01}\)-values in each disjoint \((e,j)\) layer.

**Short pairs, \(e=0\).** First suppose \(s\ge3\), so \(r\ge2\). At \(j=0\) both ones lie in the central interval, separated by \(1,2,\ldots,r\); their central coordinates sum to every integer from \(1\) through \(2H-1\). The gaps one and two supply both parities, and the interval contains at least \(r+2\) indices. Hence \(N_{0,0}=2H-1\).

For \(1\le j\le r\), any short pair having positive excess is entirely on the left side or entirely on the right side (allowing one central index). On the left, putting the boundary index at \(r-j\) and the second at any allowed central index yields precisely the values \(0,1,\ldots,r-j\); two left-boundary indices only give the already counted value zero. Reflection exchanges \(G_{01}\) and \(G_{10}\); since their sum for \(e=0\) is \(2H+j\), it gives a disjoint interval of \(r-j+1\) values starting at \(2H-r+2j>r-j\), even when \(H=r\). Consequently \(N_{0,j}=2(r-j+1)\). At \(r+1\le j\le2r-1\), both indices must be noncentral on the same side; each side contributes exactly one value. At \(j=2r\) the same-side pair is impossible, since only one index on either side has individual excess \(r\). Therefore
\[
N_{0,j}=\begin{cases}
2H-1,&j=0,\\
2(r-j+1),&1\le j\le r,\\
2,&r+1\le j\le2r-1,\\
0,&j=2r.
\end{cases}\tag{1}
\]
For the exceptional spacing \(s=2\), the only short pairs are adjacent, so the central sums are odd and number exactly \(H\); the two boundary pairs give two other values. Thus \(N_{0,0}=H\), \(N_{0,1}=2\), and \(N_{0,2}=0\).

**Long pairs, \(e=1\).** For \(j=0\), both indices are central and must differ by at least \(r+1\). Their central coordinate sums produce exactly the integer interval
\[
G_{01}\in[r,\,2H-r-2],
\]
which has \(2H-2r-1\) values. To see completeness, write the central coordinates as \(x=a-r\) and \(y=b-r\). Then \(0\le x\le y-(r+1)\le H-r-1\), and \(G_{01}=r+x+[y-(r+1)]\). Any sum from \(0\) to \(2(H-r-1)\) is realized by taking its lower and upper integer halves as \(x\) and \(y-(r+1)\).

For \(1\le j\le r\), a left-boundary index of excess \(j\) paired with a central index gives the consecutive values \([r-j,H-1]\). Two opposite boundary indices with positive excesses summing to \(j\) fill exactly \([H,H+j-2]\) (empty when \(j=1\)). A central index followed by a right-boundary index of excess \(j\) gives \([H+j-1,2H+2j-r-2]\). These three integer intervals are consecutive and nonoverlapping. Their union has \(2H-2r-1+3j\) members.

For \(r+1\le j\le2r\), each index is outside the central interval and the pair must use opposite sides: two indices on the same side have separation strictly less than \(s\). If their individual excesses are \(p,q\in[1,r]\), then \(p+q=j\) and \(G_{01}=H+q-1\). All \(q=j-r,\ldots,r\) occur, giving \(2r-j+1\) values. Summarizing,
\[
N_{1,j}=\begin{cases}
2H-2r-1+3j,&0\le j\le r,\\
2r-j+1,&r+1\le j\le2r.
\end{cases}\tag{2}
\]
This holds also for \(s=2\).

**Summation.** Equation (2) gives \(\sum_{j=0}^{2r}N_{1,j}=(r+1)(2H-1)=2sn-4s^2+s\). For \(s\ge3\), (1) gives \(\sum_j N_{0,j}=2n+s^2-3s-3\), proving the second branch of the theorem. For \(s=2\), the short-pair sum is \(H+2=n-1\), and the long-pair sum is \(4n-14\), proving \(5n-15\).

**Sharp onset.** At \(n=3s-2\) one has \(H=r\), rather than \(H\ge r+1\). The same short-pair counts and all long-pair counts with \(j\ge1\) remain valid, by the same explicit index ranges. The only difference is the \((e,j)=(1,0)\) layer: no two central indices can be at least \(r+1\) apart, so its actual size is zero, whereas the linear continuation of (2) would assign the formal number \(-1\). The total is consequently exactly one greater than the linear expression. This establishes the claimed sharp threshold. \(\square\)

## Verification
The included standalone `verify.py` independently enumerates the literal binary pair observations and the closed coordinate formula, with direct pair-enumeration agreement for 15,385 source words. Across 836 parameter pairs with \(2\le s\le20\) and \(3s-2\le n\le6s+8\), it evaluates 1,879,860 weight-two words by the formula, counts *distinct actual tuple signatures*, and checks both the stated total and every \((e,j)\)-layer cardinality in the linear regime. The checker is executable with Python 3 standard library, prints `PASS` or raises an assertion, and is supplementary to the complete integer-interval proof above.

## Relationship to prior work
Golm, Nahvi, Gabrys and Milenkovic (2022, arXiv:2201.12671) introduced the \(s\)-gapped deck and obtained general confusability thresholds and constructions; their Section I–IV text distinguishes the full deck from exact-length-only reads. It does not state a fixed-weight-two all-spacing observation count. Rigo, Stipulanti and Whiteland (2023) characterize binary \((1,2)\)-gapped equivalence and investigate factor complexity of Thue–Morse and Sturmian sequences. Their Lemma 2.1 can characterize individual equivalences for one skipped position, but does not imply the displayed arbitrary-spacing two-parameter profile census without further enumeration.

Other indexed results include four-run fibre classifications at separation two, a total profile-growth theorem over unrestricted binary words at that separation, and a short-length full-alphabet census. They concern, respectively, up to four runs, all source weights without exact capacity, and bounded word lengths. Weight-two words can have five runs, and the present result treats every integer spacing and all lengths from the sharp linear threshold. Their reported statements do not supply the present linear law or its boundary correction. These are mathematical comparison claims only; no claim of universal novelty certification is made.

## Limitations
The formulas asserted here hold only in the sharp linear regime and at its immediate predecessor, not at every smaller \(n\). The alphabet is binary, the weight is exactly two, and only subsequences of lengths at most two are observed. The theorem counts profiles, not every fibre size or the optimal code under noise. The independent scientific audit is not performed. No literature search can rule out all unindexed equivalent statements or unpublished deductions.

## References
1. R. Golm, M. Nahvi, R. Gabrys, and O. Milenkovic, *The Gapped \(k\)-Deck Problem*, arXiv:2201.12671, first public 2022-01-29. https://arxiv.org/abs/2201.12671
2. M. Rigo, M. Stipulanti, and M. A. Whiteland, *Gapped Binomial Complexities in Sequences*, ISIT 2023, especially Section II and Lemma 2.1. https://orbi.uliege.be/bitstream/2268/302524/1/isit2023.pdf
3. *Divisor-valued ambiguity fibres of binary two-gapped decks at four runs*, published mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-divisor-valued-ambiguity-fibres-of-binary-two-gapped-decks-at-fo--fdba1299bc96
4. *Sharp quartic growth of binary one-gap pair-deck profiles*, published mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-quartic-growth-of-binary-one-gap-pair-deck-profiles--15ab34345405
5. *Exact short-length \(2\)-gapped pair-deck reconstruction across finite alphabets*, published mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-short-length-2-gapped-pair-deck-reconstruction-across-fini--80befdb8fc44
