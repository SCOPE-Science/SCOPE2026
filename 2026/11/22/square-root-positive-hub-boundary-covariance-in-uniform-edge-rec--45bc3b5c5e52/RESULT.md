# Square-root positive hub–boundary covariance in uniform-edge recursive two-complexes

## Finding
Start with one triangle on vertices 1, 2, 3. At each stage choose one existing edge uniformly and add a new vertex joined to both endpoints, preserving all triangles and faces. Let \(D_N\) be the graph degree of vertex 1 and \(L_N\) the number of graph-degree-two vertices at size \(N\). The *single joint covariance theorem* is: for each integer \(N\ge 4\), \(c_N=\operatorname{Cov}(D_N,L_N)\) is determined exactly by

\[
 c_4=0,\qquad c_{N+1}=\left(1-\frac{1}{2N-3}\right)c_N+
 \frac{\mu_N(2N^2-8N+21)-10(2N-3)}{3(2N-5)(2N-3)^2},
\]
where \(\mu_N=\mathbb E D_N=\sqrt\pi\,\Gamma(N-1)/\Gamma(N-3/2)\). In particular, \(c_N>0\) for every \(N\ge5\), and

\[
\boxed{\lim_{N\to\infty}\frac{\operatorname{Cov}(D_N,L_N)}{\sqrt N}=\frac{\sqrt\pi}{12}.}
\]
Using the known marginal variances, this also gives the precise decorrelation rate

\[
\operatorname{Corr}(D_N,L_N)\sim
\sqrt{\frac{\pi}{12(4-\pi)}}\,N^{-1/2}.
\]
The covariance grows, although the correlation vanishes. The exact recurrence, the positive sign, and the cross-scale limit form one joint dependence result.

## Assumptions and scope
The growth rule chooses uniformly among all current edges, never uniformly among a union of vertices and edges. The initial complex is exactly one triangle. The construction is the *homogeneous* two-dimensional simplicial-complex model (HSC(2)), not the distinct random-recursive model (RRSC(2)). There are exactly \(M_N=2N-3\) edges at size \(N\). All expectations and covariances are over all independent random edge selections through that stage. No assumption of asymptotic normality is used or proved.

Define \(K_N\) as the number of degree-two neighbors of vertex 1, and \(J_N=\mathbf 1\{D_N=2\}\). The auxiliary quantities are needed only for proof; they are not extra findings.

## Proof
**1. Deterministic incidence structure and transitions.** At \(N=4\) there are exactly two degree-two vertices, and they are nonadjacent. This nonadjacency remains true: any chosen edge meets at most one degree-two endpoint; any such endpoint becomes degree three, and the new degree-two vertex has two neighbors of degree at least three. Each degree-two vertex has exactly two incident edges.

For the randomly chosen edge let \(I_N\) indicate incidence with vertex 1, let \(C_N\) indicate incidence with any degree-two vertex, and let \(B_N\) count incidence with a degree-two neighbor of vertex 1. Conditional on the current graph \(\mathcal F_N\),

\[
\begin{gathered}
D_{N+1}=D_N+I_N,\quad L_{N+1}=L_N+1-C_N,\quad
K_{N+1}=K_N+I_N-B_N,\\
\mathbb E[I_N\mid\mathcal F_N]=\frac{D_N}{M_N},\quad
\mathbb E[C_N\mid\mathcal F_N]=\frac{2L_N}{M_N},\quad
\mathbb E[B_N\mid\mathcal F_N]=\frac{2K_N}{M_N}.
\end{gathered}
\]

**2. The root-degree-two exception.** An edge can touch both vertex 1 and a degree-two endpoint in two ways: it can touch a degree-two *neighbor* of vertex 1 (there are \(K_N\) such edges), or vertex 1 itself can have degree two (then its two incident edges qualify). The two alternatives are disjoint. Hence the exact conditional mixed increment identity is

\[
\mathbb E[I_N(1-C_N)\mid\mathcal F_N]
=\frac{D_N-K_N-2J_N}{M_N}.
\]

The extra \(2J_N\) is essential; omitting it produces a false finite covariance. The separate marginal evolution of \(D_N\) gives
\(\mathbb E J_N=1/(2N-5)\), for \(N\ge4\).

**3. Closure of auxiliary expectations.** Put \(\mu_N=\mathbb E D_N\), \(\ell_N=\mathbb E L_N\) and \(k_N=\mathbb E K_N\). The exact base at \(N=4\) is \((\mu_4,\ell_4,k_4)=(8/3,2,4/3)\). Conditioning on \(\mathcal F_N\) gives

\[
\mu_{N+1}=\left(1+\frac1{M_N}\right)\mu_N,\quad
\ell_{N+1}=\left(1-\frac2{M_N}\right)\ell_N+1,\quad
k_{N+1}=\left(1-\frac2{M_N}\right)k_N+\frac{\mu_N}{M_N}.
\]

Solving these recurrences gives

\[
\mu_N=\sqrt\pi\frac{\Gamma(N-1)}{\Gamma(N-3/2)},\quad
\ell_N=\frac{N^2-4N+6}{2N-5},\quad
k_N=\frac{\mu_N}{3}+\frac{4}{3(2N-5)}.
\]

**4. Exact covariance and positivity.** Expanding the product of the two updates in Step 1, using the joint increment identity in Step 2, and subtracting the product of the means yields

\[
 c_{N+1}=\left(1-\frac1{M_N}\right)c_N+
 \frac{2\mu_N\ell_N}{M_N^2}-\frac{k_N}{M_N}-\frac{2}{(2N-5)M_N}.
\]

Substituting the expressions in Step 3 gives the displayed recurrence in the Finding section. Its added numerator is strictly positive: since \(\mu_N\ge\mu_4=8/3\),

\[
 3\bigl[\mu_N(2N^2-8N+21)-10(2N-3)\bigr]
 \ge 16N^2-124N+258>0\qquad(N\ge4).
\]

The quadratic has value 18 at \(N=4\), and its derivative is positive for every \(N\ge4\). Therefore \(c_4=0\) and the recurrence imply \(c_N>0\) for all \(N\ge5\).

**5. The square-root constant.** Let \(a_N=c_N/\mu_N\), and let \(f_N\) be the positive additive term in the covariance recurrence. Since \(\mu_{N+1}=(1+1/M_N)\mu_N\),

\[
 a_{N+1}=\left(1-\frac{2}{M_N+1}\right)a_N+
 \frac{2}{M_N+1}\cdot\frac{M_N f_N}{2\mu_N}.
\]

The second target satisfies

\[
\frac{M_Nf_N}{\mu_N}
=\frac{2\ell_N}{M_N}-\frac13-\frac{10}{3(2N-5)\mu_N}
\longrightarrow\frac16.
\]

The recurrence is a convex averaging step whose weights \(2/(M_N+1)\) lie in \((0,1)\) and have divergent sum. Therefore \(a_N\to1/12\). Finally, the gamma-ratio asymptotic gives \(\mu_N/\sqrt N\to\sqrt\pi\), proving the claimed limit. The already-known marginal identities \(\operatorname{Var}(D_N)\sim(4-\pi)N\) and \(\operatorname{Var}(L_N)\sim N/12\) then yield the correlation rate.

## Verification
The standalone `check.py` uses `fractions.Fraction` to enumerate **every** uniform-edge attachment history from the initial triangle through size \(N=8\), and independently verifies all four moments \((\mathbb E D_N,\mathbb E L_N,\mathbb E K_N,\operatorname{Cov}(D_N,L_N))\) against the displayed recurrences. It also checks exact rational means, auxiliary closure, forcing factorizations, and signs through size \(N=150\). A finite floating-point diagnostic at \(N=30000\) tests the stated asymptotic scale. The general positivity and infinite limit are proved above, not inferred from these finite tests. Run `python3 check.py` alongside this document.

## Relationship to prior work
Krapivsky and Lucas [1], Appendix C, define exactly this HSC(2) edge-selection model, derive the two marginal expectation formulas and the marginal variances, and study the primordial degree separately from the degree-two count. Those individual marginals do **not** determine the covariance. The additional root-neighbor count and the root-degree-two exception close the joint recurrence.

Hartle and Krapivsky [2] analyze degree and leafdegree statistics in a single-edge preferential-attachment **tree**, not in a two-complex in which every newcomer creates two edges. Janson [3] treats degree-count fluctuation covariances in random recursive trees. Cooper and Uehara [4] use a different random \(k\)-tree clique-selection procedure. These are related models or marginal results, not statements of the joint HSC(2) covariance theorem. An equivalent theorem in less readily indexed literature cannot be ruled out by searching.

## Limitations
This is a self-reviewed result, not an independent audit. No multivariate central limit theorem, conditional law, or universality beyond the specified uniform-edge rule is established. The finite checker does not certify any infinite claim. The primary related 2010 and 2004 sources were compared from abstracts only; an unindexed result or a general theorem covering this specialization remains a historical-priority risk. The numerical diagnostic is not used as proof.

## References
[1] P. L. Krapivsky and M. Lucas, *Random Recursive Simplicial Complexes*, arXiv:2608.26547 (first posted 2026-08-27), Appendix C, equations (129)–(156). https://arxiv.org/abs/2608.26547

[2] H. Hartle and P. L. Krapivsky, *Leaves of preferential attachment trees*, arXiv:2602.01021 (first posted 2026-02-01). https://arxiv.org/abs/2602.01021

[3] S. Janson, *Asymptotic degree distribution in random recursive trees*, Random Structures & Algorithms 26 (2005), 69–83. https://doi.org/10.1002/rsa.20046

[4] C. Cooper and R. Uehara, *Scale Free Properties of Random k-Trees*, Mathematics in Computer Science 3 (2010), 489–496. https://doi.org/10.1007/s11786-010-0041-6
