# Four exact recurrence populations for sequential hysteresis on double-star trees

## Finding

For integers \(a,b\ge1\), let \(D_{a,b}\) consist of two adjacent hubs \(u,v\), with \(a\) individually labelled pendant leaves adjacent to \(u\) and \(b\) individually labelled pendant leaves adjacent to \(v\). Apply the same closed-neighborhood binary bi-threshold rule at each vertex: a zero becomes one if the local sum is at least one; a one remains one if that sum is at least three. In each discrete step update \(u\), then \(v\), then all the leaves (in any order). Set
\[
T(m)=\sum_{k=2}^{m-2}\binom{m}{k}
=\begin{cases}0,&1\le m\le3,\\2^m-2m-2,&m\ge4.\end{cases}
\]
The **complete population of initially periodic labelled configurations**, grouped by *least temporal period*, is
\[
\boxed{R_1(a,b)=1,\quad R_2(a,b)=(2^a-2)(2^b-2),\quad
R_3(a,b)=3\mathbf 1_{a,b\ge2},\quad
R_6(a,b)=3\bigl(T(a)+T(b)\bigr).}
\]
No other least period occurs. Thus the numbers of distinct primitive temporal orbits at periods one, two, three and six are respectively \(1\), \(R_2/2\), \(R_3/3\) and \(R_6/6\). In particular, six-cycles occur **if and only if** \(\max(a,b)\ge4\), while three-cycles occur **if and only if** \(\min(a,b)\ge2\). The first six-cycles in the double-star family appear on seven vertices (the graph \(D_{1,4}\)).

The recurrent population has a sharp structural change: if \(\min(a,b)=1\), no primitive two-cycle exists, whereas for \(a,b\to\infty\) the fraction of recurrent configurations belonging to two-cycles tends to one, and the fraction belonging to six-cycles tends to zero. More precisely, for \(a,b\ge4\),
\[
\frac{R_6}{R_2}=\frac{3\bigl(2^a-2a-2+2^b-2b-2\bigr)}{(2^a-2)(2^b-2)}
=O(2^{-a}+2^{-b}).
\]

## Assumptions and scope

Vertices are labelled, not identified under automorphisms. An update uses the current value at its own vertex and at all its neighboring vertices, including any already updated hub within the same sweep. Every vertex updates exactly once per sweep. An *initially periodic* state is a complete state fixed by some positive iterate of this sweep; the theorem counts such states, not attraction-basin sizes or transients. All displayed equalities hold for every pair of integers \(a,b\ge1\). A leaf's up-threshold is one and its down-threshold is three even though its closed neighborhood has size two; consequently a leaf in state one always becomes zero on its update.

Write a configuration as \((h,j,A,B)\), where \(h,j\in\{0,1\}\) are the two hub bits and \(A\subseteq[a]\), \(B\subseteq[b]\) are the sets of active leaves. With \(H\), \(J\) the new hub bits, the full deterministic update is
\[
H=\begin{cases}\mathbf 1_{j+|A|\ge1},&h=0,\\\mathbf1_{1+j+|A|\ge3},&h=1,\end{cases}
\quad J=\begin{cases}\mathbf1_{H+|B|\ge1},&j=0,\\\mathbf1_{1+H+|B|\ge3},&j=1,\end{cases}
\]
followed by
\[
A'=\begin{cases}[a]\setminus A,&H=1,\\\varnothing,&H=0,\end{cases}
\qquad B'=\begin{cases}[b]\setminus B,&J=1,\\\varnothing,&J=0.\end{cases}
\]
These formulas, rather than an implementation-dependent convention, define the precise map under study.

## Proof

**Leaf synchronization dichotomy.** On a periodic trajectory, if the hub of an arm is always one, that arm's leaf set complements at every step. If its hub is zero at least once, all the leaves are zero at that step and subsequently remain synchronized (all zero or all one), including through return to that step. Therefore each recurrent trajectory has, for each arm, either a permanently active hub with a complementary leaf set, or a sometimes-inactive hub with a uniformly valued leaf set.

**Both hubs permanently one.** The complements of both leaf sets alternate. To preserve hub \(u\) at one in both parities, its leaf set must be neither empty nor full: the threshold is \(1+1+|A|\ge3\), hence both \(|A|\ge1\) and \(a-|A|\ge1\). The same applies at hub \(v\). Conversely every such pair of nonempty proper subsets gives a primitive two-cycle: both sets complement, then return. Their total number of states is \((2^a-2)(2^b-2)\). No fixed state occurs here.

**Only hub \(v\) permanently one.** The uniform leaf set at \(u\) has a forced three-step evolution
\[
(h,A)=(0,\varnothing)\longmapsto(1,[a])\longmapsto(1,\varnothing)\longmapsto(0,\varnothing),
\]
because \(j=1\) at each step and \(a\ge1\). Meanwhile \(B\) complements every step. The down-threshold of \(v\) requires \(|B|\ge2\) when the updated \(h\) is zero. As that zero recurs every third sweep while \(B\) alternates every sweep, this condition must hold for both \(B\) and \([b]\setminus B\): exactly \(2\le|B|\le b-2\). Conversely these inequalities ensure a genuine six-cycle (the hub has least period three, and the leaf subset has least period two). There are \(T(b)\) possible subsets \(B\), and three distinct phases of the \(u\)-hub clock for each chosen subset, so this family contains exactly \(3T(b)\) recurrent labelled states.

**Only hub \(u\) permanently one.** Symmetrically in the recurrent pattern but with the prescribed sequential hub order, the forced evolution at \(v\) is
\[
(j,B)=(0,\varnothing)\longmapsto(1,[b])\longmapsto(1,\varnothing)\longmapsto(0,\varnothing).
\]
Since \(u\) remains one even on phases with old \(j=0\), its leaf subset and complement must both contain at least two ones, i.e. \(2\le|A|\le a-2\). This yields precisely \(3T(a)\) further recurrent states of least period six. The two six-cycle families are disjoint because their permanently-one hubs differ.

**Neither hub permanently one.** Both leaf sets are uniform by the dichotomy. Represent them as \(A=u[a]\), \(B=v[b]\) for \(u,v\in\{0,1\}\). There are only sixteen states \((h,j,u,v)\). Their update depends on the sizes \(a,b\) only through the two predicates \(a\ge2\) and \(b\ge2\), because the hub threshold tests involve only sums \(0,1,2,3\) and the leaf sets are either empty or full. Exhausting all sixteen states in each of the four size regimes gives only the all-zero fixed configuration if either size is one; when both sizes are at least two there is in addition exactly one primitive three-cycle, represented by
\[
(0,1,\varnothing,\varnothing)\longmapsto(1,0,[a],\varnothing)
\longmapsto(1,1,\varnothing,[b])\longmapsto(0,1,\varnothing,\varnothing).
\]
For an explicit, independently reproducible finite table, `verification/profile_certificate.py` implements this exact sixteen-state test; its four observed least-period multisets are \(\{1\}\), \(\{1\}\), \(\{1\}\) and \(\{1,3\}\), respectively. The finite enumeration exhausts **all possible** uniform-branch cases for every \(a,b\), because there are only four threshold regimes; it is not an extrapolation from a bounded size search.

Combining the mutually exclusive cases proves all four formulas, their exactness, and the absence of every other period. The sharp existence cutoffs follow from the nonemptiness of the indicated binomial ranges. Taking ratios yields the final asymptotic statement.

## Verification

Two standalone programs accompany the proof. With Python 3.10 or newer, `python3 verification/profile_certificate.py` checks the complete recurrent profile decomposition, the four exact formulas and the four uniform cases, for 1,600 size pairs \(1\le a,b\le40\). Using a C++17 compiler, compile `verification/independent_exhaustive.cpp` with `g++ -std=c++17 -O2` and run the executable. It independently builds each labelled full-state functional graph, removes all transient vertices by indegree elimination, and follows each remaining temporal cycle. All 75 tested pairs with \(1\le a,b\le9\) and \(a+b+2\le17\) agree with the formulas. Exact program outputs are included as `verification/profile_output.txt` and `verification/independent_output.txt`.

These bounded computations are cross-checks. The unbounded theorem is supported by the synchronization dichotomy and the complete 16-state symbolic case reduction in the preceding proof.

## Relationship to prior work

Kuhlman, Mortveit, Murrugarra and Kumar established the bifurcation in sequential bi-threshold dynamics and gave explicit longer cycles on selected tree families, including the five-vertex X-tree's two-cycle. Their paper does not furnish an exact all-size primitive-orbit census for double stars. A published exact enumeration of maximal attainable periods over **all** trees of orders at most fourteen gives a complementary bounded-size extremal result; its statement neither entails nor states the present all-size double-star counts. Work on cycle equivalence of sequential graph dynamical systems also explains why the chosen scan order is a natural representative on a tree, although only this explicit scan order is used in the proof here.

## Limitations

The theorem concerns one specified sequential update scheme, not synchronous updating, heterogeneous thresholds, general trees, transient times, attraction basins or stochastic schedules. A broader cycle-equivalence theorem exists, but no arbitrary-order extension is needed for the stated census. The mathematical proof applies for unbounded arm sizes; the finite programs are additional cross-checks, not substitutes for its classification argument. Exhaustive historical-priority verification is not possible: unpublished or unindexed enumerations and portions of computational literature may contain an equivalent classification.

## References

1. C. J. Kuhlman, H. S. Mortveit, D. Murrugarra, V. S. Anil Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974v1 (first publicly posted 2011-08-15), https://arxiv.org/abs/1108.2974.
2. M. Macauley and H. S. Mortveit, *Cycle Equivalence of Graph Dynamical Systems*, arXiv:0802.4412v1 (first publicly posted 2008-02-29), https://arxiv.org/abs/0802.4412.
3. *Sharp primitive-period maxima through fourteen vertices for sequential bi-threshold dynamics on trees*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-primitive-period-maxima-through-fourteen-vertices-for-sequ--9e5a9ef7f73d.
