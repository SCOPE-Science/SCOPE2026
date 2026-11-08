# Sharp dimension-five onset of primitive seven- and fourteen-cycles in cubical excitation

## Finding

For every integer \(d\ge 1\), let \(Q_d\) be the Boolean hypercube, equipped with synchronous threshold-one, three-state Greenberg–Hastings dynamics. **There is a primitive period-seven orbit on \(Q_d\) if and only if \(d\ge 5\), and likewise a primitive period-fourteen orbit if and only if \(d\ge 5\).**

Both positive constructions lie in a particularly small invariant family: the configurations depending only on one coordinate, the Hamming weight of two other coordinates, and the Hamming weight of two further coordinates. Their dynamics reduce exactly to the eighteen-vertex rectangular grid \(P_2\square P_3\square P_3\). The two periods are verified by explicit full-cycle state lists on this quotient, and they persist in every higher-dimensional cube.

This is a sharp dimension threshold for **these two specified primitive periods**. It is not a classification of all periods or attraction basins in dimensions five and higher.

## Assumptions and scope

The vertices of \(Q_d\) are binary words \(v=(v_0,\ldots,v_{d-1})\in\{0,1\}^d\). Two vertices are adjacent if they differ in exactly one coordinate. States are maps \(x:V(Q_d)\to\{0,1,2\}\). At each discrete update, a resting vertex (state zero) becomes excited (state one) if and only if at least one neighbor is currently excited; an excited vertex becomes refractory (state two); a refractory vertex becomes resting. The update is fully synchronous. A primitive period-\(p\) orbit consists of \(p\) distinct states \(x,F(x),\ldots,F^{p-1}(x)\), with \(F^p(x)=x\).

Define the finite index set
\[
H=\{0,1\}\times\{0,1,2\}\times\{0,1,2\}.
\]
A state on \(H\) is encoded by an eighteen-character ternary word \(w_0w_1\cdots w_{17}\). The index of \((a,b,c)\) is \(9a+3b+c\) (last coordinate varies fastest). The graph on \(H\) joins tuples differing by one in exactly one of the three coordinates. This is the Cartesian product of paths with two, three and three vertices. The two witness words, in this index order, are:

- period seven: `000122010000221010`;
- period fourteen: `021001002200100210`.

## Proof

**1. Invariant weight quotient.** For \(d\ge5\), define
\[
\pi(v)=\bigl(v_0,\ v_1+v_2,\ v_3+v_4\bigr)\in H,
\qquad (L_d z)_v=z_{\pi(v)}.
\]
This is an injective map from ternary states on \(H\) into states on \(Q_d\): every tuple in \(H\) is achieved by some binary word. Each edge of the quotient graph corresponds to at least one binary-coordinate flip from every vertex of the relevant fiber, and every flip among the first five coordinates maps either to one of these quotient edges. A flip of an extra coordinate leaves \(\pi\) unchanged. Consequently, whenever \((L_dz)_v=0\), such extra neighbors also have state zero; they cannot produce an excitation. For states one and two the update is independent of neighbors. The local rule therefore proves the exact intertwining identity
\[
F_{Q_d}\circ L_d=L_d\circ F_H\quad\text{for every }d\ge5.
\]
As \(L_d\) is injective, it preserves the **least** period of every periodic quotient configuration.

**2. Explicit two cycles.** The files `data/period7_trace.txt` and `data/period14_trace.txt` give, respectively, seven and fourteen pairwise distinct eighteen-character words. For each consecutive pair, including the last to the first, direct evaluation of the stated local rule on \(H\) yields the second word. Thus the first list is a primitive seven-cycle and the second a primitive fourteen-cycle. In each case the period is proved by closure and pairwise distinctness, not by merely observing recurrence at a multiple of the period. The intertwining identity gives primitive periods seven and fourteen on every \(Q_d\) for \(d\ge5\). The five-cube lifts of the two initial words, encoded by vertex labels interpreted as five-bit integers from zero to thirty-one, are `00121200002222110022221100212100` and `02010102200000012000000110101020`.

**3. Lower-dimensional exclusion.** There are exactly \(3^{2^d}\) labelled states on \(Q_d\). The direct exhaustive script `tools/check_witnesses.py` constructs all of the \(9\), \(81\), and \(6561\) states for \(d=1,2,3\), obtaining primitive periods \(\{1\}\), \(\{1,4\}\), and \(\{1,3,4\}\), respectively. Two separate exhaustive implementations for \(d=4\), `tools/q4_dfs.c` and `tools/q4_peel.c`, enumerate all \(43,046,721\) states. The first classifies the functional digraph by forward depth-first traversal with cycle detection, while the second directly decodes ternary states and uses indegree peeling followed by cycle classification. Both independently obtain precisely one period-one orbit, \(292,616\) period-three orbits, \(13,190\) period-four orbits, and \(1344\) period-ten orbits. Because every possible state is classified, neither period seven nor fourteen can occur for \(d\le4\). This completes the if-and-only-if assertions.

## Verification

The standalone `tools/check_witnesses.py` checks **every transition** in both explicit quotient cycles, then checks the corresponding transitions using a separate direct thirty-two-vertex update on \(Q_5\) and another sixty-four-vertex update on \(Q_6\). It also exhaustively checks all smaller cubes through dimension three. The two compiled programs separately classify the full dimension-four functional graph. All three verifiers were executed from their included source paths; the outputs are in `data/verification_small.txt`, `data/q4_dfs_output.txt`, and `data/q4_peel_output.txt`. The two dimension-four output files agree byte for byte. The large finite computation is only used for a finite-dimensional exclusion; the persistence for all larger dimensions is an algebraic identity proved above.

To reproduce with Python 3 and a standard C compiler, from the package root run:

```sh
python3 tools/check_witnesses.py
cc -O3 -std=c11 tools/q4_dfs.c -o /tmp/q4_dfs && /tmp/q4_dfs
cc -O3 -std=c11 tools/q4_peel.c -o /tmp/q4_peel && /tmp/q4_peel
```

## Relationship to prior work

Durrett and Steif (1991) analyze the Greenberg–Hastings rule on integer lattices and asymptotic finite periodic boxes, including typical eventual periods three and four in a sparse regime. Gravner, Lyu and Sivakoff (2016) prove a general criterion for sustained excitation and identify the activity rate through cycle integrals. Doba (2018) proves a maximum-cycle-density law for arbitrary finite graphs and illustrates periodic waveforms on other graph examples. These theorems concern synchronization, excitation rates or large-volume statistics; none of their inspected statements supplies these two explicit sharp dimension-five period thresholds. Earlier exact low-dimensional cube cycle counts establish the absence of the specified periods through dimension four, but do not imply their existence in dimension five. The construction here is a positive dynamical witness in a new dimension, not a reinterpretation of earlier orbit totals.

## Limitations

The result does not count period-seven or period-fourteen orbits or their basins on \(Q_5\), nor does it determine the complete possible-period set in dimension five or beyond. No uniqueness of the displayed cycles under graph automorphisms is claimed. The two constructions are contained in a restricted weight-symmetric invariant family, which is sufficient for existence but not exhaustive of all cube trajectories. Some older foundational articles are unavailable in full electronic form, so an unindexed equivalent construction remains possible. No independent audit has been performed.

## References

1. R. Durrett and J. E. Steif, *Some Rigorous Results for the Greenberg–Hastings Model*, Journal of Theoretical Probability **4** (1991), 669–690. https://sites.math.duke.edu/~rtd/reprints/paper66.pdf
2. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, initial public version March 22, 1993. https://arxiv.org/abs/patt-sol/9303002
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting Behavior of 3-Color Excitable Media on Arbitrary Graphs*, arXiv:1610.07320 (October 24, 2016). https://arxiv.org/abs/1610.07320
4. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems **27** (2018), 101–126. https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf
