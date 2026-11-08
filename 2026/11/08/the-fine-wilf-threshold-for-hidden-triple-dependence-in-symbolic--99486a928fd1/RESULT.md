# The Fine–Wilf threshold for hidden triple dependence in symbolic self-returns

## Finding
Let \(q\ge2\) be an integer and let \(X=(X_i)_{i\ge0}\) be independent uniformly distributed symbols in \(\{0,\ldots,q-1\}\). For integers \(k\ge1\) and \(n\ge k\), write
\[
E_n(k)=\{X_i=X_{i+n}\text{ for every }0\le i<k\}.
\]
These are the exact length-\(k\) symbolic recurrence events of the one-sided full shift \(\sigma\) back to the initial point.

**Theorem (all three-time returns).** Every two distinct events \(E_n(k)\), \(E_m(k)\) are independent and each has probability \(q^{-k}\). For arbitrary \(k\le n_1<n_2<n_3\), define \(a=n_2-n_1\), \(b=n_3-n_2\), and \(g=\gcd(a,b)\). Then
\[
\Pr\bigl(E_{n_1}(k)\cap E_{n_2}(k)\cap E_{n_3}(k)\bigr)
=q^{-3k+\max(0,k-a-b+g)}.
\]
Thus three return indicators are mutually independent **if and only if** \(k\le a+b-g\). Above that threshold, the joint event is enhanced by the exact factor \(q^{k-a-b+g}\) relative to the product of its three marginals. Equivalently, the mixed third centered moment is
\[
\mathbb E\prod_{j=1}^3\bigl(\mathbf1_{E_{n_j}(k)}-q^{-k}\bigr)
=q^{-3k}\bigl(q^{\max(0,k-a-b+g)}-1\bigr).
\]
For equally spaced visits \(n,n+d,n+2d\), the enhancement is \(q^{\max(0,k-d)}\): two-time statistics remain independent, yet three-time dependence appears as soon as \(k>d\).

**Any-order companion.** For distinct times \(k\le n_1<\cdots<n_t\), make a finite undirected multigraph \(G\) with vertex set the union of the initial \(k\)-block and all translated \(k\)-blocks; for every \(j\) and \(0\le i<k\) draw an edge \(i\leftrightarrow i+n_j\). If \(V\) is the vertex count, \(c\) the number of connected components, and \(E=tk\) the edge count, then
\[
\Pr\Bigl(\bigcap_{j=1}^t E_{n_j}(k)\Bigr)=q^{-(V-c)}=q^{-tk+\beta(G)},\qquad \beta(G)=E-V+c.
\]
The three-time closed form explicitly evaluates this cycle rank for every pair of time gaps.

## Assumptions and scope
The probability law is the uniform product Bernoulli measure, not an arbitrary stationary symbolic measure. Each return time is at least the compared length \(k\), guaranteeing disjointness of the initial block from each translated block; translated blocks may overlap each other. All formulas hold for every integer \(q\ge2\), every \(k\ge1\), and every stated set of times, without an asymptotic limit. Indices begin at zero. The events are returns within the length-\(k\) cylinder of the initial sequence, not first-return events and not returns to an externally fixed word. The threshold uses the strict inequality exactly as written, including the equality boundary.

## Proof
**1. Equality graphs.** The intersection event requires the symbols at endpoints of every edge of \(G\) to be equal. On each of the \(c\) connected components all symbols must have one common value, freely chosen among \(q\) possibilities, while the \(V\) graph vertices originally have \(q^V\) independent assignments. Hence the probability is exactly \(q^{c-V}\). Since \(E=tk\), this is \(q^{-tk+E-V+c}\). This proves the any-order statement with neither independence approximation nor neglected overlapping coordinates.

**2. Two visits.** Let their gap be \(d>0\). The union of translated blocks contains \(U=k+\min(k,d)\) coordinates. Within the initial block, equality of symbols caused by a shared translated coordinate connects indices exactly \(d\) apart. The resulting graph on the initial block is a disjoint union of \(\min(k,d)\) chains, including isolated vertices. Adding a translated vertex does not change the component count after collapsing it to its linked initial indices. Thus \(V=k+U\), \(c=\min(k,d)\), and \(\beta=2k-(k+U)+c=0\). Inserting this in the graph probability gives \(q^{-2k}\), establishing pairwise independence. A single event has \(k\) independent initial–translated equalities and probability \(q^{-k}\).

**3. Three visits: union and projected components.** Write their increasing offsets as \(0,a,a+b\) after subtracting \(n_1\). The translated-block union contains
\[
U=k+\min(k,a)+\min(k,b)
\]
vertices: the second interval adds \(\min(k,a)\) points and the third adds \(\min(k,b)\). A translated vertex shared by two initial indices creates a connection between those indices with difference \(a\), \(b\), or \(a+b\), where the endpoints must lie in \(\{0,\ldots,k-1\}\). A connection of difference \(a+b\) is redundant for components: between \(i\) and \(i+a+b\), the intermediate \(i+a\) lies within the initial block and contributes steps \(a\) then \(b\). Consequently the number \(c\) of connected components of the full equality graph equals the number of components of the graph on \(\{0,\ldots,k-1\}\) with edges of lengths \(a\) and \(b\). By symmetry assume \(a\le b\).

If \(k\le b\), no edge of length \(b\) occurs. Edges of length \(a\) form \(\min(k,a)\) chains, so \(c=\min(k,a)\). The formula for \(U\) then gives \(\beta=3k-(k+U)+c=0\).

If \(k>b\), the edges of length \(a\) form \(a\) connected residue classes modulo \(a\). Contract these classes. Edges of length \(b\) have starting positions \(0,\ldots,k-b-1\) and therefore yield the edges \(r\leftrightarrow r+b\pmod a\) for exactly \(t=\min(a,k-b)\) consecutive source residues \(r=0,\ldots,t-1\). The full directed permutation \(r\mapsto r+b\pmod a\) is a union of \(g=\gcd(a,b)\) cycles, each consisting of one congruence class modulo \(g\). The first \(t\) source residues select \(t\) edges; a selected cycle only closes when all its source residues have been included. Since the largest residue in class \(j\in\{0,\ldots,g-1\}\) is \(a-g+j\), the number of completely selected cycles is exactly \(\max(0,t-a+g)\). Therefore the component count after contractions is
\[
c=a-t+\max(0,t-a+g)=\max(a-t,g)=\max(a+b-k,g).
\]
Here the last equality holds also when \(k-b\ge a\), because then both maximums equal \(g\). In this case \(U=k+a+b\), so
\[
\beta=3k-(2k+a+b)+c=k-a-b+\max(a+b-k,g)
=\max(0,k-a-b+g).
\]
Combining the cases gives the displayed triple probability. The strict dependence threshold follows since \(q>1\). Finally, the triple centered moment simplifies to the joint probability minus the product of the three marginals because every proper nonempty intersection has its product probability by Step 2. This completes the proof.

## Verification
`CHECK.py` reproduces the graph formula using a disjoint-set implementation, compares the triple cycle rank against \(\max(0,k-a-b+\gcd(a,b))\) for broad ranges of lengths and gaps, checks every two-time cycle rank, and independently enumerates finite alphabet strings for selected binary and ternary cases. The file is standalone and uses only the Python standard library. The reported test counts describe finite diagnostics; Steps 1–3 establish all quantified statements.

## Relationship to prior work
Zhao's 2026 work on interval-map return records develops Poisson-type limiting laws for suitably normalized recurrence observables; it does not state an exact finite-cylinder three-time joint probability or pairwise-independence boundary for the full shift. Holland and Todd study Poisson-type counting-process limits for recurrence in expanding systems, likewise without this fixed-resolution three-time formula in the sections inspected. The classical overlap and periodicity literature of Guibas–Odlyzko and Fine–Wilf supplies relevant combinatorial foundations: the appearance of \(a+b-\gcd(a,b)\) is the usual word-period threshold, here converted into a probabilistic cycle-rank obstruction. Prior results on pair-correlations of expanding circle maps concern a different metric observable and do not imply the three-event symbolic formula. No novelty is claimed for the equality-graph counting principle or the classical Fine–Wilf lemma themselves.

## Limitations
This is an exact fixed-length joint law, not a Poisson or normal limit theorem. Pairwise independence does **not** imply that the collection of all return events is jointly independent. The original complete Guibas–Odlyzko paper was not available for line-by-line comparison during this examination; although its abstract describes fixed-pattern overlaps and its formalism may encode some related counts, this leaves a historical-priority risk for equivalent formulations. Other older symbolic-return literature may implicitly contain this probability formula. Nonuniform Bernoulli weights, dependent shifts, overlapping initial and translated blocks (times below \(k\)), and first-return conditioning require separate analysis.

## References
1. B. Zhao, *On record behaviours of returns for interval maps*, arXiv:2610.39928, first version publicly submitted 29 October 2026. https://arxiv.org/abs/2610.39928
2. M. Holland and M. Todd, *On distributional limit laws for recurrence*, arXiv:2401.13300, first version publicly submitted 24 January 2024; subsequently *Nonlinearity* 38 (2025), 075028. https://arxiv.org/abs/2401.13300
3. L. J. Guibas and A. M. Odlyzko, *String overlaps, pattern matching, and nontransitive games*, *Journal of Combinatorial Theory, Series A* 30 (1981), 183–208. https://doi.org/10.1016/0097-3165(81)90005-4
4. N. J. Fine and H. S. Wilf, *Uniqueness theorems for periodic functions*, *Proceedings of the American Mathematical Society* 16 (1965), 109–114. https://doi.org/10.1090/S0002-9939-1965-0174934-2
