# Exact ternary length-four insertion-covering threshold and the two-codeword cost of non-equivalence

## Finding

For \(\Sigma=\{0,1,2\}\), define the insertion-covering number \(I\) to be the smallest \(|C|\) for which \(C\subseteq\Sigma^4\) meets the deletion set of every \(y\in\Sigma^5\). Define deletion covering by requiring every \(u\in\Sigma^3\) to belong to the deletion set of some \(x\in C\). Then
\[
I=31,\qquad \min\{|C|: C\text{ is insertion-covering but not deletion-covering}\}=33.
\]
In particular, all insertion-covering sets with at most \(32\) words automatically cover all length-three words under one deletion, but one with \(33\) words need not.

## Assumptions and scope

The alphabet has exactly three symbols. A subsequence preserves the original order and results from deleting positions; repeated deletion outcomes count once. Insertion-covering means that each of the \(3^5=243\) possible length-five outputs has at least one length-four subsequence in \(C\). Deletion-covering means that each of the \(3^3=27\) possible length-three outputs is a subsequence of a word of \(C\). Covering is purely combinatorial: no channel probabilities are required. All codewords have length four, and exactly one symbol is inserted or deleted.

## Proof

**Upper witnesses.** Set

\[
C_{31}=\{\text{the 31 words in the first block below}\},\qquad C_{33}=\{\text{the 33 words in the second block below}\}.
\]
Here each whitespace-delimited word is one codeword, in lexicographic order.

```text
C31: 0000 0011 0012 0021 0022 0100 0111 0122 0210 0220 1000 1011 1022 1100 1102 1111 1120 1122 1201 1220 2001 2002 2110 2112 2120 2121 2200 2211 2212 2221 2222
C33: 0000 0001 0010 0011 0022 0100 0101 0110 0111 0202 0221 1000 1001 1010 1011 1100 1101 1110 1111 1122 1212 1220 1222 2002 2021 2112 2120 2122 2200 2202 2211 2220 2222
```

Directly enumerating all five deletion positions of each of the \(243\) length-five words verifies that each has a subsequence in both displayed sets. Directly enumerating the four deletion positions of each \(C_{33}\) word shows that neither \(012\) nor \(102\) is covered by deletion. These claims are reproduced by `checker.cpp`.

**Reduction to a single forbidden deletion target.** If an insertion-covering set fails deletion covering, there exists \(u\in\Sigma^3\) that is not a deletion subsequence of any codeword. If \(u\) uses at most two different symbols, one can form a length-five word whose *every* length-four deletion subsequence contains \(u\). Up to a relabeling of symbols, the pairs \((u,y)\) witnessing this fact are \((000,00000)\), \((001,00011)\), \((010,01010)\), and \((011,00111)\). Therefore any insertion cover must contain some length-four subsequence of \(y\), and hence its deletion image contains \(u\), a contradiction. Thus the omitted word uses all three distinct symbols. Any such word is a symbol permutation of \(012\), and relabeling preserves both covering properties and cardinality. Consequently it suffices to rule out insertion covers of size at most \(32\) whose words all avoid \(012\) as a deletion subsequence.

**Finite exact lower-bound certificate.** For any list of eligible length-four centers, associate to each center a 243-bit vector whose marked coordinates are the length-five words containing it as a deletion subsequence. `checker.cpp` tests the existence of a covering subfamily with a prescribed word-count budget by an exhaustive depth-first branch search. At each uncovered target, any feasible completion must select one of its eligible parent centers, so branching on all such centers is exhaustive. The code applies only sound necessary-condition pruning: a volume bound using the largest additional coverage from any center; a greedily formed packing of uncovered targets with pairwise-disjoint sets of eligible parent centers, each requiring a different selected center; and memoization of already encountered covered-target bitsets at an equal or smaller chosen count. Centers forced by targets with a unique parent are included initially. Every parent set, bitset, pruning condition and witness is generated solely from the preceding definitions. No external optimization solver or floating-point comparison is required.

The exhaustive outcomes are `feasible=0` for a budget of \(30\) with all \(81\) possible centers and `feasible=0` for a budget of \(32\) with every center containing \(012\) as a length-three deletion subsequence forbidden. Together with the two explicit witnesses and the reduction, these prove both exact optima. The certificate is a finite exhaustion of all combinatorial possibilities, not a sampling argument.

## Verification

Compile `checker.cpp` using a C++17 compiler and execute it:

```sh
g++ -O3 -std=c++17 checker.cpp -o checker
./checker
```

The checker reconstructs the full 243-target incidence relation from the alphabet, verifies both witnesses, searches all size-at-most-30 insertion covers, and searches all size-at-most-32 insertion covers avoiding the forbidden `012` deletion output. It prints `CERTIFICATE_OK` only when all assertions hold. The checked execution examined \(7,615,421\) nodes in the first infeasibility search and \(23,213\) in the second, each ending in `feasible=0`. These node counts describe the concrete implementation, not an unverified extrapolation.

## Relationship to prior work

Xie, Sun and Ge (2026) study the fundamental distinction between insertion and deletion covering and establish bounds and constructions, particularly in large alphabets. The present statement quantifies the separation at the specific ternary length-four boundary; it does not claim the underlying logical non-equivalence as new. Pikhurko, Verbitsky and Zhukovskii (2024/2025) study lower bounds and density for insertion-covering codes and discuss smaller exact examples. Lenz, Rashtchian, Siegel and Yaakobi (2019/2021) provide general bounds for insertion/deletion covering. These results do not state the exact two-word separation for the parameters here in the examined texts. Exact deletion-covering values for longer source centers, and single-deletion *correcting* codes, involve different incidence systems and do not imply this optimum.

## Limitations

The finding concerns an exact finite ternary instance and does not establish the smallest alphabet/block length at which any separation can occur, analogous formulae for arbitrary length or alphabet, or an efficient asymptotic construction. Its numerical proof depends on the transparent, complete finite search algorithm supplied with the record; it is not an independent mathematical audit. An earlier unindexed table or unpublished exhaustive result might contain this precise value.

## References

1. C. Xie, Y. Sun, G. Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379, first publicly posted June 13, 2026. https://arxiv.org/abs/2606.15379
2. O. Pikhurko, O. Verbitsky, M. Zhukovskii, *New bounds for the optimal density of covering single-insertion codes via the Turán density*, arXiv:2409.06425, first publicly posted September 10, 2024. https://arxiv.org/abs/2409.06425
3. A. Lenz, C. Rashtchian, P. H. Siegel, E. Yaakobi, *Covering Codes using Insertions or Deletions*, arXiv:1911.09944, first publicly posted November 22, 2019. https://arxiv.org/abs/1911.09944
