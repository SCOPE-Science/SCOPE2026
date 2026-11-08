# Critical stationary half-Gaussian crossover in a source-pinned bipartite contact process

## Finding

Let \(K_{n,n}\) have a permanently infected vertex in its first part. Every other vertex recovers at rate one, and every directed edge transmits infection to a susceptible endpoint at rate \(\lambda_n=(1+c/\sqrt n)/n\), for a fixed \(c\in\mathbb R\) and sufficiently large integers \(n\ge2\) for which \(\lambda_n>0\). Denote the unique stationary numbers of infected *ordinary* vertices in the two parts by \(X_n,Y_n\), and put \(W_n=(X_n+Y_n)/\sqrt n\).

Then the **stationary critical-window law** is

\[
W_n\ \xrightarrow{\mathrm d}\ W_c,\qquad
\mathbb P(W_c\in dw)=\frac{\exp(cw-w^2/4)}{\sqrt\pi\,e^{c^2}(1+\operatorname{erf}(c))}\,\mathbf1_{\{w\ge0\}}\,dw.
\]

Moreover, \((X_n-Y_n)/\sqrt n\to0\) in \(L^2\), so the two parts each carry asymptotically half of the random total. The first moments converge:

\[
\lim_{n\to\infty}\frac{\mathbb E(X_n+Y_n)}{\sqrt n}
=2c+\frac{2e^{-c^2}}{\sqrt\pi(1+\operatorname{erf}(c))}.
\]

At the unshifted critical value \(c=0\), the limit is exactly half-normal with density \(e^{-w^2/4}/\sqrt\pi\) and mean \(2/\sqrt\pi\). The source has stationary activity of order \(\sqrt n\) in a nonreversible two-population model, despite being just one permanently active vertex.

## Assumptions and scope

The graph has two classes of \(n\) labeled vertices each, with every cross-edge and no within-class edge. Exactly one distinguished vertex in the first class is permanently infected and never recovers. Each of the remaining \(2n-1\) vertices has binary susceptible/infected state. An infected ordinary vertex recovers at rate one; each infected-to-susceptible adjacent pair transmits at rate \(\lambda_n\), with rates added when several infected neighbors contact a susceptible vertex. All processes are continuous-time Markov chains. Stationarity refers to their unique finite-state invariant distributions, not to an epidemic conditioned on survival. The limiting assertion is for fixed finite \(c\) as \(n\to\infty\), with no uniformity assertion for \(c\) depending on \(n\).

## Proof

**1. Exact two-coordinate reduction.** The infection counts \((X,Y)\) form an irreducible Markov chain on \(\{0,\ldots,n-1\}\times\{0,\ldots,n\}\), with nonzero rates

\[
\begin{aligned}
(x,y)&\to(x+1,y)&:&\quad \lambda_n y(n-1-x),\\
(x,y)&\to(x-1,y)&:&\quad x,\\
(x,y)&\to(x,y+1)&:&\quad \lambda_n(x+1)(n-y),\\
(x,y)&\to(x,y-1)&:&\quad y.
\end{aligned}
\]

The permanent source makes the chain irreducible. Write \(a_n=n\lambda_n=1+c/\sqrt n\), \(S=X+Y\), \(D=X-Y\), and \(B\) for the sum of the two birth rates. Elementary expansion gives the exact identities

\[
B=a_n(S+1)-\lambda_n\big[(S-D)+(S^2-D^2)/2\big],
\quad \mathcal L D=-(1+a_n)D-a_n,
\quad \mathcal L S=B-S.
\]

**2. Stationary moment bounds.** Set \(Q=B+S\). Because every jump of \(D\) has magnitude one,

\[
\mathcal L(D^2)=-2(1+a_n)D^2-2a_nD+Q,
\qquad Q\le a_n(S+1)+S.
\]

For sufficiently large \(n\), \(a_n\) stays between two positive constants. Stationarity of \(D\) shows \(\mathbb ED=-a_n/(1+a_n)\). Taking stationary expectations in the previous equation yields \(\mathbb ED^2\le C_c(\mathbb ES+1)\). Next, stationarity of \(S\) and the fact \(S-D=2Y\ge0\) give

\[
\frac{\lambda_n}{2}\mathbb ES^2
=(a_n-1)\mathbb ES+a_n
-\lambda_n\mathbb E(S-D)
+\frac{\lambda_n}{2}\mathbb ED^2.
\]

Using \(|a_n-1|=|c|/\sqrt n\), \(\lambda_n\asymp1/n\), and \(\mathbb ES\le\sqrt{\mathbb ES^2}\) therefore gives

\[
\mathbb ES^2\le C_c\big(n+\sqrt n\,\mathbb ES\big),
\quad\text{hence}\quad\sup_{n\ge N_c}\mathbb E(S/\sqrt n)^2<\infty,
\qquad\mathbb ED^2=O_c(\sqrt n).
\]

Thus the laws of \(W_n\) are tight and \(D/\sqrt n\to0\) in \(L^2\).

**3. Limiting stationary equation.** Let \(f\in C_c^3([0,\infty))\), and accelerate time by \(\sqrt n\). Taylor expansion of the generator of \(W=S/\sqrt n\), with derivatives evaluated at \(W\), gives

\[
\mathcal A_n f=(B-S)f'+\frac{B+S}{2\sqrt n}f''+R_n,
\quad \mathbb E|R_n|\le C_f\frac{\mathbb E(B+S)}n=O_{c,f}(n^{-1/2}).
\]

By the exact identity in step 1, the stationary moment bounds, and \(\mathbb ED^2=O_c(\sqrt n)\), these two coefficients approach in stationary \(L^1\), respectively,

\[
1+cW-W^2/2,\qquad W.
\]

It follows that any weak subsequential limit \(\nu\) of the stationary laws obeys

\[
\int_0^\infty\!\left[(1+cw-w^2/2)f'(w)+wf''(w)\right]\nu(dw)=0,
\qquad f\in C_c^3([0,\infty)).
\]

**4. Identification and normalization.** This is the stationary weak equation for the one-dimensional diffusion with drift \(b(w)=1+cw-w^2/2\) and diffusion coefficient \(\sqrt{2w}\). On \((0,\infty)\), its stationary Fokker--Planck equation has constant probability flux \(J=b(w)p(w)-(wp(w))'\). Because the test functions in the weak equation may independently prescribe their value and derivative at zero, and the speed-density solutions are locally integrable there, the boundary term forces both \(J=0\) and the absence of an atom at zero. The zero-flux equation gives

\[
\frac{p'(w)}{p(w)}=c-w/2,
\quad\text{so}\quad p(w)=Z_c^{-1}e^{cw-w^2/4}.
\]

The positive integrable solution is unique. Completing the square gives \(Z_c=\sqrt\pi e^{c^2}(1+\operatorname{erf}(c))\). Therefore all subsequences have the same limit. Finally, bounded second moments make \(W_n\) uniformly integrable, hence the means converge to \(Z'_c/Z_c\), yielding the displayed formula.

## Verification

The accompanying executable `verify.py` constructs the full finite Markov generator independently for multiple finite sizes and critical-window parameters; it solves the stationary linear equations and checks probability normalization, the exact stationary \(D\)-balance, the \(S\)-balance, and the approach of the rescaled mean toward its analytic limit. It also checks the symbolic generator identities and the Gaussian normalization/mean formula. Numerical finite-size computations check only their stated finite cases; all-\(n\) and scaling conclusions follow from the proof above.

## Relationship to prior work

Dolgoarshinnykh and Lalley (2005) prove critical diffusion scaling for an *unforced, one-population*, complete-mixing SIS epidemic with an absorbing zero state. That theorem does not provide a source-pinned stationary distribution on a balanced two-part graph. Peterson (2010) studies extinction thresholds and supercritical quasi-stationarity in complete-graph contact processes with vertex-dependent rates; it has neither the fixed source nor the present critical-window invariant law. Foxall (2014) establishes general finite-state convergence and monotonicity for spontaneous infection models, but does not calculate this two-population scaling distribution. Previous related finite-hub source-pinned calculations concern stars or \(K_{2,n}\) with a bounded hub class; neither implies the balanced \(K_{n,n}\) law with two growing classes. These comparisons do not establish absolute historical priority.

## Limitations

This theorem concerns only the stationary distribution for the specified SIS dynamics and fixed \(c\); it does not claim mixing-time asymptotics, paths started from arbitrary initial conditions, behavior under a finite number of nonpermanent sources, or uniformity outside the stated critical window. Published-index searches are not exhaustive, so potential unindexed literature on balanced bipartite source-pinned epidemics remains a historical-priority risk. The law is obtained by identifying a critical stationary diffusion limit, not by finding a finite-\(n\) closed-form invariant measure.

## References

1. R. G. Dolgoarshinnykh and S. P. Lalley, *Critical Scaling for the Simple SIS Stochastic Epidemic*, first public preprint 2005-12-12, https://arxiv.org/abs/math/0512252.
2. J. Peterson, *The contact process on the complete graph with random vertex-dependent infection rates*, first public preprint 2010-05-05, https://arxiv.org/abs/1005.0810.
3. E. Foxall, *Convergence and Monotonicity for a Model of Spontaneous Infection and Transmission*, Advances in Applied Probability 46 (2014), 560–584, https://doi.org/10.1239/aap/1401369707.
