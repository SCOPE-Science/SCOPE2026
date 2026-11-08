# The nine-point counting-logic threshold for two commuting idempotent maps

## Finding

Let \(X\) be a nonempty finite set and let \(f,g:X\to X\) satisfy
\[
f\circ f=f,\qquad g\circ g=g,\qquad f\circ g=g\circ f.
\]
Write \(\mathcal A(f,g)=(X,F,G)\) for the **binary relational** structure with two named relations \(F(x,y)\) and \(G(x,y)\) holding exactly when \(f(x)=y\) and \(g(x)=y\), respectively. The language is relational; the operations are not function symbols in the logic.

**Theorem.** For every two such structures on at most eight points, equivalence in unrestricted two-variable first-order logic with counting quantifiers, \(C^2\), implies isomorphism. On exactly nine points there are \(6{,}752\) isomorphism types and exactly \(6{,}751\) \(C^2\)-equivalence classes: precisely one class contains two nonisomorphic types, and every other class is a singleton. Consequently the first possible failure of relative \(C^2\)-identification in this natural transformation variety occurs at nine points.

An explicit exceptional pair has common first map, on the set \(\{0,\ldots,8\}\),
\[
(f(0),\ldots,f(8))=(0,1,2,0,0,1,1,2,2),
\]
and second maps
\[
\begin{aligned}
(g_A(0),\ldots,g_A(8))&=(0,0,0,3,4,4,4,3,3),\\
(g_B(0),\ldots,g_B(8))&=(0,0,0,3,4,3,4,3,4).
\end{aligned}
\]
Both structures have the same four stable counting-color classes, of sizes \(1,2,2,4\), and hence are \(C^2\)-equivalent, but the structures are not isomorphic.

## Assumptions and scope

All carriers are finite and nonempty, \(f\) and \(g\) are **named**, and both maps are total, idempotent, and commute. Isomorphisms must preserve both map names. Equivalence is relative to this class of structures. This is not an assertion that each small structure is identified among *all* binary relational structures; nor does it apply to \(C^2\) in a signature containing genuine function symbols.

The logic has arbitrary counting thresholds and arbitrary quantifier depth but only two reusable variables. The exact census and first-failure theorem concern carriers of size at most nine; they make no claim about classification of all larger structures.

## Proof

### 1. A complete normal form

Let \(h=f\circ g=g\circ f\). Idempotence and commutation give \(h^2=h\), \(h\circ f=h\), and \(h\circ g=h\). The fixed points of \(h\) are exactly the points fixed by **both** maps. For a common fixed point \(c\), its fiber \(X_c=h^{-1}(c)\) is invariant under both operations, and every \(X\) is the disjoint union of these fibers.

Within \(X_c\), let \(U_c\) be the \(f\)-fixed points other than \(c\), and let \(V_c\) be the \(g\)-fixed points other than \(c\). These sets are disjoint: a point fixed by both is \(c\). Write their cardinalities as \(p\) and \(q\). Each \(u\in U_c\) satisfies \(f(u)=u\) and \(g(u)=c\), and each \(v\in V_c\) satisfies \(f(v)=c\) and \(g(v)=v\).

Every remaining point \(w\in W_c=X_c\setminus(\{c\}\cup U_c\cup V_c)\) has
\[
f(w)\in\{c\}\cup U_c,\qquad g(w)\in\{c\}\cup V_c.
\]
Choose labels \(u_1,\dots,u_p\), \(v_1,\dots,v_q\), and abbreviate \(u_0=v_0=c\). Define the nonnegative integer matrix \(A=(a_{ij})_{0\le i\le p,\,0\le j\le q}\) by
\[
a_{ij}=\bigl|\{w\in W_c:f(w)=u_i,\ g(w)=v_j\}\bigr|.
\]
Conversely, every \(p,q\ge0\) and every such matrix define a commuting pair of idempotents on \(1+p+q+\sum a_{ij}\) points, by assigning the maps exactly as above. The common fixed point is canonical; the nonzero-index rows and columns can be permuted independently, and points within a matrix cell can be permuted freely. **These are the only isomorphism freedoms.** Consequently one component is completely classified by \((p,q,A)\) modulo \(S_p\times S_q\), with row and column zero held fixed, and an arbitrary structure is classified by the **multiset** of its component types.

This proves the exhaustiveness and nonredundancy of the finite generator used below. In particular, no assumption of transitivity, connectivity beyond a fiber, or injectivity is hidden in the census.

### 2. A complete finite \(C^2\) invariant

In the two-relation language, the complete binary atomic type of ordered points \((x,y)\) is determined by the five truth values
\[
x=y,\ F(x,y),\ F(y,x),\ G(x,y),\ G(y,x).
\]
Start by coloring each point with its two diagonal truth values \((F(x,x),G(x,x))\). At every subsequent round, replace the color of \(x\) with its previous color together with the multiset, over **all** \(y\), of pairs consisting of the complete ordered binary atomic type of \((x,y)\) and the previous color of \(y\). Relabel these signatures canonically in a **shared palette** across all structures under comparison.

Standard counting-color refinement for binary relational structures states that two finite structures are \(C^2\)-equivalent if and only if their stabilized global color histograms agree [1, §2, §2.1]. The use of the entire atomic type is important: separately refining just the two plain directed graphs need not be complete for this language.

### 3. Exhaustive finite classification

The accompanying standalone verifier implements both preceding characterizations with exact integer arithmetic. For a given order \(n\), it loops over every \(p,q\ge0\) and \(e\ge0\) with \(1+p+q+e=n\), enumerates every weak composition of \(e\) into \((p+1)(q+1)\) cells, and chooses the lexicographically least representative under all independent permutations of the positive-index rows and columns. All multisets of these components with total order \(n\) are then enumerated. Each abstract representative is reconstructed into its two transition tables and checked for the defining identities.

The shared counting-color refinement runs simultaneously on the full list of isomorphism representatives at each order. Stable signatures are grouped without any heuristic graph-isomorphism test. The resulting exact counts are:

| Order | Isomorphism types | \(C^2\) classes | Non-singleton \(C^2\) classes |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 |
| 2 | 4 | 4 | 0 |
| 3 | 12 | 12 | 0 |
| 4 | 37 | 37 | 0 |
| 5 | 105 | 105 | 0 |
| 6 | 307 | 307 | 0 |
| 7 | 861 | 861 | 0 |
| 8 | 2,432 | 2,432 | 0 |
| 9 | 6,752 | 6,751 | 1, containing two types |

The verifier asserts this entire table, the uniqueness and precise matrices of the nine-point collision, and independent orbit-stabilizer counts of all labeled pairs of maps through nine points. A second program directly enumerates all labeled commuting idempotent pairs through six points and checks their counts; through five points it independently computes simultaneous-conjugacy orbits. All computations use finite exhaustive loops. Their source and captured outputs are included in the package.

The structural normal form proves that the enumerator omits no isomorphism types; the standard correspondence between full counting-color refinement and \(C^2\) proves that the signature classification is logically exact. Thus this finite computation proves the asserted sharp threshold, rather than merely testing random instances.

### 4. Direct nonisomorphism and logical indistinguishability at nine points

For the two explicit structures, the common fixed point is \(0\), the \(f\)-only fixed points are \(1,2\), the \(g\)-only fixed points are \(3,4\), and the remaining four points are \(5,6,7,8\). Their \(2\times2\) matrices of leaf multiplicities are
\[
A_+=\begin{pmatrix}0&2\\2&0\end{pmatrix},\qquad
A_\times=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]
The first matrix has doubled opposite edges; the second has one edge in every cell. No independent row and column permutations transform one into the other, proving nonisomorphism by the normal form (and the verifier also tests all \(9!\) bijections directly).

Both structures have the same four counting-color classes: common root \(\{0\}\), two \(f\)-only fixed points \(\{1,2\}\), two \(g\)-only fixed points \(\{3,4\}\), and four free points \(\{5,6,7,8\}\). Each \(f\)-only fixed point receives exactly two incoming \(F\)-arcs from free points, and each \(g\)-only fixed point receives exactly two incoming \(G\)-arcs from free points. Every free point has one named outgoing arc to each of the two types; all other atomic pair counts agree by color class. These four classes therefore constitute identical stable equitable partitions in the two structures. Their common color histogram is \((1,2,2,4)\); the \(C^2\) correspondence gives logical equivalence.

## Verification

Run `python3 verify.py` and `python3 check_labeled.py` using the Python standard library. `verify.py` enumerates all \(6{,}752\) nine-point types, computes the full counting signatures, checks labeled orbit sizes by factorial stabilizers, and verifies the exceptional transition tables by exhaustive bijections. `check_labeled.py` independently tests all labeled pairs of idempotents on at most six points. The included `verify_output.txt` and `brute_output.txt` contain the actual successful outputs, ending in `VERIFY_OK first_collision=9 unique_doubleton_at_9=1` and `BRUTE_OK`, respectively.

All integer counts, equality tests, and matrix canonicity conditions are exact. The underlying proof of exhaustion is mathematical and appears above; replaying the program verifies the finite remaining comparisons. There is no assertion that the tests provide an independent formal proof or establish historical publication priority.

## Relationship to prior work

Kiefer, Schweitzer, and Selman [1] formulate the connection between two-variable counting logic and color refinement for finite relational structures and give broad criteria for identification among unrestricted relational structures. Their classification is a source for the **logical equivalence criterion**, but their results do not state the relative nine-point threshold, the complete nine-point census, or the commuting-idempotent normal form. In particular, identification relative to the commuting-idempotent class is weaker than absolute identification, so the general absolute criterion alone does not supply this table.

Dolinka and East [2] study idempotents and transformation semigroups with a different objective (variants, regularity, rank, and generating sets), giving the transformation-semigroup motivation. Their study does not determine \(C^2\)-equivalence for pairs of commuting idempotent maps. The standard realization of a finite bipartite multigraph as matrix-cell multiplicities makes the source of logical ambiguity visible: incidence arrangements can differ even when every vertex and cell has the same local counting profile.

## Limitations

The exact enumeration covers only sizes through nine. The uniqueness statement is restricted to two **named** commuting idempotent maps in their **binary relational** graphs. It is not an assertion of uniqueness among arbitrary two-map systems, and it does not classify all larger counting-logic equivalence classes. The enumeration and proof have been checked within the supplied computational workflow, but no independent mathematical audit or external priority certification has been performed. Earlier equivalent results might appear under semilattice-action, two-retraction, or finite automaton terminology.

## References

[1] S. Kiefer, P. Schweitzer, and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792v1, first public 2015-03-30. In particular, §§2–3 and §5. https://arxiv.org/abs/1503.08792

[2] I. Dolinka and J. East, *Variants of finite full transformation semigroups*, arXiv:1410.5253, first public 2014-10-20; subsequently International Journal of Algebra and Computation 25 (2015), 1187–1222. https://arxiv.org/abs/1410.5253
