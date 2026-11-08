# Sharp global four-deck obstruction for binary words with two one-runs

## Finding
For a binary word \(x\), let \(R(x)\) be the number of maximal runs of ones and let \(\mathcal D_4(x)\) be the multiset of all scattered length-four subsequences, retaining multiplicities. For every \(4\le n\le13\), no pair \(x,y\in\{0,1\}^n\) with \(R(x)\le2<R(y)\) has equal four-decks. At \(n=14\), exactly one such ordered pair exists:
\[
x=01111100111110,\qquad y=10101111110101.
\]
The pair has respectively two and five one-runs, and both words have the common multiplicity vector, ordered by binary patterns from \(0000\) through \(1111\),
\[
(1,5,15,30,15,50,85,140,5,25,50,100,30,100,140,210).
\]
For every \(n\ge14\), at least one such cross-class collision exists by adjoining the same zeros to this pair. In the standard length-at-least-deck-order convention, the upper bound on unrestricted-opponent reconstruction of the class \(\mathcal B_2=\{x:R(x)\le2\}\) is sharp: \(r(\mathcal B_2)=5\). The upper bound is the published theorem cited below; the new result supplies the missing lower bound and exact first obstruction.

## Assumptions and scope
All words are finite and binary. A scattered subsequence is selected at strictly increasing indices. The length-four deck is the sixteen-vector whose entry at a pattern is the number of four-index selections realizing that pattern. Deck equality is considered at equal word lengths \(n\ge4\). A one-run is a maximal nonempty consecutive block of ones; the zero word has no one-runs. The count of cross-class collision pairs orients the pair so that the first word has at most two one-runs and the second has more than two; no other symmetry identification is performed. The minimum deck order is interpreted for lengths at least that order, as required for nonempty deck observations.

## Proof
**Witness and common deck.** The first displayed word is \(0\,1^5\,0^2\,1^5\,0\), hence has two runs; the second is \(1\,0\,1\,0\,1^6\,0\,1\,0\,1\), hence has five. Directly counting every choice of four indices, grouping by the resulting pattern, produces the displayed sixteen integers for each word. The entries sum to \(1001=\binom{14}{4}\). This is a finite exact certificate of deck equality, reproduced independently by the two standalone algorithms included with the result.

**The finite minimal-length boundary.** Enumerate all \(2^{13}=8192\) words of length thirteen, compute the sixteen four-deck multiplicities of each word by the recurrence below, and partition the resulting words according to identical vectors. This produces exactly \(8176\) deck classes, and none contains both an element with at most two one-runs and an element with more than two. The standalone verification source explicitly executes the complete enumeration, with no sampling, pruning, or omitted cases. A second independently implemented enumeration based on all \(\binom{13}{4}=715\) four-subsets per word reproduces these two conclusions.

For completeness, if two length-\(n\) words have equal four-decks and \(n\ge4\), their three-decks also agree. Indeed for any length-three pattern \(v\), let \(c(u,v)\) be the number of ways to delete one coordinate of a length-four word \(u\) to obtain \(v\). Double-counting a chosen occurrence of \(v\) and a fourth index gives
\[
(n-3)N(v,x)=\sum_{u\in\{0,1\}^4}c(u,v)N(u,x).
\]
Therefore adjoining the same leading zero preserves equality of four-decks, because for any length-four pattern \(u\),
\[
N(u,0x)=N(u,x)+\mathbf 1_{\{u_1=0\}}N(u_2u_3u_4,x).
\]
Leading zero padding does not increase the number of one-runs. Thus any alleged cross-class collision of length \(4\le n<13\) could be padded to a collision at length thirteen, which the exhaustive certificate rules out. The \(n=14\) complete census enumerates all \(2^{14}=16384\) words, finds exactly \(16328\) distinct four-decks, and finds precisely one mixed class; that class has exactly the two displayed words. This proves the claimed uniqueness at the first length.

**Arbitrary lengths and sharp order.** For every \(n\ge14\), prepend \(n-14\) zeros to both witnesses. The preceding formula inductively preserves their common four-deck and their different run categories. Thus four-decks fail to reconstruct \(\mathcal B_2\) against unrestricted opponents. Angal et al., Theorem 1.3, establish the complementary upper bound \(r(\mathcal B_\ell)\le2\ell+1\); taking \(\ell=2\) gives \(r(\mathcal B_2)\le5\). Since equal four-decks also entail equal shorter decks, the displayed pair yields the opposite inequality, giving equality.

**Completeness of the finite certificates.** For every length \(n\in\{13,14\}\), `verify_dp.py` visits each integer from \(0\) through \(2^n-1\) once, using its zero-padded \(n\)-bit expansion as a distinct word. For each prefix \(s\) and subsequence length \(j\in\{0,1,2,3,4\}\), it stores the count of each binary \(j\)-subsequence; appending bit \(b\) updates the count of pattern \(u b\) by the prior count of \(u\). Descending updates therefore give the exact deck without mixing current-prefix and next-prefix counts. Dictionary keys group *all* words by exact integer tuples, and both run categories are inspected for each group. `verify_direct.py` uses no dynamic programming: for every length-thirteen word it independently enumerates all \(715\) subsets of four positions; it also independently verifies the two fourteen-bit witnesses via all \(1001\) four-subsets. Both use exact unbounded Python integers.

## Verification
Execute `python3 verify_dp.py` and `python3 verify_direct.py` alongside the files in this package. The first prints `DP_EXHAUSTIVE_OK` after the complete length-thirteen and length-fourteen censuses, and the second prints `DIRECT_EXHAUSTIVE_N13_OK` after the complete independently implemented length-thirteen census and witness checks. Both programs were executed successfully. The code specifies the entire finite computation and independently checks the combinatorial identity \(\sum_{u}N(u,x)=\binom n4\) for each word.

## Relationship to prior work
Angal, Ascoli, He, He, Post, Soe, and Zhukova, *Deck Reconstruction for Restricted Word Classes*, arXiv:2610.41110v1 (first public October 30, 2026), Theorem 1.3, proves \(r'(\mathcal B_\ell)\le2\ell\) and \(r(\mathcal B_\ell)\le2\ell+1\). It does **not** state that the latter bound is attained for \(\ell=2\), identify the first cross-class four-deck collision length, or enumerate its unique mixed class. The present result relies on that upper bound, and independently certifies its sharpness and the exact first obstruction. The earlier literature on general binary deck enumeration, including Chrisnata et al., *On the Number of Distinct k-Decks: Enumeration and Bounds*, addresses unrestricted deck counts rather than this two-run-versus-unrestricted fiber distinction.

## Limitations
The sharpness theorem applies to the at-most-two-one-run class, not all \(\ell\). The first-length uniqueness conclusion is limited to the complete length-fourteen census. The exact finite enumeration does not prove a classification of collisions at longer lengths, although zero padding proves their existence. The result uses scattered, multiplicity-retaining decks, not contiguous-factor or multiplicity-free sets. Historical priority beyond the inspected literature and independent external verification remain open.

## References
1. K. Angal, R. Ascoli, S. X. He, X. He, L. Post, A. O. Soe, and O. Zhukova, *Deck Reconstruction for Restricted Word Classes*, arXiv:2610.41110v1, October 30, 2026. https://arxiv.org/html/2610.41110v1
2. J. Chrisnata, H. M. Kiah, S. R. Karingula, A. Vardy, E. Yaakobi, and H. Yao, *On the Number of Distinct k-Decks: Enumeration and Bounds*, Advances in Mathematics of Communications 17 (2023), 960–978, DOI: 10.3934/amc.2021032. https://doi.org/10.3934/amc.2021032
