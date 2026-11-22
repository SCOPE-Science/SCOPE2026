# Even-cycle obstruction to support-rigid bracket fibers in graphical Lie algebras

## Finding
Let \(G=(V,E)\) be any finite simple graph, with \(n=|V|\), \(m=|E|\), and fix an orientation of its edges. Over any finite field \(\mathbb F_q\), form the two-step nilpotent graphical Lie algebra \(L_G=\mathbb F_q^V\oplus\mathbb F_q^E\), with the second summand central and basis brackets \([e_i,e_j]=z_{ij}\) for oriented edges. For \(z=\sum_{e\in E}z_eZ_e\in\mathbb F_q^E\), write
\[
F_G(z)=\#\{(X,Y)\in L_G^2:[X,Y]=z\}.
\]
A function on \(\mathbb F_q^E\) is **support-rigid** if its value depends only on the set of edges with nonzero coordinates, rather than on the particular nonzero field elements.

**Theorem.** For each fixed prime power \(q>2\), \(F_G\) is support-rigid if and only if \(G\) contains no cycle of even length (not necessarily induced). For \(q=2\), support-rigidity holds for every graph, trivially because each nonzero coordinate equals one. In particular, for every graph with no even cycle and every \(q\ge2\), set \(\nu(S)\) to be the maximum size of a matching in the spanning subgraph with edge set \(S\subseteq E\), and let
\[
t_e(z)=\begin{cases}q-1,&z_e=0,\\-1,&z_e\ne0.\end{cases}
\]
Then **every prescribed bracket fiber** is given exactly by
\[
\boxed{F_G(z)=q^{2n+m}\sum_{S\subseteq E}q^{-2\nu(S)}\prod_{e\in S}t_e(z).}
\]
The rational-looking expression is always a nonnegative integer because it equals the stated counting function. It includes disconnected graphs, isolated vertices, the empty graph, and all characteristics, including characteristic two.

The formula gives a meaningful boundary *within* support-rigid graphs: support-rigidity does not imply surjectivity. For the bowtie graph of two triangles sharing one vertex, with edges listed as \((01),(12),(20),(03),(34),(40)\), a prescribed target \((a,b,c,d,e,f)\) is unattainable exactly when either
\[
a=c=0,\quad b\ne0,\quad(d,f)\ne(0,0),
\]
or
\[
d=f=0,\quad e\ne0,\quad(a,c)\ne(0,0).
\]
Consequently this graph has exactly \(2q(q-1)(q^2-1)\) missing central targets, for every finite field.

## Assumptions and scope
The graph is finite, undirected, simple, and may be disconnected or empty. The chosen edge orientations define signs in coordinates; changing orientations does not alter any support statements. Define \(L_G\) as an alternating bilinear Lie bracket even in characteristic two: for \(X=(x,\xi),Y=(y,\eta)\),
\[
[X,Y]_e=x_i y_j-x_j y_i\quad(e=i\to j).
\]
Thus \(L_G\) has dimension \(n+m\) and its derived subspace is the entire edge-coordinate space. The count is over all ordered pairs of full Lie algebra elements, including their freely chosen central coordinates. No assumption that every target is attainable is made. A matching in \(S\) is a set of vertex-disjoint selected edges, and \(\nu(\varnothing)=0\).

## Proof
**1. Fourier transform of a prescribed bracket.** Fix a nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C^*\). For an edge-frequency vector \(\lambda\in\mathbb F_q^E\), let \(A_\lambda\) be the alternating \(n\times n\) matrix with entries \((A_\lambda)_{ij}=\lambda_e\), \((A_\lambda)_{ji}=-\lambda_e\) for each oriented edge \(e=i\to j\), and zero elsewhere. Then
\[
\sum_{(X,Y)\in L_G^2}\psi\bigl(\lambda\cdot[X,Y]\bigr)
=q^{2m}\sum_{x,y\in\mathbb F_q^n}\psi(x^TA_\lambda y)
=q^{2(n+m)-\operatorname{rank}A_\lambda}.
\]
Indeed, summing over \(y\) gives \(q^n\) precisely for \(x\in\ker A_\lambda\), of which there are \(q^{n-\operatorname{rank}A_\lambda}\); central choices contribute \(q^{2m}\). Fourier inversion on the \(m\)-dimensional edge space therefore gives
\[
F_G(z)=q^{2n+m}\sum_{\lambda\in\mathbb F_q^E}q^{-\operatorname{rank}A_\lambda}\psi(-\lambda\cdot z).
\]

**2. The no-even-cycle rank lemma.** Suppose a graph \(H\) contains no even cycle. Every induced subgraph of \(H\) has at most one perfect matching, for two distinct perfect matchings would have an even cycle in their symmetric difference. Let \(S\subseteq E\) be the nonzero-weight edge support of \(A_\lambda\), and let \(r=\nu(S)\). On the \(2r\) endpoints of a maximum matching, the principal Pfaffian is a single nonzero monomial (that matching), hence the principal minor is nonsingular. Conversely, a nonzero principal Pfaffian of order exceeding \(2r\) would contain a matching of more than \(r\) edges, impossible. For alternating matrices over any field, the rank is the largest order of a nonsingular principal alternating submatrix. This is valid also in characteristic two, where alternating means zero diagonal. Hence
\[
\operatorname{rank}A_\lambda=2\nu(\operatorname{supp}\lambda).
\]
Substitute this into Fourier inversion. On a fixed support \(S\), the frequencies separate by coordinate, and
\[
\sum_{a\in\mathbb F_q^\times}\psi(-az_e)=\begin{cases}q-1,&z_e=0,\\-1,&z_e\ne0.\end{cases}
\]
This proves the complete fiber formula and its support-rigidity.

**3. Necessity of excluding even cycles.** Suppose \(G\) contains a simple cycle of even length \(2r\). Choose \(\lambda\) whose support consists *exactly* of the edges of that cycle, putting zero on every other edge. The corresponding alternating matrix is a weighted cycle block plus zero rows. Its top Pfaffian is the signed sum of the two alternating perfect-matching monomials. Since all cycle weights are nonzero, varying one weight makes the Pfaffian zero, or nonzero, according as that weight equals one specified nonzero value or any other nonzero value. Both choices exist for every \(q>2\). The rank is \(2r-2\) in the first case and \(2r\) in the second: deleting two adjacent cycle vertices leaves a path with a unique perfect matching, furnishing a nonsingular principal submatrix of order \(2r-2\). Therefore \(\lambda\mapsto q^{-\operatorname{rank}A_\lambda}\) is not support-rigid.

Fourier transformation preserves invariance under coordinatewise rescaling by \((\mathbb F_q^\times)^E\) (it intertwines the scaling action with the inverse scaling action). Consequently, if \(F_G\) were support-rigid, so would its Fourier transform, which by Step 1 is a positive scalar multiple of \(q^{-\operatorname{rank}A_\lambda}\). The exhibited rank variation is a contradiction. This proves the converse for \(q>2\).

**4. Bowtie image obstruction and exact count.** Write each horizontal vertex input as a column \(u_i=(x_i,y_i)\in\mathbb F_q^2\). Every edge coordinate is \(\det(u_i,u_j)\). In a triangle with hub vertex \(0\), if both hub-edge determinants vanish and the opposite-edge determinant is nonzero, then necessarily \(u_0=0\); otherwise both other columns would be multiples of \(u_0\) and their determinant would vanish. This forces both hub-edge determinants in the *other* triangle to vanish, proving both stated obstructions.

They are also the only obstructions. If neither triangle has nonzero opposite determinant with both its hub-edge determinants zero, fix any \(u_0\ne0\). In each triangle, the hub-edge determinant equations cut out two affine lines of columns parallel to \(u_0\); varying their two free parameters realizes every prescribed opposite-edge determinant whenever at least one of the two hub-edge determinants is nonzero. When both are zero, the opposite determinant is necessarily zero, exactly the assumed condition. If a triangle has a nonzero opposite determinant with both hub-edge determinants zero, but the other triangle also has zero hub-edge determinants, choose \(u_0=0\), and realize the two opposite determinants independently by arbitrary pairs of columns. These cases exhaust all targets.

The first missing type has \(q-1\) choices for its nonzero opposite coefficient, \(q^2-1\) choices for a nonzero ordered pair of hub-edge coefficients in the second triangle, and \(q\) unrestricted choices for its opposite coefficient. The second type has the same count and the two types are disjoint. Thus exactly \(2q(q-1)(q^2-1)\) targets are absent.

## Verification
The self-contained `verify_graph_bracket_fibers.py` independently enumerates horizontal input pairs over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\) (the last constructed with the irreducible polynomial \(t^2+t+1\)) for one-edge, triangle, path, five-cycle, two-triangle bowtie, and three-triangle friendship graphs. It compares each entire prescribed fiber table against a separate maximum-matching enumeration of the displayed formula. There are eleven checked configurations, including 1,048,576 ordered horizontal input pairs over \(\mathbb F_4\) for the five-cycle and 729 target fibers for the bowtie over \(\mathbb F_3\). The checker also confirms that, on the four-cycle over both \(\mathbb F_3\) and \(\mathbb F_4\), the equally supported targets \((1,1,1,1)\) and \((1,1,1,2)\) have different fiber sizes, providing concrete instances of the necessity direction. `CHECK_OUTPUT.txt` records the outputs.

These finite computations test the formulas; they do not establish the all-graph theorem. That conclusion rests on the rank/Pfaffian and Fourier arguments in the proof.

## Relationship to prior work
Graph-associated two-step nilpotent Lie algebras and graph reconstruction are established by Mainkar (2013); that work concerns their isomorphism types, not the finite-field prescribed bracket distribution. Goze and Remm (first public 2015) treat structure and deformation of nilpotent Lie algebras, not these finite-field counting fibers. Cavers et al. (2012), especially Theorems 4.2–4.3, already establish the graph-theoretic equivalence of no even cycles with orientation-independent spectra of real sign skew-adjacency matrices, together with the unique-perfect-matching criterion. **Their graph spectral theorem and matching criterion are credited, not claimed as new.** The present claim instead characterizes a finite-field **Lie-bracket word-map distribution** at every central target, for arbitrary nonzero edge weights and all finite characteristics, and supplies its exact fiber law.

Rossmann (2022) studies graphical-group conjugacy-class sizes and centralizers; these determine the zero-bracket total but not the nonzero prescribed-target fibers. A related earlier finite-field formula for forests covers that subclass; another earlier result gives complete prescribed fibers for single odd cycles. Neither covers all odd cacti or characterizes arbitrary graphs by fiber support-rigidity. Unicyclic skew-rank enumeration and character-degree results classify *aggregated frequency ranks*, not their complete frequency-by-frequency Fourier phase needed for prescribed targets. The bowtie image obstruction is also not supplied by the separate forest and bare-cycle results.

## Limitations
This is a theorem about graphical two-step Lie brackets, not a classification of all bilinear word maps or arbitrary Lie algebras. For graphs containing even cycles, it proves the failure of support-only fibers over every field of size greater than two, but it does **not** give the complete non-support-rigid fiber law on those graphs. A graph with no even cycles need not have surjective bracket map: the bowtie counterexample exhibits this explicitly. The formula is an exact finite sum and can take exponential time to evaluate on arbitrary graphs; it is not presented as a polynomial-time graph algorithm. Historical priority against any unlocated equivalent finite-field word-map theorem is not independently certified.

## References
- M. Goze and E. Remm, *k-Step Nilpotent Lie Algebras*, arXiv:1502.05016, initial public version 17 February 2015, primary MSC 17B30. https://arxiv.org/abs/1502.05016
- M. Mainkar, *Graphs and two-step nilpotent Lie algebras*, arXiv:1310.3414, initial public version 12 October 2013. https://arxiv.org/abs/1310.3414
- M. Cavers et al., *Skew-adjacency matrices of graphs*, Linear Algebra Appl. 436 (2012), 4512–4529, Theorems 4.2–4.3. https://doi.org/10.1016/j.laa.2012.01.019
- T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, Bull. London Math. Soc. 54 (2022), 1923–1943. https://doi.org/10.1112/blms.12665
- *Prescribed bracket fibers of finite-field graphical Lie algebras on forests*, published research record, 13 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-prescribed-bracket-fibers-of-finite-field-graphical-lie-algebras--c92e90370f3f
- *A factorized Pfaffian correction for graphical groups of every unicyclic graph*, published research record, 2 November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-factorized-pfaffian-correction-for-graphical-groups-of-every-u--938aea29d44f
