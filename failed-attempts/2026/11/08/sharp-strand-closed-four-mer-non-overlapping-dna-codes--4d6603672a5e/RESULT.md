# Sharp strand-closed four-mer non-overlapping DNA codes

## Finding

Let \(\Sigma=\{0,1,2,3\}\), with Watson--Crick complementation \(\bar0=1\), \(\bar1=0\), \(\bar2=3\), and \(\bar3=2\). Write \(\rho(w_1w_2w_3w_4)=\bar w_4\bar w_3\bar w_2\bar w_1\). A code \(C\subseteq\Sigma^4\) is **strand-closed** if \(\rho(C)=C\), and **non-overlapping** if for all \(u,v\in C\), including \(u=v\), and every \(k\in\{1,2,3\}\), the length-\(k\) prefix of \(u\) differs from the length-\(k\) suffix of \(v\).

**Theorem.** The maximum size of a strand-closed non-overlapping four-mer code is exactly \(17\). There are exactly \(32\) different optimal codes on the labeled alphabet \(\Sigma\). They fall into exactly four equivalence classes, each of size \(8\), under the eight alphabet permutations commuting with complementation. Reversal of all codewords induces no additional equivalence on these codes: because \(\rho(C)=C\), reversal equals letterwise complementation of the entire code.

Here is one optimal code in the numeric convention above:

```text
0003 0011 0013 0203 0231 0233 2003 2011 2013
2103 2111 2113 2131 2133 2203 2231 2233
```

The four numeric symbols may be identified, for example, with A,T,C,G respectively.

## Assumptions and scope

The alphabet has exactly two fixed-point-free complementary pairs, the word length is exactly four, and each element is a distinct, oriented word. The code must contain the reverse complement of each of its words; this is **closure**, not the different condition that reverse-complement pairs be forbidden or have prescribed Hamming separation. The prefix--suffix condition is the full non-overlapping (cross-bifix-free or mutually uncorrelated) condition, stronger than the usual comma-free condition. No other sequence composition, distance, or biochemical restrictions are assumed.

## Proof

**1. Restricting the endpoint alphabet.** For a nonempty code \(C\), let \(A\) be its set of first letters and \(B\) its set of final letters. Strand closure gives \(B=\bar A\), while the \(k=1\) non-overlap condition gives \(A\cap B=\varnothing\). Thus \(A\) chooses at most one letter from each complementary pair, and \(1\le |A|\le 2\). Every such \(A\) is conjugate, by a permutation commuting with complementation, either to \(\{0\}\) or to \(\{0,2\}\).

**2. The one-start-letter case cannot be optimal.** Suppose \(A=\{0\}\); then all words have form \(0bc1\). If \(b=1\), the prefix `01` of this word is the suffix `01` of its reverse complement, contrary to non-overlap. If \(c=0\), its reverse complement has second letter `1`, giving the same contradiction. Hence \(b\in\{0,2,3\}\) and \(c\in\{1,2,3\}\), so \(|C|\le 9<17\). The same bound holds for each singleton \(A\).

**3. The two-start-letter case reduces to a 20-vertex weighted graph.** Fix \(A=\{0,2\}\), hence \(B=\{1,3\}\). All possible codewords lie in \(W=A\Sigma^2B\), which is invariant under \(\rho\). Partition the 64 words of \(W\) into orbits of \(\rho\). Discard an orbit if one of its words overlaps itself or another word in that orbit. The surviving 20 orbits, with indices 0 through 19, are listed verbatim in `certificate.json`. The certificate also gives a 20-entry adjacency bitmask array: two orbit vertices are adjacent exactly when a prefix--suffix overlap occurs between their words. Each vertex has weight one or two, the number of words in its orbit. Consequently, **every** admissible code with this choice of \(A\) corresponds bijectively to a weighted independent set; the weight is exactly the number of codewords.

**4. A 17-word upper bound with a short clique certificate.** Vertices \(1,2,9,10,15,19\) are isolated and have total weight \(1+2+1+2+1+1=8\). The remaining 14 vertices split into the following disjoint cliques (the index entries can be checked directly using the orbit list):

| Clique | Vertices | Maximum weight contributed by an independent set |
|---|---|---|
| First | 0, 3, 4 | 2 |
| Second | 5, 8, 14 | 2 |
| Third | 6, 7, 11 | 2 |
| Fourth | 13, 16, 18 | 2 |
| Fifth | 12, 17 | 1 |

Thus every independent set has weight at most \(8+2+2+2+2+1=17\). The displayed code attains 17 and passes all prefix--suffix and strand-closure tests, proving sharpness.

**5. Exhausting equality.** Equality forces inclusion of every isolated orbit and exactly one vertex from each of the five displayed cliques. The first four cliques have three choices each and the fifth has two; only \(3^4\cdot2=162\) choice tuples remain. Comparing all chosen pairs against the 20-vertex adjacency table leaves precisely these eight feasible index tuples, in clique order:

```text
(0,14,6,18,17)
(0,14,7,16,17)
(3,5,11,16,12)
(3,8,11,13,12)
(4,5,6,18,17)
(4,5,7,16,12)
(4,5,7,16,17)
(4,8,7,13,12)
```

They give eight distinct maximum codes for the fixed \(A=\{0,2\}\). There are exactly four possible two-element sets \(A\), each choosing one representative from each complementary pair. Complement-preserving relabelings transport the eight maximum codes to eight different maxima for each \(A\), yielding \(4\cdot8=32\) labeled maxima. The group of eight complement-preserving permutations has four orbits of size eight on these 32 codes; `certificate.json` contains one complete representative for each class. This proves both classification assertions.

## Verification

`certificate.json` contains the explicit orbit-word catalog, adjacency masks, all eight codebooks for the representative endpoint set, and four representatives for the alphabet-symmetry classes. `verify.py` reconstructs the graph from the word-level definition, performs a separate recursive maximum-weight independent-set census, checks the certificate, and computes the symmetry classes. `crosscheck.cpp` independently reconstructs the orbits and uses a full bitmask dynamic program over all \(2^{20}\) subsets (as well as all \(2^6\) subsets for the singleton-endpoint case). Both report exactly 17 as the optimum and eight maxima for \(A=\{0,2\}\); the Python check verifies 32 labeled maxima and four eight-element classes.

Reproduction, from the directory containing the files:

```sh
python3 verify.py
c++ -O2 -std=c++17 crosscheck.cpp -o crosscheck
./crosscheck
```

The proof's finite step is exhaustive because the endpoint partition is proved complete, the reverse-complement orbit list is generated from all \(4^4\) possible words, and the certificate covers every possible independent set. No finite computation is used as evidence for an unproved infinite-parameter statement.

## Relationship to prior work

Blackburn (2013) developed non-overlapping-code constructions and bounds for arbitrary alphabet size and word length. Stanovnik, Moškon and Mraz (2024, Section 5, Theorems 19--20) obtained the *unrestricted* length-four optimum and its enumeration: for a four-letter alphabet, the ordinary maximum is 27. Those theorems do not impose reverse-complement closure, and 27 cannot be attained under the additional constraint considered here. The present theorem concerns the optimum **after requiring both strand orientations to belong to the code**, together with a classification of its 32 equality cases. Levy and Yaakobi (2018) discuss mutually uncorrelated codes for DNA storage, providing applications and related terminology, but their publicly available description does not assert the present four-mer strand-closure enumeration. The overlap comparisons and their residual historical-priority limitations are detailed in `REVIEW.md` and `AUDIT.json`.

## Limitations

Only four-symbol, length-four codebooks with the particular fixed-point-free pairing are covered. The theorem makes no claim about longer codes, other alphabets or a constrained Hamming distance. Reverse-complement closure means a reader may encounter both strand orientations; assigning each reverse-complement pair to a common message or distinguishing orientation requires a separate decoding specification. The result is a combinatorial synchronization statement, not an experimental claim about primers, cross-hybridization, synthesis, or sequencing error rates.

## References

1. Simon R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026, first submitted 2013-03-05. https://arxiv.org/abs/1303.1026
2. Lidija Stanovnik, Miha Moškon and Miha Mraz, *In search of maximum non-overlapping codes*, Designs, Codes and Cryptography 92 (2024), 1299--1326. https://doi.org/10.1007/s10623-023-01344-z
3. Maya Levy and Eitan Yaakobi, *Mutually Uncorrelated Codes for DNA Storage*, arXiv:1804.05371, first submitted 2018-04-15. https://arxiv.org/abs/1804.05371
