# Branching entropy and exact primitive-three excitation counts on binary trees of triangles

## Finding

**Theorem.** For each integer \(h\geq0\), let \(G_h\) be the triangular cactus constructed from one marked triangle by attaching two child triangles, one at each nonmarked vertex, and recursively continuing for \(h\) generations. Each nonroot triangle is attached to its parent at one marked vertex and has two children at its two other vertices until the terminal generation. Thus \(G_h\) has \(2^{h+1}-1\) triangle blocks and \(2^{h+2}-1\) vertices. This graph is the line graph of a tree whose internal vertices have degree three and whose internal-vertex skeleton is a full rooted binary tree of height \(h\).

Run the synchronous deterministic, threshold-one, three-state Greenberg–Hastings update on \(G_h\): state \(1\) becomes \(2\), state \(2\) becomes \(0\), and state \(0\) becomes \(1\) exactly when an adjacent vertex is in state \(1\), remaining \(0\) otherwise. Let \(P_h\) be the number of labelled configurations whose **least period is three from the initial time**.

Define integer sequences by \(A_0=2\), \(B_0=1\) and, for every \(h\ge0\),
\[
 A_{h+1}=5A_h^2+6A_hB_h+2B_h^2,\qquad
 B_{h+1}=4A_h^2+4A_hB_h+B_h^2.
\]
Then the exact primitive-period-three population and its three-cycle orbit count are
\[
 \boxed{P_h=3A_h},\qquad \boxed{\#\text{ distinct primitive-three cycles}=A_h}.
\]
In particular, the first values of \(P_h\) are \(6,102,36390,4544307366\).

The periodic-state entropy per triangle block exists, with the explicit rapidly convergent expression
\[
 c=\lim_{h\to\infty}\frac{\log P_h}{2^{h+1}-1}
 =\frac12\log2+\sum_{j=0}^{\infty}2^{-j-2}\log(5+6r_j+2r_j^2),
 \quad r_0=\frac12,\quad r_{j+1}=\frac{4+4r_j+r_j^2}{5+6r_j+2r_j^2}.
\]
Numerically \(c\approx1.466986139797\) (growth base \(e^c\approx4.336146887348\) per triangle block). Moreover, the strictly proved inequality
\[
 \boxed{c>\log(2+\sqrt5)}
\]
shows that binary branching gives a larger primitive-three population entropy per vertex than a linear chain of triangles, whose exact growth base per block is \(2+\sqrt5\).

## Assumptions and scope

All graphs are finite, simple, connected, undirected and vertex-labelled by the recursive construction. Attached triangles share exactly one vertex with their parent and are otherwise vertex-disjoint, with no edges other than triangle edges. The root mark selects one distinguished root vertex but does not alter the graph dynamics. No asynchronous updates, stochastic excitation, higher thresholds, or eventual-period counts are included. The count includes complete color assignments on all \(2^{h+2}-1\) vertices. The fixed all-zero state is excluded.

## Proof

**0. Graph identification.** Construct a tree with one trivalent internal vertex per triangle block, connect internal vertices according to the parent-child block tree, and attach terminal leaves until every internal degree is three. Each edge of this tree becomes a vertex of its line graph; the three edges incident to each internal vertex form the corresponding triangle. Shared internal edges give exactly the prescribed one-vertex intersections, proving the stated line-graph identification.

**1. Period-three criterion.** On any connected graph, a configuration that returns after three steps either is all zero or has every vertex cyclically advancing by one color at every step. Indeed, a vertex whose three-step trajectory contains state \(1\) must follow the entire cycle \(1\to2\to0\to1\), and a vertex not following that cycle remains \(0\) at all three instants. A permanently resting vertex cannot be adjacent to an advancing vertex, because the latter is in state \(1\) during one of the three instants. Connectedness therefore rules out mixed types. For an all-advancing state, the update is valid exactly when each vertex has a neighbor with color one greater modulo three in the initial coloring: this neighbor supplies excitation at the instant the vertex is at rest. All such colorings have least period three. Hence \(P_h\) is three times the number of successor-supported colorings with a fixed root color.

**2. Boundary counts.** Regard one rooted triangular subtree \(G_h\) as attached to an unmodelled parent graph at its marked vertex. Fix that vertex's color to \(0\). Let \(A_h\) count assignments where every vertex, including the marked one, has a successor-colored neighbor within the subtree. Let \(B_h\) count assignments where every vertex except the marked one is successor-supported, while the marked one has no successor within the subtree and would require support from its parent. Global cyclic recoloring shows the counts are unchanged if the marked color is \(1\) or \(2\). For one triangle, the supported assignments at root color \(0\) have the other two colors \((1,2)\) and \((2,1)\). The unsupported assignment has \((2,2)\). Thus \((A_0,B_0)=(2,1)\).

**3. Exact nine-case branching recursion.** Fix root color \(0\) at the next level and call the other two triangle colors \(u,v\in\{0,1,2\}\). For the child at \(u\), the triangle supplies its required successor precisely when \((u+1)\bmod3\in\{0,v\}\). If supplied, that child's rooted subtree has \(A_h+B_h\) choices; otherwise it has only \(A_h\). Similarly, the child at \(v\) receives support from the root triangle precisely when \((v+1)\bmod3\in\{0,u\}\). The root receives support when \(1\in\{u,v\}\). Summing the nine ordered pairs \((u,v)\), the supported-root polynomial is
\[
2A_h(A_h+B_h)+A_h^2+2(A_h+B_h)^2=5A_h^2+6A_hB_h+2B_h^2,
\]
and the unsupported-root polynomial is
\[
A_h^2+2A_h(A_h+B_h)+(A_h+B_h)^2=4A_h^2+4A_hB_h+B_h^2.
\]
No assignment is counted twice because each child belongs to a unique rooted subtree, and the only overlaps are the two specified attachment vertices. At the full root there is no parent to provide support, so only \(A_h\) assignments per fixed root phase are valid. This proves \(P_h=3A_h\), and each orbit has exactly three states.

**4. Entropy and sharp branching comparison.** Put \(r_h=B_h/A_h\), which is positive. The recurrence gives
\[
 r_{h+1}=f(r_h)=\frac{4+4r_h+r_h^2}{5+6r_h+2r_h^2},\qquad
 \log A_{h+1}=2\log A_h+\log q(r_h),\quad q(r)=5+6r+2r^2.
\]
Direct differentiation yields \(f'(r)=-2(r+1)(r+2)/q(r)^2<0\). The interval \([1/2,3/4]\) is mapped by \(f\) into \([121/170,25/34]\subset[1/2,3/4]\). Thus every \(r_h\) is bounded there and, for \(h\ge1\), satisfies \(r_h\ge121/170\). The logarithmic recurrence iterates exactly as
\[
\log A_h=2^h\log2+\sum_{j=0}^{h-1}2^{h-1-j}\log q(r_j).
\]
Dividing by \(2^{h+1}-1\), using boundedness of \(q(r_j)\), and noting \(\log3/(2^{h+1}-1)\to0\), gives the absolutely convergent displayed series for \(c\).

For a rigorous strict comparison, \(q(r_0)=17/2\) and \(q(r_j)>10\) for all \(j\ge1\). Hence
\[
 c>\frac12\log2+\frac14\log(17/2)+\frac14\log10
  =\frac14\log340.
\]
Since \((2+\sqrt5)^4=161+72\sqrt5<340\), we obtain \(c>\log(2+\sqrt5)\). For comparison, apply the same boundary classification independently to a **linear** chain: in a rooted triangle with only one continuing child at color \(u\), its other nonroot vertex \(v\) is terminal and must have its successor within that triangle. Enumerating the nine \(u,v\) pairs under this additional terminal constraint gives supported-root \(3A+2B\) and unsupported-root \(2A+B\). Thus the one-child rooted transfer is exactly \(\begin{psmallmatrix}3&2\\2&1\end{psmallmatrix}\), whose dominant eigenvalue is \(2+\sqrt5\), and whose two-step population recurrence is \(N_{m+2}=4N_{m+1}+N_m\). A chain of \(m\) triangles has \(2m+1\) vertices. Thus the comparison is for equal vertex-per-triangle density, not merely a different normalization. This proves the theorem.

## Verification

The standalone script `recurrence_check.py` independently constructs all nine polynomial cases, verifies their coefficients, prints the integer recurrence through height six, and evaluates the convergent entropy series. Its reported real number is an approximation; the exact inequality is proved above. The separate C++17 program `direct_check.cpp` constructs the graphs and exhaustively iterates the **actual Greenberg–Hastings update three times** on every one of \(3^3+3^7+3^{15}=14,351,121\) states for heights zero, one and two. It finds respectively \(6,102,36390\) initially primitive-three states, matching the all-height recurrence. The programs and captured outputs are included and can be rerun with `python3 recurrence_check.py` and `g++ -std=c++17 -O3 direct_check.cpp -o direct_check && ./direct_check`.

## Relationship to prior work

Gravner, Lyu and Sivakoff (arXiv:1610.07320, first submitted 24 October 2016) characterize synchronization and limiting excitation activity on arbitrary finite graphs, particularly establishing that three-color Greenberg–Hastings dynamics on an ordinary tree synchronizes. Their cycle-integral criterion does not count configurations already on period-three orbits on the **line graph** of a tree. Doba (2018) likewise establishes general convergence and excitation-rate criteria, not this branching recurrence or entropy. The triangular cactus **chain** has a distinct linear transfer recurrence with dominant base \(2+\sqrt5\). A branching tree of triangles has a nonlinear two-terminal recursion and the strictly greater per-block entropy derived here; the chain formula cannot be substituted to obtain the present count. General cactus results about **eventual** excitation rates do not determine the more restrictive immediately periodic populations.

## Limitations

The result concerns only immediately period-three configurations, not the basin sizes, first-entry times, other temporal periods, or arbitrary line graphs of trees. Finite simulation is not the proof of the all-height recurrence. The entropy constant is specified as a convergent series, not claimed to have an elementary closed form. Historical-priority assessment is limited to the identified primary literature and mathematical-record searches; unindexed equivalent results remain possible. Independent external validation has not been performed.

## References

1. J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (24 Oct 2016); *Annals of Applied Probability* **28** (2018), 3324–3357, doi:10.1214/17-AAP1350. Preprint: https://arxiv.org/abs/1610.07320 ; open full text: https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf.
2. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, *Complex Systems* **27** (2018), 101–126, doi:10.25088/ComplexSystems.27.2.101, https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf.
