# Exact size and symmetry spectra of six-symbol strand-closed circular dinucleotide codes

## Finding

Let \(\Sigma=\{0,1,2,3,4,5\}\), with the fixed-point-free complement \(c(0)=1,\ c(1)=0,\ c(2)=3,\ c(3)=2,\ c(4)=5,\ c(5)=4\). For a word \(uv\), define its reverse complement by \(\rho(uv)=c(v)c(u)\). A set \(X\subseteq\Sigma^2\) is *strand closed* if \(\rho(X)=X\). It is a *circular dinucleotide code* if no nonempty circular concatenation of members admits two different two-symbol reading frames into members of \(X\); the empty set is included by convention.

The exact size enumerator of all labeled strand-closed circular dinucleotide codes is

\[
\begin{aligned}
F(z)={}&1+6z+24z^2+80z^3+192z^4+420z^5+704z^6+1032z^7\\
&+1290z^8+1334z^9+1248z^{10}+936z^{11}+612z^{12}\\
&+336z^{13}+120z^{14}+48z^{15}.
\end{aligned}
\]

Thus there are exactly \(8383\) such sets including the empty set, and \(8382\) nonempty ones. Under the group of all \(48=2^3\cdot3!\) symbol relabelings commuting with \(c\), the corresponding orbit-count enumerator is

\[
\begin{aligned}
G(z)={}&1+z+2z^2+4z^3+7z^4+12z^5+20z^6+27z^7\\
&+32z^8+33z^9+30z^{10}+23z^{11}+15z^{12}\\
&+9z^{13}+3z^{14}+z^{15}.
\end{aligned}
\]

Consequently there are exactly \(220\) equivalence classes including the empty set, and \(219\) nonempty classes. The coefficient of \(z^{15}\) means there are exactly \(48\) labeled full-size sets, all equivalent. `representatives.csv` supplies an actual codeword-list representative, with orbit size, for each of the \(220\) classes.

## Assumptions and scope

Symbols are labeled, complement pairs are exactly \(\{0,1\},\{2,3\},\{4,5\}\), and all words have length two. The reverse complement includes reversal of the symbol order. Circularity is stronger than merely forbidding a repeated codeword or its rotation: it excludes every cyclic ambiguity of a two-symbol reading frame. Distinct codes are distinct subsets of the \(36\) possible two-symbol words. The orbit group is the complete centralizer of \(c\) in \(S_6\); reading reversal alone induces the same action on a strand-closed set as global symbol complementation and hence gives no new equivalence relation.

## Proof

**Circularity and directed acyclicity.** Associate to \(X\) the directed graph on \(\Sigma\) having an arc \(u\to v\) for each \(uv\in X\). An ambiguity of cyclic two-letter framing is equivalent to a directed closed walk in this graph: reading consecutive members from one framing and the shifted framing requires every adjacent pair of symbols on the resulting circle to be a codeword. Conversely, any directed closed walk yields the two different groupings of an even repetition of its vertex sequence. Therefore circularity is equivalent to absence of directed cycles (including loops and directed two-cycles). This is the familiar graph criterion for circular dinucleotide codes, and also follows directly from the two-frame definition.

**Symmetric topological extension.** Strand closure changes an arc \(u\to v\) into \(c(v)\to c(u)\). If a strand-closed graph is acyclic and \(u\) is a source, \(c(u)\) is a sink. Removing this pair gives a smaller strand-closed acyclic graph; by induction its vertices have an order \(w\) such that the complement reverses that order. Placing \(u\) before \(w\) and \(c(u)\) after \(w\) gives an order compatible with all original arcs and still reversed by complement. There are exactly \(2^3 3!=48\) such *symmetric orders*: select and order one letter from each of the three complement pairs in the first half; the second half is forced. Every allowed set is consequently a subset of at least one of the \(48\) full transitive tournaments obtained from these orders. The tournaments are distinct, and each is strand closed, has \(\binom62=15\) arcs, and is maximal.

**Finite exhaustive encoding.** Ignore arc orientation momentarily. The complement acts on the \(\binom62=15\) unordered symbol pairs. Exactly three orbits are individual complement pairs, and the remaining \(12\) unordered pairs form six orbits of size two. Each of these nine unordered-pair orbits admits precisely three acyclicity-compatible, strand-invariant states: absent, oriented one way, or oriented the opposite way. Indeed, selecting both directions of any pair would create a directed two-cycle, while complement forces the corresponding second arc when the orbit has two pairs. The first three orbit choices have codeword weight one, and the remaining six have weight two.

Thus every possible strand-closed *acyclic* code is represented exactly once among the \(3^9=19683\) three-state words. The standalone `direct_verify.py` examines all these words, constructs the exact directed graph, and detects directed cycles by a depth-first search with a three-color recursion. Its rank histogram is exactly the sixteen coefficients of \(F(z)\) above. No stochastic sampling, truncation, or extrapolation enters this enumeration.

**Independent complete-count and orbit calculation.** `chamber_verify.py` implements a logically different enumeration: for each of the \(48\) symmetric total orders it enumerates all \(2^9\) subsets of the nine reverse-complement arc orbits of that order, and unites the resulting labeled codes. The extension lemma proves that this union is exactly the intended set, and the resulting histogram equals \(F(z)\). It computes orbit counts using Burnside's lemma, summing the fixed-code count separately for each of the \(48\) complement-preserving label permutations and dividing by \(48\). The output is precisely \(G(z)\). Independently, `direct_verify.py` constructs explicit relabeling orbits, obtains the same \(G(z)\), and checks that `representatives.csv` lists the least adjacency-mask representative of every orbit with its actual orbit size.

## Verification

Run `python3 direct_verify.py` and `python3 chamber_verify.py` in the same directory as `representatives.csv`, using an ordinary Python 3 installation. The first prints `DIRECT_VERIFY_OK` and the full labeled/orbit histograms; the second prints `CHAMBER_BURNSIDE_VERIFY_OK` and the identical histograms, plus the smaller one- and two-pair checks. The direct search covers \(19683\) candidate choices, while the independent search covers \(48\cdot512=24576\) chamber-subsets before deduplication. The embedded table has \(220\) representative rows; their orbit sizes sum to \(8383\). Both programs use only Python's standard library.

## Relationship to prior work

Michel and Pirillo (2013) enumerate the \(24\) maximal four-letter dinucleotide circular codes, of which \(8\) are reverse-complement invariant, and explicitly motivate extending their study to larger alphabets. Pellegrini and Pirillo (2014) describe maximum-size circular codes for arbitrary finite alphabet sizes, which covers the unrestricted structural extremum but not the six-letter *all-cardinalities* strand-closed histogram or symmetry quotient. Michel, Pellegrini, and Pirillo (2015) classify maximal four-letter circular codes. Fimmel, Michel, and Strüngmann (2016) establish the directed graph/acyclicity criterion, which is used rather than claimed as new here. The present result is the full cardinality distribution and the \(220\)-class symmetry classification for the first even alphabet beyond the four genetic letters with a third prescribed complementary pair.

## Limitations

The enumeration is exact for six labeled symbols with a fixed-point-free involution and dinucleotide codewords; it makes no claim about alphabets of eight or more symbols, longer codewords, biological performance, or error-correction capacity. The empty set is counted solely by an explicit convention. The maximum-size figure alone is not claimed as a new general theorem. The novelty comparison is based on inspected accessible primary material and targeted source searches; an unindexed historical six-letter census remains possible. Independent external scientific assessment has not been performed.

## References

- C. J. Michel and G. Pirillo, *Dinucleotide Circular Codes*, ISRN Biomathematics (2013), DOI: 10.1155/2013/538631, first published 2013-02-12. https://doi.org/10.1155/2013/538631
- M. Pellegrini and G. Pirillo, *On the dinucleotide circular codes of maximum cardinality*, Rivista di Biologia 107 (2014), pp. 89–95, publicly described at https://www.researchgate.net/publication/275834814_On_the_dinucleotide_circular_codes_of_maximum_cardinality
- C. J. Michel, M. Pellegrini, and G. Pirillo, *Maximal dinucleotide and trinucleotide circular codes*, Journal of Theoretical Biology 389 (2016), pp. 40–46, online 2015-09-14, DOI: 10.1016/j.jtbi.2015.08.029. https://doi.org/10.1016/j.jtbi.2015.08.029
- E. Fimmel, C. J. Michel, and L. Strüngmann, *n-Nucleotide circular codes in graph theory*, Philosophical Transactions A 374 (2016), 20150058, online 2016-02-09, DOI: 10.1098/rsta.2015.0058. https://doi.org/10.1098/rsta.2015.0058
