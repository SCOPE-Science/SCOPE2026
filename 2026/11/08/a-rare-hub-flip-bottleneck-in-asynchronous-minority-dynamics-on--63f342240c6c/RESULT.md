# A rare hub-flip bottleneck in asynchronous minority dynamics on friendship graphs

## Finding
For each integer \(m\ge1\), let \(F_m=K_1\vee(mK_2)\) consist of \(m\) edge-disjoint triangles sharing a hub \(h\). At each discrete step, choose one of the \(2m+1\) vertices uniformly and replace its binary color by the minority color of its **closed** neighborhood (the vertex and all its neighbors), preserving its current color in a tie. For this graph, all closed neighborhoods have odd cardinality, so ties never occur.

The resulting finite Markov chain has exactly one closed irreducible class and no singleton absorbing configuration. Its recurrent states are precisely the colorings in which **none of the \(m\) triangles is monochromatic**, a set of cardinality \(2\cdot 3^m\). Every starting state hits this class almost surely.

The allowed nontrivial transitions on this class are an exact two-layer graph: each layer is the Cartesian product \(P_3^{\square m}\), and the layers are joined by a matching of \(2^m\) edges between the corners of the two products. Each such edge, and each edge inside a layer, is used with probability \(1/(2m+1)\) per step; the remaining transition probability stays put.

The unique stationary distribution on the recurrent class is uniform. At stationarity, the exact probability that the hub changes color in the next step is
\[
 r_m=\frac{1}{2m+1}\left(\frac23\right)^m.
\]
Thus the stationary long-run mean number of steps per hub change is exactly \((2m+1)(3/2)^m\). For the Markov chain restricted to the recurrent class, its worst-start total-variation mixing time obeys
\[
 t_{\mathrm{mix}}(1/4)\ge
 \left\lceil\frac{2m+1}{4}\left(\frac32\right)^m\right\rceil.
\]
This is an exponential lower bound **on equilibration within a single recurrent class**, not on the time needed to enter the class.

## Assumptions and scope
All vertices and triangles are labeled; \(P_3\) is the three-vertex path. A configuration is a function from the \(2m+1\) vertices to \(\{0,1\}\). The asynchronous rule always chooses one vertex, independently and uniformly at every step. A closed neighborhood includes the selected vertex itself. The induced Markov chain on the recurrent class has transition matrix \(P\), invariant measure \(\pi\), and mixing time
\[
 t_{\mathrm{mix}}(1/4)=\min\{t\in\mathbb N_0:\max_x\|P^t(x,\cdot)-\pi\|_{\mathrm{TV}}\le1/4\}.
\]
No statement concerns synchronous open-neighborhood minority updates, positive-temperature spin flips, or continuous-time clocks.

## Proof
**1. Monotone edge energy.** Let \(E(c)\) be the number of edges with equal-colored endpoints. If a vertex of even degree \(d\) has \(s\) neighbors matching its color, then the inclusive-neighborhood minority rule changes it exactly when \(s\ge d/2\). Upon changing, its edge energy changes by \(d-2s\le0\). The hub has degree \(2m\) and each peripheral vertex degree two. Every triangle has at least one monochromatic edge, so \(E\ge m\), with equality exactly when none of the triangles is monochromatic. If some triangle is monochromatic, changing either of its two peripheral vertices reduces the energy of that triangle from three to one, without changing any other triangle. Hence every state of energy greater than \(m\) admits an energy-decreasing allowed transition and, moreover, a finite sequence of at most \(m\) peripheral changes reaches \(E=m\). Since the state space is finite and energy is nonincreasing, no state with \(E>m\) belongs to a closed communicating class.

**2. Product layers.** Fix the hub color \(h\). In each nonmonochromatic triangle, the paired peripheral colors can be: both opposite \(h\) (symbol \(0\)); first equal \(h\) and second opposite \(h\) (symbol \(1\)); or second equal \(h\) and first opposite \(h\) (symbol \(2\)). A peripheral change preserving the minimum edge energy toggles a symbol between \(0\) and one of \(1,2\), and there are no direct changes between \(1\) and \(2\). Independent peripheral updates produce \(P_3^{\square m}\) in each fixed-hub layer. There are \(2\cdot3^m\) minimum-energy states.

**3. Cross-layer matching and recurrence.** In a minimum-energy coloring, a triangle with symbol \(0\) gives no hub-neighbor matching its color, whereas a triangle with symbol \(1\) or \(2\) gives exactly one such neighbor. The hub has \(m\) matching neighbors exactly when every symbol belongs to \(\{1,2\}\), and otherwise fewer than \(m\). Therefore hub changes are possible exactly at the \(2^m\) corners in each layer. A hub change swaps symbols \(1\leftrightarrow2\) in every coordinate, giving a perfect matching between the two corner sets with \(2^m\) undirected cross-layer edges. Each layer is connected; a cross-layer edge exists for every \(m\ge1\). Thus the entire energy-minimizing set forms one closed communicating class. There are no fixed configurations because every triangle always has an active peripheral vertex in a minimum-energy state, and monochromatic triangles also contain active peripheral vertices. All initial states enter this unique recurrent class almost surely by finiteness and the absence of any other closed class.

**4. Invariant law and stationary hub-flip frequency.** An allowed energy-neutral flip has an inverse at the same vertex; in both directions its transition probability is \(1/(2m+1)\). All nontrivial transition probabilities are symmetric. Irreducibility therefore implies the unique stationary distribution is uniform on the \(2\cdot3^m\) recurrent configurations. In each layer, \(2^m\) of the \(3^m\) states permit a hub flip; the hub is selected with probability \(1/(2m+1)\). This proves the formula for \(r_m\). The stationary ergodic theorem for the indicator of a hub-flip transition gives the asserted inverse-frequency mean spacing between successive hub flips (in the stationary long-run/Palm sense).

**5. Mixing bottleneck.** Let \(A\) be the layer with hub color zero; then \(\pi(A)=1/2\). The stationary conditional probability of crossing from \(A\) to its complement in one step is \(\Phi=r_m\). Start the chain instead from \(\pi(\cdot\mid A)\). By stationarity and a union bound over directed crossings, the probability of having crossed from \(A\) to the opposite layer by time \(t\) is at most \(t\Phi\): indeed, the corresponding unconditioned stationary probability is at most \(t\pi(A)\Phi\), and conditioning on \(X_0\in A\) divides by \(\pi(A)\). Hence
\[
 \left\|\pi(\cdot\mid A)P^t-\pi\right\|_{\mathrm{TV}}\ge\frac12-t\Phi.
\]
The maximal point-start distance is at least this mixture distance by convexity of total variation. Every integer \(t<1/(4\Phi)\) consequently has maximal total-variation distance greater than \(1/4\); taking the first admissible integer yields the claimed ceiling lower bound.

## Verification
`checks/check_scc.py` directly constructs every asynchronous transition from all binary initial configurations for \(1\le m\le4\), computes strongly connected components and closed classes, and checks energy, recurrence, lack of absorbing states, and hub eligibility. `checks/check_product.py` independently implements the update rule and verifies every recurrent transition against the two-layer product description for \(1\le m\le5\), including exact rational hub-flip conductance. Both use Python's standard library only. Captured outputs are `checks/check_scc.log` and `checks/check_product.log`. These finite checks are supplementary: the proof above covers all integers \(m\ge1\).

Run from the extracted package root using `python checks/check_scc.py` and `python checks/check_product.py`.

## Relationship to prior work
Rouquier, Regnault and Thierry (2010, arXiv:1011.5119v1) study precisely the closed-neighborhood, fully asynchronous minority rule, prove the non-increase of the same-color edge energy, and analyze cliques, paths, cycles, and certain trees. Their clique result includes \(m=1\), when the friendship graph is a single triangle, but the inspected treatment does not give the \(m\)-triangle product attractor, its hub-crossing fraction, or the exponential mixing bound for arbitrary \(m\).

The connection to zero-temperature antiferromagnetic spin-flip dynamics is classical. Kim, Kim and Lee (2003, DOI 10.1103/PhysRevE.68.066127) discuss neutral spin flips on the triangular lattice, a different graph family; only an abstract was accessible during the comparison. The count \(2\cdot3^m\) alone should not be treated as the new mathematical contribution: another synchronous, open-neighborhood minority convention on the same friendship graphs has a count of the same cardinality, but a different transition rule. The distinguishing assertion here is the exact **asynchronous irreducible-class geometry**, stationary hub-flip rate, and exponential mixing obstruction.

## Limitations
The lower bound is not accompanied by a matching mixing-time upper bound, so it does not prove the exact mixing-time growth rate. Results are for the binary self-inclusive stochastic update rule on friendship graphs only. No claim is made about novel general conductance inequalities or about historical priority beyond the inspected sources. An unindexed equivalent windmill-graph calculation cannot be ruled out. Independent validation has not been performed.

## References
1. J.-B. Rouquier, D. Regnault, and É. Thierry, *Stochastic Minority on Graphs*, first available 23 November 2010, arXiv:1011.5119v1, https://arxiv.org/html/1011.5119v1.
2. E. Kim, B. Kim, and S. J. Lee, *Nonequilibrium critical dynamics of the triangular antiferromagnetic Ising model*, Phys. Rev. E 68 (2003), 066127, https://doi.org/10.1103/PhysRevE.68.066127.
