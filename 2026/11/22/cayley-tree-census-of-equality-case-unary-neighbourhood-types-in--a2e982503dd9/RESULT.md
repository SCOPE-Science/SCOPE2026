# Cayley-tree census of equality-case unary neighbourhood types in finite forests

## Finding
Let \(q\geq1\), \(m=3q\), and let \(A=[m]\) be a fixed, pointwise-named parameter set. For a finite undirected simple forest \(F\) containing \(A\), write
\[
\mathcal T(F,A)=\{\,N_F[v]\cap A:v\in V(F)\,\},\qquad N_F[v]=\{v\}\cup\{u:uv\in E(F)\}.
\]
These are exactly the truth-value vectors of the \(m\) one-variable first-order formulas \(x=a\lor E(x,a)\), evaluated at all vertices. Call \(\mathcal T(F,A)\) *saturated* when it has \(7q\) members. The sharp numerical upper bound \(7q\) itself was proved by Berthe, Foucaud, Lehtilä and Parreau (2026); it is **not** claimed here.

**Classification.** A family of subsets of \(A\) is saturated and realizable in a finite forest if and only if it consists of:

1. the empty set and all \(m\) singletons;
2. for each block of an unordered partition of \(A\) into \(q\) triples \(B\), the triple \(B\) and the two pairs \(\{c_B,u\}\) for \(u\in B\setminus\{c_B\}\), where a centre \(c_B\in B\) is specified;
3. for each edge \(BB'\) of an undirected tree on the \(q\) blocks, one pair \(\{u_{BB'},u_{B'B}\}\) with \(u_{BB'}\in B\) and \(u_{B'B}\in B'\).

When \(q=1\), the block tree has no edges. The data above are uniquely reconstructible from the family.

**Exact census.** The number \(C_q\) of *distinct saturated families of subsets of the labelled set \(A\)* is
\[
\boxed{C_q=\frac{(3q)!}{2^q q!}\;9^{q-1}\;q^{q-2}},
\]
with the standard one-vertex-tree convention \(q^{q-2}=1\) for \(q=1\). Thus \(C_1=3\), \(C_2=810\), and \(C_3=1\,837\,080\). Every family has a realizing tree on exactly \(7q\) vertices, and no realizing graph can have fewer vertices. This does **not** enumerate the possible ambient tree isomorphism types.

## Assumptions and scope
All graphs are finite, loopless, simple, undirected forests. The \(3q\) parameters are distinct vertices and their individual names are held fixed when counting families; ambient nonparameter vertices are unnamed. A *family* means an ordinary set of subsets: repeated traces of different vertices are merged. Only closed radius-one neighbourhoods are used, and each formula \(x=a\lor E(x,a)\) is evaluated even when \(x\) is itself one of the parameters. Equality in the theorem is for parameter counts divisible by three, the residue class at which the known sharp bound has no rounding slack. No claim is made about equality-family counts at the other two residues.

## Proof
Let \(A\) be any \(m\)-vertex set in a forest \(F\). Split the connected components of \(F[A]\) into \(a\) singletons, \(b\) two-vertex components and \(c\) components of size at least three; thus \(a+2b+3c\le m\). There are \(k=a+b+c\) marked components. The distinct traces of cardinality one contribute at most \(m\), and the empty trace contributes at most one.

A marked vertex in a singleton component supplies only a singleton trace. Both vertices of a two-vertex component supply the same two-element trace. Vertices of larger marked components supply at most their number of distinct nonsingleton traces. Consequently there are at most \(m-a-b\) distinct nonsingleton traces whose realizing vertex lies in \(A\).

Let \(H\) be the set of vertices outside \(A\) having at least two neighbours in \(A\), and put \(h=|H|\). Such a vertex cannot meet two marked vertices in the same component of \(F[A]\), since that would create a cycle. Contract each marked component and retain the incidences with vertices of \(H\). The resulting bipartite graph is a forest on \(k+h\) vertices, with at least \(2h\) edges. Hence \(2h\le k+h-1\) and \(h\le k-1\). Every nonsingleton trace realized outside \(A\) comes from one of these \(h\) vertices. We obtain
\[
|\mathcal T(F,A)|\le m+1+(m-a-b)+h
\le 2m+c\le 2m+\lfloor m/3\rfloor.
\]
This reproduces only the known numerical inequality, in a form that exposes its equality conditions.

Now let \(m=3q\) and suppose equality \(|\mathcal T(F,A)|=7q\) holds. Each displayed inequality must be an equality, so \(c=q\), \(a=b=0\), every marked component has exactly three vertices, and \(h=k-1=q-1\). Every three-vertex tree is a path; call its middle vertex its centre. Its three marked-vertex traces are precisely its full triple and the two centre–leaf pairs. Equality also forces the empty trace and every marked singleton to be realized.

The contracted bipartite incidence forest on the \(q\) marked triples and \(q-1\) high-degree outside vertices has \(2q-1\) vertices and at least \(2(q-1)\) edges. Since it is acyclic, it has at most \(2q-2\) edges. Thus it is a connected tree and each outside high-degree vertex has exactly two marked neighbours, belonging to two different triples. Suppressing these degree-two vertices produces an ordinary tree on the triple blocks, with a chosen attaching vertex at each endpoint of each block-tree edge. The trace family must therefore have exactly the stated form.

Conversely, take any listed partition, centres, tree and attachment choices. Within each block add the two centre–leaf edges. For every block-tree edge add a fresh unmarked vertex adjacent to its chosen two marked endpoints. Add one private fresh leaf at every marked vertex. Finally, attach a fresh vertex to one private leaf, creating a vertex with empty marked trace. Contracting block paths shows the resulting graph is connected and acyclic; it has \(3q+3q+(q-1)+1=7q\) vertices. Its marked-vertex traces are the stated triples and internal pairs, the block-edge vertices realize the cross-block pairs, the private leaves realize all singletons, and the final vertex realizes the empty set. All \(7q\) traces are distinct.

For counting, the triple partition has \((3q)!/(6^q q!)\) choices; the centres have \(3^q\) choices; the block tree has \(q^{q-2}\) choices (one for \(q=1\)); each of its \(q-1\) edges has \(3\cdot3=9\) attachment choices. Multiplication gives the asserted formula. No overcount is possible: the only three-element members of the trace family recover the blocks; the within-block two-element members recover their centres; the remaining two-element members recover the tree edges together with both attachment labels. Finally, at least \(7q\) host vertices are needed to realize \(7q\) distinct traces, and the construction reaches that lower bound.

## Verification
Execute `python3 check.py` using Python 3.9 or later. The standalone standard-library checker exhausts every labelled simple forest on at most six vertices and all nonempty parameter subsets for the general upper bound. It also constructs and verifies every prescribed extremal trace family for \(q=1\) and \(q=2\), checking that all families are different, that the realizing graph is a tree with the predicted size, and that every claimed trace is realized. It tests representative \(q=3\) tree constructions and prints the factorial/Cayley prediction for that case. The observed summary was:

```
FORESTS_TO_6 {1: 1, 2: 2, 3: 7, 4: 38, 5: 291, 6: 2932}
CENSUS (1, 3, 3)
CENSUS (2, 6, 810)
Q3_PREDICTED 1837080
ALL_CHECKS_OK
```

These finite computations are corroboration only; the preceding argument establishes the full claim for every \(q\ge1\).

## Relationship to prior work
Berthe, Foucaud, Lehtilä and Parreau (2026, Theorem 2 and Section 3) proved the optimal closed-neighbourhood bound \(\lfloor7m/3\rfloor\) for all finite forests and gave a construction using three-vertex path blocks and an arbitrary tree connecting blocks. Their bound, proof method and construction are explicitly treated as prior. The present result takes the exact equality conditions at the zero-slack multiples of three, proves a *necessary-and-sufficient* classification of all **labelled trace families**, and derives their all-size factorial/Cayley census. The cited paper does not state or count these families in its inspected Section 3. Bertrand, Charon, Hudry and Lobstein (2005) proved the precursor identifying-code inequality for trees and gave extremal constructions, but their inspected Section 2 does not classify all parameter-labelled saturated trace families. Beaudou, Bok, Foucaud, Quiroz and Raymond (2025) treat general neighbourhood/profile-complexity bounds for structured graphs, rather than this equality-family count. A semantic search of published mathematical findings was also conducted for the exact profile, its equivalent one-variable Boolean-type formulation, and potential stronger enumerative claims; none among the examined results was found to imply this enumeration. This is a best-knowledge originality conclusion, not an assertion of exhaustive historical priority.

## Limitations
The numerical upper bound and existence of extremizers are already known. The new contribution is the rigidity and exhaustive labelled-family enumeration in the natural zero-slack congruence class. The theorem does not classify ambient realizing forests up to isomorphism, does not enumerate the other congruence classes, and does not provide independent validation or a blanket priority certificate. The proof is self-contained after ordinary graph terminology and the elementary Prüfer/Cayley tree count.

## References
1. Gaétan Berthe, Florent Foucaud, Tuomo Lehtilä, Aline Parreau, *Neighbourhood complexity and identification problems for graphs of bounded treewidth and pathwidth*, arXiv:2607.16889v1 (first public July 18, 2026), especially Theorem 2 and Section 3. https://arxiv.org/html/2607.16889v1
2. Laurent Beaudou, Jan Bok, Florent Foucaud, Daniel A. Quiroz, Jean-Florent Raymond, *Profile and neighbourhood complexity of graphs with excluded minors and tree-structured graphs*, arXiv:2501.08895v1 (first public January 15, 2025), background. https://arxiv.org/html/2501.08895v1
3. Nathalie Bertrand, Irène Charon, Olivier Hudry and Antoine Lobstein, *1-identifying codes on trees*, Australasian Journal of Combinatorics 31 (2005), 21–35, Theorems 1–2. https://scispace.com/pdf/1-identifying-codes-on-trees-4rw8mu31ee.pdf
4. A. Cayley, *A theorem on trees*, Quarterly Journal of Pure and Applied Mathematics 23 (1889), 376–378 (classical labelled-tree count).
