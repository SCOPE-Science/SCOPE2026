# Complete classification of maximum ternary order-three orientable cycles

## Finding

On the labeled alphabet \(\Sigma=\{0,1,2\}\), exactly **eight** cyclic words of length \(9\), considered modulo rotation, contain each nonpalindromic length-three factor up to reversal exactly once. Equivalently, they are all maximum-period order-three orientable sequences, and they have precisely **two** symmetry classes under the simultaneous action of alphabet permutations and word reversal. The class cardinalities are \(6\) and \(2\), with rotation-canonical representatives `001120122` and `001220112`, respectively.

Here is the complete labeled rotation-canonical catalog; `orbit` means the canonical representative of its class under symbol permutation and reversal:

| Rotation-canonical word | Orbit |
|---|---|
| `001120122` | `001120122` |
| `001122012` | `001120122` |
| `001201122` | `001120122` |
| `001220112` | `001220112` |
| `002102211` | `001120122` |
| `002110221` | `001220112` |
| `002210211` | `001120122` |
| `002211021` | `001120122` |

## Assumptions and scope

A cyclic word \(s=(s_i)_{i\in\mathbb Z/m\mathbb Z}\) is *order-three orientable* when, for all indices \(i,j\), the triple \((s_i,s_{i+1},s_{i+2})\) is unequal to the reversal \((s_{j+2},s_{j+1},s_j)\). In particular, palindromic triples are excluded even for \(i=j\), and no repeated triple is permitted. The alphabet is labeled. Two cyclic words are identified initially only under rotation; the eight-word enumeration is **not** a count modulo alphabet relabeling or reversal. The second quotient additionally allows the same symbol permutation at every position and reversal of the entire cycle. No complementation or other operation is introduced.

There are \(3^3=27\) ternary triples, of which \(3^2=9\) are palindromes (first equals last). The remaining \(18\) triples form nine unordered reversal pairs; at most one member of each pair can occur in an orientable cycle. Thus \(m\le 9\). The cited literature already exhibits period-nine cycles; maximum period is not claimed new.

## Proof

A period-nine orientable cycle must select **exactly one triple** from every one of the nine reversal pairs. Index the pairs in the fixed order

```
(001,100) (011,110) (021,120)
(002,200) (012,210) (022,220)
(102,201) (112,211) (122,221)
```

For a binary selection mask choose the first triple of a pair for a `0` and the reversed triple for a `1`. There are exactly \(2^9=512\) masks. Turn every selected triple \(abc\) into a directed edge \(ab\to bc\) between length-two words. An Euler circuit of these nine edges is equivalent to a length-nine cyclic word with those triples. Conversely any period-nine orientable cycle produces just such an Euler circuit and a selection mask. Each triple is a distinct labeled edge, so no edge multiplicities require quotienting.

The necessary balance condition, equality of incoming and outgoing degrees at every nonisolated vertex, holds for exactly **ten** masks:

```
000111000 001101100 001110001 010101010 011100011
100011100 101010101 110001110 110010011 111000111
```

This list follows by testing nine explicitly given pairs against the nine possible length-two vertices; `verify_euler.py` implements exactly the \(512\)-case finite calculation, not a sampling procedure. Of the ten balanced masks, only `001101100` and `110010011` induce strongly connected digraphs on their nonisolated vertices (reachable in both the forward and reverse directed graph). Every other mask has no Euler circuit involving all selected edges.

In each of the two surviving graphs there are six nonisolated vertices with outdegree multiset \((2,2,2,1,1,1)\). With the root chosen as vertex `00`, the directed outdegree-Laplacian has a reduced \(5\times5\) minor given below in the above mask order:

```
[ 2 -1 -1  0  0 ]    [ 2  0  0 -1 -1 ]
[ 0  1 -1  0  0 ]    [-1  2  0  0  0 ]
[ 0  0  2 -1 -1 ]    [ 0 -1  1  0  0 ]
[-1  0  0  2  0 ]    [ 0 -1 -1  2  0 ]
[ 0  0  0 -1  1 ]    [ 0  0  0 -1  1 ]
```

Both determinants are exactly \(4\), by integer elimination. The directed matrix-tree theorem therefore gives four in-arborescences rooted at `00` in each graph. The BEST theorem counts cyclic Euler circuits with individually distinguished edges by

\[
\tau_{00}\prod_{v}(d^+(v)-1)!=4\cdot1=4
\]

for each graph; here the circuits are considered modulo cyclic edge rotation and have no periodic edge repetition. Thus the total number of labeled orientable length-nine cycles modulo rotation is \(4+4=8\).

Finally apply each of the \(3!=6\) alphabet permutations and reversal to the eight rotation-canonical words, canonicalizing every image by its least cyclic rotation. The explicit exhaustive orbit computation in `verify_direct.py` returns two orbits of sizes \(6\) and \(2\), represented as claimed. Their union is the full eight-word catalog, so the classification is complete.

## Verification

Run `python3 verify_euler.py` and `python3 verify_direct.py` with Python's standard library. The first enumerates all \(512\) reversal-pair orientations, verifies the ten balanced masks and the two strongly connected graphs, computes both exact Bareiss determinants and checks the four anchored Euler circuits per graph. The second independently tests all \(3^9=19{,}683\) rooted nine-letter words using cyclic windows, reduces by rotation, checks the eight exact representatives and computes the action of all six alphabet permutations and reversal. Expected terminal markers are `EULER_VERIFY_OK` and `DIRECT_VERIFY_OK`. The data file `catalog.tsv` records the complete eight-word list. These computations exhaust the finite state spaces at issue; they do not prove any statement about other alphabet sizes or window orders.

## Relationship to prior work

Orientable sequences and the position/direction sensing motivation predate this result, notably Dai, Martin, Robshaw and Wild (1993). Rampersad and Shallit (public preprint 2003-11-07) studied avoidance of reversed factors in infinite words, rather than enumerating maximum finite cyclic orientable sequences. Burris, Motta and Shipman (public preprint 2016-08-30) studied *unoriented de Bruijn sequences*, which deliberately cover palindrome classes as well as nonpalindromic reversal classes; their objects and optimal-length count are different.

Alhakim, Mitchell, Szmidt and Wild (2024), Example 5.1, construct the period-nine ternary word `001201122`, and Gabrić and Sawada (2024), Introduction, explicitly give maximum period \(9\) and a witness `001120122` found by exhaustive search. Mitchell and Wild (2026) develop general upper bounds and constructions attaining them in low orders. The narrower claim here is **the exact eight-cycle population and its two symmetry types**, not existence, the nine-period upper bound, the reversal-pair formalism, or the classical BEST and matrix-tree theorems. The inspected accessible texts give examples/bounds but no list of the eight cycles or their two-class decomposition.

## Limitations

This classification is only for the labeled ternary alphabet, length-three windows, and maximum length nine. It does not count shorter orientable sequences, cyclic sequences with larger alphabet, higher window order, or unoriented de Bruijn sequences that include palindromes. No practical position-sensing performance is tested. Historical priority is qualified: early orientable-sequence sources with year-only publication records and unindexed exhaustive enumerations might contain an equivalent finite census; the absence of a match in inspected sources is not proof of uniqueness or priority. The 2003 first-public date here identifies the earliest fully date-verified inspected reversal-avoidance preprint, **not** the invention date of orientable sequences, whose literature goes back to 1993.

## References

- Dai, Z., Martin, K. M., Robshaw, M. J. B., and Wild, P. R., *Orientable Sequences* (1993), foundational binary orientable sequences; publication year known, day not verified.
- Rampersad, N., and Shallit, J., *Words Avoiding Reversed Subwords*, arXiv:math/0311121, first publicly posted 2003-11-07. https://arxiv.org/abs/math/0311121
- Burris, C. S., Motta, F. C., and Shipman, P. D., *An Unoriented Variation on de Bruijn Sequences*, arXiv:1608.08480, first publicly posted 2016-08-30. https://arxiv.org/abs/1608.08480
- Alhakim, A., Mitchell, C. J., Szmidt, J., and Wild, P. R., *Orientable sequences over non-binary alphabets*, *Cryptography and Communications* 16 (2024), Example 5.1. https://doi.org/10.1007/s12095-024-00742-x
- Gabrić, D., and Sawada, J., *Constructing k-ary Orientable Sequences with Asymptotically Optimal Length*, arXiv:2407.07029, 2024-07-09, Introduction. https://arxiv.org/abs/2407.07029
- Mitchell, C. J., and Wild, P. R., *New orientable sequences*, *Acta Informatica* 63 (2026), article 14. https://doi.org/10.1007/s00236-026-00528-z
