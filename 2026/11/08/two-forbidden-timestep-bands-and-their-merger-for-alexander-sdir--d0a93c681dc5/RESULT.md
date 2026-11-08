# Two forbidden timestep bands and their merger for Alexander SDIRK2 diffusion on stars

## Finding

For the unit-conductance star graph \(K_{1,m}\), \(m\ge2\), with combinatorial Laplacian \(L\), consider the unmodified two-stage, second-order, L-stable Alexander diagonally implicit Runge–Kutta step
\[
T_m(h)=r(hL),\qquad r(z)=\frac{1-(\sqrt2-1)z}{(1+(1-1/\sqrt2)z)^2},\qquad h\ge0.
\]
Set \(g=1-1/\sqrt2\), \(c=\sqrt2-1\), \(n=m+1\) and \(f(z)=r(z)\). For every \(m\le4\), \(T_m(h)\) is entrywise nonnegative for every \(h\ge0\). For each integer \(m\ge5\), define \(a_m^-<a_m^+\) as the positive roots of
\[
1+m f(nh)=0,
\]
and \(b_m^-<b_m^+\) as the positive roots of
\[
H_m(h)=m+f(nh)+(m^2-1)f(h)=0.
\]
These roots exist, are distinct, and are characterized by explicit quadratic and quartic equations, respectively. Positivity holds exactly outside the union of the two open intervals \((a_m^-,a_m^+)\cup(b_m^-,b_m^+)\), endpoints included. More sharply, the intervals are disjoint for \(5\le m\le9\), and overlap for every \(m\ge10\). Consequently the positivity set equals
\[
\begin{cases}
[0,\infty),&2\le m\le4,\\
[0,a_m^-]\cup[a_m^+,b_m^-]\cup[b_m^+,\infty),&5\le m\le9,\\
[0,a_m^-]\cup[b_m^+,\infty),&m\ge10.
\end{cases}
\]
The discontinuity is in positivity as a *function of timestep*, not in the propagator. For example, the \(m=5\) forbidden intervals are approximately \((1.0701,1.8155)\) and \((7.0669,9.4405)\). At \(m=10\), the two intervals overlap and the single forbidden band is approximately \((0.3060,37.6492)\). All statements concern entrywise nonnegativity of the final end-step update, not individual Runge–Kutta stages.

## Assumptions and scope

The graph has one hub and \(m\) leaves with unit, undirected, unweighted edges, and its Laplacian is the ordinary combinatorial matrix. The continuous-time heat equation is \(\dot u=-Lu\). The two-stage Butcher tableau has diagonal \(g=1-1/\sqrt2\), lower-left coefficient \(1-g\), and weights \((1-g,g)\). The final stability function \(r(z)\) is evaluated at \(hL\). All assertions hold for all real \(h\ge0\), including equality at the boundary. They do not extend automatically to other Runge–Kutta tableaux, weighted stars or general graphs.

## Proof

**Spectral reduction.** The star Laplacian has eigenvalues \(0\), \(1\) (multiplicity \(m-1\)), and \(n=m+1\) (multiplicity one). Its spectral projectors give, with subscripts \(0\) for the hub and \(i,j\) for distinct leaves,
\[
\begin{aligned}
(T_m)_{00}&=\frac{1+mf(nh)}{n},\\
(T_m)_{0i}&=\frac{1-f(nh)}n,\\
(T_m)_{ii}&=\frac{m+f(nh)+(m^2-1)f(h)}{mn},\\
(T_m)_{ij}&=\frac{m+f(nh)-nf(h)}{mn}\quad(i\ne j).
\end{aligned}
\]
The rows sum to one. The scalar function \(f\) is at most one for nonnegative arguments; thus hub–leaf entries are nonnegative. Multiplying the leaf–leaf numerator by positive denominators \(A=(1+gh)^2\) and \(B=(1+gnh)^2\) yields the exact polynomial identity
\[
AB\big(m+f(nh)-nf(h)\big)
=mnh^2\big[g(2-g)+g^2(m+2)h+g^4nh^2\big]>0
\]
for \(h>0\). Therefore all entrywise sign failures are precisely negative hub or leaf *diagonals*.

**Small stars and the hub band.** Direct differentiation shows \(f'(z)=(-1+cgz)/(1+gz)^3\), so its unique negative minimum is
\[
\min_{z\ge0}f(z)=-\rho,\qquad\rho=\frac{\sqrt2-1}{2},\qquad z_*=\frac1{cg}.
\]
For \(m\le4\), \(1-m\rho>0\) and \(m-m^2\rho>0\). Both diagonals are then positive for all \(h\ge0\). For \(m\ge5\), the hub diagonal is negative precisely between the two roots \(a_m^-<a_m^+\) of
\[
(g^2n^2)h^2+n(2g-mc)h+(m+1)=0.
\]
The discriminant is positive exactly for integers \(m\ge5\), as follows also from \(1-m\rho<0\); the quadratic is positive at zero and infinity.

**The leaf band.** Clearing the same denominators gives a quartic \(P_m(h)=A B H_m(h)\). Its coefficients from degrees zero through four are
\[
\begin{aligned}
&p_0=mn,\quad p_1=mn(2gm+4g-1),\\
&p_2=gmn(gm^2+6gm+4g-2m),\\
&p_3=g^2mn((2g-1)m^2+(4g-1)m+2g+1),\\
&p_4=g^4mn^2.
\end{aligned}
\]
For every integer \(m\ge5\), the signs are \((+,+,+,-,+)\): the quadratic factor of \(p_2\) has positive leading coefficient and negative discriminant, while the displayed factor of \(p_3\) is decreasing and already negative at \(m=3\). Descartes' rule gives at most two positive roots. Since \(f(8)<-1/5\), \(H_m(8)<0\) for \(m\ge6\); the remaining exact surd comparison \(H_5(8)<0\) is included in the accompanying checker. Because \(H_m(0)>0\) and \(H_m(h)\to m>0\) as \(h\to\infty\), the quartic has exactly two distinct positive roots \(b_m^-<8<b_m^+\), with negative sign between them.

**Ordering and the transition at ten leaves.** For \(h\le1/c\), \(f(h)\ge0\) and hence \(H_m(h)\ge m-\rho>0\); thus \(b_m^->1/c\). The hub minimum lies before \(1/c\), since \(z_*/n<1/c\) for \(m\ge5\), so \(a_m^-<b_m^-\). Direct expansion shows \((1+8gn)^2+m(1-8cn)>0\) for all nonnegative integer \(m\) (its coefficients as a polynomial in \(m\) are \(113-72\sqrt2\), \(217-144\sqrt2\), \(104-72\sqrt2\), all strictly positive). Since \(8>z_*/n\), this implies \(a_m^+<8<b_m^+\).

For the five integers \(5\le m\le9\), exact arithmetic gives both \(1+mf(7n/2)>0\) and \(H_m(7/2)>0\); the standalone verifier checks all ten algebraic inequalities without rounding. As \(7/2>z_*/n\) and \(H_m(8)<0\), this places \(a_m^+<7/2<b_m^-\), making the intervals disjoint. For every \(m\ge10\), take the common test step \(h=17/5\). The center numerator after clearing its positive denominator is
\[
Q_m=\left(\frac{1037}{50}-\frac{374\sqrt2}{25}\right)m^2
+\left(\frac{1147}{25}-\frac{748\sqrt2}{25}\right)m
+\frac{1257}{50}-\frac{374\sqrt2}{25}.
\]
Its leading coefficient is negative, constant and linear coefficients positive, and \(Q_{10}<0\); hence \(Q_m<0\) for every integer \(m\ge10\). Also \(f(17/5)<-10/99\) and \(f(17n/5)<0\), so \(H_m(17/5)<m-10(m^2-1)/99\le0\) for all \(m\ge10\). Both bands thus contain \(17/5\). Combined with their endpoint ordering, this proves the three regimes.

## Verification

Run `python3 verify.py` using the Python standard library. It checks exact surd inequalities, the hub quadratic coefficient signs, the complete finite \(m=5,\ldots,9\) separation tests, algebraic positive offdiagonal factor identities on rational test cases, and numerical consistency of the spectral formulas over multiple degrees and timesteps. The proof above, not finite testing, handles all \(m\). Its output is `VERIFY_OK`.

## Relationship to prior work

Alexander's original second-order L-stable DIRK formula supplies the known stability function, not the star-specific positivity classification. Higueras et al. analyze tradeoffs among L-stability, scalar nonnegativity and strong stability preservation for other optimized implicit–explicit schemes; they do not provide these exact star graph diagonal bands. Quezada de Luna and Ketcheson enforce maximum principles through a modified flux-limited scheme rather than classify the unmodified Alexander map. Gao and Wu study nonlinear spatial finite-volume positivity on general meshes, not this temporal star graph map. The present contribution is the all-degree exact endpoint positivity phase diagram, including the separate hub/leaf obstructions and sharp degree-ten merger. Related published studies of different time-integrator rational functions and Markov generators do not imply this statement merely through positivity of the underlying continuous semigroup.

## Limitations

The method is L-stable but is not claimed to preserve intermediate-stage positivity. The positive-cone condition is not an accuracy recommendation: large timesteps eventually restore nonnegative final updates because the graph has a simple stationary mode and decaying nonzero spectral modes. The classification does not cover nonunit conductances, other graph shapes, nonlinear diffusion, or a general minimum dimension for positivity loss across *all* graphs. The literature comparison supports originality against inspected results, not a guarantee of publication priority. No independent audit has been performed.

## References

1. R. Alexander, “Diagonally Implicit Runge–Kutta Methods for Stiff O.D.E.’s,” SIAM J. Numer. Anal. 14 (1977), 1006–1021. https://doi.org/10.1137/0714068 .
2. I. Higueras, N. Happenhofer, O. Koch and F. Kupka, “Optimized strong stability preserving IMEX Runge–Kutta methods,” J. Comput. Appl. Math. 272 (2014), 116–140. https://doi.org/10.1016/j.cam.2014.05.011 .
3. M. Quezada de Luna and D. I. Ketcheson, “Maximum principle preserving space and time flux limiting for Diagonally Implicit Runge–Kutta discretizations of scalar convection-diffusion equations,” arXiv:2109.08272v1 (2021). https://arxiv.org/html/2109.08272v1 .
4. Z. Gao and J. Wu, “A Second-Order Positivity-Preserving Finite Volume Scheme for Diffusion Equations on General Meshes,” SIAM J. Sci. Comput. 37 (2015), A420–A438. https://doi.org/10.1137/140972470 .
5. OpenPronghorn, “LStableDirk2” method documentation, https://openpronghorn.inl.gov/source/timeintegrators/LStableDirk2.html .
