# Four-profile law for local modal validity in sparse directed frames

## Finding
Fix a real number \(c>0\), and for each integer \(n>\max\{2,c\}\) form a loopless directed graph \(G_n\) on \([n]\) by including each ordered arc between distinct vertices independently with probability \(p=c/n\). Regard it as a Kripke frame with the standard Boolean semantics. At a world \(w\), say an axiom is **locally frame-valid** when it holds at \(w\) under **every** valuation of its propositional variable. In the order \((\mathsf D,\mathsf B,\mathsf 4,\mathsf 5,\mathsf M)\), use the five standard formulas
\[
\mathsf D:\ \Box P\to\Diamond P,\qquad
\mathsf B:\ P\to\Box\Diamond P,\qquad
\mathsf 4:\ \Box P\to\Box\Box P,\qquad
\mathsf 5:\ \Diamond P\to\Box\Diamond P,\qquad
\mathsf M:\ \Box\Diamond P\to\Diamond\Box P.
\]
Let \(V_n(w)\in\{0,1\}^5\) be the corresponding local-validity vector. The four vectors
\[
v_0=(0,1,1,1,0),\quad v_1=(1,0,1,0,1),\quad
v_2=(1,0,0,0,1),\quad v_3=(1,0,0,0,0)
\]
account for all but \(O_{\mathbb P}(1)\) vertices. Their empirical proportions converge in \(L^2\) to the explicit probabilities
\[
q_0=s,\qquad q_1=t-s,\qquad q_2=1-t-u+s,\qquad q_3=u-s,
\]
where
\[
s=e^{-c},\qquad t=e^{-c(1-e^{-c})},\qquad
u=e^{-c(1+c)e^{-c}}.
\]
In particular the limiting local frame-validity frequency of the McKinsey axiom is \(1-u\); it has a unique global maximum at \(c=\varphi=(1+\sqrt5)/2\), of exact value
\[
1-\exp\bigl(-\varphi(1+\varphi)e^{-\varphi}\bigr).
\]

A finite-size version is exact up to an explicit small error. Put
\[
\alpha_{0,n}=(1-p)^{n-1},\qquad
\alpha_{1,n}=(n-1)p(1-p)^{n-2},
\]
\[
s_n=(1-p)^{n-1},\qquad t_n=[1-p(1-\alpha_{0,n})]^{n-1},\qquad
u_n=[1-p(\alpha_{0,n}+\alpha_{1,n})]^{n-1}.
\]
For a uniformly chosen root, the total-variation distance between the distribution of \(V_n(w)\) and the law supported on \(v_0,v_1,v_2,v_3\) with probabilities
\[
q_{n,0}=s_n,\quad q_{n,1}=t_n-s_n,\quad
q_{n,2}=1-t_n-u_n+s_n,\quad q_{n,3}=u_n-s_n
\]
is at most
\[
\varepsilon_{n,p}=(n-1)p^2+(n-1)(n-2)p^3+
\binom{n-1}{2}(n-2)p^4
\le\frac{c^2+c^3+c^4/2}{n}.
\]
For each \(j\in\{0,1,2,3\}\), if \(F_{n,j}=n^{-1}\#\{w:V_n(w)=v_j\}\), then
\[
\left|\mathbb EF_{n,j}-q_{n,j}\right|\le\varepsilon_{n,p},\qquad
\operatorname{Var}(F_{n,j})\le\frac{c(1+3c+c^2)}n.
\]
The bound on the expected number of worlds whose actual vector differs from the canonical vector determined by their first two outdegree generations is \(c^2+c^3+c^4/2\), uniformly in \(n\).

## Assumptions and scope
All arcs are ordered, independently sampled and irreflexive. A valuation is an arbitrary subset of the finite vertex set, not a random valuation. The parameter \(c\) is fixed as \(n\to\infty\). Empty successor sets use ordinary vacuous truth for \(\Box\) and falsity for \(\Diamond\). All probability statements refer to this model and these five precise axiom schemata.

## Proof
For a fixed world \(w\), let \(S=N^+(w)\) and \(A_x=N^+(x)\) for \(x\in S\). Standard valuation tests give the following exact criteria: \(\mathsf D\) holds iff \(S\ne\varnothing\); \(\mathsf B\) holds iff \(w\in A_x\) for every \(x\in S\); \(\mathsf 4\) holds iff \(\bigcup_{x\in S}A_x\subseteq S\); and, because the frame is loopless, \(\mathsf 5\) holds iff \(S=\varnothing\). For \(\mathsf M\), a countervaluation \(P\) must meet every \(A_x\) but must contain no \(A_x\) in full. Thus \(\mathsf M\) is valid iff \(S\ne\varnothing\) and the hyperedge family \(\{A_x:x\in S\}\) has no two-coloring in which every edge receives both colors. If any \(A_x\) is empty or a singleton, validity is automatic. If all are of size at least two and pairwise disjoint, choosing one element of each \(A_x\) as true produces a countervaluation.

Define \(K=|S|\), and classify each \(x\in S\) by whether \(|A_x|\) equals zero, equals one, or is at least two. Let \(C_0,C_1,C_2\) be the respective counts. Define a canonical vector at \(w\): \(v_0\) for \(K=0\); \(v_1\) for \(K>0,C_1=C_2=0\); \(v_2\) for \(C_0+C_1>0,C_1+C_2>0\); and \(v_3\) for \(K>0,C_0=C_1=0\). These cases partition all degree profiles. The exact frame conditions agree with this canonical vector unless at least one of three collision events occurs:

1. A reciprocal arc \(w\to x\to w\), relevant to \(\mathsf B\).
2. A triangle-like directed configuration \(w\to x,\ x\to y,\ w\to y\) with \(x\ne y\), relevant to the converse for \(\mathsf 4\).
3. Two distinct successors \(x,y\) of \(w\) having a common out-neighbor, relevant to \(\mathsf M\).

Their probabilities are bounded, by counting ordered or unordered candidate witnesses, respectively, by \((n-1)p^2\), \((n-1)(n-2)p^3\), and \(\binom{n-1}{2}(n-2)p^4\). This gives the stated coupling and total-variation bounds, and after summing over all roots the uniform expected-exception bound.

The canonical law is **exactly multinomial** for every finite \(n\). Indeed, for distinct potential children \(x\ne w\), the pairs \((1_{w\to x},|N^+(x)|)\) depend on disjoint independent arc coordinates across different \(x\); all outgoing rows from \(x\) are independent of the outgoing row from \(w\). The probability of child-degree type zero is \(\alpha_{0,n}\), of type one is \(\alpha_{1,n}\), and of type at least two is their complement. Therefore \((C_0,C_1,C_2,n-1-K)\) has multinomial parameters \(n-1\) and cell probabilities \(p\alpha_{0,n},p\alpha_{1,n},p(1-\alpha_{0,n}-\alpha_{1,n}),1-p\). Taking the relevant zero-count probabilities gives \(s_n,t_n,u_n\) and the four formulas displayed above. Binomial-to-Poisson limits give \(s,t,u\).

For concentration, resample a single directed arc \(x\to y\). This can change the local vector only at \(x\) and vertices \(z\) with \(z\to x\): at most \(1+\deg^-(x)\) vertices. The indegree is independent of the resampled arc, has mean at most \(c\), and satisfies \(\mathbb E(1+\deg^-(x))^2\le1+3c+c^2\). Applying the Efron--Stein inequality to \(F_{n,j}\), noting that two independent Bernoulli copies of the arc differ with probability \(2p(1-p)\), yields the stated variance bound. Together with the expectation bound this proves \(L^2\)-convergence and the tight exceptional-world count.

Finally \(\Pr(\mathsf M\text{ locally valid})\to1-\exp[-h(c)]\) where \(h(c)=c(1+c)e^{-c}\). Since \(h'(c)=e^{-c}(1+c-c^2)\), the unique positive maximizer is \((1+\sqrt5)/2\); both endpoint limits are zero, proving global optimality.

## Verification
The standalone `checker.py` enumerates all loopless directed graphs on two, three and four labeled vertices, independently evaluates every one-proposition valuation for the McKinsey axiom, and matches the exact finite multinomial profile probabilities. It separately checks the hypergraph two-colorability criterion and verifies an explicit nonasymptotic discrepancy bound by rational weighted enumeration on four vertices at arc probability \(1/10\). Execute `python3 checker.py` with Python 3. The finite tests do not replace the general coupling, independence or variance proofs.

## Relationship to prior work
Van Benthem, ten Cate and Yang (2026) analyze finite-frame preservation and establish \(\mathbf{coNP}\)-completeness of deciding whole-frame McKinsey validity; the present work instead determines a local validation statistic on a sparse random frame, with exact finite-size comparison and joint frequencies. Cuconato and Ferrari (2026) describe empirical local validation degrees of the structural modal axioms on semantic nearest-neighbor graphs; the present independent-arc baseline also includes McKinsey validity. Goranko and Kapron (2003) study almost-sure **whole-frame** validity under a different, uniform-frame model. General random-graph local convergence does not by itself provide the explicit four-way probabilities or McKinsey optimum without the local structural and hypergraph calculation.

## Limitations
The result does not address self-loops, undirected graph dependence, varying \(c\), joint central limit theorems, or full-frame modal validity probabilities. The error estimate may be nonsharp, and the bound on exceptional worlds proves tightness, not an exact limiting distribution. The scope is local validity under every valuation, not average satisfaction over random valuations. Earlier general random-frame or hypergraph theorems may provide alternative derivations of some components.

## References
- J. van Benthem, B. ten Cate and X. Yang, *When do modal definability and preservation theorems transfer to the finite?*, arXiv:2603.12171 (first public March 12, 2026), especially Section 5.4.
- S. Cuconato and D. Ferrari, *Human and AI-generated texts between modal logic and statistics*, arXiv:2609.20311 (2026); abstract describes local frequencies for modal axioms \(\mathsf B,\mathsf4,\mathsf5,\mathsf D\).
- V. Goranko and B. Kapron, *The modal logic of the countable random frame*, Archive for Mathematical Logic 42 (2003), 221–243, doi:10.1007/s001530100135.
