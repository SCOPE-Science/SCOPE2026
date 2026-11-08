# Two-sample binary contextuality on graphs: a complete census and a sharp fraction threshold

## Finding

Let \(G=(V,E)\) be a finite labelled simple graph, with \(n=|V|\). Contexts are its edges and the isolated singleton vertices, and each measurement has outcomes \(\{0,1\}\). A *two-sample empirical model* assigns each context a probability distribution whose entries are integer multiples of \(1/2\), and whose marginals agree on overlaps (no disturbance). Let \(U\subseteq V\) be the set of observables with fair marginal, let \(e(U)=|E(G[U])|\), and let \(c(U)\) be the number of connected components of the induced graph \(G[U]\), counting singleton components and setting \(c(\varnothing)=0\).

There are exactly
\[
N_{\mathrm{ND}}(G)=\sum_{U\subseteq V}2^{n-|U|+e(U)}
\]
labelled no-disturbance models, of which exactly
\[
N_{\mathrm{NC}}(G)=\sum_{U\subseteq V}2^{n-c(U)}
\]
are probabilistically noncontextual (extend to a joint probability distribution on \(\{0,1\}^{V}\)). Every remaining model is *strongly contextual*: it has no global assignment consistent with the support of all contexts. In particular the contextual fraction of **each** two-sample model is either \(0\) or \(1\), with the following exact census of contextual models:
\[
N_{\mathrm{SC}}(G)=\sum_{U\subseteq V}2^{n-c(U)}\left(2^{e(U)-|U|+c(U)}-1\right).
\]
For a graph with no cycles, all models are noncontextual. A graph admits a strongly contextual two-sample model exactly when it has a cycle; the minimum number of fair observables in one is its girth. On a simple cycle with \(k\ge3\) vertices, exactly \(2^{k-1}\) models are strongly contextual. For the four-cycle Bell/CHSH scenario there are \(136\) no-disturbance models, \(128\) noncontextual models and \(8\) strongly contextual models.

The denominator is sharp: when all probabilities are integers, all models are noncontextual; with probabilities in multiples of \(1/3\), a four-cycle admits a contextual model of contextual fraction exactly \(2/3\), neither \(0\) nor \(1\).

## Assumptions and scope

A *context distribution* is normalized and nonnegative. A model has no disturbance if its marginal at every vertex is the same regardless of the context used to measure that vertex. On an isolated vertex, the singleton distribution is part of the model. We count fixed labelled observables and distinguish the two outcome labels. A *global distribution* is an ordinary probability measure on all \(2^n\) assignments whose context marginals reproduce the model. A *global support assignment* is an assignment whose restriction to every context has positive context probability. A model is *strongly contextual* if no such assignment exists. The *noncontextual fraction* is the largest \(\lambda\in[0,1]\) for which the model decomposes as \(\lambda L+(1-\lambda)Q\), with \(L\) a noncontextual model and \(Q\) a no-disturbance model. The *contextual fraction* is \(1-\lambda\). No assumption of quantum realizability or of being an extreme point of a no-signalling polytope is made.

For any \(U\subseteq V\), put \(\beta(U)=e(U)-|U|+c(U)\), the cycle rank of \(G[U]\), and use the empty-graph conventions above. Isolated vertices are included in all formulas.

## Proof

**1. Complete normal form.** A binary distribution whose entries are multiples of \(1/2\) is either a point mass or an equiprobable pair of distinct outcomes. Hence every one-variable marginal is either deterministic or fair. Let \(U\) contain the fair variables. For an edge with both endpoints fair, the only possible joint tables are
\[
\tfrac12(\delta_{00}+\delta_{11})\quad\text{and}\quad
\tfrac12(\delta_{01}+\delta_{10}),
\]
namely the equality and inequality tables. Indeed, the two nonzero pair outcomes must each occur once and must have opposite first and opposite second coordinates. Write \(s_{uv}\in\mathbf F_2\) for the corresponding equation \(x_u\oplus x_v=s_{uv}\). If exactly one endpoint is deterministic, the table is uniquely fixed by that bit and the fair marginal of the other endpoint; if both endpoints are deterministic the table is a point mass. Thus every no-disturbance model is represented *uniquely* by a triple \((U,b,s)\), where \(b:V\setminus U\to\{0,1\}\) assigns the deterministic outcomes, and \(s:E(G[U])\to\{0,1\}\) assigns parity to each fair–fair edge. Conversely every such triple defines a normalized no-disturbance model, including singleton contexts at isolated vertices. There are exactly \(2^{n-|U|+e(U)}\) triples with fixed \(U\). Summing proves the first formula.

**2. Locality and all-or-nothing contextuality.** A global support assignment must coincide with \(b\) outside \(U\) and solve
\[
x_u\oplus x_v=s_{uv}\qquad(uv\in E(G[U])).
\]
Such a solution exists if and only if every cycle of \(G[U]\) has even mod-two sum of signs. The necessity follows by summing edge equations around a cycle; for sufficiency, select a root in each component, assign it an arbitrary bit, and propagate through a spanning tree. Vanishing cycle sums guarantee the remaining edges agree. This is the classical *balanced signed graph* / \(\mathbf F_2\)-coboundary criterion, not an originality claim here.

If the signs are balanced, select one independent fair root bit per connected component, propagate all other fair variables, and fix all deterministic variables at \(b\). This defines a global distribution with the required edge and isolated-vertex marginals: within any component each vertex is fair, and each fair–fair edge is supported equally on its two parity-compatible outcomes. Thus the model is noncontextual. Conversely, any global joint distribution would have support consisting of global support assignments, so an unbalanced signing is not noncontextual. If the signing is unbalanced, *no* global support assignment exists; every positive weight placed on a noncontextual component would put positive weight on a global support assignment and contradict the zero entries in some context. Consequently the noncontextual fraction is \(0\). If balanced, it is \(1\). This proves the claimed \(\{0,1\}\) contextual-fraction dichotomy.

**3. Exact counts and graph threshold.** For fixed \(U\), the signings with zero cycle sums are the image of the \(\mathbf F_2\)-linear map \(\partial:C^0(G[U];\mathbf F_2)\to C^1(G[U];\mathbf F_2)\), \((\partial x)_{uv}=x_u+x_v\). Its kernel consists of one constant per connected component, so the image has dimension \(|U|-c(U)\). Thus precisely \(2^{|U|-c(U)}\) signings are balanced. Multiplication by the \(2^{n-|U|}\) choices of deterministic bits gives \(2^{n-c(U)}\) noncontextual models at fixed \(U\), proving the second formula and hence the third.

If \(G\) is a forest, every induced graph has cycle rank zero, so all signings are balanced. If \(G\) has a cycle, choose \(U\) to be the vertices of a shortest cycle, assign signs whose parity around this cycle is odd, and fix the other variables; the resulting model is strongly contextual. Any unbalanced signing needs at least one cycle in \(G[U]\), hence at least the girth many fair vertices. For a simple cycle on \(k\) vertices, every proper induced subgraph is a forest, and only \(U=V\) contributes strongly contextual models: exactly half the \(2^k\) edge signings are unbalanced, giving \(2^{k-1}\). For \(C_4\), the direct finite sum gives \(N_{\mathrm{ND}}=136\), \(N_{\mathrm{NC}}=128\).

**4. Sharp denominator-three contrast.** On the four-cycle with observables \(A_0,A_1,B_0,B_1\) and contexts \((A_i,B_j)\), take the first three tables \((i,j)\ne(1,1)\) to have \(P(00)=2/3\) and \(P(11)=1/3\), and the fourth table to have \(P(00)=P(01)=P(10)=1/3\), \(P(11)=0\). Every observable has marginal \(P(1)=1/3\), so these tables have no disturbance. They equal a mixture of the deterministic all-zero model of weight \(1/3\) and the standard parity-odd PR-box model of weight \(2/3\) (first three contexts demand equality and the fourth inequality). This gives a noncontextual fraction at least \(1/3\). Conversely the support of the first three tables forces every global support assignment to set all four variables equal. The fourth table forbids the all-one assignment, so only all-zero is permitted globally. Its event \(00\) has fourth-context probability \(1/3\); hence any noncontextual subdistribution dominated contextwise by the model has total mass at most \(1/3\). Therefore the contextual fraction is exactly \(2/3\). With denominator one, each context is deterministic and consistency forces a single global assignment, proving sharpness.

## Verification

The standalone checker \(\texttt{check\_half\_integral.py}\) implements the subset/connected-component formulas and **independently** enumerates all ten unordered pairs of the four binary edge outcomes on each edge (equivalently the ten normalized two-sample edge tables). It checks marginal consistency and whether a global support assignment exists. Its complete outputs are: triangle \((40,36)\); four-cycle \((136,128)\); four-vertex path \((116,116)\); triangle with one pendant edge \((140,124)\); five-cycle \((464,448)\); the ordered pairs are (no-disturbance count, support-extendible count). It ends with \(\texttt{CHECK\_OK}\). The proof, not the finite checker, establishes the all-graph formulas and equivalence of support extension and probabilistic noncontextuality. The denominator-three witness is verified by the explicit distribution and support argument above.

## Relationship to prior work

Le Maguet's 2026 polyteam logic treats local and global dependence, semiring-weighted empirical models and contextuality, expressly leaving computational questions for later work [1]. The signed-cycle consistency criterion is classical and is explicitly connected with XOR games and switching in Gnaciński et al. [2]; it is used here, not rediscovered. Abramsky and Brandenburger [3] provide the general sheaf/global-section framework for contextuality, with no restriction to the two-sample graph case. The present statement adds a complete all-graph finite-precision count, exact counts of both the extendible and strongly contextual strata, and a uniform contextual-fraction dichotomy with a sharp denominator-three counterexample. The newer quantitative contextual-fraction analysis [4] concerns different uniform higher-arity relational lifts and hard global packing problems, not the two-sample pairwise graph census. The formulas might admit reformulations through known graphical partition polynomials; this is an explicit priority risk, rather than evidence of uniqueness.

## Limitations

The contexts are graph edges and isolated singletons, the outcomes are binary, the graph is simple and finite, and all probabilities lie in the indicated finite-denominator grid. The counts distinguish labels and outcome bit names. Noncontextuality is ordinary probability-global-section noncontextuality, not a statement about quantum realizability. The two-sample all-or-nothing property fails already at denominator three. No classification is asserted for hypergraph contexts, higher outcome alphabets, or larger denominators. Historical priority and independent verification beyond the inspected literature are not established.

## References

[1] Loan Le Maguet, *Polyteam logics for quantum contextuality*, arXiv:2611.00814v1, first posted 2026-10-31. https://arxiv.org/abs/2611.00814

[2] Piotr Gnaciński, Monika Rosicka, Ravishankar Ramanathan, Karol Horodecki, Michał Horodecki, Paweł Horodecki, Simone Severini, *Linear game non-contextuality and Bell inequalities - a graph-theoretic approach*, arXiv:1511.05415v1, first posted 2015-11-17. https://arxiv.org/abs/1511.05415

[3] Samson Abramsky and Adam Brandenburger, *The sheaf-theoretic structure of non-locality and contextuality*, arXiv:1102.0264, 2011. https://arxiv.org/abs/1102.0264

[4] Ronald Katende, *Contextual Fraction Beyond Satisfiability: Pure NAE Completeness, Exact Orbit Packings, and Width Barriers*, arXiv:2609.20281. https://arxiv.org/abs/2609.20281
