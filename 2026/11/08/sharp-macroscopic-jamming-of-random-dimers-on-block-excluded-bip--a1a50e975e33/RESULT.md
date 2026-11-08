# Sharp macroscopic jamming of random dimers on block-excluded bipartite networks

## Finding

Let \(A_n,B_n\) be disjoint vertex classes of size \(n\). Choose subsets \(A_n^0\subset A_n\) and \(B_n^0\subset B_n\) of sizes \(a_n,b_n\). Remove all edges between \(A_n^0\) and \(B_n^0\) from the complete bipartite graph; retain every other cross-edge. On this graph, repeatedly choose an edge uniformly from those with both endpoints uncovered, occupy its endpoints by an irreversible dimer, and stop when no such edge remains. Let \(R_n\) be the number of uncovered vertices **in each side** at termination (the two counts are equal).

For any \(\alpha,\beta\in(0,1)\) and integer sequences satisfying \(a_n/n\to\alpha\), \(b_n/n\to\beta\),
\[
\frac{R_n}{n}\xrightarrow{\mathbb P}L(\alpha,\beta),\qquad
\frac{\mathbb E R_n}{n}\longrightarrow L(\alpha,\beta),
\]
where
\[
L(\alpha,\beta)=
\begin{cases}
\displaystyle\exp\!\left(\frac{(1-\alpha)\log\alpha-(1-\beta)\log\beta}{\beta-\alpha}\right),&\alpha\ne\beta,\\[5pt]
\displaystyle\alpha\exp\!\left(-\frac{1-\alpha}{\alpha}\right),&\alpha=\beta.
\end{cases}
\]
Every such limiting density is strictly positive. The graph has a perfect matching exactly when \(a_n+b_n\le n\). In the asymptotically perfect-matchable region \(\alpha+\beta\le1\),
\[
0<L(\alpha,\beta)\le \frac{1}{2e},
\]
with equality only at \(\alpha=\beta=1/2\). In particular, even a family of graphs with perfect matchings can leave a sharp fraction \(1/(2e)\) of **each** side uncovered under the random dimer process. The fraction of vertices covered at equality is \(1-1/(2e)\).

## Assumptions and scope

The graphs are deterministic, simple, finite, and bipartite; the deleted edges form one complete bipartite rectangle. Only the four vertex types (bad/good in the two sides) matter. Edges all have equal positive arrival rates, and every accepted dimer permanently excludes its two endpoints. Uniformly choosing from currently allowable edges gives the same order law as independent continuous exponential edge clocks, regardless of the common clock-rate multiplier. The limit concerns fixed positive limiting blocked proportions below one, not a joint microscopic regime with \(\alpha\) or \(\beta\) tending to zero.

## Proof

**1. Exact finite-state chain.** At any time let \((x,u,y,v)\) be the respective numbers of uncovered vertices in \(A_n^0,A_n\setminus A_n^0,B_n^0,B_n\setminus B_n^0\). There are exactly \(xv\) admissible bad-A/good-B edges, \(uy\) good-A/bad-B edges, and \(uv\) good-A/good-B edges, with no bad-A/bad-B edges. The next accepted edge is chosen with the three corresponding probabilities, normalized by \(xv+uy+uv\). In particular, the two sides always retain the same number of uncovered vertices.

**2. Hydrodynamic law.** Give each graph edge an independent rate \(1/n\) Poisson arrival process. For normalized counts \(Z_n=(X_n,U_n,Y_n,V_n)=(x,u,y,v)/n\), the exact drift in continuous time is
\[
b(X,U,Y,V)=(-XV,-U(Y+V),-YU,-V(X+U)).
\]
For each coordinate and fixed \(T<\infty\), the martingale part has jumps of magnitude \(1/n\) and predictable quadratic variation at most \(T/n\). Doob's inequality and Gronwall's inequality, using that \(b\) is Lipschitz on \([0,1]^4\), imply uniform convergence in probability on \([0,T]\) to the unique solution \((X,U,Y,V)\) of \(z'=b(z)\), initially \((\alpha,1-\alpha,\beta,1-\beta)\). No asymptotic independence assumption is used.

**3. Exact solution of the relevant limiting dynamics.** The equality \(X+U=Y+V=:K\) is preserved. Set
\[
\theta(t)=\exp\!\left(-\int_0^t K(s)\,ds\right),\qquad
W(t)=\int_0^t\theta(s)\,ds.
\]
Then
\[
U=(1-\alpha)\theta,\quad V=(1-\beta)\theta,\quad
X=\alpha e^{-(1-\beta)W},\quad
Y=\beta e^{-(1-\alpha)W}.
\]
For \(\alpha\ne\beta\), the balance identity \(X-Y=(\alpha-\beta)\theta\) gives the exact scalar equation
\[
\frac{dW}{dt}=\theta(W)=\frac{\alpha e^{-(1-\beta)W}-\beta e^{-(1-\alpha)W}}{\alpha-\beta},
\quad W(0)=0.
\]
Its right side is positive for \(0\le W<W_*\) and zero first at
\[
W_* = \frac{\log(\beta/\alpha)}{\beta-\alpha}>0.
\]
Local uniqueness and monotonicity imply \(W(t)\uparrow W_*\) as \(t\to\infty\); thus \(\theta(t)\to0\), both good populations vanish, and both bad populations tend to the same positive value
\[
X(\infty)=Y(\infty)=\alpha e^{-(1-\beta)W_*}=L(\alpha,\beta).
\]
For \(\alpha=\beta=a\), equality of the two bad and good populations instead yields, by \(d\theta/dW=-(X+U)\),
\[
\theta(W)=e^{-(1-a)W}(1-aW),\quad W(t)\uparrow 1/a,
\]
so that \(X(\infty)=Y(\infty)=a e^{-(1-a)/a}\). This proves the continuous formula at the diagonal as well.

**4. From finite time to terminal jamming.** After any fixed \(T\), every additional loss of a bad-A vertex consumes a previously uncovered good-B vertex. Consequently,
\[
X_n(T)-V_n(T)\le X_n(\infty)\le X_n(T),
\]
and similarly \(Y_n(T)-U_n(T)\le Y_n(\infty)\le Y_n(T)\). The terminal uncovered density on either side is \(R_n/n=X_n(\infty)+U_n(\infty)\), and \(0\le U_n(\infty)\le U_n(T)\). Therefore it lies between \(X_n(T)-V_n(T)\) and \(X_n(T)+U_n(T)\). First let \(n\to\infty\) at fixed \(T\), and then \(T\to\infty\). Step 3 gives \(U(T)+V(T)\to0\) and \(X(T)\to L\), proving convergence in probability at the actual jammed terminal state. Since \(0\le R_n/n\le1\), convergence of expectations follows by boundedness.

**5. Hall feasibility and sharp inefficiency.** All bad-A vertices must match to good-B vertices, which is possible only if \(a_n\le n-b_n\); the symmetric condition is identical. If \(a_n+b_n\le n\), first match the two bad classes into opposite good classes and then match the remaining good vertices, proving sufficiency. Thus \(a_n+b_n\le n\) is the exact perfect-matching criterion.

For \(\alpha\ne\beta\), define \(g(s)=\log s+1-1/s\). The formula above is equivalently
\[
\log L(\alpha,\beta)
=\frac{1}{\beta-\alpha}\int_\alpha^\beta g(s)\,ds,
\]
with the integral interpreted in either orientation. The same expression holds on the diagonal by continuity. Since \(g'(s)=1/s+1/s^2>0\) and \(g''(s)=-1/s^2-2/s^3<0\), Jensen's inequality and \((\alpha+\beta)/2\le1/2\) yield
\[
\log L\le g\!\left(\frac{\alpha+\beta}{2}\right)\le g(1/2)=\log(1/(2e)).
\]
Strict concavity and strict monotonicity give equality precisely when \(\alpha=\beta=1/2\). Integer choices \(a_n=b_n=\lfloor n/2\rfloor\) attain the limit while satisfying the exact Hall condition. This completes the proof.

## Verification

The included `verify_block.py` implements the exact four-count transition kernel using rational arithmetic for all small states with \(2\le n\le8\), checks terminal probabilities, support and Hall obstructions, and independently runs seeded event-driven experiments for larger sizes. It also evaluates the closed formula and strict-concavity bound at several asymmetric and symmetric parameter pairs. Execute `python verify_block.py` with Python 3; it requires only the standard library. These computations check finite cases and numerical consistency; the universal probability limit and sharp bound are established by the analytical argument above.

## Relationship to prior work

Random sequential adsorption on graphs and the interpretation through random edge orders are classical (Penrose--Sudbury, 2005). Dyer--Frieze (1991) analyzes randomized greedy matching on fixed graphs, including worst-case behavior, and Arnosti (2021) compares randomized greedy algorithms on bipartite random graph ensembles. The precise two-block exclusion family, the two-parameter explicit limiting jam density, and the sharp \(1/(2e)\) worst feasible density are not implied by the **examined** theorems in those sources. The last statement is a literature-comparison assessment rather than a claim of global priority.

## Limitations

The assertion is asymptotic for two fixed positive blocked proportions; it gives neither a central-limit theorem nor a finite-size error bound. It does not address weighted, adaptive, or online-vertex matching algorithms. The inaccessible full text of Dyer--Frieze (1991) leaves residual uncertainty about historical formulations, despite the comparison with its publicly available abstract and with later full-text discussions. Independent validation and an exhaustive historical-priority assessment have not been performed.

## References

1. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, Ann. Appl. Probab. 15 (2005), 853--889, arXiv:math/0503519 (first arXiv version 2005-03-24), https://arxiv.org/abs/math/0503519.
2. M. Dyer and A. Frieze, *Randomized greedy matching*, Random Structures & Algorithms 2 (1991), 29--45, https://doi.org/10.1002/rsa.3240020104.
3. N. Arnosti, *Greedy Matching in Bipartite Random Graphs*, Stochastic Systems 12 (2022), 133--150, first published online 2021-11-02, https://doi.org/10.1287/stsy.2021.0082.
