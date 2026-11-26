# Exact cyclic three-gram fibers and capacity for binary words avoiding adjacent ones

## Finding
For every integer \(n\ge 1\), let \(\mathcal N_n\) be the binary necklaces of circumference \(n\) with no cyclic occurrence of `11`; two necklaces are observationally equivalent if their *oriented* cyclic length-three factor multisets agree. If the necklace has \(r>0\) ones, let \(t\) be the number of gaps of at least two zeros between consecutive ones, and let \(R=n-2r-t\). Its entire three-gram profile is determined by \((n,r,t)\). The profile is feasible precisely when \(0\le t\le r\), with either \(t=0,n=2r\), or \(t\ge1,R\ge0\). For \(t\ge1\), its exact inverse-fiber size (number of necklaces) is
\[
F(n,r,t)=\frac1r\sum_{d\mid\gcd(r,t,R)}\varphi(d)
\binom{r/d}{t/d}\binom{R/d+t/d-1}{t/d-1}.
\]
The all-zero and alternating profiles have one source each. The number \(P_n\) of distinguishable three-gram profiles, equivalently the maximum noiseless codebook size with cyclic length-three multiset reads, has generating series
\[
\sum_{n\ge1}P_nz^n=\frac{z}{1-z}+\frac{z^2}{1-z^2}
+\frac{z^3}{(1-z)(1-z^2)(1-z^3)}.
\]
Exactly \(S_n\) profiles have a single necklace, with generating series
\[
\sum_{n\ge1}S_nz^n=\frac{z}{1-z}+\frac{z^2}{1-z^2}
+\frac{z^3}{(1-z)(1-z^2)}+\frac{z^6+z^7+z^8}{1-z^3}.
\]
In particular \(P_n=n^2/12+O(n)\), \(S_n=n/2+O(1)\), and the uniquely reconstructible fraction among distinguishable profiles is asymptotic to \(6/n\). All profiles at circumferences at most seven are singletons; ambiguity first occurs at eight.

## Assumptions and scope
A necklace is a binary cyclic word up to rotation but **not** reflection or symbol complementation. Cyclic avoidance of `11` includes the closing-to-opening boundary. The read observation includes *multiplicities* of all eight oriented triples, with indices interpreted modulo \(n\), even for \(n<3\). Reconstruction candidates are required to lie in the same cyclic `11`-free source family, not among arbitrary binary circles. The codebook is a set of necklaces with distinct observations; no noise is present. Euler's totient is \(\varphi\). For \(r=0\) only the all-zero necklace occurs; a circle with \(r>0\) can be represented uniquely up to rotation by its cyclic sequence of \(r\) positive zero-gap lengths.

## Proof
Write the zero gaps as \((a_1,\ldots,a_r)\), where each \(a_i\ge1\) and \(\sum_i a_i=n-r\). Let \(u\) count unit gaps and \(t=r-u\) count gaps of length at least two. A direct inspection of every cyclic triple gives the ordered profile, in the coordinate order `000,001,010,011,100,101,110,111`, as
\[
(n-3r+u,\ t,\ r,\ 0,\ t,\ u,\ 0,\ 0)
=(R,\ t,\ r,\ 0,\ t,\ r-t,\ 0,\ 0).
\]
Thus \(n,r,t\) are both necessary and sufficient to identify the profile. For \(t\ge1\) choose the positions of the \(t\) long gaps among \(r\) gaps. Set each long gap initially to two and each short gap to one; the remaining \(R=n-2r-t\) zeros are distributed among the \(t\) long gaps. Burnside's lemma for rotations of the gap sequence now applies. A rotation with repetitions \(d\) fixes a gap sequence precisely if \(d\mid r,t,R\); a primitive block of length \(r/d\) has \(t/d\) long positions and \(R/d\) extra zeros. There are \(\binom{r/d}{t/d}\binom{R/d+t/d-1}{t/d-1}\) possibilities. Exactly \(\varphi(d)\) rotations have repetition factor \(d\). Averaging over \(r\) rotations proves the fiber formula. If \(t=0\), all gaps are one, so \(n=2r\) and there is exactly one alternating necklace.

For each \(n\), profiles consist of one all-zero case, one alternating case when \(n\) is even, and the parameter pairs \(r\ge t\ge1\), \(n\ge2r+t\). Introduce a nonnegative slack \(R\); summing \(z^{2r+t+R}\) over \(r=t+j\), \(t\ge1\), \(j,R\ge0\) yields the asserted series for \(P_n\).

It remains to determine singletons. A positive-weight nonalternating profile has a singleton fiber if and only if one of these disjoint conditions holds: (i) \(t=1\); (ii) \(t\ge2,u=r-t=0,R=0\) or \(R=1\); (iii) \(t\ge2,u=1,R=0\). In (i) there is one long gap; in (ii) all gaps are equal except possibly one extra zero; in (iii) one unit gap fixes the unique cyclic placement. Conversely, with \(t\ge2\) and \(u\ge2\), the unit-gap/long-gap patterns with long gaps adjacent versus separated are distinct, regardless of excess-zero assignments. With \(t\ge2,u=1,R\ge1\), the unit gap fixes a reference point, and putting the extra zero in the first versus the second long gap gives distinct necklaces. With \(t\ge2,u=0,R\ge2\), allocating two excess zeros together versus to different long gaps likewise gives distinct necklaces. These cases exhaust all possibilities. Their series are respectively \(z^3/((1-z)(1-z^2))\), \((z^6+z^7)/(1-z^3)\), and \(z^8/(1-z^3)\). Adding the all-zero and alternating singletons gives \(S_n\).

The first two rational terms of the capacity series grow at most linearly in coefficient count, whereas the third has a triple pole with coefficient \(1/6\) in its local expansion at \(z=1\); hence \(P_n=n^2/12+O(n)\). The singleton series similarly yields \(S_n=n/2+O(1)\). The capacity statement follows because distinct observation profiles require separate representatives and selecting one representative from each profile is achievable. For \(n\le7\), the singleton classification covers every feasible parameter triple. At \(n=8,r=t=2,R=2\), zero gaps \((2,4)\) and \((3,3)\) exhibit distinct necklaces with identical profiles, proving first ambiguity.

## Verification
The included independent stdlib-only program `check.py` exhausts binary circles through circumference \(15\), quotients by rotation, independently measures all oriented triple multiplicities, and compares each entire observed inverse fiber with the Burnside expression. It also independently checks both profile and singleton generating-series coefficient formulas and the first ambiguity boundary. Run `python3 check.py` from the directory containing this document and the checker.

## Relationship to prior work
Karhumäki, Saarela and Zamboni introduced and investigated general \(k\)-Abelian equivalence, but their infinite-word complexity theorems do not enumerate inverse fibers of cyclic three-gram spectra in the no-adjacent-ones language. Bresler, Bresler and Tse study reconstruction from substring reads and de Bruijn graph assembly, not this explicit constrained necklace fiber/capacity classification. Previously indexed work enumerates unrestricted cyclic binary three-gram *profiles* or no-`11` cyclic **four**-gram fibers; neither statement gives these **three**-gram inverse-fiber counts by implication. Another analysis concerns cyclic three-gram fibers forbidding isolated ones (`010`), which is a different and non-containing source restriction. General enumerative methods such as Burnside's lemma are classical and not claimed as new; the proposed contribution is the complete inverse-spectrum and singleton classification for this exact constrained observation model.

## Limitations
All conclusions concern oriented circular reads with multiplicities and source-restricted reconstruction. Linear words, unknown source constraints, higher read lengths, and corrupted/noisy spectra are not covered. The nearest indexed reports were accessible only as titles and abstracts, so a prior equivalent specialization hidden in their complete documents cannot be excluded. Same-model proof and finite verification do not amount to independent audit.

## References
- J. Karhumäki, A. Saarela, L. Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, arXiv:1301.5104v1, posted 2013-01-22, https://arxiv.org/abs/1301.5104.
- G. Bresler, M. Bresler, D. Tse, *Optimal Assembly for High Throughput Shotgun Sequencing*, arXiv:1301.0068v1, posted 2013-01-01, https://arxiv.org/abs/1301.0068.
