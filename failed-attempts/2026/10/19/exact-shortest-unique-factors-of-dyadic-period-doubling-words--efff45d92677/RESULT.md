# Exact shortest unique factors of dyadic period-doubling words

## Finding
Let \(\mu(0)=01\) and \(\mu(1)=00\), and put \(P_k=\mu^k(0)\). A *unique factor* is a contiguous substring occurring at exactly one starting position; a *shortest unique factor* is one of smallest possible length. For every integer \(k\ge4\), the minimum length of a unique factor of \(P_k\) is
\[
L_k=2^{k-2}+1.
\]
Precisely four factors attain this length, at the zero-based starting positions
\[
2^{k-2}-1,\qquad 3\cdot2^{k-3}-1,\qquad 2^{k-1}-1,\qquad 3\cdot2^{k-2}-1.
\]
If \(Q_k\) denotes \(P_k\) with its final letter removed, the same minimum length holds, with precisely the first three of these starting positions attaining it.

## Assumptions and scope
A factor is taken **linearly**, without wrapping around the end; its multiplicity counts all zero-based start indices, including overlapping occurrences. All statements concern the finite binary words \(P_k\) and \(Q_k\) for integer \(k\ge4\). The four minimal factors of \(P_k\) are pairwise distinct because each occurs exactly once; likewise for \(Q_k\). The theorem does not assert a description of all longer unique factors or uniqueness properties of the infinite fixed point.

## Proof
For a binary word \(X\), let \(\operatorname{SU}(X)\) be the minimum length of a factor occurring exactly once. Define \(X=P_{k-1}\) of length \(N=2^{k-1}\) and \(Y=Q_{k-1}\) of length \(N-1\). The defining morphism implies
\[
P_k[2j]=0,\qquad P_k[2j+1]=1-X[j]\quad(0\le j<N),
\]
and \(Q_k=P_k[0\ldots 2N-2]\), the complete word with its final odd-indexed symbol deleted. The symbol \(1\) can occur only at odd global indices. No factor of length four is \(0000\): among any four consecutive positions, two consecutive odd global indices occur, whose symbols are complements of consecutive entries of \(X\); by induction on the morphism, \(X\) has no \(11\), so at least one complement equals \(1\). (Directly, every \(P_j\) has no \(11\), since images start in \(0\) and contain at most one \(1\).) The same holds for truncations \(Q_k\).

Therefore every factor of length at least four contains a \(1\). Such a factor beginning at an even index has its \(1\)'s only at **odd relative offsets**; one beginning at an odd index has its \(1\)'s only at **even relative offsets**. Hence factors from opposite start-index parities can never be equal. Furthermore, in a fixed start-index parity class the factor is completely determined by the entries of \(X\) read in the odd global positions, since the other positions are all zero. Thus factor multiplicity is exactly the multiplicity of its selected factor of \(X\), or the corresponding prefix \(Y\) if the boundary excludes the final symbol.

For clarity, here are the precise occurrence-preserving bijections, with \(m\ge2\). For odd target length \(2m-1\): in \(P_k\), odd start positions correspond to length-\(m\) factors of \(X\), while even starts correspond to length-\((m-1)\) factors of \(Y\). In \(Q_k\), odd starts correspond to length-\(m\) factors of \(Y\), and even starts to length-\((m-1)\) factors of \(Y\). For even target length \(2m\): in \(P_k\), even starts correspond to length-\(m\) factors of \(X\), and odd starts to length-\(m\) factors of \(Y\). In \(Q_k\), **both** start parities correspond separately to length-\(m\) factors of \(Y\). In each case the target index is \(2j\) or \(2j+1\) when the source index is \(j\); these correspondences run over all allowable indices and preserve exact multiplicity within the parity class. Cross-parity equality is impossible for lengths at least four.

The base case \(k=4\) follows from directly listing factors and their multiplicities in
\[
P_4=0100010101000100,\qquad Q_4=010001010100010.
\]
Both have shortest-unique length \(5\); the unique starts of \(P_4\) are \(3,5,7,11\), and those of \(Q_4\) are \(3,5,7\). This finite base is reproducible by the supplied exact checker.

Assume the minimum unique factor length of both \(X\) and \(Y\) equals \(L\), and that their starts are those prescribed at index \(k-1\). Consider any factor length \(\ell\ge4\) below \(2L-1\). Its bijective underlying source factor has length at most \(L-1\), irrespective of its start parity or the presence of the final symbol; therefore no such factor can be unique. A unique factor of length less than four would extend to a unique factor of length four (as both target words have length at least sixteen), already excluded. At length \(2L-1\), only odd starts can be unique, since the even-start class corresponds to source length \(L-1\). The odd-start factors are unique precisely when their length-\(L\) source factors are unique. Thus
\[
\operatorname{SU}(P_k)=\operatorname{SU}(Q_k)=2L-1,
\]
with the complete-word and truncated-word position sets obtained from the previous corresponding position sets by \(j\mapsto2j+1\). Starting from \(L_4=5\), we obtain \(L_k-1=2^{k-4}(L_4-1)=2^{k-2}\). Applying the same position recurrence to the four (respectively three) base indices gives exactly the displayed formulas. This completes simultaneous induction on \(k\).

## Verification
The bundled `checker.py` computes factor multiplicities by exact substring equality (not probabilistic hashing) for every \(k\in\{4,5,6,7,8,9\}\), independently for the complete and final-symbol-deleted words. For every length below the claimed minimum it checks that no factor is unique, and at the minimum it verifies the complete index list. Run `python3 checker.py`; the recorded output is in `checker_output.txt`. These finite tests support the proof but do not substitute for the induction.

## Relationship to prior work
The 2026 work *Faster Algorithms for Shortest Unique or Absent Substrings* develops general shortest-unique-substring algorithms; it does not supply this displayed dyadic family formula in its inspected presentation. The 2026 article *The Smallest String Attractors of Fibonacci and Period-Doubling Words* determines attractor-related properties of these words; its inspected period-doubling analysis concerns attractors, a different extremum and quantifier. A 2025 study of generalized period-doubling sequences investigates kernel words and gap factorizations, not the global shortest-unique threshold for these finite prefixes. Published attractor and distinct-window invariants cannot themselves determine unique-factor multiplicity minima.

## Limitations
The result is about factors of finite words, not the corresponding infinite word, not the full inventory of unique factors, and not minimal unique substrings conditioned on a specified covered position. Originality has been checked against the cited accessible sources and related search results, but an unindexed or differently phrased earlier statement remains possible. This is not an independently validated result.

## References
1. *Faster Algorithms for Shortest Unique or Absent Substrings*, arXiv:2605.04826 (first publicly available 2026-05-06).
2. *The Smallest String Attractors of Fibonacci and Period-Doubling Words*, arXiv:2602.16152 (first publicly available 2026-02-18).
3. *A new factorization of generalized period-doubling sequences through kernel words and gaps sequences*, arXiv:2511.20881 (first publicly available 2025-11-25).
4. OEIS A367184 (a distinct, maximal-all-windows-unique invariant; consulted for possible implication).
