# A sharp forest-wide ambiguity gap for closed-neighborhood rough observations

## Finding

Let \(T=(V,E)\) be any finite nonempty *simple forest with no isolated vertices*. Its rough observations are the ordered pairs \((L(X),U(X))\), where \(X\) ranges over all subsets of \(V\), and
\[
L(X)=\{v\in V:N_T[v]\subseteq X\},\qquad
U(X)=\{v\in V:N_T[v]\cap X\ne\varnothing\}.
\]
Here \(N_T[v]\) is the reflexive closed neighborhood in \(T\). The complete inverse-fiber size is described by an edge-cover enumeration with parity constraints. In particular, the *fully uncertain* observation \((\varnothing,V)\) is uniquely most frequent, with a sharp multiplicative deficit for every different observation.

More precisely, let \(c\) be the number of components, and let \(e(T)\) count edge sets incident to every vertex of \(T\) (edge covers). Then
\[
|\{X:L(X)=\varnothing,\ U(X)=V\}|=2^c e(T).
\]
For any disjoint \(A,Z\subseteq V\), write
\[
M_T(A,Z)=\big|\{X:L(X)=A,\ V\setminus U(X)=Z\}\big|.
\]
If \(s\) components meet \(A\cup Z\), then
\[
M_T(A,Z)\le 2^{-s}M_T(\varnothing,\varnothing).
\]
Thus every noncentral observation has at most half the multiplicity of the central one, and \(2^{-s}\) is best possible for each pair of integers \(c\ge s\ge1\).

## Assumptions and scope

The forest is finite, undirected, loopless, without parallel edges, nonempty, and has minimum degree at least one. The input subset \(X\) is not assumed connected or nonempty. Colors are binary: a vertex is colored \(1\) precisely when it lies in \(X\). For a vertex set \(B\), \(T[B]\) denotes its induced subforest. An *edge cover* of \(T[B]\) is a subset \(F\subseteq E(T[B])\) incident to every vertex of \(B\). The empty induced forest has exactly one edge cover, namely \(F=\varnothing\); an induced forest with an isolated vertex has none.

For disjoint \(A,Z\), put \(W=A\cup Z\), \(B=V\setminus W\). Write \(s=|\{C:C\text{ a component of }T,\ C\cap W\ne\varnothing\}|\). In each of these \(s\) components choose an anchor \(w_C\in W\cap C\). Let \(P_T(u,v)\) denote the unique undirected edge path in a component from \(u\) to \(v\). All parities below are modulo two, and \(\mathbf1_A\) is the indicator function of \(A\).

## Proof

**1. Disagreement edges recognize the observation.** For a binary coloring \(x=\mathbf1_X\), define
\[
F_x=\{uv\in E:x(u)\ne x(v)\}.
\]
Because \(N_T[v]\) contains \(v\) itself, \(v\in L(X)\) exactly when \(x\) is identically \(1\) on \(N_T[v]\), and \(v\notin U(X)\) exactly when it is identically \(0\) there. These two events occur precisely at vertices of disagreement degree zero, labeled by their own colors. Every other vertex is incident with at least one disagreement edge. Consequently \(L(X)=A\), \(V\setminus U(X)=Z\) holds exactly when (i) \(F_x\) avoids every vertex of \(W\) and covers every vertex of \(B\), and (ii) \(x(w)=\mathbf1_A(w)\) for all \(w\in W\). Condition (i) says that \(F_x\) is an edge cover of the induced graph \(T[B]\).

**2. Every forest edge set is a binary cut.** On a tree component, fix any root bit. For any \(F\subseteq E\), give each other vertex the root bit toggled once for every edge of \(F\) along its unique root path. This realizes precisely \(F\) as the set of bichromatic edges. Conversely every coloring with bichromatic edges \(F\) has one of these two root bits. Different components are independent. Thus an arbitrary forest edge set has exactly \(2^c\) compatible colorings before fixing any vertex colors.

**3. Exact inverse-fiber formula.** Consider an edge cover \(F\) of \(T[B]\). In a component meeting \(W\), the anchor \(w_C\) has prescribed bit \(\mathbf1_A(w_C)\), and all other vertex bits are forced by the unique-path construction. The prescribed colors on \(W\cap C\) hold if and only if
\[
|F\cap P_T(w_C,w)|\equiv
\mathbf1_A(w_C)\oplus\mathbf1_A(w)\pmod2
\quad(w\in W\cap C).
\]
In a component not meeting \(W\), both root bits are allowed. Therefore the exact count is
\[
\boxed{M_T(A,Z)=2^{c-s}\left|\left\{F\subseteq E(T[B]):
\begin{array}{l}
F\text{ covers }B,\\
|F\cap P_T(w_C,w)|\equiv\mathbf1_A(w_C)\oplus\mathbf1_A(w)\ (\mathrm{mod}\ 2)\\
\text{for each component }C\text{ meeting }W\text{ and each }w\in C\cap W
\end{array}
\right\}\right|.}
\]
This also proves the formula for unrealizable observations, for which the right side is zero. When \(W=\varnothing\), all path constraints disappear and \(s=0\), giving \(M_T(\varnothing,\varnothing)=2^ce(T)\).

**4. Injection establishing the sharp gap.** Fix a nonempty \(W\). For each \(w\in W\), select any edge \(e_w\) of \(T\) incident with \(w\); such an edge exists because there are no isolated vertices. Put \(Q_W=\{e_w:w\in W\}\). Every edge cover \(F\subseteq E(T[B])\) avoids \(W\), hence \(F\cap Q_W=\varnothing\). The set \(F\cup Q_W\) covers all vertices of \(T\), and the map \(F\mapsto F\cup Q_W\) is injective, since \(F\) is recovered by deleting \(Q_W\). Thus the number of admissible \(F\) is at most \(e(T)\), including after parity constraints. Multiplication by \(2^{c-s}\) proves the gap.

**5. Attainment at every component deficit.** Take \(T\) to be a disjoint union of \(c\) edges. Each edge component has exactly two central colorings and exactly one coloring for either monochromatic rough observation. Choose \(s\) components to be monochromatic and the remaining \(c-s\) to be central. The resulting fiber has size \(2^{c-s}\), while the central fiber has size \(2^c\), giving equality for every \(c\ge s\ge1\). Since \(e(T)\ge1\) (every forest without isolates admits an edge cover), the central fiber is positive, and for \(s\ge1\) the bound is strictly smaller.

## Verification

The standalone `checker.py` computes lower and upper observations by direct subset enumeration; independently it enumerates edge sets of each induced forest and checks the parity constraints of the closed formula. It also verifies the sharp multiplicity bound and the identity \(M_T(\varnothing,\varnothing)=2^ce(T)\). Execute `python3 checker.py` from this directory. The recorded test suite covers every labeled isolate-free forest with \(2\le |V|\le5\), plus independent random labeled trees on six and seven vertices. Tests are finite regression evidence; the five-step argument above proves the theorem for every finite forest.

For computing the peak without enumerating edge sets, root each tree and let \(a_v(b)\) count selections in the rooted subtree where the parent edge has inclusion status \(b\in\{0,1\}\) and all vertices in that subtree are covered. If \(v\) has children \(u\), then
\[
a_v(1)=\prod_u(a_u(0)+a_u(1)),\qquad
a_v(0)=a_v(1)-\prod_u a_u(0).
\]
The empty product convention makes a leaf satisfy \(a_v(1)=1\), \(a_v(0)=0\). Hence \(e(T)\) is the product of \(a_r(0)\) over all component roots; the recurrences take linear arithmetic-operation time (integer bit complexity depends on the output sizes).

## Relationship to prior work

Hafez, Dib, El-Shanawany and El Atik (published online March 14, 2026) address covering-based rough graphs and graph-approximation validity, motivating attention to non-partition granules. Their work does not provide this inverse-fiber theorem for the specific reflexive neighborhood relation. El Atik, Nawar and Atef (2020) study graph-neighborhood approximation definitions and accuracy/boundary measures; the current statement optimizes the multiplicity of a fixed pair of approximation sets, a different quantitative question. Tang, She and Zhu (2012) treat equivalence-based rough sets through graph/matroid representations, whereas the relation here is generally a nontransitive tolerance.

Published results on inverse-fiber spectra of clique bouquets and exact rough-pair counts for paths or crown graphs concern specific graph classes or a different aggregate invariant. The present statement is forest-wide, applies to every observation, and gives a uniform sharp component-count deficit. Exact counting of edge covers is classical; its use as a complete inverse-fiber parity parameterization and maximal-ambiguity bound is the proposed contribution, not edge-cover counting by itself.

## Limitations

The theorem requires a forest without isolated vertices. It does not claim the same multiplicity inequality for arbitrary cyclic graphs or arbitrary covering-based approximation operators. The general parity-free edge-cover injection may fail as stated when cycles impose cut-space constraints. The parity formula can be exponential to evaluate for a prescribed observation; only the central peak is supplied with a linear-operation dynamic program. No independence or external historical-priority certification is asserted.

## References

1. H. M. Hafez, K. A. Dib, R. El-Shanawany, A. A. El Atik, *A study on rough graphs*, Mathematics in Applied Sciences and Engineering (online March 14, 2026), https://doi.org/10.5206/mase/23201.
2. A. El Atik, A. Nawar, M. Atef, *Rough approximation models via graphs based on neighborhood systems*, Granular Computing (first published November 5, 2020), https://doi.org/10.1007/s41066-020-00245-z.
3. J. Tang, K. She, W. Zhu, *Matroidal Structure of Rough Sets from the Viewpoint of Graph Theory*, Journal of Applied Mathematics (2012), https://doi.org/10.1155/2012/973920.
