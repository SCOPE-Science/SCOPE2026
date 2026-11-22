# Sharp three-round thresholds and certified extremizers for coloured-pair structures

## Finding

Let \(q\ge 2\) be an integer, let \(C=\{0,1,\ldots,q-1\}\), and choose an involution \(\iota:C\to C\) with \(\iota(0)=0\). Consider finite structures \(X\) with a pair state \(c_X(u,v)\in C\) for each ordered pair of *distinct* vertices, subject only to \(c_X(v,u)=\iota(c_X(u,v))\). The state \(0\) denotes absence of a nonzero pair relation. Embeddings preserve *all* pair states, including zero. Let \(\operatorname{rk}(X)\) be the one-point-extension rank relative to this hereditary class, as defined below, and let \(e_*(X)\) count unordered pairs whose state is nonzero.

The following vertex and support minima are simultaneously sharp:

\[
\min\{|X|:\operatorname{rk}(X)\ge3\}=q^2+q+1,
\qquad
\min\{e_*(X):\operatorname{rk}(X)\ge3\}
=q^3-\frac{q(q-1)}2-1.
\]

For every \(n\ge q^2+q+1\), the latter edge-support minimum is attained by an \(n\)-vertex structure. At the first possible vertex order, the support-minimizers admit the complete **rooted-and-certified** normal form below. The number of its isomorphism types, where a rank witness root and one partner for each of the \(q\) relation states are designated, is exactly

\[
\boxed{(q-1)^{\binom q2}\left(\frac{q!}{2}\right)^{q(q-1)}.}
\]

The count is for *certified* structures, not for unpointed structures with possibly multiple choices of certificates. For ordinary unoriented simple graphs, \(q=2\), it specializes to the previously known seven-vertex, six-edge extremum and one certified type. For **oriented graphs allowing nonedges**, take \(q=3\), \(\iota(1)=2\), \(\iota(2)=1\): the first rank-three example has **13 vertices**, the least possible number of arcs is **23** at every host order at least 13, and there are **5,832** rooted-and-certified isomorphism types at the simultaneous vertex/arc minimum.

## Assumptions and scope

All structures are finite, irreflexive, and have no loops or unary predicates. Pair states are mutually exclusive and exhaustive on distinct ordered pairs. The involution guarantees coherent reversal; no triangle, transitivity, or other higher-order constraint is imposed. For oriented graphs, state \(1\) means the first vertex points to the second and state \(2\) means the reverse; state \(0\) means neither arc occurs. A nonzero *unordered* pair contributes one to \(e_*(X)\), independently of the chosen nonzero state.

For a finite induced substructure \(F\subseteq X\), define \(\operatorname{rk}_X(F)\ge0\) always, and \(\operatorname{rk}_X(F)\ge t+1\) iff **for every abstract one-vertex extension** of the named structure \(F\) in this class, some vertex \(z\in X\setminus F\) realizes that extension and satisfies \(\operatorname{rk}_X(F\cup\{z\})\ge t\). Put \(\operatorname{rk}(X)=\operatorname{rk}_X(\varnothing)\). This is the finite fragment of the ordinal-valued definition in the reference below; higher ordinal behavior is not needed here.

For distinct \(v,w\in X\), write
\[
P_X(v,w)=\{(c_X(v,z),c_X(w,z)):z\in X\setminus\{v,w\}\}.
\]
The **full-pair** property is \(P_X(v,w)=C^2\). The choice of the order \((v,w)\) is used for notation but fullness is independent of the order.

## Proof

### A three-round local criterion

Every abstract one-point extension of the *empty* structure has the same singleton type. Over a named singleton \(v\) there are exactly \(q\) one-point extension types, indexed by the state \(c_X(v,w)\). Over a named pair \((v,w)\), every pair of states \((c_X(v,z),c_X(w,z))\in C^2\) is a permitted extension, independently of the existing relation between \(v,w\). Unfolding the rank definition therefore gives the equivalence
\[
\operatorname{rk}(X)\ge3\quad\Longleftrightarrow\quad
\exists v\in X\ \forall i\in C\ \exists w_i\in X\setminus\{v\}:
\ c_X(v,w_i)=i\ \land\ P_X(v,w_i)=C^2.
\tag{1}
\]
The vertices \(w_i\) are necessarily distinct. Call \((v,(w_i)_{i\in C})\) a *certificate* for rank at least three.

### Vertex bound

Fix a certificate and partition \(X\setminus\{v\}\) into its \(q\) relation classes \(B_j=\{z:c_X(v,z)=j\}\). Since \(P_X(v,w_j)=C^2\), for every state \(s\in C\) there is a distinct \(z\in B_j\setminus\{w_j\}\) having \(c_X(w_j,z)=s\). Consequently \(|B_j|\ge q+1\) for every \(j\in C\). Hence \(|X|\ge1+q(q+1)\).

### Support bound

All \(q-1\) nonzero relation classes have size at least \(q+1\). Thus there are at least \((q-1)(q+1)=q^2-1\) nonzero pairs meeting the root \(v\). For each ordered index pair \((i,j)\in C^2\), fullness of \((v,w_i)\) requires a vertex of \(B_j\setminus\{w_i\}\) in each of the \(q-1\) distinct *nonzero* states as seen from \(w_i\). This yields at least \(q^2(q-1)\) incidences of nonzero pairs between a designated partner and a relation class.

Every nonzero unordered pair outside the root is counted at most once by these incidences, **except** a pair of different designated partners \(w_i,w_j\), which is counted twice if nonzero. There are at most \(\binom q2\) such pairs. Therefore the number of nonzero unordered pairs outside the root is at least \(q^2(q-1)-\binom q2\), proving
\[
e_*(X)\ge(q^2-1)+q^2(q-1)-\binom q2
=q^3-\binom q2-1.
\tag{2}
\]

Equality in (2) forces: each nonzero root class has exactly \(q+1\) vertices; all pairs among the \(q\) designated partners are nonzero; each partner \(w_i\) has **exactly one** neighbour of each nonzero state in each class \(B_j\); and no other nonzero pairs exist. At the minimum vertex order, \(|B_0|=q+1\) as well. These conditions are necessary by the equality cases of the disjoint support accounting and sufficient in conjunction with the full-pair property, which the following normal form makes explicit.

### Construction and complete certified normal form at the minimum vertex order

Take one distinguished root \(v\); for every \(j\in C\) take a partner \(w_j\) and \(q\) other vertices \(x_{j,s}\) indexed by \(s\in C\). These are all distinct, so the host has \(1+q(q+1)\) vertices. Prescribe:

1. \(c_X(v,z)=j\) for every \(z\in\{w_j\}\cup\{x_{j,s}:s\in C\}\).
2. \(c_X(w_j,x_{j,s})=s\) for every \(j,s\in C\).
3. For each unordered pair of distinct partners, choose an arbitrary **nonzero** state, respecting converse by \(\iota\).
4. For each **ordered** pair of distinct indices \((i,j)\), the edge \((w_i,w_j)\) already uses one nonzero state as viewed from \(w_i\). Assign each of the remaining \(q-2\) nonzero states to a different vertex among the \(q\) vertices \(x_{j,s}\), and assign state zero to the two remaining vertices.
5. Give state zero to every pair of vertices of the form \(x_{j,s},x_{k,t}\).

Assignments in steps 3–4 never conflict: step 3 sets only partner-to-partner pairs, and step 4 sets only partner-to-peripheral pairs in *other* relation classes. All converse states are determined by \(\iota\). Each \((v,w_i)\) now realizes all \(q^2\) state pairs: for the class \(B_i\), the \(q\) peripheral vertices supply all \(q\) states, and for each other class \(B_j\), the partner \(w_j\) plus the peripheral vertices supply every state. Thus (1) proves rank at least three. Direct counting shows the construction attains equality in both bounds. Adding isolated vertices preserves the existing certificate and support count, attaining the support minimum at every larger order.

Conversely, take any certified structure attaining both bounds. In its own class \(B_j\), the partner \(w_j\) has one peripheral vertex of each state \(s\in C\); those uniquely label the peripheral vertices as \(x_{j,s}\). Equality in (2) now forces *exactly* the five steps above. The normal form is therefore necessary and sufficient for a rank-three, support-minimal structure **with a specified certificate** at the smallest vertex order.

The chosen partner-to-partner states contribute \((q-1)^{\binom q2}\) independent possibilities. For each ordered pair \(i\ne j\), injecting the \(q-2\) remaining nonzero states into \(q\) named peripheral vertices contributes \(q!/(q-(q-2))!=q!/2\) choices, independently. Each rooted-and-certified structure has **no nontrivial automorphism preserving the certificate**: the root and all partners are fixed, and each peripheral vertex \(x_{j,s}\) is uniquely identified by its state from \(w_j\). Consequently the product counts isomorphism types, not just labelled constructions. For \(q=3\) it is \(2^3\cdot3^6=5832\).

## Verification

The standalone Python 3 standard-library program `checker.py` independently implements the three-round rank definition by recursion and, separately, the full-pair criterion. It constructs the normal form with the identity converse involution and with nontrivial converse involutions for \(q=2,3,4,5\), checking the vertex/support formulas and every certificate pair. It then enumerates all \(5832\) canonical oriented-graph normal forms at \(q=3\), verifies the 23-arc bound and pair profiles, and checks that all encoded structures are distinct. It also verifies by the unrolled rank recursion that deleting any one of the 23 arcs in one explicit minimizer destroys rank three, and checks all \(32768\) labelled six-vertex ordinary graphs against the rank-three criterion. The program prints explicit PASS messages for each test family.

The finite experiments check only the stated finite cases. The full theorem for all integers \(q\ge2\), every allowed converse involution, and arbitrarily large finite hosts follows from the structural arguments, not from these experiments.

## Relationship to prior work

López-Callejas and Navarro-Castillo, *A rank function for Fraïssé classes and the rank property* (first public arXiv version April 15, 2026; arXiv:2604.14461v1), provide the rank definition and prove general finite-rank realizability for free-amalgamation classes, including directed and edge-coloured structures. Their Sections 4–5 give constructions, but not the sharp three-round vertex and nonzero-pair support minima or the present certified normal forms.

The published result *Sharp rank-three onset and six-edge extremum for finite graphs* (published-finding corpus, November 8, 2026) already proves the **\(q=2\)** case, including the uniqueness of the ordinary unpointed six-edge minimizer. This specialization is credited, **not claimed as original here**. The new parameter-uniform theorem, the oriented-graph \(q=3\) minima, and the certification-count formula are not consequences of that binary case without the additional state-class and support-overlap analysis. The full published graph result was compared at the level of its criterion, proof and scope.

## Limitations

The enumeration \(5832\) classifies structures **with a distinguished root and one designated partner for each state**. It is not an enumeration of unrooted or uncertified oriented graphs, and no uniqueness of a minimum-arc oriented graph is asserted. The equality normal form explicitly counts configurations at the simultaneous minimum vertex order; at larger orders the minimum support count remains sharp, but the possible support placements need not be concentrated in a thirteen-vertex induced core. No general formula for rank four or higher is claimed. Historical originality beyond the inspected sources and search results remains subject to further independent verification.

## References

1. C. López-Callejas and J. Navarro-Castillo, *A rank function for Fraïssé classes and the rank property*, arXiv:2604.14461v1, first posted 2026-04-15. https://arxiv.org/html/2604.14461v1
2. *Sharp rank-three onset and six-edge extremum for finite graphs*, published 2026-11-08. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-rank-three-onset-and-six-edge-extremum-for-finite-graphs--a3c35b6162f1/RESULT.md
