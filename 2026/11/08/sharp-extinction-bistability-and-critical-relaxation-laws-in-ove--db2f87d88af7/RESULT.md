# Sharp extinction, bistability, and critical relaxation laws in overlap-reinforced hypergraph SIS closures

## Finding

The homogeneous single-pathogen, discrete-time **exponential mean-hazard closure** of an overlap-reinforced triangle-hypergraph SIS model has an exact fixed-point and extinction phase diagram at its pairwise spectral threshold. This is a result about that deterministic closure, **not** about the finite-state stochastic SIS process or all spatially heterogeneous initial conditions.

Let a finite, nonempty, simple 3-uniform hypergraph have a binary pairwise projection of constant degree \(d>0\), a constant number \(t>0\) of incident triangles per vertex, and a constant number \(q\geq0\) of unordered pairs of incident triangles meeting in one additional vertex. With recovery \(0<\mu<1\), pairwise intensity \(\beta_1=\mu/d\), triangle intensity \(\beta_h\geq0\), and overlap intensity \(\gamma\geq0\), put \(B=t\beta_h\) and \(C=q\gamma\). On the invariant homogeneous subspace the recurrence is

\[
 x_{s+1}=F(x_s)=(1-\mu)x_s+(1-x_s)\bigl(1-\exp[-\mu x_s-Bx_s^2-Cx_s^3]\bigr),\qquad 0\leq x_s\leq1.
\]

Define the two exact critical intensities and the quartic logarithmic coefficient by

\[
 B_2=\mu+\frac{\mu^2}{2},\qquad
 C_3=\mu+\mu^2+\frac{\mu^3}{3},\qquad
 D_4=\frac{(1+\mu)^4-1}{4}>0.
\]

Set \(u=(1+\mu)^{-1}\). If \(0\leq B<B_2\), then

\[
 T_B(x)=\frac{\log\!\left(\frac{1-x}{1-(1+\mu)x}\right)-\mu x-Bx^2}{x^3},\qquad 0<x<u,
\]

is strictly convex, diverges at both endpoints, and has a unique minimizer \(x_*(B)\). Write \(C_*(B)=T_B(x_*(B))\). Then the **exact numbers of positive fixed points** on \((0,1]\) are

\[
\begin{array}{c|c}
\text{parameter regime}&\text{number of positive fixed points}\\\hline
 B<B_2,\ C<C_*(B)&0\\
 B<B_2,\ C=C_*(B)&1\ \text{(double)}\\
 B<B_2,\ C>C_*(B)&2\\
 B=B_2,\ C\leq C_3&0\\
 B=B_2,\ C>C_3&1\\
 B>B_2&1.
\end{array}
\]

All parameters are assumed nonnegative as stated. In the two-positive-fixed-point regime, extinction and the upper endemic fixed point are locally attracting, and the lower positive fixed point is repelling. At \(C=C_*(B)\), the double positive fixed point has multiplier one. Whenever the positive fixed-point count is zero, every strictly positive homogeneous initial value converges to zero. The three sharp critical-decay laws are, for every \(x_0\in(0,1]\),

\[
\begin{aligned}
 B<B_2,\quad C<C_*(B):&\qquad \lim_{s\to\infty}s x_s=\frac{1}{B_2-B},\\
 B=B_2,\quad C<C_3:&\qquad \lim_{s\to\infty}\sqrt{s}\,x_s=\frac{1}{\sqrt{2(C_3-C)}},\\
 B=B_2,\quad C=C_3:&\qquad \lim_{s\to\infty}s^{1/3}x_s=\frac{1}{(3D_4)^{1/3}}.
\end{aligned}
\]

The third regime can be realized by positive overlap reinforcement only when \(q>0\). The graph's local overlap count thus controls whether its closure can realize the most degenerate critical law without introducing genuinely four-vertex hyperedges.

## Assumptions and scope

A *simple 3-uniform hypergraph* \(H=(V,E)\) has distinct three-element hyperedges, no multiplicities, and finite nonempty \(V\). Define \(A_{ij}=1\) if \(i\ne j\) and a hyperedge contains both \(i\) and \(j\), and zero otherwise. For \(i\ne j\), let \(m_{ij}\) be the number of hyperedges containing both. Set

\[
 d_i=\sum_j A_{ij},\qquad t_i=|\{e\in E:i\in e\}|,\qquad
 q_i=\sum_{j\ne i}\binom{m_{ij}}2.
\]

Assume \(d_i=d>0\), \(t_i=t>0\), \(q_i=q\ge0\) for every \(i\). Then \(q_i\) equals the number of unordered distinct hyperedge pairs through \(i\) sharing exactly one more vertex: two distinct triples cannot share more than two vertices. In a homogeneous infection state with marginal probability \(x\), every pairwise contact contributes \(x\), every active triangle contributes \(x^2\), and every overlapping pair of active triangles contributes \(x^3\) under the **mean-hazard replacement of products of distinct carrier indicators by products of marginal probabilities**. This is precisely the single-pathogen mean-hazard closure described in Liu and Schaposnik (2026, Section IV.1), applied to the regular-contact homogeneous invariant subspace.

The original stochastic infection event has conditional acquisition probability \(1-e^{-\lambda}\) at pressure \(\lambda\), and infected nodes independently recover with probability \(\mu\). The deterministic closure averages the pressure in the exponent before evaluating acquisition; this choice is not the alternative independent-Bernoulli product closure. Positive \(\gamma\) describes reinforcement due to overlap; no simultaneous competing or synergistic second-pathogen dynamics are asserted. Initial conditions are \(x_i(0)=x_0\in(0,1]\) for all \(i\). The pairwise criticality condition is \(\beta_1 d=\mu\).

For the complete triangle system on \(n\ge4\) vertices, \(d=n-1\), \(t=\binom{n-1}{2}\), and \(q=(n-1)\binom{n-2}{2}\). In a cyclic triple system \(\{i,i+1,i+2\}\) on \(n\ge6\) cyclic vertices, \((d,t,q)=(4,3,2)\); in the seven-point projective plane triangle system, \((d,t,q)=(6,3,0)\). These examples show that a genuine overlap statistic, not simply triangle count, enters the cubic threshold.

## Proof

**1. Exact reduction and invariance.** Pairwise, active-triangle and overlap pressures are \(\beta_1 d x\), \(\beta_h t x^2\), and \(\gamma q x^3\) by the definitions. With \(\beta_1d=\mu\), the hazard is \(h(x)=\mu x+Bx^2+Cx^3\), giving the displayed scalar map. For \(0\le x\le1\), the nonnegative recovery-survival and acquisition terms sum to at most \((1-\mu)x+(1-x)=1-\mu x\le1\). Thus the state interval is invariant. If \(0<\mu<1\) and \(x>0\), then \(F(x)\ge(1-\mu)x>0\).

**2. Exact positive-equilibrium equation.** The equation \(F(x)=x\) is equivalent to

\[
 \mu x=(1-x)(1-e^{-h(x)}).
\]

For \(x\ge u=(1+\mu)^{-1}\), the right side is strictly less than \(1-x\le\mu x\), so there is no positive equilibrium there. For \(0<x<u\), rearrangement and taking natural logarithms yields \(h(x)=L(x)\), where

\[
 L(x)=\log\frac{1-x}{1-(1+\mu)x}
     =\sum_{k=1}^{\infty}\frac{(1+\mu)^k-1}{k}x^k.
\]

The expansion converges absolutely on \((0,u)\), with strictly positive coefficients \(L_k=((1+\mu)^k-1)/k\). In particular, \(L_1=\mu\), \(L_2=B_2\), \(L_3=C_3\), \(L_4=D_4\). Dividing \(h(x)=L(x)\) by \(x^3\) yields the level-set equation \(C=T_B(x)\).

**3. Every equilibrium and its stability.** For \(B<B_2\), the exact power series is

\[
 T_B(x)=\frac{B_2-B}{x}+C_3+\sum_{k\ge4}L_kx^{k-3}.
\]

Its derivative tends to \(-\infty\) at zero and to \(+\infty\) at \(u\). Its second derivative is strictly positive because the first term contributes \(2(B_2-B)/x^3>0\), and every remaining nonconstant power contributes a nonnegative amount. Consequently there is one and only one interior global minimum, which is positive, and the level sets have exactly the stated cardinalities. For \(B=B_2\), the same series lacks the pole and is strictly increasing from its unattained boundary value \(C_3\) to infinity. For \(B>B_2\), the pole is negative, all derivatives of the remainder are positive, and \(T_B\) strictly increases from \(-\infty\) to infinity. This establishes all six fixed-point regimes.

To check local multipliers, differentiate the scalar map:

\[
 F'(x)=e^{-h(x)}\left[1+(1-x)h'(x)\right]-\mu>-\mu>-1.
\]

For \(0<x<u\), the sign of \(F(x)-x\) is the sign of \(h(x)-L(x)=x^3[C-T_B(x)]\). At a simple positive root, the derivative of \(F(x)-x\) has the opposite sign from \(T'_B(x)\). Thus a root on a decreasing branch of \(T_B\) has multiplier above one (repelling), whereas a root on an increasing branch has multiplier strictly between \(-1\) and one (attracting). At the unique minimum, the multiplier is exactly one. Near zero, the first nonvanishing coefficient of \(F(x)-x\) has the sign of \(B-B_2\), or of \(C-C_3\) when \(B=B_2\), establishing the stated local extinction or repulsion.

**4. Global extinction when there is no positive fixed point.** On \((0,u)\), \(F(x)-x\) has the sign of \(C-T_B(x)\). Thus in each zero-positive-root regime it is strictly negative. On \([u,1]\), it is strictly negative by the argument in step 2. Every orbit from \(x_0>0\) is therefore strictly decreasing and bounded below by zero. Its limit is a fixed point by continuity; because zero is the only one, its limit is zero.

**5. Exact asymptotic coefficients.** For \(0<x<u\), write

\[
 F(x)-x=(1-x)e^{-L(x)}\bigl(1-e^{-[h(x)-L(x)]}\bigr).
\]

The multiplier \((1-x)e^{-L(x)}\) tends to one as \(x\downarrow0\). The first nonzero term in \(h(x)-L(x)\) is respectively \(-(B_2-B)x^2\), \(-(C_3-C)x^3\), or \(-D_4x^4\) in the three stated extinction regimes. Hence \(F(x)=x-a x^{p+1}+O(x^{p+2})\), with \((p,a)=(1,B_2-B)\), \((2,C_3-C)\), or \((3,D_4)\). Since the orbit decreases to zero,

\[
 x_{s+1}^{-p}-x_s^{-p}\longrightarrow pa>0.
\]

Cesàro averaging the increments yields \(x_s^{-p}/s\to pa\), which is exactly the three displayed limits.

## Verification

The standalone \(verify.py\) accompanying this statement uses only the Python 3 standard library. It counts vertex degree, incident triangles and common-source triangle overlaps directly, and cross-checks the co-degree identity for complete three-uniform systems, cyclic triple systems and a seven-point projective-plane example. It calculates Taylor coefficients of the actual exponential update with exact rational arithmetic at multiple recovery probabilities and compares the coefficients independently with \(B_2\), \(C_3\), and \(D_4\). For several parameter pairs, it numerically locates the unique minimum of \(T_B\) and checks the predicted zero/two-root regions and the one-root regions. Three long iterates provide finite-horizon checks of the distinct asymptotic powers. Running \(python verify.py\) printed \(\texttt{PASS 166 check groups}\) in the preparation environment.

This finite computation does not prove strict convexity, uniqueness, or asymptotic limits; those are proved analytically above. Numerical root scans do not certify the absence of unobserved roots. The proof of the entire fixed-point census is the positive-coefficient series and its monotonicity/convexity analysis.

## Relationship to prior work

Liu and Schaposnik (arXiv:2610.26072v1, first public 19 October 2026) define overlap-reinforced HyCo-SIS and the one-pathogen exponential mean-hazard closure (Sections III.5 and IV.1). Their Proposition IV.1 identifies the pairwise linear threshold, explicitly leaving equality undecided; their main results address finite-time overlap effects, projections and representation of four-person interactions. The present result uses precisely that closure, but determines the complete homogeneous fixed-point diagram *at equality* and sharp decay coefficients, including the overlap-induced \(s^{-1/3}\) case.

Earlier work by Kiss, Iacopini, Simon and Georgiou (arXiv:2309.12752), and Kiss, Bick and Simon (arXiv:2410.15330), studies continuous-time polynomial mean-field dynamics with higher-order infection and its bifurcations. Those papers establish that higher-order contacts can produce backward transitions and bistability; that general phenomenon is not claimed as new here. Their continuous polynomial flows are not the exponential discrete-time hazard map studied here. In particular, their equilibrium equations and critical numerical coefficients are not the logarithmic level-set equation \(C=T_B(x)\) in this result.

Liang, Cui and Liu (arXiv:2408.08602) study a discrete-time **polynomial** hypergraph SIS recursion and sufficient stability conditions for general hypergraphs, but not the exponential-hazard homogeneous exact threshold curve or its three sharp critical relaxation rates. Related hypergraph epidemic threshold results of Higham and de Kergorlay (2021) and Higham and coauthors (2022) are based on distinct models and spectral sufficient conditions. These comparisons do not establish absolute novelty; unpublished or unindexed equivalents remain possible.

## Limitations

Only a single-pathogen *deterministic mean-hazard closure* is considered; it should not be confused with the exact stochastic model, with the independent-neighbor product closure, or with a general two-pathogen co-infection theorem. All agents start with an identical marginal infection probability. No convergence or equilibrium classification is asserted for heterogeneous starting vectors. The scope is finite, simple 3-uniform hypergraphs with constant \(d,t,q\). The model's exponential hazard is not a linearization of the hazard map; its full nonlinearity is crucial. At a double positive fixed point the derivative is one, so the proof does not claim exponential stability there. An independent scientific audit has not been carried out.

## References

1. K. Liu and L. P. Schaposnik, *Higher-Order Co-Infection on Hypergraphs*, arXiv:2610.26072v1 (19 October 2026), https://arxiv.org/html/2610.26072v1.
2. I. Z. Kiss, I. Iacopini, P. L. Simon and N. Georgiou, *Insights from exact social contagion dynamics on networks with higher-order structures*, arXiv:2309.12752 (2023), https://arxiv.org/pdf/2309.12752.
3. I. Z. Kiss, C. Bick and P. L. Simon, *Decoding how higher-order network interactions shape complex contagion dynamics*, arXiv:2410.15330 (2024), https://arxiv.org/html/2410.15330v1.
4. L. Liang, S. Cui and F. Liu, *Discrete-time SIS Social Contagion Processes on Hypergraphs*, arXiv:2408.08602 (2024), https://arxiv.org/html/2408.08602v1.
5. D. J. Higham and H.-L. de Kergorlay, *Epidemics on hypergraphs: spectral thresholds for extinction*, Proc. R. Soc. A 477 (2021), https://doi.org/10.1098/rspa.2021.0232.
6. D. J. Higham and collaborators, *Mean Field Analysis of Hypergraph Contagion Models*, SIAM J. Appl. Math. 82 (2022), https://doi.org/10.1137/21M1440219.
