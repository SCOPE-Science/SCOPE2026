# Sharp fourth-order Walsh cancellation for sixteen-point noncrossing matchings

## Finding

Place sixteen labelled points \(0,1,\ldots,15\) in strictly convex position, in cyclic order. Let \(E\) consist of their 64 even-to-odd chords, and let \(\mathcal N_8\subset\mathbb F_2^E\) consist of the incidence vectors of the 1,430 noncrossing perfect matchings. For each chord support \(S\subseteq E\), define the unnormalized Walsh coefficient
\[
 W(S)=\sum_{M\in\mathcal N_8}(-1)^{|S\cap M|}.
\]

**Theorem.** No coefficient with \(1\le|S|\le3\) vanishes. Exactly 544 four-chord supports satisfy \(W(S)=0\). Under the full 32-element dihedral group of the labelled sixteen-gon these 544 supports comprise exactly 17 orbits, each of size 32. Exactly 256 supports are four-edge stars \(K_{1,4}\) (eight dihedral orbits); the other 288 are four-edge brooms, with nonzero graph degrees \((3,2,1,1,1)\) (nine dihedral orbits). No other four-chord graph shape occurs in the zero set.

More generally, for every even \(n=2k\ge4\), the analogous family \(\mathcal N_n\) on \(2n\) convex vertices has at least \(2n\,2^k\) distinct zero characters of weight \(k\), all stars. Hence its smallest possible Walsh-zero support weight is at most \(n/2\). Sharpness for arbitrary even \(n>8\) is **not** asserted.

In the sixteen-point case this is a sharp fourth-order parity-unbiasedness threshold: for a uniformly random noncrossing matching, every parity test on one, two, or three chord incidences is biased, while precisely 544 tests on four incidences are unbiased.

## Assumptions and scope

All vertices are distinct and strictly convex, and all chords are straight line segments. A matching is a set of eight pairwise nonincident, pairwise noncrossing chords covering all sixteen vertices. A chord in such a matching must join vertices of opposite parity; the 64 possible chords are exactly all such even-to-odd pairs. Fourier characters, supports, and the convolution group refer to this 64-coordinate Boolean cube, not the larger cube containing impossible same-parity chords. The transform is an integer count without probability normalization, so unbiasedness is equivalently \(W(S)=0\). For the general star statement, \(\mathcal N_n\) uses \(n^2\) even-to-odd chord coordinates on \(2n\) vertices.

## Proof

**1. Catalan structure and the unrestricted construction.** A chord \(\{v,v+2j+1\}\), with indices modulo \(2n\), divides the remaining vertices into arcs containing \(2j\) and \(2(n-1-j)\) vertices. There are therefore \(C_jC_{n-1-j}\) matchings containing it, where \(C_j=\binom{2j}{j}/(j+1)\) and \(C_n=\sum_{j=0}^{n-1}C_jC_{n-1-j}\). When \(n=2k\), the indices \(j\) and \(n-1-j\) are distinct and paired, with equal Catalan products. Fix one vertex \(v\), select one incident chord from each of the \(k\) mirrored pairs, and call the chosen set \(S\). Every matching contains exactly one chord at \(v\); exactly half of the \(C_n\) matchings have that chord in \(S\). Thus \(W(S)=C_n-2(C_n/2)=0\). There are \(2^k\) choices at each of \(2n\) centers, and because \(k\ge2\), each such star support uniquely identifies its center. This yields \(2n\,2^k\) distinct zeros of weight \(k\), for every even \(n\ge4\).

**2. Exact signed interval recursion.** For a support \(S\), put \(w_S(a,b)=-1\) if chord \(\{a,b\}\) belongs to \(S\), and \(+1\) otherwise. On any half-open consecutive interval of vertices, define its signed noncrossing matching sum \(D_S(a,b)\). Set \(D_S(a,a)=1\) and, for positive even length, use
\[
 D_S(a,b)=\sum_{\substack{a<j<b\\j-a\;\mathrm{odd}}}
 w_S(a,j)D_S(a+1,j)D_S(j+1,b).
\]
Pairing the smallest available vertex \(a\) to \(j\) uniquely decomposes the matching into the two noncrossing submatchings, so this recurrence is exact, has no overcount, and satisfies \(W(S)=D_S(0,16)\). Its signed integers lie within \([-C_8,C_8]\) for this calculation.

**3. Exhaustive low-degree certificate.** Every chord support of weight \(d\) is one of exactly \(\binom{64}{d}\) distinct \(d\)-subsets. For \(d=1,2,3,4\), these numbers are respectively \(64,2016,41664,635376\). The accompanying standalone C++17 checker generates each combination in increasing edge-index order, computes all 32 rotation/reflection images, retains exactly one minimum-bitmask representative from each orbit, and evaluates the recurrence in Step 2 for that representative. Dihedral relabelling preserves noncrossing matchings and signed character sums; each representative is weighted by its **actual distinct orbit size**, not automatically by 32. The computed zero counts are \((0,0,0,544)\). The 544 supports form 17 orbits of size 32. The support-graph degree multisets classify these orbits as eight stars and nine brooms, giving \(8\cdot32=256\) and \(9\cdot32=288\) supports. `ORBIT_CERTIFICATE.txt` records the 17 canonical representatives, one per orbit.

**4. Independent integer computation.** A second standalone Python checker recursively constructs all \(C_8=1430\) noncrossing matchings, and for every chord subset \(A\) of size at most four tabulates the exact inclusion count \(N(A)=|\{M\in\mathcal N_8:A\subseteq M\}|\). It then applies the independent identity
\[
 W(S)=\sum_{A\subseteq S}(-2)^{|A|}N(A)
\]
for every support \(S\) of size at most four. It separately obtains zero counts \((0,0,0,544)\) and the same 256/288 graph-shape split. The identity follows by expanding \(\prod_{e\in S}(1-2\mathbf1_{\{e\in M\}})\) inside each matching. This is exhaustive integer arithmetic rather than sampling or floating-point fitting.

Together these steps establish the entire stated theorem. The general star construction is an all-order proof, whereas the exhaustive certificate establishes the exact low-degree classification only at the specifically claimed finite orders.

## Verification

From a directory containing the supplied standalone files, execute:

```sh
c++ -std=c++17 -O2 noncrossing_walsh_checker.cpp -o check
./check
python3 noncrossing_walsh_moments.py
```

The first program independently outputs the preceding zero counts, orbit and shape counts, and marker `NONCROSSING_MATCHINGS_WALSH_EXACT_PASS`. The second outputs marker `NONCROSSING_MATCHINGS_MOMENT_PASS`. Both also check first-zero counts at \(n=4,6\) as boundary comparisons, respectively 32 at degree two and 216 at degree three. The main classification is at \(n=8\), not a claim of an infinite minimal-degree law.

## Relationship to prior work

The Catalan enumeration and the decomposition of convex-polygon noncrossing matchings are classical. Pilaud and Rué [1] study the generating functions and asymptotics of crossing-free and fixed-crossing matchings, but not their edge-incidence Walsh cancellation locus. Asinowski [2] treats extremal numbers of noncrossing matchings and supplies the classical Catalan decomposition, not cancellation on four edge coordinates. Brauch, Kézdy and Snevily [3] relate a discrete Fourier transform to matching detection through determinant and matroid techniques in different ambient objects. The related published result [4] gives exact one-/two-edge Catalan moments and the first-degree centered Walsh Gram rank of convex-polygon noncrossing matchings; those results do **not** specify the necessary three-/four-edge moments, the sharp sixteen-point zero threshold, or its 17-orbit fourth-degree classification. The present theorem claims none of the classical enumeration, covariance, or flip-graph results as new.

## Limitations

The complete zero support is determined only through Fourier weight four on sixteen vertices, not for higher weights or higher polygon sizes. No full convolution rank, endpoint projection norm, or unrestricted all-size minimum-zero theorem is claimed. The theorem assumes labelled convex vertices and parity-admissible chord coordinates. The finite classification relies on exhaustively inspectable integer checkers rather than a shorter hand classification of all 17 orbit types. Historical priority beyond the inspected searchable records and primary sources is not independently certified.

## References

1. V. Pilaud and J. Rué, *Analytic combinatorics of chord and hyperchord diagrams with \(k\) crossings*, arXiv:1307.6440v1, first publicly posted 2013-07-24, https://arxiv.org/abs/1307.6440.
2. A. Asinowski, *The number of non-crossing perfect plane matchings is minimized (almost) only by point sets in convex position*, arXiv:1502.05332v1, first publicly posted 2015-02-18, https://arxiv.org/abs/1502.05332.
3. T. M. Brauch, A. E. Kézdy and H. S. Snevily, *The Combinatorial Nullstellensatz and DFT on Perfect Matchings in Bipartite Graphs*, Ars Combinatoria 114 (2014), 461–475, https://combinatorialpress.com/ars-articles/volume-114-ars-articles/the-combinatorial-nullstellensatz-and-dft-on-perfect-matchings-in-bipartite-graphs/.
4. *Integral Fourier identifiability from noncrossing perfect matchings*, publicly available mathematical research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-fourier-identifiability-from-noncrossing-perfect-matchi--e353f7965df9.
5. M. C. Hernando, F. Hurtado and M. Noy, *Graphs of Non-Crossing Perfect Matchings*, Graphs and Combinatorics 18 (2002), 517–532, https://doi.org/10.1007/s003730200038.
