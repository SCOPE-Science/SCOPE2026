# Sharp two-contact extinction on the two canonical triangle-free four-chromatic graphs

## Finding

Consider the synchronous three-state Greenberg–Hastings excitation map with **two-contact activation**: a resting vertex becomes excited if and only if at least two of its neighbors are excited; excited vertices become refractory; refractory vertices become resting. On each of the two canonical smallest triangle-free four-chromatic graphs, every initial condition becomes completely resting, but at different sharp times. For the eleven-vertex Grötzsch graph \(G=\mu(C_5)\), \(F_G^5(x)=\mathbf0\) for all \(x\in\{0,1,2\}^{11}\), and \(F_G^4\) is not identically zero. For the twelve-vertex four-regular Chvátal graph \(H\), \(F_H^6(x)=\mathbf0\) for all \(x\in\{0,1,2\}^{12}\), and \(F_H^5\) is not identically zero. These are exact finite-state identities, not asymptotic or high-probability assertions.

For \(t\ge0\), define \(a_G(t)\) and \(a_H(t)\) as the numbers of labelled initial configurations that reach the all-rest state **for the first time exactly at update \(t\)**. The complete histograms are:

| First rest time \(t\) | Grötzsch \(a_G(t)\) | Chvátal \(a_H(t)\) |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 2,047 | 4,095 |
| 2 | 51,361 | 117,272 |
| 3 | 87,116 | 237,555 |
| 4 | 36,202 | 151,450 |
| 5 | 420 | 20,160 |
| 6 | 0 | 908 |
| **Total** | **177,147** | **531,441** |

Both maps have only one periodic configuration (all resting). Nevertheless both graphs sustain genuinely periodic three-state excitation with **one-contact** activation. In the same vertex labellings, the base-three integer \(448\) is an initially primitive three-periodic state at threshold one in both cases. Thus the increase from one to two simultaneous contacts destroys all oscillations on these two canonical graph benchmarks. The extinction is not a general consequence of four-regularity or triangle-freeness: under the same two-contact rule the triangle-free four-regular graph \(K_{4,4}\) supports a primitive four-cycle (a concrete witness is given below).

## Assumptions and scope

Graphs are finite, simple and undirected. All states are labelled \(0\) (rest), \(1\) (excited), and \(2\) (refractory). For an integer contact threshold \(\theta\), the simultaneous update at vertex \(v\) is
\[
(F_\theta x)(v)=\begin{cases}
2,&x(v)=1,\\
0,&x(v)=2,\\
1,&x(v)=0\text{ and }|\{u\sim v:x(u)=1\}|\ge\theta,\\
0,&\text{otherwise}.
\end{cases}
\]
The theorem takes \(\theta=2\). There is no stochastic forcing and no self-neighbor. Vertex labels start at zero; `graph_data.json` specifies every edge and is an integral definition of the two graphs. For Grötzsch, vertices \(0,\ldots,4\) form a pentagon, vertices \(5,\ldots,9\) are its Mycielski twins, and vertex \(10\) is adjacent to all twins. For Chvátal, use the canonical 24-edge labelled graph explicitly in `graph_data.json`. The graph-definition checker verifies in each case triangle-freeness and chromatic number four; the Chvátal graph is four-regular.

Encode a configuration \(x\) as \(s(x)=\sum_{v=0}^{n-1}x(v)3^v\), an integer in \(0\le s<3^n\). A first-rest time is \(T(x)=\min\{t\ge0:F_2^t(x)=\mathbf0\}\). The theorem proves this minimum exists for all configurations in the stated domains. It does not concern every four-chromatic graph or every network of the same degree.

## Proof

**Exact enumeration gives universal extinction.** The Python program `verify_reverse.py`, using the explicit graph specification in `graph_data.json`, constructs the complete deterministic successor array for each of the \(3^{11}=177147\) and \(3^{12}=531441\) states. It computes every indegree and repeatedly removes zero-indegree vertices. In any finite functional digraph, this elimination removes exactly the vertices outside directed cycles; the survivors are precisely the recurrent cycle vertices. The program finds **only state zero** surviving, on each graph. Thus all configurations eventually reach \(\mathbf0\), which is fixed. In reverse removal order it assigns \(T(0)=0\) and \(T(s)=1+T(F_2(s))\), so the complete exact first-rest histograms and maximum rest times follow. There is no statistical sampling or extrapolation here: every integer in each indicated range is processed.

**Independent full forward enumeration proves the sharp bounds.** The separate C++17 program `verify_forward.cpp` independently assembles vertex states by base-three division, applies the local contact rule directly, and checks every initial integer by forward iteration. On Grötzsch it finds all states at zero by update five, with precisely \(420\) first arriving at update five; on Chvátal it finds all states at zero by update six, with precisely \(908\) first arriving at update six. Its seven histogram rows agree with those from reverse elimination. In particular the two explicit sharpness witnesses \(s=1089\) on Grötzsch and \(s=120\) on Chvátal have respective integer trajectories
\[
1089\to67792\to153098\to43767\to54\to0
\]
and
\[
120\to9232\to254180\to492804\to40825\to2\to0.
\]
The displayed integers are base-three state encodings, not vertex counts. Either trajectory directly rules out an earlier global zero-map identity.

**Threshold comparison.** For one-contact activation, both independent implementations verify that the same labelled initial state \(s=448\) is primitive three-periodic: on Grötzsch its successive encodings are \(448\to88769\to176502\to448\), and on Chvátal they are \(448\to265916\to530796\to448\). This compares two distinct dynamical rules on fixed graphs rather than claiming an unverified threshold monotonicity theorem. To show that two-contact extinction does not follow from degree four or the absence of triangles, on \(K_{4,4}\) with shores \(0,\ldots,3\) and \(4,\ldots,7\), the state \((2,2,0,0,1,1,0,0)\) belongs to the primitive four-cycle
\[
(2,2,0,0,1,1,0,0)\to(0,0,1,1,2,2,0,0)\to(0,0,2,2,0,0,1,1)\to(1,1,0,0,0,0,2,2)\to(2,2,0,0,1,1,0,0).
\]
Each transition follows the same two-contact rule, giving a small independently checkable boundary example.

## Verification

Put `graph_data.json`, `verify_reverse.py`, and `verify_forward.cpp` in one directory. Execute:

```sh
python3 verify_reverse.py
c++ -O2 -std=c++17 -Wall -Wextra verify_forward.cpp -o verify_forward
./verify_forward
```

The first checker uses a functional-graph indegree peel and reverse recursion, and additionally checks exact three- and four-colorability and triangle-freeness by backtracking. The second checker uses direct forward trajectories, with its graph and local-update implementation separately specified. Their results agree for all 708,588 states, including every nonzero terminal layer. The C++ checker also verifies the two three-cycle threshold-one witnesses and the displayed primitive four-cycle on \(K_{4,4}\). Both methods are exhaustive finite computations, not a general symbolic theorem for larger graphs. Expected numeric output is included in `counts.json`.

## Relationship to prior work

Durrett–Griffeath introduced the general contact-threshold Greenberg–Hastings model and studied lattice phase diagrams, including threshold-dependent stable periodic objects [1]. Their work does not provide these two labelled finite-graph extinction histograms. Gravner–Lyu–Sivakoff's finite-graph theory [2, §§1–4] explicitly uses **one-contact** three-color GHM and proves activity statements under that different rule; those results do not imply universal extinction at contact threshold two. A published general half-degree rigidity theorem [3] identifies when four-regular graphs can have *initial* primitive three-periodic orbits at contact threshold two, but does not exclude longer recurrent periods, determine transient depths, or supply these zero-attraction laws. The published four-state Chvátal-graph enumeration [4] concerns **four total states at contact threshold one**, not the present three-state, two-contact rule. Canonical graph constructions and their extremal chromatic properties are documented in [5,6].

The contribution here is the paired, completely exact threshold-two extinction and first-hitting-time classification, not the graph constructions, the Greenberg–Hastings rule, or general dynamical theorems. No uniqueness inference is made from unsuccessful searches.

## Limitations

This is a finite computer-assisted classification of **two explicitly labelled graphs**, not a universal statement about triangle-free four-chromatic networks, and not a proof of extinction on arbitrary larger Mycielski graphs. Correctness depends on the supplied programs and the precise stated update rule. Independent human assessment has not been performed. A mathematically equivalent obscure historical enumeration may exist; the cited published work and record searches do not prove otherwise.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, first public preprint 1993-03-22, https://arxiv.org/abs/patt-sol/9303002. Lawful full text https://services.math.duke.edu/~rtd/reprints/paper79.pdf, especially pp. 183–185.
2. J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, first public preprint 2016-10-24, https://arxiv.org/html/1610.07320v1, especially §§1–4 and Theorem 3.
3. *Half-degree rigidity and a sharp contact-threshold collapse on squared cycles*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-half-degree-rigidity-and-a-sharp-contact-threshold-collapse-on-s--7c3fe196f42d.
4. *Four-state Chvátal excitation: period collapse and six extremal symmetry classes*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-four-state-chv-tal-excitation-period-collapse-and-six-extremal-s--924e4654e069.
5. V. Chvátal, *The smallest triangle-free 4-chromatic 4-regular graph*, J. Combinatorial Theory 9 (1970), 93–94, https://doi.org/10.1016/S0021-9800(70)80057-6.
6. *Grötzsch Graph*, MathWorld, https://mathworld.wolfram.com/GroetzschGraph.html.
