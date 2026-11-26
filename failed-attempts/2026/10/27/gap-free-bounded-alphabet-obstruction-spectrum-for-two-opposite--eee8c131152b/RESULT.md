# Gap-free bounded-alphabet obstruction spectrum for two opposite dependence atoms

## Finding

Fix finite nonempty, disjoint value sets \(X\) and \(Y\), of respective cardinalities \(a\) and \(b\). A team is an arbitrary subset \(T\subseteq X\times Y\), interpreted as assignments to variables \(x,y\). Use the standard *splitting* team-semantics disjunction
\[
\varphi:=\operatorname{dep}(x,y)\lor\operatorname{dep}(y,x).
\]
A team \(C\) is an *irreducible counterexample* when \(C\not\models\varphi\) but every proper subteam satisfies \(\varphi\). Let \(\mathcal S(a,b)\) be the set of their possible cardinalities and put \(s=\min\{a,b\}\).

**Theorem (complete obstruction-size spectrum).** If \(s=1\), or \(a=b=2\), every team satisfies \(\varphi\) and \(\mathcal S(a,b)=\varnothing\). In every other case, define
\[
H(a,b)=\begin{cases}
2s+1,&a=b,\\
2s+2,&a\ne b.
\end{cases}
\]
Then the attainable sizes are **all** the integers in the interval
\[
\boxed{\mathcal S(a,b)=\{6,7,\ldots,H(a,b)\}.}
\]
Consequently every counterexample \(T\) has a counterexample subteam of at most \(H(a,b)\) assignments, and the bound is best possible. There is a one-assignment difference between square and nonsquare alphabets, and no missing intermediate obstruction sizes.

This is an *at-most-size* detection theorem. It does **not** assert \(k\)-coherence in the convention where precisely \(k\)-element subteams, rather than all subteams of size at most \(k\), are tested.

## Assumptions and scope

The two variables are independently typed over finite nonempty alphabets \(X,Y\), whose copies are disjoint (or equivalently treated as tagged bipartite shores). Every pair in \(X\times Y\) may occur at most once, as assignments form a set, not a multiset. The formula uses ordinary functional-dependence atoms and their usual lax splitting disjunction: \(T\models\varphi\) means that \(T=T_1\cup T_2\) for subteams \(T_1,T_2\), with \(T_1\models\operatorname{dep}(x,y)\) and \(T_2\models\operatorname{dep}(y,x)\). One may make the split disjoint without changing the truth value because both atoms are downward closed. No other formula connectives or attributes are considered.

For \(a=b=1\), as well as for \(a=1\) or \(b=1\) in general, the failure spectrum is empty. For \(a=b=2\), it is empty despite both shores having more than one value. The first possible counterexample occurs at \((a,b)=(2,3)\) or its transpose and has six assignments.

## Proof

**1. Graph equivalence (known, included for completeness).** Associate to \(T\) the simple bipartite graph \(G_T\) with shores \(X,Y\) and one edge \(xy\) per assignment. A satisfying split orients each edge from \(x\) to \(y\) in the first part and from \(y\) to \(x\) in the second. The two functional dependencies say exactly that each vertex has at most one outgoing edge. In each connected component, such an orientation implies \(|E|\le |V|\). Conversely a connected component with at most as many edges as vertices is a tree or a unicyclic graph: orient a tree toward a root, or orient the unique cycle cyclically and all attached trees toward the cycle. Every vertex then has outdegree at most one. Thus
\[
T\models\varphi\quad\Longleftrightarrow\quad
\text{every connected component of }G_T\text{ has }|E|\le|V|.
\]
This correspondence is the established graph interpretation of the formula, as in Fröhlich--Kolaitis--Meier, Lemma 15; it is not claimed as new.

**2. Every irreducible failure is small and balanced.** The formula is downward closed, so irreducibility is equivalent to failure together with success after deleting any one edge. A minimal failing edge set has exactly one non-pseudoforest component; minimality makes the entire non-isolated graph connected. It has minimum degree at least two: deleting a leaf edge does not remove any cycle and leaves a failing component, contradicting minimality. Write its numbers of vertices on the two shores as \(\ell,r\) and its edges as \(e\). If \(e\ge\ell+r+2\), delete an edge from a cycle; this is a non-bridge, so the graph remains connected with at least \(\ell+r+1\) edges and still fails. Consequently
\[
e=\ell+r+1.
\]
As every vertex has degree at least two, \(e\ge2\ell\) and \(e\ge2r\); hence \(|\ell-r|\le1\). Since \(\ell\le a\) and \(r\le b\), we obtain \(e\le2s+1\) if \(a=b=s\), and \(e\le2s+2\) otherwise. A simple bipartite graph with \(e=|V|+1\) requires at least five non-isolated vertices: any graph on at most four with both shores nonempty is a subgraph of \(K_{2,2}\) or a star and has \(e\le|V|\). Thus \(e\ge6\). If \(s=1\), all bipartite graphs are forests; if \(a=b=2\), all are subgraphs of a four-cycle, so in these exceptional cases every team satisfies \(\varphi\).

**3. Even irreducible sizes.** For any integer \(t\ge2\), use \(t\) distinct left vertices and \(t+1\) distinct right vertices. Connect two chosen left vertices with three internally vertex-disjoint paths having lengths \(2\), \(2\), and \(2t-2\). These paths exist with disjoint internal vertices: each short path has one right internal vertex; the long path has \(t-1\) right and \(t-2\) left internal vertices. Their union is a theta graph with \(2t+2\) edges and \(2t+1\) vertices. It has two independent cycles, but deleting any edge turns it into a unicyclic graph. Therefore it is an irreducible failing team. The construction fits the prescribed alphabets whenever \(t\le s\) and the larger shore has at least \(t+1\) values. For \(a=b=s\), this permits \(t\le s-1\); for unequal sizes, \(t\le s\). Swapping the shores handles the opposite order.

**4. Odd irreducible sizes.** For each integer \(t\ge3\), form a Hamiltonian alternating cycle of length \(2t\) in the complete bipartite graph on \(t+t\) vertices and add a single cross-edge not already on the cycle. Explicitly, with left vertices \(u_0,\ldots,u_{t-1}\) and right vertices \(v_0,\ldots,v_{t-1}\), take edges \(u_iv_i\), \(u_{i+1\bmod t}v_i\) for every \(0\le i<t\), and the extra edge \(u_0v_1\). When \(t\ge3\) the latter is a genuinely new chord. The resulting theta graph has \(2t+1\) edges and is irreducible by the same deletion argument. It fits both alphabets exactly when \(t\le s\).

**5. Interval and sharpness.** For \(a=b=s\ge3\), the even constructions yield \(6,8,\ldots,2s\), and the odd constructions yield \(7,9,\ldots,2s+1\). For \(a\ne b\) with \(s\ge2\), the even constructions yield \(6,8,\ldots,2s+2\), and the odd constructions (when \(s\ge3\)) yield \(7,9,\ldots,2s+1\). These exhaust every integer from six to the upper bound, and the bounds in step 2 exclude all other sizes. Every failing team contains an inclusion-minimal failing subteam since it is finite; the size bound follows. The top-size theta witnesses make the bound sharp. \(\square\)

## Verification

The included standalone `checker.py` independently enumerates all subteams of the eight rectangles \((1,1)\), \((1,5)\), \((2,2)\), \((2,3)\), \((2,4)\), \((3,3)\), \((3,4)\), and \((4,4)\). It tests irreducibility by actual single-edge deletions, compares graph recognition directly against all splittings when there are at most nine potential assignments, and checks the odd/even explicit witness constructions for every \(2\le t\le40\) in their respective domains. Executing `python3 checker.py` prints `ALL_CHECKS_OK` and reports 71,636 tracked diagnostic checks. These are finite consistency tests, not the proof of the arbitrary-size result.

For illustration, the numbers of labelled irreducible subteams at sizes \(6,7,8,9\) in \(K_{4,4}\) are, respectively, \(48,288,432,816\). The theorem asserts the size spectrum, not a uniform formula for these multiplicities.

## Relationship to prior work

Fröhlich, Kolaitis and Meier prove the team-to-pseudoforest equivalence (their Lemma 15) and establish global incoherence of the formula (Theorem 25). Their explicit cyclic witnesses account for arbitrarily large odd minimal failures when both coordinates use the same number of values; these ingredients and the established bicircular-matroid interpretation are prior results. The present statement instead gives the **exact maximal support of a minimal failure under two fixed, possibly unequal alphabet sizes**, includes the exceptional trivial alphabets, and proves that **every** size between six and that maximum occurs. The complete sharp rectangular size spectrum is not contained in the identified statements of the main paper.

The recent work of Barlag and collaborators studies coherence and first-order rewritability in a wider logical setting, not this cardinality-parameterized binary-team spectrum. Bicircular-matroid work by Neudauer, Meyers and Stevens studies bases of complete bipartite graphs; the accessible abstract does not establish whether their full text treats circuit sizes. Putnam's dissertation studies bicircular circuit spectra generally, including consecutive lengths. It is a possible source of overlapping graph-theoretic ideas, but a derivation of the exact bipartite rectangle bounds has not been verified from its inaccessible full text.

## Limitations

The theorem is confined to **binary** teams and the specific disjunction of two opposite unary functional dependencies; it does not address arbitrary dependence formulas, infinite alphabets, multisets, or the count of irreducible witnesses of each size. The at-most-size property is different from the literature's exact-size definition of \(k\)-coherence. The graph equivalence and global incoherence are previously known. Priority cannot be claimed uniquely: older bicircular-matroid circuit-spectrum literature might already imply some or all of the exact rectangular bounds. The 2003 complete-bipartite bases article and Putnam's 2014 dissertation were inspected only through accessible abstracts, not their full texts.

## References

1. N. Fröhlich, P. G. Kolaitis, and A. Meier, *Disjunctions of Two Dependence Atoms*, arXiv:2508.16146v1 (first posted 2025-08-22), later CSL 2026, DOI:10.4230/LIPIcs.CSL.2026.10. See Lemma 15 and Appendix Theorem 25. https://drops.dagstuhl.de/storage/00lipics/lipics-vol363-csl2026/html/LIPIcs.CSL.2026.10/LIPIcs.CSL.2026.10.html
2. T. Barlag et al., *Aspects of Coherence in Dependence Logic*, arXiv:2605.31269v1 (2026-05-29). https://arxiv.org/abs/2605.31269
3. N. A. Neudauer, A. M. Meyers, and B. Stevens, *Enumeration of the Bases of the Bicircular Matroid on a Complete Bipartite Graph*, Ars Combinatoria 66 (2003), 165--178. https://combinatorialpress.com/ars-articles/volume-066-ars-articles/enumeration-of-the-bases-of-the-bicircular-matroid-on-a-complete-bipartite-graph/
4. B. C. Putnam, *The Characterization of Graphs with Small Bicycle Spectrum*, PhD dissertation, University of Mississippi (2014). https://egrove.olemiss.edu/etd/681/
