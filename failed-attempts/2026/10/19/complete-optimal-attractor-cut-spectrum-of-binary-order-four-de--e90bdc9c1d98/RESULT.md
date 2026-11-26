# Complete optimal-attractor cut spectrum of binary order-four de Bruijn cycles

## Finding
A **binary de Bruijn cycle of order four** is a cyclic binary word of length 16 in which all 16 length-four binary words occur exactly once cyclically. For a cut \(c\in\{0,\ldots,15\}\), write \(R_c\) for the rotation beginning at cyclic position \(c\), and let \(T_c\) be the length-19 linear word obtained by appending the first three symbols of \(R_c\) to \(R_c\). Let \(\gamma(T_c)\) be its minimum *full string-attractor* size, with an attractor defined as a set of positions crossing an occurrence of every nonempty contiguous factor.

**Theorem (complete order-four spectrum).** Up to rotation, there are exactly 16 binary de Bruijn cycles of order four. Each cycle has either 8, 12, or 16 cuts with \(\gamma(T_c)=4\). Among the 16 cycles, respectively 4, 8, and 4 have those three numbers of optimal cuts. At every other cut, \(\gamma(T_c)=5\). Consequently, over all \(16\cdot16=256\) pairs (cyclic class, cut), the exact distribution is
\[
\#\{\gamma=4\}=192,\qquad \#\{\gamma=5\}=64.
\]
Whenever four positions suffice, their **unique** choice is \(\{4,8,12,16\}\) in one-based coordinates of the unfolding. Each cycle therefore has at least eight optimal cuts, but one quarter of all cut pairs fail to attain four.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), the de Bruijn order is exactly four, and the cyclic class is quotiented by rotation alone—not by bit complement or reversal. A cut is indexed from zero, while a marked position in the linear unfolding is indexed from one. The factor language is the ordinary **linear** factor language of \(T_c\), not the cyclic factor language of its original cycle. The claimed \(\gamma\) concerns *all* nonempty factor lengths, not merely length-four factors or a sharp four-attractor.

## Proof
**Sharp universal lower bound and rigidity.** Every \(T_c\) has all 16 length-four factors exactly once, with their occurrences starting at the 16 positions \(1,\ldots,16\). A marked position intersects at most four such occurrences, so \(\gamma(T_c)\ge4\). If four marks cover all 16 unique length-four factors, each must intersect *exactly* four distinct length-four occurrences, and their covered sets of starts must be disjoint. To cover the first start, the first mark must therefore be at position 4 (a mark at positions 1, 2, or 3 intersects fewer than four length-four occurrences). Applying the same argument to the remaining starts successively forces positions 8, 12, and 16. Thus \(G=\{4,8,12,16\}\) is the only possible four-position attractor. In particular a cut for which \(G\) misses a factor has minimum at least five.

**Finite exhaustive classification, with fully specified certificate.** It remains to classify those cuts where \(G\) hits every factor and to show five marks suffice elsewhere. The two independent exhaustive enumerators in `CHECKER.py` produce identical lists of 16 canonical cyclic representatives: the first examines all 65,536 labeled 16-bit words and retains precisely those with 16 distinct cyclic four-grams; the second enumerates Euler tours of the binary order-three de Bruijn directed graph, whose 16 edges are the four-grams, and quotients the resulting cycles by rotation. Both procedures are exhaustive by construction: a binary de Bruijn cycle is precisely an Euler tour of that graph, and every possible 16-bit cyclic labeling occurs among the 65,536 candidates.

For each of the 16 canonical representatives and each of its 16 cuts, `CHECKER.py` constructs all distinct nonempty factors of the 19-letter unfolding and the exact bit-mask of factors crossed at each position. It checks \(G\) against the complete factor mask. When \(G\) fails, the code searches all five-element subsets of the 19 positions in lexicographic order and records the first successful witness. The resulting 256 complete certificates, each storing canonical cycle, cut, exact minimum and a crossing-position witness, appear in `CUT_CERTIFICATE.tsv`. Running the verifier rebuilds the cycle universe independently, recomputes every factor mask and every first witness, and demands exact equality with all 256 certificate lines.

The canonical 16-cycle classification can also be independently read from the following tabulation; the right column gives the number of cuts with \(\gamma=4\):

| Canonical 16-bit cycle | Optimal cuts |
| --- | ---: |
| `0000100110101111` | 16 |
| `0000100111101011` | 12 |
| `0000101001101111` | 16 |
| `0000101001111011` | 12 |
| `0000101100111101` | 8 |
| `0000101101001111` | 12 |
| `0000101111001101` | 8 |
| `0000101111010011` | 8 |
| `0000110010111101` | 8 |
| `0000110100101111` | 12 |
| `0000110101111001` | 12 |
| `0000110111100101` | 12 |
| `0000111100101101` | 12 |
| `0000111101001011` | 12 |
| `0000111101011001` | 16 |
| `0000111101100101` | 16 |

These rows give four cycles with 8 optimal cuts, eight with 12, and four with 16. All other cuts have a verified five-position crossing set. The rigidity lemma excludes a four-position alternative at those cuts, while the displayed crossing sets exclude needing six or more. This proves every assertion. The finite enumerations are **complete** over the stated exact finite domain, rather than extrapolations to higher orders or other alphabets.

## Verification
Place `CHECKER.py` and `CUT_CERTIFICATE.tsv` in the same directory and execute `python3 CHECKER.py` (Python 3 standard library only). It must finish with `ORDER4_DEBRUIJN_ATTRACTOR_PASS cycles=16 cuts=256 min4=192 min5=64` followed by the 8/12/16 robustness histogram. The verifier checks all 65,536 binary words, separately exhausts graph tours, rechecks every cut and all distinct linear factors, constructs five-position witnesses, and compares all 256 reproduced rows to the embedded certificate. The proof's inequality and four-mark uniqueness argument are independent of this computation; the complete finite tables and five-mark witnesses are verified by exact exhaustive algorithms.

## Relationship to prior work
Mantaci, Restivo, Romana, Rosone, and Sciortino analyzed string-attractor bounds for de Bruijn words and exhibited one order-four binary unfolding with minimum attractor \(\{4,8,12,16\}\). Their Proposition 41 concerns general upper/lower bounds, not the full cyclic cut spectrum. Whittington subsequently highlighted the difference between sharp \(k\)-attractors and full attractors and explicitly raised the question of how different cuts and de Bruijn cycles affect the optimum. His prime-order Lyndon construction proves the existence of a suitable cycle for each prime order, but neither that existence theorem nor the single order-four example determines the 16-cycle order-four cut profile calculated here. In particular, the present result does *not* claim any extension to all composite orders or higher alphabets.

## Limitations
The theorem settles only binary order four. It does not prove a general all-order existence or rotation-robustness statement. Its novelty assessment is comparative and may be affected by an equivalent unpublished or unindexed enumeration. The proof uses finite exact enumeration for a genuinely finite classification and has no unverified infinite extrapolation. The result has undergone self-review but not independent audit.

## References
- P. Whittington, *Online String Attractors*, arXiv:2407.15599, first posted 2024-07-22, Section on optimal attractors for de Bruijn sequences (definitions, prime-order existence result, and cut-dependence question). https://arxiv.org/abs/2407.15599
- S. Mantaci, A. Restivo, G. Romana, G. Rosone, and M. Sciortino, *A combinatorial view on string attractors*, Theoretical Computer Science 850 (2021), 236–248, especially Proposition 41 and its order-four example. https://doi.org/10.1016/j.tcs.2020.11.006
