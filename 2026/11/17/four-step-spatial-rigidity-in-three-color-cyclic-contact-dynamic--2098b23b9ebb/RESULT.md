# Four-step spatial rigidity in three-color cyclic contact dynamics on two-row Moore tori

## Finding

For every integer \(n\ge3\), the three-color cyclic-contact automaton on the labelled periodic two-row Moore lattice has

\[
P_4(n)=24\mathbf1_{4\mid n},\qquad C_4(n)=6\mathbf1_{4\mid n},
\]

where \(P_4(n)\) is the number of configurations of **least temporal period four** and \(C_4(n)\) is the number of temporal four-orbits before quotienting by spatial translations. Consequently,

\[
\#\operatorname{Fix}(F_n^4)=3+24\mathbf1_{4\mid n}.
\]

There is complete **spatial rigidity**: every primitive four-periodic configuration has identical rows, each equal to a repetition of one of the 24 four-symbol words obtained by taking the word `2100`, optionally reversing it, cyclically shifting it and adding a constant modulo three. All have least spatial period four. One synchronous update is a spatial translation by one column, with direction determined by the orientation. For each circumference divisible by four there are precisely six temporal orbits and two wave orientations.

## Assumptions and scope

Vertices are indexed by \((r,j)\in\mathbb Z_2\times\mathbb Z_n\), with \(n\ge3\), and have color in \(\mathbb Z_3\). The distinct neighbors of \((r,j)\) are \((1-r,j)\), plus \((s,j-1)\) and \((s,j+1)\) for both \(s\in\mathbb Z_2\), with the second coordinate reduced modulo \(n\). These are five distinct neighboring vertices. The full eight-offset Moore convention on the quotient duplicates some incidences but, at successor threshold one, produces exactly the same dynamics.

Writing \(x_v\) for the color at a vertex, the simultaneous update is

\[
(F_nx)_v=\begin{cases}x_v+1\pmod3,&\exists w\sim v:\ x_w=x_v+1\pmod3,\\ x_v,&\text{otherwise.}\end{cases}
\]

The theorem concerns **immediate periodic configurations**; no claim is made about their attraction basins or the complete eventual period spectrum.

## Proof

**Step 1: every vertex must have the same activity type.** Assume \(F_n^4x=x\). During the four updates, each vertex advances either zero or three times, since each advance adds one modulo three and the total must be divisible by three. A vertex advancing zero times is constant over the four sampled time slices. A neighbor advancing three times visits every one of the three colors in those slices, including the constant vertex's successor color; the latter vertex would then be forced to advance, a contradiction. Connectedness therefore forces all vertices either to advance zero times or to advance three times. In the first case, any edge with unequal endpoint colors forces one endpoint to advance, and connectedness leaves only the three monochromatic fixed points.

**Step 2: a finite spatial transfer encodes the active case completely.** If every vertex advances three times, its four-time trace is determined uniquely by its initial color \(c\in\mathbb Z_3\) and one hold time \(h\in\{0,1,2,3\}\). Thus each site has 12 possible four-time traces; a two-row spatial column has \(12^2=144\) temporal column states. Let \(A,B,C\) denote three consecutive column states, each specifying all colors at four times. Declare this triple admissible when, at every time and for both rows of center column \(B\), its next listed color agrees with the successor-contact rule using the opposite row of \(B\) and both rows of \(A,C\).

Take a directed graph whose vertices are ordered column pairs \((A,B)\), with edge \((A,B)\to(B,C)\) precisely for admissible triples. It has \(144^2=20736\) vertices. The finite exhaustive construction in `verify_transfer.cpp` gives exactly 20,340 edges and 20,718 strongly connected components. Its **only cyclic strongly connected components** are six directed simple four-cycles. These numerical finite statements are independently rederived using successor-bitmasks and a separate graph traversal in `verify_masks.py`. Both check the complete finite construction, not a bounded set of torus widths.

Any torus of circumference \(n\) defines a closed walk of length \(n\) in this graph by listing its temporal columns around the ring. Conversely, each such closed walk defines one four-periodic configuration uniquely, because temporal histories and all local update constraints are explicitly encoded. Every closed walk lies in one of the six four-cycle components. Hence closed walks exist only when \(4\mid n\), and then each of the six components has four choices of a starting pair, yielding exactly 24 active configurations. These are all of least temporal period four because every site has exactly three changes in four updates and cannot be fixed or two-periodic.

**Step 3: identify the configurations.** The certificate reconstructs the four-column pattern at each of the 24 cyclic vertices. For every pattern the two rows agree, and the set of common rows is exactly the 24 distinct cyclic shifts, phase shifts and reversals of `2100`. Direct substitution shows that the update rotates each such row one column clockwise or counterclockwise, with four updates giving the identity. None has a smaller spatial period. The six temporal orbits follow by dividing the 24 labelled states by four. This completes the proof for all \(n\ge3\).

## Verification

Three separate, reproducible checks are included.

- `verify_transfer.cpp` constructs all \(144^3\) candidate triples, rejects invalid local histories, computes strongly connected components with iterative Kosaraju, and asserts the precise cyclic-core classification and list of 24 wave patterns.
- `verify_masks.py` independently constructs the full transfer graph using eight-bit successor-contact masks and a separate standard-library graph implementation, checking that the 20,340 edges lead to six four-vertex cyclic components.
- `verify_direct.cpp` independently applies the original cellular automaton to **every** initial configuration for each circumference from three through seven, verifying the exact values \(3,27,3,3,3\) of \(\#\operatorname{Fix}(F_n^4)\).

Compile the two C++17 programs using `g++ -std=c++17 -O2` or `-O3`, respectively, and run `python3 verify_masks.py` with Python 3. The complete outputs `transfer_output.txt`, `masks_output.txt`, and `direct_output.txt` are supplied. The transfer argument, not the direct finite-width enumeration, is the all-circumference proof.

## Relationship to prior work

Fisch, Gravner and Griffeath (1991) introduced two-dimensional cyclic cellular automata, topological defects and periodic wave clocks, focusing primarily on the planar nearest-neighbor setting and large periodic computational boxes. Durrett and Griffeath (1993) study periodic wave activity more generally. Gravner, Lyu and Sivakoff (2016) establish an arbitrary-graph circulation characterization of asymptotic excitation rates for three-color cyclic automata. Those results supply the conceptual setting but do not enumerate immediate period-four states on this particular five-distinct-neighbor two-row graph, nor do they state the constant 24-state classification and row-equality rigidity. In particular, an asymptotic rate description does not by itself identify the exact finite set of states recurring after precisely four updates.

Other exact cyclic-contact results on square ladders, complete multipartite graphs or at different contact thresholds concern different adjacency structures, dynamical periods or parameter regimes and do not imply this two-row Moore classification. The elementary period-three sector on the same geometry is not being enumerated here.

## Limitations

The result uses exactly three colors, threshold-one successor contact, the two-row periodic Moore quotient and integer circumferences at least three. It does not extend automatically to four-neighbor square ladders, different thresholds or different colors. It classifies configurations already periodic at time zero, not those eventually attracted to them. Literature retrieval and exact-claim comparisons reduce but do not eliminate the risk of an unindexed earlier equivalent enumeration. Independent mathematical review has not yet been performed.

## References

1. R. Fisch, J. Gravner, and D. Griffeath, *Cyclic Cellular Automata in Two Dimensions*, in *Spatial Stochastic Processes*, 1991, pp. 171–185. https://www.math.ucdavis.edu/~gravner/papers/cca.pdf
2. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, archival preprint publicly submitted 1993-03-22. https://arxiv.org/abs/patt-sol/9303002
3. J. Gravner, H. Lyu, and D. Sivakoff, *Limiting Behavior of 3-Color Excitable Media on Arbitrary Graphs*, archival preprint publicly submitted 2016-10-24. https://arxiv.org/abs/1610.07320
