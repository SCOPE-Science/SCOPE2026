# A component-rank staircase theorem and sharp kernels for finite unions of chains

## Finding

**General component-rank theorem.** Let \(\mathcal H\) be any hereditary class of finite relational structures in a positive-arity language without constants, with exactly one isomorphism type of nonempty singleton. Form \(\mathcal H^{\sqcup}\) by adjoining a distinguished equivalence relation \(E\), requiring every \(E\)-class to induce a member of \(\mathcal H\) and every other relation tuple to lie within one \(E\)-class. For a finite host \(X\) and a marked induced \(F\subseteq X\), write \(a_C=\operatorname{rk}^{\mathcal H}_C(F\cap C)\) for each occupied \(E\)-class \(C\). For the unoccupied \(E\)-classes \(D\), sort the *local host ranks* \(\rho_j=\operatorname{rk}^{\mathcal H}_{D_j}(\varnothing)\) into \(\rho_1\geq\cdots\geq\rho_k\). Then for every \(r\geq1\),

\[
\operatorname{rk}^{\mathcal H^{\sqcup}}_X(F)\geq r
\quad\Longleftrightarrow\quad
\bigl(a_C\geq r\text{ for every occupied }C\bigr)
\ \land\ k\geq r\ \land\
\bigl(\rho_j\geq r-j+1\text{ for }1\leq j\leq r\bigr).
\]

Thus the component construction sends arbitrary local game-rank values to a **descending staircase of rank capacities**. In particular, if the base class has a single finite induced-embedding kernel \(H_j\) for the threshold \(j\), then its component class has the single kernel \(H_r\sqcup H_{r-1}\sqcup\cdots\sqcup H_1\), with the components distinguished by \(E\). This is one theorem together with the following exact chain application.

For the hereditary class \(\mathcal K\) of finite strict partial orders that are disjoint unions of nonempty linear chains (also admitting the empty structure), the one-point-extension rank of **every** finite host \(X\) relative to **every** marked induced substructure \(F\subseteq X\) admits a complete simultaneous gap-and-component criterion.

For an integer \(r\geq1\), let \(L_r=2^r-1\). A component of \(X\) is *occupied* if it meets \(F\). The marked elements in each occupied chain divide that chain into intervals of unmarked vertices, called its *gaps*. Let \(g\) range over their cardinalities. Let \(m_1\geq\cdots\geq m_k\geq1\) be the sizes of all *unoccupied* components, sorted decreasingly. Then for each integer \(r\geq1\),

\[
\operatorname{rk}_X(F)\geq r\quad\Longleftrightarrow\quad
\bigl(\text{every occupied-chain gap has size at least }L_r\bigr)
\ \land\ k\geq r\ \land\
\bigl(m_j\geq L_{r-j+1}\text{ for }1\leq j\leq r\bigr).
\]

In the general statement, the base signature has only positive-arity relations and no constants, and the empty base structure belongs to the hereditary class. The empty set of gap inequalities is vacuous. Equivalently, putting \(\min\varnothing=+\infty\), for \(k\geq1\),

\[
\operatorname{rk}_X(F)=\min\left\{k,\ \min_g\left\lfloor\log_2(g+1)\right\rfloor,\ \min_{1\leq j\leq k}\left(j-1+\left\lfloor\log_2(m_j+1)\right\rfloor\right)\right\}.
\]

When \(k=0\), the rank is zero.

Let \(U_r\) denote the disjoint union of chains of lengths \(L_r,L_{r-1},\ldots,L_1\), and let \(U_0=\varnothing\). Thus \(U_r\) is a *single induced-embedding kernel*: for every finite \(X\in\mathcal K\),

\[
\operatorname{rk}(X)\geq r\quad\Longleftrightarrow\quad U_r\hookrightarrow X.
\]

Consequently the unique (up to isomorphism) minimum-order rank-at-least-\(r\) host has

\[
|U_r|=N_r=\sum_{i=1}^{r}(2^i-1)=2^{r+1}-r-2.
\]

For each \(r\geq1\), there are exactly \(r+1\) isomorphism types of order \(N_r+1\) with rank at least \(r\): increase the length of one chain of \(U_r\) by one, or add one singleton chain. Their labelled count on a fixed \((N_r+1)\)-element set is \((r+\tfrac12)(N_r+1)!\). Both the minimum and next-to-minimum hosts have rank exactly \(r\).

## Assumptions and scope

A finite \(X=(V,<)\) belongs to \(\mathcal K\) if \(<\) is a strict partial order and comparability-or-equality is an equivalence relation; the equivalence classes are chains, and distinct chains are mutually incomparable. Each chain is nonempty. A marked induced substructure means the literal subset \(F\subseteq V\) with its inherited order, so realizations of a one-point extension must fix \(F\) pointwise. All ranks in this statement are natural-number ranks of finite hosts; they are not first-order quantifier ranks or ranks of infinite orders.

Use the Kubiś–Shelah/López-Callejas–Navarro-Castillo recursion: \(\operatorname{rk}_X(F)\geq0\) always, while \(\operatorname{rk}_X(F)\geq r+1\) means that **for every** admissible one-point extension type \(B\) of \(F\), there exists a realization \(F\cup\{x\}\subseteq X\) over \(F\) with \(\operatorname{rk}_X(F\cup\{x\})\geq r\). The ordinary rank is \(\operatorname{rk}(X)=\operatorname{rk}_X(\varnothing)\). An induced embedding must preserve both comparability and incomparability.

## Proof

**0. Universal component-rank composition lemma.** Work in the equivalence-expanded class \(\mathcal H^{\sqcup}\). A one-point extension of \(F\) either adjoins a point in a new \(E\)-class (one possible singleton type, by hypothesis), or chooses one occupied \(E\)-class and one admissible local \(\mathcal H\)-extension type. Induct on \(r\). The assertion is vacuous for \(r=0\). If rank is at least \(r\), challenge by an arbitrary extension in any occupied class; the global rank-\(r-1\) response has local rank at least \(r-1\) there, giving \(a_C\geq r\) by the local rank definition. Challenge instead by a new singleton class. The successful response chooses a vertex in some unused class \(D\), whose resulting local marked rank is at least \(r-1\); therefore its original local host rank is at least \(r\). The other unused classes must still dominate the \((r-1,r-2,\ldots,1)\) rank ladder. Sorting shows \(\rho_j\geq r-j+1\) for the first \(r\) unused ranks. Conversely, if the local-rank and sorted ladder conditions hold, each occupied-class type has a local response of rank at least \(r-1\), while a fresh-component type can be realized inside an unused class of largest local rank at least \(r\), leaving the remaining ranks at least \(r-1,\ldots,1\). In both cases the induction hypothesis makes the global response rank at least \(r-1\). This proves the general lemma in both directions, including the base threshold \(r=1\).

If \(H_j\) is a principal local rank-\(j\) kernel, then an unused component has local rank at least \(j\) precisely when \(H_j\) embeds into it. The staircase criterion at the empty marking is therefore equivalent to the componentwise induced embedding of \(H_r\sqcup\cdots\sqcup H_1\), proving the kernel-transfer assertion. No amalgamation assumption on \(\mathcal H\) is needed for this finite-rank statement.

**Specialization.** For \(\mathcal H\) the class of all finite strict linear orders, the source's interval characterization gives the exact local rank at a marked subset as the minimum over its gaps of \(\lfloor\log_2(g+1)\rfloor\), and local empty-marking rank is \(\lfloor\log_2(m+1)\rfloor\) for a chain of length \(m\). Substitution in the proved *general* component lemma yields the displayed finite-disjoint-chain gap/component criterion and the ensuing universal kernel. For completeness, steps 1–5 below give an independent direct proof in the chain class and of its sharp enumerative consequences.

**1. Classification of prime-extension types.** Because every comparability class is a chain, a fresh vertex in a one-point extension of \(F\) either is incomparable with all of \(F\) (a wholly new chain), or belongs to exactly one occupied component and is inserted into exactly one of the order gaps determined there by marked elements. There are no other types: comparing a fresh vertex to two different components would merge two previously incomparable marked elements into a chain, contradicting preservation of the induced order. Each gap represents a distinct extension type over the pointwise fixed marked elements.

**2. Criterion, inductive necessity.** The \(r=0\) statement has no restrictions. Suppose the criterion holds at threshold \(r-1\), with \(r\geq1\), and \(\operatorname{rk}_X(F)\geq r\). Challenge the rank game by inserting a fresh vertex into any specified occupied gap of size \(g\). A successful response yields two fresh subgaps each of size at least \(L_{r-1}\), by the induction hypothesis; hence \(g\geq 2L_{r-1}+1=L_r\). For the new-component type, a successful response chooses a vertex in a previously unoccupied chain \(C\). The two gaps it creates inside \(C\) have at least \(L_{r-1}\) vertices each, so \(|C|\geq L_r\). The other unoccupied components must simultaneously include chains of sizes at least \(L_{r-1},L_{r-2},\ldots,L_1\). Thus the original unoccupied multiset admits an assignment to all \(r\) thresholds \(L_r,\ldots,L_1\). Since these thresholds are decreasing, the decreasing rearrangement obeys \(m_j\geq L_{r-j+1}\) for \(1\leq j\leq r\). For \(r=1\), the induction's gap and remaining-component constraints are vacuous, and the same argument requires only one available point in one new chain.

**3. Criterion, inductive sufficiency.** Assume all the displayed conditions at threshold \(r\). For an extension into an occupied gap, choose a vertex that leaves at least \(L_{r-1}\) vertices on each side; such a point exists because \(g\geq L_r=2L_{r-1}+1\). Every other gap remains at least \(L_{r-1}\), and the unused-component thresholds for \(r-1\) continue to hold. For the new-component extension, choose a vertex in a longest unoccupied chain, which has size at least \(L_r\); place it leaving at least \(L_{r-1}\) on each side. The remaining unoccupied chains still dominate \(L_{r-1},\ldots,L_1\). In either case the induction hypothesis gives rank at least \(r-1\) for the new position. These are all extension types, so rank is at least \(r\).

**4. Scalar formula.** For any \(r\leq k\), the inequalities \(m_j\geq2^{r-j+1}-1\) are equivalent to \(r\leq j-1+\lfloor\log_2(m_j+1)\rfloor\) for all \(j\leq k\): for \(j>r\) the latter inequality holds automatically. The occupied-gap inequalities are equivalent to \(r\leq\lfloor\log_2(g+1)\rfloor\). Taking their joint largest feasible integer gives the stated minimum. If \(k=0\), the new-chain extension is unavailable and the rank equals zero.

**5. Universal kernel and extremizers.** At \(F=\varnothing\) there are no occupied gaps. The criterion reduces to the existence of \(r\) distinct components with lengths at least \(L_r,\ldots,L_1\), which is exactly the induced-embeddability of \(U_r\). Their total order is at least \(N_r\), with equality only when these are the only components and their lengths equal the thresholds. All thresholds are distinct, so this minimum host is unique up to isomorphism. Adding exactly one vertex gives only \(r\) ways to lengthen one existing component and one way to add a singleton. Distinctness of the powers-of-two-minus-one lengths makes these \(r+1\) types distinct. The labelled count is \((N_r+1)!\) for each lengthening, since all chain sizes remain distinct, and \((N_r+1)!/2\) when a second singleton is added, since exactly two singleton components can be swapped. Finally \(N_{r+1}-N_r=2^{r+1}-1>1\), hence neither the minimum nor next-to-minimum order can support rank \(r+1\).

## Verification

The standalone pure-Python program `check_chainrank.py` compares two separate routines on every partition-shaped host with at most ten vertices and every literal marked subset: one routine evaluates the defining one-point-extension game recursively by enumerating the actual available vertices for every prime-extension type; the other evaluates the closed gap/component criterion. The executed test reported `ALL_CHECKS_OK 66963 marked host configurations (each through 4 thresholds)`. Each configuration was checked at thresholds 0, 1, 2, 3 and 4. A second standalone checker `check_component_rank.py` uses independent direct game recursion for arbitrarily edged finite simple graph components (not ordered chains). It checked `GENERAL_COMPONENT_CHECK_OK 838 marked graph-component positions`, at all thresholds zero through three or the host order, independently evaluating the general component staircase. This is finite corroboration, not the proof for arbitrary order; the latter is the preceding induction. The graph test is not exhaustive for all hereditary relational classes.

For example the first kernel sizes are \(N_1=1\), \(N_2=4\), \(N_3=11\), and \(N_4=26\), corresponding to chain-length multisets \((1)\), \((3,1)\), \((7,3,1)\), \((15,7,3,1)\).

## Relationship to prior work

The rank-capacity decomposition is a general compositional principle: it applies to any hereditary component class with a unique singleton type, not only to linear orders. Taking the component class to be pure finite sets recovers a linear staircase for equivalence relations, whereas finite linear orders produce the **exponential** staircase. Neither specialization alone gives the general transfer assertion; the two-resource induction above supplies the claim and the proof. The original Kubiś–Shelah evolution-rank work gives a general finite-list witness principle, whereas the kernel-transfer assertion here gives one explicit principal witness whenever the base class has principal rank layers.

López-Callejas and Navarro-Castillo (2026, §§2 and 6) introduce the relevant one-point-extension rank and prove \(\lfloor\log_2(n+1)\rfloor\) for a single finite linear order. Their interval characterization supplies the one-dimensional antecedent, but no component-demand criterion for finite *unions* of independent chains; a single long chain has rank zero in the present class because it lacks a fresh incomparable component. Macpherson's survey (2011, §2.2) identifies finite disjoint unions of chains as ages of standard homogeneous posets. A separately indexed finite-disjoint-chain result concerns unrestricted-depth fixed-variable first-order equivalence, not the present one-host game rank; an indexed rank-three count for finite direct sums of at most three chains likewise concerns first-order theories. Neither description directly implies the simultaneous gap/component theorem. Full text of the two indexed comparisons was not accessible during this review; historical priority remains provisional.

## Limitations

The general component theorem is for **finite** hosts of hereditary classes with a unique singleton type and a named equivalence partition; it is not asserted for arbitrary amalgamation constructions or multiple singleton types. Its detailed numerical classification is for **finite** independent strict chains, not arbitrary finite posets, coloured chains, infinite hosts or transfinite ranks. The rank is evaluated with a literal fixed marked subset, not an arbitrary variable embedding. The numerical test covers only ten host vertices and thresholds at most four; no inference about the infinite range relies on that test. The originality assessment is based on accessible primary work, indexed comparisons and recorded searches, rather than a complete review of all historic literature. No independent external mathematical audit has been performed.

## References

1. C. López-Callejas and J. Navarro-Castillo, *A rank function for Fraïssé classes and the rank property*, arXiv:2604.14461v1, 15 April 2026. https://arxiv.org/html/2604.14461v1
2. D. Macpherson, *A survey of homogeneous structures*, January 2011, §2.2. https://paperzz.com/doc/9426993/a-survey-of-homogeneous-structures
3. *Exact fixed-variable theories of finite disjoint unions of chains*, indexed research record, 2026. The accessible description concerns fixed-variable first-order equivalence; full document not inspected.
4. *Exactly 102 rank-three theories of finite direct sums of at most three chains*, indexed research record, 2026. The accessible description concerns Ehrenfeucht–Fraïssé quantifier-rank theories; full document not inspected.
