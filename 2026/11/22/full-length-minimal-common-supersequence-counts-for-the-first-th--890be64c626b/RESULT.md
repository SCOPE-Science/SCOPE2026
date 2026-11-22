# Full-length minimal common-supersequence counts for the first three cyclic permutation alphabets

## Finding

Let \(q\in\{3,4,5\}\), \(k\ge1\), and let \(X=(0\,1\cdots(q-1))^k\) and \(Y=(1\,2\cdots(q-1)\,0)^k\). A common supersequence contains \(X\) and \(Y\) as scattered subsequences. Call it *minimal* if deleting any one symbol destroys the common-supersequence property. Let \(T_q(k)\) be the number of **distinct** minimal common-supersequence words of length exactly \(2qk\). Then

\[
\boxed{T_3(k)=1,\qquad T_4(k)=2^{4k-1},\qquad T_5(k)=F_{10k-1},}
\]
where \(F_0=0\), \(F_1=1\), and \(F_{r+2}=F_{r+1}+F_r\). For \(k=1,2,3\), the respective triples of counts are \((1,1,1)\), \((8,128,2048)\), and \((34,4181,514229)\), indexed by repetition count within each alphabet size. In all cases there are no minimal common supersequences longer than \(2qk\), so the claimed class is the **maximum-length layer**, not the complete set of minimal common supersequences.

## Assumptions and scope

The alphabet has \(q\) pairwise distinct symbols and only the displayed cyclic shifts are considered. Both inputs have \(n=qk\) symbols. An embedding of a word \(U\) in \(W\) is an increasing injection from the positions of \(U\) to equal-letter positions of \(W\). Counts distinguish output words, not masks or alignments. A minimal common supersequence is minimal for the scattered-subsequence partial order, not necessarily shortest by length. Every positive integer \(k\) is included; the theorem makes no assertion for \(q\ge6\) or for the full distribution across shorter minimal lengths.

## Proof

**1. Full-length minimality equals a disjoint, uniquely embedded shuffle.** Let \(U,V\) have lengths \(m,n\), respectively. Any minimal common supersequence \(W\) has length at most \(m+n\): choose one embedding of each input, and delete any position outside their union. At length \(m+n\), the chosen embeddings must be disjoint and partition all output positions, otherwise a position is unused. Moreover, each embedding must be unique. Indeed, if another embedding of \(U\) exists, combining it with the original \(V\)-embedding yields a union smaller than \(m+n\), hence a deletable position. Conversely, a shuffle of the two inputs in which both assigned embeddings are unique is minimal: deleting a position assigned to either input destroys its unique embedding. Distinct successful shuffle masks therefore give distinct words, since a successful word has only one embedding of each input.

**2. Local path criterion for unique embeddings.** Record a shuffle as a lattice path from \((0,0)\) to \((m,n)\), in which an \(U\)-step increments the first coordinate and a \(V\)-step increments the second. Write \(u_i,v_j\) for zero-indexed input letters. The selected embedding of \(U\) is unique precisely when no \(V\)-letter between two consecutive assigned \(U\)-positions (including boundary gaps) can replace an assigned \(U\)-letter. To justify sufficiency, observe that the set of embeddings of one fixed pattern into one fixed host is closed under coordinatewise minimum and maximum: both preserve increasing order and the letter at every pattern index. Given a second embedding, one of these two operations yields a different embedding coordinatewise comparable to the selected one. Choosing the last differing coordinate in a rightward perturbation, or the first differing coordinate in a leftward perturbation, produces a valid one-coordinate replacement. Hence an alternative embedding always implies such a local replacement.

For an \(U\)-step from state \((i,j)\), the immediately preceding and following \(V\)-symbols in the host, if present, are \(v_{j-1}\) and \(v_j\). Thus the step is permissible exactly when \(u_i\ne v_{j-1}\) for \(j>0\) and \(u_i\ne v_j\) for \(j<n\). Similarly a \(V\)-step is permissible exactly when \(v_j\ne u_{i-1}\) for \(i>0\) and \(v_j\ne u_i\) for \(i<m\). This gives a necessary and sufficient local rule for unique embeddings of both inputs, and counts successful masks by lattice-path dynamic programming without ever identifying different outputs.

**3. The offset automata.** Specialize to the displayed inputs, and put \(d=i+j\), \(\delta=i-j\). Away from an input boundary, the \(U\)-step is permitted exactly when \(\delta\not\equiv0,1\pmod q\), while the \(V\)-step is permitted exactly when \(\delta\not\equiv1,2\pmod q\). A \(U\)-step increases \(\delta\) by one, and a \(V\)-step decreases it by one. On the two boundaries, omit only the nonexistent adjacent-letter comparison from Step 2. Starting from \((0,0)\), the branch taking a \(U\)-step first is immediately blocked. Any other offset outside the following live-state tables is either blocked by one of the two forbidden residues or enters a boundary dead end; it cannot reach \((n,n)\). This follows by applying the displayed residue rules and the nonnegative-coordinate and \(i,j\le n\) restrictions: the reachable interior live offsets form the indicated closed transition graphs, and any extra offset is an outward boundary spur with no return transition. The full live transition table is:

| \(q\) | Even \(d\ge2\): live offsets | Odd \(d\ge3\): live offsets | Allowed live edges (offsets) |
|---|---|---|---|
| \(3\) | \(0\) | \(-1\) | \(0\to-1\), \(-1\to0\) |
| \(4\) | \(-2,0\) | \(-1\) | \(-2\to-1\), \(0\to-1\), \(-1\to-2,0\) |
| \(5\) | \(-2,0\) | \(-3,-1\) | \(-2\to-3,-1\), \(0\to-1\), \(-3\to-2\), \(-1\to-2,0\) |

Initially at \(d=1\) only the live state \(\delta=-1\) has one path. At \(d=2\), the counts are \((1)\) for \(q=3\) and \((1,1)\), ordered as the even-offset columns, for \(q=4,5\). All listed edges remain legal until the target boundary; edges leaving the grid are suppressed. These statements can also be checked directly using the residue rules, without any probabilistic or finite-enumeration assumption.

**4. Evaluation of the three transition systems.** For \(q=3\), the live path is unique at every depth, giving \(T_3(k)=1\). For \(q=4\), after \(d=2r\), \(1\le r\le n-1\), each of the two even offsets has \(2^{r-1}\) paths; at \(d=2r+1\) the single odd offset has \(2^r\) paths. This follows by the two-to-one and one-to-two edge pattern. The terminal odd depth \(2n-1\) has \(2^{n-1}\) paths, each with one final legal step, so \(T_4(k)=2^{n-1}=2^{4k-1}\).

For \(q=5\), after depth \(2r\), the counts at offsets \((-2,0)\) are \((F_{2r},F_{2r-1})\). At odd depth \(2r+1\), the counts at \((-3,-1)\) are \((F_{2r},F_{2r+1})\). The transition table gives both identities inductively from the depth-two counts \((1,1)\), because \(F_{2r+1}=F_{2r}+F_{2r-1}\) and \(F_{2r+2}=F_{2r}+F_{2r+1}\). The \(-3\) state is outside the grid at the final odd depth, so the only viable terminal state has \(F_{2n-1}\) paths, each with one final step. Therefore \(T_5(k)=F_{2n-1}=F_{10k-1}\). This completes the proof for every positive \(k\).

## Verification

The portable Python program `verification/grid_count.py` implements the exact local uniqueness rule directly on the full grid without relying on the small-state table. It verified all \(45\) cases \(q\in\{3,4,5\}\), \(1\le k\le15\), including large Fibonacci values. The separate C++ program `verification/exhaustive.cpp` generates *distinct actual shuffle words*, directly tests whether every single-position deletion destroys at least one of the two subsequence embeddings, and agrees for \((q,k)=(3,1),(3,2),(3,3),(4,1),(4,2),(5,1),(5,2)\). Its larger \((5,2)\) case checks \(45,542\) different shuffle outputs and finds exactly \(4,181\) qualifying words. Both programs' recorded outputs appear alongside the source files and can be regenerated with Python 3 and a C++17 compiler. These finite tests support, but do not replace, the all-parameter proof.

## Relationship to prior work

Sopp, Liyanage, Gong and Zhu (2026) give algorithms for computing and enumerating minimal common supersequences of arbitrary two inputs; their general algorithmic method does not imply the three closed counts without analyzing this particular cyclic-shift family. Fraser (1995, Chapter 6.3) develops a general dynamic programming description of minimal common-supersequence lengths and recoverability, likewise without giving these formulas in the inspected sections. Published exact counts for *shortest* common supersequences of repeated reversed permutations concern a different input-pair relation and a different extremal-length criterion. Published binary opposite-run spectra involve a two-letter alphabet rather than these three nonbinary cyclic-shift families. A published classification of the output sets of two alternating binary shuffles does not impose the unique-embedding criterion used here. Thus none of the materially inspected statements implies the present maximum-length counts.

## Limitations

The theorem treats only three alphabet sizes and only the full-length layer, not all minimal-supersequence lengths. It does not claim new general enumeration complexity bounds or rule out undiscovered equivalent presentations. Relevant older works may contain unindexed examples or subsidiary formulas not found in the inspected text. One older publisher version was not separately available in full; the open thesis covers its principal algorithmic results. The verification programs test finitely many parameters, whereas the proof supplies the unbounded-parameter conclusion. No independent external audit has been performed.

## References

- Sopp, Liyanage, Gong and Zhu, *Computing and Enumerating Minimal Common Supersequences Between Two Strings*, arXiv:2603.22591, first posted 2026-03-23. https://arxiv.org/abs/2603.22591
- C. B. Fraser, *Subsequences and Supersequences of Strings*, doctoral thesis, University of Glasgow, 1995, especially Sections 6.3.2–6.4. https://theses.gla.ac.uk/74575/1/10992195.pdf
- Irving and Fraser, *Maximal Common Subsequences and Minimal Common Supersequences*, Combinatorial Pattern Matching, 1994, DOI:10.1007/3-540-58094-8_16.
- *A Binomial Law for Shortest Common Supersequences of Opposite Permutation Powers*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-binomial-law-for-shortest-common-supersequences-of-opposite-pe--980cf845dba3
- *Exact Minimal-Supersequence Spectra for Unequal Opposite Binary Runs*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-minimal-supersequence-spectra-for-unequal-opposite-binary--d41f14eae316
- *Exact Output Languages of Two Alternating Binary Shuffles*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-output-languages-of-two-alternating-binary-shuffles--18f373001e8b
