# The Möbius–Kantor majority clock: twelve symbolic necklaces and six two-cycle basin sizes

## Finding

For synchronous binary, open-neighbor majority dynamics on the labelled Möbius–Kantor graph (the cubic symmetric graph \(GP(8,3)\)), the global map \(F\) obeys the **sharp** finite identity
\[
F^5=F^3,\qquad F^4\ne F^2.
\]
The map has exactly **72 fixed states** and **2,556 primitive temporal two-cycle orbits**, with no longer cycles. The total \(5,184\) recurrent states are indexed by ordered pairs of symbols from a canonical \(72\)-element set; one update exchanges the two symbols. Every initial state first enters periodic behavior by update three. The number entering for the first time at updates \(0,1,2,3\) is respectively
\[
(5{,}184,\ 15{,}552,\ 22{,}528,\ 22{,}272).
\]

The following list completely classifies the **attraction-basin sizes** of primitive temporal orbits, including the periodic states themselves. Spatial automorphisms do not identify orbits.

| Orbit type | Basin size | Number of orbits |
| --- | ---: | ---: |
| Fixed state | 1 | 22 |
| Fixed state | 4 | 48 |
| Fixed state | 4,761 | 2 |
| Primitive two-cycle | 2 | 231 |
| Primitive two-cycle | 4 | 1,056 |
| Primitive two-cycle | 8 | 1,128 |
| Primitive two-cycle | 138 | 44 |
| Primitive two-cycle | 276 | 96 |
| Primitive two-cycle | 9,522 | 1 |

In particular, **22 equilibria and 231 primitive oscillations are dynamically isolated:** their only basin members are their own periodic configurations. At the other extreme, one primitive two-cycle attracts \(9{,}522\) initial states. The total attracting populations are \(9{,}736\) configurations reaching fixed states and \(55{,}800\) reaching two-cycles.

## Assumptions and scope

Label vertices \(0,1,\ldots,15\) modulo 16. Put in cycle edges \(\{i,i+1\}\) for all \(i\) and eight additional edges \(\{2j,2j+5\}\) for \(j=0,\ldots,7\), with indices reduced modulo 16. This is the LCF presentation \([5,-5]^8\) of the Möbius–Kantor graph. Every vertex has three neighbors; the bipartition consists of even vertices \(B_j=2j\) and odd vertices \(A_j=2j+1\), \(j\in\mathbf Z/8\mathbf Z\). The rule is
\[
F(x)_i=1\ \Longleftrightarrow\ \sum_{v\sim i}x_v\ge2.
\]
No ties are possible, and vertex opinions are not counted as their own neighbors. A *primitive two-cycle* is an unordered pair of distinct configurations \(\{x,F(x)\}\) with \(F^2(x)=x\). A *basin* counts all distinct labelled initial states eventually entering one temporal orbit. A *first-entry time* is the minimum \(t\ge0\) at which a state is on a temporal cycle.

For an eight-bit word \(s=(s_0,\ldots,s_7)\), let \(M(a,b,c)\) be the Boolean majority \((a\wedge b)\vee(a\wedge c)\vee(b\wedge c)\). All subscripts below are modulo eight. Define two maps on \(\{0,1\}^{8}\):
\[
\begin{aligned}
f(s)_j&=M(s_{j-2},s_j,s_{j+1}),\\
g(s)_j&=M(s_{j-1},s_j,s_{j+2}),\\
h&=f\circ g,\qquad k=g\circ f.
\end{aligned}
\]
In these conventions, an odd-shore word is listed first and an even-shore word second, so \(F(u,v)=(f(v),g(u))\).

## Proof

**1. Exact eight-bit certificate and the sharp clock.** The complete input domain of each shore map has only \(256\) words. The file `verify_shores.py` explicitly evaluates the displayed majority polynomials for *every* word. It certifies the identities
\[
f\circ k^2=f\circ k,\qquad g\circ h^2=g\circ h,
\]
and \(h^3=h^2\), \(k^3=k^2\). They are exact finite Boolean identities, not sampled instances. Therefore
\[
F^3(u,v)=(f(k(v)),g(h(u)))=F^5(u,v)
\]
for all \(2^{16}\) configurations, proving the universal three-update cutoff and excluding longer periodic orbits. The explicitly listed starting state encoded as integer 261 (bit \(i\) is the state at vertex \(i\)) first reaches a cycle at time three, proving sharpness. The independent `verify_full.py` checks this fact by direct graph-level updates over all \(65{,}536\) states.

**2. Classification of 72 recurrent symbols.** Let \(S=\{s:h(s)=s\}\) and \(T=\{s:k(s)=s\}\). The same finite truth table shows \(\lvert S\rvert=\lvert T\rvert=72\) and that \(g\) maps \(S\) bijectively onto \(T\) with inverse \(f\). A compact certificate of all elements of \(S\) is the following twelve cyclic-necklace representatives. Read the binary strings left to right as bits indexed \(0\) through \(7\). Each representative stands for all its distinct cyclic rotations.

| Representative | Distinct rotations | Fiber weight \(w\) |
| --- | ---: | ---: |
| `00000000` | 1 | 69 |
| `11100000` | 8 | 2 |
| `10110000` | 8 | 2 |
| `10100100` | 8 | 2 |
| `11110000` | 8 | 1 |
| `10110100` | 8 | 1 |
| `11001100` | 4 | 1 |
| `10101010` | 2 | 1 |
| `11111000` | 8 | 2 |
| `11110100` | 8 | 2 |
| `11011010` | 8 | 2 |
| `11111111` | 1 | 69 |

Here \(w(s)=\#\{z:h^2(z)=s\}\). Exhaustive application of the explicitly defined maps on the 256 possible inputs verifies **both completeness** of this necklace list and the fiber weights. No word is omitted: the table has \(1+3(8)+8+8+4+2+3(8)+1=72\) distinct rotations. In particular, 22 symbols have weight one, 48 have weight two, and the two constant symbols have weight 69. Moreover, the dual fibers satisfy
\[
\#\{z:k^2(z)=g(s)\}=w(s),\qquad s\in S.
\]

**3. Swap dynamics, complete basin spectrum.** A configuration is recurrent exactly when both its shore words lie in \(S\times T\): if it is periodic, \(F^2=(h,k)\) forces \(h(u)=u\) and \(k(v)=v\); conversely every pair in \(S\times T\) is two-periodic. Represent such a state as \((s,g(t))\) with \(s,t\in S\). Then
\[
F(s,g(t))=(t,g(s)).
\]
Thus the recurrent dynamics is exchange of two members of \(S\). There are \(72\) fixed states and \(\binom{72}{2}=2{,}556\) primitive two-cycles. Since \(F^4(u,v)=(h^2(u),k^2(v))\) is recurrent for every input, the basin of fixed symbol \(s\) has size \(w(s)^2\). For unequal symbols \(s,t\), the basin of the two-cycle indexed by \(\{s,t\}\) has size \(2w(s)w(t)\): the two phases have disjoint preimage fibers under \(F^4\). Using the weight multiplicities \((22,48,2)\) for weights \((1,2,69)\) yields all nine rows of the basin table. For example, the \(\binom{22}{2}=231\) pairs of weight-one symbols are the isolated two-cycles, and the two weight-69 symbols form the unique basin of size \(2\cdot69^2=9{,}522\). The basin totals sum to \(2^{16}\).

**4. Exact entrance-time layers.** A state is recurrent at time \(t\) if both shore outputs after \(t\) steps lie in their respective fixed sets. The same complete shore truth table finds exactly 72 allowed words per shore at time zero; 144 at time one; 208 at time two; and 256 at time three. This is a product criterion because \(F\) interchanges the shores. Hence the cumulative numbers periodic by updates \(0,1,2,3\) are
\[
72^2,\quad144^2,\quad208^2,\quad256^2.
\]
Successive differences give the four first-entry populations in the finding. The completely separate graph-level enumeration verifies the refined entrance-time and eventual-period table as follows.

| First-entry time | Eventual fixed point | Eventual two-cycle |
| ---: | ---: | ---: |
| 0 | 72 | 5,112 |
| 1 | 480 | 15,072 |
| 2 | 3,712 | 18,816 |
| 3 | 5,472 | 16,800 |

## Verification

Two independent Python 3 programs requiring only the standard library accompany this result. Run `python3 verify_shores.py` to evaluate the complete \(256\)-word truth tables, check the polynomial identities, verify the twelve necklaces, compute the retraction-fiber weights, and derive the orbit/basin formulas. Run `python3 verify_full.py` to construct the LCF graph independently, check all \(2^{16}\) synchronous transitions, classify every orbit by first-entry time and eventual period, and compute its exact attraction basin. Outputs from actual runs are included as `verify_shores_output.txt` and `verify_full_output.txt`. Both programs assert every main numerical and algebraic claim; the full-state checker checks its own explicit time-three witness. The finite exhaustive computation proves a finite assertion and makes no claim about graphs of other orders.

## Relationship to prior work

Goles and Olivos proved the general period-at-most-two property for finite symmetric threshold dynamics; this theorem is not claimed as new. Benjamini, Chan, O'Donnell, Tamuz and Tan (arXiv:1405.2486v1, especially the introduction and sections 2 and 4) give this background and results on infinite unimodular and random graphs. Their analysis does not imply the \(72\)-symbol necklace structure, 69-to-one retraction fibers, first-entry distribution, or exact attraction basins of this particular graph. The Möbius–Kantor graph is the classical \(GP(8,3)\) and the unique cubic symmetric graph on sixteen vertices, as documented in standard graph references.

The closest exact published analogue examined is *A two-step majority projection and exact attraction basins on the Heawood graph* (2026). On that different, fourteen-vertex Fano-incidence graph the shore retraction is idempotent immediately, with 58 recurrent symbols and a maximum transient of two. Here the shore retraction has an intermediate 88-word image, stabilizes only on its **second** application at 72 words, and gives a **sharp three-update** clock with a different six-class oscillation-basin spectrum. The prior Heawood formulas therefore do not imply this result. An exact Pappus-graph census concerns a different eighteen-vertex incidence geometry and also does not imply these 8-site necklace and fiber counts. Searches using the aliases \(GP(8,3)\), Möbius–Kantor, Moebius–Kantor, 16-vertex cubic symmetric graph, majority automaton, fixed states, two-cycle and basin revealed no exact matching published claim. A failure to find one is not a proof of absolute novelty.

## Limitations

This is a finite, graph-specific classification, not an all-size generalized Petersen or all-cubic-graph theorem. Graphs with ties, asynchronous updates, a self-inclusive rule, or colored states outside \(\{0,1\}\) are outside the claim. Exhaustive computation is decisive for the displayed finite graph but does not imply generic convergence cutoffs. Some historical papers, including the original full Goles–Olivos article, were not accessible for inspection; an unindexed exact census could exist. No independent external audit has been performed.

## References

1. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first posted 2014-05-11, https://arxiv.org/abs/1405.2486 .
2. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1 .
3. E. W. Weisstein, *Möbius–Kantor Graph*, MathWorld, https://mathworld.wolfram.com/Moebius-KantorGraph.html .
4. NetworkX documentation, *moebius_kantor_graph*, https://networkx.org/documentation/stable/reference/generated/networkx.generators.small.moebius_kantor_graph.html .
5. *A two-step majority projection and exact attraction basins on the Heawood graph* (2026), publicly available research record, indexed record identifier 8cd2964a9d93 .
