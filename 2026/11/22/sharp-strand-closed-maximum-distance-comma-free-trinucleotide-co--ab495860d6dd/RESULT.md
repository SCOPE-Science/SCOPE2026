# Sharp strand-closed maximum-distance comma-free trinucleotide codes

## Finding
Let \(\Sigma\) be an alphabet of even size \(q\ge 2\), equipped with a fixed-point-free involution \(c:\Sigma\to\Sigma\) (a prescribed complementary-base pairing). A code \(C\subseteq\Sigma^3\) is **strand-closed** if \((a,b,d)\in C\) implies \((c(d),c(b),c(a))\in C\); it is **comma-free** if neither \((b,d,e)\) nor \((d,e,f)\) belongs to \(C\) for any \((a,b,d),(e,f,g)\in C\). Require in addition Hamming distance exactly three between all distinct codewords (equivalently, minimum distance at least three).

The sharp maximum is
\[
 M(q)=\begin{cases}0,&q=2,\\q,&q\ge4\text{ even}.
 \end{cases}
\]
The empty code is admitted, and the distance condition is vacuous for codes of size at most one. There is no nonempty admissible code when \(q=2\), because reverse complementation has no fixed word of odd length.

All equality cases at even \(q\ge4\) have a uniform exact classification. Fix labels \(\Sigma=\{0,\ldots,q-1\}\) with \(c(i)=i\mathbin{\mathrm{xor}}1\), and write permutation composition right-to-left. For a permutation \(f\) of \(\Sigma\), set \(g=c\circ f^{-1}\circ c\circ f\). Then
\[
 C_f=\{(i,f(i),g(i)):i\in\Sigma\}
\]
is admissible if and only if
\[
 \forall i\in\Sigma:\quad g(i)\ne f(f(i)).\tag{1}
\]
Conversely, every admissible \(q\)-word code is exactly one \(C_f\), with \(f\) uniquely determined. Thus (1) is a constructive classification for every even alphabet size.

For the four-base alphabet there are exactly **six** labeled optimal codebooks. They form **two** orbits of cardinalities **two and four** under the eight alphabet relabelings commuting with \(c\). With codewords written as digit triples, the complete list is:

| Codebook | Four codewords |
|---|---|
| A | `002`, `133`, `220`, `311` |
| B | `003`, `122`, `211`, `330` |
| C | `020`, `131`, `212`, `303` |
| D | `022`, `113`, `200`, `331` |
| E | `030`, `121`, `202`, `313` |
| F | `033`, `112`, `221`, `300` |

The same exact permutation test yields \(160\) labeled optimal codes for \(q=6\) and \(8988\) for \(q=8\); these are finite computed consequences, not formulas asserted for arbitrary \(q\).

## Assumptions and scope
The model uses three aligned symbol positions, substitution Hamming distance, standard length-three comma-free concatenation tests at shifts one and two, and **closure** under reversal followed by the fixed complement involution. Closure differs from merely requiring codeword distance from the reverse complement of another word. In particular, an optimal code is not claimed to have cross-bifix-freeness, and the statement makes no assumption of constant GC content. The alphabet must consist of complement pairs; no odd alphabet size is addressed.

## Proof
**Upper bound.** If two distinct codewords have distance three, they differ in all three coordinates. Each of the three coordinate projections on \(C\) is injective, so \(|C|\le q\).

**Exact full-size characterization.** At equality, the first coordinate labels every element of \(\Sigma\) exactly once, and the other two coordinates are permutations \(f,g\). A splice at shift one from \((i,f(i),g(i))\) to a word indexed \(j\) equals a codeword precisely when its first two symbols \((f(i),g(i))\) agree with \((f(i),f(f(i)))\); one may then choose \(j=g(f(i))\) to match the third symbol. Consequently all shift-one splices are excluded if and only if \(g(i)\ne f^2(i)\) at every \(i\). A shift-two splice can equal a codeword exactly if \(f^2(g(i))=g^2(i)\), which is the failure of the same inequality at index \(g(i)\). As \(g\) is bijective, the shift-two condition adds no further restriction.

Write \(t=c\circ g\). If \(C\) is reverse-complement closed, then the reverse complement of the word indexed by \(i\) has first coordinate \(t(i)\). Matching its middle coordinate forces \(f\circ t=c\circ f\), hence \(t=f^{-1}\circ c\circ f\) and \(g=c\circ f^{-1}\circ c\circ f\). Its third coordinate is automatically correct because \(t^2\) is the identity. Conversely this formula for \(g\) ensures closure. Combining these facts proves the bijection with permutations satisfying (1).

**Binary obstruction.** For \(q=2\), the permutation group consists of the identity and \(c\); these commute with \(c\) and each squares to the identity. Therefore \(g=c f^{-1}c f\) and \(f^2\) are both the identity for either choice of \(f\), contradicting (1). Every nonempty strand-closed code has even cardinality because reverse complementation has no fixed length-three words. Its size would therefore be two, already excluded by the full-size case.

**Attaining \(q\) for all even \(q\ge4\).** For \(q=4\), use
\[
C_4=\{003,122,211,330\}.
\]
For \(q=6\), use
\[
C_6=\{003,125,211,344,430,552\}.
\]
In each displayed code, the complement pairs are \(0\leftrightarrow1\), \(2\leftrightarrow3\), and, when applicable, \(4\leftrightarrow5\). Their distance, closure and comma-free conditions follow by the explicit thirty-two or seventy-two ordered-splice tests, or by checking (1) on their middle-coordinate permutations. If two admissible codes are written on disjoint alphabets, each preserved by the complement, their union is admissible: codewords from different blocks disagree in every coordinate, and each splice between blocks contains letters from both blocks and cannot equal a word supported within one block. Every even integer at least four is a sum of fours or a six plus fours. Direct unions of \(C_4\) and \(C_6\) therefore meet the upper bound at every claimed size.

**Four-base completeness and orbits.** At \(q=4\), the classification has exactly \(4!=24\) candidates \(f\). Direct substitution into (1) leaves six permutations, with one distinct codebook per permissible \(f\). Their words are listed above. Independently, every length-three word is paired with a distinct reverse complement; hence there are \(64/2=32\) complementary pairs. Every four-word strand-closed code comprises exactly two such pairs. Testing the \(\binom{32}{2}=496\) candidates directly leaves precisely the six displayed codebooks. The relabeling group consists of the eight permutations \(\sigma\) satisfying \(\sigma c=c\sigma\); direct action on these six sets gives orbit sizes \(2\) and \(4\). This finishes the classification.

## Verification
Two standalone standard-library Python programs implement different finite checks. Run `python3 verify_permutations.py` and `python3 verify_direct.py`. The first enumerates all \(q!\) permutations and tests the exact criterion at \(q=2,4,6,8\), obtaining counts \(0,6,160,8988\). It also directly checks examples of the disjoint-block construction. The second independently generates every reverse-complement pair of length-three words on four symbols, examines all \(496\) unordered pairs of pairs by the literal splice and Hamming tests, and verifies the complete six-code census and the orbit sizes. Both finish without external packages.

The proof for arbitrary even \(q\ge4\) is symbolic and uses the upper bound and disjoint-block construction; finite checks are independent consistency tests, **not** extrapolations or an infinite proof.

## Relationship to prior work
The classical theory of comma-free coding studies frame synchronization without the simultaneous reverse-complement-closure and maximal substitution-distance requirements. Michel and Pirillo (2011) give a hierarchy of trinucleotide circular and comma-free codes and compare stronger prefix/suffix restrictions, but their inspected definitions and results do not classify maximum-distance strand-closed codes. Michel (2015) studies the different problem of twenty-word self-complementary circular codon sets in genes; the accessible abstract is not enough for a negative full-paper priority determination. The published non-overlapping (cross-bifix-free) model is stricter than comma-freeness: no full-size distance-three code here can be non-overlapping, since every alphabet symbol occurs in the first and last coordinates. These distinctions preclude straightforward implication from the stated neighboring results.

## Limitations
The theorem assumes a fixed-point-free complement, aligned correction of one substitution, and exact length three. It does not classify nonoptimal codebooks, infer any biochemical reliability, or establish novelty against inaccessible historical full texts. The counts \(160\) and \(8988\) are exact finite-enumeration consequences of the proved bijection, not an all-alphabet counting formula. The six DNA solutions are labeled by a specified Watson–Crick pairing; arbitrary alphabet permutations are not symmetries of the paired problem.

## References
1. C. J. Michel and G. Pirillo, *Strong Trinucleotide Circular Codes*, International Journal of Combinatorics (2011), doi:10.1155/2011/659567, first published August 25, 2011. https://onlinelibrary.wiley.com/doi/full/10.1155/2011/659567
2. C. J. Michel, *The maximal \(C^3\) self-complementary trinucleotide circular code X in genes of bacteria, eukaryotes, plasmids and viruses*, Journal of Theoretical Biology 380 (2015), 156–177, doi:10.1016/j.jtbi.2015.04.009, online April 29, 2015. https://pubmed.ncbi.nlm.nih.gov/25934352/
3. S. R. Blackburn, *Non-Overlapping Codes*, IEEE Transactions on Information Theory 61 (2015), 4890–4894, doi:10.1109/TIT.2015.2456634. https://arxiv.org/abs/1303.1026
4. *Generalized DNA Barcode Design Based on Hamming Codes*, PLOS ONE (2012), https://pmc.ncbi.nlm.nih.gov/articles/PMC3355179/ (for the separate Hamming-distance design motivation).
