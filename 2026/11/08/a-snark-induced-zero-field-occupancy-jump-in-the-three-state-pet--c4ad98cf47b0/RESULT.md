# A snark-induced zero-field occupancy jump in the three-state Petersen-line Potts antiferromagnet

## Finding

Let \(P\) be the Petersen graph, let \(L(P)\) be its \(15\)-vertex, \(30\)-edge line graph, and let \(\sigma_e\in\{0,1,2\}\) be the Potts state attached to each edge \(e\) of \(P\). With antiferromagnetic coupling \(J>0\), an arbitrary real field \(h\) favoring color \(0\), and \(x=h/J\), define
\[
H_{J,h}(\sigma)=J\sum_{\{e,f\}\in E(L(P))}\mathbf1_{\sigma_e=\sigma_f}-h\sum_{e\in E(P)}\mathbf1_{\sigma_e=0}.
\]
The exact zero-temperature ground energy, for every real \(x\), is
\[
\boxed{\frac{E_0(h)}{J}=\min\{10,\;2-4x,\;2-6x,\;10-10x,\;30-15x\}.}
\]
Its four distinct crossing fields are \(h/J=-2,0,2,4\). The complete favored-color occupancies and ground-state degeneracies (with all three colors labeled) are:

| Field range | Occupancies of color \(0\) | Number of ground configurations |
|:--|:--|--:|
| \(x<-2\) | \(0\) | 1782 |
| \(x=-2\) | \(0,1,2,3,4\) | 17022 |
| \(-2<x<0\) | \(4\) | 300 |
| \(x=0\) | \(4,5,6\) | 1800 |
| \(0<x<2\) | \(6\) | 300 |
| \(x=2\) | \(6,7,8,9,10\) | 11652 |
| \(2<x<4\) | \(10\) | 192 |
| \(x=4\) | \(10,11,12,13,14,15\) | 3123 |
| \(x>4\) | \(15\) | 1 |

The zero-field minimum has precisely two monochromatic line-graph bonds and 1800 configurations: 900 have color-class sizes \((5,5,5)\), and 900 have color-class sizes a permutation of \((4,5,6)\). In particular, a positive arbitrarily small field selects only the 300 zero-field states with six favored-color sites; a negative arbitrarily small field selects only the 300 with four. This contrasts with any properly three-edge-colorable cubic graph on ten vertices, where every defect-free three-edge-coloring has exactly five edges of each color.

## Assumptions and scope

The graph \(P=GP(5,2)\) has vertices \(u_i,v_i\), \(i\in\mathbb Z/5\mathbb Z\), and fifteen edges in the three families \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\). The graph is simple and cubic; \(L(P)\) joins two of these edges precisely when they share an endpoint. Color \(0\) is physically distinguished, whereas colors \(1\) and \(2\) remain labeled distinct spin values. The statements hold for every \(J>0\) and \(h\in\mathbb R\) at strictly zero temperature. No thermodynamic-limit phase transition is claimed.

For an integer occupancy \(0\le k\le15\), write \(F(\sigma)\) for the number of monochromatic bonds of \(L(P)\), and define \(m_k=\min\{F(\sigma):|\{e:\sigma_e=0\}|=k\}\). The complete exact fixed-occupancy table is:

| \(k\) | \(m_k\) | Multiplicity \(g_k\) |
|--:|--:|--:|
| 0 | 10 | 1782 |
| 1 | 8 | 5880 |
| 2 | 6 | 6420 |
| 3 | 4 | 2640 |
| 4 | 2 | 300 |
| 5 | 2 | 1200 |
| 6 | 2 | 300 |
| 7 | 4 | 2520 |
| 8 | 6 | 5520 |
| 9 | 8 | 3120 |
| 10 | 10 | 192 |
| 11 | 14 | 1440 |
| 12 | 18 | 1160 |
| 13 | 22 | 300 |
| 14 | 26 | 30 |
| 15 | 30 | 1 |

## Proof

**Local lower bounds.** At each original cubic vertex, the three incident edges of \(P\) form a triangle in \(L(P)\). If exactly \(r\in\{0,1,2,3\}\) of those edges have color \(0\), the smallest number of monochromatic pairs at that vertex is respectively \(f(r)=1,0,1,3\). Indeed, for \(r=0\), three items are distributed among only two colors; for \(r=1\), the other two can receive the two distinct remaining colors; and the other cases follow directly. For each such \(r\), the three inequalities
\[
f(r)\ge 1-r,\qquad f(r)\ge r-1,\qquad f(r)\ge 2r-3
\]
hold. Summing over the ten original vertices, and observing that the sum of their favored incidences is \(2k\), proves
\[
F(\sigma)\ge \max\{10-2k,\;2k-10,\;4k-30\}.
\]

**Exceptional sector and edge-coloring obstruction.** At \(k=5\), the preceding bound gives only zero. The Petersen graph is not properly three-edge-colorable. One direct proof uses its perfect matchings: in the stated outer/inner/spoke presentation, exactly six perfect matchings exist, one comprising all five spokes and five comprising exactly one spoke. In each case the complementary two-factor is a union of two odd five-cycles. A proper three-edge-coloring would make each color class a perfect matching and would force its complementary two-factor to alternate between the other two colors, contradicting the two odd cycles. Therefore \(F\ne0\). Also \(F\ne1\): one monochromatic pair would mean exactly one of the ten original cubic vertices uses a color twice and omits a different color, while the other nine vertices use all three colors exactly once. The total incidence count of the repeated color would then be eleven, impossible because every edge bearing that color contributes two incidences. Consequently \(m_5\ge2\).

**Attainment.** The following 16 explicit color strings, indexed by \(k=0,\ldots,15\), attain each corresponding lower bound, with the exception \(k=5\), where they attain the proved strengthened bound two. The string positions order the fifteen edges as \((u_i,u_{i+1}),(u_i,v_i),(v_i,v_{i+2})\), in that order for each \(i=0,1,2,3,4\). They can be verified by checking at most thirty pairs per string:

```text
k  witness
0  111121121122212
1  011121121122212
2  010121121122212
3  010120212112211
4  010120212012211
5  001120020212121
6  001120002212101
7  000010021121202
8  000010010012212
9  000010010012102
10 000010101001100
11 000000010001101
12 000000000001101
13 000000000000101
14 000000000000001
15 000000000000000
```

This establishes every \(m_k\) analytically from local inequalities, the Petersen edge-coloring obstruction, and finite explicit witnesses; the full enumeration is needed only for the multiplicities.

**Exhaustive multiplicity certificate.** Set \(U=E(P)\). For every subset \(S\subseteq U\), define \(c(S)\) to be the number of line-graph edges whose two endpoints lie in \(S\). A unique three-color configuration is an ordered disjoint partition \(U=M\sqcup A\sqcup B\), in which \(M\) has color \(0\), \(A\) has color \(1\), and \(B\) has color \(2\). Thus
\[
F=c(M)+c(A)+c(B),\quad k=|M|,\quad
 g_k=\sum_{|M|=k}\;\sum_{A\subseteq U\setminus M}
 \mathbf1_{\{c(M)+c(A)+c(U\setminus(M\cup A))=m_k\}}.
\]
This enumerates \(3^{15}=14,348,907\) distinct configurations, without sampling or omissions. The standalone `VERIFY_PARTITION.cpp` computes all \(c(S)\) exactly by the recurrence \(c(S)=c(S\setminus\{v\})+|N(v)\cap (S\setminus\{v\})|\) on the line graph, then exhausts the displayed partition formula. Independently, `VERIFY_DFS.cpp` grows a three-color assignment edge by edge and accumulates every newly closed monochromatic adjacency. The programs use different edge orderings and distinct enumeration methods, agree on all sixteen exact pairs \((m_k,g_k)\), and both explicitly check the total number of states.

**Field envelope and coexistence.** Each fixed-occupancy sector has minimal field energy \(Jm_k-hk\). Taking the lower envelope of all sixteen affine functions gives exactly the five displayed lines. On the four crossing fields, all equality sectors in the envelope are precisely those recorded in the degeneracy table; summing their \(g_k\) gives the stated totals. Finally, the 1800 zero-field configurations consist of \(g_4+g_5+g_6=300+1200+300\) states. Global permutation of the three colors partitions them into exactly 900 of class-size type \((4,5,6)\) and 900 of type \((5,5,5)\), which is also directly checked by full enumeration.

## Verification

Both C++17 files compile using a standard C++17 compiler with `-O2`. Run:

```sh
c++ -std=c++17 -O2 VERIFY_DFS.cpp -o verify_dfs && ./verify_dfs
c++ -std=c++17 -O2 VERIFY_PARTITION.cpp -o verify_partition && ./verify_partition
```

Each program constructs the Petersen graph from explicit labeled edges, builds its line-graph adjacencies, visits all \(14,348,907\) states, and checks hard-coded independently stated expected counts. Successful terminal markers are `VERIFY_DFS_OK` and `VERIFY_PARTITION_OK`. The second method uses a 32768-entry exact integer subset-edge array and disjoint-subset enumeration, while the first method uses recursive ternary assignments. The displayed witness strings provide an additional short certificate for the fixed-sector minima. The finite exhaustive procedure constitutes a complete finite proof for this explicitly fixed 15-site graph; it establishes no infinite-family statement.

## Relationship to prior work

The correspondence between proper coloring and zero-temperature antiferromagnetic Potts models is classical; Boettcher and Percus, arXiv:cond-mat/0402282, study three-coloring on random graphs, not this fixed Petersen line graph. Shrock and Xu, arXiv:1009.1182, give generalized-field Potts partition functions and evaluate path, circuit, star, complete, and wheel families, but do not evaluate the Petersen line graph's frustrated sectors or its all-field envelope. Ellis-Monaghan and Moffatt, arXiv:1005.5470, establish a general deletion-contraction/\(\boldsymbol V\)-polynomial representation for the field-dependent Potts partition function on arbitrary graphs; such general machinery is fully acknowledged and is not claimed anew. Candráková and Lukoťka, arXiv:1311.0512, explain the edge-coloring and two-factor obstruction and the Petersen graph's two five-cycles, but do not provide the three-state field-specific sector multiplicities. The new evaluated facts here are the explicit sixteen-sector minimum/multiplicity table and its zero-field occupancy jump and four-field coexistence diagram. The graph's uncolorability alone does not determine these counts.

## Limitations

The claim concerns one finite graph, an exactly homogeneous antiferromagnetic coupling and a uniform color-selecting field. It is a ground-energy/degeneracy result, not a statement about a nonanalytic bulk phase transition, finite-temperature dynamics, other Potts values, or disordered couplings. Literature searches and inspection of relevant preprints cannot conclusively exclude an unindexed prior exact enumeration, particularly a field specialization of a previously tabulated multivariate Potts polynomial. No independent external scientific validation has been performed.

## References

- S. Boettcher and A. G. Percus, *Extremal Optimization at the Phase Transition of the 3-Coloring Problem*, arXiv:cond-mat/0402282, first publicly submitted 2004-02-10, https://arxiv.org/abs/cond-mat/0402282.
- R. Shrock and Y. Xu, *Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings*, arXiv:1009.1182, first publicly submitted 2010-09-07, https://arxiv.org/abs/1009.1182.
- J. A. Ellis-Monaghan and I. Moffatt, *The Tutte-Potts connection in the presence of an external magnetic field*, arXiv:1005.5470, first publicly submitted 2010-05-29, https://arxiv.org/abs/1005.5470.
- B. Candráková and R. Lukoťka, *Avoiding 5-circuits in a 2-factor of cubic graphs*, arXiv:1311.0512, first publicly submitted 2013-11-03, https://arxiv.org/abs/1311.0512.
