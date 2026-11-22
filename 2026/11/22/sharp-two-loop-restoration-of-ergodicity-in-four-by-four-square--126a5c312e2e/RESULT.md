# Sharp two-loop restoration of ergodicity in four-by-four square ice

## Finding

On the labelled \(4\times4\) periodic square-ice lattice, let \(\mathcal I\) be all configurations with exactly two arrows entering and two arrows leaving every site. Let a **face move** reverse one coherently directed elementary square, and let the eight possible **short winding moves** reverse one coherently directed four-edge row or column loop at a *fixed labelled location*. All moves are reversible; a proposed non-directed loop is rejected. The sixteen face moves are always available as types, whereas an arbitrary fixed subset \(R\) of the four horizontal row loops \(H_0,\dots,H_3\) and four vertical column loops \(V_0,\dots,V_3\) may additionally be allowed.

**The exact irreducibility criterion is**
\[
\boxed{\text{The configuration graph is connected}\iff R\cap\{H_0,H_1,H_2,H_3\}\ne\varnothing\ \text{and}\ R\cap\{V_0,V_1,V_2,V_3\}\ne\varnothing.}
\]
In particular the minimal number of designated winding loops is **two**, one of each direction. Every one of the sixteen perpendicular pairs suffices, while every same-direction pair fails. Over all \(2^8=256\) designated subsets, exactly \((2^4-1)^2=225\) give a connected state graph, and the remaining 31 fail. For comparison, the face-only state graph has 69 components; adding one designated winding loop leaves 19 components, two distinct parallel loops leave 11, and two transverse loops leave one. The count \(|\mathcal I|=2970\), and the face-only component count, are known background facts, not claimed as new.

A random walk assigning a positive proposal probability to each permitted face and designated winding move, accepting only directed loops and otherwise staying put, is irreducible precisely in the connected cases. If the chain has positive holding probability it is also aperiodic. **No claim is made about mixing times.**

## Assumptions and scope

The lattice is \(C_4\square C_4\) with vertices \((i,j)\in(\mathbb Z/4\mathbb Z)^2\), 16 distinct labelled vertices and 32 distinct labelled bonds. A horizontal arrow variable \(h_{ij}\in\{0,1\}\) equals one when the arrow goes from \((i,j)\) to \((i,j+1)\); the vertical variable \(v_{ij}\in\{0,1\}\) equals one when the arrow goes from \((i,j)\) to \((i+1,j)\). The square-ice rule is the integer equality
\[
h_{ij}+v_{ij}=h_{i,j-1}+v_{i-1,j}\qquad\text{for all }i,j\in\mathbb Z/4\mathbb Z.
\]
A face at \((i,j)\) has edge set \(\{h_{ij},v_{i,j+1},h_{i+1,j},v_{ij}\}\); its reversal is permitted exactly when its boundary is a directed cycle. Each \(H_i\) is the four horizontal edges in row \(i\). Each \(V_j\) is the four vertical edges in column \(j\). A loop move is allowed only if the four arrows form a directed cycle, clockwise or counterclockwise for faces and either cyclic sense for winding loops. Only these 24 loop *types* are considered. No global choice of a dynamically discovered noncontractible cycle is allowed.

## Proof

**Necessary transverse types.** At any vertical cut the horizontal signed flux \(a=\sum_i h_{ij}\) is independent of the chosen cut by the ice rule; likewise the vertical flux \(b=\sum_j v_{ij}\) is independent of the chosen horizontal cut. Reversing an elementary directed square preserves both. Reversing a designated horizontal row loop changes only \(a\); reversing a designated vertical column loop changes only \(b\). If no horizontal loop is designated, \(a\) is invariant under every allowed move, and configurations with different \(a\) exist. If no vertical loop is designated, the same argument applies to \(b\). Thus a connected move graph requires both types.

**Exact enumeration of the complete configuration space.** Choose the sixteen horizontal bits freely, in \(2^{16}\) ways. In each column \(j\), choose the first incoming vertical bit in two ways and successively impose
\[
v_{ij}=v_{i-1,j}+h_{i,j-1}-h_{ij}\quad(\text{ordinary integer arithmetic}).
\]
Discard any intermediate value outside \(\{0,1\}\) or any nonperiodic column. Combine all viable columns. This exhausts \(\mathcal I\) without duplication, giving exactly \(2970\) states. Every state is explicitly checked against the sixteen ice-rule equalities. The checker `verify_ice_winding.py` performs the exhaustive loops and asserts that count; the independent checker `verify_ice_hypercube.py` generates the same total from a distinct, four-cube parity representation.

**Exact adjacency certificate.** Encode the 32 edge directions as bits. For each of the 16 face supports and eight designated length-four winding supports, toggle those four positions in a state \(s\) to get \(s\oplus M\). This yields another ice-rule state precisely when the corresponding length-four cycle is directed: at its four vertices the two toggled incident arrows must include one entering and one leaving, which is equivalent to a directed circuit. Construct every such edge and apply a disjoint-set union algorithm to all \(2970\) states. The complete face-only graph contains \(8768\) undirected edges and has exactly \(69\) connected components. For each single designated winding loop there are exactly \(19\) components. For any pair of different parallel loops there are exactly \(11\) components, and for any perpendicular pair there is exactly **one**. The checker then repeats connectivity testing for **all 256** designated subsets, obtaining the claimed equivalence and \(225\) connected subsets. All counts are exact integer operations, not randomized tests.

**Independent implementation and completion.** The second supplied checker represents \(C_4\square C_4\cong Q_4\) through Gray-coded coordinate cycles. It independently chooses two outgoing arcs at each of eight even-parity four-cube vertices (six possibilities per vertex), then checks the eight odd-parity indegree conditions. It obtains exactly \(2970\) ice states; categorizes the 24 four-cube squares into 16 elementary faces and eight short winding circuits; and independently computes all 256 component counts. The two checks agree. Necessity was proved above; connectivity for each of the 16 minimal perpendicular pairs follows exhaustively; and adding permitted moves cannot disconnect a graph. Hence the if-and-only-if claim holds for every subset \(R\).

These are finite exhaustive proofs for a single labelled graph, not numerical evidence for a theorem at all torus sizes.

## Verification

With Python 3 and only its standard library, run `python3 verify_ice_winding.py` and `python3 verify_ice_hypercube.py` in the directory containing the supplied files. Both scripts reconstruct the complete state space and the actual allowed directed moves. The first validates every one of 256 update repertoires. The second uses a separately formulated \(Q_4\) edge-orientation enumeration and checks the same exact criterion. The tests report the configuration count 2970, face-only components 69, one-loop components 19, same-direction two-loop components 11, transverse two-loop components 1, and 225 connected repertoires. Neither requires external data, floating-point arithmetic, random seeds or a network connection.

## Relationship to prior work

Barkema and Newman (1997) develop loop-based ice-model Monte Carlo algorithms; their general loop choices are not the *fixed pair of specified four-edge winding cycles* considered here. The homology and facial-flip theory of Zhang and Qian (2020) explains why face moves cannot cross winding classes, but does not imply that any *one specified row loop plus any one specified column loop*, conditioned on being directed, is enough to connect all 2970 labelled states. Borodin and Bufetov (2015) treat another toroidal six-vertex Markov dynamics. Kondákor and Penc (2023) explicitly describe flux sectors and their alteration by loops crossing periodic boundaries and enumerate 16-site flux sectors, but do not give this sharp designated-loop generator criterion or the 256-repertoire census. The published finite face-reversal census *Exact face-reversal sectors and metric centers of the four-by-four square-ice torus* already determines 69 face-only components and 2970 configurations; these baseline facts are **not novel claims** here. The contribution is the sharp minimal fixed-loop selection law, with exhaustive reproducible evidence.

## Limitations

This statement concerns only the labelled 4-by-4 periodic square lattice, non-directed-move rejection, and the listed 24 length-four loop types. It does not extend to other lattice sizes, longer or arbitrary winding circuits, open boundaries, noisy or nonuniform dynamics, continuous-time rate choices, or estimates of mixing speed. Aperiodicity requires an explicit holding rule. No independent scientific audit has been carried out, and historical-priority review cannot exclude all earlier finite-size simulations or unindexed equivalent classifications.

## References

1. G. T. Barkema and M. E. J. Newman, *Monte Carlo simulation of ice models*, arXiv:cond-mat/9706190 (first public 18 June 1997), journal version *Physical Review E* 57 (1998), 1155–1166.
2. W. Zhang and J. Qian, *Flips on homologous orientations of surface graphs with prescribed forbidden facial circuits*, arXiv:2011.07481 (2020).
3. A. Borodin and A. Bufetov, *An irreversible local Markov chain that preserves the six vertex model on a torus*, arXiv:1509.05070 (2015).
4. M. Kondákor and K. Penc, *Crystalline phases and devil's staircase in qubit spin ice*, arXiv:2305.08571 (2023), *Physical Review Research* 5, 043172; see flux-sector discussion and Appendix A.
5. *Exact face-reversal sectors and metric centers of the four-by-four square-ice torus*, published finite-model research record, 8 November 2026 (used for comparison and deduplication of the known face-only component census).
