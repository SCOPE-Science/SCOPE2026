# Exponential vacancy law and Gaussian fluctuations for dimer jamming on complete split graphs

## Finding
Let \(S_{a,b}=K_a\vee\overline{K}_b\) be the complete split graph with a clique of size \(a\) and an independent set of size \(b\). Sequentially deposit a dimer on one edge chosen uniformly among all edges with two uncovered endpoints, and remove its endpoints from future consideration. Let \(B_{a,b}\) be the number of independent-set vertices left uncovered at termination.

For every pair of nonnegative integers \(a,b\), the full law \(Q_{a,b}(z)=\mathbb E[z^{B_{a,b}}]\) is determined by the exact rational recurrence
\[
Q_{a,b}(z)=\frac{a-1}{a-1+2b}Q_{a-2,b}(z)+\frac{2b}{a-1+2b}Q_{a-1,b-1}(z),\qquad a\ge2,
\]
where the second summand is omitted if \(b=0\), with \(Q_{0,b}(z)=z^b\), \(Q_{1,b}(z)=z^{b-1}\) for \(b\ge1\), and \(Q_{1,0}(z)=1\).

Fix \(\alpha,\beta>0\), and for each positive integer \(r\) take \(a_r=\lfloor\alpha r\rfloor\), \(b_r=\lfloor\beta r\rfloor\). Then
\[
\frac{B_{a_r,b_r}}r\xrightarrow{\mathbb P}\beta e^{-\alpha/\beta},
\qquad
\sqrt r\left(\frac{B_{a_r,b_r}}r-\beta e^{-\alpha/\beta}\right)
\xrightarrow{\mathrm d}\mathcal N\left(0,\;\beta\left[4e^{-c}-(c+2)^2e^{-2c}\right]\right),
\quad c=\alpha/\beta.
\]
The convergence of the normalized uncovered count also holds in every fixed finite \(L^p\). With \(a=b=r\), the graph has a perfect matching for all \(r\), yet the irreversible process leaves asymptotically \(r/e\) uncovered vertices (in probability), with limiting covered-vertex fraction \(1-1/(2e)\). The number of dimers divided by the maximum matching size converges to the same \(1-1/(2e)\).

## Assumptions and scope
The graph is finite, simple and undirected; every available edge has the same strictly positive deposition-attempt rate, and every accepted deposition irreversibly occupies its two endpoints. Attempts that overlap already occupied vertices do nothing. Equivalently, independently exponentially timed edge attempts with equal rates generate the uniform-available-edge sequence. The law concerns terminal jammed states, not a fixed physical waiting time. The central-limit assertion uses the stated integer rounding to control deterministic centering at the fluctuation scale. More generally, the law of large numbers holds whenever \(a_r/r\to\alpha>0\), \(b_r/r\to\beta>0\).

## Proof
**Exact finite law.** If \(a\) clique and \(b\) independent vertices remain, exactly \(\binom a2\) available edges are internal to the clique and exactly \(ab\) join the two parts. The cross-edge probability for \(a\ge2\) is \(2b/(a-1+2b)\), after which the residual graph is \(S_{a-1,b-1}\); an internal edge leaves \(S_{a-2,b}\). The boundary graphs with zero or one clique vertex are terminal or have one forced cross-edge deposition. Conditioning on the first dimer yields the recurrence and its base cases without approximation.

**Macroscopic law.** Temporarily assign each currently available edge an independent rate-\(1/r\) exponential clock. Let \(A_r(t),B_r(t)\) be the uncovered clique and independent counts and put \(X_r(t)=A_r(t)/r\), \(Y_r(t)=B_r(t)/r\). Memorylessness shows that this is the stated uniform-edge process with random waiting times. Its exact drift is
\[
\left(-X_r(X_r+Y_r)+X_r/r,\;-X_rY_r\right).
\]
On any fixed time interval the jumps have norm at most \(2/r\), the total rate is bounded by a constant times \(r\), and the quadratic variation of each scaled compensated coordinate is \(O(1/r)\). The drift is uniformly Lipschitz on the compact initial-state rectangle, up to a uniformly \(O(1/r)\) error. Doob's inequality and Gronwall's inequality thus give uniform-in-probability convergence on compact time intervals to the deterministic solution
\[
\dot x=-x(x+y),\qquad\dot y=-xy,\qquad x(0)=\alpha,\quad y(0)=\beta.
\]
Direct differentiation proves the first integral
\[
\frac{x(t)}{y(t)}-\log\frac{y(t)}\beta=\frac\alpha\beta.
\]
Because \(\dot x\le-x^2\), one has \(x(t)\to0\); the first integral forces \(y(t)\to y_*=\beta e^{-\alpha/\beta}>0\). For every fixed \(T\), the number of future cross-edge depositions after time \(T\) cannot exceed the number of uncovered clique vertices then, giving the deterministic pathwise sandwich
\[
Y_r(T)-X_r(T)\le B_{a_r,b_r}/r\le Y_r(T).
\]
First let \(r\to\infty\), then \(T\to\infty\), proving convergence in probability. Uniform boundedness of the scaled counts implies convergence in each finite \(L^p\).

**Fluctuations.** Write \(c=\alpha/\beta\) and let \(F(x,y)=x/y-\log y\), defined for \(y>0\). Along the deterministic trajectory, \(\nabla F\cdot(\dot x,\dot y)=0\). On the event that the terminal independent count exceeds \(\eta r\) for a fixed \(0<\eta<y_*\), which has probability tending to one by the just-proved law of large numbers, every intermediate count also exceeds \(\eta r\). For the embedded discrete chain, a cross-edge step changes \(F\) by
\[
\Delta_{\rm cross}F=\frac{x}{r y^2}+O(r^{-2}),
\]
whereas a clique-internal step changes it by
\[
\Delta_{\rm clique}F=-\frac{2}{r y}+O(r^{-2}),
\]
uniformly for \(y\ge\eta\) and bounded \(x\). Conditional probabilities are \(2y/(x+2y)+O(r^{-1})\) and \(x/(x+2y)+O(r^{-1})\); the displayed leading conditional mean vanishes. Thus each expected stepwise drift of \(F\) is \(O(r^{-2})\). There are at most \((a_r+b_r)/2=O(r)\) accepted steps, so their cumulative drift is \(O(r^{-1})\), negligible after multiplying by \(\sqrt r\).

The centered increments of \(\sqrt r F\) form a martingale array with maximal jump \(O(r^{-1/2})\). Its predictable quadratic variation converges to
\[
V_F=\int_0^\infty\left(\frac{x(t)^3}{y(t)^3}+\frac{2x(t)^2}{y(t)^2}\right)\,dt.
\]
To justify the infinite-time limit, the fixed-interval fluid approximation yields convergence of the finite-time quadratic variations. Past a fixed time \(T\), at most \(A_r(T)\) more depositions occur; on \(y\ge\eta\), the remaining quadratic variation is bounded by \(C A_r(T)/r\), whose limiting bound \(Cx(T)\) vanishes as \(T\to\infty\). The usual bounded-increment martingale central limit theorem is therefore applicable, including the stopped process at the harmless lower barrier \(y=\eta\).

Substitute \(u=x/y=c+\log(y/\beta)\). Since \(dy/dt=-xy\), the integral evaluates exactly:
\[
V_F=\frac{e^c}{\beta}\int_0^c u(u+2)e^{-u}\,du
=\frac{4e^c-(c+2)^2}{\beta}.
\]
Initially \(F(X_r(0),Y_r(0))=c-\log\beta+O(r^{-1})\). At termination, \(A_r(\infty)\in\{0,1\}\) and \(F(X_r(\infty),Y_r(\infty))=-\log(B_{a_r,b_r}/r)+O(r^{-1})\) on the high-probability lower-barrier event. The martingale CLT followed by the delta method at \(y_*=\beta e^{-c}\) gives the claimed normal law with variance \(y_*^2V_F=\beta[4e^{-c}-(c+2)^2e^{-2c}]\).

**Balanced perfect-matchable case.** When \(a=b=r\), match each independent vertex to one clique vertex to exhibit a perfect matching of size \(r\). Every realized greedy terminal state has at most one uncovered clique vertex, so its unmatched fraction differs from \(B_{r,r}/(2r)\) by at most \(1/(2r)\). Therefore its occupied fraction and dimer-count ratio both tend to \(1-1/(2e)\). For instance the exact finite law is \(Q_{4,4}(z)=24/55+(8/15)z^2+(1/33)z^4\).

## Verification
Run `python verify_exact.py` for an independent labeled-vertex exact recursion versus the two-count rational recurrence on all \(49\) choices \(0\le a,b\le6\). Run `python verify_limits.py` for the symbolic ODE invariant and closed quadratic-variation integral, plus independent, seeded large-finite stochastic checks at three initial ratios. The exact checker uses only Python's standard library; the independent fluctuation checker uses the two packages listed in `requirements.txt`. These computations validate algebra and finite cases, not the infinite limit in isolation. The infinite statements follow from the probabilistic proof above.

## Relationship to prior work
The model is the graph-edge version of irreversible random sequential adsorption and of edge-uniform random greedy matching. Cadilhe, Araújo and Privman (arXiv:cond-mat/0611413, first posted 2006-11-15) survey jammed-state coverage, including finite lattice and patterned substrates, but do not provide this complete-split-graph law. Pippenger (1989) treats graph RSA with regular low-cycle assumptions and an edge variant; these do not imply the present dense, triangle-rich two-population fluctuation theorem on the supplied published description. Dyer and Frieze (1991) study the same edge-uniform matching rule on arbitrary fixed graphs, primarily bounds and sparse classes; their inaccessible full text is a residual historical overlap risk. Gamarnik and Goldberg (arXiv:0807.1277, 2008) analyze regular graphs with bounded degree and large girth, including bounded-degree concentration, while the split graphs here are dense and strongly irregular. Krivelevich, Mészáros, Michaeli and Shikhelman (2023) give a local-limit framework for random greedy independent sets and relate matching to the line graph; the required local-finite setting is not this dense growing-degree line-graph family. The finite recurrence, two-parameter jamming law and explicit Gaussian variance are a joint claim; a generic algorithm definition or unrelated upper bound does not establish them.

## Limitations
The theorem assumes equal edge attempt rates, independent exponentially distributed waiting times (or their discrete uniform-available-edge equivalent), an initially empty graph, and fixed strictly positive limiting proportions. It is not a finite-time kinetic rate law or a result for weighted rates, varying ratios with \(\beta\to0\), or spatially local geometric adsorption. A source-priority search, including checked full texts and an attempted inaccessible primary text, cannot rule out obscure equivalent treatments. Independent external scientific validation has not been performed.

## References
- A. Cadilhe, N. A. M. Araújo and V. Privman, *Random sequential adsorption: from continuum to lattice and pre-patterned substrates*, arXiv:cond-mat/0611413 (2006), https://arxiv.org/abs/cond-mat/0611413.
- N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics 2 (1989), 393–401, https://doi.org/10.1137/0402034.
- M. Dyer and A. Frieze, *Randomized greedy matching*, Random Structures & Algorithms 2 (1991), 29–45, https://doi.org/10.1002/rsa.3240020104.
- D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections*, arXiv:0807.1277 (2008), https://arxiv.org/abs/0807.1277.
- M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, Random Structures & Algorithms 64 (2024), 986–1015, https://doi.org/10.1002/rsa.21200.
