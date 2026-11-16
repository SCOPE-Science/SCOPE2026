# Exact Fourier nullity and sharp recovery gap for nine-vertex Hamiltonian-cycle convolution

## Finding

Let \(G=\mathbb F_2^{E(K_9)}\), with the \(36\) coordinates indexed by undirected edges of the labelled complete graph on nine vertices. Let \(f:G\to\{0,1\}\) indicate the \(20{,}160\) unoriented Hamiltonian-cycle incidence vectors. For every edge-frequency set \(S\), use the unnormalized Walsh transform \(W(S)=\sum_{x\in G}f(x)(-1)^{\langle S,x\rangle}\). The exact absolute-multiplier histogram has **38 levels** including zero. Each frequency in the following reduced histogram occurs exactly \(256\) times in the original \(36\)-dimensional group.

| \(\lvert W\rvert\) | Reduced multiplicity | \(\lvert W\rvert\) | Reduced multiplicity |
|---:|---:|---:|---:|
| 0 | 52,179,336 | 32 | 61,341,840 |
| 64 | 24,494,400 | 96 | 40,670,280 |
| 128 | 38,384,640 | 160 | 16,475,760 |
| 192 | 6,791,400 | 224 | 5,854,680 |
| 256 | 7,091,280 | 288 | 6,028,400 |
| 320 | 1,829,520 | 352 | 1,088,640 |
| 384 | 1,840,860 | 416 | 635,040 |
| 448 | 232,470 | 480 | 1,520,568 |
| 512 | 635,040 | 576 | 81,900 |
| 608 | 15,120 | 640 | 90,720 |
| 672 | 317,520 | 768 | 347,760 |
| 832 | 90,720 | 864 | 216,720 |
| 960 | 15,876 | 1,056 | 22,680 |
| 1,152 | 67,200 | 1,440 | 20,328 |
| 1,536 | 22,680 | 1,728 | 15,120 |
| 1,920 | 3,024 | 2,112 | 1,890 |
| 2,400 | 7,560 | 2,880 | 1,134 |
| 3,360 | 2,520 | 5,760 | 756 |
| 10,080 | 72 | 20,160 | 2 |

Consequently the unnormalized counting-convolution operator \(T_f:g\mapsto f*g\) has exact real rank \(55{,}361{,}566{,}720\) and nullity \(13{,}357{,}910{,}016\), on its ambient space of dimension \(2^{36}\). Its smallest positive singular value is \(32\), its largest singular value is \(20{,}160\), its Moore–Penrose inverse has sharp Euclidean operator norm \(1/32\), and the positive-spectrum condition number is \(630\).

## Assumptions and scope

The graph and its vertices are labelled. Cycles and paths are undirected and counted without either orientation; a cycle is represented by its edge-incidence vector, not by a word or starting vertex. Signs are \((-1)\)-valued and convolution is counting convolution, with no probability normalization or Haar factor. The claim concerns only the nine-vertex complete graph and does not extrapolate the histogram to other orders.

## Proof

Fix vertex \(0\). Switching every edge sign incident with a vertex \(i\) leaves every Hamiltonian-cycle product unchanged because the cycle has degree two at every vertex. There is a unique switch choice making all eight root-star edge signs positive. Hence each reduced internal-edge signing appears with exactly \(2^8\) original frequencies. Removing vertex \(0\) from an unoriented Hamiltonian cycle produces an unoriented Hamiltonian path on the eight remaining labelled vertices, and conversely closing this path through \(0\) produces a unique Hamiltonian cycle. Thus it suffices to transform the incidence function of the \(8!/2=20{,}160\) Hamiltonian paths inside \(\mathbb F_2^{28}\).

The first exhaustive method, `verify_walsh.cpp`, enumerates the \(20{,}160\) Hamiltonian-path masks (permutations divided by endpoint reversal). It sets the indicator at precisely those masks and performs all \(28\) integer Walsh butterfly stages across \(2^{28}\) masks. Every intermediate entry has absolute value at most \(20{,}160\), because it is a signed sum over a subset of the original path indicator, so signed 16-bit integer storage is exact. The resulting complete absolute histogram is `spectrum_counts.txt`.

An algebraically different method starts from \((-1)^a=1-2a\), valid for \(a\in\{0,1\}\), to obtain
\[
W(S)=\sum_{F\subseteq S}(-2)^{|F|}H(F),
\]
where \(H(F)\) counts undirected Hamiltonian paths containing every edge of \(F\). The count is zero unless \(F\) is a disjoint union of nontrivial paths and isolated vertices. For nonempty such \(F\) with \(t=|F|\le7\) edges and \(r\ge1\) nontrivial path components, contraction gives
\[
H(F)=2^{r-1}(8-t)!.
\]
The empty set contributes \(H(\varnothing)=8!/2\). Indeed, after contracting forced paths one may order the \(8-t\) components arbitrarily and orient each of the \(r\) nontrivial paths in two ways, then divide by total path reversal. The second program, `verify_zeta.cpp`, independently enumerates all admissible forced forests, initializes their weighted counts and computes the exact subset-zeta transform to recover every \(W(S)\). Its histogram agrees entry by entry with the Walsh computation. During subset summation the absolute intermediate is at most \((8!/2)3^7=44{,}089{,}920\), well within signed 32-bit storage.

The second method proves the generated histogram is a complete integer certificate rather than sampling: there are exactly \(2^{28}\) frequency masks, every mask is visited, and all possible nonzero forced-edge configurations are enumerated (any Hamiltonian path has seven edges). The histograms each sum to \(268{,}435{,}456=2^{28}\). Both satisfy Parseval exactly:
\[
\sum_{S\in\mathbb F_2^{28}}W(S)^2=2^{28}(8!/2)=5{,}411{,}658{,}792{,}960.
\]
There are \(52{,}179{,}336\) reduced zero multipliers and \(216{,}256{,}120\) reduced nonzero multipliers. Multiplying both counts by \(256\) gives the full nullity and rank. Fourier diagonalization of finite-group convolution yields the singular values \(|W(S)|\), so the tabulated smallest positive value \(32\) and largest value \(20{,}160\) give the stated sharp inverse norm and condition number.

## Verification

Run `g++ -O3 -std=c++17 verify_walsh.cpp -o verify_walsh && ./verify_walsh > walsh.txt` and separately `g++ -O3 -std=c++17 verify_zeta.cpp -o verify_zeta && ./verify_zeta > zeta.txt`. Both outputs include the same \(38\) lines of positive/zero absolute magnitudes. Their first-line fields differ only by the additional fourth-moment residue emitted by the Walsh implementation. Compare the histogram lines from line two onward against `spectrum_counts.txt` from line two onward. Both exhaustive methods completed in exact arithmetic. `python3 verify_dp.py` separately checks the signed path count by an endpoint-subset dynamic program, including a four-negative-edge cancellation.

## Relationship to prior work

John Gimbel's 2004 work on abelian edge labels of Hamiltonian cycles characterizes important cases in which all cycles share the same label sum, rather than the distribution and total cancellations between opposite cycle signs. Xiyong Yan's 2025 work classifies when positive and negative Hamiltonian cycles both exist in a signed complete graph, but the presence of both signs does not determine their exact imbalance, Fourier nullity or spectral condition numbers. Previous results on Fourier sampling of directed tours and on Walsh transforms of perfect matchings address different sampling systems or different combinatorial supports. A prior nonvanishing/vanishing result at selected complete-graph orders already supplies a single nine-vertex cancellation example, but does not imply the exact \(52{,}179{,}336\)-zero count, full histogram or sharp positive-spectrum bounds.

## Limitations

The exact full histogram is certified at nine vertices only; it implies neither a general formula nor a monotonicity statement in graph order. The finite computation is exhaustive and reproducible but is not a general symbolic closed form. The C++ exhaustive implementations each use roughly \(0.5\)–\(1.1\) GiB of working memory and require ordinary 64-bit arithmetic for aggregated checks. Historical priority is only assessed against accessible indexed and inspected literature; an unindexed equivalent computation could exist. Independent mathematical audit has not been performed.

## References

- J. Gimbel, “Abelian Group Labels on Hamiltonian Cycles,” *Journal of Combinatorial Mathematics and Combinatorial Computing* 51 (2004), 3–32. Public source dated 30 November 2004. https://combinatorialpress.com/article/jcmcc/Volume%20051/vol-051-paper%201.pdf
- X. Yan, “Hamiltonian Cycles in Signed and Multisigned Complete Graphs,” arXiv:2502.10612 (submitted 15 February 2025). https://arxiv.org/html/2502.10612v1
