# Exact one-adjacent-swap capacity of GC-balanced reverse-complement DNA four-mers

## Finding

Let \(\Sigma=\{A,C,G,T\}\). Write \(\overline A=T\), \(\overline T=A\), \(\overline C=G\), and \(\overline G=C\), and let \(\rho(x_1x_2x_3x_4)=\overline{x_4}\overline{x_3}\overline{x_2}\overline{x_1}\). A codebook \(C\subseteq\Sigma^4\) is admissible when each member has exactly two letters in \(\{C,G\}\), \(\rho(C)=C\), no member is fixed by \(\rho\), and the closed single-adjacent-swap balls of any two distinct members are disjoint. Then

\[
\max |C|=22,
\]

and exactly \(5184\) labeled admissible codebooks achieve this size. Here labeled means that nucleotide identities and all four coordinate positions are fixed, without dividing by any symmetry group.

One attaining codebook, in lexicographic order, is

`AACC AAGG ACAG AGAC ATCC ATCG ATGG CACA CCAT CCTT CGAA CGAT CTAC CTGT GAGA GGAT GGTT GTAG GTCT TCTC TGTG TTCG`.

For comparison, dropping reverse-complement closure and the self-reverse-complement prohibition while retaining composition and correction raises the maximum to \(25\) codewords; this comparison is verified independently.

## Assumptions and scope

The error model allows either no change or one swap of two **adjacent positions** among the three pairs of positions in a four-letter word. In particular, a swap of equal letters causes no change. For a word \(x=x_1x_2x_3x_4\), denote the set of these possible received words by

\[
B(x)=\{x,s_1(x),s_2(x),s_3(x)\},
\]

where \(s_i\) interchanges positions \(i\) and \(i+1\). Correctability is the necessary and sufficient condition \(B(x)\cap B(y)=\varnothing\) for all distinct \(x,y\in C\). There are no deletions, substitutions, reversals, or arbitrary non-adjacent permutations in the channel. Closure under \(\rho\) means that both orientations are separately present as codewords, not that the decoder is allowed to identify a word with its reverse complement.

## Proof

**Reduction to reverse-complement orbits.** There are \(\binom42 2^4=96\) words with exactly two C/G symbols. Exactly eight satisfy \(x=\rho(x)\). Every remaining word belongs to a disjoint two-element orbit \(\{x,\rho(x)\}\), giving \(44\) orbits. Because admissible codes contain no fixed words and satisfy \(\rho(C)=C\), they are unions of these two-element orbits. Four orbits are immediately impossible: their two members have intersecting swap balls. The remaining \(40\) orbits are candidate vertices.

**Conflict graph.** Join two distinct admissible orbit vertices \(P,Q\) when \(\bigcup_{x\in P}B(x)\) intersects \(\bigcup_{y\in Q}B(y)\). An admissible codebook corresponds bijectively to an independent set of this \(40\)-vertex graph, with exactly twice as many codewords as selected vertices. The graph has \(100\) undirected edges. Since adjacent swaps preserve the multiset of symbols, and reverse complementation sends each symbol multiset to its complement, the conflict graph separates by complementary multiset classes. Its five nonempty connected components have the following exact independently checked data:

| Component vertices | Maximum independent-set size | Number of maximum independent sets |
|---:|---:|---:|
| 6 | 2 | 3 |
| 12 | 3 | 12 |
| 6 | 2 | 3 |
| 12 | 3 | 12 |
| 4 | 1 | 4 |

**Exhaustive finite upper bound and equality count.** The first verifier enumerates every subset of each component, tests every selected pair against the conflict edges, and determines both the largest size and the exact number of subsets of that size. This is exhaustive over exactly \(2^6+2^{12}+2^6+2^{12}+2^4\) candidate masks: no unsearched larger graph or heuristic cutoff remains. A global independent set restricts to an independent set in each component; conversely, the union of any independent choices from these disjoint components is independent. Thus the maximum orbit count is

\[
2+3+2+3+1=11,
\]

and the number of labeled maximum orbit selections is

\[
3\cdot12\cdot3\cdot12\cdot4=5184.
\]

Every orbit contributes two distinct codewords, proving the claimed maximum \(22\) and exact enumerator \(5184\). The displayed witness is checked directly from its \(22\) DNA words, rather than inferred merely from graph independence.

**Unrestricted comparison.** Independently, partition all \(96\) composition-balanced words by their nine exact nucleotide multisets. Adjacent-swap balls from distinct multisets cannot intersect. The second verifier enumerates the maximum independent set within each such multiset class using an exact mask recursion, obtaining total maximum \(25\). This comparison is not used to prove the constrained result.

## Verification

Run `python verify.py` and `python verify_independent.py` in the same directory as these files; both use only the Python standard library and reconstruct all candidate words, error balls, and conflict relations from their mathematical definitions. The first reconstructs the five components and exhaustively tests every component subset; the second uses a different, composition-first partition and a recursive maximum-independent-set count. Expected end markers are `PASS_ALL_EXHAUSTIVE_CERTIFICATES` and `ALTERNATIVE_COMPOSITION_DP_PASS`. Both programs were executed successfully, and the complete witness was independently tested against every pair of its own swap balls. The packaged source code is the reproducibility artifact; no external solver or unexplained precomputed table is required.

## Relationship to prior work

King's 2003 work develops constant-GC DNA code bounds involving Hamming separation and Watson–Crick reverse-complement constraints. Its Hamming formulation neither establishes correction of adjacent transpositions nor enumerates the present closed-code optima. Gabrys, Yaakobi and Milenkovic (2016) introduce adjacent-transposition and deletion coding motivated by DNA storage and explicitly restrict their principal analysis to binary alphabets; they do not establish this quaternary, constant-composition, reverse-complement-closed four-mer optimum. Bennenni, Guenda and Mesnager (2015) construct reverse-complement cyclic/skew cyclic DNA codes over finite rings, with Hamming and edit-distance applications, but their stated constructions and tables address different code families and do not provide this extremizer census. Kiah, Puleo and Milenkovic (2014) investigate DNA sequence-profile channels, not the present full-word swap channel.

The calculation is a statement-level comparison of code alphabets, channels, closure conventions, and exact parameter questions, not a claim that absence of matching keywords proves novelty. A full historical-priority review beyond the inspected primary sources remains necessary.

## Limitations

This theorem is limited to four-letter DNA words of length exactly four with exactly two C/G symbols, closure under Watson–Crick reverse complement, exclusion of fixed words, and correction of zero or one adjacent swap. It does not imply anything about the performance of laboratory DNA strands, substitution/deletion correction, longer strands, unconstrained best codes, or physical strand stability. It has had self-review only, not an independent scientific audit.

## References

- O. D. King, *Bounds for DNA codes with constant GC-content*, arXiv:math/0306197, first public June 12, 2003, https://arxiv.org/abs/math/0306197.
- R. Gabrys, E. Yaakobi, and O. Milenkovic, *Codes in the Damerau Distance for Deletion and Adjacent Transposition Correction*, arXiv:1601.06885, first public January 26, 2016, https://arxiv.org/abs/1601.06885.
- N. Bennenni, K. Guenda, and S. Mesnager, *New DNA Cyclic Codes over Rings*, arXiv:1505.06263, first public May 23, 2015, https://arxiv.org/abs/1505.06263.
- H. M. Kiah, G. J. Puleo, and O. Milenkovic, *Codes for DNA Storage Channels*, arXiv:1410.8837, first public October 31, 2014, https://arxiv.org/abs/1410.8837.
