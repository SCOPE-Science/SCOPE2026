# The five exact contagion-time layers of optimal Nauru-graph seeds

## Finding

In synchronous irreversible two-neighbor bootstrap percolation on the Nauru graph \(G=\operatorname{GP}(12,5)\), the minimum cardinality of a percolating seed set is \(7\). Among the \(\binom{24}{7}=346{,}104\) subsets of this cardinality, exactly \(12{,}384\) eventually infect every vertex. All have exact completion times between four and eight synchronous updates, with the following exhaustive census:

| Completion updates | One residual tree | Two residual trees | Total |
| --- | ---: | ---: | ---: |
| 4 | 0 | 120 | 120 |
| 5 | 1,872 | 1,416 | 3,288 |
| 6 | 4,968 | 1,488 | 6,456 |
| 7 | 1,224 | 360 | 1,584 |
| 8 | 864 | 72 | 936 |
| **Total** | **8,928** | **3,456** | **12,384** |

Here the residual forest is the graph induced by the vertices *not* initially selected. In particular all 120 minimum-time seeds leave a disconnected residual forest. Precisely 72 have two components with (order, diameter) pairs \((3,2)\) and \((14,6)\), and precisely 48 have pairs \((4,2)\) and \((13,6)\). At the slowest extreme, 576 seeds leave one seventeen-vertex tree of diameter fourteen, 288 leave one of diameter fifteen, and 72 leave a singleton and a sixteen-vertex tree of diameter fourteen.

## Assumptions and scope

Graph vertices are \(u_i\) and \(v_i\) for \(0\le i<12\), with subscripts modulo \(12\). The undirected edges are \(u_i u_{i+1}\), \(u_i v_i\) and \(v_i v_{i+5}\), each listed for every \(i\). The vertex order used by both checkers is \(u_0,\dots,u_{11},v_0,\dots,v_{11}\). The initial seed vertices are active at time zero; at each subsequent integer round, every inactive vertex with at least two already active neighbors becomes active simultaneously and remains active. The completion time is the smallest number of updates until all 24 vertices are active. Counts refer to labeled subsets of the stated graph, not to isomorphism classes or to the number of activation orders.

## Proof

**Equivalence with induced forests.** In any cubic graph, an inactive vertex becomes active at the next update exactly when it has at most one still-inactive neighbor. Thus the remaining inactive vertices undergo simultaneous deletion of all vertices of current degree at most one. A nonempty induced cycle cannot lose a vertex in this process, while a finite forest is completely removed by repeated leaf deletion. Hence a seed set percolates if and only if its complement induces a forest. A tree of diameter \(d\) is removed in exactly \(\lfloor d/2\rfloor+1\) rounds, as follows by peeling all leaves inward toward its center; the time of a forest is the maximum of the component times, with an isolated vertex having time one.

**Sharp cardinality lower bound.** The graph is cubic on 24 vertices with 36 edges. If a seed set \(S\) contains \(k\) vertices and \(e(S)\) induced edges, and its complement is a forest with \(c\) components, then the complement has \(36-3k+e(S)\) edges but also \(24-k-c\) edges. Equating gives \(2k=12+e(S)+c\). For a proper percolating seed, \(c\ge1\) and \(e(S)\ge0\), so \(k\ge7\). For \(k=7\), necessarily \(e(S)+c=2\). Consequently the only possibilities are \((e(S),c)=(0,2)\) and \((1,1)\).

**Exact finite enumeration.** The two complete, standalone verifiers test all \(\binom{24}{7}=346{,}104\) candidate seven-element subsets, without sampling. The Python program constructs all 36 edges as a set, discards candidates with more than one induced seed edge using the proved necessary condition, and then directly simulates the simultaneous infection process until full infection or a fixed point. It counts each successful subset by time and by the complement's number of components. For every extremal-time solution, it independently computes the connected components and tree diameters by graph searches. The C++17 program constructs the three generalized-Petersen edge families, checks complement acyclicity by exact component and edge counts, and simulates activation round by round. These genuinely different selection predicates give the same nine nonzero time/component cells and all five totals above. At least one valid seven-element seed exists (the enumerators explicitly produce 12,384); together with the lower bound, seven is the minimum. All cited finite counts follow because every possible minimum-size seed was checked.

## Verification

Run `python3 verify_nauru_py.py`. Independently run `c++ -O2 -std=c++17 verify_nauru_cpp.cpp -o verify_nauru_cpp && ./verify_nauru_cpp`. Both require only their language's standard library. The Python verifier asserts the complete 346,104-candidate sweep, all five time counts, the nine time/component cells and the five extremal forest shapes; the C++ verifier independently reconstructs the same time/component table and total. All counts are exact integers. The scientific proof is finite for this one specified graph; the checkers do not assert an infinite-family theorem.

## Relationship to prior work

Morris (first arXiv version 2007-02-13) develops minimal bootstrap-percolation seed sets on grids. Rapaport, Suchan, Todinca and Verstraete (2009 online, also LATIN 2008) study threshold-two propagation on cubic graphs and establish general structural/probabilistic dissemination results, not the complete Nauru minimum-seed timing census. Wei and Li (2013) and Gao and coauthors (2015) treat the *decycling number* of generalized Petersen graphs, so the scalar optimum is not presented as novel independent of existing decycling theory. Their general scalar cardinality results do not imply this graph's 12,384 labeled optimal seed sets, exact time layers, or extreme forest shapes. Marcilon and Sampaio (2015) study complexity of maximizing two-neighbor percolation time on grids and other graph classes, not the present labeled finite census.

The Nauru graph also occurs in published records on anti-forcing of perfect matchings and edge-coloring reconfiguration. Those objects are different from initial infected vertex sets. The neighboring established full minimum-feedback-set census for the Desargues graph \(\operatorname{GP}(10,3)\) concerns a different 20-vertex graph and does not imply these counts for \(\operatorname{GP}(12,5)\).

## Limitations

This is an exact statement for the Nauru graph with a specified synchronous update rule. It does not give the total percolating-set polynomial, a theorem for all generalized Petersen graphs, an analytic closed form for the entire 97-orbit classification, or an independently audited publication-priority guarantee. The exact published full text of the directly titled 2013 and 2015 generalized-Petersen decycling papers was not available for detailed comparison; a hidden finite table remains a residual priority risk. A search returning no identical statement is not proof of novelty. Verification and scientific assessment are same-model only, with no independent scholarly audit.

## References

1. R. Morris, *Minimal Percolating Sets in Bootstrap Percolation*, arXiv:math/0702370v1 (submitted 2007-02-13), subsequently Electronic Journal of Combinatorics 16 (2009), R2. https://arxiv.org/abs/math/0702370
2. I. Rapaport, K. Suchan, I. Todinca, J. Verstraete, *On Dissemination Thresholds in Regular and Irregular Graph Classes*, Algorithmica 59 (2011), 16–34; online 2009-04-21. https://doi.org/10.1007/s00453-009-9309-0
3. E. Wei and Y. Li, *Decycling Number and Upper-Embeddibility of Generalized Petersen Graphs*, Acta Mathematica Sinica, Chinese Series 56 (2013), 211–216. https://doi.org/10.12386/A2013sxxb0022
4. L. Gao, X. Xu, J. Wang, D. Zhu, Y. Yang, *The decycling number of generalized Petersen graphs*, Discrete Applied Mathematics 181 (2015), 297–300. https://doi.org/10.1016/j.dam.2014.09.005
5. T. B. Marcilon and R. M. Sampaio, *The maximum time of 2-neighbour bootstrap percolation in grid graphs and some parameterized results*, arXiv:1508.06847v1 (2015-08-27). https://arxiv.org/abs/1508.06847
