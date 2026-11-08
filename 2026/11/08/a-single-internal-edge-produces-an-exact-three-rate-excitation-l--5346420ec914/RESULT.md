# A single internal edge produces an exact three-rate excitation law

## Finding

Let \(G_{p,q}^{+}\), for integers \(p\ge2\) and \(q\ge1\), be the labelled complete bipartite graph \(K_{p,q}\) with one additional edge \(h_1h_2\) joining two specified vertices in its part of size \(p\). Start either the synchronous three-color cyclic cellular automaton (CCA), or the three-state threshold-one Greenberg–Hastings model (GHM), from any colouring \(x:V(G_{p,q}^{+})\to\{0,1,2\}\). Write \(\alpha_C\) for the long-run fraction of CCA updates in which a given vertex changes colour, and \(\alpha_G\) for the long-run fraction of GHM updates in which it goes from state \(0\) to \(1\). These limits exist and are vertex-independent.

**Theorem.** Always \(\alpha_C=3\alpha_G\) and \(\alpha_C\in\{0,3/4,1\}\). Define \(T_j=3^j-3\cdot2^j+3\) and
\[
Z_{p,q}=3(3^p+3^q)-9-6\cdot3^{p-2}+3(2^p-2)(2^q-2),
\]
\[
H_{p,q}=6\cdot3^{p-2}(3^q-2^q)+T_pT_q
 -6(3^{p-2}-2^{p-2})T_q.
\]
Exactly \(Z_{p,q}\), \(3^{p+q}-Z_{p,q}-H_{p,q}\), and \(H_{p,q}\) of the \(3^{p+q}\) labelled initial colourings have CCA rates \(0\), \(3/4\), and \(1\), respectively (and GHM rates \(0\), \(1/4\), and \(1/3\), respectively).

The rate-one event is precisely the union of: (i) the distinguished edge has distinct endpoint colours, and the second part contains the third colour; and (ii) each bipartition class contains all three colours. The rate-three-quarters event is precisely the complement of this rate-one event among colourings whose two partwise colour supports both have size at least two and whose union has size three.

**Sharp book transition.** At \(p=2\), the intermediate rate is impossible, and exactly \(6(3^q-2^q)\) colourings have maximal rate. In comparison, without the internal edge, \(K_{2,q}\) has exactly \(6(3^q-2^q-1)\) colourings of rate \(3/4\), none of rate \(1\), and the remaining colourings of rate zero. Adding the edge sends every previously rate-\(3/4\) colouring to rate \(1\), and activates exactly six previously rate-zero colourings. This holds for every \(q\ge1\).

## Assumptions and scope

The graph is finite, simple, undirected, labelled, and has exactly the edges specified above. Both rules update all vertices simultaneously. CCA updates \(i\to i+1\pmod3\) if a neighbour currently holds \(i+1\pmod3\), otherwise retaining \(i\). GHM updates \(1\to2\to0\) automatically; a vertex in state \(0\) updates to \(1\) exactly if a neighbour is in state \(1\). Excitation counts for GHM refer only to \(0\to1\), not automatic changes. Colourings are counted with each vertex distinguished, with no quotient by graph automorphisms or colour permutation. The theorem concerns asymptotic excitation *rates*, not full transient or period distributions.

## Proof

**1. Cycle-rate reduction.** Gravner–Lyu–Sivakoff (2016, Theorem 3) proves that for any finite connected graph the asymptotic excitation rate of either rule is the maximal mean of a corresponding oriented initial-colour edge form along simple cycles, with zero if all cycle integrals vanish. For CCA, orient an edge \(u\to v\) and set \(w_C(u,v)=0,1,-1\) as \(x(v)-x(u)\pmod3\) is \(0,1,2\). For GHM, \(w_G(u,v)=1\) for \((x(u),x(v))=(0,1)\), \(-1\) for \((1,0)\), and zero otherwise. Define \(\phi(0)=0\), \(\phi(1)=-2\), \(\phi(2)=-1\). For every oriented edge,
\[
w_C(u,v)-3w_G(u,v)=\phi(x(v))-\phi(x(u)).
\]
This telescopes around every closed walk. Therefore corresponding cycle means, and hence excitation rates, differ by the exact factor three.

**2. The only possible maximal means.** For a fixed colouring, replace all *ordinary* vertices of the \(p\)-part having the same colour by one colour-type vertex, and do the same for vertices of the \(q\)-part; keep \(h_1,h_2\) individually. Preserve all cross-part type edges and the exceptional edge \(h_1h_2\). The resulting weighted type graph has at most \(2+3+3=8\) vertices. Every original closed walk maps to a closed walk on this type graph; conversely, every simple type cycle lifts to an original simple cycle by choosing one representative of each type. Decomposing closed walks into simple cycles shows that the two graphs have the same maximal cycle mean.

A simple type cycle has length at most eight. Its CCA circulation is an integer multiple of three because edge increments represent colour changes modulo three. At lengths \(3,4,5,6,7,8\), a strictly positive cycle mean exceeding \(3/4\) is therefore possible only for a fully successor-coloured triangle (mean \(1\)), a fully successor-coloured six-cycle (mean \(1\)), or a seven-cycle with exactly six successor edges and one equal-colour edge (mean \(6/7\)). All triangles use \(h_1h_2\); a rainbow triangle exists exactly when its endpoints have different colours and the opposite part contains the third colour. Every six-cycle uses only cross-part edges; a fully successor-coloured one exists exactly when both partwise supports contain all three colours.

The apparently additional seven-cycle possibility introduces nothing new. Such a cycle uses \(h_1h_2\) and has four vertices in the first part and three in the second. If its unique zero-weight edge is \(h_1h_2\), the other six successive colour steps along the cross-part path force all three colours to occur in both parts, yielding a fully successor-coloured six-cycle. Otherwise \(h_1h_2\) is a successor edge: after orienting it from colour \(0\) to \(1\), the remaining six-edge cross-part path has five successor steps and one equal-colour step. Either its first edge is a successor edge, immediately putting colour \(2\) in the opposite part, or its first edge is the unique zero edge, in which case the third opposite-part vertex has colour \(2\). Thus a rainbow triangle already exists. So absent the two rate-one sources, every cycle mean is at most \(3/4\).

A cross-part four-cycle has circulation of absolute value three if and only if both shores use at least two colours and their combined support is all three colours. To see sufficiency, choose two distinct colours in each shore, with one colour shared and the other two distinct; the resulting four-cycle traverses three consecutive successor steps and one equal-colour edge, in one orientation. Necessity follows by reducing any four-edge colour word with circulation three to this pattern. Such a cycle gives rate \(3/4\). Finally, all cycle integrals vanish if neither a rainbow triangle nor a resonant cross-part square exists: cross-part cycles are generated over integer oriented chains by squares, and cycles using the added edge are generated by a triangle plus cross-part cycles. This exhausts \(0,3/4,1\).

**3. Counting colourings.** A non-resonant colouring must satisfy one of three disjointly countable conditions: (a) the first shore is monochromatic, (b) the second shore is monochromatic and no rainbow triangle exists, or (c) both shores use the same pair of colours, each of them onto that pair. Inclusion-exclusion for (a) and (b), with exactly \(6\cdot3^{p-2}\) rainbow-triangle colourings among monochromatic second shores, gives
\[
3\cdot3^q+3\cdot3^p-9-6\cdot3^{p-2}.
\]
Condition (c) contributes \(3(2^p-2)(2^q-2)\), establishing \(Z_{p,q}\).

There are \(6\cdot3^{p-2}(3^q-2^q)\) triangle-source colourings: choose ordered distinct endpoint colours, colour ordinary first-shore vertices freely, and require the third colour somewhere on the opposite shore. There are \(T_pT_q\) fully supported colourings in both parts, because \(T_j\) counts surjections of \(j\) labelled vertices onto three colours. Their intersection has size \(6(3^{p-2}-2^{p-2})T_q\). Inclusion-exclusion gives \(H_{p,q}\). All other colourings have intermediate rate, completing the three counts.

**4. One-edge transition.** For \(p=2\), the first shore consists only of \(h_1,h_2\). A resonant cross-part square necessarily uses distinct endpoint colours and the remaining third colour in the other shore, hence creates a rainbow triangle. There cannot be a fully supported first shore. Thus the intermediate count is zero, and the maximal count simplifies to \(6(3^q-2^q)\). Without the exceptional edge, the only cycles are bipartite squares and their integer combinations; the square-support condition gives \(6(3^q-2^q-1)\) rate-three-quarters states. The difference consists of the six colourings with opposite shore entirely in the third colour. This proves the sharp comparison.

## Verification

The fixed-size type-graph reduction is exhaustively checked for **all 504** choices of ordered special-endpoint colours, ordinary-first-shore colour support, and nonempty second-shore support, by `scripts/check_type_cycles.py`. For each, the program enumerates every oriented simple cycle of the type graph and directly computes its maximum mean, then independently matches the three-event support criterion. This is an exhaustive finite check of the *universal type reduction*, not sampling graph sizes.

An independent implementation in `scripts/check_dynamics.py` iterates the actual synchronous maps from all initial configurations for ten small graphs, checking orbit-average excitation rates under both rules, the factor-three identity, and every asserted population formula. It checks **13,716** labelled initial configurations. Recorded outputs are in `verification/type_cycles.txt` and `verification/dynamics.txt`. Both checkers use only the Python standard library. Mathematical generality rests on the reduction and proof above; the direct trajectories are corroborating tests.

## Relationship to prior work

The foundational cycle-integral and finite-graph excitation-rate theorem is Gravner, Lyu, and Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (first posted 2016-10-24), Theorem 3. It supplies the general dynamical reduction; the three-rate classification, perturbation criterion and all-parameter counts for \(G_{p,q}^{+}\) are the graph-specific contributions made here. Earlier works by Durrett and Griffeath study CCA/GHM in lattice settings rather than this single-internal-edge graph family. Doba (2018) likewise states a general finite-graph maximum-cycle-density principle, not a specialized census in the accessible abstract.

## Limitations

No transient-time distribution, full periodic-orbit census, or speed of convergence is asserted. Independent scientific audit and exhaustive historical-priority verification have not been performed. A general graph cycle-maximization theorem is an essential previously published ingredient; the present claim does not present it as new. A potentially relevant later general finite-graph treatment was accessible only by abstract, and an unindexed equivalent graph-specific phase count cannot be excluded.

## References

1. J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, 2016-10-24. https://arxiv.org/pdf/1610.07320.
2. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, 1993. https://arxiv.org/abs/patt-sol/9303002.
3. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, *Complex Systems* 27 (2018), 101–126, DOI:10.25088/ComplexSystems.27.2.101; accessible abstract: https://www.complex-systems.com/abstracts/v27_i02_a01/.
