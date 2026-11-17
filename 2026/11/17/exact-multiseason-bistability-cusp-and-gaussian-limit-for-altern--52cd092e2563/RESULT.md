# Exact multiseason bistability cusp and Gaussian limit for alternating quadratic population maps

## Finding

A sequence of individually regular two-species quadratic stochastic operators can have two stable seasonal population cycles. There is a sharp, explicit cusp for every extinction-season length of at least two, and the entire cusp sequence has a nontrivial Gaussian-map limit.

Fix an integer \(m\ge2\), let \(d=2^m\), and take \(0<p,q<1\). Define the two-species maps (using the first species' share \(x\in[0,1]\))
\[
A_\alpha(x)=\alpha x^2,\qquad B_q(x)=1-q(1-x)^2,\qquad \alpha=p^{1/(d-1)}.
\]
The period-\((m+1)\) seasonal schedule consists of one \(B_q\) season followed by \(m\) identical \(A_\alpha\) seasons. Its return is exactly
\[
G_{p,q,d}(x)=A_\alpha^{\circ m}(B_q(x))=p[1-q(1-x)^2]^d.
\]
Every individual \(A_\alpha\) map converges globally to \(0\); every individual \(B_q\) map converges globally to \(1\). Nevertheless the seasonal return can have three interior fixed points, of which the smallest and largest attract and the middle repels. All initial states have a limiting seasonal configuration; there are never more than three.

Write
\[
q_d=\frac{2d-1}{d^2},\quad x_d=\frac{d-1}{2d-1},\quad
p_d=\frac12\left(\frac{2d-1}{2(d-1)}\right)^{d-1}.
\]
For \(0<q\le q_d\), the return has exactly one fixed point in \((0,1)\). At \((p,q)=(p_d,q_d)\) this point is a triple parabolic fixed point, at \(x_d\). For \(q_d<q<1\), put
\[
t_\pm(q)=\frac{d-1\pm\sqrt{(d-1)^2-(2d-1)(q^{-1}-1)}}{2d-1},
\qquad
P_\pm(q)=\frac{t_\pm(q)}{[1-q(1-t_\pm(q))^2]^d}.
\]
Then \(0<P_+(q)<P_-(q)\). The return has precisely three simple fixed points if and only if
\[
P_+(q)<p<P_-(q),\qquad 0<p<1.
\]
The two outer fixed points are asymptotically attracting; the middle one is repelling, and its location is the exact basin boundary. On either fold \(p=P_+(q)\) or \(p=P_-(q)\), if that fold lies in the open parameter square, there are two distinct fixed points, one double and one simple. At every other parameter except the cusp there is exactly one fixed point. For any initial state, iteration under the increasing return map converges monotonically after the first iterate to one of its fixed points.

At the cusp, for every \(x_0\in[0,1]\setminus\{x_d\}\),
\[
\lim_{n\to\infty}\sqrt n\,|G_{p_d,q_d,d}^{\circ n}(x_0)-x_d|
=\sqrt{\frac{3d^2(d-1)}{(2d-1)^3}}.
\]
In particular, the new first multiseason case \(d=4\) has
\[
(q_4,p_4,x_4)=\left(\frac7{16},\frac{343}{432},\frac37\right),
\qquad
\lim_{n\to\infty}\sqrt n\,|x_n-3/7|=\frac{12}{7\sqrt7}.
\]
At \(d=4\), \(q=1/2\), \(p=22/25\), the three fixed points are approximately \(0.1351644985\), \(0.4126843285\), and \(0.8305324824\). Their respective multipliers are approximately \(0.746898\), \(1.171563\), and \(0.571195\).

The cusp has a sharp large-season limit:
\[
dq_d\longrightarrow2,\quad p_d\longrightarrow\frac{\sqrt e}{2},\quad
x_d\longrightarrow\frac12,\quad
d(1-p_d^{1/(d-1)})\longrightarrow\log2-\frac12.
\]
If \(q=c/d\), with fixed \(c>0\), the full return maps converge uniformly with their derivatives through every fixed finite order to
\[
G_{p,c,\infty}(x)=p\exp[-c(1-x)^2].
\]
This limiting map has the unique interior triple-fixed-point cusp at \(c=2\), \(p=\sqrt e/2\), \(x=1/2\). Thus a sharply tuned long extinction season generates a Gaussian nonlinear population return, rather than simply the same finite-season quadratic response.

## Assumptions and scope

The state space is the closed two-species probability simplex represented by \(x\in[0,1]\). The parameter square is open: \(0<p,q<1\); the integer \(m\ge2\) is fixed for the finite-season theorem. Individual seasons are genuine quadratic stochastic operators: for \(A_\alpha\), the first-species offspring probabilities at parental pairs \((11),(12),(22)\) are \((\alpha,0,0)\); for \(B_q\) they are \((1,1,1-q)\). All lie in \([0,1]\). A seasonal fixed point means a fixed point of the return after the entire scheduled block, not an assertion about minimal period when the season labels are forgotten. No claim is made for arbitrary switching order or stochastic schedules.

## Proof

**Composition and individual regularity.** Induction gives \(A_\alpha^{\circ m}(x)=\alpha^{2^m-1}x^{2^m}\), giving the return. As \(0<\alpha<1\), \(A_\alpha(x)<x\) for \(x>0\), so its iterates converge to \(0\). Since \(1-B_q(x)=q(1-x)^2<1-x\) for \(x<1\), the other map's iterates converge to \(1\).

**Fixed-point reduction.** Set \(h(x)=1-q(1-x)^2\), positive on \([0,1]\). The equation \(G(x)=x\) is equivalent to \(p=R_q(x):=x/h(x)^d\). We have \(R_q(0)=0\), \(R_q(1)=1\), so every \(p\in(0,1)\) has at least one interior solution. Direct differentiation yields
\[
\operatorname{sign}R_q'(x)=\operatorname{sign}\{1-q(1-x)[1+(2d-1)x]\}.
\]
The concave quadratic \(D(x)=(1-x)[1+(2d-1)x]\) has its unique maximum \(d^2/(2d-1)\) at \(x_d=(d-1)/(2d-1)\). Therefore \(q\le q_d\) makes \(R_q\) strictly increasing except possibly for one stationary point when \(q=q_d\). For \(q>q_d\), its two critical points are exactly \(t_-<t_+\), both in \((0,1)\), with \(R_q\) increasing/decreasing/increasing on the three successive intervals. Their critical values are \(P_-=R_q(t_-)\) (the local maximum) and \(P_+=R_q(t_+)\) (the local minimum). The root census and fold statements follow from this shape and the open endpoint bounds. Note that if \(P_-\ge1\), the upper fold is outside the allowed \(p\)-range; this is automatically accounted for by intersecting the displayed inequalities with \(0<p<1\).

**Dynamics and stability.** \(G\) is strictly increasing on \([0,1]\). If \(G(x)>x\), its forward iterates increase; if \(G(x)<x\), they decrease. Their limits are fixed points by continuity, giving global convergence and excluding nontrivial periodic points of the return. For any interior fixed point \(z\), differentiate \(G(x)-x=h(x)^d[p-R_q(x)]\). At a fixed point, \(G'(z)-1=-h(z)^d R_q'(z)\). Thus the two roots on the increasing branches of \(R_q\) have \(0<G'(z)<1\), while the middle root has \(G'(z)>1\). The middle root separates the two attraction basins by monotonicity.

**Cusp and its time law.** At \(q=q_d\), the stationary point is \(x_d\), and setting \(p=R_{q_d}(x_d)\) simplifies to \(p=p_d\). Direct substitution yields \(G(x_d)=x_d\), \(G'(x_d)=1\), \(G''(x_d)=0\), and
\[
G'''(x_d)=-\frac{(2d-1)^3}{d^2(d-1)}<0.
\]
Consequently, with \(e_n=x_n-x_d\),
\[
e_{n+1}=e_n-\frac{(2d-1)^3}{6d^2(d-1)}e_n^3+O(e_n^4).
\]
Strict monotonicity of \(G\) prevents any nonfixed initial point from landing exactly at \(x_d\). Since all orbits approach it at the cusp, the reciprocal-square increments converge to \((2d-1)^3/[3d^2(d-1)]\); their Cesàro means prove the displayed square-root law.

**Long-season limit.** With \(q=c/d\), the identity \(d\log(1-c(1-x)^2/d)\to-c(1-x)^2\) and its termwise derivatives, uniformly on the compact interval, give \(C^r\) convergence for each fixed \(r\). Taking logarithms in the explicit finite cusp coefficients gives the displayed parameter limits. The limiting fixed-point fold obeys \(1=2cx(1-x)\), so its first tangency is at \(c=2,x=1/2\), where the fixed-point equation gives \(p=\sqrt e/2\); direct differentiation shows cubic, not higher, contact.

## Verification

The attached standalone `check.py` uses exact rational/symbolic arithmetic to test the critical fixed-point equation and its first three derivatives at \(d=2,4,8,16\), to validate the fold equations at representative parameters, and to count and classify all three fixed points of the explicit \(d=4\) witness. The symbolic checks corroborate the parameter formulas; the continuum inequalities and all-integer proof are the analytic argument above. Run `python check.py` with SymPy installed.

## Relationship to prior work

Jamilov, Mukhamedov, Mukhamedova and Souissi establish regularity of individual \(F\)-stochastic operators and certain compositions within a common attracting class. Their results do not establish periodic alternation between **different** attracting vertices or the resulting multiseason bistability. The present elementary two-species maps are instances of quadratic stochastic maps, and one is obtained by exchanging the species labels of a regular extinction map.

Lawnik, Moysis and Volos introduce a broad two-branch interval family without fixed points. An available precise analysis of its strictly alternating quadratic regime has an exponent-two cusp at \(3/4\). This agrees with the \(d=2\) member of our fixed-point-return normal form under parameter relabeling: that special case is **prior work, not part of the new claim**. The new statements concern every season length \(m\ge2\), the explicit depth-dependent cusp thresholds, and their Gaussian large-season limit. The 2023 article's reported parameter illustrations are not a theorem giving these multiseason statements. General one-dimensional fold theory explains the local phenomenon but does not give these exact parameter formulas or the season-length scaling.

## Limitations

The population interpretation is mathematical; no demographic data or biological mechanism is inferred. The finite-season phase diagram assumes one \(B_q\) season followed by \(m\) identical \(A_\alpha\) seasons and the indicated positive parameter range. A fixed point of the return gives a seasonal orbit; minimal period of the scalar time-forgotten sequence is not classified. Only the cusp orbit's leading convergence constant is asserted. The broader publication-priority risk is an equivalent unindexed multiseason composition theorem; no independent audit has been performed.

## References

1. U. Jamilov, F. Mukhamedov, F. Mukhamedova and A. Souissi, *Dynamics of nonlinear stochastic operators and associated Markov measures*, Mathematical Methods in the Applied Sciences **47** (2024), 13300–13312. First publicly published 2024-05-16. DOI: https://doi.org/10.1002/mma.10191. Open full text: https://onlinelibrary.wiley.com/doi/full/10.1002/mma.10191.
2. M. Lawnik, L. Moysis and C. Volos, *A Family of 1D Chaotic Maps without Equilibria*, Symmetry **15** (2023), 1311. First public date 2023-06-27. DOI: https://doi.org/10.3390/sym15071311. Open full text: https://www.mdpi.com/2073-8994/15/7/1311.
