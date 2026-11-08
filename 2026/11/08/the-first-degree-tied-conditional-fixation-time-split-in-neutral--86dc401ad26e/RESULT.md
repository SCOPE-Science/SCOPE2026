# The first degree-tied conditional-fixation-time split in neutral evolutionary networks

## Finding

**Theorem.** Consider the neutral discrete-time birth–death Moran process on a connected, simple, undirected, unweighted graph \(G\) of order \(n\ge 2\). Each vertex initially holds one resident, except for one mutant initially at \(v\). At each update, a vertex is selected uniformly for reproduction and replaces a uniformly chosen neighbor. Let \(p_G(v)\) be its eventual all-mutant fixation probability and \(\tau_G(v)\) the expected number of updates until fixation, **conditional on fixation**.

1. On every such graph with \(2\le n\le 4\), vertices of equal fixation probability have equal conditional fixation time.
2. Among the \(21\) isomorphism classes of connected graphs with \(n=5\), **exactly seven** have a pair of vertices of equal fixation probability but different conditional fixation times. A canonical graph-bitmask list (specified below) is \(29,58,62,185,187,221,254\).
3. The path on five vertices \(0-1-2-3-4\) is one witness: \[p_{P_5}(1)=p_{P_5}(2)=\frac17,\qquad \tau_{P_5}(1)=\frac{14650}{329},\qquad \tau_{P_5}(2)=\frac{26955}{658},\] so that \[\tau_{P_5}(1)-\tau_{P_5}(2)=\frac{335}{94}>0.\]

Thus five vertices are **sharp** for fixation-probability-equivalent starting positions with different conditional fixation times. The seven-class count is for *unlabelled* connected simple graphs, not for their labelled presentations.

## Assumptions and scope

The graph is finite, simple, loopless, connected, undirected, unweighted, and has at least two vertices; there is no mutation after initialization. Mutants and residents have identical, fixed reproductive fitness. Time is measured in **all** birth–death updates, including updates that leave types unchanged. The quantity \(\tau_G(v)\) conditions on ultimate all-mutant fixation; it is neither unconditional absorption time nor extinction-conditional time. No conclusion is asserted for selected fitness ratios different from one, for death–Birth updating, for directed or weighted graphs, or for graphs with six or more vertices.

## Proof

Write \(d(v)\) for vertex degree and \(S\) for the set of current mutant vertices. Let \(Z=\sum_{v\in V(G)}1/d(v)\), and define \(h(S)=Z^{-1}\sum_{v\in S}1/d(v)\). For an edge \(uv\), when \(u\) is mutant and \(v\) resident, reproduction from \(u\) into \(v\) has probability \(1/[n d(u)]\) and raises \(h\) by \(1/[Z d(v)]\); the reverse reproduction has probability \(1/[n d(v)]\) and lowers \(h\) by \(1/[Z d(u)]\). These expected contributions cancel edge by edge. Thus \(h(S_t)\) is a bounded martingale. Connectedness and finiteness imply absorption at \(\varnothing\) or \(V(G)\) almost surely: from every nonabsorbing configuration there is a positive-probability finite string of successful type-changing updates leading to absorption. Consequently, by optional stopping, \[\Pr_S(\text{eventual fixation})=h(S).\] For a single mutant this is the known neutral inverse-degree formula \[p_G(v)=\frac{d(v)^{-1}}{\sum_{w\in V(G)}d(w)^{-1}}.\]

For graphs through four vertices, two vertices have equal \(p_G\) precisely when they have equal degree. In each of the nine connected unlabelled graph types on \(2,3,4\) vertices (respectively \(1,2,6\) types), all vertices of any fixed degree lie in one automorphism orbit. An automorphism preserves every birth–death transition and conditional fixation event, hence preserves \(\tau_G\). This proves part 1 without numerical approximation.

For the five-vertex census, let \(\mathcal T\) comprise all nonempty proper vertex subsets and let \(Q_{ST}\) denote the one-step transition matrix restricted to these states. For \(S\in\mathcal T\), put \(u(S)=\mathbb E_S[T\mathbf 1_{\mathrm{fix}}]\), where \(T\) is the first absorption time. First-step conditioning gives the **exact** linear system
\[u(S)=h(S)+\sum_{R\in\mathcal T}Q_{SR}u(R),\qquad u=(I-Q)^{-1}h,\qquad \tau_G(v)=\frac{u(\{v\})}{h(\{v\})}.\]
The inverse exists because all transient states are absorbed almost surely. The transition probabilities are explicitly \(1/[n d(u)]\) for each ordered reproduction event \(u\to w\) along an edge, updating the type at \(w\); no-event updates are included on the diagonal of \(Q\).

For a fully explicit exhaustive certificate, number vertices \(0,\ldots,n-1\) and order the potential edges lexicographically: \((0,1),(0,2),\ldots,(n-2,n-1)\). A graph mask has bit \(j\) set exactly when potential edge \(j\) is present. Enumerate all \(2^{\binom n2}\) masks, discard disconnected graphs, and use the **minimum** mask over all \(n!\) vertex permutations as its isomorphism representative. Solve the rational system above for each representative and test all pairs with equal exact \(h\). The exhaustive standard-library certificate `neutral_moran_census.py` obtains the graph-class counts \(1,2,6,21\) for orders \(2,3,4,5\), respectively; the corresponding numbers with the asserted distinction are \(0,0,0,7\). At order five, precisely the canonical masks \(29,58,62,185,187,221,254\) pass the distinction test. All comparisons use Python's exact `Fraction` arithmetic, so ties and strict inequalities are algebraic, not floating-point tolerances. This proves part 2.

For the path witness, the interior vertices all have degree two and the endpoints have degree one, yielding \(Z=7/2\) and \(p_{P_5}(1)=p_{P_5}(2)=1/7\). Mutants descending from one initial mutant occupy a contiguous interval until extinction or fixation. The independent 14-transient-interval calculation `neutral_moran_path_interval.py` uses exactly the four possible boundary expansion/contraction events, their degree-dependent probabilities, and the same first-step moment equation. Exact elimination yields \(u(\{1\})/h(\{1\})=14650/329\) and \(u(\{2\})/h(\{2\})=26955/658\), a positive difference \(335/94\). This establishes part 3 and sharpness.

## Verification

Run the two standalone scripts using Python 3, without external datasets or non-standard libraries:

```text
python3 neutral_moran_census.py
python3 neutral_moran_path_interval.py
```

The census script independently constructs all labelled graph masks, reduces by all vertex permutations, checks that the known graph-class totals arise, and solves the exact transient-state linear equations. It checks the stated seven canonical masks, the vanishing of the distinction through four vertices, and the exact path values. The second script uses an independently built contiguous-interval transition system and verifies its rational linear-system residuals and witness fractions. Both scripts return `PASS` on the supplied package; the mathematical conclusion does not rely on finite sampling or numerical simulations.

## Relationship to prior work

The conserved inverse-degree reproductive value and the underlying neutral invasion process are established in Sood, Antal and Redner (2008). The finite-state Markov approach to fixation probabilities and times appears in Hindersin and Traulsen (2014) and Hindersin and coauthors (2015); these methods are **not** presented as new. Their cited small-network examples concern graphs through four vertices or the general algorithm, rather than the exact five-vertex classification of degree-tied seeds by conditional time. McAvoy and Hauert (2015) **already establish the qualitative failure** of fixation-probability equivalence to imply equal conditional fixation times, using the twelve-vertex regular Frucht graph; the present theorem neither claims that phenomenon is new nor asserts it first arises on regular graphs. Their example does not establish the minimum over all connected unweighted graphs or the exact seven-of-21 five-vertex census. Möller, Hindersin and Traulsen (2019) enumerate graphs and study graph-averaged fixation probability and conditional time, whereas this theorem concerns comparisons *between vertices of the same graph*. Mohamadichamgavi and Miękisz (2024) use random-graph simulations and mean-field approximations to study placement and degree effects; these do not supply an exact five-vertex isomorphism census. Brewster and colleagues (2026) investigate mixtures of two update rules, bounds, and network classes but do not assert this fixed neutral birth–death five-vertex classification. The exact new claim is the sharp order and the seven-class census, not the known inverse-degree fixation law or the general Markov computation method.

## Limitations

The sharp threshold and seven-class count apply only to neutral birth–death updates on connected unweighted undirected graphs. The explicit numbers measure model updates rather than physical time. No statement about strong selection, biological fitness landscapes, population-size asymptotics, or universal spatial ordering of conditional fixation times is established. Literature databases are incomplete; a pre-existing independent small-graph table or unpublished calculation could affect priority. A general exact algorithm predates this particular classification, although the inspected papers do not report the classification itself.

## References

- Sood, V., Antal, T. and Redner, S. *Voter Models on Heterogeneous Networks*. arXiv:0712.4288, first submitted 27 December 2007; *Physical Review E* **77**, 041121 (2008). https://arxiv.org/abs/0712.4288
- Hindersin, L. and Traulsen, A. *Counterintuitive properties of the fixation time in network-structured populations*. arXiv:1406.4415, first submitted 17 June 2014; *Journal of the Royal Society Interface* **11**, 20140606. https://arxiv.org/abs/1406.4415
- Hindersin, L., Möller, M., Traulsen, A. and Bauer, B. *Exact numerical calculation of fixation probability and time on graphs*. arXiv:1511.02696, first submitted 9 November 2015. https://arxiv.org/abs/1511.02696
- McAvoy, A. and Hauert, C. *Structural symmetry in evolutionary games*. arXiv:1509.03777, first submitted 12 September 2015; *Journal of the Royal Society Interface* **12**, 20150420 (2015). https://arxiv.org/abs/1509.03777
- Möller, M., Hindersin, L. and Traulsen, A. *Exploring and mapping the universe of evolutionary graphs identifies structural properties affecting fixation probability and time*. *Communications Biology* **2**, 137 (2019). https://doi.org/10.1038/s42003-019-0374-x
- Mohamadichamgavi, J. and Miękisz, J. *Effect of the degree of an initial mutant in Moran processes in structured populations*. *Physical Review E* **109**, 044406 (2024). https://doi.org/10.1103/PhysRevE.109.044406
- Brewster, D. A., Huang, Y., Mitzenmacher, M. and Nowak, M. A. *Mixed updating in structured populations*. *PLOS Computational Biology* (30 September 2026). https://doi.org/10.1371/journal.pcbi.1014829
