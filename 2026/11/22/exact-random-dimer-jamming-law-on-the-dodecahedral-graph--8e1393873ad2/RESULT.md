# Exact random dimer-jamming law on the dodecahedral graph

## Finding

Let \(G\) be the twenty-vertex dodecahedral graph, equivalently the generalized Petersen graph \(GP(10,2)\), and run uniform irreversible random sequential **edge-dimer** adsorption. Let \(K\) be the terminal number of accepted dimers. Its complete probability distribution is

| \(k\) | \(\Pr(K=k)\) |
|---:|---:|
| 6 | \(1/3125\) |
| 7 | \(91294494167/2756754000000\) |
| 8 | \(1796566904214749/4862914056000000\) |
| 9 | \(2544405065946811/4862914056000000\) |
| 10 | \(123231298227/1667666000000\) |

All other probabilities are zero. Consequently,
\[
\mathbb E[K]=\frac{42002246692500247}{4862914056000000},
\quad
\Pr(K=10)=\frac{123231298227}{1667666000000}.
\]
The rare minimum-jamming probability \(\Pr(K=6)=5(1/5)^6=1/3125\) also has a direct geometric proof: exactly five independent eight-vertex sets can remain vacant, and each has six disjoint five-way arrival competitions. This identifies the kinetic role of the five inscribed cubes in the regular dodecahedron. Although the graph admits perfect matchings, complete deposition occurs with probability only about \(0.07389447\).

## Assumptions and scope

Use the vertex set \(\{0,1,\ldots,19\}\). For \(i\in\{0,\ldots,9\}\), include the three edges
\[
\{i,(i+1)\bmod 10\},\quad
\{10+i,10+((i+2)\bmod 10)\},\quad
\{i,10+i\}.
\]
These are the thirty distinct edges of \(GP(10,2)\), isomorphic to the graph of the pentagonal dodecahedron. Each edge has one independent, continuously distributed arrival priority with the same law (equivalently an independent rate-one first-arrival exponential clock). Processing edges in increasing priority, a dimer is accepted exactly when both endpoints are then unoccupied; accepted dimers permanently occupy both endpoints. Rejected arrivals have no later effect. The claim concerns the terminal distribution, not finite-time deposition rates or physical binding energies.

The dodecahedron is the natural twenty-site all-pentagon fullerene cage. The finite-size irreversible matching law is a canonical benchmark for pair-exclusion kinetics on a non-bipartite, pentagon-rich cubic network; it is not asserted to model the full chemistry of the carbon cage.

## Proof

**Exact transfer identity.** For an occupied-vertex set \(S\subseteq V\), let
\[
A(S)=\{\{u,v\}\in E:\ u,v\notin S\}.
\]
Let \(F_S(z)\) be the probability generating polynomial for the *number of additional dimers accepted* starting from occupied set \(S\). If \(A(S)=\varnothing\), then \(F_S(z)=1\). Otherwise the next successful dimer is uniformly distributed over \(A(S)\), because all still-available edges have exchangeable remaining first-arrival priorities; any edge previously rejected cannot become available again. Thus
\[
F_S(z)=\frac{z}{|A(S)|}\sum_{e\in A(S)}F_{S\cup e}(z).
\tag{1}
\]
The recursion strictly increases \(|S|\) by two and terminates. Hence it defines each coefficient as a unique exact rational number, without stochastic approximation or unproved extrapolation. The accompanying complete standard-library program evaluates (1) by memoized backward transfer and independently by forward mass transport over occupied masks. Each yields the five rational coefficients displayed above; the backward computation visits exactly \(94940\) reachable masks. The explicit graph and all fraction assertions are contained in `dodecahedron_rsa_check.py`.

**Support and the sharp six-dimer probability.** The inner vertices \(10,\ldots,19\) form two disjoint five-cycles, allowing at most four independent inner vertices. The outer vertices form a ten-cycle, allowing at most five independent outer vertices. An independent set of five outer vertices must be one of the two alternating parity classes; it precludes selecting three inner vertices because the five unblocked inner vertices then form one five-cycle, with independence number two. If four inner vertices are selected, two come from each inner five-cycle; their spokes forbid at least one vertex in each of the two outer parity classes, so only four outer vertices may be independent. Therefore \(\alpha(G)\le8\), with equality witnessed by the explicit sets below. For any jammed matching, all uncovered vertices form an independent set; thus \(20-2K\le8\) and \(K\ge6\). The ten spokes form a perfect matching, so \(K\le10\).

The five independent eight-vertex sets, using the labeling above, are

```
(0,2,5,7,13,14,18,19)
(0,3,5,8,11,12,16,17)
(1,3,6,8,10,14,15,19)
(1,4,6,9,12,13,17,18)
(2,4,7,9,10,11,15,16)
```

They are exhaustive: checking the two inner five-cycles and the two outer alternating classes (or the finite independent-set check in the embedded program) leaves precisely these five sets. For each such set \(U\), the induced graph on the other twelve vertices consists of exactly six disjoint edges. The remaining twenty-four edges each join \(U\) to one of those twelve vertices. A jammed outcome with vacant set \(U\) occurs exactly when each of the six induced edges is earlier than its four incident cross edges. The edge sets in these six races are disjoint and partition all thirty edges, so the six events are independent and each has probability \(1/5\). Thus a specified \(U\) has probability \((1/5)^6\); summing over five disjoint possibilities proves \(\Pr(K=6)=1/3125\) independently of the transfer calculation.

**Remaining exact coefficients.** For \(k=7,8,9,10\), equation (1) and the provided complete finite evaluation determine the coefficients displayed in the table. The independent forward propagation gives the same exact fractions. Its terminal occupied-mask counts, by the final number of dimers, are respectively \(5,420,1310,160,1\) for \(k=6,7,8,9,10\). Every displayed coefficient is strictly positive and their sum is exactly one, so no possible terminal value has been omitted.

## Verification

Run `python3 dodecahedron_rsa_check.py` using Python's standard library. The code independently implements backward rational recursion and forward rational probability flow, asserts exact agreement with all five claimed rational probabilities, checks the number of vertices and edges and cubic degrees, enumerates all size-eight and size-nine independent sets, verifies that each maximum independent set has a six-edge induced perfect matching on its complement, checks the analytical \(5/5^6\) identity, and verifies the exact expectation and normalization. There is no randomized test in the proof. Results were obtained with 94940 distinct backward-transfer masks and the exact terminal-mask counts noted above.

## Relationship to prior work

Penrose and Sudbury [1] formalized dimer random sequential adsorption and general graph vacancy dynamics; their article gives no explicit terminal five-point rational probability distribution for the twenty-site dodecahedron. Pippenger [2] gives earlier general graph adsorption theory, including edge deposition, but the full historical comparison remains limited by unavailable complete text. The classical five-cube compound is well known [3]; the five geometric eight-vertex sets are used here to derive the *kinetic* probability of minimum coverage, not claimed as a new geometric discovery. Published exact dimer-jamming calculations on the ten-vertex Petersen graph concern a different cubic graph and do not imply these dodecahedral values. The present contribution is the evaluated full finite-network law and the direct five-cube kinetic identity, not the general random-priority recursion.

## Limitations

The model assumes identical independent continuous edge-arrival priorities, single-attempt irreversible adsorption, no desorption and no chemical relaxation. It is a finite twenty-site calculation, not a thermodynamic limit, infinite-volume prediction, or realistic first-principles molecular adsorption result. Exact rational arithmetic and the full deterministic recurrence establish the stated finite probabilities; they do not certify historical uniqueness. An inaccessible earlier publication may contain an equivalent evaluated table.

## References

1. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, Annals of Applied Probability **15** (2005), 853–889. First arXiv posting 24 March 2005: https://arxiv.org/abs/math/0503519 . DOI: https://doi.org/10.1214/105051604000000765 .
2. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics **2** (1989), 393–401. DOI: https://doi.org/10.1137/0402034 .
3. E. W. Weisstein, *Cube 5-Compound*, MathWorld: https://mathworld.wolfram.com/Cube5-Compound.html .
4. H. Prinzbach et al., *Gas-phase production and photoelectron spectroscopy of the smallest fullerene, C20*, Nature **407** (2000), 60–63. DOI: https://doi.org/10.1038/35024037 .
