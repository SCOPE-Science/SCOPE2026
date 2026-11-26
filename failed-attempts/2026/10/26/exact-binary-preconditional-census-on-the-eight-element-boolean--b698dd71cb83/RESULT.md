# Exact binary preconditional census on the eight-element Boolean algebra

## Finding
Let \(B=\mathcal P(\{1,2,3\})\) with its Boolean order and labelled atoms. Among **all** binary operations \(\Rightarrow:B^2\to B\) satisfying Holliday's five preconditional axioms, Chen's conditional identity and semicomplementation, exactly **\(7820\)** are \(\mathsf T\)-preconditionals. Exactly **\(1021\)** additionally satisfy double-negation inflation and hence are \(\mathsf F\)-preconditionals. These are counts of binary operation tables, not unary reducts and not isomorphism classes.

Put \(N(A)=A\Rightarrow\varnothing\). For the \(\mathsf F\)-subfamily, unary negations are parametrized by the eight simple graphs on the three labelled atoms. If the graph has respectively \(0,1,2,3\) edges, the number of **binary** \(\mathsf F\)-preconditionals inducing that fixed negation is respectively \(729,81,16,1\). Thus the binary census is \(729+3\cdot81+3\cdot16+1=1021\).

The eight-element Boolean algebra is the **smallest Boolean algebra on which a fixed unary negation can admit multiple \(\mathsf T\)- or \(\mathsf F\)-preconditional extensions**. With one atom there is one operation in both classes; with two atoms there are four \(\mathsf T\) and two \(\mathsf F\) operations, and each has a distinct unary negation. With three atoms, one \(\mathsf F\)-negation already admits \(729\) different operations.

## Assumptions and scope
The Boolean lattice \(B=\mathcal P(V)\), where \(V\) has \(n\) labelled atoms, has \(0=\varnothing\) and \(1=V\). A **preconditional** is a binary operation satisfying, for all \(a,b,c\in B\):

\[
\begin{aligned}
\text{P1: }&1\Rightarrow a\subseteq a,\\
\text{P2: }&a\cap b\subseteq a\Rightarrow b,\\
\text{P3: }&a\Rightarrow b\subseteq a\Rightarrow(a\cap b),\\
\text{P4: }&a\Rightarrow(b\cap c)\subseteq a\Rightarrow b,\\
\text{P5: }&a\Rightarrow((a\cap b)\Rightarrow c)\subseteq(a\cap b)\Rightarrow c.
\end{aligned}
\]

A \(\mathsf T\)-preconditional also satisfies \(a\Rightarrow a=V\) and \(a\cap(a\Rightarrow\varnothing)=\varnothing\). A \(\mathsf F\)-preconditional further satisfies \(a\subseteq N(N(a))\). No modus-ponens, normality, or negation-import axiom is assumed. Counts are for the fixed labelled Boolean carrier; the proof's counting part concerns \(n\le3\), not arbitrary lattices or unlabelled expansion classes.

## Proof
**1. Exact row reduction.** For any preconditional, P1 and P2 give \(V\Rightarrow b=b\). P3 and P4 give \(a\Rightarrow b=a\Rightarrow(a\cap b)\), and P4 gives monotonicity in its second argument. For each \(a\subseteq V\), define \(f_a(t)=a\Rightarrow t\) on \(t\subseteq a\). P2, conditional identity and semicomplementation respectively impose
\[
t\subseteq f_a(t),\qquad f_a(a)=V,\qquad a\cap f_a(\varnothing)=\varnothing.
\]
The maps \(f_a\) are monotone, \(f_V(t)=t\), and \(f_\varnothing(\varnothing)=V\). The entire content of P5 is the following **finite row-coherence condition**, for every \(d\subseteq a\) and \(t\subseteq d\):
\[
 f_a\bigl(a\cap f_d(t)\bigr)\subseteq f_d(t). \tag{1}
\]
Conversely, all these displayed row conditions imply P1--P5, conditional identity and semicomplementation, by reversing the preceding substitutions. In particular, the \(d=a\) part of (1), together with monotonicity and extensivity, is equivalent to \(f_a(a\cap f_a(t))=f_a(t)\).

**2. Three-atom \(\mathsf T\) census.** Set \(V=\{1,2,3\}\), and write \(N_i=f_{\{i\}}(\varnothing)\). On a singleton antecedent, the entire row is determined by \(N_i\subseteq V\setminus\{i\}\), because \(f_{\{i\}}(\{i\})=V\). The three \(N_i\) therefore give \(4^3=64\) possibilities, identified with loop-free directed graphs on \(V\): an arrow \(i\to j\) means \(j\in N_i\).

Fix a doubleton \(a=\{i,j\}\), writing \(k\) for the remaining atom, and put \(x=f_a(\varnothing)\), \(y=f_a(\{i\})\), \(z=f_a(\{j\})\). Self-coherence in (1) leaves precisely
\[
x\in\{\varnothing,\{k\}\},\quad
y\in\{\{i\},\{i,k\},V\},\quad
z\in\{\{j\},\{j,k\},V\},
\]
with \(x\subseteq y\cap z\) and \(f_a(a)=V\). The only additional nontrivial conditions are
\[
f_a(a\cap N_i)\subseteq N_i,\qquad
f_a(a\cap N_j)\subseteq N_j. \tag{2}
\]
Indeed, each proper nonempty sub-antecedent of a doubleton is a singleton; the \(d=\varnothing\) and \(d=V\) conditions are automatic. No two different doubleton rows are comparable, hence after the singleton rows are fixed the three doubleton rows can be chosen independently.

For a directed graph \(G\), let \(c_{ij}(G)\) be the number of at most \(2\cdot3\cdot3=18\) triples \((x,y,z)\) surviving these explicitly stated tests for \(a=\{i,j\}\). The exact total is therefore
\[
\sum_{G\text{ on }\{1,2,3\}\text{ directed loop-free}}
 c_{12}(G)c_{13}(G)c_{23}(G)=7820. \tag{3}
\]
Here is a short complete finite evaluation, grouped into the sixteen directed-graph relabelling orbits. Encode a graph as a six-bit integer \(g\) with bit positions (least significant first) corresponding to the directed edges \((1,2),(1,3),(2,1),(2,3),(3,1),(3,2)\). The columns give a representative, orbit size, and the three local row counts; the contribution of a row is the orbit size times the product of the three counts.

| \(g\) | Orbit size | \((c_{12},c_{13},c_{23})\) |
|---:|---:|:---|
| 0 | 1 | (9,9,9) |
| 1 | 6 | (3,9,9) |
| 3 | 3 | (6,6,9) |
| 5 | 3 | (1,9,9) |
| 6 | 6 | (3,3,9) |
| 7 | 6 | (2,6,9) |
| 10 | 3 | (13,3,3) |
| 11 | 6 | (8,6,3) |
| 15 | 3 | (5,6,6) |
| 21 | 6 | (1,3,13) |
| 23 | 3 | (2,2,13) |
| 25 | 2 | (3,3,3) |
| 27 | 6 | (8,2,3) |
| 30 | 3 | (8,1,8) |
| 31 | 6 | (5,2,8) |
| 63 | 1 | (5,5,5) |

There are \(64\) directed graphs in the sixteen orbits; the weighted product sum is exactly \(7820\). This is a finite combinatorial identity with every option and filter specified, not an extrapolation from sampled algebras.

**3. The \(\mathsf F\) refinement.** For antitone \(N\), double-negation inflation is equivalent to the self-adjointness rule \(A\subseteq N(B)\Longleftrightarrow B\subseteq N(A)\). Together with semicomplementation this identifies \(N\) with the polarity of a simple undirected graph on the atoms: \(j\in N(\{i\})\) iff \(i\) is adjacent to \(j\), and \(N(A)\) is the common-neighbor set of all vertices in \(A\). Thus there are eight choices of \(N\).

For each such \(N\), condition (2) remains the exact constraint on each doubleton row, now also fixing \(x=N(a)\). If the graph has no edges, the three doubleton rows each admit nine choices, giving \(9^3=729\). If there is one edge, their counts are \((1,9,9)\), giving \(81\). With two edges the counts are \((4,2,2)\), giving \(16\). For the complete graph every doubleton row is forced, giving \(1\). Summing over the \(1,3,3,1\) graphs of these types gives exactly \(1021\).

**4. Minimality of nonunique negation lifts.** On the two-element Boolean algebra, the top and bottom rows are forced. On the four-element Boolean algebra the only other rows have singleton antecedents, each uniquely determined by its value at \(\varnothing\); there are four \(\mathsf T\) operations and exactly two satisfy \(\mathsf F\). No two on either carrier share the same negation. On \(\mathcal P(\{1,2,3\})\), the empty simple graph has the same \(\mathsf F\)-negation for \(729\) different binary operations, proving both strictness and sharpness. Explicitly, with that negation the row for antecedent \(\{1,2\}\) may take the value \(\{1\}\) or \(\{1,3\}\) at consequent \(\{1\}\), keeping the other row choices fixed at their minimal allowed values; the coherence tests still hold.

## Verification
Run `python3 verify_census.py` using Python 3 with its standard library. It generates all row maps satisfying the necessary and sufficient normal form, reconstructs all complete tables, and **checks each table directly against all five original axioms**, identity and semicomplementation. It separately checks double-negation inflation, all negation fibers, and the sixteen directed-graph orbit contributions. Its completion marker is `BOOLEAN_PRECONDITIONAL_BINARY_CENSUS_OK`. All asserted numbers are exact integers. The executable checker is a reproducibility aid and finite enumeration certificate; the finite combinatorial proof above establishes exhaustiveness.

## Relationship to prior work
Holliday introduced preconditionals with axioms P1--P5 and proved general representation theorems. His finite-Boolean selection-frame representation (Proposition 7) imposes additional modus-ponens, normality and negation-import conditions; it does not give this full binary \(\mathsf T\)/\(\mathsf F\) census. Chen introduced the explicit \(\mathsf T\)/\(\mathsf F\) hierarchy with conditional identity, semicomplementation and double-negation inflation, establishing completeness and decidability; the inspected text does not give these counts or fiber sizes. Existing classifications of unary negation reducts distinguish only \(125\) and \(8\) unary operations on this Boolean carrier; the present theorem counts their distinct binary lifts. Published finite-chain preconditional enumerations address non-Boolean carriers and do not imply the Boolean three-atom census by restriction or duality.

## Limitations
The numbers concern labelled binary operation tables on exactly eight Boolean elements. They do not count isomorphism classes, all preconditionals without the \(\mathsf T\) axioms, or all higher-atom Boolean carriers. The novelty comparison is best-knowledge rather than an exhaustive mathematical-publication census; an unlocated equivalent finite-algebra enumeration remains a priority risk. No independent audit or external validation has been performed.

## References
1. Zhicheng Chen, *Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations*, arXiv:2607.20221, first version 22 July 2026. https://arxiv.org/html/2607.20221
2. Wesley H. Holliday, *Preconditionals*, arXiv:2402.02296, first version 3 February 2024; relevant Definitions and Propositions 1--2 and 7. https://arxiv.org/pdf/2402.02296
3. *Factorial classification of preconditionals on finite chains*, published-finding corpus public record `2026/10/4/SCOPE-factorial-classification-of-preconditionals-on-finite-chains--cbc434a2c6a0`. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-factorial-classification-of-preconditionals-on-finite-chains--cbc434a2c6a0
