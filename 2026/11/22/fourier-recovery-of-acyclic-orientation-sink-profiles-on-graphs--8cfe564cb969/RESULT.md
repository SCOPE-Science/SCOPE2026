# Fourier recovery of acyclic-orientation sink profiles on graphs of maximum degree two

## Finding

**Theorem.** Let \(G=(V,E)\) be a finite simple graph of maximum degree at most two, including the empty graph and isolated vertices. For \(x\in H_G=\mathbb F_2^V\), define \(f_G(x)\) as the number of acyclic orientations of all edges of \(G\) whose set of sinks has indicator \(x\). (An isolated vertex is a sink.) Let \(T_G\) be unnormalized XOR convolution \(T_G h=f_G*h\) on \(\ell^2(H_G)\).

Then \(T_G\) is invertible **if and only if** \(G\) has no degree-one vertex, equivalently, every connected component of \(G\) is an isolated vertex or a cycle. If the cycle components have lengths \(n_1,\ldots,n_c\ge3\), the exact extremal absolute Walsh multipliers are
\[
\min_{\xi\in H_G}|\widehat f_G(\xi)|=2^c,\qquad
\max_{\xi\in H_G}|\widehat f_G(\xi)|=\prod_{j=1}^c(2^{n_j}-2),
\]
so the sharp Hilbert-space convolution condition number is
\[
\kappa_2(T_G)=\prod_{j=1}^c(2^{n_j-1}-1).
\]
All products over empty sets are one. In particular, a single cycle \(C_n\) has full Walsh support for every \(n\ge3\), exact spectral gap \(2\), and condition number \(2^{n-1}-1\).

## Assumptions and scope

All graphs are finite, undirected, simple and vertex-labelled; orientations assign a direction to each edge. A sink is a vertex with outdegree zero. Acyclic means that no directed cycle occurs. For a Boolean frequency \(\xi\subseteq V\), the Fourier normalization throughout is the **unnormalized** sum
\[
\widehat f_G(\xi)=\sum_{x\in H_G}f_G(x)(-1)^{|x\cap\xi|}
=\sum_{o\text{ acyclic}}(-1)^{|\operatorname{Sink}(o)\cap\xi|}.
\]
The Walsh characters form an orthogonal eigenbasis of \(T_G\), with eigenvalues \(\widehat f_G(\xi)\). This is a counting convolution: distinct orientations with the same sink set contribute separate units to \(f_G\).

For a single \(C_n\), write \(S\subseteq\mathbb Z/n\mathbb Z\) for a frequency set, \(z=n-|S|\), and define integers
\[
q_0=q_1=2,\qquad q_{k+2}=2q_{k+1}-2q_k
\quad(k\ge0).
\]
Equivalently, \(q_k=(1+i)^k+(1-i)^k\). If \(S\) is nonempty and proper, let \(\ell_1,\ldots,\ell_r\ge1\) be the lengths of its maximal *cyclic* runs of consecutive selected vertices. The complete multiplier formula is
\[
\widehat f_{C_n}(S)=
\begin{cases}
2^n-2,&S=\varnothing,\\
q_n-2,&S=V(C_n),\\
2^{z-r}\prod_{j=1}^{r}q_{\ell_j}-2,&\varnothing\subsetneq S\subsetneq V(C_n).
\end{cases}
\]

An equivalent hard-core-polynomial formulation is
\[
\widehat f_{C_n}(S)=2^n I(C_n[S];-1/2)-2,
\]
where \(I(H;t)=\sum_{U\subseteq V(H)\text{ independent}}t^{|U|}\) is the independence polynomial of the subgraph induced by \(S\) in \(C_n\). This equality is about a **signed evaluation with a final subtraction of two**, not the indicator convolution by independent sets.

## Proof

**1. Leaf obstruction.** If \(G\) has a leaf \(v\), reverse its unique incident edge. This involution preserves acyclicity, because a directed cycle cannot contain a leaf. It toggles whether \(v\) is a sink. Therefore its paired orientations contribute opposite signs to the singleton-frequency Fourier multiplier, and \(\widehat f_G(\{v\})=0\). A connected finite simple graph of maximum degree at most two is an isolated vertex, a path, or a cycle. Every nontrivial path has a leaf.

**1a. Equivalent hard-core evaluation.** Expand the character weight as \(\prod_{v\in S}(1-2\mathbf1_{\{v\text{ is a sink}\}})\). For a nonempty prescribed subset \(U\subseteq S\), simultaneously requiring all its vertices to be sinks is possible only when \(U\) is independent. The two edges at each such cycle vertex point inward, and removing \(U\) leaves a forest with exactly \(n-2|U|\) free edges, so precisely \(2^{n-2|U|}\) orientations meet the requirement. For \(U=\varnothing\), the number of acyclic orientations is \(2^n-2\). Expanding the product proves the independent-set identity above. The transfer proof below establishes the stronger, uniform arithmetic separation from zero, which is not automatic from the general hard-core identity.

**2. Cycle transfer matrices.** Number the cycle vertices modulo \(n\). Set \(b_j=1\) when the edge \(j\to j+1\) is oriented forward, and zero otherwise. Vertex \(j\) is a sink exactly when \((b_{j-1},b_j)=(1,0)\). Among all \(2^n\) binary edge-orientation words, precisely the two constant words are directed cycles; both have empty sink set. Thus, with
\[
J=\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
M=\begin{pmatrix}1&1\\-1&1\end{pmatrix},
\]
the required signed count is
\[
\widehat f_{C_n}(S)=\operatorname{tr}\left(\prod_{j=0}^{n-1} A_j\right)-2,
\qquad A_j=\begin{cases}M,&j\in S,\\J,&j\notin S.\end{cases}
\]
The \((a,b)\)-entry of \(M\) is \((-1)^{a(1-b)}\); this proves the transfer trace identity independently of any graph-polynomial formula.

**3. Cyclic run factorization.** Let \(u=(1,1)^\mathsf T\), so \(J=uu^\mathsf T\), \(J^g=2^{g-1}J\) for \(g\ge1\), and \(u^\mathsf T M^k u=q_k\). The characteristic polynomial of \(M\) is \(t^2-2t+2\), giving the stated recurrence. Grouping positive-length selected runs and intervening positive-length unselected runs inside the trace gives \(2^{z-r}\prod_jq_{\ell_j}\). For the fully selected case, \(\operatorname{tr}(M^n)=q_n\); for the empty case, \(\operatorname{tr}(J^n)=2^n\). The three-case formula follows.

**4. Nonvanishing and exact gap.** Since \(1\pm i=\sqrt2\,e^{\pm\pi i/4}\), for every integer \(k\ge1\), either \(q_k=0\) (exactly when \(k\equiv2\pmod4\)), or \(|q_k|\ge2\); equality in the latter occurs only at \(k=1\). In fact, if \(k\ge2\), then \(q_k=0\) or \(|q_k|\ge4\).

For nonempty proper \(S\), if some selected run has \(q_{\ell_j}=0\), its transfer trace is zero and the Walsh multiplier is \(-2\). Otherwise its trace has absolute value at least \(2^{z-r}2^r=2^z\). When \(z\ge2\), this is at least four. When \(z=1\), necessarily \(r=1\), with sole run length \(n-1\ge2\), so the trace again has absolute value at least four. For fully selected \(S\), \(q_n=0\) or \(|q_n|\ge4\) because \(n\ge3\). Finally, the empty-set multiplier is \(2^n-2\ge6\). In every case the multiplier equals \(-2\) or an even integer at distance at least two from zero. Choosing exactly two adjacent selected vertices makes \(q_2=0\) and attains \(-2\). Hence the smallest absolute multiplier is **exactly two**. Triangle inequality gives \(|\widehat f_{C_n}(S)|\le\widehat f_{C_n}(\varnothing)=2^n-2\), with equality at the empty frequency.

**5. Disjoint components.** The sink-count measure for a disjoint union is the tensor product of component measures, and its Fourier multipliers multiply. For an isolated vertex the unique orientation has that vertex as a sink, so its two Fourier multipliers have absolute value one. All components are cycles or isolates precisely when no leaf occurs. Multiplying the cycle minimum and maximum yields the stated exact extremes and \(\ell^2\) condition number. This also handles the graph with no vertices.

## Verification

Run `python3 verify.py` with Python 3 and only its standard library. The checker independently enumerates every edge orientation, performs a generic directed-acyclicity test, collects exact sink-indicator multiplicities, and applies an integer fast Walsh transform. It compares every frequency against the closed formula on cycles of length three through fourteen; it tests the leaf obstruction on paths of length two through eleven, several connected/disconnected edge cases, direct character sums for smaller cycles, and the integer recurrence through index one thousand. It reports `PASS: 166855 exact integer assertions`. These are finite checks; the infinite claim depends on the preceding algebraic proof, not numerical extrapolation.

## Relationship to prior work

The sink of an acyclic graph orientation and its enumerative importance appear in Gebhard and Sagan, *Sinks in Acyclic Orientations of Graphs* (1999 public preprint, published 2000). Hwang, Jung, Lee, Oh and Yu, *Acyclic orientation polynomials and the sink theorem for chromatic symmetric functions* (2019 preprint, revised 2020), define the multivariate polynomial whose coefficients are precisely the sink-profile counting measure and give general deletion–contraction, subgraph and bond-lattice expansions. Radchenko, *Independence polynomials and hypergeometric series* (2021), Proposition 5.1, gives a general cycle independence-polynomial transfer trace; the independent-set representation above acknowledges this broader computational tool. Their formula in principle determines every signed evaluation by substitution; it does not directly provide the all-size zero-free classification, sharp extremal Walsh multipliers, or graph-family recovery condition number proved here. Thus the contribution is an arithmetic Fourier specialization, not a new definition of a sink polynomial or a general graph enumerator.

## Limitations

This theorem classifies only graphs of maximum degree at most two; it proves a leaf-induced obstruction for any graph with a leaf but does not characterize graphs of larger minimum degree. It does not claim positive definiteness, positivity of individual nonzero multipliers, or the complete inertia distribution. The eigenvalue minimum is for unnormalized counting convolution; probability-normalizing by the total number of acyclic orientations changes the numerical inverse norm. General sink-polynomial formulas and possibly unindexed specializations create a residual priority risk. 

## References

1. D. D. Gebhard and B. E. Sagan, *Sinks in Acyclic Orientations of Graphs*, arXiv:math/9907078v1, first public 1999-07-12, https://arxiv.org/abs/math/9907078 .
2. B.-H. Hwang, W.-S. Jung, K.-J. Lee, J. Oh and S.-H. Yu, *Acyclic orientation polynomials and the sink theorem for chromatic symmetric functions*, arXiv:1910.10920 (first posted 2019-10-24; v2 2020-08-22), https://arxiv.org/abs/1910.10920 .
3. D. Radchenko, *Independence polynomials and hypergeometric series*, Bull. London Math. Soc. 53 (2021), doi:10.1112/blms.12545, https://doi.org/10.1112/blms.12545 .
