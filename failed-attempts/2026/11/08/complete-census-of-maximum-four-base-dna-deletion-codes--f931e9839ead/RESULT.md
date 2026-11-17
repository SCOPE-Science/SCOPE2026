# Complete census of maximum four-base DNA deletion codes

## Finding

Fix the labeled alphabet \(\Sigma=\{A,C,G,T\}\), with Watson--Crick complement \(A\leftrightarrow T\) and \(C\leftrightarrow G\). Let \(\rho(w)\) be the reversal followed by complementation of a word, and let \(\mathcal D(w)\) be the set of all distinct words obtained from \(w\) by deleting exactly one position.

A length-four DNA deletion code is a subset \(C\subseteq\Sigma^4\) satisfying **all** of the following: \(\rho(C)=C\); \(w\ne\rho(w)\) for every \(w\in C\); and \(\mathcal D(u)\cap\mathcal D(v)=\varnothing\) for every distinct \(u,v\in C\). Words and codebooks are labeled, with no identification under reversal or symbol permutation unless expressly stated.

The known maximum code size is \(22\). **There are exactly \(44\) different labeled codes of that maximum size.** Under the group of all eight alphabet permutations commuting with Watson--Crick complementation, these codes form **nine orbits**: seven of size \(4\) and two of size \(8\). Adjoining global word reversal does not enlarge these orbits, because a reverse-complement-closed code obeys \(\operatorname{rev}(C)=\operatorname{comp}(C)\), and global complementation belongs to the eight-element group.

Every maximum code contains the two reverse-complement pairs \(\{AAAA,TTTT\}\) and \(\{CCCC,GGGG\}\). These are the **only** pairs present in every optimum. The accompanying `maximum_codebooks.tsv` gives all \(44\) codebooks; each row lists the lexicographically smaller member of each of its eleven reverse-complement pairs. The accompanying `symmetry_representatives.tsv` gives one representative and its orbit size for each of the nine classes.

## Assumptions and scope

Deletion observations retain the order of the three surviving symbols, but forget which of the four positions was deleted. Repeated deletions leading to the same word are counted once; disjointness is a condition on sets, not multiplicities. All four DNA letters are distinct, and every individual strand is explicitly included with its reverse complement. Self-reverse-complementary words are disallowed, as in the source definition of a DNA code with deletion similarity.

There are \(4^4=256\) four-letter words. Exactly \(16\) are fixed by reverse complementation, leaving \(120\) distinct two-word reverse-complement orbits. Direct construction shows that for all \(120\) such orbits, the deletion sets of the two members are disjoint.

## Proof

For each nonfixed reverse-complement orbit \(O=\{w,\rho(w)\}\), set \(B(O)=\mathcal D(w)\cup\mathcal D(\rho(w))\). Construct the finite compatibility graph \(G\) with the \(120\) orbits as vertices and put an edge between distinct vertices \(O,O'\) exactly when \(B(O)\cap B(O')=\varnothing\). Every valid code is uniquely the union of a clique of these orbits, and a clique of size \(k\) yields exactly \(2k\) strands. These equivalences follow immediately from the three code axioms; the statement that all \(120\) candidate pairs are internally compatible is independently checked from the explicit deletion rule.

The exhaustive certificate in `census.cpp` constructs \(G\) directly from the alphabet, computes all cliques of size \(12\), and confirms that there are none. It then enumerates every size-\(11\) clique once, finding exactly \(44\). This proves the optimum size \(22\) independently of the previously published optimum, and proves the new count. The complete listing is in `maximum_codebooks.tsv`.

Here is the crucial exhaustive-search invariant. At every recursive call, the selected vertices are a strictly increasing clique and the candidate set consists exactly of later vertices adjacent to all selected ones. The recursion branches on the lowest remaining candidate, removes it before processing subsequent choices, and intersects the residual candidates with its neighbor set. This partitions the family of possible clique extensions without omission or duplication. A safe pruning bound greedily partitions the candidate graph into independent color classes; every possible clique contains at most one vertex from each such class. A branch is discarded only when this rigorous bound, or the raw remaining vertex count, is smaller than the number of vertices still needed. Thus the certificate is exhaustive, rather than a heuristic optimizer.

A second implementation, `verify.py`, independently reconstructs the graph from deletion strings and uses a Bron--Kerbosch pivot enumeration of maximal cliques. It confirms the absence of larger cliques and exactly \(44\) maxima, and checks equality with the complete certificate. It then enumerates the eight complement-preserving alphabet permutations and their actions on these \(44\) codes. Their orbit sizes are \(4,4,4,4,4,4,4,8,8\). Taking the intersection of the eleven chosen pair-representatives over all \(44\) rows gives exactly \(\{AAAA,CCCC\}\), proving the compulsory-pair assertion.

## Verification

With a standard C++17 compiler and Python 3 standard library, run:

```sh
c++ -std=c++17 -O2 census.cpp -o census
./census > reconstructed_codebooks.tsv
python3 verify.py reconstructed_codebooks.tsv symmetry_representatives.tsv
```

The first program reports `ORBIT_CANDIDATES=120; SIZE_12_SETS=0; MAXIMUM_CODEBOOKS=44`. The second reports `INDEPENDENT_VERIFICATION_OK 44 maxima; 9 symmetry classes; compulsory pairs AAAA,CCCC`. The delivered complete file `maximum_codebooks.tsv` is also verified by invoking the second program on it. Both programs directly use the definition of deletion; no proprietary solver or external database is needed to reproduce the finite proof.

## Relationship to prior work

D'yachkov and collaborators (2003) introduced the reverse-complement-closed DNA-code model using deletion similarity. D'yachkov and collaborators (2005), Example 5 and Remark 4, **already give and assert optimality of size \(22\)** for four-letter length-four, one-deletion DNA codes; their Example 5 is among the \(44\) codebooks enumerated here. They also discuss a related size-\(24\) ordinary deletion code admitting self-reverse-complementary strands, which is **not** a code in the present model. The new claim is the complete count, symmetry classification, and compulsory-pair characterization, **not** rediscovery of maximum size \(22\).

King (2003) considers DNA codes with Hamming and GC-content restrictions, not the deletion-shadow packing model. A one-page 2006 remark to the 2005 paper has an identifiable bibliographic record but was not available in full for inspection. Searches of related work did not locate a previous count of \(44\) optimum codebooks; this is a qualified priority assessment, not proof of historical novelty.

## Limitations

The theorem is specific to length-four, quaternary labeled words, reverse-complement closure, exclusion of fixed strands, and correction of one **deletion**. It does not extend automatically to insertions plus substitutions, additional GC-content or biochemical constraints, other word lengths, or unlabeled alphabets. Enumeration is exhaustive for this finite case only; no arbitrary-length result is claimed. The finite computations and source comparisons have been reviewed within this report, but **no independent scientific audit** has been performed. The inaccessible 2006 remark remains a historical-priority risk.

## References

1. A. G. D'yachkov et al., *Exordium for DNA Codes*, Journal of Combinatorial Optimization 7 (2003), 369--379. https://www.renyi.hu/~elp/Evol/DNATut-JCombOpt03.pdf ; https://doi.org/10.1023/B:JOCO.0000017385.39168.0d
2. A. G. D'yachkov et al., *On DNA Codes*, Problems of Information Transmission 41 (2005), 349--367, especially Example 5, Example 6, Remark 4. https://doi.org/10.1007/s11122-006-0004-3 ; author-uploaded full text: https://www.researchgate.net/publication/225807128_On_DNA_codes
3. O. D. King, *Bounds for DNA codes with constant GC-content*, arXiv:math/0306197, first posted June 12, 2003. https://arxiv.org/abs/math/0306197
4. A. G. D'yachkov et al., *Remark on "On DNA Codes"*, Problems of Information Transmission 42 (2006), 166. https://doi.org/10.1134/S0032946006020104 (full text not inspected).
