# Global two-gram singleton boundary for nonnesting double-occurrence words

## Finding
Fix an integer \(n\ge 1\) and an alphabet \(\Sigma\) of \(n\) distinct labeled letters. Let \(D_n\) be the words of length \(2n\) in which every letter occurs twice. A word is *nonnesting* if it has no two distinct letters in the order \(a,b,b,a\). Define its two-gram observation \(H(w)\) to consist of the multiplicity of every oriented contiguous factor of length one or two. The *global fiber* of \(w\) contains all words, without a nonnesting restriction, with the same observation.

**Theorem.** For every nonnesting \(w\in D_n\), the following conditions are equivalent:

1. The global fiber of \(H(w)\) contains only \(w\).
2. The interlacement graph of \(w\) is a disjoint union of cliques (equivalently, it contains no induced path on three vertices).
3. There is a unique sequence of nonempty, disjoint labeled blocks \(B_1,\ldots,B_m\), each listing distinct letters, such that \(w=B_1B_1B_2B_2\cdots B_mB_m\). The order of all letters in the blocks is a permutation of \(\Sigma\).
4. The Dyck path recording first and second occurrences is a concatenation of mountain excursions \(U^{r_1}D^{r_1}\cdots U^{r_m}D^{r_m}\) with \(r_i\ge 1\) and \(\sum_i r_i=n\).

The number of globally uniquely reconstructible nonnesting words is exactly
\[
\boxed{n!\,2^{n-1}}.
\]
The nonnesting source contains \(n!C_n\) words, with \(C_n=\frac1{n+1}\binom{2n}{n}\), so its exact global singleton fraction is \(2^{n-1}/C_n\), asymptotic to \(\sqrt{\pi}\,n^{3/2}/2^{n+1}\).

## Assumptions and scope
Words are linear, indexed, and oriented; no identification under reversal, rotation, or relabeling is made. Each letter occurs **exactly twice**, and labels remain distinguishable. An observation counts adjacent ordered factors with overlaps, and also counts single-letter factors (the latter fix the content). A competitor can be any word over the same alphabet, not necessarily nonnesting; equality of all counts forces it to lie in \(D_n\). This theorem concerns read lengths one and two, not scattered subsequences, unordered pairs, circular spectra, or deletion channels. The case \(n=1\) is included.

For distinct letters \(a,b\), call them *interlaced* if their occurrences have order \(a,b,a,b\) or \(b,a,b,a\). Their interlacement graph has an edge between every interlaced pair. A Dyck word uses \(U\) for the first occurrence of each letter and \(D\) for its second occurrence. The first occurrences can be read as a permutation \(\sigma\) of \(\Sigma\).

## Proof

**1. FIFO encoding.** In a nonnesting word, if the first occurrence of \(a\) precedes the first occurrence of \(b\), then the second occurrence of \(a\) precedes the second occurrence of \(b\); otherwise these four positions form a forbidden nesting. Conversely this ordering of second occurrences excludes all nestings. Thus a nonnesting word is uniquely given by a Dyck path and a permutation \(\sigma\): assign successive \(U\) steps the letters of \(\sigma\), and assign successive \(D\) steps the same letters in that order. The Dyck condition holds because each second occurrence follows its first. In particular there are \(n!C_n\) such words.

**2. Mountain paths and clique components.** A primitive Dyck excursion consisting of \(U^rD^r\) gives the factor \(BB\), where \(B\) is the list of the \(r\) letters whose first occurrences appear in that excursion. Every two distinct letters in \(B\) interlace, and letters in different excursions do not. Hence a concatenation of mountains has an interlacement graph which is a disjoint union of cliques.

Conversely, suppose a primitive excursion is not a mountain. Its initial ascent and first subsequent descent have shape \(U^pD^qU\), with \(1\le q<p\). Let \(a\) be the first opened letter, \(b\) the \(p\)-th opened letter, and \(c\) the next newly opened letter. FIFO closing gives \(a_1<b_1<a_2<b_2\) and \(b_1<c_1<b_2<c_2\), whereas \(a_2<c_1\). Therefore \(a,b,c\) induce precisely the interlacement edges \(ab\) and \(bc\), with no \(ac\). The graph is not a disjoint union of cliques. This proves the equivalence of conditions 2–4.

**3. Every mountain concatenation is globally rigid.** Write \(w=B_1B_1\cdots B_mB_m\), with \(B_j=x_{j,1}\cdots x_{j,r_j}\), all letters distinct across blocks. Its directed adjacent-pair multigraph contains, inside block \(j\), exactly two arcs \(x_{j,i}\to x_{j,i+1}\) for each \(i<r_j\) and one closing arc \(x_{j,r_j}\to x_{j,1}\). When \(r_j=1\) the closing arc is a loop. Between consecutive blocks there is precisely one bridge \(x_{j,r_j}\to x_{j+1,1}\). There are no other interblock arcs.

Any word with the same observation is an Euler trail through this fixed directed multigraph, with parallel copies indistinguishable. For \(n\ge2\), the starting and ending letters are uniquely specified by the nonzero out-minus-in degree and in-minus-out degree: they are the first letter of \(B_1\) and the last letter of \(B_m\), which are distinct. The bridges must be traversed from left to right, and all internal arcs of a block must be used before leaving it because no arc returns to that block. Within a block, every \(x_{j,i}\) for \(i<r_j\) can only lead to \(x_{j,i+1}\). At \(x_{j,r_j}\), the closing arc must be taken before the bridge (or before ending the trail) or the unused cycle would become inaccessible. Consequently the only possible local traversal spells \(B_jB_j\), and concatenating them recovers \(w\). For \(n=1\), the sole word is the double letter. Thus conditions 3–4 imply 1.

**4. Every other nonnesting word admits a distinct global competitor.** An elementary directed-spectrum switch applies whenever a word factors as
\[
P\,a\,B\,b\,C\,a\,D\,b\,S
\quad\longleftrightarrow\quad
P\,a\,D\,b\,C\,a\,B\,b\,S.
\]
Here \(a,b\) are distinct and occur at precisely the displayed positions; \(B,C,D,P,S\) are arbitrary intervening factors. Both sides have exactly the same symbol counts and oriented adjacent-pair multiplicities: the two paths from \(a\) to \(b\), through \(B\) and \(D\), merely exchange their order; all other boundaries and internal adjacencies are unchanged. If \(B\ne D\), the words differ.

For the nonmountain primitive excursion in step 2, use \(a\) and \(b\) from its initial ascent \(U^p\). The factor \(B\) between their first occurrences consists of the other newly opened letters of this ascent. The factor \(D\) between their second occurrences includes the later newly opened letter \(c\), which does not occur in \(B\). Hence \(B\ne D\), and the switch produces a distinct competing word of the same complete two-gram observation. Therefore condition 1 implies 4.

**5. Exact enumeration.** With a fixed first-occurrence permutation \(\sigma\), a mountain concatenation is uniquely described by the ordered composition \((r_1,\dots,r_m)\) of \(n\). There are \(2^{n-1}\) such compositions, independently of the \(n!\) labeled permutations. Every such word is globally rigid by step 3, and no other nonnesting word is rigid by step 4. The exact count follows. Finally the stated proportion and its asymptotic follow from \(C_n\sim 4^n/(\sqrt{\pi}n^{3/2})\).

For a minimal ambiguous example, \(w=121323\) is nonnesting but has a nonmountain Dyck shape; \(w'=132123\) is distinct and has the same oriented adjacent-pair multiset \(\{12,21,13,32,23\}\). In contrast, \(1212\) is a rigid nonnesting word that is *not* noncrossing.

## Verification
Run `python3 check.py` with Python 3. The program enumerates all nonnesting words through \(n=6\), computes each complete global fiber size independently by a directed arborescence/BEST count, and compares its singleton indicator with the mountain criterion. For \(n\le5\), it also exhaustively enumerates all unrestricted double-occurrence words and confirms the arborescence fiber counts. The resulting singleton counts for \(n=1,2,3,4,5,6\) are \(1,4,24,192,1920,23040\).

Run `python3 check_switch.py` in the same directory. For every canonical FIFO matching represented by every Dyck path through \(n=9\), this separate checker either finds an explicit distinct word with equal adjacent-pair and letter spectra or verifies the mountain condition. Computation checks small instances only; the all-length conclusion comes from the proof above.

## Relationship to prior work
Karhumäki, Saarela and Zamboni formalized \(k\)-Abelian equivalence, including the adjacent-factor formulation used here, and studied complexity and periodicity of infinite words. Shtylla, Traldi and Zulli studied double-occurrence words and their interlacement graphs for a different, planar-realizability problem. Albert and Bouvel studied Catalan structures and avoidance-based Wilf equivalence. Their methods provide nearby language and structural context, but the inspected texts do not state this global reconstruction boundary.

The numerical sequence \(n!2^{n-1}\) is previously recorded as [OEIS A002866](https://oeis.org/A002866), for example as the count of ordered sequences of nonempty lists on a labeled set. No novelty is claimed for that integer sequence or for its composition enumeration. The new assertion is that it counts precisely the globally two-gram reconstructible **nonnesting** double-occurrence words, with the sharp induced-path obstruction and explicit ambiguity switch.

The theorem is distinct from a related global rigidity statement for **noncrossing** double-occurrence words: nonnesting and noncrossing are different Catalan families, and the word \(1212\), included here, is excluded from that statement. The new theorem also classifies precisely which nonnesting words fail global reconstruction; it is not implied by the count of Catalan matchings or by unrestricted 2-Abelian class enumeration alone.

## Limitations
This is a self-review, not independent expert validation. The theorem classifies global singleton fibers **among sources that are nonnesting**; it does not enumerate all globally singleton unrestricted double-occurrence words, nor all fiber sizes of nonnesting sources. Existing general Euler-trail facts, Catalan enumeration, and the independently tabulated numerical sequence OEIS A002866 are ingredients, not new results. A previously unpublished or unindexed equivalent reconstruction theorem may exist. The computational checks cannot replace the proof at unbounded \(n\).

## References
- B. Shtylla, L. Traldi, L. Zulli, *On the Realization of Double Occurrence Words*, arXiv:0709.2933v1, 18 September 2007, https://arxiv.org/html/0709.2933v1.
- J. Karhumäki, A. Saarela, L. Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, arXiv:1301.5104v1, 22 January 2013, https://arxiv.org/html/1301.5104v1.
- M. Albert, M. Bouvel, *A general theory of Wilf-equivalence for Catalan structures*, arXiv:1407.8261v1, 31 July 2014, https://arxiv.org/abs/1407.8261.
- OEIS Foundation, *A002866*, previously tabulated sequence \(a(n)=2^{n-1}n!\), with dated contributions from 2000 onward, https://oeis.org/A002866.
