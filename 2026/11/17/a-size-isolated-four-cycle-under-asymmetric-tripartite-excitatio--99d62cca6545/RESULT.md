# A size-isolated four-cycle under asymmetric tripartite excitation

## Finding

Let \(a,b,c\) be positive integers and let \(G=K_{a,b,c}\) have three labelled independent shores \(A,B,C\). Every vertex has one of three states: resting \(0\), excited \(1\), and refractory \(2\). Updates are simultaneous: \(1\to2\to0\); a resting vertex changes to \(1\) if and only if at least \(\theta\) of its neighbors are excited. Take shore-dependent thresholds \((\theta_A,\theta_B,\theta_C)=(1,1,2)\).

**Theorem.** Every labelled initial configuration first becomes periodic after at most seven updates. The only eventual primitive periods are \(1,3,4\). Period \(3\) occurs precisely when \(a\ge2\) or \(b\ge2\); period \(4\) occurs **precisely when \(a=b=2\)**, independent of the positive size \(c\) of the threshold-two shore. Whenever it occurs, there are exactly **eight** labelled primitive-four configurations, forming exactly two temporal four-cycle orbits. The unique fixed configuration is the all-resting state. The universal seven-update bound is sharp already on \(K_{1,2,2}\), and the global update map obeys

\[
F^{19}=F^7.
\]

Thus heterogeneous excitation creates two four-cycle orbits already on \(K_{2,2,1}\), although neither homogeneous threshold-one excitation nor homogeneous threshold-two excitation on that same graph has a four-cycle. Adding even one vertex to either threshold-one shore removes these four-cycles, however large the third shore may be.

There is also an **exact all-size, all-transient census**. For \(r\in\{0,1,2\}\) put
\[
E_0(z)=1,\qquad E_1(z)=z,\qquad E_2(z)=e^z-1-z.
\]
Let \(\mathcal S\) be the finite set of nine-coordinate vectors \(s=(s_{ij})\), with three coordinates \(j=0,1,2\) in each shore \(i=A,B,C\), each coordinate in \(\{0,1,2\}\), and at least one nonzero coordinate in each shore. Thus \(|\mathcal S|=26^3=17576\). For each \(s\), let \(\tau(s)\) and \(\pi(s)\) be the first-entry time and least eventual period obtained by the explicit tagged-class recurrence given below, and exactly tabulated in `certificates/all_signatures.csv`. Then, for every \(t\ge0\) and \(p\ge1\), the number \(N_{a,b,c}(t,p)\) of labelled initial configurations whose first periodic entry is \(t\) and eventual least period is \(p\) equals

\[
\boxed{
N_{a,b,c}(t,p)=a!b!c!\,[x^ay^bz^c]
\sum_{\substack{s\in\mathcal S\\\tau(s)=t,\ \pi(s)=p}}
\prod_{j=0}^{2}E_{s_{Aj}}(x)E_{s_{Bj}}(y)E_{s_{Cj}}(z).
}
\]

In particular, the number of primitive temporal orbits of period \(p\) is \(N_{a,b,c}(0,p)/p\). The fixed finite certificate makes this formula effective for arbitrary positive shore sizes, not just small examples.

## Assumptions and scope

Graphs are finite, undirected, simple and loopless. Every shore has at least one labelled vertex. Only neighbors in *different* shores count toward excitation. A vertex in state \(0\) retains \(0\) unless its threshold is met; a vertex in state \(1\) always moves to \(2\); a vertex in state \(2\) always moves to \(0\). All updates are simultaneous. First periodic entry is the smallest \(t\ge0\) for which \(F^t(X)\) lies on a periodic orbit, and primitive period means the least positive return period of that orbit. Counts distinguish assignments to labelled vertices, not just shore histograms.

## Proof

**A finite factor that preserves labelled return times.** Fix an initial assignment. In each shore partition its vertices into initial-color classes by their *initial* colors \(0,1,2\). Two vertices from the same initial-color class remain in the same color forever: they begin equal, see the same other shores at every step and use the same threshold. Consequently the full labelled state at every time is determined by the colors of the at most nine initially occupied initial-color classes. Occupied initial-color classes always have a vertex witness, so two full labelled states are equal exactly when every occupied initial-color class has the same color at the two times. Merely comparing aggregate color histograms is **not** sufficient.

Write \(m_{ij}\) for the initial cardinality of initial-color class \(j\) in shore \(i\), and truncate to \(s_{ij}=\min(2,m_{ij})\). Every future threshold test asks only whether a union of initial-color classes contains at least one excited vertex (for \(A,B\)) or at least two (for \(C\)). Since all cardinalities are nonnegative, truncation at two preserves both tests for every possible union, at every time. It also preserves exactly which initial initial-color classes are occupied. Therefore **every** initial configuration, of arbitrary shore sizes, has the same first periodic-entry time and eventual primitive period as its tagged truncated-initial-color class representative.

Here is the explicit deterministic recurrence. A nonempty initial initial-color class \((i,j)\) carries weight \(s_{ij}\) and color \(q_{ij}(0)=j\); absent initial-color classes are never updated. At time \(t\), define
\[
H_i(t)=\sum_{j:s_{ij}>0}s_{ij}\,\mathbf1_{\{q_{ij}(t)=1\}},\qquad
h_i(t)=\mathbf1_{\{\sum_{k\ne i}H_k(t)\ge\theta_i\}}.
\]
For every occupied initial-color class,
\[
q_{ij}(t+1)=\begin{cases}
1,&q_{ij}(t)=0\text{ and }h_i(t)=1,\\
0,&q_{ij}(t)=0\text{ and }h_i(t)=0,\\
2,&q_{ij}(t)=1,\\
0,&q_{ij}(t)=2.
\end{cases}
\]
The full tuple of occupied tagged-class colors, rather than the three shore color histograms, defines a finite orbit whose first repetition supplies \(\tau(s)\) and \(\pi(s)\).

**Exhaustive finite classification.** There are exactly \(3^3-1=26\) nonempty truncated cardinality triples per shore, hence exactly \(17576\) signatures. `verification/finite_quotient.py` uses only standard-library Cartesian products and the preceding recurrence, visits every one of these signatures and stops at its first exact repeat. Its explicit expected histogram in the source checks all \(21\) populated pairs \((\tau,\pi)\). The only periods found are \(1,3,4\), the maximal entry time is seven, and no period-four signature has entry time above four. The resulting complete table is `certificates/all_signatures.csv`, including all nine truncated counts and the two orbit statistics on every physical data row. The verifier reopens that table and compares every row with its computed results.

The four and only four period-four signatures, with each shore listed as its initial \((0,1,2)\)-color cardinality triple, are
\[
\begin{array}{lll}
((1,0,1),(1,1,0),(1,0,0)),&((1,0,1),(1,1,0),(2,0,0)),\\
((1,1,0),(1,0,1),(1,0,0)),&((1,1,0),(1,0,1),(2,0,0)).
\end{array}
\]
Thus both threshold-one shores must have size exactly two. Conversely, when \(a=b=2\) either of the two displayed color arrangements can be realized, each with \(2!\cdot2!=4\) assignments to the labelled first two shores. The third shore is uniformly at rest and can have *any* positive cardinality. Exactly eight labelled configurations are initially primitive-four, and they form \(8/4=2\) orbits.

The same exhaustive certificate tests all feasible initial signatures for each \(1\le a,b,c\le7\), and verifies that a primitive-three signature is realizable precisely when \(a\ge2\) or \(b\ge2\). The test extends to every larger size because a capped triple \(v\in\{0,1,2\}^3\setminus\{0\}\) is realizable in a shore of size \(m\) precisely when \(\sum_jv_j\le m\) and either \(\sum_jv_j=m\) or at least one \(v_j=2\). For every \(m\ge7\), the feasible set of capped triples is exactly that for \(m=7\). Hence checking the bounded shore-size cube is an **exhaustive all-size proof** of both onset conditions.

The truncated signature \(((1,0,0),(1,1,0),(0,1,1))\) on \(K_{1,2,2}\) has exact first periodic-entry time seven, with subsequent fixed state. This proves sharpness. Since every eventual period divides twelve and every first-entry time is at most seven, \(F^{19}=F^7\) holds on every permitted graph. The presence of period-three and period-four orbits in the family makes twelve the least common universal eventual period.

**Exact enumeration of labelled initial states.** A initial-color class of truncated size \(0\) must be empty; one of truncated size \(1\) contains exactly one vertex; and one of truncated size \(2\) contains at least two. Their exponential generating functions are respectively \(E_0,E_1,E_2\). Multinomial assignment across the three initial colors of each labelled shore is therefore counted by \(m![z^m]\prod_jE_{s_{ij}}(z)\). Multiply the three independent shore factors and sum over the signatures classified as \((t,p)\). This gives the exact stated census, with no dependence on experiments at bounded graph sizes.

## Verification

Run `python3 verification/finite_quotient.py` from the artifact root to regenerate and validate `certificates/all_signatures.csv`; its expected histogram, sharpness witness, all-size feasibility reduction, and period existence predicates are asserted explicitly. A second, separately implemented `verification/direct_graph.py` builds actual labelled complete tripartite graphs and iterates individual vertex colors without using the class update. It exhaustively checks **179604 initial labelled configurations** on **56 graphs** with positive shore sizes and total size three through eight against the certificate, including exact primitive-period-four counts. Its test also independently realizes the seven-step witness. The recorded, replayed standard-output files accompany both scripts. These finite graph tests provide corroboration; the infinite-family theorem follows from the mathematical initial-color-class truncation correspondence plus exhaustive enumeration of all possible capped signatures.

## Relationship to prior work

Fisch, Gravner and Griffeath introduced threshold contact dynamics and investigated spatially homogeneous Greenberg–Hastings waves; Durrett and Griffeath studied deterministic excitable cellular automata and their periodic structures. Gravner, Lyu and Sivakoff give a general graph theory for the standard **threshold-one** three-state rule. Previously reported complete-tripartite exact classifications treat **all three thresholds equal to one**, yielding only periods \(1,3\) and a four-step cutoff, or **all three equal to two**, permitting periods \(1,3,4,12\) with a period-four size window requiring the largest shore to have at least four vertices. The present unequal-threshold model is neither homogeneous rule and is not obtained from either theorem by relabelling a shore or specializing shore sizes. In particular, the period-four orbit on \(K_{2,2,1}\) occurs in neither homogeneous model on that graph. The comparison does not claim a new definition of excitable dynamics or a general theorem for arbitrary threshold assignments.

## Limitations

This is an exactly reproducible computer-assisted finite-factor theorem, not a symbolic closed-form solution for each of the \(21\) nonzero transient/period categories. It requires three states, three nonempty complete shores, precisely the fixed shore thresholds \((1,1,2)\), and synchronous updates. The theorem does not concern arbitrary graphs, other numbers of colors, arbitrary heterogeneous thresholds or probabilistic perturbations. Exhaustive checking of a finite exact factor is not external mathematical certification; independent audit has not been performed. Unindexed equivalent prior work remains a residual priority risk.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, first posted 1993-03-22. https://arxiv.org/abs/patt-sol/9303002
2. R. Fisch, J. Gravner and D. Griffeath, *Threshold-range scaling of excitable cellular automata*, *Statistics and Computing* **1** (1991), 23–39; publicly dated arXiv:patt-sol/9304001, 1993-04-02. Author full-text copy: https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, first posted 2016-10-24. https://arxiv.org/abs/1610.07320
4. *Exact ten-class temporal census for three-state excitation on complete tripartite graphs*, accessible research record: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-ten-class-temporal-census-for-three-state-excitation-on-co--5f4b0c36707a
5. *A nonmonotone twelve-cycle window for threshold-two excitable dynamics on tripartite graphs*, accessible research record: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-nonmonotone-twelve-cycle-window-for-threshold-two-excitable-dy--f93d052f0961
