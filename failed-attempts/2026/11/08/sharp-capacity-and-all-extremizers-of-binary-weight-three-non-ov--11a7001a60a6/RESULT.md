# Sharp capacity and all extremizers of binary weight-three non-overlapping codes

## Finding

Let \(n\ge4\) be an integer. A binary code is **non-overlapping** (equivalently **cross-bifix-free**) when no nonempty proper prefix of any codeword equals a suffix of any codeword, including itself. Require every codeword to have exactly three ones, and let \(M_3(n)\) be the maximum possible number of codewords. Then

\[
M_3(n)=\left\lfloor\frac{(2n-3)^2}{24}\right\rfloor.
\]

All maximizers have a complete explicit classification. For integers \(t\ge1\) define \(B_{n,t}\) to be the binary words with one-positions precisely \(\{0,i,j\}\), using zero-based positions, where \(1\le i\le t\) and \(i<j\le n-1-t\). Let \(B_{n,t}^{\mathrm{rev}}\) denote their reversals. If \(n\equiv1,2\pmod3\), every maximum codebook is \(B_{n,k}\) or \(B_{n,k}^{\mathrm{rev}}\), where \(k=\lfloor n/3\rfloor\). If \(n=3k\) with \(k\ge2\), every maximum codebook is one of \(B_{n,k-1},B_{n,k},B_{n,k-1}^{\mathrm{rev}},B_{n,k}^{\mathrm{rev}}\). Thus there are precisely two labeled maximum codebooks in the first case and four in the second. The capacity satisfies \(M_3(n)\sim n^2/6\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\); the length \(n\ge4\) and Hamming weight three are fixed. A proper prefix or suffix has length between \(1\) and \(n-1\). Distinct inter-codeword and self-overlaps are both forbidden. Codebooks are labeled by their coordinate positions, not quotiented by reversal or complement. No Hamming-distance or error-correction requirement is imposed. The empty code is allowed. At length three the unique weight-three word has a nonempty border, so the capacity is zero; the classification above starts at length four.

## Proof

**Orientation.** A single non-overlapping word has unequal first and last bits, because the length-one prefix cannot equal the length-one suffix. If two codewords had opposite endpoint orientations, the first bit of one would equal the last bit of the other, contradicting the length-one condition. Hence all codewords of any nonempty code have the same orientation. Reversal preserves the non-overlapping property, so it suffices to classify those starting in \(1\) and ending in \(0\).

**Position parametrization and sharp compatibility criterion.** Every such weight-three word has one-positions \(\{0,i,j\}\) with \(1\le i<j\le n-2\). Given a nonempty codebook \(C\), set
\[
I=\max_{w\in C}i(w),\qquad J=\max_{w\in C}j(w).
\]
Choose words \(u,v\in C\) with \(i(u)=I\) and \(j(v)=J\). If \(I+J\ge n\), then the length \(n-J\) prefix of \(u\) and the length \(n-J\) suffix of \(v\) both consist of a single \(1\) followed by zeros: this prefix stops before the second one of \(u\), and that suffix starts at the last one of \(v\). Both lengths are proper and positive, giving a forbidden overlap. Thus the necessary inequality is
\[
I+J\le n-1.
\]
Conversely, suppose a family of words of the displayed orientation satisfies \(I+J\le n-1\). Every nonempty prefix starts with \(1\), so only suffixes starting at the second or third one could match. A suffix beginning at the third one of a word \(v\) has length \(n-j(v)\) and exactly one one; its corresponding prefix of a word \(u\) already includes the second one because \(i(u)\le I<n-j(v)\). A suffix beginning at the second one of \(v\) has length \(n-i(v)\) and exactly two ones; the corresponding prefix of \(u\) contains all three because \(j(u)\le J<n-i(v)\). Every other suffix starts in zero. Hence no forbidden overlap occurs. This proves the necessary-and-sufficient whole-family criterion.

**Rectangles and exact maximum.** Since \(I+J\le n-1\), each word in \(C\) has \(1\le i\le I\) and \(i<j\le n-1-I\). Thus \(C\subseteq B_{n,I}\). Conversely, all words in each nonempty \(B_{n,t}\) are mutually non-overlapping by the criterion, so optimal families are among these rectangular codebooks. Their cardinalities are
\[
|B_{n,t}|=\sum_{i=1}^{t}(n-1-t-i)=\frac{t(2n-3-3t)}2,
\quad1\le t\le\left\lfloor\frac{n-2}{2}\right\rfloor.
\]
The integer-concave quadratic has vertex \((2n-3)/6\). If \(n=3k\), the maximizing integers are \(k-1,k\); if \(n=3k+1\) or \(3k+2\), the unique maximizing integer is \(k\). Substitution and elementary division by \(24\) give the displayed floor formula for \(M_3(n)\).

Finally, if a codebook \(C\) has maximum cardinality, the containment \(C\subseteq B_{n,I}\) and \(|B_{n,I}|\le M_3(n)=|C|\) force \(C=B_{n,I}\). The maximizing integer calculation leaves exactly the claimed one or two orientations and their reversals. The families are distinct for \(n\ge4\); hence the classification and counts are exact. The leading term is \(n^2/6\). \(\square\)

## Verification

The standalone file `verify.py` uses only the Python standard library. Run `python verify.py` to reproduce direct prefix/suffix checks for 15,156 ordered pairs among analytically admissible candidates through length \(18\), exact maximum-clique and all-optimum counts for lengths \(4\) through \(9\), and the explicit construction sizes through length \(18\). The expected terminal marker is `VERIFY_OK`. These finite calculations check the derivation; the proof above, not enumeration, establishes the all-length theorem.

## Relationship to prior work

Chee, Kiah, Purkayastha and Wang [1] study general cross-bifix-free codes, near-optimal unrestricted constructions and Fibonacci estimates. Blackburn [2] establishes unrestricted bounds, constructions and short-length cases. Blackburn et al. [3] study restricted sets of forbidden overlap *lengths*, rather than all forbidden lengths with exact binary Hamming weight three. Stanovnik, Moškon and Mraz [4] develop unrestricted maximum-code formulations and enumerations. Their [5] studies almost-balanced and restricted-run non-overlapping codes; its fixed balanced-word constraints do not imply the all-length sparse weight-three capacity or the listed extremizers. The numerical all-length fixed-weight-three optimum and complete extremizer classification are not asserted to follow from any of these results. This is a restricted-class capacity theorem, not an improvement to the unrestricted alphabet-size optimum.

## Limitations

The claim applies only to binary constant Hamming weight three with every nontrivial overlap forbidden. Weight four or larger, nonbinary alphabets, fixed minimum Hamming distance and weaker overlap constraints are not covered. Historical originality remains conditional on the indexed and accessible publications compared; equivalent results may exist in unindexed literature or as unstated specializations. The work has not undergone independent mathematical audit.

## References

[1] Y. M. Chee, H. M. Kiah, P. Purkayastha, C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, arXiv:1209.0236, initial public version September 3, 2012. https://arxiv.org/abs/1209.0236

[2] S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026, initial version March 5, 2013. https://arxiv.org/abs/1303.1026

[3] S. R. Blackburn, N. N. Esfahani, D. L. Kreher, D. R. Stinson, *Constructions and bounds for codes with restricted overlaps*, arXiv:2211.10309. https://arxiv.org/abs/2211.10309

[4] L. Stanovnik, M. Moškon, M. Mraz, *In search of maximum non-overlapping codes*, *Designs, Codes and Cryptography* 92 (2024), 1299–1326. https://doi.org/10.1007/s10623-023-01344-z

[5] L. Stanovnik, M. Moškon, M. Mraz, *On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths*, arXiv:2410.18458. https://arxiv.org/abs/2410.18458
