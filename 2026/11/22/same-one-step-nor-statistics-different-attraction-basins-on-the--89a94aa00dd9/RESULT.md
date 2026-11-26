# Same one-step NOR statistics, different attraction basins on the Shrikhande and rook graphs

## Finding

Let \(R=K_4\square K_4\) and let \(H\) be the Shrikhande graph, both on \(V=\mathbb Z_4^2\), numbered by \(i=4x+y\). For \(S\subseteq V\) put \(F_G(S)=\{v\in V:N_G(v)\cap S=\varnothing\}\). This is synchronous open-neighborhood NOR; in particular, a vertex does not use its own state as input. All states are labelled; temporal orbits are counted modulo time shift, not graph automorphisms.

Both systems have exactly 654 recurrent states, and every state enters recurrence in at most one update. There are explicit, separate permutations \(q\) of the input labels and \(p\) of the output labels with
\[
F_H(q(S))=p(F_R(S))\qquad\text{for every }S\subseteq V.
\]
Thus the full distributions of \((|S|,|F_G(S)|)\) agree, and \(p\) identifies the one-step output supports with their fiber sizes. The output supports are **not** equal on the original shared labels. The basins of the empty/full two-cycles have the same size 53,732 and are identified by \(q\), not by the identity on the original labels. The complete attractor-basin spectra differ:

| Eventual orbit and basin size | \(R\): orbits | \(H\): orbits |
|---|---:|---:|
| Fixed, basin 1 | 0 | 32 |
| Fixed, basin 5 | 24 | 16 |
| Primitive two-cycle, basin 2 | 160 | 144 |
| Primitive two-cycle, basin 10 | 18 | 22 |
| Primitive two-cycle, basin 20 | 120 | 120 |
| Primitive two-cycle, basin 549 | 16 | 16 |
| Primitive two-cycle, basin 53,732 | 1 | 1 |
| **Total fixed / two-cycle orbits** | **24 / 315** | **48 / 303** |

The fixed-point attraction populations are 120 and 112, respectively. The following common output census records the nonempty preimage fibers, grouped by output size:

| Output size | Number of outputs | Size of each fiber |
|---:|---:|---:|
| 0 | 1 | 53,731 |
| 1 | 16 | 548 |
| 2 | 120 | 19 |
| 3 | 320 | 1 |
| 4 | 60 | 5 |
| 6 | 120 | 1 |
| 10 | 16 | 1 |
| 16 | 1 | 1 |

## Assumptions and scope

In \(R\), distinct vertices \((x,y),(u,v)\) are adjacent when \(x=u\) or \(y=v\). In \(H\), adjacency means \((u-x,v-y)\pmod 4\in\{(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)\}\). Both are simple, undirected and 6-regular. The basin of an orbit includes every initial state that eventually visits it, including the states on the orbit. The numerical claims are for these two labelled graphs, not for a general class of strongly regular graphs or for closed-neighborhood NOR.

## Proof

**Recurrence and basins.** For any undirected graph the map \(F=F_G\) reverses inclusion, and \(S\subseteq F^2(S)\) since a vertex in \(S\) has no neighbor in \(F(S)\). Order reversal gives \(F^3(S)\subseteq F(S)\); applying the original inclusion to \(F(S)\) gives the reverse. Thus \(F^3=F\). The image is exactly the set of recurrent states, and \(F\) restricts to an involution there. The basin size of a recurrent orbit \(C\) is \(\sum_{Y\in C}|F^{-1}(Y)|\), since the state after the first update belongs to the eventual orbit.

**Separate input and output relabellings.** In the index order \(0,\ldots,15\), use the permutations given by their values:

```
p = [0,1,9,8,2,3,11,10,12,7,15,4,14,5,13,6]
q = [13,4,12,5,15,6,14,7,3,0,8,11,1,2,10,9]
```

Substitution in the adjacency rules gives \(i\sim_R j\iff p(i)\sim_H q(j)\) for all 256 ordered pairs, as can also be checked by `verify_structural.py`. The resulting isomorphism of bipartite doubles gives \(F_H(q(S))=p(F_R(S))\), hence \(F_H^{-1}(p(Y))=q(F_R^{-1}(Y))\) (where \(q\) acts on each subset in a fiber). In particular \(q\) identifies the two basins of the empty/full cycles, since \(p\) fixes \(\varnothing\) and \(V\).

The distinction from equality on the original labels is concrete. The rook output of \(\{(0,0)\}\) has complement \(N_R((0,0))\), a 6-set with three vertices in row 0. A nonempty Shrikhande input with an output of size ten would have a union of open neighborhoods of size six; this union must equal the neighborhood of any active vertex, as each has size six. Every single Shrikhande neighborhood has at most two points per row, so the displayed rook output is missing from the Shrikhande image. Also \(S=\{0\}\times\mathbb Z_4\) has \(F_R(S)=\varnothing\) but \(F_H(S)=\{2\}\times\mathbb Z_4\). By one-step entry, \(S\) is in the rook empty/full basin and not the Shrikhande one.

**Exact enumeration.** The following finite enumeration specifies the calculation. Write \(N_i\) as the integer mask of the neighbors of vertex \(i\), and \(A=2^{16}-1\). In increasing input order fill the tables \(U[0]=0\) and, for \(s>0\),
\[
b=s\mathbin{\&}(-s),\quad i=\log_2 b,\quad U[s]=U[s-b]\mathbin{\vert}N_i,\quad F[s]=A\mathbin{\mathrm{xor}}U[s];\qquad F[0]=A.
\]
Here \(\&\), \(\vert\), and \(\mathrm{xor}\) denote bitwise operations. The entries \(U[s]\) are exactly the unions of the active vertices' open neighborhoods, by induction on the input order. Incrementing the count for \(F[s]\) once per input produces the fiber counts; incrementing the pair of popcounts of \(s,F[s]\) gives 29 occupied cells, equal between the graphs. There are 654 masks of positive count in each graph, with the eight output types above. Scanning these masks against their output masks gives the following support-size transitions in either graph:
\[
(0,16):1,\ (16,0):1,\ (1,10):16,\ (10,1):16,\ (2,6):120,\ (6,2):120,\ (3,3):320,\ (4,4):60.
\]
The tests \(F[Y]=Y\) give 24 size-four fixed points for \(R\), and 32 size-three plus 16 size-four fixed points for \(H\). As a separate way to count those, test each subset of size three or four for independence and domination, equivalent to being fixed; no other sizes have a same-size transition. The rook fixed configurations are precisely the \(4!\) permutation placements.

**Orbit counts from the census.** Unequal-size transitions yield one two-cycle of basin size \(53731+1\), sixteen of basin size \(548+1\), and 120 of basin size \(19+1\). Of the 320 size-three outputs, all are paired for \(R\) and all but 32 are paired for \(H\), with basin size two for each pair. Of the 60 size-four outputs, 24 are fixed for \(R\) and 16 for \(H\); the others form 18 and 22 pairs with basin size ten. A fixed point has basin size equal to its fiber size, one or five according to its output size. This gives the asserted table and accounts for all \(2^{16}\) initial states in each graph.

## Verification

`python3 verify_direct.py` checks the finite transition/basin census directly from the vertex neighborhoods. `python3 verify_structural.py` uses row and column occupancies for the rook graph (the local test is \(r_i+c_j-2s_{ij}=0\)), checks the double isomorphism and formula on all inputs, and enumerates maximal independent sets separately. Recorded outputs are in `direct_output.txt` and `structural_output.txt`. The proof above also specifies the census directly by a mask-union recurrence, without needing to use the rook-specific row test. The unequal labelled support and basin claims have explicit witnesses in the proof.

## Relationship to prior work

The NOR period bound and fixed-point correspondence with maximal independent sets are known. Brouwer records that the bipartite doubles of the two graphs are isomorphic; agreement of full one-step data up to separate label changes follows from that known fact. The published rook-NOR classification gives the rook-only periodic-state and orbit counts (654 states, 24 fixed points, 315 two-cycles at size \(4\times4\)). Majority-dynamics comparisons for the same graphs concern a different update rule. The finite calculation here resolves how integrating the two bipartite sides back into each labelled automaton changes the recurrence and basin partitions, despite the one-step equivalence: in particular, the two graphs assign different pairings to the size-three and size-four recurrent supports, with distinct fixed-point populations and basin multiplicities. It does not claim the shared bipartite double or rook-only recurrence counts as new, nor absolute publication priority.

## References

1. J. A. Aledo, S. Martinez, and J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, J. Appl. Math. (2015), 594294, https://doi.org/10.1155/2015/594294.
2. J. Aracena, A. Richard, and L. Salinas, *Fixed points in conjunctive networks and maximal independent sets in graph contractions*, https://arxiv.org/abs/1507.06141.
3. A. E. Brouwer, *Shrikhande*, https://aeb.win.tue.nl/drg/graphs/Shrikhande.html.
4. *NOR dynamics on rook graphs: rectangles, matchings, and a square-board gap*, https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-nor-dynamics-on-rook-graphs-rectangles-matchings-and-a-square-bo--c79fc7919f54.
5. *Spectral twins separate under majority dynamics: exact Shrikhande–rook attraction censuses*, https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-spectral-twins-separate-under-majority-dynamics-exact-shrikhande--a7ee2eb89698.
