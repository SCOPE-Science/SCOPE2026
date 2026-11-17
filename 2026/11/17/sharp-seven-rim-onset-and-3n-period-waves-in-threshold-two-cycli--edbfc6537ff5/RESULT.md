# Sharp seven-rim onset and \(3n\)-period waves in threshold-two cyclic wheel dynamics

## Finding

**Theorem (sharp wheel onset and linear-period waves).** Let \(n\ge3\) be an integer, and let \(W_n=K_1\vee C_n\) have one central hub and a labelled rim of length \(n\). Under the synchronous three-colour, threshold-two cyclic cellular automaton defined below:

1. Exactly \(3(n+2)\) configurations are fixed points, for every \(n\ge3\).
2. For \(3\le n\le6\), every orbit eventually reaches a fixed point. At \(n=7\), there are exactly two primitive cycles of length \(21\), and no other nontrivial recurrent cycles; exactly \(168\) of the \(3^8=6561\) initial configurations reach one of those two cycles.
3. For **every** \(n\ge7\), there is a primitive temporal orbit of length exactly \(3n\). One explicit state on such an orbit has hub colour \(1\) and clockwise rim word \(0^{n-4}1122\); after three synchronous updates the hub returns to colour \(1\) and the rim word rotates by one position.

Thus seven is the minimum rim length supporting **any** non-fixed periodic orbit; periods of the explicit wheel waves grow without bound as the rim grows. The theorem does not assert that the explicitly exhibited periods exhaust the spectrum at larger rim lengths.

## Assumptions and scope

All graphs are undirected simple wheels \(W_n\) with \(n\ge3\); a rim vertex has the hub and its two cyclic rim neighbours as three distinct neighbours, and the hub has \(n\) neighbours. Colours lie in \(\mathbb Z/3\mathbb Z\). Let \(x_t(v)\in\{0,1,2\}\). The simultaneous update is
\[
x_{t+1}(v)=\begin{cases}
x_t(v)+1\pmod3,&\#\{u\sim v:x_t(u)=x_t(v)+1\pmod3\}\ge2,\\
x_t(v),&\text{otherwise}.
\end{cases}
\]
The threshold counts **distinct neighbouring vertices** and does not include the vertex being updated. A fixed point has temporal least period \(1\); a primitive period-\(p\) cycle consists of exactly \(p\) distinct configurations. The basin of a periodic orbit includes the orbit itself and all configurations eventually entering it. Words are written in a fixed clockwise rim indexing; a one-step left rotation sends \(c_1\cdots c_n\) to \(c_2\cdots c_nc_1\).

## Proof

**Fixed configurations.** By global colour-rotation symmetry, fix hub colour \(0\). The hub is stable only if there is at most one rim vertex of colour \(1\). A rim vertex of colour \(2\) cannot be adjacent to a rim vertex of colour \(0\): its successor colour is \(0\), and it would then see that neighbour *and* the hub in colour \(0\), forcing an advance. With at most one rim vertex in colour \(1\), a cyclic word containing both \(0\) and \(2\) necessarily contains adjacent \(0\)- and \(2\)-vertices, so is impossible at a fixed point. If no rim vertex has colour \(2\), the rim is all \(0\) or contains exactly one \(1\); all these \(n+1\) words are fixed. If no rim vertex has colour \(0\), the rim is all \(2\) or contains one \(1\); in the latter case that single \(1\) has two rim neighbours of colour \(2\) and would advance, so only the all-\(2\) word is fixed. Therefore precisely \(n+2\) fixed words occur for hub colour \(0\), and three hub colours give \(3(n+2)\).

**An exact three-step travelling wave.** For \(n\ge7\), put \(a=n-4\ge3\), and write a state as (hub, rim word). A direct neighbourhood count gives the following three simultaneous steps:
\[
(1,\ 0^a1^22^2)
\longmapsto(2,\ 0^{a-1}1^32^2)
\longmapsto(0,\ 0^{a-1}1^22^3)
\longmapsto(1,\ 0^{a-1}1^22^20).
\]
The hub can make the three changes because its successor colours occur at least twice at the appropriate times: first the two \(2\)'s, then \(a-1\ge2\) zeros, then two \(1\)'s. Each intermediate rim change occurs only at the forward colour boundary, where the current hub colour supplies the second successor-coloured neighbour. In each step, all other rim vertices have at most one successor-coloured neighbour. The final rim word is the one-step left rotation of the original. The wheel update commutes with every cyclic rotation of its rim; iterating the displayed identity gives hub colour \(1\) and a \(j\)-step rim rotation at time \(3j\). The word \(0^a1^22^2\) has no nontrivial cyclic rotational symmetry (each colour has one nonempty contiguous block). Hence no time \(3j\), with \(0<j<n\), returns to the initial state. The hub advances on each of the three phases, so any return time must be divisible by three. The least return time is therefore exactly \(3n\).

**Sharpness of seven and the complete seven-rim recurrent census.** The only rim sizes smaller than seven permitted by the wheel definition are \(3,4,5,6\). The standalone `exhaustive_finite.py` enumerates every \(3^{n+1}\) labelled state for \(n=3,4,5,6,7\), iterates the precise local update, identifies cycles in the finite functional digraph, and assigns each visited state its eventual period. No sampling, truncation, timeout inference, or heuristic cycle search occurs: a finite orbit is followed until a previously visited state is encountered, and every initially unassigned labelled state is processed. Counts of recurrent cycles by least period are respectively \(\{1:15\}\), \(\{1:18\}\), \(\{1:21\}\), \(\{1:24\}\), and \(\{1:27,21:2\}\). The final size has basins \(\{1:6393,21:168\}\). The separately implemented `independent_checks.py` applies Floyd cycle detection to every integer-encoded state for the same five sizes and reproduces all basin counts. These exhaustive finite computations establish the only remaining finite assertions.

## Verification

The two independently implemented Python 3 programs use different representations: one explicit labelled tuples and full functional-graph traversal, the other base-three integer encoding and Floyd's cycle detector. Execute `python3 exhaustive_finite.py` and `python3 independent_checks.py` in the directory containing this document; exact expected outputs are included as `exhaustive_output.txt` and `independent_output.txt`. The latter also enumerates all fixed states through rim length nine, tests the three-step wave identity at every rim length from seven through 120, and directly checks minimal return times for lengths seven through 20. The unbounded construction is proved symbolically above, not inferred from those finite tests.

## Relationship to prior work

The contact-threshold cyclic cellular automaton is classical. Durrett and Griffeath (1993), especially the introduction and sections on stable periodic objects, study large-range lattice dynamics and spiral-core existence; those results do not enumerate recurrent states of finite wheel graphs or establish the exact seven-rim threshold and explicit \(3n\)-waves. Bello and Sivakoff (2021) treat threshold-at-least-two CCA and GHM on infinite regular trees with random initial conditions, proving probabilistic fluctuation/fixation criteria rather than finite-wheel period laws. Other exact calculations for complete bipartite graphs or friendship graphs concern different graphs; their periods and sharp wheel onset do not imply this theorem. Identifying the same qualitative phenomenon (periodic excitations) does not alone imply the parameter-exact statement here.

## Limitations

The exact seven-rim basin count is computer-assisted but exhaustive and reproducible; the proof does not furnish an independent handwritten classification of its \(6561\) labelled states. The infinite-family construction is analytic, but a complete period spectrum and basin census for \(n>7\) are **not** claimed. No global upper bound on transient length for arbitrary \(n\) is asserted. Literature comparisons support originality only to the extent of indexed and inspected sources; unpublished or poorly indexed wheel-specific work may already contain an equivalent result. Independent mathematical validation has not been performed.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, Experimental Mathematics 2 (1993), 183–208. DOI: 10.1080/10586458.1993.10504277. Public preprint arXiv:patt-sol/9303002, first posted 1993-03-22. Author-hosted full text: https://sites.math.duke.edu/~rtd/reprints/paper79.pdf.
2. J. Bello and D. Sivakoff, *Cyclic Cellular Automata and Greenberg–Hastings Models on Regular Trees*, arXiv:2108.06404, first posted 2021-08-13. Full text: https://arxiv.org/pdf/2108.06404.
