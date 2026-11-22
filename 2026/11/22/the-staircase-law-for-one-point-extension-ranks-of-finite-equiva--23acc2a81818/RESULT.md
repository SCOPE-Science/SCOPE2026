# The staircase law for one-point-extension ranks of finite equivalence relations

## Finding

Let \(\mathcal E\) be the hereditary class of all finite structures with one binary equivalence relation, including the empty structure. Equip \(\mathcal E\) with the one-point-extension rank of López-Callejas and Navarro-Castillo [1, Definition 2.3]. For a finite \(X\in\mathcal E\), with its equivalence-class cardinalities written \(\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_b\ge1\), its exact rank is

\[
\operatorname{rk}(X)=\max\bigl\{t\in\mathbb N_0:b\ge t\ \text{and}\ \lambda_j\ge t-j+1\text{ for }1\le j\le t\bigr\}.
\]

Equivalently, its class-size Young diagram contains the staircase partition \((t,t-1,\ldots,1)\) precisely when its extension rank is at least \(t\). This is a complete formula for every finite equivalence structure, not merely a family of examples.

The stronger local assertion is as follows. Fix any induced substructure \(F\subseteq X\). For each equivalence class \(C\) meeting \(F\), put \(c_C=|C\setminus F|\). List the sizes of all equivalence classes disjoint from \(F\) as \(b_1\ge\cdots\ge b_u\ge1\). For every \(t\in\mathbb N_0\),

\[
\operatorname{rk}_X(F)\ge t\ \Longleftrightarrow\
\bigl(\forall C\cap F\ne\varnothing,\ c_C\ge t\bigr)
\ \land\ \bigl(u\ge t\ \land\ \forall j\in\{1,\ldots,t\},\ b_j\ge t-j+1\bigr).
\]

At \(t=0\), both conditions on the right are vacuous. As a sharp extremal consequence, the smallest number of points in any rank-\(t\) structure is \(t(t+1)/2\). At that size the unique isomorphism type has class sizes \((t,t-1,\ldots,1)\), with exactly \((t(t+1)/2)!/\prod_{j=1}^{t}j!\) labelled realizations. For each \(n\ge0\), the largest possible rank among structures on \(n\) points is \(\lfloor(\sqrt{8n+1}-1)/2\rfloor\).

## Assumptions and scope

A finite equivalence relation is a finite set together with a reflexive, symmetric and transitive binary relation; embeddings preserve and reflect the relation, so substructures are induced. The empty structure is permitted. A *prime extension* of \(F\) is an induced extension by one new point, with no restriction on how large the ambient finite extension could otherwise be. Thus one may add a point to any represented equivalence class or start an entirely new class. This rank is not first-order quantifier rank, the partition lattice rank, or the \(K\)-rank of partial types [3].

Rank is defined recursively: \(\operatorname{rk}_X(F)\ge0\); for an integer \(s\ge0\), \(\operatorname{rk}_X(F)\ge s+1\) when every abstract prime-extension type of \(F\) in \(\mathcal E\) has a realization \(F\cup\{v\}\subseteq X\) with rank at least \(s\). The standard definition uses all ordinals, with the condition at limits, but any finite \(X\) has rank at most \(|X|\), so the finite recursion is exhaustive here. The rank of the structure is \(\operatorname{rk}(X)=\operatorname{rk}_X(\varnothing)\).

## Proof

**Local staircase lemma.** We prove the displayed characterization by induction on the nonnegative integer \(t\).

For \(t=0\) it is tautological. Suppose the result holds at \(t-1\), and fix \(t\ge1\). Every prime extension of \(F\) is of one of just two sorts: (i) add a new point equivalent to one of the equivalence classes meeting \(F\), or (ii) add a point in a class new to \(F\).

For necessity, assume \(\operatorname{rk}_X(F)\ge t\). For each class \(C\) meeting \(F\), consider the prime extension which adds a point to that class. It must admit a realization of rank at least \(t-1\). The induction hypothesis applied to this realization forces the residual capacity of \(C\), after adding that point, to be at least \(t-1\). Hence \(c_C\ge t\), for *each* represented class.

Next choose the abstract prime extension which starts a new class. A realization of rank at least \(t-1\) selects some previously untouched class \(D\) of size at least \(t\): after one point of \(D\) is used, its remaining capacity must be at least \(t-1\). The other previously untouched classes, by the induction hypothesis, contain a staircase of lengths \((t-1,t-2,\ldots,1)\). Consequently the original multiset of untouched sizes contains \((t,t-1,\ldots,1)\) componentwise when sorted in decreasing order. This is exactly \(u\ge t\) and \(b_j\ge t-j+1\) for \(1\le j\le t\).

For sufficiency, assume all listed conditions. Consider any abstract prime extension of \(F\). If it adds to an already represented class \(C\), choose any available point of that class. The residual capacity of \(C\) decreases from at least \(t\) to at least \(t-1\), the other represented capacities remain at least \(t\), and untouched classes still contain the smaller staircase \((t-1,\ldots,1)\). Thus the new substructure has rank at least \(t-1\) by induction. If the extension starts a new class, choose a point from a largest untouched class \(D\). Its size is at least \(t\), leaving at least \(t-1\) points of that represented class, and removal of this largest class leaves untouched sizes satisfying \(b_{j+1}\ge(t-1)-j+1\) for each \(1\le j\le t-1\). All previously represented classes still have at least \(t\) unused points. By induction this realization has rank at least \(t-1\). Both types of one-point extension can therefore be met, proving \(\operatorname{rk}_X(F)\ge t\).

Taking \(F=\varnothing\) yields the first formula. Rank is finite because each realized prime extension uses a fresh point and a finite structure cannot sustain more than \(|X|\) successive moves.

**Sharp minimum and classification.** Rank at least \(t\) forces at least \(t\) classes of sizes at least \(t,t-1,\ldots,1\), so the total order is at least \(t(t+1)/2\). Equality forces *exactly* that descending class-size partition; conversely it satisfies the staircase test and has rank exactly \(t\) because it has only \(t\) classes. The class sizes are pairwise distinct, so the number of equivalence relations on a fixed labelled ground set of this order is the multinomial \((t(t+1)/2)!/\prod_{j=1}^t j!\). The maximal-rank statement on \(n\) points follows from this threshold, with equality realized by enlarging the first block of the rank-\(t\) staircase to use any extra points; the number of classes remains \(t\), preventing rank \(t+1\). The empty case has rank zero.

## Verification

The accompanying standalone `verify.py` implements the literal minimax semantics of prime extensions: for every induced substructure \(F\) it enumerates all abstract types (join each represented equivalence class or introduce a new class), computes the maximum rank among concrete realizations of each type, and takes the minimum over types. This procedure does not use the staircase recurrence. It was compared against the proposed closed criterion on **all 5,296 set partitions of orders zero through eight**, and on **every induced substructure** of each, totaling **1,187,043** cases. Every result agreed. The script also checks the extremal staircase arithmetic for the first eight ranks. Run with `python verify.py` using standard Python only. These tests are finite corroboration; the preceding induction is the proof for all finite orders.

## Relationship to prior work

López-Callejas and Navarro-Castillo [1] establish the underlying rank definition, analyze its behavior for general Fraïssé classes, prove the rank property for suitable free-amalgamation classes and tournaments, and compute ranks for finite and countable linear orders. Their linear-order interval formula is a different combinatorial specialization: one-point extensions specify a *gap* rather than a preexisting equivalence class or a new class. The free-amalgamation theorem does not apply directly because the free union of equivalence structures over an overlap can violate transitivity. The present result instead gives a closed formula and extremal-size classification for the non-free-amalgamation age of equivalence relations.

Kubiś and Shelah [2] introduced the rank framework in evolution systems. Guingona and Parnes [3] study a different \(K\)-rank of partial types, including examples based on equivalence relations; the definitions and target invariants differ. Neither general rank definition nor first-order quantifier-rank classifications by themselves imply the displayed finite staircase formula.

## Limitations

Only finite equivalence structures are classified. The theorem does not calculate the transfinite ranks of countably infinite equivalence structures or prove the rank property for their entire age. The formula is for the one-point-extension rank relative to the whole hereditary class of finite equivalence relations, not for graph rank relative to all finite graphs. The literature comparisons establish no claim of absolute historical priority; independent mathematical validation has not been performed.

## References

1. C. López-Callejas and J. Navarro-Castillo, *A rank function for Fraïssé classes and the rank property*, arXiv:2604.14461, first submitted 15 April 2026. https://arxiv.org/html/2604.14461
2. W. Kubiś and S. Shelah, *Evolution systems — an ordinal rank measuring universality*, manuscript dated 19 August 2024. https://users.math.cas.cz/kubis/pdfs/ranksEvasPS_ver2.pdf
3. V. Guingona and M. Parnes, *Ranks Based on Strong Amalgamation Fraïssé Classes*, Archive for Mathematical Logic 62 (2023), 889–929; arXiv:2007.02922. https://arxiv.org/abs/2007.02922
