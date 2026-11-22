# All smallest suffixient sets of sentinel-terminated distinct-run powers

## Finding

Let \(q\ge2\), let \(a_0,\ldots,a_{q-1}\) be pairwise distinct letters, and let \(r_0,\ldots,r_{q-1}\ge2\) and \(k\ge2\) be integers. Put
\[
P=a_0^{r_0}\cdots a_{q-1}^{r_{q-1}},\quad T=P^k\#,\quad p=|P|,
\]
where \(\#\) is a new terminal letter, occurring only at the end. A substring \(u\) of \(T\), possibly empty, is *right-maximal* when it has two distinct right-following letters in \(T\). A *right extension* is a word \(ux\) for such \(u\) and a letter \(x\) immediately following one occurrence of \(u\). A *supermaximal right extension* (SRE) is a right extension that is not a proper suffix of any other right extension. A *suffixient set* is a set \(S\) of ending positions of \(T\) such that every right extension occurs ending at some position of \(S\). The minimum possible cardinality is \(\chi(T)\).

**Theorem (complete SRE and minimum-set census).** The complete list of SRE words consists exactly of
\[
\begin{array}{ll}
 a_i^{r_i}\text{ and }a_i^{r_i-1}a_{i+1},&0\le i<q-1,\\
 a_{q-1}^{r_{q-1}},&\\
 P^{k-1}a_0\text{ and }P^{k-1}\#.&
\end{array}
\]
The \(2q-1\) short SRE words each have exactly \(k\) occurrences, and the two long SRE words each have exactly one occurrence. Their sets of ending positions are pairwise disjoint. Consequently
\[
\boxed{\chi(T)=2q+1,\qquad \#\{\text{smallest suffixient position sets of }T\}=k^{2q-1}.}
\]
Every smallest suffixient set is obtained uniquely by choosing one ending position of each of the \(2q+1\) listed words. In particular the count is independent of all \(r_i\) in the stated non-singleton-run regime.

**Comparison with string attractors.** A string attractor meets an occurrence of each nonempty factor, without the right-maximality condition. For the same sentinel-terminated word \(T\), its minimum cardinality is \(q+1\). Thus the two minimum sizes differ by exactly \(q\) even though both are independent of \(k\) and of the run lengths. This comparison uses the standard cyclic-transition covering argument supplied below; it does not identify the two types of position sets.

## Assumptions and scope

The alphabet contains the \(q\) displayed letters and the extra marker \(\#\), which occurs **exactly once**. The word is linear, not circular. Positions are one-based and include the terminal position \(kp+1\). The statement covers arbitrary \(q\ge2\), \(k\ge2\), and independently chosen integer run lengths \(r_i\ge2\); it does not claim the same formula for singleton runs or unmarked words. The use of the terminal symbol is substantive: it creates the two long SRE words and forces the terminal position to be selected.

## Proof

**1. Right-maximality from the periodic phase.** Consider first \(P^\omega\). Because each letter occupies precisely one run per period and all letters are distinct, an occurrence of a factor containing two different letters identifies its cyclic phase: its first letter-change is an ordered pair \(a_i a_{i+1}\) (with cyclic subscripts), and that transition has a unique offset modulo \(p\). Thus all occurrences of a nonunary factor in \(P^\omega\) have the same follower. A unary factor \(a_i^t\), with \(1\le t<r_i\), has two follower choices: \(a_i\) inside a run and the cyclic successor at its end. A factor \(a_i^{r_i}\) has only the cyclic successor, except that the last run of the finite text is followed by the terminal marker.

In \(T=P^k\#\), a nonunary factor can therefore be right-maximal only if an occurrence ends immediately before the unique marker, thereby acquiring \(\#\) as an additional follower. Such a factor must be a suffix of \(P^k\), and to have another follower it must also occur earlier. Because its phase is fixed, such a repetition exists precisely when its length does not exceed \((k-1)p\); it is then a suffix of \(P^{k-1}\). Its two followers are \(a_0\) and \(\#\). This argument also applies to nonempty unary suffixes of the last run, while the empty factor is right-maximal because the text uses at least two letters.

**2. Maximal extensions under the suffix order.** For each \(i<q-1\), the unary word \(a_i^{r_i-1}\) has both followers \(a_i\) and \(a_{i+1}\), giving the two short extensions in the theorem. No longer right-maximal predecessor word can give either as a suffix: increasing its unary exponent reaches \(r_i\), which has only one follower, while prepending the preceding distinct letter fixes the cyclic phase and also gives a unique follower. This includes \(i=0\), since \(r_0\ge2\) means the long extension ending in \(a_0\) is not a suffix of \(a_0^{r_0}\).

For the final letter \(a_{q-1}\), the short word \(a_{q-1}^{r_{q-1}}\) is an extension of the right-maximal \(a_{q-1}^{r_{q-1}-1}\). It cannot be extended to the left while retaining right-maximality, by the same cyclic-phase argument. The remaining right extensions with follower \(a_0\) or \(\#\), arising from any suffix of the last run or any longer suffix repeated across the period boundary, are all suffixes of \(P^{k-1}a_0\) or \(P^{k-1}\#\), respectively. Both of these are right extensions of the right-maximal \(P^{k-1}\). They cannot be enlarged: a longer suffix of \(P^k\) occurs only once before the terminal marker, since its length exceeds \((k-1)p\). Finally the right extensions from the empty word are covered by one of the listed extensions, since every alphabet letter and the marker occurs as the last letter of a listed word. Therefore the displayed list is complete and consists of SRE words.

**3. Multiplicities and minimum position sets.** Each short word ends at one fixed offset inside each of the \(k\) periods. For \(i<q-1\), the end offsets of \(a_i^{r_i}\) and \(a_i^{r_i-1}a_{i+1}\) are, respectively, the last position of the \(i\)-th run and the first position of the next run. The end offset of \(a_{q-1}^{r_{q-1}}\) is the last position of the last run. All these \(2q-1\) offsets are distinct because every run has length at least two. Each short word hence has \(k\) endings; the long word \(P^{k-1}a_0\) ends at the first position of the last period, which is another offset, and \(P^{k-1}\#\) ends at the unique marker position. Their ending sets are pairwise disjoint.

Every suffixient set must contain at least one ending position for each SRE, because no distinct SRE can end at the same position: otherwise one would be a suffix of the other. Conversely, choosing one ending position of each SRE covers all right extensions, because every right extension is a suffix of some SRE. Thus the smallest sets have exactly one position per SRE, and disjointness of the ending sets makes those choices independent. There are \((k)^{2q-1}\cdot1\cdot1\) such sets and their cardinality is \(2q+1\).

**4. Attractor comparison.** Any string attractor of \(T\) must hit the \(q+1\) distinct one-letter factors, giving a lower bound \(q+1\). To attain it, in \(P^k\) select the last position of every letter-run in its first period. A factor consisting of one letter occurs so as to cover the chosen last position in that run. A nonunary factor of length at most \(p\) has a transition of some cyclic type, and a copy aligned with the corresponding transition in or immediately after the first period crosses a chosen last-run position. For a factor longer than \(p\), shift any occurrence leftward by integral multiples of \(p\) until its start lies in the first period; the resulting occurrence spans a complete period and hence meets a chosen last-run position. Together these \(q\) positions attract every factor of \(P^k\); adjoining the terminal position attracts every factor containing \(\#\). Therefore the bound \(q+1\) is attained.

## Verification

Run `python verify.py` with Python 3. The self-contained program constructs every literal factor of each tested \(T\), its right followers, the full right-extension set and the SREs independently of the symbolic classification. It checks SRE identities, occurrence multiplicities, disjoint ending sets and coverage. It also exhaustively enumerates **all** minimum-sized candidate position sets for four small examples and checks each predicted count directly. Its captured output is in `verify_output.txt`.

The test checked 246 parameter instances and 12,358 right extensions, including every tuple of run lengths from \(\{2,3,4\}\) for alphabet sizes two through four and repetition counts two and three; selected five- and six-symbol instances were added. These finite checks support, but are not substituted for, the proof for arbitrary parameters.

## Relationship to prior work

The source of the suffixient-set definition, supermaximal-right-extension characterization and online motivation is Köppl and Kucherov, *Smallest suffixient set maintenance in near-real-time* (first public 30 April 2026). Cenzato and coauthors give general constructions and structural results for suffixient arrays. Fujimaru, Navarro, Romana and Urbina study the suffixient-set repetitiveness measure, including a complete minimum-set classification for the separate Fibonacci family and upper bounds for episturmian factors. The inspected full texts do not give the explicit SRE list, minimum-set count or the marked distinct-run power comparison here.

A relevant existing result for the same \(P^k\) family classifies *string attractors*, not suffixient sets: the complete cyclic-bigram certificate and the number \(2k^{q-1}(k-1)\) of smallest attractors when all runs are non-singleton are already known. That result is not the present minimum-suffixient-set theorem; its position sets obey a different covering condition and generally have a different size and count. The unmarked cyclic-attractor formula is not claimed as new.

## Limitations

The result is sensitive to the extra terminal symbol and to the lower bound of two on every run length. Neither restriction may be dropped without a separate classification. The proof treats a single period comprising one contiguous run of every distinct letter, not arbitrary periodic words with repeated alphabet symbols in separated runs. The numerical checker covers finitely many instances; it cannot establish the infinite claim by itself. The literature and indexed comparisons do not exclude an unindexed equivalent theorem. No independent scientific audit has been performed.

## References

1. D. Köppl and G. Kucherov, *Smallest suffixient set maintenance in near-real-time*, arXiv:2604.27548v1 (30 April 2026), https://arxiv.org/abs/2604.27548 ; MFCS 2026, DOI 10.4230/LIPIcs.MFCS.2026.86.
2. D. Cenzato, L. Depuydt, T. Gagie, S.-H. Kim, G. Manzini, F. Olivares and N. Prezza, *Suffixient Arrays: A New Efficient Suffix Array Compression Technique*, Theory of Computing Systems 70 (2026), article 50, https://doi.org/10.1007/s00224-026-10287-6.
3. H. Fujimaru, G. Navarro, G. Romana and C. Urbina, *Smallest Suffixient Sets: Effectiveness, Resilience, and Calculation*, arXiv:2506.05638v7 (first public 5 June 2025), https://arxiv.org/html/2506.05638v7.
4. *Cyclic bigram certificates and all minimum attractors of distinct-run powers*, published research record (2 November 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-cyclic-bigram-certificates-and-all-minimum-attractors-of-distinc--7fb760d3d179 ; relevant statement in `RESULT.md`.
