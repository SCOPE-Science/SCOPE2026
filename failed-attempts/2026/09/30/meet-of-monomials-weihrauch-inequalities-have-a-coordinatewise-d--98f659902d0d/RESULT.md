# Meet-of-monomials Weihrauch inequalities have a coordinatewise dominance normal form
## Finding
Fix \(d\geq 1\) variables \(x_1,\ldots,x_d\). For a nonzero vector \(\alpha=(\alpha_1,\ldots,\alpha_d)\in\mathbb N^d\), let \(M_\alpha\) be the Weihrauch term obtained by taking \(\alpha_i\) product-copies of \(x_i\) for every \(i\), omitting coordinates with exponent \(0\). For a finite nonempty set \(A\subseteq\mathbb N^d\setminus\{0\}\), define
\[
T_A=\mathop{\bigsqcap}_{\alpha\in A}M_\alpha.
\]
For finite nonempty \(A,B\subseteq\mathbb N^d\setminus\{0\}\), the universal pointed-degree inequality
\[
T_A\leq_{\bullet}T_B
\]
holds exactly when
\[
\forall\beta\in B\ \exists\alpha\in A\quad
\alpha_i\leq\beta_i\text{ for every }i.
\]
The universal ordinary Weihrauch inequality
\[
T_A\leq T_B
\]
holds exactly when the same coordinatewise-dominance condition holds and
\[
\operatorname{supp}(B)\subseteq\operatorname{supp}(A),
\]
where
\[
\operatorname{supp}(A)=\{i:\exists\alpha\in A\ (\alpha_i>0)\}.
\]
The same ordinary criterion also characterizes universal validity over strong Weihrauch degrees.

Consequently, if \(\operatorname{Min}(A)\) denotes the coordinatewise-minimal members of \(A\), then
\[
T_A\equiv_{\bullet}T_B
\quad\Longleftrightarrow\quad
\operatorname{Min}(A)=\operatorname{Min}(B),
\]
whereas ordinary and strong universal equivalence hold exactly when
\[
\operatorname{Min}(A)=\operatorname{Min}(B)
\quad\text{and}\quad
\operatorname{supp}(A)=\operatorname{supp}(B).
\]
Thus the pointed fragment has a canonical finite-antichain invariant, and the ordinary/strong fragment has the same invariant together with total variable support.

Given the exponent vectors explicitly, a universal inequality is decidable using \(O(|A||B|d)\) coordinate comparisons, plus a linear support scan in the ordinary/strong case. Canonicalization by deleting dominated vectors is polynomial-time. This is a tractable fragment inside the general \((\sqcap,\times)\) universal-validity problem, which is known to be \(\Sigma^p_2\)-complete.

## Assumptions and scope
The terms contain only finite products of variables and finite meets of those monomials. The sets \(A\) and \(B\) are finite and nonempty, and every exponent vector is nonzero, so no convention for an empty product or empty graph component is needed.

The notation \(\leq_{\bullet}\) refers to universal validity when variables range over pointed Weihrauch degrees, as in the cited source. The ordinary and strong statements concern universal validity over ordinary and strong Weihrauch degrees, respectively.

Complexity is measured in the explicit exponent-vector representation. An integer comparison has the usual bit cost when exponents are binary encoded, so the stated comparison bound yields polynomial time in the ordinary bit model.

## Proof
The cited graph characterization interprets a variable as one colored vertex, meet as disjoint union, and product as graph join. Therefore the graph of \(M_\alpha\) is a clique \(C_\alpha\) containing exactly \(\alpha_i\) vertices of color \(x_i\), and the graph of \(T_A\) is the disjoint union of the cliques \(C_\alpha\) for \(\alpha\in A\). Its maximal cliques are exactly those components.

For pointed universal validity, the graph theorem asks for a partial color-preserving map from the vertices of the graph of \(T_B\) to the vertices of the graph of \(T_A\) such that the image of every maximal clique on the right contains a maximal clique on the left.

Fix \(\beta\in B\). If the image of \(C_\beta\) contains \(C_\alpha\), then for every color \(x_i\), at least \(\alpha_i\) distinct vertices of color \(x_i\) must occur in \(C_\beta\). Hence \(\alpha_i\leq\beta_i\) for every \(i\). This proves necessity.

Conversely, suppose that for every \(\beta\in B\) some \(\alpha\in A\) satisfies \(\alpha\leq\beta\) coordinatewise. For each color \(x_i\), select \(\alpha_i\) vertices of \(C_\beta\) and map them bijectively onto the \(\alpha_i\) vertices of color \(x_i\) in \(C_\alpha\). Leave every remaining vertex of \(C_\beta\) undefined. Doing this independently for each component gives a partial color-preserving map whose image of every \(C_\beta\) contains a whole maximal clique \(C_\alpha\). The graph theorem therefore yields
\[
T_A\leq_{\bullet}T_B.
\]

For ordinary universal validity the graph map must be total. The preceding dominance condition is still necessary. Totality additionally forces every color appearing anywhere in the graph of \(T_B\) to have a same-colored target vertex somewhere in the graph of \(T_A\), which is exactly
\[
\operatorname{supp}(B)\subseteq\operatorname{supp}(A).
\]
This support condition is also sufficient: perform the componentwise mapping just constructed, and send each leftover right-hand vertex to any left-hand vertex of the same color. No adjacency preservation is required by the reduction notion, so these extra assignments do not disturb the already covered maximal clique. Hence the ordinary criterion follows.

The source proves that the equational theories of ordinary and strong Weihrauch degrees coincide for the signature \((\sqcap,\times)\). Since an inequality is expressible as a meet equation, the same criterion characterizes universal validity in the strong degrees.

For the canonical form, define the upward closure
\[
\uparrow A=\{\gamma\in\mathbb N^d:\exists\alpha\in A\ (\alpha\leq\gamma)\}.
\]
The pointed criterion is equivalent to
\[
\uparrow B\subseteq\uparrow A.
\]
Thus pointed equivalence is exactly equality of the two upward closures. Every finitely generated coordinatewise upward-closed subset of \(\mathbb N^d\) has its unique finite set of minimal generators, namely \(\operatorname{Min}(A)\). Therefore pointed equivalence is equivalent to equality of the minimal antichains. Mutual ordinary validity adds the two support inclusions, hence support equality. The strong statement follows from the same equational-theory coincidence.

The decision algorithm directly tests, for every \(\beta\in B\), whether some \(\alpha\in A\) is coordinatewise at most \(\beta\), requiring at most \(|A||B|d\) coordinate comparisons. Computing supports and deleting dominated generators are also polynomial-time operations.

## Verification
The proof was reconstructed directly from the current graph-reduction theorem rather than from the withdrawn proposition noted in the first preprint version. The direction of the graph map, the maximal-clique condition, and the distinction between partial pointed maps and total ordinary maps were checked explicitly.

A finite exhaustive sanity check is included as `verify.py`. It generates all nonzero two-coordinate exponent vectors with entries at most \(2\) and total size at most \(3\), forms every one- or two-component family within a small total-vertex budget, enumerates all color-preserving partial and total maps, and compares exact graph reducibility with the stated dominance-and-support criterion. It checks \(1242\) pointed/ordinary cases and terminates with `VERIFY_OK 1242`.

Two edge cases were checked separately in the proof. A color can occur only in a dominated, nonminimal monomial; this does not change pointed equivalence but can change ordinary equivalence, which is why total support must be retained. Repeated product factors of the same color require distinct source vertices to cover the target clique, which is exactly why coordinatewise multiplicity rather than mere support controls the pointed criterion.

## Relationship to prior work
Neumann, Pauly, and Pradic give the general finite-colored-graph characterization of universal inequalities in the Weihrauch signature \((\sqcap,\times)\), distinguish partial reductions for pointed degrees from total reductions for ordinary degrees, prove coincidence with the strong equational theory for this signature, and show that the unrestricted universal-validity problem is \(\Sigma^p_2\)-complete.

The result here specializes their graph theorem to finite meets of pure product monomials. In this class the term graphs collapse to disjoint unions of colored cliques, so the general clique-cover condition becomes coordinatewise domination of exponent vectors. This yields both a canonical antichain invariant and a polynomial-time decision procedure for the fragment.

## Limitations
The theorem does not cover terms in which meet occurs inside a product, terms using join or finite parallelization, the constant \(1\), empty meets, or empty products. Those operations can create cographs that are not simply disjoint unions of the monomial cliques used here.

The polynomial-time statement is for the explicit exponent-vector representation and does not contradict the \(\Sigma^p_2\)-completeness of unrestricted \((\sqcap,\times)\) universal validity.

The ordinary canonical invariant needs both the minimal exponent antichain and the full variable support. Discarding dominated monomials alone can erase a color needed for total reductions.

The originality assessment is best-of-knowledge. The general graph theorem is published as a preprint result; targeted searches did not locate this coordinatewise dominance normal form or its canonical-antichain consequence as a separately stated result.

## References
Eike Neumann, Arno Pauly, and Cécilia Pradic, “The equational theory of the Weihrauch lattice with multiplication,” arXiv:2403.13975v2. First public version submitted 20 March 2024; current version dated 4 September 2024. The current version removes a false proposition from the first version; the present argument uses the retained graph characterization of universal validity.
