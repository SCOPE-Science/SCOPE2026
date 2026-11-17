# Sharp span-two pair-selecting periods for arbitrary alphabet involutions

## Finding

Let \(\Sigma\) be a finite alphabet and let \(\sigma:\Sigma\to\Sigma\) be an involution with exactly \(f\ge0\) fixed symbols and \(r\ge1\) transposition pairs (so \(|\Sigma|=f+2r\)). For a nonempty cyclic word \(w=w_0\cdots w_{L-1}\), indices are modulo \(L\); its length-two windows are the ordered pairs \((w_i,w_{i+1})\) at all \(L\) positions. The word is **pair-selecting** if those windows are distinct and no window is present together with its coordinatewise involutive image \((\sigma(w_i),\sigma(w_{i+1}))\). In particular, no fixed window may appear.

**Theorem.** The exact maximum length of a pair-selecting cyclic word of span two is
\[
M(f,r)=\begin{cases}
2r(f+r), & f\ge1,\\
2r^2, & f=0\text{ and }r\text{ even},\\
2r^2-1, & f=0\text{ and }r\text{ odd}.
\end{cases}
\]
Every asserted optimum is achieved by an explicitly specified Euler-tour construction. For a fixed-point-free involution, the orbit-count bound is sharp exactly when the alphabet has cardinality divisible by four. With alphabet cardinality congruent to two modulo four its sharp deficit is precisely one.

## Assumptions and scope

All alphabets are finite. The involution acts **coordinatewise**, not by reversing the two coordinates. Cyclic windows wrap from the final symbol to the first, and a cycle of period one is permitted (as in the standard cut-down de Bruijn convention). The displayed theorem assumes \(r\ge1\), i.e. a nonidentity involution. If \(r=0\), every length-two window is fixed, so there is no nonempty admissible cyclic word. Word length and primitive period agree for a pair-selecting word, since a shorter period would repeat a length-two window.

## Proof

**1. Orbit upper bound.** A pair \((x,y)\in\Sigma^2\) is fixed by coordinatewise \(\sigma\) precisely when both coordinates are fixed symbols, hence there are \(f^2\) forbidden fixed windows. The other \((f+2r)^2-f^2\) windows form \(2r(r+f)\) disjoint two-element orbits. At most one window from each orbit is allowed. Therefore \(L\le2r(r+f)\).

**2. The quotient directed multigraph.** Represent each transposition pair by a vertex \(P_i\) (\(0\le i<r\)) and each fixed symbol by a vertex \(F_a\) (\(0\le a<f\)). Label the two members of the \(i\)-th transposition pair by \((i,0)\) and \((i,1)\), with \(\sigma(i,b)=(i,1-b)\). Make one quotient edge for every nonfixed orbit of length-two windows:

- For every ordered \((i,j)\), make exactly two edges \(P_i\to P_j\), labeled \(d=0\) and \(d=1\). The edge labeled \(d\) represents the orbit of \(((i,b),(j,b\oplus d))\), independent of \(b\).
- For each \((a,i)\), make one edge \(F_a\to P_i\) and one edge \(P_i\to F_a\).
- Make no edges between fixed vertices, because those windows are fixed by \(\sigma\).

Call this graph \(H\). Each paired vertex has indegree and outdegree \(2r+f\); each fixed vertex has indegree and outdegree \(r\). Because \(r\ge1\), all its vertices lie in one strongly connected directed component. Thus \(H\) has an Eulerian circuit using exactly \(2r(r+f)\) edges.

**3. Lifting a quotient circuit.** A current letter at \(P_i\) has a bit \(b\). Following a labeled edge \(P_i\to P_j\) with label \(d\) forces the next letter to be \((j,b\oplus d)\), while an edge \(P_i\to F_a\) forces the next letter to be \(F_a\). At \(F_a\), the quotient edge \(F_a\to P_i\) can be lifted using either representative at \(P_i\). Consequently a directed walk in \(H\), starting at a fixed vertex, always lifts to a cyclic word when the walk returns to that fixed vertex. If \(f\ge1\), take an Eulerian circuit starting at \(F_0\): its lift uses exactly one representative of every nonfixed orbit of windows. Hence it is pair-selecting of length \(2r(r+f)\), attaining the upper bound.

**4. The obstruction when there is no fixed vertex.** Suppose \(f=0\). For any cyclic word, label the bit in its \(i\)-th transposition pair as \(b_i\). Each cyclic window has a well-defined quotient edge label \(d_i=b_i\oplus b_{i+1}\). Since the word is cyclic, \(\bigoplus_i d_i=0\). If \(L=2r^2\), every nonfixed window orbit is selected; for each of the \(r^2\) ordered pairs \((P_i,P_j)\), one selected window has \(d=0\) and one has \(d=1\). Therefore \(\bigoplus_i d_i\equiv r^2\pmod2\). For odd \(r\) this contradicts cyclic closure, proving \(L\le2r^2-1\). More generally, the lift of a closed quotient walk in paired vertices closes in the original alphabet exactly when the xor of its edge labels is zero.

**5. Sharpness in both parity cases.** If \(f=0\) and \(r\) is even, any Eulerian circuit of \(H\) has xor of all edge labels \(r^2\equiv0\pmod2\). Starting at either representative of \(P_0\), its lift closes and has length \(2r^2\). If \(r\) is odd, delete from \(H\) the label-one loop \(P_0\to P_0\). Deleting one loop preserves indegree-outdegree balance and strong connectivity (for \(r=1\), the remaining label-zero loop suffices). The remaining graph has an Eulerian circuit of \(2r^2-1\) edges whose label xor is \(r^2-1\equiv0\pmod2\). Its lift is a pair-selecting cycle of length \(2r^2-1\). Together with Step 4 this proves the last case and finishes the theorem.

## Verification

The standalone standard-library program `verify.py` constructs the quotient graph, generates an Eulerian circuit by Hierholzer's algorithm, lifts it to an actual cyclic word, and verifies every cyclic window directly against the involution. It checks all \(56\) pairs \((f,r)\) with \(0\le f\le7\) and \(1\le r\le7\). A separate direct letter-level exhaustive depth-first search (not relying on the quotient graph) checks optimum lengths in the four small instances \((f,r)=(0,1),(0,2),(1,1),(2,1)\), including the exceptional binary case. This is a finite reproducibility check, not the justification for the infinite theorem.

The construction itself is effective: the quotient graph has \(M(f,r)\) edges after the possible one-loop deletion, and an Euler tour plus its lift can be produced in \(O(M(f,r))\) time and space. Canonical labels used in the verifier put fixed symbols first, followed by adjacent swapped-symbol pairs. Any alphabet involution with the same \((f,r)\) is conjugate by a relabeling to this canonical form.

For example, with no fixed symbol, \(r=2\) admits period eight and \(r=3\) admits period seventeen. With \(f=3,r=1\), period eight is attained. The verifier prints explicit witness words.

## Relationship to prior work

Mitchell and Wild, *Negative Avoiding Sequences*, arXiv:2603.25286, published initially on 26 March 2026, prove the corresponding orbit bound is attainable for negation modulo \(k\), where the symbol involution has only one fixed point (odd \(k\)) or two (even \(k\)). In Section 8 they explicitly ask about other alphabet involutions and discuss binary complementing, including its span-two exception. Their Sections 6.1 and 6.2 construct the span-two negation cases. Those results do not imply the general dependence on the number of fixed symbols or the fixed-point-free parity law proved here.

Kari and Xu, *De Bruijn Sequences Revisited* (2012), investigate pseudo de Bruijn words for **antimorphic** involutions, which reverse the order of letters as well as possibly exchanging letters. Their two-letter reverse-orbit problem is mathematically distinct from the coordinatewise morphic involution used here. Alhakim and colleagues' 2024 nonbinary orientable sequences likewise pair a factor with its **reversal**, not with its coordinatewise alphabet image.

The quotient graph is a natural edge-orbit/Euler-tour reduction for this new family; searches of available mathematical research records and the cited primary literature found no published statement giving the above three-case formula. That search is not a proof of absolute novelty.

## Limitations

Only length-two **cyclic** windows are classified; higher spans may exhibit additional constraints. This theorem does not claim enumeration of all extremizing cycles. It makes no assertion about noncyclic pseudo de Bruijn words paired by reversal. One-symbol cycles in the binary exceptional case are admitted by the stated cyclic-window convention. Priority over unindexed prior work remains unconfirmed, and no independent mathematical audit has been performed.

## References

1. C. J. Mitchell and P. R. Wild, *Negative Avoiding Sequences*, arXiv:2603.25286 (first public version 26 March 2026), especially Sections 6 and 8. https://arxiv.org/abs/2603.25286
2. L. Kari and Z. Xu, *De Bruijn Sequences Revisited*, International Journal of Foundations of Computer Science 23 (2012), 1307–1322, especially Section 3. https://doi.org/10.1142/S0129054112400540
3. A. Alhakim, C. J. Mitchell, J. Szmidt and P. R. Wild, *Orientable sequences over non-binary alphabets*, Cryptography and Communications 16 (2024), 1309–1326. https://doi.org/10.1007/s12095-024-00742-x
4. J. Sawada et al., *De Bruijn Sequence and Universal Cycle Constructions*, cut-down de Bruijn sequences overview, https://debruijnsequence.org/db/cutdown (accessed 1 November 2026 UTC).
