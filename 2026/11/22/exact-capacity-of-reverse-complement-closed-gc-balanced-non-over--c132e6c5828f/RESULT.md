# Exact capacity of reverse-complement-closed GC-balanced non-overlapping DNA six-mers

## Finding

Let \(\Sigma=\{A,T,C,G\}\) have Watson–Crick complement \(A\leftrightarrow T\) and \(C\leftrightarrow G\). Among all length-six codebooks \(\mathcal C\subseteq\Sigma^6\) that (i) have exactly three symbols from \(\{C,G\}\) in each word, (ii) are closed under reversal followed by letterwise complementation, and (iii) are non-overlapping, the sharp maximum is

\[
\boxed{\max |\mathcal C|=44.}
\]

Here *non-overlapping* means no nonempty proper prefix of any codeword equals a suffix of any (possibly identical) codeword. A concrete optimum is given in `WITNESS.txt`; the finite exact upper-bound algorithm is in `CHECK.py`.

## Assumptions and scope

All words are **indexed, oriented, length-six DNA words**; rotations do not identify codewords. Define \(\rho(w)=\overline{w_6}\cdots\overline{w_1}\). For words \(u,v\) define compatibility by requiring simultaneously that, for each \(1\le k\le5\), the suffix of \(u\) of length \(k\) differs from the prefix of \(v\) of length \(k\), and vice versa. These restrictions apply to all ordered pairs from \(\mathcal C\), including the same word twice. Exactly three positions of every word are C or G. No minimum Hamming distance, homopolymer bound, or physical primer performance is claimed.

## Proof

**Finite reduction.** There are \(\binom63 2^6=1280\) GC-balanced words of length six: choose three positions occupied by C or G, then choose one of two bases independently at every position. The involution \(\rho\) preserves this set. Its fixed words have even GC-count because a self-reverse-complementary six-mer is partitioned into three complemented position pairs, with both bases of each pair in the same GC class. Therefore the 1280 words fall into 640 distinct two-word orbits.

An orbit \(\{w,\rho(w)\}\) can occur in a non-overlapping, reverse-complement-closed code only if both constituent words are non-overlapping with themselves and with one another. Exhausting these 640 pairs leaves **248 admissible orbits**. Form an undirected compatibility graph \(G\) on the 248 orbits; two distinct orbits are joined when all four cross-pairs are non-overlapping. Direct enumeration gives exactly **9048 edges**.

A reverse-complement-closed code is precisely a union of admissible orbits that form a clique of \(G\). Since every orbit has two words, the largest code size is \(2\omega(G)\).

**Exact upper bound.** The provided standalone Python program `CHECK.py` constructs the entire graph by the definitions above, then exhaustively determines its clique number by recursive branch-and-bound. At each node, it greedily partitions the induced candidate vertices into independent color classes. This proper coloring supplies a rigorous upper bound on the size of any clique in that node. The recursion considers vertices in reverse color order and discards a branch only when its partial clique size plus this upper bound cannot exceed the best clique already exhibited. In the included implementation, all earlier candidate vertices are retained for each branch through exact integer-bitset adjacency intersections. Thus every possible improving clique is explored or eliminated by a valid coloring bound; no heuristic optimum assumption enters the proof.

The complete deterministic computation visits **15,560 recursive nodes**, finds a clique of **22**, and terminates with no improving branch, proving \(\omega(G)=22\). Therefore \(|\mathcal C|\le44\).

**Attainment.** `WITNESS.txt` lists 44 distinct DNA six-mers, each GC-balanced. The code checks its closure under \(\rho\) and verifies all 44-squared ordered pairs and all five overlap lengths. This gives \(|\mathcal C|\ge44\) and completes the proof.

## Verification

With Python 3 installed, place `CHECK.py` and `WITNESS.txt` together and run `python3 CHECK.py`. The checker uses the standard library only and reconstructs all possible words and orbits; it does not read a prerecorded graph. It asserts the counts 1280, 248, 9048, a maximum compatibility-clique size of 22, and the external witness's validity. Its observed deterministic search totals were 15,560 recursive calls and 15,559 branch extensions. A separate exact integer-optimization calculation also returned 22, but is not required to reproduce the proof.

## Relationship to prior work

Stanovnik, Moškon and Mraz [1] analyze balanced non-overlapping codes without reverse-complement closure and report exact optima at small alphabet/block sizes. In the four-letter balanced six-mer case their unrestricted optimum is **192**, so the additional strand-closure condition here reduces capacity to \(44/192=11/48\) of that value. Their general balanced-code bound does not imply the stricter value 44. Their earlier work [2] characterizes unrestricted maximal non-overlapping codes, without this combined GC and strand-closure optimum. Frith, Noé and Kucherov [3] give the unrestricted six-mer maximum 251 in a sequence-search application, again not the present constrained maximum. Primer constructions that combine balance and overlap constraints [4] concern different code families and asymptotic/design bounds.

The distinction is structural: requiring both ends of each Watson–Crick strand pair to participate in the same cross-bifix-free code removes most balanced candidate orbits, so the unrestricted maximum cannot be obtained by a mere symbol relabeling or applying a known size formula.

## Limitations

The exact result concerns only six-base words with exactly three GC symbols and closure under the specified Watson–Crick involution. It is a finite combinatorial optimum, not a general formula for longer primers, error-correction capability, or biochemical reliability. The upper bound relies on an exhaustive but small, independently executable search; a short purely symbolic bound of 22 is not supplied. Historical priority cannot be established by finite literature searches alone; independent mathematical audit has not been performed.

## References

[1] L. Stanovnik, M. Moškon, M. Mraz, *On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths*, arXiv:2410.18458 (first public 2024-10-24), https://arxiv.org/abs/2410.18458 ; Computational and Applied Mathematics 44, 109 (2025), https://doi.org/10.1007/s40314-024-03055-0.

[2] L. Stanovnik, M. Moškon, M. Mraz, *In search of maximum non-overlapping codes*, arXiv:2307.12593, https://arxiv.org/abs/2307.12593 ; Designs, Codes and Cryptography 92 (2024), https://doi.org/10.1007/s10623-023-01344-z.

[3] M. C. Frith, L. Noé, G. Kucherov, *Minimally overlapping words for sequence similarity search*, Bioinformatics 36 (2020), 5344–5350, https://pmc.ncbi.nlm.nih.gov/articles/PMC8016470/.

[4] S. M. H. T. Yazdi, H. M. Kiah, R. Gabrys, O. Milenkovic, *Mutually Uncorrelated Primers for DNA-Based Data Storage*, arXiv:1709.05214, https://arxiv.org/abs/1709.05214.
