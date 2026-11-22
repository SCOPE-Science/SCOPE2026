# Orbit-geodesic normal form for finitely supported binary relations on equality atoms

## Finding
Let \(\mathbb A\) be an infinite pure set of atoms, let \(S\subset\mathbb A\) have size \(m\), and let \(R\subseteq\mathbb A^2\) be invariant under all permutations fixing \(S\) pointwise. There is an exact finite normal form for **every directed shortest-path distance** of \(R\). In particular, the distance matrix on named atoms is the entrywise minimum of the internal directed distance matrix and a min-plus rank-one correction; all distances involving unnamed atoms are determined by two vectors and one scalar.

Write \(G=\mathbb A\setminus S\). Let \(E=R\cap(S\times S)\), and write \(\delta(c,d)\) for the shortest directed path length from \(c\) to \(d\) in \((S,E)\), where \(\delta(c,c)=0\) and unreachable distances are \(\infty\). Define
\[
F=\{c\in S: aRc\text{ for one, equivalently every, }a\in G\},\qquad
B=\{c\in S:cRa\text{ for one, equivalently every, }a\in G\}.
\]
Let \(o=1\) if \(aRb\) for two distinct elements of \(G\), and \(o=0\) otherwise. Put
\[
\alpha(c)=\min_{p\in F}\delta(p,c),\quad
\beta(c)=\min_{q\in B}\delta(c,q),\quad
\gamma=\min_{p\in F,q\in B}\delta(p,q),
\]
with empty minima \(\infty\). All sums and minima use the extended natural numbers.

For the *reflexive* graph distance \(d_R(u,v)\), these formulas hold simultaneously:
\[
\begin{aligned}
d_R(c,d)&=\min\{\delta(c,d),\,\beta(c)+2+\alpha(d)\} &&(c,d\in S),\\
d_R(a,c)&=1+\alpha(c) &&(a\in G,c\in S),\\
d_R(c,a)&=1+\beta(c) &&(c\in S,a\in G),\\
d_R(a,b)&=\begin{cases}1,&o=1,\\2+\gamma,&o=0\end{cases} &&(a,b\in G,\ a\ne b),\\
d_R(u,u)&=0 &&(u\in\mathbb A).
\end{aligned}
\]
(The named-pair equation includes \(c=d\), hence returns zero there.) The additional orbit bit recording generic loops \(aRa\) does not change these reflexive distances.

Consequently, for every \(m\ge0\), **every reachable ordered pair is connected by a path of length at most \(m+1\)**, and this uniform bound is sharp. Every finite-distance orbit profile can be evaluated by ordinary all-pairs shortest paths on the \(m\)-vertex graph \((S,E)\), followed by vector minima, in \(O(m^3)\) time. Also, the unnamed atoms are either all in one strongly connected component, or each lies in its own singleton component: the former occurs exactly when \(o=1\) or \(\gamma<\infty\).

The central claim is the five-case exact geodesic normal form (including its min-plus rank-one named-pair correction and the generic-component dichotomy). A universal finite-step reachability bound alone is already obtainable from general fixed-context orbit arguments and is not asserted as a separately novel principle.

## Assumptions and scope
The atom set is infinite, with the full equality symmetry (all permutations); \(S\) is any fixed finite support, not necessarily the least support. The relation \(R\) is arbitrary, including asymmetric edges and self-loops. The graph is unweighted and directed. Reflexive distances assign zero to identical endpoints even in the absence of a self-loop. An absent path has distance \(\infty\). All formulas apply when \(m=0\). Invariance makes the four types of generic-involving edge orbit uniform: \(G\times\{c\}\), \(\{c\}\times G\), the diagonal of \(G^2\), and its off-diagonal. This yields precisely the data \(E,F,B,o\) and a fifth, inessential generic-loop bit.

## Proof
**Orbit decomposition.** Permutations of \(G\) fixing \(S\) can map any element of \(G\) to any other, and any pair of distinct elements to any other such pair. Therefore \(R\) is specified by its restriction \(E\), the sets \(F\) and \(B\), and two Boolean choices for generic loops and distinct-generic edges. The definitions above are independent of the chosen generic atoms.

**Path normalization.** Let a directed path have at least two unnamed visits separated by a nonempty segment of named vertices. If the path enters the first unnamed atom from a named vertex \(q\) and exits its last unnamed atom to a named vertex \(p\), the edges \(q\to a\) and \(b\to p\) imply \(q\to b\) and \(b\to p\) for any unnamed \(b\). Replace that entire section by a two-edge passage through one unnamed vertex, which is no longer than the original. For a path starting at an unnamed atom, any later unnamed-to-named exit can instead be taken directly from the starting atom, because membership in \(F\) does not depend on which unnamed atom is used. The dual operation works for paths ending unnamed. Loops are deleted from shortest paths.

A shortest named-to-named path thus has either no unnamed vertex or exactly one. In the former case its length is \(\delta(c,d)\). In the latter it consists of a named path from \(c\) to some \(q\in B\), an edge to an unnamed atom, an edge to some \(p\in F\), and a named path to \(d\). Its minimum possible length is
\[
\min_{q\in B,p\in F}\bigl(\delta(c,q)+2+\delta(p,d)\bigr)=\beta(c)+2+\alpha(d).
\]
Conversely each finite term describes an actual path, so equality holds. A shortest unnamed-to-named path starts with an edge into some \(p\in F\) and stays named thereafter, proving \(1+\alpha(c)\); the converse construction works. Reversing gives the named-to-unnamed formula.

For two **distinct** unnamed endpoints, a direct edge exists exactly when \(o=1\). If it does not, unnamed-to-unnamed edges are only self-loops and cannot move between unnamed atoms. Every path between two distinct unnamed atoms must therefore leave the starting atom through some \(p\in F\), traverse named atoms, then return through some \(q\in B\). All other unnamed excursions can be shortcut as above, yielding the exact value \(2+\gamma\). This completes the five cases, including the zero-length diagonal case.

**Strong components.** The formula for \(d_R(a,b)\), where \(a,b\) are distinct unnamed atoms, is symmetric in their identities. Thus if one pair of distinct unnamed atoms is mutually reachable, all such pairs are; this happens exactly when \(o=1\) or \(\gamma<\infty\). If neither condition holds, no two distinct unnamed atoms are connected by any positive directed path, so their strongly connected components are singletons.

**Uniform cutoff.** Removing repeated vertices from any finite named-only shortest path uses at most \(m-1\) edges. A shortest path with one unnamed intermediate vertex cannot repeat any named vertex (otherwise it could be shortened); it uses at most \(m\) named vertices and hence at most \(m\) edges between named endpoints. For an unnamed/named pair the first/last unnamed visit, plus at most \(m\) named vertices, gives at most \(m\) edges. For two distinct unnamed endpoints, a shortest path either is a single edge or traverses at most \(m\) distinct named vertices between them, using at most \(m+1\) edges. Hence \(R^{\le m+1}=R^*\), where \(R^*=\bigcup_{j\ge0}R^j\) is the reflexive transitive closure.

For sharpness when \(m\ge1\), label \(S=\{c_1,\ldots,c_m\}\) and take only the named chain \(c_1Rc_2R\cdots Rc_m\), all arcs from unnamed atoms to \(c_1\), and all arcs from \(c_m\) to unnamed atoms; add no other arcs. Every path from one unnamed atom to a *distinct* unnamed atom then has length at least \(m+1\), achieved by the displayed chain. When \(m=0\), take all arcs between distinct atoms and no loops; the sharp length is one. These constructions also show that every support size admits the claimed bound without finite-domain artifacts.

## Verification
Run `python verify.py` with Python 3. The independent exhaustive checker constructs the actual finite directed graph on \(m\) named vertices and three anonymous representatives for every possible orbit encoding when \(m=0,1,2,3\), runs Floyd–Warshall on the full graph, and compares all entries to the five explicit formulas. These exhaustive cases comprise \(4+32+1024+131072=132132\) relations. It also tests 3000 deterministic-seeded samples with \(m=4\), and the sharp family through \(m=7\). On the reviewed package it returns `VERIFY_OK 135132 exhaustive m<=3, sampled m=4; sharp examples m=0..7`. The tests are finite checks only: the proof above supplies all-\(m\), infinite-atom validity.

## Relationship to prior work
Ciobanu (2026) develops fixed-context semantics for infinitely many atoms, including the bound on Boolean fixed-point iterations in terms of orbit counts and a reachability construction. For a starting singleton, that general orbit argument already yields a uniform finite path-length bound of this order. It does **not state the five exact pairwise geodesic formulas**, the min-plus rank-one form of the named distance matrix, or the all-or-none component dichotomy for unnamed atoms. The contribution here is that finer **inverse distance classification**, rather than mere termination.

Bojańczyk, Braud, Klin and Lasota (2012), Section 4.1, explicitly compute the transitive closure of an example equality-atom binary relation and present generic nominal computation of closures. Klin and Szynwelski (2016), Sections 1 and 7, provide formula-based symbolic transitive closure. These works explain how to compute closures in the nominal setting, but the inspected sections do not provide a universal point-to-point distance normal form or the min-plus rank-one formula for an arbitrary finite support. General decidability of transitive closure does not identify the exact shortest distances in closed form.

## Limitations
The theorem concerns **pure equality symmetry** and binary relations directly on the atoms; it does not cover richer ordered or random-graph atom symmetries, arbitrary orbit-finite state carriers, weighted distances, or regular-language-constrained paths. No historical-priority claim is made beyond the inspected sources, and the derivability of the cutoff alone from earlier orbit-lattice bounds is acknowledged. The mathematical argument and finite verification have not undergone independent specialist audit.

## References
1. G. Ciobanu, *Finite-Context Semantics in Finitely Supported Structures*, arXiv:2609.31917v1, first posted 25 September 2026, https://arxiv.org/abs/2609.31917. Relevant material: Sections 3, 8, 10.
2. M. Bojańczyk, L. Braud, B. Klin, S. Lasota, *Towards Nominal Computation*, POPL 2012, pp. 401–412, https://doi.org/10.1145/2103656.2103704. Author-accessible full text: https://www.cs.ox.ac.uk/people/bartek.klin/papers/popl12.pdf. Relevant material: Sections 3–4, 9.
3. B. Klin, M. Szynwelski, *SMT Solving for Functional Programming over Infinite Structures*, EPTCS 207 (2016), pp. 57–75, https://doi.org/10.4204/EPTCS.207.3, arXiv:1604.01185. Relevant material: Sections 1–2, 7.
