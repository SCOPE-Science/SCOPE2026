# Rare-hub variance inflation and nonuniform Gaussian fluctuations in greedy wheel adsorption

## Finding

For every integer \(n\ge4\), form the *wheel* \(W_{n+1}=K_1\vee C_n\) from a cycle on \(n\) rim vertices and one universal hub. Give every vertex an independent continuous uniform priority, inspect vertices in increasing priority, and accept a vertex if no previously accepted neighbor exists. Let \(Y_n\) count the accepted vertices. This is the terminal monomer-blocking random sequential adsorption process.

Set
\[
c=\frac{1-e^{-2}}2,\qquad v=e^{-4},\qquad q_n=\frac1{n+1}.
\]
Let \(S_n\) denote the count for the same random greedy algorithm on an *isolated cycle* \(C_n\), and let \(P_m\) denote the count on a path of \(m\) vertices, with \(P_0=0\). The entire finite law factors as
\[
\mathcal L(Y_n)=q_n\delta_1+(1-q_n)\mathcal L(S_n),
\qquad S_n\stackrel d=1+P_{n-3}.
\]
In particular, for \(n\ge4\), \(\Pr(Y_n=1)=1/(n+1)\), and
\[
\operatorname{Var}(Y_n)=\frac n{n+1}\operatorname{Var}(S_n)
+\frac n{(n+1)^2}(\mathbb ES_n-1)^2.
\]
The asymptotic consequences, valid without subsequences, are
\[
\frac{Y_n-cn}{\sqrt n}\ \Longrightarrow\ N(0,v),\qquad
\operatorname{Var}(Y_n)=(v+c^2)n+O(1).
\]
These disagree at second-moment level: the weak Gaussian limit has variance \(v\), whereas the variance of the centered, scaled variables converges to \(v+c^2\). Numerically \(v\approx0.018315639\), \(v+c^2\approx0.205226907\), a factor of about \(11.205\).

Two sharper manifestations of the same boundary effect are proved. For every fixed \(0<\varepsilon<c\),
\[
\Pr\{Y_n\le\varepsilon n\}=\frac{1+o(1)}n.
\]
Moreover,
\[
\mathbb E[(Y_n-\mathbb EY_n)^3]=-c^3n^2+o(n^2),\qquad
\operatorname{Skew}(Y_n)\sim
-\frac{c^3}{(v+c^2)^{3/2}}\sqrt n.
\]
Thus a Gaussian distributional limit coexists with diverging negative standardized skewness and a polynomial lower tail.

## Assumptions and scope

The graph is exactly the unweighted simple wheel with \(n\ge4\) rim vertices. All \(n+1\) vertices are attempted once, at independent identically distributed continuous times; equivalent random vertex orders give the same law. Rejected attempts are not retried; acceptance is irreversible and excludes every neighbor. The count is measured after every attempt has occurred. No annealed random-graph structure or independent-per-site postprocessing is assumed.

## Proof

**1. Exact first-decision reduction.** Each vertex is equally likely to have first priority. If the hub is first, it is accepted and permanently blocks the entire rim, giving exactly one accepted vertex. If any rim vertex is first, that vertex is accepted and blocks the hub forever. The remaining rim vertices have a uniformly random relative order; deleting the selected rim vertex and its two rim neighbors leaves a path of \(n-3\) vertices. Greedy decisions on this path are independent of the rejected vertices' positions in the order. This proves both distributional identities and the law-of-total-variance formula above. For \(n\ge4\), the cycle always accepts at least two vertices, establishing the stated one-point probability.

**2. Exact path moments.** Let \(F_m(z)=\mathbb E z^{P_m}\), and take \(F_0(z)=F_{-1}(z)=1\). Conditioning on the first path vertex to be attempted gives, for every \(m\ge1\),
\[
F_m(z)=\frac z m\sum_{j=1}^{m}F_{j-2}(z)F_{m-j-1}(z).
\]
With \(H(x,z)=\sum_{m\ge0}F_m(z)x^m\), the recurrence is equivalent, as an identity of formal power series, to
\[
\partial_x H=z(1+xH)^2,\qquad H(0,z)=1.
\]
The first and second factorial-moment generating functions \(M(x)=\partial_zH(x,1)\) and \(B(x)=\partial_z^2H(x,1)\) therefore solve
\[
M'=\frac1{(1-x)^2}+\frac{2x}{1-x}M,\quad
B'=\frac{2x}{1-x}B+\frac{4x}{1-x}M+2x^2M^2,
\quad M(0)=B(0)=0.
\]
Direct differentiation verifies the unique formal solutions
\[
M(x)=\frac{1-e^{-2x}}{2(1-x)^2},
\]
\[
B(x)=\frac{x^2(1-e^{-2x})^2}{2(1-x)^3}
+\frac{2x-1+(2x+1)e^{-4x}}{4(1-x)^2}.
\]
Coefficient extraction at the isolated pole \(x=1\), using that the remaining numerators are entire, yields
\[
\mathbb EP_m=c(m+1)-e^{-2}+o(1),\qquad
\operatorname{Var}(P_m)=vm+O(1).
\]
Since \(S_n\stackrel d=1+P_{n-3}\) and \(2c+e^{-2}=1\), it follows that
\[
\mathbb ES_n=cn+o(1),\qquad
\operatorname{Var}(S_n)=vn+O(1).
\]
The linear path variance coefficient \(v\) and a corresponding central limit theorem were already established for one-dimensional blocking adsorption by Penrose and Sudbury; they are reconstructed or invoked here, not asserted as discoveries.

**3. Cycle central limit theorem and variance mismatch.** The one-dimensional monomer-blocking central limit theorem for a finite path at terminal time is Theorem 11 of Penrose--Sudbury (2005), giving \((P_m-\mathbb EP_m)/\sqrt m\Rightarrow N(0,v)\). The path reduction therefore gives \((S_n-cn)/\sqrt n\Rightarrow N(0,v)\). The hub-first event has probability \(q_n\to0\), so the total variation distance between \(Y_n\)'s law and \(S_n\)'s law is at most \(q_n\). Consequently \((Y_n-cn)/\sqrt n\Rightarrow N(0,v)\). Substituting the exact cycle mean and variance into the finite variance identity gives \(\operatorname{Var}(Y_n)=(v+c^2)n+O(1)\). The additional \(c^2n\) comes from \(q_n(1-q_n)(\mathbb ES_n-1)^2\), even though the corresponding event vanishes in probability.

**4. A fourth-moment bound for the cycle.** This step proves the sharp left tail and skewness rather than extrapolating from a central limit theorem. Give each rim vertex an independent uniform arrival mark. The terminal occupancy indicator at a vertex is determined by its radius-\(L\) neighborhood unless a strictly decreasing-priority path starting at that vertex extends outside this neighborhood. In a cycle there are only two candidate directions. For \(n>3L\), the probability of this event is at most \(2/(L+1)!\). Let \(\widetilde I_i\) be the occupancy indicator obtained by running greedy adsorption on the induced length-\(2L+1\) path centered at vertex \(i\), using those same marks. Then \(\widetilde I_i\) depends only on marks within distance \(L\), and \(\Pr(\widetilde I_i\ne I_i)\le2/(L+1)!\). The centered variables \(\widetilde I_i-\mathbb E\widetilde I_i\) have a dependency graph of maximum degree at most \(4L\). Expand the fourth centered moment of their sum. A term vanishes whenever its four indices have an isolated vertex in the induced dependency graph, by independence and centering. All remaining ordered index quadruples form either two adjacent pairs (at most \(O(n^2L^2)\) possibilities) or a connected graph (at most \(O(nL^3)\) possibilities). Each term has absolute value at most one. With \(L=\lceil6\log(n+1)\rceil\), the union bound makes the probability of any indicator mismatch superpolynomially small, and the difference between sums is at most \(n\). Therefore
\[
\mathbb E[(S_n-\mathbb ES_n)^4]
=O(n^2\log^2 n),\qquad
\mathbb E|S_n-\mathbb ES_n|^3
=O(n^{3/2}\log^{3/2}n)=o(n^2).
\]
For fixed \(0<\varepsilon<c\), the mean is separated from \(\varepsilon n\) by a positive multiple of \(n\). Markov's inequality applied to the fourth power yields
\[
\Pr(S_n\le\varepsilon n)=O(\log^2 n/n^2)=o(1/n).
\]
The exact two-component mixture now gives the claimed \(\Pr(Y_n\le\varepsilon n)\sim1/n\), because the hub-first outcome is eventually within the event.

**5. Third centered moment.** Write \(q=q_n\), \(\mu=\mathbb ES_n\), \(a=\mu-1\), \(V=\operatorname{Var}S_n\), and \(T=\mathbb E[(S_n-\mu)^3]\). Direct conditioning gives the exact identity
\[
\mathbb E[(Y_n-\mathbb EY_n)^3]
=(1-q)T+3q(1-q)aV+q(1-q)(2q-1)a^3.
\]
By step 4, \(T=o(n^2)\). Since \(a=cn+O(1)\), \(V=vn+O(1)\), and \(q=(n+1)^{-1}\), the last term is \(-c^3n^2+o(n^2)\) and the middle term is \(O(n)\). Dividing by \(\operatorname{Var}(Y_n)^{3/2}\) proves the skewness asymptotic.

## Verification

The accompanying `check.py` uses exact rational arithmetic to generate small-path laws from the first-decision recurrence and independently enumerates all priority permutations on paths, cycles, and wheels. It also checks coefficients of \(M\) and \(B\), exact wheel mixture laws, and the finite variance identity. The program uses only the Python standard library and is executable as `python check.py`. It reports 62 assertions passed. These finite checks independently test key algebra but do not prove infinite asymptotics, which are established above.

## Relationship to prior work

Penrose and Sudbury (2005), Theorem 11, already prove the path blocking-adsorption central limit theorem and the variance coefficient \(v=e^{-4}\) at terminal time. Their normal-approximation theorem for general graphs assumes uniformly bounded degree; the wheels here have diverging hub degree. Krivelevich, Mészáros, Michaeli, and Shikhelman (first public version July 16, 2019) investigate random greedy maximal-independent-set densities on general graph sequences and include path-type limits; density convergence does not determine the unnormalized second or third moments and no wheel-specific rare-hub theorem was located in the inspected paper.

The distinction here is the **simultaneous, exact wheel law**, a Gaussian weak limit with a different limiting variance, the sharp rare left-tail constant, and diverging skewness. This is a boundary of moment transfer from low-degree local limits, not a claim that the underlying one-dimensional central limit theorem or elementary mixture calculus is new. Priority-to-adsorption equivalence and the path first-decision recurrence are standard. Historical exhaustiveness is not certified: further wheel-specific or generic high-degree mixture results could cover the conclusion.

## Limitations

The mechanism depends on one universal hub; the result is not asserted for arbitrary growing-degree graphs, graph sequences with several hubs, nonuniform priority laws, or repeated adsorption. The Gaussian limit is distributional, not a limit in quadratic mean or a variance-normalized central limit theorem. The fourth-moment estimate is sufficient for a sharp rare-event asymptotic, not an optimal concentration rate. Independent mathematical verification and exhaustive historical-priority determination have not been performed.

## References

- M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, Annals of Applied Probability 15 (2005), 853–889; first public arXiv version March 24, 2005, https://arxiv.org/abs/math/0503519. Relevant: definition of blocking RSA and Theorems 7 and 11.
- M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, first public arXiv version July 16, 2019, https://arxiv.org/abs/1907.07216; later journal version, https://doi.org/10.1002/rsa.21200. Relevant: greedy graph process, path densities and concentration regime.
