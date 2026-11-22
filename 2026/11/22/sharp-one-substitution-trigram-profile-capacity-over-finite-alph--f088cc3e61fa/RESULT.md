# Sharp one-substitution trigram-profile capacity over finite alphabets

## Finding

Let \(q\ge2\) and \(n\ge5\). For a word \(w\in\Sigma^n\) on a labeled alphabet of \(q\) symbols, let \(H_3(w)\) be the vector recording the number of occurrences of each oriented, overlapping length-three factor. Let \(B_q(w)\) count the distinct vectors \(H_3(v)\) obtainable by replacing exactly one position of \(w\) with a different symbol. Then
\[
 B_q(w)\le (q-1)(q^5-q^2-4q+4).
\]
The bound is attained for every \(n\ge q^5+4\); in particular, the all-length maximum is exactly
\[
 M_q=(q-1)(q^5-q^2-4q+4).
\]
For \(q=2,3,4,5\), the maxima are \(24,452,2988,12336\), respectively. If \(N_q\) is the smallest source length at which equality occurs, then
\[
 q^5-q^2-4q+4\le N_q\le q^5+4,
\]
so \(N_q=q^5+O(q^2)\) as \(q\to\infty\). The exact \(N_q\) is not determined here.

## Assumptions and scope

Letters are distinct labeled symbols; sequences are **linear**, not circular. Every substitution must change one letter and leaves the length unchanged. A profile is a complete \(q^3\)-coordinate multiplicity vector, not an ordered read list, an unordered composition profile, or the altered word itself. \(B_q(w)\) counts distinct observations, not edit histories. The result requires \(n\ge5\) for its four nonoverlapping boundary-center types; smaller lengths are excluded.

Write \(e_{abc}\) for the unit vector indexed by the ordered triple \((a,b,c)\). For an interior substitution with context \(abcde\), replacing center \(c\) by \(f\ne c\) changes the profile by
\[
 \Delta(a,b,c,d,e;f)=e_{abf}+e_{bfd}+e_{fde}-e_{abc}-e_{bcd}-e_{cde}.
\]
All the vectors considered have zero coordinate sum. Equality of resulting profiles from one fixed source is equivalent to equality of these difference vectors.

## Proof

**1. Universal local collision certificate.** A length-five window and a distinct replacement have \(q^5(q-1)\) possible indexed parameter tuples. The exact finite-support lemma proved in `verify_symbolic.py` says that (a) each distinct letter appearing in \((a,b,c,d,e,f)\) occurs in a nonzero-coordinate triple of \(\Delta\); (b) no difference vector has a fiber larger than two; and (c) all double fibers arise, under injective renaming of their letters, from the following seven pairs of tuples, written as six-symbol strings \((a,b,c,d,e,f)\):

```
000011  ~  100001
000101  ~  010001
000111  ~  110001
001010  ~  101000
001100  ~  011000
010011  ~  100101
010122  ~  210102
```

The first six types each have two distinct letters and give exactly \(q(q-1)\) double fibers; the seventh has three distinct letters and gives exactly \(q(q-1)(q-2)\). Thus the number of **distinct interior** substitution changes is
\[
 I_q=q^5(q-1)-6q(q-1)-q(q-1)(q-2)=q(q-1)(q^4-q-4).
\]

For completeness, the finite lemma is valid **for every alphabet size**, not merely for six letters. Any operation touches at most six distinct symbols. Item (a) ensures that two equal difference vectors have identical supports, hence that their combined operation symbols use at most six letters. Relabel these letters injectively into a six-symbol alphabet. Such relabeling preserves and reflects equality of vectors. The provided finite verifier enumerates exactly all \(6^5(6-1)=38880\) operations, constructs the full signed-coordinate differences, checks item (a), establishes \(38280\) singleton and \(300\) double fibers with no larger ones, and canonicalizes all double fibers into precisely the seven patterns displayed above. Consequently this is an exhaustive bounded-support proof of the all-\(q\) identities, not an inference from small-\(q\) experiments.

**2. Four boundary types.** For \(n\ge5\), substitution at the first position changes one trigram, at the second changes two, at the next-to-last changes two, and at the last changes one. The finite certificate also checks that each such signed vector has all its participating symbols visible in the nonzero-coordinate support, and that the four boundary-type vector sets are mutually disjoint and disjoint from the interior vector set. Every boundary type is generated using at most five input/replacement symbols. Consequently the same six-symbol relabeling argument proves the boundary disjointness universally. Each boundary position has exactly \(q-1\) distinct changes (the new symbol identifies a positive triple). Hence
\[
 B_q(w)\le I_q+4(q-1)=(q-1)(q^5-q^2-4q+4).
\]

**3. Attaining the bound.** By the standard de Bruijn/Euler-circuit construction, for every \(q\) a cyclic word exists containing every \(q\)-ary length-five word exactly once. Linearize it by appending its first four letters, obtaining a word of length \(q^5+4\). Each of the \(q^5\) five-letter contexts appears at an interior position, so all \(I_q\) interior changes occur for each permitted replacement. Its four boundary positions give an additional \(4(q-1)\) distinct changes by step 2. This proves sharpness. Appending copies of the last letter preserves the original five-factor coverage and therefore every interior difference, while the four new boundary types still contribute the same disjoint \(4(q-1)\); sharpness persists for all longer lengths.

**4. First-attainment bracket.** The \(n\) source positions each allow only \(q-1\) changes, hence \(B_q(w)\le n(q-1)\). Combining this with \(B_q(w)=M_q\) yields \(n\ge q^5-q^2-4q+4\). The construction in step 3 gives \(n\le q^5+4\), proving the stated bracket.

## Verification

`verify_symbolic.py` is a terminating, self-contained exact certificate over six abstract symbols, covering \(38880\) genuine interior parameter tuples and all four boundary forms. It checks the full signed vectors, support recovery, exact collision fibers, seven canonical templates, and all boundary intersections. `verify_direct.py` separately computes entire trigram histograms of substituted words, verifies the de Bruijn construction for alphabets of size two through four, and exhausts all \(2048\) binary words of length eleven, \(2187\) ternary words of length seven, and \(4096\) quaternary words of length six. It also checks padding and confirms the local difference against direct profile subtraction. Their actual replay results are in `verification_outputs.txt`; neither bounded sample enumeration is used as a substitute for the alphabet-independent proof.

## Relationship to prior work

Kiah, Puleo and Milenkovic (2016) study DNA sequence profiles and the bounded local effect of edit errors on overlapping read counts, rather than enumerating the exact set of all one-substitution profile observations from one source. En Gad (2026) uses substring-count differences and their linear dependence to construct deletion/mixed-edit correcting codes; the relevant preprint material inspected does not state a sharp alphabet-uniform trigram substitution observation count or classify the seven collision types. An analogous two-gram substitution problem differs mathematically because one internal edit affects two ordered adjacent pairs instead of three overlapping trigrams. Results on globally realizable trigram profiles and on deletion spheres also do not imply this exact one-substitution ball-size formula.

## Limitations

The exact first maximizing length \(N_q\) is bracketed but not determined. Nothing is claimed about two or more substitutions, other factor lengths, cyclic words, or recovery of an underlying word. Equality classification beyond the explicit de Bruijn witnesses is not established. Historical priority remains subject to unindexed or otherwise uninspected equivalent work; related published sources and a material portion of the 2026 preprint were inspected, not every possible external document. The finite verifier is essential for the seven-template lemma, while the proofs transferring that certificate to arbitrary alphabets and obtaining sharpness are fully mathematical.

## References

1. H. M. Kiah, G. J. Puleo and O. Milenkovic, *Codes for DNA Sequence Profiles*, IEEE Transactions on Information Theory **62** (2016), 3125–3146, DOI:10.1109/TIT.2016.2555321; open manuscript: https://www3.ntu.edu.sg/home/hmkiah/docs/papers/DNASeqProfile.pdf.
2. E. En Gad, *Polynomially larger deletion codes by linear hashing of substring counts*, arXiv:2609.19493, first publicly posted 2026-09-16, https://arxiv.org/abs/2609.19493; revised preprint inspected at https://pdfs.assets.alphaxiv.org/2609.19493v2.pdf.
3. N. G. de Bruijn, *A combinatorial problem*, Koninklijke Nederlandse Akademie van Wetenschappen, Proceedings **49** (1946), 758–764; standard universal-word construction used only for existence of de Bruijn sequences.
