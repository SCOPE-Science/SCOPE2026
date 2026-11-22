# Sharp q-ary one-deletion trigram-profile capacity and saturation witnesses

## Finding
Let \(\Sigma\) be a fixed alphabet with \(q\ge3\) symbols. For a finite word \(w\), let \(H_3(w)\in\mathbb N^{\Sigma^3}\) count overlapping **contiguous** occurrences of every oriented three-symbol factor, and let \(w^{\setminus i}\) denote the word obtained by deleting position \(i\). Then, for every \(w\),
\[
\left|\{H_3(w^{\setminus i}):1\le i\le |w|\}\right|
\le M_q:=q^5-2q^4+2q^3-3q^2+3q+4.
\]
The bound is sharp **at every word length** \(n\ge q^5+12\). In particular \(M_3=121\), \(M_4=608\), and \(M_5=2069\). If \(s_q\) is the first length at which the bound is attained, then
\[
M_q\le s_q\le q^5+12,\qquad s_q/q^5\longrightarrow1\quad(q\to\infty).
\]
No claim that the displayed upper bound for \(s_q\) is the exact first-attainment length is made.

## Assumptions and scope
The histogram is an **oriented, multiplicity-preserving** three-mer profile, not a scattered-subsequence deck, unordered-composition profile, or the sequence of raw deletion descendants. All positions are indexed within the original linear word; a deletion removes exactly one symbol and there are no cyclic wrap-around factors. For words shorter than three symbols the trigram histogram is zero. The novel all-alphabet assertion concerns \(q\ge3\); the binary specialization \(M_2=14\) is included solely as a consistency check against earlier binary work.

## Proof
Write \(e_{abc}\) for the coordinate unit vector of the oriented trigram \(abc\). At an interior position with two symbols on both sides, the five-symbol neighborhood is \(abcde\), with \(c\) deleted. Its histogram change is exactly
\[
\Delta(abcde)=e_{abd}+e_{bde}-e_{abc}-e_{bcd}-e_{cde}.
\]
Let \(\mathcal D_q\) denote the **set of distinct** such signed vectors as \(abcde\) runs through \(\Sigma^5\). Each vector has total coordinate sum \(-1\), so it has nonempty symbol support. For any vector supported on a nonempty subset \(S\subseteq\Sigma\), any realizing five-tuple may be relabeled by a map fixing \(S\) and sending every letter outside \(S\) into \(S\). Since forming signed trigram histograms commutes with relabeling, the resulting five-tuple over \(S\) realizes exactly the same vector. Therefore the number of vectors whose symbol support is any prescribed \(k\)-element set is independent of the ambient alphabet, and \(k\le5\).

The exhaustive, constant-size equality-pattern census has the following counts for full support of a fixed set of \(k\) letters:

| \(k\) | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| Distinct \(\Delta\)-vectors supported on all \(k\) letters | 1 | 8 | 90 | 192 | 120 |

These integers are finite mathematical certificates, not asymptotic guesses: `verify_local.py` enumerates **all** \(k^5\) five-tuples for each \(1\le k\le5\), forms the signed histogram by direct subtraction, extracts exact nonzero-coordinate symbol support, and deduplicates the vectors. The complete executable census and output are included. Consequently
\[
|\mathcal D_q|=q+8\binom q2+90\binom q3+192\binom q4+120\binom q5
=q^5-2q^4+2q^3-3q^2+3q.
\]
For a word of length at least five, every deletion except the first two and last two has one of these changes. At most four additional changes arise at the boundary. For a shorter word, there are fewer than five deletion positions. Translation by the original histogram is injective on the signed changes, so these observations give the universal bound \(|\mathcal D_q|+4=M_q\).

To attain it, choose any linearization \(B_q\) of a \(q\)-ary de Bruijn cycle of order five: it has length \(q^5+4\) and contains every five-tuple as a contiguous factor. For \(q\ge3\), form
\[
W_q=\mathtt{0100}\;B_q\;\mathtt{0012}.
\]
This word has length \(q^5+12\). Every interior vector from \(\mathcal D_q\) occurs at the middle of some length-five factor of \(B_q\). Its four boundary changes, from the first, second, penultimate and last positions, are, respectively,
\[
-e_{010},\quad e_{000}-e_{010}-e_{100},\quad
-e_{001}+e_{002}-e_{012},\quad -e_{012}.
\]
They are pairwise different and all lie outside \(\mathcal D_q\). For completeness, this disjointness can be checked exhaustively over the three-symbol alphabet; the support-collapsing argument already proved shows that a purported realization using extra alphabet symbols would induce a realization using only \(0,1,2\), which does not exist. The exact check is in `verify_local.py`. Thus \(W_q\) attains \(|\mathcal D_q|+4\). Inserting any number of copies of \(0\) immediately before the final four symbols preserves both boundary patterns and all five-factors within \(B_q\), proving sharpness for all greater lengths.

Finally, a word of length \(n\) has at most \(n\) deletion outcomes. Hence \(s_q\ge M_q\); combining with the construction and the displayed polynomial establishes \(s_q/q^5\to1\).

## Verification
Run `python3 verify_local.py` and `python3 verify_global.py` with Python 3 and no external packages. The first independently computes the five full-support signature counts and all boundary noncollision tests; it also recomputes \(|\mathcal D_q|\) for \(2\le q\le6\). The second generates de Bruijn words and **directly recomputes complete three-gram histograms after every deletion** of the four explicit witness words for \(q=2,3,4,5\); measured outcomes equal \(14,121,608,2069\). Their actual outputs are included. These finite checks establish the table and sample witnesses; the relabeling and covering arguments, rather than finite sampling in \(q\), give the infinite-alphabet proof.

## Relationship to prior work
En Gad's publicly dated 2026 work on linear hashes of substring counts motivates understanding how deletion operations perturb fixed-length read-frequency vectors; its advertised conclusions are coding-rate bounds, not this exact one-deletion three-mer capacity. The established binary one-deletion three-mer capacity \(14\) is recovered, but it is not independently claimed as new. Kiah–Puleo–Milenkovic formalized \(q\)-ary length-\(\ell\) profile-vector channels and global profile enumeration, but the inspected model and results do not give the sharp one-source deletion image of oriented three-mers. Work on cyclic or linear three-mer profile enumeration counts **all realizable profiles at fixed word length**, a different quantity from the profiles produced by deleting one position of a **single fixed word**. De Bruijn universal cycles supply a factor-covering construction, but without the signed-difference census they do not imply the maximum \(M_q\).

## Limitations
The exact earliest saturation length \(s_q\) is not determined for \(q\ge3\); the established interval is stated above. The proof concerns exactly one deletion, linear words, and oriented contiguous trigrams only. The finite signature census is reproducible but requires checking its short code; no independent formal proof assistant or third-party audit was used. The full text of the 2026 substring-count hashing preprint was not accessible during the comparison, leaving a limited residual risk of an unindexed equivalent or subsidiary statement; no scientific priority beyond inspected evidence is claimed.

## References
- H. M. Kiah, G. J. Puleo and O. Milenkovic, *Codes for DNA Sequence Profiles*, IEEE Transactions on Information Theory 62 (2016), 3125–3146, https://www3.ntu.edu.sg/home/hmkiah/docs/papers/DNASeqProfile.pdf .
- E. En Gad, *Polynomially larger deletion codes by linear hashing of substring counts*, arXiv:2609.19493, first submitted 2026-09-16, https://arxiv.org/abs/2609.19493 .
- Z. Ye and G. Ge, *Substring Edit Correcting Codes and Optimal Single Burst-Deletion Correcting Codes*, arXiv:2610.05696, first submitted 2026-10-05, https://arxiv.org/abs/2610.05696 .
- D. Gabric, W. Imam, L. J. Jones and J. Sawada, *Decoding universal cycles for t-subsets and t-multisets by decoding bounded-weight de Bruijn sequences*, arXiv:2603.11934, first submitted 2026-03-12, https://arxiv.org/abs/2603.11934 .
