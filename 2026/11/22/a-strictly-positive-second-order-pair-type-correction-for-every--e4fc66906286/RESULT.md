# A strictly positive second-order pair-type correction for every fixed tetrahedron-free hypergraph core

## Finding
Let \(\mathcal M\) be the countable homogeneous \(K_4^{(3)}\)-free three-uniform hypergraph, in the language of one symmetric irreflexive ternary relation. Fix **any** finite \(K_4^{(3)}\)-free three-hypergraph \(H\) with \(k\geq0\) labelled vertices. For each \(n\geq k\), let \(A_n\) be the disjoint union of \(H\) and \(n-k\) isolated vertices, all named individually. Count complete types of **ordered pairs of distinct new vertices** over \(A_n\), and denote this count by \(T_H(n)\). Let \(T_0(n)\) denote the corresponding count for the empty three-hypergraph on \(n\) named vertices.

Write \(\mathcal P=\binom{V(H)}2\), \(K=|\mathcal P|\), and let \(F_H:\{0,1\}^{\mathcal P}\to\{0,1\}\) indicate that the link graph of one new vertex does **not** complete a forbidden tetrahedron with an old triple of \(H\). Set
\[
f_H=\mathbb E F_H(X),\qquad a_p=\mathbb E[F_H(X)\mid X_p=0],\qquad b_p=\mathbb E[F_H(X)\mid X_p=1],
\]
where all coordinates of \(X\) are independent fair bits. Define the computable rational invariant
\[
\boxed{D_H=\frac1{12}\sum_{p\in\mathcal P}(a_p-b_p)(a_p+3b_p).}
\]
Then \(D_H\geq0\), with \(D_H=0\) **if and only if** \(H\) has no hyperedges. Moreover, for every \(n\geq k\),
\[
\boxed{T_H(n)\geq f_H^2 T_0(n),}
\]
and the inequality is strict if \(H\) has an old hyperedge. In particular this is an exact finite-size theorem, not just an asymptotic sign assertion.

For the following explicit probability law, put \(q=3/4\) and
\[
\Pr(S_n=s)=\frac{\binom ns q^{\binom s2}}{\displaystyle\sum_{j=0}^n\binom njq^{\binom j2}},\qquad 0\leq s\leq n.
\]
With \((s)_r=s(s-1)\cdots(s-r+1)\), and the convention that a term with \(r>n\) is zero, there is the sharper, **uniform-for-fixed-\(H\)** expansion
\[
\boxed{\frac{T_H(n)}{T_0(n)}=f_H^2+D_H\frac{\mathbb E(S_n)_2}{(n)_2}+O_H\left(\frac{(\log n)^3}{n^3}\right).}
\]
Here and throughout the asymptotic formula \(n\to\infty\). The exceptional values \(n<2\) are governed by the exact finite inequality, not the displayed ratio of falling factorials. Since \(\mathbb E(S_n)_2\sim(\log n)^2/(\log(4/3))^2\),
\[
\boxed{\lim_{n\to\infty}\frac{n^2}{(\log n)^2}\left(\frac{T_H(n)}{T_0(n)}-f_H^2\right)=\frac{D_H}{(\log(4/3))^2}.}
\]
The limiting correction is therefore strictly positive **for every nonempty core** and vanishes precisely for an empty core.

For a core consisting of one old triple, \(f_H=7/8\), \(D_H=13/64\), and the limiting constant is \(13/(64\log(4/3)^2)\). For a four-vertex core consisting of two triples sharing an old pair, \(f_H=25/32\), \(D_H=865/3072\).

## Assumptions and scope
A \(K_4^{(3)}\) is the complete three-uniform hypergraph on four vertices, with all four possible triples. The class of finite \(K_4^{(3)}\)-free hypergraphs has free amalgamation, so every finite admissible diagram over \(A_n\) extends in \(\mathcal M\); homogeneity makes distinct such diagrams distinct complete types. No algebraic types, repeated new coordinates, unlabeled base equivalences, or probabilistic random vertices are included. The uniform probability distribution in this theorem is on the **finite set of ordered logical types**, not on vertices of \(\mathcal M\).

All old hyperedges of \(A_n\) lie in the fixed labelled core \(H\); the remaining \(n-k\) old vertices are isolated in the induced old hypergraph, but may freely participate in triples involving new vertices. Nothing in the theorem assumes that the old hyperedges of \(H\) are linear or pairwise disjoint.

## Proof
**1. Exact two-point diagrams.** For an ordered pair \((x,y)\) of distinct new vertices, its relations to the old base are specified by three data: the link-edge indicators \(X_{ab}=1_{R(x,a,b)}\) and \(Y_{ab}=1_{R(y,a,b)}\), for each old unordered pair \(ab\), and the subset \(S\) of old vertices on which \(R(x,y,a)\) holds. There is no ternary relation on \(x,y\) alone. A four-set of the form \(\{x,a,b,c\}\) is forbidden precisely if \(abc\) is an old triple and \(X_{ab}=X_{ac}=X_{bc}=1\); these are exactly the clauses encoded by \(F_H(X)\). The analogous condition is \(F_H(Y)=1\). A four-set \(\{x,y,a,b\}\) is forbidden exactly when \(a,b\in S\) and \(X_{ab}=Y_{ab}=1\). These are **all** four-set possibilities. Thus admissibility is equivalent to \(F_H(X)F_H(Y)=1\) and avoidance of the state \((X_{ab},Y_{ab})=(1,1)\) on every old pair contained in \(S\). Free amalgamation realizes every such finite diagram.

**2. Empty-base normalization.** For fixed \(S\) with \(|S|=s\), each old pair contained in \(S\) allows three states \((0,0),(0,1),(1,0)\); every other pair allows four. Consequently, with \(N=\binom n2\),
\[
\boxed{T_0(n)=\sum_{s=0}^n\binom ns3^{\binom s2}4^{N-\binom s2}=4^N\sum_{s=0}^n\binom ns q^{\binom s2}.}
\]
For a general core, first sample \(S\) with weight proportional to \(q^{\binom{|S|}2}\), and then sample independently, for every old pair, a uniformly random allowed state of \((X_{ab},Y_{ab})\). The ratio \(T_H(n)/T_0(n)\) is exactly the probability that both core link clauses hold. Conditional on \(|S|=s\), \(S\) is uniform among the \(s\)-subsets.

**3. Strict positive correlation at arbitrary finite size.** Fix \(S\). The pair-state law on the core is independent across pairs. For any core pair \(p\notin\binom S2\), \((X_p,Y_p)\) consists of two independent fair bits; for \(p\in\binom S2\), it is uniform on the three states other than \((1,1)\). Start with all core pairs unconditioned and impose these three-state restrictions one at a time. Fix the other coordinates at one such step. The two factors of \(F_H(X)F_H(Y)\) become \(u(X_p)v(Y_p)\), with \(u(0)\geq u(1)\geq0\) and \(v(0)\geq v(1)\geq0\), because each forbidden-tetrahedron clause is decreasing. Direct subtraction gives
\[
\mathbb E_3[uv]-\mathbb E_4[uv]
=\frac{(u(0)-u(1))(v(0)+v(1))+2u(1)(v(0)-v(1))}{12}\geq0.
\]
Here \(\mathbb E_3\) and \(\mathbb E_4\) refer to the uniform three-state and four-state distributions at one pair. Hence imposing any collection of restrictions cannot decrease the chance of joint validity, proving \(T_H(n)/T_0(n)\geq f_H^2\). If \(H\) contains a triple \(abc\), choose \(p=ab\) and \(S\) with \(S\cap V(H)=\{a,b\}\), an event of positive weight. The inequality at that sole active core pair is strict: taking \(X_{ac}=X_{bc}=1\) and all other link bits zero makes changing \(X_{ab}\) from zero to one change legality. Thus the global inequality is strict. If \(H\) has no triples, \(F_H\equiv1\), and equality holds.

**4. The exact second-order coefficient.** A core intersection \(T=S\cap V(H)\) of size zero or one activates no core pair and contributes exactly \(f_H^2\). If \(T=\{a,b\}\), only \(p=ab\) is active. The one-pair success probability is
\[
\frac{a_p^2+2a_pb_p}{3},
\]
whereas the baseline is \(f_H^2=((a_p+b_p)/2)^2\). Their difference is precisely
\[
d_p=\frac{(a_p-b_p)(a_p+3b_p)}{12}.
\]
For core intersections of cardinality at least three, the success probability remains in \([0,1]\). Since \(S\) conditional on \(|S|\) is exchangeable, set \(\pi_r(n)=\mathbb E(S_n)_r/(n)_r\). For any fixed core pair \(p\), the probability that \(S\cap V(H)=p\) equals \(\pi_2(n)+O_k(\pi_3(n))\), by the union bound over other core vertices; also \(\Pr(|S\cap V(H)|\geq3)=O_k(\pi_3(n))\). It follows *without dropping any other intersection cases* that
\[
\frac{T_H(n)}{T_0(n)}=f_H^2+\left(\sum_{p\in\mathcal P}d_p\right)\pi_2(n)+O_H(\pi_3(n)).
\]
The sum is \(D_H\). Every \(a_p\geq b_p>0\), by monotonicity and the all-zero legal assignment. Equality \(a_p=b_p\) holds if \(p\) participates in no old triple, while \(a_p>b_p\) whenever \(p\) lies in some old triple, using the three-link witness of the preceding paragraph. This proves the claimed sharp zero/positive characterization.

**5. Moment scale and the limit.** Put \(w_{n,s}=\binom ns q^{\binom s2}\), so
\[
\frac{w_{n,s+1}}{w_{n,s}}=\frac{n-s}{s+1}q^s,
\]
a strictly decreasing function of \(s\). If \(m_n\) is a maximal-weight index, the two adjacent ratio inequalities imply
\[
m_n=\frac{\log n-\log\log n+O(1)}{\log(4/3)}.
\]
Moreover adjacent weight ratios decrease by a factor at most \(q\). For every integer \(j\geq1\), both defined tails satisfy \(w_{n,m_n\pm j}/w_{n,m_n}\leq q^{j(j-1)/2}\). The normalized law is therefore uniformly sub-Gaussian around \(m_n\), and for each fixed positive integer \(r\), \(\mathbb E(S_n)_r\sim m_n^r\). In particular \(\pi_3(n)=O((\log n)^3/n^3)\) and \(\pi_2(n)\sim(\log n)^2/(n^2\log(4/3)^2)\). Inserting these into the exact reduction proves the expansion and displayed limit.

**6. Exact small cores.** For one old triple \(abc\), \(F_H(X)=0\) exactly when all three link bits are one. Thus \(f_H=7/8\), and at any pair \(p\subset abc\), \((a_p,b_p)=(1,3/4)\), giving \(d_p=13/192\), hence \(D_H=13/64\). For two triples \(abc,abd\), exact enumeration of the six link bits gives \(f_H=50/64=25/32\); the coefficient calculation gives \(D_H=865/3072\). These evaluations can also be reconstructed directly from the standalone finite checker.

## Verification
The standalone `verify.py` first constructs the admissibility predicate from old-triple clauses, independently enumerates all ordered link-bit pairs and all choices of \(S\) for every selected core of size at most four, and compares the results with a separate exact summation formula. It also verifies the exact finite inequality, strictness, and the rational value of \(D_H\) for one triple, two pair-overlapping triples, three triples on four points, and the empty core. It checks empty-old-base formulas independently through four old vertices. Output is recorded in `verification_output.txt` and ends in `EXACT_FORMULA_AND_STRICT_INEQUALITY_OK`. Finite tests corroborate the exact combinatorial reduction; the inequalities and asymptotic limit for all \(n\) follow from the proof, not from extrapolation.

## Relationship to prior work
Conant's free-amalgamation treatment gives the generic \(K_4^{(3)}\)-free Fraïssé structure, but does not count these two-point types or study isolated-base perturbations. The previously available sharp overlap-matching result for tetrahedron-free hypergraphs counts **one-point** types and in fact supplies \(f_H\) for a given old core, but it neither implies the strict pair-type inequality nor the coefficient \(D_H\). In contrast, the present theorem analyzes the joint two-point compatibility constraints and identifies their first nonzero contribution. Brown–Dilcher–Manna's expected-independence polynomial, and subsequent saddle-point work, already cover the scalar normalizing sum \(T_0(n)/4^{\binom n2}\) and its asymptotics; no novelty is claimed for that sum, its ratios, or logarithmic localization alone. A distinct published result for \(K_4^-\)-free three-hypergraphs forbids three edges on four vertices and does not cover the present tetrahedron-free class. The existing lattice-phase result for union-closed team properties derives a related coefficient-index law; its different parameterization does not contain the fixed-core second-order pair-type invariant established here.

## Limitations
The fixed core \(H\) is held fixed as \(n\to\infty\); no uniform error bound as \(|H|\) grows is proved. The asymptotic coefficient is an explicitly computable finite-core quantity, but evaluating it from a large hypergraph need not be computationally efficient. The theorem concerns complete ordered **two-point** types, not higher tuple arities, and only bases formed by adjoining isolated old vertices to a fixed core. The model uses the tetrahedron \(K_4^{(3)}\) prohibition, not the stronger \(K_4^-\) prohibition. The binomial-sum asymptotics are established background, and equivalent older treatments of joint free-amalgamation link distributions are a residual priority risk. No independent mathematical validation has occurred.

## References
1. G. Conant, “An axiomatic approach to free amalgamation,” arXiv:1505.00762, first publicly posted 2015-05-04, especially Section 3 and the generic forbidden-clique hypergraph example. https://arxiv.org/abs/1505.00762
2. J. I. Brown, K. Dilcher and D. V. Manna, “On the Roots of Expected Independence Polynomials,” *Journal of Graph Theory* 73 (2013), 322–326; first published online 2012-07-30. https://doi.org/10.1002/jgt.21678
3. W. Gawronski and T. Neuschel, “On a conjecture on sparse binomial-type polynomials by Brown, Dilcher and Manna,” arXiv:1310.5256, first posted 2013-10-19. https://arxiv.org/abs/1310.5256
4. “Sharp overlap-matching bounds for one-point types of the generic tetrahedron-free 3-hypergraph,” published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-overlap-matching-bounds-for-one-point-types-of-the-generic--5ae2c90229c3
5. “A lattice-phase local law with a first correction for two-generator union-closed team properties,” published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-lattice-phase-local-law-with-a-first-correction-for-two-genera--decdf6cc1aac
