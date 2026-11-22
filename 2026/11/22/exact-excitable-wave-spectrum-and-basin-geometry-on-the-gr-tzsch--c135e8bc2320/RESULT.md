# Exact excitable-wave spectrum and basin geometry on the Grötzsch graph

## Finding

On the eleven-vertex Grötzsch graph, the Mycielski lift \(G=\mu(C_5)\), synchronous three-state, threshold-one Greenberg–Hastings dynamics has precisely **one fixed point and 1,290 primitive nonconstant temporal cycles**. The exact primitive-period census is

| Least period | 1 | 3 | 4 | 7 | 10 |
|---:|---:|---:|---:|---:|---:|
| Primitive orbits | 1 | 700 | 190 | 330 | 70 |

All \(3^{11}=177{,}147\) states enter their ultimate cycle after at most **nine** synchronous updates; this is sharp, with exactly **120** states entering for the first time at update nine, all in the basins of period-four orbits. Thus \(F^{429}=F^9\), and \(F^{428}\neq F^8\).

The unique fixed state is all quiescent and attracts exactly **13,887** starting configurations, a fraction \(1543/19683\). The individual basin-size distribution for all 1,291 attractors is specified exactly by `COUNTS.json`; the complete first-entry-by-period census appears below.

| First periodic entry | Fixed (period 1) | Period 3 | Period 4 | Period 7 | Period 10 | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 2,100 | 760 | 2,310 | 700 | 5,871 |
| 1 | 2,047 | 1,880 | 11,820 | 8,370 | 1,000 | 25,117 |
| 2 | 4,629 | 6,030 | 26,160 | 14,850 | 1,160 | 52,829 |
| 3 | 4,016 | 8,150 | 21,180 | 11,340 | 380 | 45,066 |
| 4 | 3,194 | 6,120 | 16,090 | 6,210 | 0 | 31,614 |
| 5 | 0 | 1,990 | 5,100 | 1,200 | 0 | 8,290 |
| 6 | 0 | 620 | 3,370 | 0 | 0 | 3,990 |
| 7 | 0 | 110 | 3,030 | 0 | 0 | 3,140 |
| 8 | 0 | 0 | 1,110 | 0 | 0 | 1,110 |
| 9 | 0 | 0 | 120 | 0 | 0 | 120 |
| **Total** | **13,887** | **27,000** | **88,740** | **44,280** | **3,240** | **177,147** |

## Assumptions and scope

Label the vertices \(v_0,\ldots,v_4,u_0,\ldots,u_4,w\) by \(0,\ldots,10\), with indices on the five-element groups modulo five. The edge set consists **exactly** of

\[\{v_iv_{i+1},\; v_iu_{i-1},\; v_iu_{i+1},\;u_iw: i\in\mathbb Z/5\mathbb Z\}.\]

There are 11 vertices and 20 distinct undirected edges. A configuration \(x=(x_0,\ldots,x_{10})\) has \(x_i\in\{0,1,2\}\): resting, excited, refractory. Simultaneously at every vertex \(i\),

\[
F(x)_i=\begin{cases}
1,&x_i=0\text{ and some neighbor has state }1,\\
0,&x_i=0\text{ and no neighbor has state }1,\\
2,&x_i=1,\\
0,&x_i=2.
\end{cases}
\]

No noise, delays, forcing, self-neighbors, or threshold above one are present. A state's first periodic-entry time is the smallest \(t\geq0\) for which \(F^{t+p}(x)=F^t(x)\) for some integer \(p\geq1\); its eventual least period is the smallest such \(p\) at this entry. A primitive period-\(p\) orbit contains \(p\) distinct states, and its basin consists of all configurations eventually entering that specific orbit.

## Proof

**Finite exhaustive proof.** Represent a state uniquely by the integer \(s=\sum_{i=0}^{10}x_i3^i\), with \(0\leq s<3^{11}\). The executable `verify_decomposition.py` builds precisely the twenty edges above, checks all degrees and distinct edges, and explicitly evaluates the displayed coordinate formula once at each of the 177,147 states, producing a total function \(F\) on this exact finite state set.

For the functional digraph \(s\longrightarrow F(s)\), initialize the indegree of each state and repeatedly delete every indegree-zero vertex, decreasing its successor's indegree. **Lemma:** the surviving vertices are precisely those on directed cycles. Indeed, every vertex removed is outside a directed cycle, whereas no vertex of a directed cycle can become indegree zero; conversely, any remaining finite digraph of outdegree one and positive indegree everywhere is a union of directed cycles. The code enumerates every surviving cycle and its least length. Reinsert deleted states in reverse order: each gets the period and basin of its unique successor and entry depth one greater than that successor. This is a proof by induction over the elimination order, so the computed cycle and basin census covers **every** initial state without sampling.

The complete computed period-orbit counts are \((1,700,190,330,70)\) for periods \((1,3,4,7,10)\). Their periodic-state count is \(1+3(700)+4(190)+7(330)+10(70)=5{,}871\). The entry-depth histogram is \((5871,25117,52829,45066,31614,8290,3990,3140,1110,120)\) at depths zero through nine. Its sum is exactly 177,147. Summing basin populations by exact cycle gives 13,887 in the zero state, with every other basin size in `COUNTS.json`.

**Sharpness and map identity.** The initial ternary vector \((2,1,1,1,0,2,2,0,0,0,0)\) has integer code 1985. Its successive state codes through update thirteen are recorded in `COUNTS.json`; its first repeated orbit begins at update nine and has least period four. Therefore the global upper bound is sharp. Because the least common multiple of the allowed periods is \(\mathrm{lcm}(1,3,4,7,10)=420\), the global identity is \(F^{429}=F^9\), not an identity with a ten-update shift. More tightly, for each \(p\in\{1,3,4,7,10\}\) and each state \(x\), \(F^{9+p}(x)=F^9(x)\) whenever \(x\) ultimately has least period \(p\). The nine-step witness has \(F^{8+420}(x)\ne F^8(x)\).

The proof of the fixed-basin size also has an independent non-dynamical check. The irrotationality theorem for three-color Greenberg–Hastings dynamics on finite connected graphs (Gravner–Lyu–Sivakoff, 2016, Theorem 3) characterizes eventual quiescence by zero circulation of its antisymmetric initial excitation 1-form on all cycles. Ten fundamental cycles form a basis of the 20-edge, 11-vertex graph's cycle space. `verify_irrotational.py` checks their integer circulations for every initial state and independently obtains exactly 13,887 zero-circulation states. Here the form on an oriented edge is \(+1\) for \(0\to1\), \(-1\) for \(1\to0\), and zero otherwise.

## Verification

Run from the directory containing the embedded files, with Python 3 and no third-party packages:

```text
python3 verify_decomposition.py
python3 verify_trajectories.py
python3 verify_irrotational.py
python3 verify_basecycle.py
```

The first checker independently constructs all transitions and decomposes the functional graph by indegree elimination. The second constructs the graph via independent adjacency formulas, traces each previously unresolved trajectory to a known suffix or a repeated state, and compares the complete depth-period table and basin-size histogram with `COUNTS.json`. Both cover all 177,147 inputs. The third enumerates all inputs and checks a fundamental cycle basis using the published irrotationality criterion, without tracing dynamics. The fourth independently checks the five-cycle baseline.

A relevant comparison is the base five-cycle \(C_5\): the same three-state update has only one fixed point and two primitive period-five orbits, and 153 of 243 inputs extinguish. Mycielski lifting changes the attainable nonconstant periods from \(\{5\}\) to \(\{3,4,7,10\}\), while the extinction fraction falls from \(17/27\) to \(1543/19683\). All comparison values are checked by `verify_basecycle.py`.

## Relationship to prior work

Gravner, Lyu and Sivakoff (2016) establish general excitation/rotation criteria and limiting activity for three-color dynamics on arbitrary connected graphs. Their result is used here to verify extinction through cycle-space circulation, **not** presented as new. Doba (2018) independently studies a maximum-cycle-density criterion for finite-graph Greenberg–Hastings dynamics. Neither inspected source supplies this Grötzsch-specific period-orbit census, transient-depth table or individual basins. Other published finite-graph censuses, including excitation on the twelve-vertex Chvátal graph and the two ten-vertex generalized Petersen graphs, concern different graphs and do not directly imply the numerical Grötzsch classification. The historical-priority search found no exact equivalent, but unindexed calculations remain possible.

## Limitations

This is a finite, exact, computer-assisted classification for one explicitly labelled graph, not a uniform theorem for all Mycielski graphs or a statement about stochastic excitable media. The proof's numerical step relies on complete 177,147-state enumeration by the provided standalone verifiers. Reproducibility and a historical literature search do not constitute an independent external audit or establish an absolute novelty guarantee. No claim is made about a stronger dynamical property than the stated periods, transient times and basin populations.

## References

1. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, publicly available 2016-10-24, arXiv:1610.07320. https://arxiv.org/abs/1610.07320 (Theorem 3 and the update rule).
2. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, *Complex Systems* 27 (2018), 101–124. https://doi.org/10.25088/ComplexSystems.27.2.101 (general cycle-density criterion).
3. J. Mycielski, *Sur le coloriage des graphes*, *Colloquium Mathematicum* 3 (1955), 161–162 (graph construction; bibliographic date only, not used as a day-resolved date).
