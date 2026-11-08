# A quadratic restart threshold on two-hub trees

## Finding
For integers \(a,b\ge 1\), let \(G_{a,b}\) be the tree consisting of adjacent vertices \(H,J\), two distinguished leaves \(s,t\) adjacent to \(H\), \(a-1\) further leaves adjacent to \(H\), and \(b\) leaves adjacent to \(J\). Thus \(H\) has degree \(a+2\), \(J\) has degree \(b+1\), and \(|V(G_{a,b})|=a+b+3\).

Start a continuous-time random walk at \(s\). Independently, at rate \(1\) it jumps to a uniform neighbor of its current vertex, and at rate \(r\ge0\) it instantaneously resets to \(s\); a reset at \(s\) changes nothing. Stop at the first visit to \(t\), and denote the mean completion time by \(M_{a,b}(r)\).

**Theorem.** For all integer \(a,b\ge1\) and real \(r\ge0\),
\[
M_{a,b}(r)=(r+2)\left(a+2+\frac{b}{1+(b+1)r(r+2)}\right).
\]
The function \(r\mapsto M_{a,b}(r)\) is strictly convex. Its unique minimizer on \([0,\infty)\) is positive if and only if
\[
a<4b^2+3b-2.
\]
In that regime the unique positive optimum \(r_*\) is characterized by
\[
(a+2)[1+(b+1)r_*(r_*+2)]^2
=b[(b+1)(r_*+2)^2-1].
\]
For \(a\ge4b^2+3b-2\), the unique minimizer is \(r_*=0\). In particular, the no-reset mean is \(M_{a,b}(0)=2(a+b+2)\). For each fixed integer \(a\ge1\), as \(b\to\infty\),
\[
r_*(a,b)\longrightarrow\frac1{\sqrt{a+2}},\qquad
\min_{r\ge0}M_{a,b}(r)\longrightarrow 2(a+2)+2\sqrt{a+2},
\]
although the unreset mean diverges linearly in \(b\).

## Assumptions and scope
The graph is unweighted, finite, connected, loop-free and undirected. Ordinary walks have one exponential jump clock of rate \(1\), *not* rate one per incident edge. Independent restart clocks are exponential with rate \(r\) and have zero relocation duration. The target \(t\) is absorbing on first arrival; the process starts and resets only at \(s\). All formulas are exact for the stated integer leaf counts and all real rates. For \(b=1\), the vertex \(J\) has degree \(2\); the formula remains valid though it need not be called a proper double star.

## Proof
Write \(S,H,A,J,L\) for mean times to hit \(t\) from respectively \(s\), the first hub, any of its other \(a-1\) non-target leaves, the second hub, and any of its \(b\) leaves. If \(a=1\), the symbol \(A\) may simply be omitted. For a non-target vertex \(v\), first-event conditioning gives
\[
(1+r)E_v=1+\frac1{\deg(v)}\sum_{w\sim v}E_w+rS,
\]
where \(E_t=0\). A reset from \(s\) is a self-transition and cancels from this equation. In particular \(S=1+H\). Every other leaf adjacent to the first hub satisfies \((1+r)A=1+H+rS\), hence \(A=S\).

Put \(d=J-S\). The equation at a leaf adjacent to the second hub yields
\[
L=S+\frac{1+d}{1+r}.
\]
The equation at the second hub is \((1+r)J=1+rS+(H+bL)/(b+1)\). Substituting \(H=S-1\), \(J=S+d\), and the displayed formula for \(L\), gives
\[
[(b+1)(1+r)^2-b]d=b(r+2),
\]
so
\[
d=\frac{b(r+2)}{1+(b+1)r(r+2)}.
\]
Finally the first-hub equation is
\[
(1+r)H=1+rS+\frac{S+(a-1)A+J}{a+2}.
\]
Substituting \(H=S-1\), \(A=S\), and \(J=S+d\) gives \(S=(a+2)(r+2)+d\), proving the exact formula.

Set \(B=b+1\) and \(D(r)=1+Br(r+2)\). Direct differentiation yields
\[
M'_{a,b}(r)=a+2+\frac{b[1-B(r+2)^2]}{D(r)^2},
\]
\[
M''_{a,b}(r)=\frac{2bB\,[B(r+2)^3-3(r+2)+2]}{D(r)^3}>0.
\]
For the strict inequality, \(r+2\ge2\), \(B\ge2\), so the bracket is strictly positive. Also
\[
M'_{a,b}(0)=a-4b^2-3b+2,\qquad
\lim_{r\to\infty}M'_{a,b}(r)=a+2>0.
\]
Strict convexity therefore gives exactly one positive optimizer when the initial derivative is negative; otherwise zero is the unique optimizer. At an interior optimum, setting the derivative to zero gives the stated scalar equation. The function tends to infinity with \(r\), so this optimizer is globally optimal.

With \(a\) fixed and \(b\to\infty\), for each fixed \(r>0\),
\[
M_{a,b}(r)\longrightarrow (a+2)(r+2)+\frac1r,
\qquad
M'_{a,b}(r)\longrightarrow a+2-\frac1{r^2}.
\]
The limit derivative is negative below \(1/\sqrt{a+2}\) and positive above it. The strict monotonicity of the finite-\(b\) derivative traps its sole zero between any two rates straddling that limit, proving convergence of the optimizers. Substitution and continuity on a compact interval away from zero prove convergence of the minimum values. The unreset mean follows directly by setting \(r=0\).

## Verification
A standalone Python 3 standard-library checker is supplied as `check_reset.py`. Run `python3 check_reset.py`. It builds every labeled \(G_{a,b}\) for \(1\le a,b\le5\), sets the target absorbing, solves the full generator's rational linear system at four nonnegative rational reset rates, and compares the result to the claimed closed form in all 100 cases. It additionally checks the derivative threshold and positivity of the computed second derivative at those parameters. This is an independent full-state finite check of the symbolic five-orbit argument, not a replacement for that argument or a claim about exhaustive graph enumeration. The symbolic proof above establishes all real rates and all integers \(a,b\ge1\).

For illustration, \((a,b)=(1,1)\) gives \(M(0)=8\) and an interior optimal rate about \(0.153423\), with minimum about \(7.756911\); \((a,b)=(5,1)\) is the zero-rate boundary.

## Relationship to prior work
Riascos, Boyer, Herringer, and Mateos (arXiv:1910.13568, first public 2019-10-29) derived spectral first-passage methods for network walks with resetting and investigated rings, regular Cayley trees and random networks. Its Appendix B also discusses continuous-time dynamics. The paper supplies general machinery but does not state the present two-hub leaf-to-leaf closed form, strict convexity, quadratic boundary, or fixed-\(a\) limit.

Reuveni (2016) established generic exponential-restart identities and an optimal-restart fluctuation property. These encompass the renewal principle behind the model but do not evaluate the unreset transform on this asymmetric two-hub family or derive the present integer phase boundary. Riascos, Boyer, and Mateos (arXiv:2110.15437) derive a general criterion in a **discrete-time** model where resetting consumes a step and study rings and regular Cayley trees; that criterion is not the continuous-time rate-zero threshold proved here. Michelitsch and collaborators (arXiv:2409.08394) study general discrete-time renewal resets on networks, with numerical random-network examples rather than this parameterized tree classification.

The statement and proof here are graph-specific rather than a claim that the general restart formula is new. Published-source searching did not reveal prior explicit coverage of this phase diagram, but this is not a proof of historical uniqueness.

## Limitations
The theorem concerns independent instantaneous exponential restarting at one fixed leaf, with a rate-one node-centric walk; conclusions need not persist for discrete-time restarts, vertex-dependent jump rates, biased edges, other seed/target placements, or arbitrary graphs. The finite checker is supporting evidence, while infinite-parameter claims rest on the displayed algebra. The claimed originality remains subject to external literature review; no independent mathematical audit has been performed.

## References
- A. P. Riascos, D. Boyer, P. Herringer, and J. L. Mateos, *Random walks on networks with stochastic resetting*, arXiv:1910.13568 (first posted 2019-10-29), https://arxiv.org/abs/1910.13568 .
- A. P. Riascos, D. Boyer, and J. L. Mateos, *Discrete-time random walks and Lévy flights on arbitrary networks: when resetting becomes advantageous?*, arXiv:2110.15437 (first posted 2021-10-28), https://arxiv.org/abs/2110.15437 .
- T. M. Michelitsch, G. D'Onofrio, F. Polito, and A. P. Riascos, *Random walks with stochastic resetting in complex networks: a discrete time approach*, arXiv:2409.08394 (first posted 2024-09-12), https://arxiv.org/abs/2409.08394 .
- S. Reuveni, *Optimal Stochastic Restart Renders Fluctuations in First Passage Times Universal*, Phys. Rev. Lett. 116, 170601 (2016), https://doi.org/10.1103/PhysRevLett.116.170601 .
