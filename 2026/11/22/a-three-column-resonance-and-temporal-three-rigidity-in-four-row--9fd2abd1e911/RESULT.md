# A three-column resonance and temporal-three rigidity in four-row Toom dynamics

## Finding

For synchronous deterministic north-east-center majority on the labelled binary four-row torus of horizontal circumference \(n\ge3\), **the only configurations of least temporal period three are two spatially translating wave families**. They occur precisely when \(3\mid n\). In that case there are exactly six labelled configurations, forming exactly two temporal three-orbits; when \(3\nmid n\) there are none:

\[
\boxed{\#\{x:\ F^3x=x,\ Fx\ne x\}=6\mathbf1_{\{3\mid n\}},\qquad
\#\{\text{primitive temporal three-orbits}\}=2\mathbf1_{\{3\mid n\}}.}
\]

Write \(A=(1,0,1,0)\) and \(B=(0,1,0,1)\) for vertical column words with the first entry at row zero. The two orbits are represented by the column words \((A,A,B)^{n/3}\) and \((A,B,B)^{n/3}\), together with their two horizontal cyclic translates. A single synchronous update shifts either repeating word one column, and three updates return it to itself. No other temporally primitive period-three patterns exist.

## Assumptions and scope

The vertices are \((r,i)\in(\mathbb Z/4\mathbb Z)\times(\mathbb Z/n\mathbb Z)\), with each coordinate labelled. The state \(x_{r,i}\) is binary, and the deterministic update is simultaneous:

\[
(Fx)_{r,i}=\operatorname{maj}(x_{r,i},x_{r+1\bmod4,i},x_{r,i+1\bmod n}),
\]

where the three-input majority is one if at least two inputs are one. Vertical periodicity is four, horizontal periodicity \(n\ge3\), and neither spatial translations nor column permutations are quotiented out. A *primitive temporal three-cycle* is an orbit whose least positive return time is three. As three is prime, the configurations satisfying \(F^3x=x\) that are not fixed by \(F\) are exactly its primitive period-three configurations. No statement about transient times, other primitive temporal periods, noise, or other strip widths is made.

## Proof

Encode each vertical four-bit column by \(u\in\{0,\ldots,15\}\), with row \(r\) at bit position \(r\). For consecutive columns \(u,v\), define the updated column \(f(u,v)\) by

\[
f(u,v)_r=\operatorname{maj}(u_r,u_{r+1\bmod4},v_r).
\]

Thus the column of \(F^3x\) at horizontal site \(i\) depends only on four successive original columns \((a,b,c,d)\); it is exactly

\[
g(a,b,c,d)=f\bigl(f(f(a,b),f(b,c)),\ f(f(b,c),f(c,d))\bigr).
\]

Construct a finite directed graph \(G\) on the \(16^3=4096\) ordered triples \((a,b,c)\). Put the edge

\[
(a,b,c)\longrightarrow(b,c,d)
\quad\Longleftrightarrow\quad g(a,b,c,d)=a.
\]

This is an exact one-to-one *constraint encoding*: every labelled circumference-\(n\) configuration fixed by \(F^3\) corresponds to one indexed closed walk of length \(n\) in \(G\), and vice versa (including the short circumferences \(n=3\)). There are exactly 10,824 directed edges. All are constructed by sixteen-way integer loops in the accompanying standalone certificate; no floating-point or heuristic search is used.

The exhaustive strongly connected component calculation yields six cyclic components, of sizes \(136,8,3,3,1,1\). For every one of these components except the two three-vertex components, each state \((a,b,c)\) obeys \(f(a,b)=a\). Any closed walk contained there therefore represents a configuration fixed after *one* update. The only two exceptional strongly connected components each consist of one simple directed three-cycle, with vertices respectively

\[
\begin{aligned}
&(5,5,10)\longrightarrow(5,10,5)\longrightarrow(10,5,5)\longrightarrow(5,5,10),\\
&(5,10,10)\longrightarrow(10,10,5)\longrightarrow(10,5,10)\longrightarrow(5,10,10).
\end{aligned}
\]

Here column integers \(5\) and \(10\) encode \(A\) and \(B\) as specified above. A finite closed directed walk lies entirely within one cyclic strongly connected component. Hence a closed walk in an exceptional component must have length divisible by three; when that holds, exactly three indexed starting vertices occur per component. The corresponding six configurations are direct three-step horizontal traveling waves and are not one-step fixed. All remaining walks are one-step fixed. This proves the complete classification for every \(n\ge3\).

To make the finite certificate independently checkable, `verify_graph.py` explicitly builds each edge from \(g\), constructs the reverse graph, performs two exhaustive graph traversals to enumerate strongly connected components, checks all internal edges of each cyclic component and each one-step-fixed condition, and verifies both exceptional three-cycles. Its sorted edge-stream SHA-256 is `bee9571a222b202d87194ab67c8a685114cc14b3dea77a2ac79cbee421c98b26`. Each critical all-length inference above depends on this completely finite, reproducible graph calculation and on the elementary closed-walk correspondence, not on a finite-length extrapolation.

## Verification

The two included programs require only standard Python 3 and no third-party packages. Run `python verify_graph.py` for the exact complete graph certificate. It prints the 4,096 states, 10,824 edges, six cyclic-component sizes, the two exceptional three-cycles, and `CHECKS PASSED`. Run `python verify_direct.py` for a distinct, cellwise update enumerator. It exhaustively checks every \(2^{4n}\) binary initial configuration at \(n=3,4,5\), returning fixed / three-step-fixed counts respectively \((22,28)\), \((42,42)\), and \((266,266)\). The latter computation corroborates the formula; only the full finite graph certificate and the proof of the graph correspondence establish the theorem at arbitrary circumference.

## Relationship to prior work

The north-east-center majority rule is classical; this work neither introduces that rule nor claims a new generic transfer-matrix method. The 1988 cylindrical-cellular-automata theory of Jen gives a broad framework for counting spatially periodic and temporally periodic states by finite-state constructions, but its relevant examined sections do not state this exact four-row Toom period-three classification. Makowiec's 1998 preprint treats critical properties of *noisy* two-dimensional Toom models, not this exact deterministic primitive-cycle spectrum. Gács' 2001 manuscript develops erosion and interface properties of Toom dynamics and does not provide the four-row period-three enumeration in its examined results. A related three-row Toom fixed-point result counts stationary configurations, while a three-row period-three classification exhibits much larger temporally recurrent families. Neither statement implies the two-orbit four-row rigidity theorem: strip width and temporally primitive period differ materially. The 1997 paper about Toom ground-state configurations is a plausible historical comparator, but only its abstract was available for examination.

## Limitations

This is a classification only of temporal period three on the *four-row, binary, vertically and horizontally periodic* deterministic Toom strip; other periods, other widths, and transient attraction are not classified. The formal certificate is finite and exact, but independently rerunning the supplied program is not an external mathematical audit. The exact 1997 ground-state article could not be examined in full; despite its stationary-state focus in the abstract, unrecognized earlier equivalent results cannot be excluded. No independent scientific validation has been performed.

## References

1. E. Jen, *Cylindrical Cellular Automata*, Communications in Mathematical Physics **118** (1988), 569–590. https://www.academia.edu/72440176/Cylindrical_cellular_automata
2. D. Makowiec, *Critical properties of Toom cellular automata*, arXiv:cond-mat/9808247v1, first public preprint 1998-08-22. https://arxiv.org/abs/cond-mat/9808247
3. P. Gács, *A Toom rule that increases the thickness of sets*, arXiv:math-ph/0102009v1, first public preprint 2001-02-08. https://arxiv.org/abs/math-ph/0102009
4. D. Makowiec, *Ground-state configurations for Toom cellular automata: Experimental hints*, Physical Review E **56** (1997), 5195–5203. https://doi.org/10.1103/PhysRevE.56.5195 (public abstract examined; full text unavailable).
