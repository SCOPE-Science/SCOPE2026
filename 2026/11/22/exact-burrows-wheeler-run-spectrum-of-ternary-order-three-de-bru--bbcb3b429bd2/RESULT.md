# Exact Burrows–Wheeler run spectrum of ternary order-three de Bruijn cycles

## Finding

Let \(\Sigma=\{0,1,2\}\) with the displayed order. A ternary de Bruijn cycle of order three is a length-\(27\) circular word in which every ordered three-letter factor occurs exactly once. Identify words differing only by cyclic rotation, but **not** by alphabet relabeling or reversal. Let \(L\) be the sentinel-free circular Burrows–Wheeler transform (BWT): sort the \(27\) distinct cyclic rotations lexicographically and read their preceding letters. Define the ordinary linear BWT run count \(r\) and the circular BWT run count \(c\) by

\[
r=1+\sum_{i=1}^{26}\mathbf 1\{L_i\ne L_{i-1}\},\qquad
c=\sum_{i=0}^{26}\mathbf 1\{L_i\ne L_{(i+1)\bmod 27}\}.
\]

**Theorem.** The complete joint distribution of \((r,c)\) over the \(373248\) rotation classes is the following table. Every pair not displayed has multiplicity zero.

| Linear runs \(r\) | Circular runs \(c\) | Number of cycles |
|---:|---:|---:|
| 19 | 18 | 16 |
| 19 | 19 | 58 |
| 20 | 19 | 320 |
| 20 | 20 | 534 |
| 21 | 20 | 1866 |
| 21 | 21 | 4462 |
| 22 | 21 | 7466 |
| 22 | 22 | 17468 |
| 23 | 22 | 16984 |
| 23 | 23 | 47150 |
| 24 | 23 | 26112 |
| 24 | 24 | 76186 |
| 25 | 24 | 24438 |
| 25 | 25 | 77934 |
| 26 | 25 | 13158 |
| 26 | 26 | 44788 |
| 27 | 26 | 2952 |
| 27 | 27 | 11356 |

In particular the least possible linear BWT run count is \(19\), attained by precisely \(74\) cycles, while the least possible circular BWT run count is \(18\), attained by precisely \(16\) cycles. The maximum of either count is \(27\). The marginal linear run counts, indexed by \(r=19,20,\ldots,27\), are

\[
(74,854,6328,24934,64134,102298,102372,57946,14308).
\]

The marginal circular counts, indexed by \(c=18,19,\ldots,27\), are

\[
(16,378,2400,11928,34452,73262,100624,91092,47740,11356).
\]

## Assumptions and scope

The alphabet is ordered and labeled; its three symbols are not quotiented by permutations. A de Bruijn cycle has period exactly \(27\), so it has precisely \(27\) distinct rotations. The BWT contains no endmarker or extra suffix. The linear number of maximal constant-letter runs in its output is distinct from the number when the first and last BWT positions are treated as adjacent. The theorem counts each source cycle once, independent of the chosen starting position.

## Proof

**Step 1: a complete finite parametrization.** Index the \(27\) length-three factors by states \((a,b,c)\in\Sigma^3\). Every de Bruijn cycle defines a successor permutation of these states, sending \((a,b,c)\) to \((b,c,d)\) for the next symbol \(d\). For a fixed suffix \((b,c)\), the three successors \((b,c,d)\) must be distinct. Consequently there is a permutation \(P_{bc}\) of \(\Sigma\) for which

\[
T_P(a,b,c)=(b,c,P_{bc}(a)).
\]

Conversely, any family \(P=(P_{bc})_{(b,c)\in\Sigma^2}\) of nine letter permutations makes \(T_P\) a permutation of all \(27\) triples. It represents exactly one de Bruijn cycle up to rotation if and only if \(T_P\) consists of a single cycle of length \(27\). This is a bijection: the cycle of states uniquely recovers the circular source word and all its transitions, and any de Bruijn cycle uniquely determines its nine local permutations.

**Step 2: an exact BWT boundary formula.** The lexicographic order of cyclic rotations is already fixed by their three-letter prefixes, which are all distinct. For each fixed two-letter prefix \((a,b)\), the three successive rows begin \((a,b,0)\), \((a,b,1)\), \((a,b,2)\). The preceding letters of these rows are respectively

\[
P_{ab}^{-1}(0),\ P_{ab}^{-1}(1),\ P_{ab}^{-1}(2).
\]

Thus the complete BWT consists of nine lexicographically ordered blocks, each a permutation of \(\Sigma\). The blocks themselves are a known structural property, not a novelty claim. They contribute exactly \(18\) internal boundaries where consecutive BWT symbols differ. Label the nine two-letter prefixes by integers \(u=0,1,\ldots,8\) in base three, and write \(Q_u=P_u^{-1}\). For \(u=0,\ldots,8\) define

\[
\delta_u=\mathbf 1\{Q_u(2)\ne Q_{(u+1)\bmod9}(0)\}.
\]

Then the exact run counts for any accepted permutation family are

\[
r=19+\sum_{u=0}^{7}\delta_u,\qquad c=18+\sum_{u=0}^{8}\delta_u.
\]

In particular the joint distribution is the coefficient table of the following fully specified *finite* polynomial, where the sum is over \(6^9=10077696\) labeled permutation choices:

\[
F(X,Y)=\sum_{P\in(S_3)^9}\mathbf1\{T_P\text{ is a 27-cycle}\}\,
X^{19+\sum_{u=0}^{7}\delta_u}\,
Y^{18+\sum_{u=0}^{8}\delta_u}.
\]

**Step 3: exhaustive integer evaluation.** `verify_orientations.cpp` enumerates the six permutations at each of the nine contexts by a nine-digit base-six index, with no sampling or pruning of candidate families. For each of the \(10077696\) choices, it starts from state \((0,0,0)\) and follows at most \(27\) successor steps, recording a \(27\)-bit visited mask. Such a permutation is a single \(27\)-cycle if and only if its orbit returns to zero and the visited mask contains all \(27\) bits. For each accepted family it evaluates the nine displayed boundary indicators with integer comparisons and increments one table cell. This gives exactly \(373248\) accepted families and the \(18\) cells above.

A second enumeration, `verify_euler.cpp`, avoids the permutation-family test entirely. It enumerates Euler tours of the directed overlap graph on the nine length-two words, with all \(27\) distinct length-three words as labeled edges. Every tour contains the self-loop edge \((0,0,0)\) exactly once, so fixing it as the first edge gives one tour per rotational class. For each of the \(373248\) completed tours, the code reconstructs the \(27\)-symbol word, orders its rotations by their distinct length-three prefixes, reads the BWT directly, and counts adjacent changes. Its complete integer table agrees cell by cell with the first program. These programs therefore give a finite exhaustive certificate for every number in the table, not a probabilistic estimate.

## Verification

In a C++17 environment, from the directory containing the two standalone source files, run

```text
g++ -O2 -std=c++17 verify_orientations.cpp -o verify_orientations
./verify_orientations
g++ -O2 -std=c++17 verify_euler.cpp -o verify_euler
./verify_euler
```

Both programs contain hard assertions for the full \(18\)-cell table and the total \(373248\). The first emits `ORIENTATION_CERTIFICATE_OK 373248`, and the second emits `EULER_CERTIFICATE_OK 373248`. They enumerate the same mathematical objects by different representations: successor permutations versus Eulerian edge tours. Each runs without external data or third-party libraries. The published de Bruijn count \((3!)^9/3^3=373248\) is an additional independently established total-count benchmark, but is not used in place of enumerating the distribution.

## Relationship to prior work

The general BWT inversion and permutation-block structure is established in earlier literature. Higgins explicitly proves the concatenation-of-permutations property for de Bruijn sets and the familiar total number of de Bruijn necklaces [2]. Fici and Gabory develop its Hamiltonian-cycle interpretation, and their Table 1 already records the total \(373248\) for ternary length \(27\) [3]. Neither of those findings determines the joint run-count multiplicities. Kufleitner discusses standard and bijective BWT variants [1] without such an order-three ternary enumeration. Date and Zatesko study run-minimal BWT patterns and obtain a general lower bound for a different, endmarked linearized setting, not the distribution across sentinel-free ternary order-three necklaces [4]. A separately recorded *binary order-five* BWT spectrum [5] has a different alphabet and cycle class and does not imply these ternary coefficients. These structural and cardinality results are **credited**, not presented as new. The novel candidate is specifically the exact \(18\)-cell joint spectrum and its sharp extremal multiplicities.

## Limitations

This is an exact finite classification for the fixed alphabet size three and de Bruijn order three; it is **not** a distribution theorem for arbitrary order or alphabet size, nor a proof of a new general run lower bound. The proof uses exhaustive finite integer computation and includes complete reproducible enumerators, but no separate formal verification system or independent external audit. Historical priority is qualified: an unlocated exact historical table under different terminology could cover the numerical claim. The run counts concern the *sentinel-free circular-rotation BWT*, not an endmarked suffix BWT, and linear versus cyclic runs must not be conflated.

## References

1. Manfred Kufleitner, *On Bijective Variants of the Burrows-Wheeler Transform*, arXiv:0908.0239, first posted 2009-08-03. https://arxiv.org/abs/0908.0239
2. Peter M. Higgins, *Burrows–Wheeler transformations and de Bruijn words*, Theoretical Computer Science 457 (2012), 128–136; open full-text version https://arxiv.org/html/1901.08392v1. In particular Section 3, Theorem 3.4.
3. Gabriele Fici and Estéban Gabory, *Generalized De Bruijn Words, Invertible Necklaces, and the Burrows-Wheeler Transform*, arXiv:2502.12844 (2025), particularly Section 3 and Table 1. https://arxiv.org/abs/2502.12844
4. Vinicius T. V. Date and Leandro M. Zatesko, *On the near-tightness of \(\chi\le 2r\): a general \(\sigma\)-ary construction and a binary case via LFSRs*, arXiv:2512.20598 (2025), particularly Section 5. https://arxiv.org/abs/2512.20598
5. *Complete BWT-run spectrum of binary order-five de Bruijn cycles*, available research record, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-complete-bwt-run-spectrum-of-binary-order-five-de-bruijn-cycles--1eb61f1d72f3
