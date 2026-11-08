# Complete regular-set orbit classification for squares of cycles

## Finding
Let \(n\ge5\) and let \(G_n=C_n^2\), with labelled vertices \(\mathbb Z/n\mathbb Z\) and edges at cyclic differences \(\pm1,\pm2\). A nonempty proper subset \(S\subset V(G_n)\) is **\((a,b)\)-regular** when each vertex in \(S\) has exactly \(a\) neighbours in \(S\), and each vertex outside \(S\) has exactly \(b\) neighbours in \(S\).

**Theorem.** Every \((a,b)\)-regular subset of \(G_n\), for all integers \(n\ge5\) and \(0\le a,b\le4\), is obtained by repeating one of the following primitive binary words to length \(n\) and applying a cyclic shift. A \(1\) denotes membership of a vertex in \(S\). A primitive word of length \(d\) contributes exactly \(d\) distinct labelled subsets if and only if \(d\mid n\).

| \((a,b)\) | All primitive words up to rotation | Number of subsets |
|:--|:--|:--|
| \((0,1)\) | `00001` | \(5\mathbf1_{5\mid n}\) |
| \((0,2)\) | `001` | \(3\mathbf1_{3\mid n}\) |
| \((1,2)\) | `00011`, `00101` | \(10\mathbf1_{5\mid n}\) |
| \((1,3)\) | `0011` | \(4\mathbf1_{4\mid n}\) |
| \((2,2)\) | `01`, `000111` | \(2\mathbf1_{2\mid n}+6\mathbf1_{6\mid n}\) |
| \((2,3)\) | `00111`, `01011` | \(10\mathbf1_{5\mid n}\) |
| \((2,4)\) | `011` | \(3\mathbf1_{3\mid n}\) |
| \((3,4)\) | `01111` | \(5\mathbf1_{5\mid n}\) |

All seventeen other parameter pairs admit no nonempty proper regular subset. In particular, **every** nontrivial equitable two-cell partition of a cycle square is periodic with primitive period at most six; the full family has eleven translation orbits distributed over eight parameter pairs.

The two \((1,2)\)-orbits are genuinely distinct even under cycle reflections: `00011` has adjacent selected positions, whereas `00101` has nonadjacent selected positions in the five-periodic pattern. For \((2,2)\), six additional selected-set configurations appear exactly when \(6\mid n\), beyond the two parity classes.

## Assumptions and scope
Graphs are simple and undirected, with the four neighbours \(i-2,i-1,i+1,i+2\) distinct because \(n\ge5\). The two classes \(S\) and \(V\setminus S\) are named: neither class is empty. Binary words are interpreted at the labelled residues in increasing cyclic order; different rotations usually give different labelled subsets. The parameters are inclusive integers between zero and four, with no additional balancing requirement.

## Proof
Write \(c_i\in\{0,1\}\) for the indicator of \(i\in S\). The regularity condition at every \(i\in\mathbb Z/n\mathbb Z\) is equivalent to
\[
 c_{i-2}+c_{i-1}+c_{i+1}+c_{i+2}
 =b+(a-b)c_i.\tag{1}
\]
Rearranging yields the deterministic two-sided recurrence
\[
 c_{i+2}=b+(a-b)c_i-c_{i-2}-c_{i-1}-c_{i+1}.\tag{2}
\]
For each pair \((a,b)\), consider the directed graph whose vertices are all sixteen four-bit states \((u_0,u_1,u_2,u_3)\). A directed edge leads to \((u_1,u_2,u_3,t)\) precisely when
\[
 t=b+(a-b)u_2-u_0-u_1-u_3\in\{0,1\}.\tag{3}
\]
Equation (3) also determines the predecessor's first bit uniquely from its successor, so each state has at most one outgoing and at most one incoming edge. Thus each connected component consists of one directed path or one directed cycle. In particular, any bi-infinite periodic indicator word must follow a directed cycle, and each directed cycle gives exactly one primitive periodic word, up to rotation. Conversely, a repeated cycle word satisfies (1) at every vertex. This is a bijection, valid even when the circumference is smaller than the recurrence span, since the four neighbours remain distinct for \(n\ge5\).

The remaining calculation is finite and completely specified: for each of the 25 possible ordered parameter pairs, evaluate (3) on each of the 16 binary states, discard edges whose computed \(t\) is not binary, and list the nonconstant directed cycles. The resulting exact state-cycle table is precisely the eleven primitive words displayed in the theorem. One-state cycles `0` and `1` are discarded because they encode the excluded empty and full sets. The executable `verify.py` performs this explicit 400-state calculation, compares all eleven cycles against the printed table, and also separately enumerates the graph subsets at small orders. The proof's finite calculation is exhaustive over **all** states and parameter pairs; it does not infer infinite validity from tested graph sizes.

Each table word has least period equal to its printed length \(d\). It can close on a length-\(n\) cycle exactly if \(d\mid n\), and then its \(d\) rotations are distinct labelled subsets. Different directed cycles cannot yield the same subset because the initial four-bit state fixes the entire recurrence. Summing \(d\) over the cycles for each \((a,b)\) gives the counting column and completes the classification.

For added orientation, complementing a set interchanges parameters via \((a,b)\mapsto(4-b,4-a)\); this pairs the listed rows \((0,1)\) with \((3,4)\), \((0,2)\) with \((2,4)\), and \((1,2)\) with \((2,3)\). The two self-complementary pairs \((1,3)\) and \((2,2)\) have precisely the indicated periods.

## Verification
Run `python3 verify.py` with Python 3.8 or later. The program uses only the Python standard library. It checks every one of the 25 four-bit transition graphs (400 potential state transitions), recovers exactly the eleven nonconstant cycles, and independently enumerates every subset of \(G_n\) for \(5\le n\le14\), testing each neighbor count directly. Finally, it directly checks all classified patterns whenever their period divides \(n\), for \(5\le n\le180\). A successful run ends in `VERIFY_OK`.

The exhaustive 16-state calculation is the finite lemma used in the unrestricted proof. Independent small-graph enumeration and the longer-family checks are corroborating tests, not a replacement for that lemma.

## Relationship to prior work
Abdollahi, Bagherian, Jafari, Khatami, Shokoohi and Sobhani (arXiv:2609.09414, first submitted 2026-09-08) determine **existence** of \((a,b)\)-regular sets in arbitrary connected quartic circulants, including this family. Their paper provides modular constructions and nonexistence criteria, rather than the complete set-by-set orbit census and precise multiplicities above. In particular, the modular construction for \((1,2)\) exhibits a five-periodic two-residue class; the present theorem distinguishes two different five-periodic rotation orbits and proves that no other sets occur. Their \((2,2)\) discussion gives a parity-class construction, while the additional six-periodic orbit is enumerated here. We do not claim novelty for the existing existence criteria or for the known \((0,1)\) and \((1,1)\) code-existence cases.

Obradović, Peters and Ružić (2007) give an existence characterization for efficient dominating sets in circulants with two chord lengths; their abstract also describes structure for that narrower \((0,1)\) case. Kwon, Sohn and Chen (2020) address existence of \((1,1)\)-regular sets in quartic circulants. Neither source is used as evidence that equivalent enumeration is impossible; priority for the complete eleven-orbit census is necessarily provisional pending additional bibliographic review. The broader notions of equitable two-cell partitions and perfect two-colourings are mathematically equivalent to \((a,b)\)-regular subsets and have been included in comparison searches.

## Limitations
This result concerns **only** the cycle-square family with chord lengths one and two. It does not classify regular subsets of arbitrary quartic circulants or multicolour equitable partitions. The primitive words are representative of cyclic rotations; neither graph isomorphism or arbitrary colour-swapping nor nonregular subsets are being counted. The small-order restriction \(n\ge5\) is essential to the degree-four adjacency description. Historical priority is not independently established.

## References
1. A. Abdollahi, J. Bagherian, F. Jafari, M. Khatami, Z. Shokoohi and R. Sobhani, *Regular sets of circulant quartic graphs*, arXiv:2609.09414 (first public submission 2026-09-08), https://arxiv.org/abs/2609.09414.
2. N. Obradović, J. G. Peters and G. Ružić, *Efficient domination in circulant graphs with two chord lengths*, Information Processing Letters 102 (2007), 253–258, https://doi.org/10.1016/j.ipl.2007.02.004.
3. Y. S. Kwon, M. Y. Sohn and X.-G. Chen, *Existence of efficient total dominating sets of circulant graphs of degree 4*, Discrete Mathematics 343 (2020), 111742, https://doi.org/10.1016/j.disc.2019.111742.
