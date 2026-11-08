# Two named terminals rigidify two-variable logic on theta networks

## Finding

Let \(\mathcal T\) be the family of finite undirected simple graphs formed from three internally vertex-disjoint paths between distinct terminals \(s,t\), each having at least two edges. Denote the graph with path lengths \(\ell_1,\ell_2,\ell_3\ge2\) by \(\Theta(\ell_1,\ell_2,\ell_3)\). In the vocabulary consisting of adjacency, equality, and two constants naming the terminals, the following equivalence holds for every two members of \(\mathcal T\):

\[
(\Theta(\ell_1,\ell_2,\ell_3),s,t)\equiv_{\mathrm{FO}^{2}}
(\Theta(m_1,m_2,m_3),s',t')
\quad\Longleftrightarrow\quad
\{\!\{\ell_1,\ell_2,\ell_3\}\!\}=\{\!\{m_1,m_2,m_3\}\!\}.
\]

Here \(\mathrm{FO}^{2}\) is counting-free first-order logic using only two reusable variable symbols and no quantifier-depth bound. In contrast, after forgetting the constants, **all graphs in \(\mathcal T\) have the same \(\mathrm{FO}^{2}\) theory**, regardless of size or path lengths. Thus naming the two naturally distinguished terminals changes one infinite theory into complete isomorphism separation within the family.

For a fixed number \(N\ge6\) of edges, the number of distinct two-variable theories in the named-terminal vocabulary is

\[
\#\mathrm{Th}^{2}_{N}(\mathcal T)
=p_{\le3}(N-6)=\left\lfloor\frac{N^2-6N+12}{12}\right\rfloor,
\]

where \(p_{\le3}(n)\) counts partitions of \(n\) into at most three nonnegative parts. In the unnamed vocabulary there is one two-variable theory across the entire family. Two variables are necessary for the named-terminal rigidity: the structures with three length-four paths and three length-five paths have the same one-variable theory.

## Assumptions and scope

The language has one symmetric irreflexive binary adjacency relation \(E\). In the expanded language, \(c_s,c_t\) are distinct constant symbols interpreted by the two vertices of degree three. The other vertices have degree two. Every path length is an integer at least two, so there is no terminal edge and the terminal distance \(a=d(s,t)=\min_i\ell_i\) is at least two. All equivalences are **relative to this family** and concern sentences with unrestricted finite quantifier depth; no counting quantifiers, order, or other predicates are used. Path lengths are edge counts, not internal-vertex counts.

The multiset comparison treats permutations of the three paths as identical. Both rooted and unrooted graph isomorphism have this multiset invariant, but the logical languages and their discriminating power differ sharply.

## Proof

**1. Distances from named terminals require only two variables.** For either fixed constant \(c\in\{c_s,c_t\}\), the unary predicate \(d(c,x)\le r\) is definable by formulas using only two variable symbols. Start with \(R^c_0(x):=(x=c)\); inductively set

\[
R^c_{r+1}(x):=R^c_r(x)\lor\exists y\bigl(E(x,y)\land R^c_r(y)\bigr).
\]

In the occurrence \(R^c_r(y)\), alternate the names \(x,y\) when expanding the recursion, binding the unused name inside its local scope. The result has only one free variable and uses no third variable symbol. Thus exact distance \(d(c,x)=r\) is expressible as \(R^c_r(x)\land\neg R^c_{r-1}(x)\) for \(r\ge1\), or \(x=c\) for \(r=0\).

**2. A strict distance-difference lemma.** Fix a path of length \(L'\) and its vertex \(v_i\) at position \(i\) from \(s\), where \(0\le i\le L'\). All routes from \(v_i\) to a terminal either follow its own path or go first to the other terminal and then use a shortest terminal route of length \(a\). Hence

\[
d(s,v_i)=\min(i,L'-i+a),\qquad
d(t,v_i)=\min(L'-i,i+a).
\]

If either minimum uses a detour through the opposite terminal (including a tie), the two terminal distances differ by exactly \(a\) in absolute value. Consequently,

\[
|d(s,v_i)-d(t,v_i)|<a
\quad\Longrightarrow\quad
 d(s,v_i)+d(t,v_i)=L'
\]

and both distances equal their direct-path values \(i,L'-i\). This implication is the critical reconstruction step: distance pairs with strict terminal-distance slack identify the length of the path containing the vertex.

**3. Exactly one midpoint witness per path.** For each integer \(L\ge2\), put \(p=\lfloor L/2\rfloor\) and \(q=\lceil L/2\rceil\). Let \(M_L(x)\) express the conjunction \(d(s,x)=p\) and \(d(t,x)=q\). It is an \(\mathrm{FO}^{2}\) formula by step 1. Because \(|p-q|\le1<a\), step 2 proves that a vertex satisfying \(M_L\) must lie on a path of length exactly \(L\), at position \(p\). Conversely, every path of length \(L\) has exactly one such vertex. Thus the finite set defined by \(M_L\) has size equal to the number \(m_L\) of length-\(L\) paths.

The two-variable sentences \(\exists x\,M_L(x)\) and

\[
\exists x\exists y\,\bigl(x\ne y\land M_L(x)\land M_L(y)\bigr)
\]

recognize \(m_L\ge1\) and \(m_L\ge2\), respectively. There is no variable capture: the internal distance tests in \(M_L(x)\) may rebind \(y\) only inside that conjunct, and the tests in \(M_L(y)\) may likewise rebind \(x\). Since exactly three paths exist, knowledge of all these two thresholds determines every \(m_L\). Indeed, whenever a multiplicity is three it is the only positive one; otherwise all multiplicities are at most two. Therefore distinct path-length multisets are distinguishable by a sentence of \(\mathrm{FO}^{2}\). Equal multisets yield an isomorphism preserving both terminal constants, proving the stated equivalence.

**4. Forgetting the constants erases all differences.** Every graph in \(\mathcal T\) has at least five vertices; each vertex has degree two or three and has both a distinct neighbor and a distinct nonneighbor. Duplicator wins the unrestricted two-pebble game between any two such graphs. When one pebble is retained, the other can always be answered by the same vertex, by a neighbor, or by a distinct nonneighbor, as dictated by equality and adjacency to the retained vertex. These options exist on both sides indefinitely. If no pebble is retained, answer arbitrarily. At every round the correspondence is a partial isomorphism. The two-pebble characterization of \(\mathrm{FO}^{2}\) now gives the single unnamed theory.

**5. Counting theories at fixed size.** Writing \(\ell_i=2+a_i\) gives nonnegative integers with \(a_1+a_2+a_3=N-6\). Unordered triples correspond exactly to partitions into at most three parts. The classical three-part partition enumeration gives the displayed floor formula; it can also be verified by summing, for \(0\le a\le b\le c\), the equation \(a+b+c=N-6\). Each tuple is a different named-terminal theory by step 3.

**6. One variable does not suffice.** For the two named-terminal structures \(\Theta(4,4,4)\) and \(\Theta(5,5,5)\), the constant-constant atomic diagram agrees. Their realized one-variable atomic types agree: the two named terminals; vertices adjacent to exactly the first terminal; vertices adjacent to exactly the second; and vertices adjacent to neither. No vertex is adjacent to both terminals. Every \(\mathrm{FO}^{1}\) sentence in a relational language with constants depends only on these realized unary atomic types and the constant diagram. The two structures are therefore one-variable equivalent despite having different path lengths.

## Verification

The standalone file `verify_two_terminal_theta.py` constructs theta graphs, computes all graph distances by breadth-first search, checks the midpoint-witness lemma for every unordered length triple with entries from two through eight, and independently enumerates the partitions behind the theory count. A separate exact two-variable noncounting tuple-refinement implementation checks both languages for twelve selected graphs, including repeated lengths and distinct triples of equal total size. Run with Python 3 and no dependencies:

```bash
python verify_two_terminal_theta.py
```

Its expected exact standard output is supplied in `verification_output.txt`. Finite testing corroborates, but does not prove, the unrestricted statement. The proof in the previous section covers all integer lengths.

## Relationship to prior work

Pikhurko and Verbitsky's survey of logical graph complexity (arXiv:1003.4865, initially public 2010-03-25) treats fixed-variable first-order logic, pebble games and variable recycling for distance formulas. Its general three-variable distance formula does not state the present special reduction to two variables with named terminals or the three-path multiplicity reconstruction.

Knor, Sedlar and Škrekovski (arXiv:2203.07335) and Benakli, Froitzheim and Martinez (arXiv:2510.12100) analyze vertex/edge metric dimension of theta networks and generalized theta graphs. Their use of distances and repeated-path symmetries is closely relevant. In particular, the terminals may fail to resolve individual vertices on equal-length paths; that does not prevent their **distance-profile multiplicities** from recovering the global three-path length multiset. The inspected sections do not state fixed-variable logical equivalence or the named-versus-unnamed collapse. The scientific comparison is based on the actual claims and implications, not merely matching words; an unknown stronger general result remains a priority risk.

## Limitations

The result is restricted to three internally disjoint paths of length at least two, to the two named branch terminals when establishing rigidity, and to the corresponding unlabelled family for the collapse. The proof does not classify generalized theta graphs with an arbitrary number of parallel paths; two-variable formulas in general cannot count arbitrary multiplicities. The claim is relative to the theta family and does not give global defining widths among all finite graphs. The result does not apply without alteration when a direct edge connects the terminals (shortest length one), because the strict distance-difference witness argument changes. Independent mathematical audit has not been performed; historical originality is assessed against inspected accessible sources and remains provisional.

## References

1. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865 (initial submission 2010-03-25), https://arxiv.org/abs/1003.4865.
2. M. Knor, J. Sedlar and R. Škrekovski, *Remarks on the vertex and the edge metric dimension of 2-connected graphs*, arXiv:2203.07335 (2022), https://arxiv.org/abs/2203.07335.
3. N. Benakli, N. Froitzheim and D. Martinez, *Metric Dimension of Generalized Theta Graphs*, arXiv:2510.12100 (2025), https://arxiv.org/abs/2510.12100.
