# Five-cycle survival and two four-cycle symmetry types in four-state Petersen excitation

## Finding

Let \(P=KG(5,2)\) be the Petersen graph. On the labelled vertex set, consider the synchronous four-state Greenberg–Hastings maps \(F_1\) and \(F_2\), where a resting vertex requires respectively at least one or at least two excited neighbors to fire, while all nonresting states progress through their refractory clock. The following finite-state identities are exact on all \(4^{10}=1{,}048{,}576\) configurations:

\[
F_1^{31}=F_1^{11},\qquad F_2^5\equiv\mathbf 0.
\]

The threshold-one map has exactly one fixed state, ninety primitive four-cycles and thirty primitive five-cycles, with no other periodic orbits. All trajectories reach their eventual periodic orbit within eleven updates, and exactly 1,920 initial configurations need all eleven updates; all 1,920 approach four-cycles. The 120 nontrivial temporal cycles split into exactly **three** classes under the full \(S_5\) graph automorphism action: two four-cycle classes of 30 and 60 temporal orbits and one five-cycle class of 30 temporal orbits. The maximally delayed states form sixteen graph-symmetry classes, each of size 120.

Raising the excitation threshold from one to two extinguishes all nontrivial recurrent activity. The sharp first-entry time becomes five updates, attained by exactly 3,740 configurations. The first-entry/period census for both maps is given completely in `census.csv`, and every count is an integer computation, not a statistical estimate.

## Assumptions and scope

The ten labelled vertices are the two-subsets of \(\{0,1,2,3,4\}\), ordered lexicographically as

```
(0,1), (0,2), (0,3), (0,4), (1,2),
(1,3), (1,4), (2,3), (2,4), (3,4)
```

Two vertices are adjacent exactly when their two-subsets are disjoint. A state \(x\) assigns one of \(\{0,1,2,3\}\) to each vertex. For \(\theta\in\{1,2\}\), the rule is

\[
F_\theta(x)(v)=
\begin{cases}
1,&x(v)=0\text{ and }\#\{u\sim v:x(u)=1\}\ge\theta,\\
0,&x(v)=0\text{ and }\#\{u\sim v:x(u)=1\}<\theta,\\
2,&x(v)=1,\\
3,&x(v)=2,\\
0,&x(v)=3.
\end{cases}
\]

An initial state has entry time \(\tau\) when \(\tau\ge0\) is the least update count for which its image lies on a directed cycle. Its eventual least period \(p\) is the length of that cycle. Vertices are distinguished by their given labels; only explicitly stated orbit counts identify temporal phase or graph symmetry. The claim is specific to the finite Petersen graph and these two contact thresholds.

## Proof

**1. Exact finite state space and update table.** Encode a state in the displayed order by

\[
s(x)=\sum_{j=0}^9 x(v_j)4^j,\qquad 0\le s(x)<4^{10}.
\]

Each integer has a unique ten-coordinate four-adic representation. `verify_kneser.py` generates every edge by disjointness and applies the update equation directly at all ten vertices for every one of the \(4^{10}\) inputs, separately for both thresholds. `verify_outer_inner.cpp` independently builds the outer pentagon, spokes and inner pentagram, and constructs the same dynamics in a distinct vertex order. The two representations describe isomorphic labelled copies of the Petersen graph; hence graph-invariant counts must coincide.

**2. Exhaustiveness and first-entry clock.** For any finite self-map, repeatedly deleting vertices of indegree zero leaves precisely its directed cycles: an indegree-zero vertex cannot be on a cycle, and every finite acyclic in-tree has an indegree-zero leaf. Reverse deletion order therefore computes the exact entry time via \(\tau(x)=1+\tau(F(x))\) and transfers the least period from the next state. The C++ program implements this lemma on all inputs and obtains exactly the rows in `census.csv`. Its threshold-one cycle lengths and counts are \((1,1),(4,90),(5,30)\); its maximum entry time is eleven and its maximum-time row is \((\tau,p,N)=(11,4,1920)\). The threshold-two system has only the zero fixed point and exactly 3,740 states at entry time five.

Independently, the Python program constructs the map on \(KG(5,2)\) and explicitly tests \(F_1^{31}(x)=F_1^{11}(x)\) and \(F_2^5(x)=\mathbf 0\) for every encoded state, with no stopping based on samples. The exponent twenty in the first identity is the least common multiple of the only observed nontrivial primitive periods four and five. Its verification is independent of the C++ indegree method. The Python program marks every output after eleven updates, proves each is periodic by verifying its twenty-step return, and directly traces the first entry of each of the \(4^{10}\) inputs. Its complete \((\tau,p)\) table matches the C++ table. The presence of states with \(\tau=11\), and similarly with \(\tau=5\) at threshold two, proves both bounds sharp. Concrete examples in the lexicographic encoding are \(s=21100\) for the eleven-step threshold-one bound and \(s=1300\) for the five-step threshold-two bound.

**3. Exactly three nontrivial geometric types.** The graph automorphism group of \(KG(5,2)\) is \(S_5\), induced by permuting the five underlying symbols. This can be seen because its five maximum independent four-vertex stars consist of pairs containing a fixed ground symbol: an automorphism permutes the stars, and their pairwise intersections determine every vertex. The Python verifier enumerates all \(5!=120\) ground-symbol permutations and their actions on each periodic temporal cycle. It finds precisely one fixed-state class, one four-cycle class of 30 temporal orbits, a second four-cycle class of 60 temporal orbits, and one five-cycle class of 30 temporal orbits. Because these disjoint classes account for all \(1+90+30\) cycles found exhaustively, the classification is complete. Representatives, in the vertex order above, are

| Period | Orbit-class size | Representative colors |
|---:|---:|---|
| 4 | 30 | `(3,1,3,2,3,1,2,1,0,0)` |
| 4 | 60 | `(0,1,3,2,3,1,2,1,0,0)` |
| 5 | 30 | `(0,0,0,2,3,1,0,1,0,0)` |

The same full action partitions the 1,920 maximally delayed configurations into sixteen 120-element symmetry classes; the verifier confirms that every such configuration has eventual least period four.

**4. Total-mass consistency checks.** At threshold one, the periodic populations are \(1\), \(360\) and \(150\), and the complete attraction basins into periods one, four and five contain respectively \(429136\), \(90600\) and \(528840\) initial states, summing to \(4^{10}\). At threshold two, every state enters the zero configuration after at most five updates, with entry-time populations \(1,1023,58025,669622,316165,3740\), also summing to \(4^{10}\). These independently calculated counts agree exactly in both programs.

## Verification

All ingredients are embedded. Run from the directory containing the files:

```
python3 verify_kneser.py
c++ -O2 -std=c++17 verify_outer_inner.cpp -o verify_outer_inner
./verify_outer_inner 4 1
./verify_outer_inner 4 2
```

The Python program uses the standard library only, with a direct Kneser-graph implementation and an explicit twenty-step-return certificate for every state; the C++ program uses a distinct outer/inner Petersen graph construction and functional-graph indegree elimination. Stored outputs are `check_kneser.txt` and `check_outer_inner.txt`. `census.csv` is the exact common aggregate. Only the C++ binary is a temporary compilation product and is not needed as an embedded dependency. Integer assertions and explicit iteration cover all cases; no infinite-family conclusion is inferred from finite experiments.

## Relationship to prior work

Greenberg and Hastings introduced discrete excitable-media dynamics in 1978. Fisch, Gravner and Griffeath describe the arbitrary-color and threshold Greenberg–Hastings rule and emphasize spatial lattice wave formation, not the labelled Petersen graph. The full 2018 paper of Gravner, Lyu and Sivakoff treats *three*-color excitation on arbitrary graphs and derives criteria and limiting activity, not this four-state finite orbit census. The separately published three-state Petersen census determines \(1,80,60,30,60\) primitive orbits of periods \(1,3,4,5,8\), with maximum entry six; that different state space does not imply the present four-state counts, three geometric cycle types, eleven-step clock, or threshold-two extinction. A published four-state tripartite-graph formula gives only periods one and four on complete tripartite graphs; the Petersen graph is neither complete multipartite nor covered by that formula, and its genuine five-cycles demonstrate the distinction.

## Limitations

This is a rigorously exhaustive *finite* computation on a canonical ten-vertex graph, not an analytical classification for all cubic graphs, all Kneser graphs, or arbitrary numbers of colors. The all-state functional-graph identity depends on the exact enumerating code; no short conceptual derivation of the eleven-step cutoff is claimed. The original 1978 publication has a month-only publication date in accessible bibliographies, and its full text was unavailable. The first precisely day-dated accessible archival supporting source used here was posted in March 1993; this is not a claim that the original model was first public then. Relevant indexed sources were compared, but historical priority against unindexed work is not proved. No independent mathematical audit has been performed.

## References

- J. M. Greenberg and S. P. Hastings, *Spatial Patterns for Discrete Models of Diffusion in Excitable Media*, SIAM Journal on Applied Mathematics **34** (1978), 515–523, DOI: https://doi.org/10.1137/0134040 (accessible abstract and bibliographic record).
- R. Fisch, J. Gravner and D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing **1** (1991), 23–39, https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf (full paper inspected).
- R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, archival submission March 22, 1993, https://arxiv.org/abs/patt-sol/9303002.
- J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320 (2016), Annals of Applied Probability **28** (2018), 3324–3357, https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf (full paper inspected).
- A. E. Brouwer, *Petersen graph*, https://aeb.win.tue.nl/graphs/Petersen.html (graph structure and automorphism group).
- *Five periods and two extremal symmetry orbits in Petersen excitation dynamics*, publicly indexed mathematical result (three-state comparison).
- *A sharp six-update cutoff and an exact four-cycle census for tripartite excitation*, publicly indexed mathematical result (different graph family).
