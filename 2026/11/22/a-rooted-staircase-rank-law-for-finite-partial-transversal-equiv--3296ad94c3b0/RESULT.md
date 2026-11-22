# A rooted-staircase rank law for finite partial-transversal equivalence relations

## Finding

Consider finite structures \(X=(V,E,P)\) consisting of an equivalence relation \(E\) and a unary predicate \(P\) with **at most one \(P\)-point in each equivalence class**. Use one-point-extension rank relative to the hereditary class of all such finite structures, including the empty structure.

Write \(b\) for the number of equivalence classes containing a \(P\)-point, and sort their counts of ordinary (non-\(P\)) points as \(u_1\ge\dots\ge u_b\ge0\). Write \(z\) for the total number of ordinary points in the classes containing no \(P\)-point. For every integer \(t\ge1\),

\[
\operatorname{rk}(X)\ge t
\quad\Longleftrightarrow\quad
b\ge t,\quad
u_j\ge t-j+1\quad(1\le j<t),\quad
u_t+z\ge1.
\]

The subscript on each \(u_j\) refers to an ordered rooted equivalence class, not to an individual vertex. The rank of every finite \(X\) is the largest nonnegative integer satisfying these conditions.

In particular, the least size of a structure of rank at least \(t\ge1\) is

\[
N_t=\frac{t(t+3)}2.
\]

At this size there are **exactly two nonisomorphic extremal structures**: either rooted classes of sizes \(2,3,\ldots,t+1\), or rooted classes of sizes \(1,3,4,\ldots,t+1\) together with a separate unrooted singleton. Here a rooted class means an equivalence class with exactly one \(P\)-point. Both have rank exactly \(t\), and no structure with fewer than \(N_t\) vertices reaches \(t\). Consequently, for every integer \(n\ge0\),

\[
\max_{|X|=n}\operatorname{rk}(X)
=\left\lfloor\frac{\sqrt{8n+9}-3}{2}\right\rfloor.
\]

## Assumptions and scope

The language contains equality, one binary equivalence relation \(E\), and one unary predicate \(P\). Its models are precisely the finite, possibly empty, structures where each \(E\)-class has at most one \(P\)-point. A substructure always means an **induced** substructure, so a rooted class may become unrooted after deleting its root.

For a finite host \(X\) and an induced marked substructure \(F\subseteq X\), let \(\operatorname{rk}_X(F)\ge0\) hold. Recursively, \(\operatorname{rk}_X(F)\ge t+1\) means that **every** isomorphism type over \(F\) of a permitted one-point extension can be realized inside \(X\) by adding one previously unused point so the resulting position has rank at least \(t\). This is the rank of Definition 2.3 in López-Callejas and Navarro-Castillo (2026), not ordinary first-order quantifier rank or the model-theoretic rank of a partial type. Set \(\operatorname{rk}(X)=\operatorname{rk}_X(\varnothing)\).

The following stronger relative characterization includes all finite marked positions. Let \(\mathcal A(F)\) be the set of host equivalence classes meeting \(F\); for \(C\in\mathcal A(F)\), let \(f_C\) count its ordinary points outside \(F\). Let \(U\) be the induced union of all host classes not meeting \(F\). Then, for each integer \(t\ge1\),

\[
\operatorname{rk}_X(F)\ge t
\quad\Longleftrightarrow\quad
\left(\forall C\in\mathcal A(F): C\cap P\ne\varnothing\ \text{and}\ f_C\ge t\right)
\quad\text{and}\quad \operatorname{rk}_U(\varnothing)\ge t.
\tag{R}
\]

## Proof

**1. The relative separation lemma (R).** Every one-point-extension type of \(F\) is one of four forms: an ordinary point in a specified active class; a \(P\)-point in a specified active class with no \(P\)-point already marked; an ordinary point in an entirely new class; or a \(P\)-point in an entirely new class. Each is a legitimate abstract extension whenever its stated marking condition holds, even if the host cannot realize it.

We prove (R) by induction on \(t\). At \(t=1\), each active class must admit both its ordinary-point extension and, if its root has not yet been marked, its \(P\)-point extension. This requires an actual root and at least one unused ordinary point in each active class. The two new-class types require respectively an ordinary point and a \(P\)-point in the untouched union \(U\). These two independent requirements say precisely \(\operatorname{rk}_U(\varnothing)\ge1\). Thus (R) holds for \(t=1\).

Assume (R) for \(t-1\) with \(t\ge2\). If the rank at \(F\) is at least \(t\), every active class must have an actual root: if its root has not been marked, the corresponding \(P\)-extension is mandatory, while if already marked its existence is automatic. The ordinary-point extension in any active class must lead to a position of rank at least \(t-1\). By induction the class then has at least \(t-1\) ordinary points still unused, hence it had at least \(t\) before that move.

For any of the two new-class types, the rank assumption supplies a realization in some class \(C\subseteq U\) whose expanded position has rank at least \(t-1\). By the inductive characterization, its restriction to the still-untouched union \(U\setminus C\), together with the newly active class \(C\), is a legal position of rank at least \(t-1\) **within \(U\)**. Hence both new-class types have suitable responses in \(U\), showing \(\operatorname{rk}_U(\varnothing)\ge t\).

Conversely, suppose the right side of (R). An ordinary-point request in any old class consumes one of at least \(t\) ordinary points. A root request in that class consumes its available root, if unmarked. Either way the old class retains its root in the host and at least \(t-1\) unmarked ordinary points; the untouched union remains rank at least \(t\), hence at least \(t-1\). For a request for a new class, use a rank-at-least-\(t\) response in \(U\). The old classes still meet the required capacity \(t-1\), and the new active class plus the remaining untouched union satisfy the inductive conditions in \(U\). In all cases the whole resulting position has rank at least \(t-1\) by induction. Therefore \(\operatorname{rk}_X(F)\ge t\), completing the proof of (R).

**2. Empty-position peeling.** At rank one, the empty position must realize an ordinary new singleton and a rooted new singleton, independently. Thus

\[
\operatorname{rk}(X)\ge1\quad\Longleftrightarrow\quad
P\ne\varnothing\quad\text{and}\quad V\setminus P\ne\varnothing.
\tag{B}
\]

For \(t\ge2\) we claim the exact recursive criterion

\[
\operatorname{rk}(X)\ge t\quad\Longleftrightarrow\quad
\exists\text{ rooted class }C:\ |C\setminus P|\ge t
\ \text{and}\ \operatorname{rk}(X\setminus C)\ge t-1.
\tag{P}
\]

For necessity, challenge first with a new-class ordinary point. The chosen host class \(C\) must give a rank-at-least-\(t-1\) marked position. Equation (R) implies that \(C\) contains a root, that at least \(t-1\) ordinary points remain after the move, and that the untouched remainder has rank at least \(t-1\). Therefore \(|C\setminus P|\ge t\), proving the right side of (P).

For sufficiency, use the stated rooted class \(C\) as a response to **either** of the two new-class types. If an ordinary point is requested, at least \(t-1\) ordinary points of \(C\) remain; if a root is requested, at least \(t\) remain. In either case the root is present in \(C\) and the untouched union \(X\setminus C\) has rank at least \(t-1\). By (R) both responses have rank at least \(t-1\), proving (P).

Iterating (P), rank at least \(t\) is equivalent to selecting \(t-1\) **distinct rooted classes** with ordinary capacities at least \(t,t-1,\ldots,2\), leaving a remainder that satisfies (B). The exchange argument for sorted capacities is straightforward but important: if a selected class has smaller ordinary capacity than an unselected rooted class, exchange them. Each selected threshold remains satisfied, and the remainder can still satisfy (B), since the smaller rooted class supplies at least one root; if the old remainder had an ordinary point only in the exchanged class, the exchanged-out class necessarily has positive ordinary capacity as well. Repeating yields the \(t-1\) largest rooted classes as a valid choice whenever any choice exists.

After these classes are removed, a rooted class remains precisely when \(b\ge t\); the remainder has an ordinary point precisely when \(u_t+z\ge1\). The chosen classes meet their thresholds precisely when \(u_j\ge t-j+1\) for \(1\le j<t\). This proves the announced sorted criterion, including the \(t=1\) boundary via (B).

**3. Sharp minimum order and rigidity.** For rank at least \(t\), the peeled rooted classes have sizes at least \(t+1,t,\ldots,3\), and the terminal rank-one remainder has at least two points (one rooted, one ordinary). Hence

\[
|X|\ge2+\sum_{i=2}^{t}(i+1)=\frac{t(t+3)}2.
\]

Equality forces the peeled rooted classes to have exactly the displayed sizes, and the terminal remainder to have exactly two points, with at least one root and one ordinary point. Up to isomorphism there are precisely two such two-point remainders: a single rooted two-point class, or a rooted singleton and a separate unrooted ordinary singleton. The two constructions meet (P) recursively and thus achieve rank at least \(t\). They cannot have rank at least \(t+1\), because the already proved size lower bound for \(t+1\) is strictly greater. This establishes the minimum-size classification. Finally, adding arbitrary ordinary points or classes cannot decrease rank, so the sharp maximum on exactly \(n\) points follows by solving \(t(t+3)/2\le n\) and taking the integer floor.

## Verification

The self-contained `checker.py` enumerates every unlabelled permitted host through ten vertices, uses an individual-subset minimax recursion following the definition of rank, and compares each marked position with (R). It also cross-checks the empty-host rank against the sorted criterion and a separately implemented component-profile game. The verified totals are **1,215 hosts** and **2,325,866 marked-position/threshold comparisons**. Randomized component-level checks and both minimum-size templates through rank six passed. Run `python3 checker.py` with Python 3 standard library only; the expected final line begins `ALL_CHECKS_OK`. The computation is finite corroboration; the all-size statement follows from the induction and exchange argument above, not enumeration.

## Relationship to prior work

López-Callejas and Navarro-Castillo (2026) introduce the precise extension-game rank used here and compute it for linear orders and other classes; their inspected text has no result characterizing the finite partial-transversal equivalence class. The classical uncoloured equivalence-class staircase cannot be transferred by simply forgetting \(P\): the permitted prime extensions and the rooted-versus-rootless residual obstruction change, and minimum rank-one hosts already have two distinct forms.

The published finite-theory classifications *A sharp thirteen-element rank-two model bound for unary-coloured equivalence relations* and *Twenty-one rank-three theories of finite equivalence relations* count **ordinary first-order quantifier-rank theories**. The former even allows many \(P\)-points in one class. These claims do not imply the one-host extension-game formula (R) or its sharp minimum-size law. The published idempotent-unary-structure theorem *Twelve rank-two theories of idempotent unary structures and a sharp seven-point reduction* also concerns first-order logical equivalence; rooted-star components are related objects, but its rank is a different mathematical invariant. Guingona and Parnes (2020, revised 2026) define a further distinct \(\mathbf K\)-rank on partial types, not the extension-game rank used here.

## Limitations

All results concern **finite** structures and finite integer ranks, the exact signature \(\{E,P\}\), and at most one \(P\)-point per class. No statement about countably infinite rank spectra or arbitrary unary-coloured equivalence relations is made. The exact historical priority of the formula remains provisional; the accessible literature and published comparisons do not constitute an exhaustive survey of all older or inaccessible sources. Computer checks do not constitute an independent audit or a proof of the infinite family of claims.

## References

1. C. López-Callejas and J. Navarro-Castillo, *A rank function for Fraïssé classes and the rank property*, arXiv:2604.14461v1, first posted 2026-04-15. https://arxiv.org/html/2604.14461v1
2. V. Guingona and M. Parnes, *Ranks Based on Algebraically Trivial Fraïssé Classes*, arXiv:2007.02922, first posted 2020-07-06, revised 2026. https://arxiv.org/abs/2007.02922
3. *A sharp thirteen-element rank-two model bound for unary-coloured equivalence relations*, scientific record: https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-sharp-thirteen-element-rank-two-model-bound-for-unary-coloured--e2acfc789698
4. *Twenty-one rank-three theories of finite equivalence relations*, scientific record: https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-twenty-one-rank-three-theories-of-finite-equivalence-relations--a736c29db7bd
5. *Twelve rank-two theories of idempotent unary structures and a sharp seven-point reduction*, scientific record: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-twelve-rank-two-theories-of-idempotent-unary-structures-and-a-sh--8f7963a8fbee
