# Global two-gram rigidity of labeled noncrossing double-occurrence words

## Finding
For every integer \(n\ge 1\), let \(D_n\) be the indexed linear words on the fixed labeled alphabet \(\{1,\ldots,n\}\) in which every label occurs exactly twice. Let \(N_n\subseteq D_n\) be the words in which distinct labels never interlace as \(a,b,a,b\) or \(b,a,b,a\). For a word \(w\), define the *directed, multiplicity-preserving adjacent-pair spectrum* by
\[
B(w)_{ab}=\#\{i:1\le i<2n,\ (w_i,w_{i+1})=(a,b)\},\qquad a,b\in\{1,\ldots,n\}.
\]
**Global rigidity theorem.** For every \(n\ge1\), every \(w\in N_n\), and every \(v\in D_n\),
\[
B(v)=B(w)\quad\Longrightarrow\quad v=w.
\]
In particular, an explicit recursive algorithm reconstructs \(w\) from this spectrum without even needing to impose the noninterlacing promise on competing source words. The number of distinct achievable spectra on the noninterlacing source, and its exact maximum zero-error readout code size, equal
\[
|N_n|=n!C_n=\frac{(2n)!}{(n+1)!},\qquad C_n=\frac1{n+1}\binom{2n}{n}.
\]
The corresponding injectivity statement for the unrestricted source \(D_n\) holds for \(n\le2\), but fails for all \(n\ge3\). At \(n=3\), distinct words \(311232\) and \(323112\) both yield exactly the five ordered pairs \(31,11,12,23,32\), each once. Additional consecutive new-label doublets preserve these collisions at every greater order. For \(n\ge2\), single-letter counts alone are identical for every source word, so two is the least consecutive-factor length at which global rigidity of \(N_n\) is possible.

## Assumptions and scope
All words are *linear and indexed*, not cyclic and not taken up to relabeling or reversal. Labels are known to be distinct, with two occurrences of each. Observations include orientation and multiplicity of every contiguous factor of length two. The source is the full noninterlacing class \(N_n\), equivalently labeled noncrossing matchings on \(2n\) ordered positions. Competing reconstructions are allowed from the larger unrestricted double-occurrence class \(D_n\). There is no noise, deletion, or hidden start position.

## Proof
**Lemma 1 (removable pair).** Every nonempty noninterlacing double-occurrence word has a contiguous factor \(aa\), and after removing such a factor the remaining word is again noninterlacing.

Indeed, view occurrences of each symbol as matched endpoints of an interval. Among the finitely many intervals choose one of minimum length. If its endpoints are nonadjacent, the first symbol strictly between them has its partner inside: otherwise its arc interlaces the chosen arc. This would give a shorter matching interval, contradiction. Thus an adjacent pair exists. Deletion of two occurrences of one label cannot introduce any interlacing between remaining labels.

**Lemma 2 (spectral deletion).** Suppose \(u\in D_n\) contains the adjacent pair \(aa\). Its bigram multiplicity \(B(u)_{aa}\) is exactly one, because there are only two copies of \(a\). The pair has a unique exterior predecessor \(p\), unless it begins the word, and a unique exterior successor \(q\), unless it ends the word. Those neighbor labels and the boundary cases are determined solely by \(B(u)\): they are respectively the unique nonloop edge entering \(a\) and leaving \(a\). Removing \(aa\) changes the spectral counts by deleting \(aa\), any existing \(pa\), any existing \(aq\), and—if both neighbors exist—adding \(pq\). Hence the spectrum of the reduced word is determined by \(B(u)\) alone.

**Lemma 3 (nonrepeated directed bigrams).** Every oriented adjacent pair in a word from \(N_n\) occurs at most once. The case \(aa\) is immediate because the source has two occurrences of \(a\). For distinct \(a,b\), two disjoint occurrences of the adjacent factor \(ab\) force \(a,b,a,b\) at strictly increasing positions, forbidden by definition.

**Induction.** We prove the global rigidity for all \(n\). For \(n=1\) the only double-occurrence word is \(11\). Suppose the theorem holds for \(n-1\) distinct labels (the induction property is invariant under bijective relabeling). Fix \(w\in N_n\), and take a label \(a\) that appears as \(aa\), which exists by Lemma 1. If \(v\in D_n\) has \(B(v)=B(w)\), the positive loop count \(B(w)_{aa}=1\) forces \(aa\) to be adjacent also in \(v\). By Lemma 2 their respective exterior neighbors and their reduced spectra agree. The reduced word \(w'\) is noninterlacing; the reduced competitor \(v'\) is an arbitrary double-occurrence word. By induction, \(v'=w'\). Recovering \(w\) from \(w'\), insert \(aa\) at the known beginning or end if a boundary neighbor is absent. Otherwise insert between an occurrence of the known ordered pair \(pq\); by Lemma 3 there is exactly one such occurrence in \(w'\). Thus the insertion is forced, so \(v=w\). This proves global rigidity without requiring the competitor to be noninterlacing.

**Constructive decoder.** Starting with a valid spectrum, select the smallest label with positive loop count, determine its exterior predecessor/successor from the unique nonloop incoming/outgoing edges, apply the edge-count update from Lemma 2, recursively decode the smaller spectrum, and reinsert the pair at the unique indicated edge or boundary. The proof establishes correctness at every recursive stage for spectra arising from \(N_n\). A direct implementation uses polynomially many elementary operations.

**Exact capacity and sharp boundary.** Noninterlacing matchings of \(2n\) ordered positions are in bijection with Dyck paths of semilength \(n\). Assigning the \(n\) distinct labels to the pairs gives exactly \(n!C_n\) different words. Because no two such words have the same spectrum, every source word may be included in a zero-error reconstruction code. For unrestricted words at \(n\le2\), the complete list has one or six elements and all their spectra differ (or directly inspect the six words \(1122,1212,1221,2112,2121,2211\)). At \(n=3\), the two distinct words \(311232\) and \(323112\) have identical directed length-two spectra. Appending \(44,55,\ldots,nn\) to both words changes the spectrum only by their common trailing boundary and the shared additional doublets, preserving the collision for every \(n>3\). The matching total of \(2n\) letter counts contains no information about arrangement for \(n\ge2\).

## Verification
The bundled stand-alone Python 3 program `verify_noncrossing_bigram.py` enumerates labeled noncrossing words independently from the Catalan/Dyck decomposition and tests the spectrum-only recursive decoder for all source words through \(n=6\). It checks all unrestricted double-occurrence words and their entire profile fibers through \(n=5\), confirming that every noncrossing source has an unrestricted singleton fiber and that unrestricted collisions first arise at \(n=3\). The tested noncrossing source cardinalities are \(1,4,30,336,5040,95040\) for \(n=1,\ldots,6\). The bounded enumerations are consistency tests, **not** the argument proving the infinite theorem. Reproduce with `python3 verify_noncrossing_bigram.py`; the exact output is bundled as `verification_output.txt`.

## Relationship to prior work
The adjacent-pair readout is a finite-word form of the \(2\)-Abelian invariant introduced in Karhumäki–Saarela–Zamboni (2013). That work develops general equivalence and complexity, but does not state a global singleton-fiber theorem for labeled noninterlacing double-occurrence words. Brualdi–Dahl (2024), in its open-access treatment of quasi-Stirling multipermutations, describes the noninterlacing class through the forbidden patterns \(1212\) and \(2121\), and studies other reconstruction statistics including inversion multisets; an inversion multiset is not the adjacent-pair histogram. Cruz and collaborators (2018) study equivalent double-occurrence words under insertion and relabeling, not this fixed-labeled directed adjacent-pair readout. The Catalan count of noncrossing pair matchings and the above general concepts are established background, not asserted new. The proposed result is specifically the *global* uniqueness theorem against all unrestricted competitors and its recursive decoder and sharp contrast with unrestricted double-occurrence words.

## Limitations
The source must be a *linear, labeled* word with **exactly two copies of every distinct label**; the observation must retain direction and exact multiplicity of every adjacent pair. The proof does not cover cyclic spectra, read errors, arbitrary bounded symbol multiplicities, or forgetting orientations. It does not imply every crossing word is ambiguous: the exhibited collision proves only that full unrestricted injectivity fails sharply. The historical novelty assessment is not an independent review; an unindexed previous equivalent result may exist.

## References
1. J. Karhumäki, A. Saarela, L. Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, publicly posted 2013-01-22, https://arxiv.org/abs/1301.5104 .
2. R. A. Brualdi, G. Dahl, *Multipermutations and Stirling Multipermutations*, *Graphs and Combinatorics* 40 (2024), https://doi.org/10.1007/s00373-024-02751-2 .
3. R. Cruz and collaborators, *Insertions Yielding Equivalent Double Occurrence Words*, 2018 preprint, https://arxiv.org/abs/1811.11739 .
