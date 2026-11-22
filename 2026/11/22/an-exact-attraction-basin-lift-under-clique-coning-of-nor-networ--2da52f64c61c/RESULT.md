# An exact attraction-basin lift under clique coning of NOR networks

## Finding
Let \(H\) be any finite undirected simple graph with \(n\ge2\) labelled vertices and **no isolated vertices**. Put \(G_r=H\vee K_r\), where the \(r\ge0\) added vertices form a clique and are all adjacent to every vertex of \(H\). On every graph use synchronous binary **open-neighborhood NOR**: a vertex changes to one exactly when all its graph-neighbors are zero (without reading its own bit).

The all-zero and all-one configurations form a distinguished primitive two-cycle \(\mathcal A_r\). Let \(T(H)\) be the number of *total dominating sets* of \(H\), meaning subsets \(S\subseteq V(H)\) such that every vertex has a neighbor in \(S\). Its full attraction basin obeys the all-size identity
\[
\boxed{\bigl|\mathcal B_{G_r}(\mathcal A_r)\bigr|
       =2^{n+r}-2^n-r+1+T(H).}
\]
More strongly, every other fixed point or primitive two-cycle of the base NOR map survives after adjoining \(K_r\), with **exactly the same basin cardinality and least period**, on states where all new vertices are zero. There are precisely \(r\) additional fixed points (one for each new clique singleton), each with a singleton attraction basin, and no other new attractors. Consequently, if \(f_H\) has \(a\) fixed points and \(b\) primitive two-cycles, then \(f_{G_r}\) has \(a+r\) fixed points and \(b\) primitive two-cycles.

Every state is periodic after at most one update: \(f_{G_r}^3=f_{G_r}\). For every \(r\ge1\), the distinguished two-cycle has the unique largest basin, indeed strictly more than half the \(2^{n+r}\) states. At fixed base \(H\), its attraction probability tends to one as the number of added clique vertices grows:
\[
\Pr(\mathcal A_r)=1-\frac{2^n-T(H)-1+r}{2^{n+r}}\longrightarrow1.
\]

## Assumptions and scope
All graphs are finite, loopless and undirected; their vertex labels are fixed. All state bits update simultaneously, and no local rule reads the site's own state. Every vertex of \(H\) has at least one neighbor; the theorem is not stated for isolated-base vertices. The all-one configuration is understood on the *whole current* graph. A basin is the set of initial states eventually entering the specified orbit, counting periodic points themselves. The binomial-like graph operation \(\vee\) is the graph join; \(K_0\) is empty. The formulas are exact for every \(n\ge2\) and integer \(r\ge0\).

## Proof
**General NOR identity.** For any undirected simple graph \(X\), let \(f\) denote its open-neighborhood NOR map. With coordinatewise Boolean order, \(f\) is antitone. Moreover \(x\le f^2(x)\): if \(x_v=1\), each neighbor \(w\) of \(v\) receives \(f(x)_w=0\), so \(f^2(x)_v=1\). Antitonicity gives \(f^3(x)\le f(x)\), while applying the inflation inequality to \(f(x)\) gives \(f(x)\le f^3(x)\). Thus \(f^3=f\) for every \(X\), and each first iterate is fixed or two-periodic.

**Base basin.** Since \(H\) has no isolated vertices, \(f_H(\mathbf0)=\mathbf1\), \(f_H(\mathbf1)=\mathbf0\), and \(f_H(x)=\mathbf1\) holds only when \(x=\mathbf0\): any active vertex would force an output zero at one of its neighbors. Also \(f_H(x)=\mathbf0\) if and only if the active support of \(x\) totally dominates \(H\). Every state is periodic after at most one update. Hence the base distinguished two-cycle has exactly \(T(H)+1\) incoming states in its basin: the \(T(H)\) total-dominating states (mapping to zero) and the single all-zero state (mapping to all-one). These sets are disjoint.

**One-vertex lift.** Write a state of \(X\vee K_1\) as \((h,x)\), where \(X\) has no isolates, with hub bit \(h\). The exact rule is
\[
F(h,x)=\bigl(\mathbf1_{\{x=\mathbf0\}},\ (1-h)f_X(x)\bigr).
\]
The point \((1,\mathbf0)\) is fixed and has no other predecessor. Every \((1,x)\) with \(x\ne\mathbf0\) maps to \((0,\mathbf0)\), and \((0,\mathbf0)\) maps to \((1,\mathbf1)\); these states reach the new distinguished oscillator. For \(x\ne\mathbf0\), the state \((0,x)\) maps to \((0,f_X(x))\) unless \(f_X(x)=\mathbf0\), when it enters the distinguished oscillator. If \(f_X(x)\ne\mathbf0\), then \(f_X^2(x)\ge x\ne\mathbf0\), and \(f_X^3=f_X\) prevents any later zero. Therefore its subsequent trajectory stays on the hub-zero slice and agrees exactly with the old orbit, including its basin assignment. It follows that all nonprincipal basins are unchanged; the principal basin gains \(2^{|V(X)|}-1\) states, and a new singleton fixed basin appears.

**Iteration.** Each \(G_j\) has no isolated vertices. Apply the one-vertex lift successively for \(j=0,\ldots,r-1\). The distinguished basin gains \(2^{n+j}-1\) at stage \(j\), so summation gives
\[
T(H)+1+\sum_{j=0}^{r-1}(2^{n+j}-1)
=T(H)+1+2^{n+r}-2^n-r.
\]
All remaining attractors and their basin populations are preserved except for one singleton fixed point added at each stage. Since \(V(H)\) itself is total dominating, \(T(H)\ge1\). For \(r=1\), the special basin is \(2^n+T(H)>2^n\), more than half the enlarged state space. It remains more than half under subsequent stages because the special basin grows by \(2^{n+j}-1\), while the total population doubles. Equivalently, the displayed formula directly verifies this for every \(r\ge1\). It is therefore the unique largest basin. The limiting probability follows by division by \(2^{n+r}\).

## Verification
Two structurally distinct standalone Python programs accompany the proof. `verify_coning.py` uses bit-mask transitions and successor-path basin decomposition. It checked every labelled isolate-free graph with \(2\le n\le5\) (814 base graphs), each with one and two added universal clique vertices, and 131 additional seeded random graphs on six vertices with both attachment sizes: **1,890 graph/attachment experiments**, all passing. `verify_coning_independent.py` uses sets of vertices, explicit edge predicates and a separately implemented state-trajectory partition, exhaustively covering all 46 isolate-free base graphs of orders two through four with one, two and three added vertices: **138 experiments**, all passing. Each checker compares the complete labelled attractor/basin dictionary, not only the principal basin formula; the first additionally checks \(F^3=F\) state by state. Both run with Python 3 standard library alone:

```sh
python3 verify_coning.py
python3 verify_coning_independent.py
```

Concrete cases: for \(H=P_4\), \(T(H)=4\) and the distinguished basin grows from \(5\) on \(H\) to \(20\), \(51\), \(114\) on \(H\vee K_r\) for \(r=1,2,3\). For \(H=C_4\), \(T(H)=9\), giving \(10\), \(25\), \(56\), \(119\). For \(H=K_4\), \(T(H)=11\), giving \(12\), \(27\), \(58\), \(121\). The proof, rather than those finite checks, establishes all orders and all attachment sizes.

## Relationship to prior work
The fixed-point/independent-set correspondence for negative AND-NOT networks was studied by Veliz-Cuba and Laubenbacher (public online date 15 October 2011), and the graph-theoretic fixed-point extremal theory by Aracena, Richard and Salinas (2014). General parallel graph dynamics were surveyed by Aledo, Martinez and Valverde (2015); the 2020 paper of Aledo and collaborators studies periodic-point counts in homogeneous max/minterm networks. Those concerns do not themselves state this exact *transport of every attraction basin* under arbitrary clique joins, nor its total-domination correction and sharp dominance.

The earlier wheel-specific NOR basin identity for \(H=C_n\) is a special case of the principal-basin count and is not claimed to be new. The result proved here is instead the all-base, all-clique **complete basin transport theorem**: every other attraction basin remains exactly unchanged and the newly introduced basins are precisely specified. This is stronger information than a single oscillator's attraction probability. No claim of definitive historical priority is made.

## Limitations
The proof assumes no isolated vertex in the base graph. It does not classify the original base graph's nonprincipal attractors internally; rather it transfers any such classification without changing its basin data. Computational checks cover only the finite ranges stated and are not a proof of the quantified theorem. Historical priority requires further independent specialist review; one directly relevant 2011 fixed-point article was accessible in abstract and bibliographic form but not in full through the available access route.

## References
1. A. Veliz-Cuba and R. Laubenbacher, *On the computation of fixed points in Boolean networks*, Journal of Applied Mathematics and Computing 39 (2012), 145–153, first online 2011-10-15, https://doi.org/10.1007/s12190-011-0517-9.
2. J. Aracena, A. Richard and L. Salinas, *Maximum number of fixed points in AND–OR–NOT networks*, Journal of Computer and System Sciences 80 (2014), 1175–1190, https://doi.org/10.1016/j.jcss.2014.04.025.
3. J. A. Aledo, S. Martinez and J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Journal of Applied Mathematics (2015), Article 594294, first online 2015-03-24, https://doi.org/10.1155/2015/594294.
4. J. A. Aledo, A. Barzanouni, G. Malekbala, L. Sharifan and J. C. Valverde, *Counting Periodic Points in Parallel Graph Dynamical Systems*, Complexity (2020), Article 9708347, https://doi.org/10.1155/2020/9708347.
