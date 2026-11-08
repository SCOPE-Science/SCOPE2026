# Exact three-periodic excitation census on full graph subdivisions

## Finding
Let \(H=(V,E)\) be any finite connected simple graph with at least two vertices, and let \(S(H)\) be its **full subdivision**: replace every edge \(uv\in E\) with the path \(u,e_{uv},v\), with a distinct new vertex for each edge. Consider synchronous three-state threshold-one Greenberg–Hastings excitation on \(S(H)\). The number \(P_3(S(H))\) of labelled configurations whose **least** temporal period is exactly three, with all three phases counted, is
\[
P_3(S(H))=\sum_{c:V\to\mathbb Z/3\mathbb Z}\;\prod_{v\in V}\bigl(2^{d^-_c(v)}-1\bigr),\qquad
 d^-_c(v)=\#\{w\in N_H(v):c(w)=c(v)+2\pmod3\}.
\]
In particular,
\[
P_3(S(H))>0\quad\Longleftrightarrow\quad H\text{ contains a simple cycle of length divisible by }3.
\]
Exactly one configuration is fixed by the dynamics (the all-resting configuration), so the number of configurations fixed by the third iterate is \(1+P_3(S(H))\). Every nonfixed configuration counted above has least period three, and the number of distinct primitive three-cycles is \(P_3(S(H))/3\).

For \(H=K_n\), where \(n\ge3\), the sum specializes to
\[
P_3(S(K_n))=
\sum_{\substack{a,b,c\ge1\\a+b+c=n}}
\frac{n!}{a!\,b!\,c!}
(2^c-1)^a(2^a-1)^b(2^b-1)^c.
\]
The first values for \(n=3,4,5,6,7,8\) are respectively \(6,108,2850,127440,9109086,1024394868\).

## Assumptions and scope
The graph is finite, undirected, connected, loopless and simple, with at least two vertices; vertices and inserted edge-vertices are individually labelled. At each integer time, vertices update simultaneously under
\[
0\mapsto\begin{cases}1&\text{if some neighbor has state }1,\\0&\text{otherwise},\end{cases}
\qquad 1\mapsto2,\qquad2\mapsto0.
\]
A configuration is **initially periodic of primitive period three** if the third iterate equals the initial configuration and the first iterate does not. Time phases are counted as distinct labelled configurations, not identified by spatial automorphism. The formula does not claim to enumerate transient basins or other primitive periods.

## Proof
**1. Every nonfixed three-periodic trajectory is fully cycling.** In any three-step periodic trajectory, each vertex either remains in state zero at all times or visits the states \(0,1,2\) once each. Indeed, a state one must advance to two, then zero; if it recurs within three updates, the zero-to-one transition must also occur. If a vertex remains zero throughout, none of its neighbors can visit state one (since that neighbor would force an excitation during one of the three phases). Because \(S(H)\) is connected, the presence of one cycling vertex forces every vertex to cycle. Thus every nonfixed three-periodic state is of the form \(z_t(x)=z_0(x)+t\pmod3\) at every vertex, and the necessary and sufficient local condition is
\[
\forall x\in V(S(H))\quad\exists y\in N_{S(H)}(x):z_0(y)=z_0(x)+1\pmod3.
\tag{1}
\]
If (1) holds, the stated rotating trajectory satisfies the local rule for all three phases. Conversely, any fully cycling trajectory must satisfy (1).

**2. Eliminate the inserted vertices.** Fix arbitrary labels \(c:V(H)\to\mathbb Z/3\mathbb Z\) of the original vertices. For an inserted vertex \(e_{uv}\), condition (1) says its label \(z(e_{uv})\) must belong to
\[
\{c(u)-1,\;c(v)-1\}\pmod3.
\tag{2}
\]
If \(c(u)=c(v)\), this is a singleton and the choice can help neither endpoint of the original edge. If the colors differ, (2) has exactly two options. Exactly one endpoint, namely the endpoint \(v\) for which the other endpoint has color \(c(v)+2\pmod3\), can be helped by this edge: one option in (2) puts the inserted vertex in color \(c(v)+1\), which supplies its required successor; the other option helps neither endpoint. In particular, an edge of unlike colors never supplies the needed successor to both endpoints.

For each original vertex \(v\), exactly \(d^-_c(v)\) incident original edges are eligible to help it. To satisfy (1) at \(v\), a nonempty subset of these edges must choose their helpful option. There are \(2^{d^-_c(v)}-1\) such subsets. Each unlike-colored original edge belongs to exactly one of these eligible-edge sets, so the choices are disjoint across original vertices. Same-colored edges have their unique forced label. Therefore the choices multiply and give the stated summand. Summation over all original colorings gives precisely \(P_3(S(H))\), by Step 1, without overcounting.

**3. Exact cycle criterion.** The summand associated with \(c\) is positive if and only if every vertex \(v\) has a neighbor of color \(c(v)+2\pmod3\). If this holds, choose one such neighbor \(f(v)\) for each vertex. Iterating the function \(f\) on the finite vertex set produces a directed simple cycle. Along every directed edge the color decreases by one modulo three, so the cycle length is a positive multiple of three. Its length cannot be one or two because \(H\) has no loops and opposite edges cannot both decrease the color by one modulo three. Hence \(H\) contains a simple cycle of length divisible by three.

Conversely, take a simple cycle of length divisible by three and orient it cyclically. Color successive vertices \(0,1,2,0,1,2,\ldots\). Each cycle vertex has its predecessor as a neighbor whose color is two greater modulo three. Extend this coloring to the remaining vertices along a spanning forest rooted on the cycle, assigning to each new child the color of its parent plus one modulo three. Every vertex now has such a predecessor neighbor. All factors in the product are positive, and Step 2 constructs at least one primitive three-periodic state. This proves the equivalence.

**4. Complete-graph specialization and orbit count.** In \(K_n\), positivity forces all three original colors to occur. If their class sizes are \(a,b,c\), the predecessor-neighbor counts are \(c,a,b\) on the three respective classes. The number of original colorings with those class sizes is \(n!/(a!b!c!)\), yielding the stated sum. Since all nonzero counted states rotate all vertices by one modulo three, they have least period three and form disjoint groups of three. The only fixed state of the Greenberg–Hastings rule is the all-zero state, proving the remaining assertions.

## Verification
The standalone scripts `verify_direct.py` and `verify_structure.py` use only the Python standard library. Run from a directory containing the scripts using `python verify_direct.py` and `python verify_structure.py`.

`verify_direct.py` directly constructs the full subdivision, iterates the three-state dynamics over every state, and compares primitive-period-three counts against an independently coded product. It checks the triangle, complete four-vertex graph, four-cycle, complete bipartite graph on parts of sizes two and three, and six-cycle, examining a total of \(774927\) configurations. The expected and direct counts agree: \(6,108,0,0,6\), with exactly one fixed state in each case.

`verify_structure.py` independently enumerates allowed labels for all inserted edge-vertices. It compares this enumeration with the local-product formula and a separate simple-cycle search for all \(43\) connected labelled graphs on two, three or four vertices. It also evaluates the complete-graph specialization through eight original vertices and cross-checks the first three sizes against the local-product sum. Both scripts passed in the recorded outputs. These finite tests corroborate the explicit unrestricted proof; they do not substitute for it.

## Relationship to prior work
The three-state Greenberg–Hastings rule and persistent wave objects are classical; see Durrett–Griffeath (1993). Gravner–Lyu–Sivakoff (2016), Theorem 3, characterizes synchronization and asymptotic excitation rate on finite connected graphs by cycle integrals of an initial-coloring one-form; its Lemma 1 provides a comparison representation. These results address broad excitation and nonfixation questions, but the displayed material does not present the exact **initially primitive three-periodic configuration** count for full subdivisions or the edge-factorization formula here. The cycle criterion here is specifically for immediate primitive period three; it is **not** a criterion for any eventual nontrivial oscillation. For example, a four-cycle has no cycle of length divisible by three, so its full subdivision has no initially primitive three-periodic state; this does not contradict the general activity results.

## Limitations
The formula may require an exponential sum over colorings of \(H\) on unstructured inputs. It counts only the initially primitive three-periodic subsystem and not longer periods, transient dynamics, or period-three basins. All counts are for labelled configurations; dividing by graph automorphisms is not justified. The stated historical comparison is based on inspected accessible sources and targeted searches, not on an exhaustive worldwide priority certification; results expressed in an alternative graph-coloring language could provide unrecognized overlap.

## References
- R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, first submitted 1993-03-22. https://arxiv.org/abs/patt-sol/9303002
- J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, first submitted 2016-10-24; especially Section 2, Lemma 1 and Theorem 3, and Section 4. https://arxiv.org/html/1610.07320v1
