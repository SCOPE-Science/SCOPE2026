# Four low-width theories and necklace invariants for cyclic independent-fiber digraphs

## Finding
For each integer \(L\ge3\) and positive integers \(a_0,\ldots,a_{L-1}\), let \(B(L;\mathbf a)\) be the finite loopless digraph obtained from the consistently oriented cycle on \(\mathbb Z/L\mathbb Z\) by replacing vertex \(i\) by an independent nonempty fiber \(A_i\) of size \(a_i\). There is an arc \(x\to y\) exactly when \(x\in A_i\), \(y\in A_{i+1}\) (indices modulo \(L\)). The signature is a single binary directed-arc relation and equality, with no constants, counting quantifiers, or additional predicates.

The complete counting-free finite-variable first-order equivalence classification at **unrestricted quantifier depth** is as follows.

* Every two digraphs in this family are \(\mathrm{FO}^{1}\)-equivalent.
* At width two there are exactly four theories. Write \(s(B)=|\{i:a_i=1\}|\) if \(L=3\), and \(s(B)=0\) if \(L\ge4\). Then \(B\equiv_{\mathrm{FO}^{2}}B'\) exactly when \(s(B)=s(B')\). The possible values are \(0,1,2,3\). The \(s=0\) class includes all lengths \(L\ge4\) and all triangle blow-ups in which every fiber has size at least two.
* For every \(k\ge3\), two such digraphs are \(\mathrm{FO}^{k}\)-equivalent if and only if their cycle lengths coincide and their cyclic words \((\min(a_i,k))_{i\in\mathbb Z/L\mathbb Z}\) agree up to **rotation** (not reversal).

For each fixed \(L\ge3\) and \(k\ge3\), the exact number of width-\(k\) theories is the necklace number
\[
N_{L,k}=\frac1L\sum_{d\mid L}\varphi(d)k^{L/d}.
\]
Every width-\(k\) theory in this fixed-length class has a unique smallest representative up to digraph isomorphism, obtained by clipping every fiber size at \(k\). More precisely, if \(f_{L,k}(n)\) counts these theories whose smallest representative has exactly \(n\) vertices, then the complete generating polynomial is
\[
\sum_n f_{L,k}(n)z^n=\frac1L\sum_{d\mid L}\varphi(d)\bigl(z^d+z^{2d}+\cdots+z^{kd}\bigr)^{L/d}.
\]
The counting-free variable-width hierarchy is strict on this family at every transition: from one to two, from two to three, and from \(k\) to \(k+1\) for each \(k\ge3\).

## Assumptions and scope
All fibers are nonempty and independent, and arcs between successive fibers are complete in the forward direction only. No other arcs or loops are allowed, including arcs within a fiber. The cyclic length \(L\) can be any integer at least three, and fiber sizes are arbitrary positive integers. Logical equivalence concerns all sentences using at most \(k\) reusable variable names, without a bound on quantifier rank. The above classification and minimum representatives are relative to this explicitly defined infinite family; no global graph-identification claim is made.

## Proof
**1. Structural uniqueness of fibers.** For vertices \(x,y\), consider the three-variable formula
\[
\operatorname{Twin}(x,y):=\forall z\bigl(E(x,z)\leftrightarrow E(y,z)\bigr).
\]
The out-neighborhood of a vertex of \(A_i\) is exactly the nonempty set \(A_{i+1}\). Distinct fibers have disjoint nonempty out-neighborhoods. Hence \(\operatorname{Twin}(x,y)\) holds exactly when \(x,y\) lie in the same fiber. The quotient of the digraph by this definable equivalence relation is the oriented simple cycle of length \(L\). Every graph isomorphism therefore rotates the fibers, without reflecting their cyclic order.

**2. Counting the size of one fiber with \(k\) variables.** Fix \(k\ge3\). For every integer \(1\le j\le k\), there is a formula \(C_j(x)\) using at most \(k\) variable names, with only \(x\) free, asserting that at least \(j\) distinct vertices lie in the \(\operatorname{Twin}\)-class of \(x\). Explicitly, \(C_1(x)\) is \(x=x\); for \(j\ge2\), select \(j-1\) distinct witnesses in the class of \(x\), requiring pairwise inequality and \(\operatorname{Twin}\) between each witness and \(x\). Each expanded \(\operatorname{Twin}\) test needs one locally bound third variable, which may reuse a witness's variable name outside the test's scope. Thus no extra globally free variable is required. At truncated value \(t<k\) use \(C_t(x)\wedge\neg C_{t+1}(x)\); at value \(k\) use \(C_k(x)\). Denote these unary tests by \(Q_t(x)\).

**3. Recovering cyclic length and ordered size pattern.** For every positive integer \(m\ge3\), a three-variable sentence \(W_m\) asserts the existence of a directed closed walk of precisely \(m\) arcs. Keep a starting vertex in one variable and alternate the other two variable names along the walk; when a name is reused, the former value is no longer needed. For example, at length three this is \(\exists x\exists y\exists z(E(x,y)\wedge E(y,z)\wedge E(z,x))\). Every arc increments the fiber index by one, so \(W_m\) holds in \(B(L;\mathbf a)\) exactly when \(L\mid m\). In particular the least positive directed closed-walk length is \(L\), and graphs of different cyclic lengths are separated already by \(\mathrm{FO}^{3}\).

For any \(L\)-word \(\mathbf t=(t_0,\ldots,t_{L-1})\) over \(\{1,\ldots,k\}\), strengthen the closed-walk formula for \(W_L\) by conjoining the unary test \(Q_{t_i}\) at each \(i\)-th visited vertex. This still uses at most \(k\) variable names: each local unary test uses only its current vertex freely and may shadow any other names **within its own subformula**; the starting anchor and next-path variables recover their meanings outside that local scope. Because an \(L\)-step closed walk visits precisely one vertex in each successive fiber, this sentence holds exactly when \(\mathbf t\) is a cyclic rotation of \((\min(a_i,k))\). This proves the necessity of the high-width invariant.

**4. Permanent pebble strategy.** Conversely, suppose two length-\(L\) digraphs have matching clipped words after a fixed rotation. Pair their fibers by that rotation and maintain that all occupied vertices in corresponding fibers are related by a partial bijection. A move of one of the \(k\) pebbles removes its old pair, leaving at most \(k-1\) occupied vertices in any fiber. If the chosen vertex is already occupied by another pebble, choose its partner; otherwise choose a new vertex of the corresponding fiber. This is possible because either the two fiber sizes agree below \(k\), or both are at least \(k\). The preserved partial map is always a partial isomorphism, since arcs depend only on successive fiber indices. The response works in either direction and indefinitely. The permanent-game characterization of counting-free \(\mathrm{FO}^{k}\) gives sufficiency.

**5. The exceptional two-variable collapse.** Let
\[
P(x):=\forall y\bigl(y=x\ \lor\ E(x,y)\ \lor\ E(y,x)\bigr).
\]
A vertex satisfies \(P\) exactly when it is adjacent in some direction to every different vertex. In a triangle blow-up (\(L=3\)), these are exactly the vertices in singleton fibers: all other fibers are adjacent to its fiber, and a nonsingleton fiber supplies a nonadjacent distinct vertex. When \(L\ge4\), every vertex has a nonadjacent vertex in \(A_{i+2}\); hence \(P\) is empty.

The sentences \(\exists xP(x)\), \(\exists x\exists y(x\ne y\wedge P(x)\wedge P(y))\), and \(\forall xP(x)\) distinguish the four values of \(s\), using only two variable names (locally binding a name inside one occurrence of \(P\) does not alter the scope of another occurrence). If \(s>0\) agrees in two graphs, they are both triangle blow-ups whose singleton/non-singleton patterns agree up to rotation. Keep the block correspondence and a partial injection with only two pebbles; singleton sizes agree exactly, while every nonsingleton fiber has at least two available vertices. This is an indefinite winning strategy.

If \(s=0\), every vertex has an incoming neighbor, an outgoing neighbor, and a distinct nonneighbor. In a two-pebble game, after lifting one pebble there is at most one stationary vertex; Duplicator can therefore choose a vertex equal to it, pointing to it, pointed to by it, or nonadjacent to it, exactly as Spoiler does. These four atomic cases are available in both graphs and are mutually exclusive. The strategy preserves every atomic relation indefinitely, even when the cycle lengths differ. With one variable only \(E(x,x)\) and equality can be tested, and all these graphs are nonempty and loopless. This completes the low-width classification.

**6. Enumeration and strictness.** For \(k\ge3\), width-\(k\) theories of fixed length \(L\) correspond bijectively to cyclic orbits of words of length \(L\) over \(k\) colors. Burnside's lemma counts words fixed by a rotation of order \(d\), giving \(k^{L/d}\) choices for its \(L/d\) cycles, and there are \(\varphi(d)\) such rotations. Weighting each color \(t\) by \(z^t\), the fixed-point contribution becomes \((z^d+\cdots+z^{kd})^{L/d}\). This proves both displayed formulas and the unique minimum representatives.

Width one is separated from width two by the directed triangle and the directed four-cycle. Width two is separated from width three by the directed four-cycle and the triangle blow-up with all fibers of size two: both have \(s=0\), but their quotient lengths differ. For every \(k\ge3\), the triangle blow-ups with fiber sizes \((k,1,1)\) and \((k+1,1,1)\) agree at width \(k\) but not at width \(k+1\).

## Verification
`verification/check_pebble.py` independently builds cyclic blow-ups and computes the stable partition of all \(k\)-tuples under repeated one-coordinate replacement by **sets** of attainable colors, not multisets. This fixed-point procedure directly represents finite counting-free \(k\)-variable logical types. It compares the resulting theory palettes with the claimed invariants, including the exceptional two-variable cases. Its recorded run checked 703 width-two pairs, 510 width-three pairs, 190 width-four pairs, and a three-versus-four fiber-size threshold example, without discrepancy.

`verification/check_necklaces.py` independently constructs the digraphs and checks the three-variable out-neighborhood predicate against actual fiber membership, closed-walk divisibility, Burnside's necklace counts, and the coefficients of the minimum-order generating polynomial. The recorded run checked 765 constructed digraphs, 78,070 ordered vertex pairs, 8,250 closed-walk lengths, and 20 necklace-parameter pairs, without discrepancy. A third program, `verification/check_formulas.py`, directly evaluates the recursively scoped formula syntax on small digraphs, checking 90 decorated closed-walk formulas and 308 local unary size tests against their intended semantics, including variable-name shadowing. All three programs use only Python 3 and its standard library. Reproduce with `python verification/check_pebble.py`, `python verification/check_necklaces.py`, and `python verification/check_formulas.py`, comparing with the three recorded output text files. The third program imports `check_necklaces.py` from the same `verification/` directory. Finite tests corroborate the all-parameter proof but are not substitutes for it.

## Relationship to prior work
Grohe and Schweikardt (arXiv:cs/0502047, first publicly posted 2005-02-09) analyze finite-variable logic on linear orders, chiefly formula succinctness, not this directed-graph family. Dawar and Holm (arXiv:1205.0913, first posted 2012-05-04) develop general games for finite-variable logics and explicitly describe the standard \(k\)-pebble characterization used in the proof, but do not supply this class's four width-two theories, its definable cyclic-fiber reconstruction, or the resulting necklace spectrum. Hatami, Hirst, and Norine (arXiv:1108.5699, 2011-08-29) study independent-fiber blow-ups for undirected induced-density extremal problems, not their finite-variable theories.

The later research result *Forward-shift blow-ups preserve digraph homotopy type* studies **exactly the same complete blow-up construction on directed cycles**, but proves homotopy equivalence and a path-homology calculation rather than logical equivalence; it does not imply the above theory distinctions or theory counts. Another related classification treats cyclic digraphs with incoming pendant leaves, where only core vertices are cyclic and the attached leaves are terminal; its high-width necklace pattern is similar, but the present family has no distinguished sparse core, and its exceptional two-variable classification is different. Neither result establishes the claim here by direct logical implication. A general unpublished or uninspected substitution theorem remains a possible stronger source and a historical-priority risk.

## Limitations
No counting quantifiers, unary colors, constants, nonempty intra-fiber arcs, reverse arcs, bidirected base cycles, or disconnected unions are included. The total number of theories across **all** allowed cycle lengths is infinite for every width at least three; the finite Burnside count is for a fixed length. Minimality and defining-width statements are relative to the stated family. The proof does not determine optimal formula length or quantifier rank for separating two inequivalent graphs. Primary-paper and research-record comparisons are bounded.

## References
1. M. Grohe and N. Schweikardt, *The succinctness of first-order logic on linear orders*, arXiv:cs/0502047, first posted 2005-02-09; *Logical Methods in Computer Science* **1** (2005), Article 6. https://arxiv.org/abs/cs/0502047.
2. H. Hatami, J. Hirst, and S. Norine, *The inducibility of blow-up graphs*, arXiv:1108.5699, first posted 2011-08-29. https://arxiv.org/abs/1108.5699.
3. A. Dawar and B. Holm, *Pebble games with algebraic rules*, arXiv:1205.0913, first posted 2012-05-04. https://arxiv.org/abs/1205.0913.
4. *Forward-shift blow-ups preserve digraph homotopy type*, openly accessible scientific result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-forward-shift-blow-ups-preserve-digraph-homotopy-type--1f84401a7952/RESULT.md.
