# Finite-variable theories of rooted height-two parent structures

## Finding

In the pure signature consisting of equality and one binary relation \(E\), let \(\mathcal T\) be the class of finite structures obtained from a rooted tree of height at most two by directing each nonroot edge toward its parent and retaining the loop \(E(r,r)\) at the root. An edge \(E(x,y)\) means that \(y\) is the unique parent of \(x\); the unique root is a fixed point. Every nonroot point is at distance one or two from the root, and every first-level vertex may have any nonnegative number of children.

For \(T\in\mathcal T\), let \(a_j(T)\) be the number of first-level vertices having exactly \(j\) second-level children, let \(t_0=a_0\), \(t_+=\sum_{j\ge1}a_j\), and \(L=\sum_{j\ge1}j a_j\). Equivalence \(\equiv_{\mathrm{FO}^{k}}\) means agreement on every counting-free first-order sentence employing at most \(k\) reusable variable names, with **no restriction on quantifier depth**.

**Theorem.** The following are exact, for every pair \(S,T\in\mathcal T\).

1. For \(k=1\), \(S\equiv_{\mathrm{FO}^{1}}T\) exactly when both are root-only or both have a nonroot vertex. There are two theories.
2. For \(k=2\), \(S\equiv_{\mathrm{FO}^{2}}T\) exactly when the three coordinates \(\min(t_0,2)\), \(\min(t_+,2)\), and \(\min(L,2)\) agree. There are exactly twelve theories.
3. For every \(k\ge3\), put \(m_j^{(k)}(T)=\#\{v\text{ first-level}:\min(\deg_{\rm child}(v),k)=j\}\), for \(0\le j\le k\). Then

\[
S\equiv_{\mathrm{FO}^{k}}T\quad\Longleftrightarrow\quad
\min(m_j^{(k)}(S),k)=\min(m_j^{(k)}(T),k)
\quad(0\le j\le k).
\]

There are exactly \((k+1)^{k+1}\) distinct theories for each \(k\ge3\), each with a unique minimum-cardinality representative up to isomorphism. The variable-width hierarchy on this class is strict at every width.

## Assumptions and scope

The class includes the one-vertex tree, trees whose first-level vertices have no children, and arbitrary finite multisets of child multiplicities; no uniform degree bound is assumed. There are no unary predicates, constants, function symbols, counting quantifiers, or named root in the language. The root loop is essential to the signature. The isomorphism type of a structure is exactly the multiset of the nonnegative first-level child counts. For a first-level vertex \(v\), \(\deg_{\rm child}(v)\) is the cardinality of \(\{x:E(x,v),\ x\ne v\}\). Each variable width is fixed, but formula nesting may be arbitrarily deep.

## Proof

**One variable.** The root is the unique element satisfying \(E(x,x)\). Every other vertex fails \(E(x,x)\), and these are the only one-variable atomic possibilities. Hence a root-only structure and every nontrivial structure are the two theories.

**Two-variable classification.** Four vertex types are definable with two variable names: root \(R\), childless first-level vertex \(M_0\), first-level vertex having a child \(M_+\), and second-level leaf \(L\). In particular \(R(x)\) is \(E(x,x)\); \(M_+(x)\) is \(\neg E(x,x)\wedge\exists y\,E(y,x)\); and \(M_0(x)\) is
\[
\neg E(x,x)\wedge\exists y\bigl(E(x,y)\wedge E(y,y)\bigr)\wedge\neg\exists y\,E(y,x).
\]
The remaining vertices have type \(L\). Existence of one or two distinct vertices of any of these types is expressible with two variables (inner type tests may locally rebind the other variable). This recovers all three truncated coordinates in the theorem.

For the converse, consider the permanent two-pebble game. For a pinned root, the available response types depend only on which of \(M_0,M_+,L\) occur. For a pinned \(M_0\), a distinct \(M_0\) exists exactly when \(t_0\ge2\); all leaves and all \(M_+\) are unrelated to it. For a pinned \(M_+\), a related leaf always exists; an unrelated leaf exists exactly when \(t_+\ge2\), while distinct \(M_+\) and any \(M_0\) are controlled by the same truncated coordinates. For a pinned leaf, there is a unique related \(M_+\), a different \(M_+\) exactly when \(t_+\ge2\), and a distinct leaf exactly when \(L\ge2\). Equality, both directed incidences, and the type of the newly placed vertex are therefore preserved using only the triple of capped numbers, for either choice of moved pebble, in indefinitely many rounds. The feasible triples number \(3\) when \(t_+=0\), \(6\) when \(t_+=1\), and \(3\) when \(t_+\ge2\): twelve in total.

**Function-symbol reduction for at least three variables.** Temporarily write \(f(x)\) for the unique \(E\)-successor. On this class, \(f(f(x))=r\) for every \(x\). Every atomic equality between terms in the single-unary-function language therefore reduces to a Boolean combination of equality, incidence, the root-loop test, and formulas using just one auxiliary variable. For example, \(f(x)=f(y)\) is
\[
\exists z\bigl(E(x,z)\wedge E(y,z)\bigr),
\]
while \(f^2(x)=y\) is \(E(y,y)\) and \(f(x)=r\) is \(\exists z(E(x,z)\wedge E(z,z))\). Thus each atomic formula (which involves at most two distinct free variables) can be translated with three variable names. The auxiliary name may locally shadow another surrounding variable: no free name of that atom is captured. By induction, \(\mathrm{FO}^{k}\) over \(E\) and \(\mathrm{FO}^{k}\) over \(f\) have equal distinguishing power on this class whenever \(k\ge3\). The reverse translation \(E(x,y)\leftrightarrow f(x)=y\) is atomic.

**Detecting first-level child counts.** In the functional language, a first-level vertex satisfies \(f(v)\ne v\) and \(f^2(v)=f(v)\). Fix \(k\ge3\). With a free variable \(v\), the condition that \(v\) has at least \(j<k\) distinct children uses \(j+1\le k\) variables. To detect at least \(k\) children, choose \(k-1\) distinct children \(y_2,\ldots,y_k\) of \(v\), then rebind the variable name \(v\) to a further distinct point with \(f(v)=f(y_2)\). Before rebinding, the \(k-1\) original child-parent incidences have been tested; after rebinding, the \(k\)-th child has the same parent as the first selected child. This is a legitimate \(k\)-variable formula. Consequently each exact clipped child-count type \(j\in\{0,\ldots,k\}\) is definable with one free variable and at most \(k\) names. Existence of \(s\le k\) distinct first-level vertices of this type can be asserted with \(k\) outer variables, because the local type-test quantifiers may shadow unused outer variable names within their own subformulas. This distinguishes every differing coordinate \(\min(m_j^{(k)},k)\).

**Permanent strategy for matching profiles.** Assume the clipped count-of-counts profiles agree. In the functional-language \(k\)-pebble game, maintain a bijection between *represented* first-level branches (those containing a pebbled middle vertex or pebbled leaf), matching their clipped child counts, and maintain an injection between the leaves pebbled within paired branches. The roots match. When a pebble is moved, first release any branch no longer represented; then a new branch of clipped type \(j\) can always be matched: at most \(k-1\) branches are represented before the placement, while each profile class has equal multiplicity below \(k\), or has at least \(k\) branches on both sides. Similarly, a fresh leaf in a previously matched branch can be matched because at most \(k-1\) leaves were selected before this placement and both branch sizes are equal below \(k\) or at least \(k\). This invariant preserves the complete functional term graph of all pebbled points, including their parents and the root, so is maintained for arbitrarily many rounds. Translating back to \(E\) proves the converse.

**Counting, minimum models, strictness.** Every \((k+1)\)-tuple of capped branch-type multiplicities in \(\{0,\ldots,k\}^{k+1}\) occurs: use exactly the specified number of branches, taking exactly \(j\) children in each type \(j\). That representative minimizes cardinality coordinatewise and is unique up to isomorphism. Hence the theory count is \((k+1)^{k+1}\). The root-only structure versus the root with one child witnesses a one-variable separation, while the root with one versus two childless first-level vertices separates two variables but not one. At width two versus three, the child multiplicity multisets \((1,1)\) and \((1,2)\) have the same two-variable invariant but different three-variable profiles. For each \(k\ge3\), one branch with \(k\) versus \(k+1\) leaves separates widths \(k\) and \(k+1\).

## Verification

Two standalone Python programs, `check_pebble_refinement.py` and `check_invariants.py`, are included with their recorded JSON outputs. The first applies joint stable, set-based (noncounting) \(k\)-pebble refinement to all partial tuples of finite samples and compares its sentence colors with the theorem. Its pair comparisons were: \(2,346\) at width one; \(2,346\) at width two; \(595\) at width three; \(325\) at width four; all with zero mismatches. The second checks one-point two-pebble extension profiles for \(69\) examples and validates \(609\) child-threshold instances, also with zero discrepancies. It separately constructs the combinatorial spectrum counts \(256\) for width three and \(3,125\) for width four. Reproduce from these files using `python check_pebble_refinement.py` and `python check_invariants.py` in an ordinary Python 3 environment with no third-party packages. These experiments are finite corroboration, not infinite proofs; the theorem above is proved by formulas and a permanent game strategy.

## Relationship to prior work

Immerman and Kozen's bounded-variable definability work develops reusable-variable games and sharp results for *bounded-branching trees* in an ancestry-order language, and distinguishes finite-model behavior. Its hypotheses and stated classifications do not provide the exact unrestricted-depth two-variable twelve-phase spectrum or the arbitrary-unbounded-degree height-two parent-edge spectrum here. Dawar and Holm develop the general finite-variable game machinery without this specialized family classification. Work on logical complexity of trees in the undirected graph signature likewise does not state the theorem above. The construction combines established game techniques with the explicit low-variable incidence obstruction and a resource-preserving functional-to-relational translation. No claim is made that the game framework itself is new.

## Limitations

This is a theorem about finite, rooted, height-at-most-two functional digraphs in the stated **loop-retaining parent-edge** signature. It is not a classification for arbitrary deeper rooted trees, undirected trees, root-labeled expansions, counting logic, or two-variable unary-function logic (where terms are already available without a third variable). The exact spectrum formula is for widths at least three. Finite programs do not establish the infinite-universe theorem. The comparison with earlier literature is substantial but cannot exclude a previously unidentified stronger result under different terminology.

## References

1. N. Immerman and D. Kozen, “Definability with Bounded Number of Bound Variables,” *Information and Computation* 83 (1989), 121–139; an earlier version appeared at LICS 1987. Public author's full text: https://www.cs.cornell.edu/~kozen/Papers/bbv.pdf.
2. A. Dawar and B. Holm, “Pebble Games with Algebraic Rules,” arXiv:1205.0913, first submitted 2012-05-04, https://arxiv.org/abs/1205.0913.
3. O. Pikhurko and O. Verbitsky, “Logical complexity of graphs: a survey,” arXiv:1003.4865, first submitted 2010-03-25, https://arxiv.org/abs/1003.4865.
