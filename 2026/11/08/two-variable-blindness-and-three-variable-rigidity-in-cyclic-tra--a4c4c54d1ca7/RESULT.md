# Two-variable blindness and three-variable rigidity in cyclic transitive-block tournaments

## Finding

Let \(C_3\) denote the directed triangle \(0\to1\to2\to0\). For positive integers \(a,b,c\), let \(T(a,b,c)\) be the tournament obtained by replacing the three vertices of \(C_3\) by internally **transitive** tournaments of sizes \(a,b,c\), with all arcs between blocks oriented as in \(C_3\). In the pure irreflexive arc language \(\{R\}\), without constants, counting quantifiers or named blocks, the following statements hold for all positive triples.

1. Every two such tournaments satisfy precisely the same sentences of the one- and two-variable fragments of first-order logic, at **all** quantifier depths.
2. For any \(k\ge3\), \(T(a,b,c)\equiv_{\mathrm{FO}^{k}}T(a',b',c')\) if and only if \((a',b',c')\) is a cyclic rotation of \((a,b,c)\). In this family, three-variable equivalence is therefore exactly isomorphism; reversing the ordered triple is generally detected.
3. At total order \(N\ge3\), the number of distinct three-variable theories (equivalently, isomorphism types) is
\[
\frac13\left(\binom{N-1}{2}+2\,\mathbf 1_{3\mid N}\right).
\]
The number of labelled tournaments in the family on a fixed labelled set of \(N\) vertices is
\[
\frac{N!}{3}\binom{N-1}{2}.
\]
Their automorphism groups are trivial unless \(a=b=c\), in which case the group is cyclic of order three.

## Assumptions and scope

A **tournament** is a finite irreflexive binary structure in which, for each distinct \(x,y\), exactly one of \(R(x,y)\) and \(R(y,x)\) holds. A transitive tournament is a strict total order with arcs directed from smaller to greater. The three substituted blocks in \(T(a,b,c)\) are all nonempty. Only the arc predicate and equality are available to the formulas. The fragment \(\mathrm{FO}^k\) permits at most \(k\) variable **names** but arbitrary reuse and quantifier depth.

The three block sizes are not unary labels and may coincide. A cyclic rotation corresponds to the orientation-preserving automorphism of \(C_3\); a reflection reverses its orientation and is not a permissible relabelling in general.

## Proof

**Step 1: an exact three-variable block predicate.** Write \(\operatorname{Cyc}(x,y,z)\) for
\[
\bigl(R(x,y)\land R(y,z)\land R(z,x)\bigr)\lor
\bigl(R(y,x)\land R(x,z)\land R(z,y)\bigr).
\]
In a lexicographic substitution into \(C_3\) with transitive blocks, a triple induces a directed three-cycle if and only if its three vertices lie in three *distinct* substituted blocks. Indeed, a triple contained in one block is transitive; when two vertices are in the same block and the third is elsewhere, those two vertices have identically oriented arcs to the third; and one vertex from each block forms a directed cycle. Since every block is nonempty, for distinct vertices \(x,y\), a vertex \(z\) making \(\operatorname{Cyc}(x,y,z)\) exists if and only if \(x,y\) lie in *different* blocks. Hence the following uses three variable names and defines the equivalence relation of belonging to the same block:
\[
S(x,y)\;:=\; x=y\ \lor\ \neg\exists z\,\operatorname{Cyc}(x,y,z).
\]
Consequently \(D(x,y):=S(x,y)\land R(x,y)\) defines the strict total order *within* each block.

**Step 2: exact unbounded block-size tests in three variables.** For every fixed integer \(h\ge0\), define a unary formula \(P_h(u)\) expressing that there is a \(D\)-directed path of length \(h\) starting at \(u\); take \(P_0(u)\) to be \(u=u\), and recursively use \(P_{h+1}(u)=\exists v\,[D(u,v)\land P_h(v)]\). The recurrence is a **variable-name schema**, not an instruction to retain new names: at each nesting, alpha-rename its bound variables, cycling through the names \(x,y,z\). The only free name inside each unary subformula is its stated argument, while the third name in the definition of \(D\) is bound locally by \(S\). Thus every expanded instance has at most the three names \(x,y,z\), independent of \(h\). As \(D\) is a strict finite total order in each block, \(P_h(u)\) holds precisely when at least \(h\) vertices occur later than \(u\) in its own block.

For each integer \(h\ge1\), define the three-variable unary formula
\[
\operatorname{AtLeast}_h(u):=\exists v\,[S(u,v)\land P_{h-1}(v)].
\]
It holds exactly if the block of \(u\) has cardinality at least \(h\). Therefore \(\operatorname{Exactly}_h(u):=\operatorname{AtLeast}_h(u)\land\neg\operatorname{AtLeast}_{h+1}(u)\) defines vertices in a block of cardinality exactly \(h\). All quantifier-bound variables in separate conjuncts can be locally shadowed; none requires a fourth variable name.

**Step 3: three-variable separation.** For any positive \(a,b,c\), consider the sentence
\[
\begin{aligned}
\Phi_{a,b,c}:=\exists x\exists y\exists z\,[&R(x,y)\land R(y,z)\land R(z,x)\\
&\land\operatorname{Exactly}_a(x)\land\operatorname{Exactly}_b(y)\land\operatorname{Exactly}_c(z)].
\end{aligned}
\]
The outer three vertices must occur, in oriented cyclic order, in the three distinct blocks. The sentence therefore holds in \(T(a',b',c')\) if and only if the ordered triple \((a,b,c)\) is one of the three cyclic rotations of \((a',b',c')\). The three uses of \(\operatorname{Exactly}\) occur in separate scopes, and local bound names may shadow outer names without capturing the displayed free argument. This proves that inequivalent cyclic triples are separated within \(\mathrm{FO}^3\). Conversely, cyclic rotation yields an isomorphism, proving the equivalence for all \(k\ge3\).

**Step 4: permanent two-pebble strategy.** Every vertex of \(T(a,b,c)\) has both an incoming and an outgoing neighbor, because each of the two *other* nonempty blocks supplies one entire direction. Consider the standard two-pebble game on any two loopless tournaments in which every vertex has both types of neighbor. With no remaining pebble, Duplicator may respond arbitrarily. With one remaining paired pebble, if Spoiler selects that vertex, Duplicator does the same; otherwise Spoiler's selected vertex is either an in-neighbor or an out-neighbor of the remaining vertex. Duplicator chooses a corresponding neighbor of the paired vertex, which exists by hypothesis. Equality and arc orientation are preserved after every move, for an arbitrary number of rounds. Thus the two tournaments satisfy the same \(\mathrm{FO}^2\) sentences at all quantifier depths. One-variable equivalence follows immediately.

**Step 5: enumeration and automorphisms.** Positive ordered compositions \(a+b+c=N\) are counted by \(\binom{N-1}{2}\). The rotation group \(C_3\) acts on the ordered triples, and each nonidentity rotation fixes exactly the equal-size triple, which exists precisely when \(3\mid N\). Burnside's lemma gives the stated orbit count. For labelled tournaments, for each ordered triple of block sizes one may partition the labelled set into the three ordered blocks and linearly order each block in precisely \(N!\) ways. Every labelled tournament of this family is represented by exactly the three cyclic rotations of its three *intrinsically definable* blocks; hence the count \(N!\binom{N-1}{2}/3\). The within-block orders have no nontrivial automorphisms, and the only possible nonidentity block automorphism is the threefold cyclic rotation when all three sizes match. This proves the stated group description.

## Verification

The standalone program `tournament_logic_refinement.py` constructs one tournament for each of the twenty cyclic-rotation classes of positive triples with total size between three and eight. It computes exact, counting-free, simultaneous finite-variable logical types by refining ordered tuple types with *sets* of replacement types, not multiplicity counts. The stabilized sentence types match the theorem for widths two and three: one type at width two, twenty types at width three. It checks all four hundred ordered graph pairs.

Independently, `tournament_formula_check.py` tests 364 ordered positive triples of orders three through fourteen, verifying the same-block/three-cycle characterization, all local block-size thresholds, orbit counts, and the labelled tournament count by direct census through six vertices. The precise finite-test totals and commands appear in the adjacent verification document and output files. These finite experiments corroborate but do not replace the all-orders proof above.

## Relationship to prior work

The classical \(C_3\)-structure of a tournament records its directed three-cycles and is central to Boussaïri, Ille, Lopez and Thomassé (2004). Their interval-inversion and decomposition results motivate the three-cycle block predicate here; they do not state the unrestricted finite-variable dichotomy, three-variable separating sentences, or exact theory spectrum for cyclic substitutions of three transitive tournaments. In particular, a three-cycle hypergraph discards internal linear orders, while the present formulas additionally recover the sizes of those orders.

Achour, Boudabbous and Boussairi (2012) study tournament reconstruction under vertex deletions, and Liu (2012) studies structural decompositions of \(U_5\)-free tournaments; neither inspected statement implies this variable-width theorem. Dawar and Holm (2012) establish general finite-variable pebble-game machinery, without supplying this family's exact theory classification. Geniet and Thomassé (2022) investigate first-order methods and twin-width for tournament classes, rather than this precise three-block unrestricted-depth spectrum. The novelty comparison is qualified: a stronger, differently phrased earlier composition theorem may exist, and historical priority is not independently certified.

## Limitations

Only the designated family of nonempty *transitive* substitutions into a directed triangle is classified; arbitrary lexicographic substitutions, empty blocks, named blocks, counting logic, and logics with additional numerical predicates are excluded. The result treats unrestricted quantifier depth at fixed variable width, not minimum quantifier rank or formula-size complexity. The all-orders proof is mathematical; finite scripts cannot establish the infinite statements by themselves. Independent mathematical validation and an exhaustive historical-priority review have not been performed. The 2004 source predates the earliest exact-day primary seed cited in metadata; its earliest public calendar day was not verified and has not been invented.

## References

1. Boussaïri, Ille, Lopez and Thomassé, *The C3-structure of the tournaments*, *Discrete Mathematics* 277 (2004), 29–43, DOI: `10.1016/S0012-365X(03)00244-9`. Author-accessible full text: `https://perso.ens-lyon.fr/stephan.thomasse/liste/bilt.pdf`.
2. Achour, Boudabbous and Boussairi, *The {-3}-reconstruction and the {-3}-self duality of tournaments*, `arXiv:1204.2513`, initially public 2012-04-11.
3. Dawar and Holm, *Pebble Games with Algebraic Rules*, `arXiv:1205.0913`, initially public 2012-05-04.
4. Liu, *Structure theorem for U5-free tournaments*, `arXiv:1208.0398`, initially public 2012-08-02.
5. Geniet and Thomassé, *First Order Logic and Twin-Width in Tournaments and Dense Oriented Graphs*, `arXiv:2207.07683`, initially public 2022-07-15.
