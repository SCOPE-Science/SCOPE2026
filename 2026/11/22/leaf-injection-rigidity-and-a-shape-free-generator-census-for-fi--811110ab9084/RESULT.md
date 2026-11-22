# Leaf-injection rigidity and a shape-free generator census for finite modal forests

## Finding

**Theorem (all finite out-forests).** Let \(F=(W,R)\) be any finite nonempty disjoint union of rooted directed trees. Every arrow is directed from a parent to one of its *immediate* children; there are no loops or shortcut edges. Put \(n=|W|\), let \(L\ge1\) be the number of vertices with no children, and let \(h\) be the maximum number of edges on a directed path in \(F\). Equip the Boolean powerset \(\mathcal P(W)\) with the ordinary existential modal operation \(\Diamond U=\{v:\exists w\,(vRw\land w\in U)\}\).

For any \(k\ge0\), an ordered \(k\)-tuple of Boolean subsets supplies an atomic colour \(c(v)\in\{0,1\}^k\) to each vertex. Write \(q=2^k\). The following statements are equivalent:

1. The \(k\) subsets generate the **whole** Boolean modal powerset algebra \(\mathcal P(W)\).
2. Every pair of distinct leaf vertices has **different** atomic colours.

No constraint whatsoever is imposed on the colours of internal vertices. Consequently, the exact number of ordered generating \(k\)-tuples is
\[
\boxed{G_F(k)=(2^k)_{\underline L}\,(2^k)^{n-L},}
\]
where \((z)_{\underline L}=\prod_{j=0}^{L-1}(z-j)\) is taken to be zero if \(L>z\). The minimum number of Boolean generators, including the possibility of an empty tuple, is
\[
\boxed{\operatorname{rank}(F)=\lceil\log_2 L\rceil.}
\]

Every singleton has an explicit defining formula of modal depth **at most \(h\)** for every generating tuple. This depth bound is uniformly sharp: on an all-one-colour outward directed path of height \(h\ge1\), no family of formulas of depth below \(h\) separates its root from its first child.

With independent uniform atomic colours at the vertices, the exact generation probability is
\[
\Pr(\mathrm{generates})=\frac{(q)_{\underline L}}{q^L}.
\]
In particular, for any sequence with \(L\to\infty\), if \(q/L^2\to c\in(0,\infty)\), the probability converges to \(\exp(-1/(2c))\); it converges to zero when \(q/L^2\to0\), and to one when \(q/L^2\to\infty\). These expressions depend on tree shape only through \(n\) and \(L\), and the sharp depth bound only through \(h\).

## Assumptions and scope

The frame is a finite **outward-oriented forest**: each component has one root and each other vertex has exactly one parent, so any leaf and any fixed upward distance determine at most one ancestor. The relation \(R\) means immediate child, not reflexive reachability, transitive descendant, an undirected edge, or an arbitrary acyclic directed graph. The modal language has constants, Boolean complement, union and intersection, and \(\Diamond\); the dual \(\Box\) is therefore available. An empty tuple of generators is permitted when \(k=0\), and has one available colour (the empty bit string). Count vertices as labeled, generators as ordered, and colour assignments independently across vertices. A leaf means outdegree zero, even if it is also an isolated root.

Define the **residual height** \(d(v)\) to be the maximum length of a directed path from \(v\) to any leaf. Thus \(0\le d(v)\le h\), and every path of length exactly \(d(v)\) from \(v\) ends at a leaf. For \(k\ge0\), the atomic colour minterm \(M_a\) is the conjunction, over each generator coordinate, of that generator or its negation according to the bit of \(a\); for the empty bit string, \(M_a=\top\).

## Proof

**1. Necessity of leaf injection.** Let \(u,v\) be distinct leaves with \(c(u)=c(v)\). Every propositional generator has the same truth value at \(u\) and \(v\), as do all Boolean constants. Induct on formula construction: Boolean connectives preserve agreement; both vertices have no children, so both make every formula of the form \(\Diamond\varphi\) false. Hence all Boolean modal terms built from the generators agree on \(u,v\), and no generated subset separates their singleton points. Therefore the full powerset algebra is not generated.

**2. A concrete singleton formula.** Suppose the leaf colours are pairwise different. For each \(0\le d\le h\), define
\[
E_d=\begin{cases}
\Diamond^d\top\ \wedge\neg\Diamond^{d+1}\top,&d<h,\\
\Diamond^h\top,&d=h.
\end{cases}
\]
Here \(\Diamond^0\psi=\psi\); in particular, if \(h=0\), \(E_0=\top\). By the definition of maximum path length, \(E_d\) holds at exactly the vertices of residual height \(d\). Its modal depth is \(d+1\) for \(d<h\), and \(h\) for \(d=h\), hence never exceeds \(h\).

Take any vertex \(v\) and put \(d=d(v)\). Choose a leaf \(\ell\) at distance exactly \(d\) below \(v\), and consider the formula
\[
\theta_v:=E_d\ \wedge\ \Diamond^d M_{c(\ell)}.
\]
Clearly \(v\models\theta_v\). If another vertex \(w\models\theta_v\), then \(d(w)=d\). Every endpoint of a path of length \(d\) from \(w\) is a leaf, so some leaf at distance \(d\) has colour \(c(\ell)\). Leaf-colour injectivity forces that endpoint to be the **same** leaf \(\ell\). In an outward-oriented forest a leaf has exactly one ancestor at a given distance; hence \(w=v\). Thus \(\theta_v\) defines precisely \(\{v\}\) and has modal depth at most \(h\). Taking finite Boolean unions gives every subset of \(W\), establishing sufficiency.

**3. Counting and minimum rank.** An ordered tuple of \(k\) subsets is equivalent bijectively to a choice of one of \(q=2^k\) bit words at each of the \(n\) labeled vertices. There are \((q)_{\underline L}\) injections from the \(L\) labeled leaves into the palette, and independently \(q^{n-L}\) arbitrary choices for all internal vertices. This gives the exact formula, including \(q<L\) yielding zero. Generation is possible precisely when \(2^k\ge L\), which gives the displayed minimum, with \(k=0\) valid exactly if \(L=1\).

**4. Sharp depth.** Consider a path of \(h\) edges directed from its root toward its sole leaf, and give all vertices the same colour. At modal depth \(t\), any two path vertices whose remaining heights are both at least \(t\) have the same modal theory: this follows inductively in \(t\), since their atomic valuations agree and they each have a unique successor with remaining height at least \(t-1\), while the depth-zero case is immediate. The root (remaining height \(h\)) and its child (height \(h-1\)) therefore agree on every formula of depth at most \(h-1\). Yet \(\Diamond^h\top\) holds only at the root. The bound \(h\) cannot be decreased uniformly. The degenerate height-zero case has all singletons definable at depth zero whenever leaf colours are injective.

**5. Random-generation threshold.** Independent uniform colors make the probability of pairwise distinct leaf colors exactly \((q)_{\underline L}/q^L=\prod_{j=0}^{L-1}(1-j/q)\) when \(q\ge L\), and zero otherwise. If \(q/L^2\to c\in(0,\infty)\), then \(L/q\to0\) and Taylor expansion gives
\[
\log\Pr(\mathrm{generates})=-\frac{L(L-1)}{2q}+O\left(\frac{L^3}{q^2}\right)\longrightarrow-\frac1{2c}.
\]
If \(q/L^2\to0\), the probability is zero for \(q<L\), and otherwise its logarithm is at most \(-L(L-1)/(2q)\to-\infty\). If \(q/L^2\to\infty\), a union bound for coinciding leaf colors makes the failure probability at most \(L(L-1)/(2q)\to0\). This proves all asserted limits.

## Verification

The included standalone `verify.py` represents each finite rooted forest on labeled vertices by its parent array, independently computes the bottom-up modal observation signatures, tests leaf-colour injectivity, verifies the exact generating-tuple census for every forest checked, and separately constructs the closure of generated subsets under Boolean connectives and \(\Diamond\) in small cases. Run using Python 3 and no third-party dependencies:

```text
python3 verify.py
```

Its actual output was:

```text
VERIFY_OK coloring_cases=830839 direct_boolean_closures=4435 forest_cases=5913 sharp_paths=30
```

The 5,913 enumerated out-forests cover every increasing-parent forest through seven vertices (which represents every isomorphism class in that range, though not every labeled parent numbering); colour assignments include one- and two-colour cases through seven vertices and four-colour cases through five vertices. Direct Boolean modal term closures are checked on 4,435 small cases. Sharp-depth witnesses are checked for path heights one through thirty. These finite computations corroborate, but do not replace, the unrestricted proof above.

Examples: on an outward path, \(L=1\), so **every** choice of predicate values generates the whole algebra (including the empty tuple). On an outward star with \(m\) leaves, generation requires all leaf colors distinct; the root's color is arbitrary, so the exact count is \((q)_{\underline m}q\). With two distinct leaf nodes in different tree components, one Boolean generator suffices irrespective of the components' heights.

## Relationship to prior work

The 2026 study *On Local Finiteness of Modal K4 Algebras* treats finite generation and local finiteness for **transitive** modal relations, including order-theoretic classifications. Our finite immediate-child forests are generally nontransitive and the question is the count of **specific generating colorings** for the full finite powerset algebra; neither the leaf-only criterion nor its exact census follows as a stated result there.

The classical modal **colouring theorem**, as presented in J. Carr's 2022 thesis (Theorem 2.19), characterizes generation abstractly by the absence of monochromatic nontrivial modal equivalences. It does not supply the finite-forest reduction of this condition to leaf injection, the all-labeling count, or the sharp modal-depth and probability formulas. The singleton construction above supplies the additional structural argument; an abstract equivalence alone is not counted as the new claim.

The published *Exact observable-labeling census for finite deterministic modal frames* gives a primitive-necklace and incoming-fiber product for **total functional successor relations**. The outward tree relation here is generally many-successor and partial, and the leaf-only coloring criterion is different; neither statement subsumes the other. The published *A sharp 47-vertex tree for all sixteen depth-three modal types* uses the same immediate-child semantics but concerns **atom-free depth-three type coverage** and minimum witness size, not generator valuations on a fixed forest. Other existing work on ordinary versus graded bisimulation on colored complete trees compares quotient cardinalities rather than characterizing and enumerating fully distinguishing color assignments. General coalgebraic modal-witness algorithms produce singleton separators once inequivalence is known; they do not state a leaf-injection criterion or a shape-free census.

## Limitations

The theorem assumes a **finite, nonempty, outward-oriented forest with immediate-child arrows**, using ordinary (not counting or graded) existential modal logic and full Boolean operations. It makes no claim for infinite forests, transitive closures, undirected edges, or acyclic graphs where different parents share descendants. For example, two same-coloured roots each pointing to one shared leaf are modally indistinguishable even though the graph has only one leaf, demonstrating the need for unique-parent structure. The birthday limit is the classical collision calculation once the structural criterion is proved and is not separately presented as a novel probability theorem. The counting formula treats ordered predicates and labeled vertices; it does not quotient by symmetries. Historical priority for the leaf-only criterion under other coalgebraic terminology remains provisional. Finite checks are not an infinite proof; independent verification is not claimed.

## References

1. G. Agnew, *On Local Finiteness of Modal K4 Algebras*, arXiv:2606.02941 (first publicly submitted 1 June 2026), https://arxiv.org/abs/2606.02941.
2. J. Carr, *Hereditary Structural Completeness over K4: Rybakov's Theorem Revisited*, MSc thesis, University of Amsterdam (2022), Theorem 2.19 (colouring theorem), https://eprints.illc.uva.nl/id/eprint/1875/1/MoL-2022-02.text.pdf.
3. *Exact observable-labeling census for finite deterministic modal frames* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-exact-observable-labeling-census-for-finite-deterministic-modal--5345b2acbad9.
4. *A sharp 47-vertex tree for all sixteen depth-three modal types* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-sharp-47-vertex-tree-for-all-sixteen-depth-three-modal-types--dda455b75ffa.
5. *A sharp arity threshold for graded-versus-ordinary bisimulation compression of regular trees* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-a-sharp-arity-threshold-for-graded-versus-ordinary-bisimulation--818ec1eeacfe.
6. T. Wißmann, S. Milius, L. Schröder, *Quasilinear-time Computation of Generic Modal Witnesses for Behavioural Inequivalence*, Logical Methods in Computer Science 18(4), 2022, arXiv:2203.11175, https://arxiv.org/abs/2203.11175.
