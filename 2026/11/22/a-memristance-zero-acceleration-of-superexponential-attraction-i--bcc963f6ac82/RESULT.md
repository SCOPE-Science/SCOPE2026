# A memristance-zero acceleration of superexponential attraction in a four-dimensional map

## Finding
For every pair \(a,b>0\), consider the four-dimensional discrete parabolic memristor map
\[
\begin{aligned}
x_{n+1}&=a y_n^2,\\
y_{n+1}&=b(1-w_n^2/2)y_n(1-z_n),\\
z_{n+1}&=1-x_n,\\
w_{n+1}&=w_n+y_n.
\end{aligned}
\]
It has the fixed-point line \((0,0,1,w)\). Let \(\rho\) and \(\beta\) be the unique positive roots of
\[
\rho^3-\rho^2-2=0,\qquad \beta^3-2\beta^2-2=0,
\]
respectively, so \(\rho=1.6956207695\ldots\) and \(\beta=2.3593040859\ldots\).

**Interior memory selection.** There is a nonempty open set of strictly positive initial states for which all coordinates remain positive, \(y_n>0\), \(w_n\uparrow w_\infty\in(0,\sqrt2)\), and
\[
\lim_{n\to\infty}\rho^{-n}\log\frac1{y_n}=L\in(0,\infty).
\]
Moreover, \(x_n\to0\) and \(z_n\to1\).

**Memristance-zero endpoint selection.** For every \(a,b>0\), there are strictly positive initial states, constructed below for every sufficiently small scalar \(s>0\), whose full positive trajectories satisfy \(w_n\uparrow\sqrt2\) and
\[
\boxed{\quad y_n=(ab\sqrt2)^{-1/3}\exp(-L_*\beta^n)(1+o(1)),\qquad L_*>0.\quad}
\]
The change from \(\rho\) to \(\beta\) is an exact, realized acceleration of double-exponential attraction at the vanishing-memristance boundary. At this endpoint the first multiplicative prefactor is universal, while the positive exponential amplitude \(L_*\) depends on the initial state.

## Assumptions and scope
The parameters \(a,b\) are arbitrary strictly positive real numbers. The source's memristor constants are fixed at \(\epsilon=1\) and \(\eta=-1/2\), and the parabolic coupling parameter is \(c=1\). All limits concern forward iterates with strictly positive real coordinates and the branch \(0<w_n<\sqrt2\). The interior conclusion holds on a sufficiently small open set; the endpoint conclusion holds on a nonempty, explicitly constructed family, not on every initial state or an open set.

## Proof
**1. Exact reduction and fixed line.** The fourth coordinate identity forces \(y=0\) at every fixed point, after which the other equations give the entire line \((0,0,1,w)\). Since \(x_{n+1}=a y_n^2\) and \(z_{n+1}=1-x_n\), for every orbit and each \(n\ge2\) there is the exact scalar-memory identity
\[
 y_{n+1}=ab\left(1-\frac{w_n^2}{2}\right)y_n y_{n-2}^{2},\qquad
 w_{n+1}=w_n+y_n.\tag{1}
\]
No truncation or center-manifold approximation is involved.

**2. Interior positive open region.** Choose \(s>0\) sufficiently small in terms of \(a,b\), and take
\[
 0<x_0,y_0,1-z_0<s,\qquad 0<w_0<\tfrac12.
\]
Choose \(s\) so that \(bs^2<s\), \(b^2s^3<s\), \(abs^2<1/2\), \(2s<1/2\), and \(as^2<1\). The first two iterates satisfy \(0<y_1\le bs^2<s\) and \(0<y_2\le b^2s^3<s\). Induction in (1), while \(w_n<1\), yields \(0<y_{n+1}\le q y_n\) for \(n\ge2\), where \(q=abs^2<1/2\). Consequently \(\sum_n y_n<2s\) for smaller \(s\), giving the self-consistent bound \(0<w_n<1\), \(w_n\uparrow w_\infty\in(0,1)\); also \(x_n<1\), \(z_n>0\).

Let \(u_n=-\log y_n\) and \(A=ab\). Equation (1) becomes
\[
 u_{n+1}=u_n+2u_{n-2}+g_n,\qquad
 g_n=-\log\left[A(1-w_n^2/2)\right].\tag{2}
\]
The forcing is uniformly bounded since \(0<w_n<1\). In vector form, the companion matrix is
\[
 C_1=\begin{pmatrix}1&0&2\\1&0&0\\0&1&0\end{pmatrix},
 \qquad\det(tI-C_1)=t^3-t^2-2.
\]
It is primitive and has Perron eigenvalue \(\rho\); its two other eigenvalues have modulus \(\sqrt{2/\rho}<\rho\). Thus the dominant projection of (2), divided by \(\rho^n\), converges, and the other projections vanish at this scale. Taking \(s\) smaller makes the three initial \(u_j\) arbitrarily large, so the strictly positive Perron projection dominates the bounded cumulative forcing. The resulting limit is finite and strictly positive. The exact identities for \(x,z\) finish the interior claim.

**3. Construction of the boundary orbit.** Fix any \(a,b>0\), and set \(A=ab\). For sufficiently small \(s>0\), prescribe
\[
 Y_0=s,\qquad Y_1=s^3,\qquad Y_2=s^7,
 \qquad Y_{n+1}=2\sqrt2 A Y_n^2Y_{n-2}^2\quad(n\ge2).\tag{3}
\]
Smallness ensures \(Y_{n+1}\le Y_n/2\) for \(n\ge2\), and \(\sum Y_n<\sqrt2\). Consider sequences with the first three entries fixed at \(s,s^3,s^7\) and the remaining entries in \([0,Y_n]\). Define \(d_n=\sum_{j\ge n}y_j\) and the simultaneous operator on the tail by
\[
 (Ty)_{n+1}=A\bigl(\sqrt2 d_n-d_n^2/2\bigr)y_n y_{n-2}^2,\qquad n\ge2.\tag{4}
\]
The bound \(d_n\le2Y_n\) shows that \(T\) preserves this product interval. The function \(d\mapsto\sqrt2d-d^2/2\) is increasing on the relevant small interval. Hence iteration of \(T\) from the zero tail is coordinatewise increasing and bounded. Monotone convergence of the absolutely dominated tail sums supplies a fixed point. Its third entry is positive immediately; positivity propagates one index at a time, so every \(y_n>0\).

Now put
\[
 w_n=\sqrt2-\sum_{j\ge n}y_j\quad(n\ge0),\qquad
 x_0=\frac{y_2}{b(1-w_1^2/2)y_1},\qquad
 z_0=1-\frac{y_1}{b(1-w_0^2/2)y_0}.\tag{5}
\]
In particular \(w_0>0\). As \(s\downarrow0\), both \(x_0\) and \(1-z_0\) are asymptotic to \(s/(b\sqrt2)\); hence all four initial coordinates are strictly positive for sufficiently small \(s\). Equations (5) reproduce exactly the prescribed \(y_1,y_2\) under the four-dimensional map, and (4) ensures all subsequent iterates. Thus \(w_{n+1}=w_n+y_n\uparrow\sqrt2\). All coordinates remain positive because \(x_0<1\), \(a s^2<1\), and all later \(x_n\) are smaller.

**4. Endpoint spectral clock and prefactor.** Along this boundary orbit, \(d_n=\sqrt2-w_n\downarrow0\). From (1), (3), and \(d_n\le2Y_n\),
\[
 0<\frac{y_{n+1}}{y_n}\le 2\sqrt2 A Y_nY_{n-2}^2\longrightarrow0.
\]
The tail is therefore asymptotic to its first term, \(d_n/y_n\to1\), and
\[
 1-w_n^2/2=\sqrt2d_n-d_n^2/2=\sqrt2y_n(1+o(1)).
\]
For \(u_n=-\log y_n\), the exact logarithmic recurrence consequently reads
\[
 u_{n+1}=2u_n+2u_{n-2}-\log(A\sqrt2)+e_n,
 \qquad e_n\to0.\tag{6}
\]
The companion matrix \(C_2=\left(\begin{smallmatrix}2&0&2\\1&0&0\\0&1&0\end{smallmatrix}\right)\) has characteristic polynomial \(t^3-2t^2-2\), Perron eigenvalue \(\beta>2\), and two remaining eigenvalues of modulus \(\sqrt{2/\beta}<1\). Its Perron projection yields \(u_n/\beta^n\to L_*<\infty\). The upper-bound recurrence (3) itself has a strictly positive Perron coefficient for sufficiently small \(s\); since \(u_n\ge-\log Y_n\), it forces \(L_*>0\). The other modes contract. The constant particular solution of (6) is \(\tfrac13\log(A\sqrt2)\). Since \(e_n\to0\), spectral decomposition and the vanishing future tail of the Perron projection give
\[
 u_n=L_*\beta^n+\tfrac13\log(A\sqrt2)+o(1).
\]
Exponentiating gives exactly the endpoint formula, including the prefactor.

## Verification
The accompanying standalone \(\texttt{check.py}\) verifies the exact three-step elimination, both characteristic polynomials and root locations, finite monotone tail bounds, and consistency between the constructed boundary data and several direct four-dimensional iterates. The infinite existence proof is the order-preserving fixed-point argument in Step 3, not the finite diagnostic. Reported decimal roots are informative approximations; the root equations are exact.

## Relationship to prior work
Wang, Tong, Li, Zhang, Iu and Li introduced the four-dimensional map and analyzed its fixed-point line, Lyapunov spectra and numerical multistability (2023), but did not quantify the two positive-orbit superexponential clocks or construct the memory-cancellation endpoint orbit. The corresponding **three-dimensional** \(c=1\) parabolic subsystem, without a memory coordinate, also gives the root \(\rho\) by elementary variable elimination; that subsystem and its rate are not claimed as new here. In contrast, the constructed **four-dimensional** endpoint orbit has the different root \(\beta\) and exact prefactor because the memristance itself approaches zero at the same rate as the population coordinate.

## Limitations
The theorem treats \(c=1\), positive trajectories and the memory interval below \(\sqrt2\). It does not classify all initial states, rule out other boundary behaviors or prove the critical endpoint family is a smooth separatrix. The open attraction region is distinct from the boundary family. The conclusions are mathematical, not hardware or physical performance guarantees. Priority against all unindexed literature has not been independently established.

## References
1. M. Wang, L. Tong, C. Li, X. Zhang, H. H.-C. Iu and Z. Li, *A Novel Four-Dimensional Memristive Hyperchaotic Map Based on a Three-Dimensional Parabolic Chaotic Map with a Discrete Memristor*, Symmetry **15** (2023), 1879, first published 2023-10-06, https://doi.org/10.3390/sym15101879.
