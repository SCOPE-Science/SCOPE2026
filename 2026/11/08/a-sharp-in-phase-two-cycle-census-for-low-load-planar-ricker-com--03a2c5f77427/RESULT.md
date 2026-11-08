# A sharp in-phase two-cycle census for low-load planar Ricker competition

## Finding
Consider the two-species Ricker competition map
\[
T(x,y)=\bigl(r x e^{-x-\alpha y},\ s y e^{-y-\beta x}\bigr)
\]
on the positive quadrant. Suppose \(r,s,\alpha,\beta>0\), \(\alpha\beta\ne1\), and the unique coexistence equilibrium \(E=(X,Y)\) is strictly positive, with
\[
X+\alpha Y=\log r,\qquad \beta X+Y=\log s,
\qquad 0<X\le2,\quad0<Y\le2.
\]
Then **the map has exactly one prime-period-two orbit contained entirely in the positive quadrant, up to exchanging the two orbit points, if and only if**
\[
\boxed{\alpha\beta>\left(\frac2X-1\right)\left(\frac2Y-1\right).}
\]
At or below equality it has no positive prime-period-two orbit. Whenever the orbit exists it is necessarily *in-phase*, taking the form
\[
(X+u,Y+v)\longleftrightarrow(X-u,Y-v),
\qquad 0<u<X,\quad0<v<Y.
\]
The exact criterion is equivalently \(\det(I+DT(E))<0\). In particular the zero determinant at equality cannot conceal any distinct positive two-cycle in the stated domain. Here and throughout, a *prime two-cycle* means two distinct positive points exchanged by one application of \(T\), and uniqueness is of the unordered orbit.

## Assumptions and scope
The growth factors \(r,s\) and the cross-competition coefficients \(\alpha,\beta\) are arbitrary positive real numbers, except that \(\alpha\beta=1\) is excluded. The assumed positive equilibrium is determined by the two displayed linear equations; no assumption that it is locally stable is imposed. Its component bounds \(0<X\le2\) and \(0<Y\le2\) are imposed on the coexistence equilibrium, **not** on \(\log r\) or \(\log s\). All claims refer only to two-cycles whose four coordinates are strictly positive; boundary cycles are outside this census.

## Proof
**1. Midpoint rigidity.** Let two distinct positive states \((x_0,y_0)\) and \((x_1,y_1)\) be exchanged by \(T\). Taking logarithms of the first species' two updating ratios and adding gives
\[
0=2\log r-(x_0+x_1)-\alpha(y_0+y_1).
\]
The second species similarly gives
\[
0=2\log s-\beta(x_0+x_1)-(y_0+y_1).
\]
Since \(1-\alpha\beta\ne0\), the unique solution to this linear system is
\[
(x_0+x_1)/2=X,\qquad(y_0+y_1)/2=Y.
\]
Thus write the states as \((X+u,Y+v)\) and \((X-u,Y-v)\), necessarily with \(|u|<X\), \(|v|<Y\). Reversing the two states changes both signs and nothing else.

**2. Exact amplitude equations and forced phase agreement.** Using the equilibrium relations and the first half of the cycle, one obtains
\[
\frac{X-u}{X+u}=e^{-u-\alpha v},\qquad
\frac{Y-v}{Y+v}=e^{-v-\beta u}.
\]
Equivalently, with \(\psi_Z(w)=2\operatorname{artanh}(w/Z)-w\) defined for \(|w|<Z\), the two-cycle equations are
\[
\psi_X(u)=\alpha v,\qquad \psi_Y(v)=\beta u.
\]
For \(0<Z\le2\), \(\psi_Z\) is odd and strictly increasing on \((-Z,Z)\): its derivative is \(2/[Z(1-(w/Z)^2)]-1\), nonnegative everywhere and strictly positive except possibly at the isolated point \(Z=2,w=0\). Thus \(\psi_Z(w)\) has the same sign as \(w\). If either \(u\) or \(v\) vanished, both would vanish, giving the fixed point rather than a prime cycle. Otherwise the positivity of \(\alpha,\beta\) forces \(u\) and \(v\) to have the same sign. Exchange the two points if necessary to arrange \(u,v>0\). This rules out **all** positive out-of-phase prime two-cycles in the domain, without symmetry assumptions on the two species.

**3. Sharp existence and uniqueness.** For \(0<Z\le2\) and \(0<w<Z\), put
\[
H_Z(w)=\frac{\psi_Z(w)}w
=\frac2Z\sum_{k=0}^{\infty}\frac{(w/Z)^{2k}}{2k+1}-1.
\]
The positive-term expansion shows that \(H_Z(w)>0\) and is strictly increasing in \(w>0\). Moreover,
\[
\lim_{w\downarrow0}H_Z(w)=\frac2Z-1,
\qquad\lim_{w\uparrow Z}H_Z(w)=+\infty.
\]
The first amplitude equation determines a strictly increasing function \(v(u)=\psi_X(u)/\alpha\) starting at zero and diverging as \(u\uparrow X\). There is therefore a unique \(u_{\max}\in(0,X)\) for which \(v(u_{\max})=Y\), and \(0<v(u)<Y\) for \(0<u<u_{\max}\).

For such \(u\), the two amplitude equations are equivalent to the single equation
\[
H_X(u)H_Y(v(u))=\alpha\beta.
\]
The left side is continuous, strictly increasing from the limit
\[
\left(\frac2X-1\right)\left(\frac2Y-1\right)
\]
at the left endpoint to \(+\infty\) at the right endpoint. It reaches the strictly positive target \(\alpha\beta\) at **exactly one** interior \(u\) if and only if that target exceeds its left-endpoint limit. This proves necessity, sufficiency, and uniqueness, including the equality and \(X=2\) or \(Y=2\) boundary cases. The equations used were obtained by taking logarithms of positive quantities; exponentiating them verifies the forward half-cycle, and the reversed signs verify the backward half-cycle. Thus the constructed solution is an actual prime period-two orbit, not merely a root of an auxiliary necessary condition.

**4. Relation to the fixed-point flip factor.** Direct differentiation at the equilibrium gives
\[
DT(E)=\begin{pmatrix}1-X&-\alpha X\\-\beta Y&1-Y\end{pmatrix},
\]
so
\[
\det(I+DT(E))=(2-X)(2-Y)-\alpha\beta XY.
\]
Since \(X,Y>0\), its sign is negative exactly under the displayed strict criterion. The statement concerns the algebraic \(-1\) characteristic factor and the global two-cycle census; it does **not** assert that every parameter crossing of the equality hypersurface is a nondegenerate dynamical flip bifurcation.

## Verification
Run `python verify_ricker.py` with Python and `mpmath` installed. The checker evaluates seven parameter cases above, below, and at the predicted threshold, and reconstructs both legs of the positive two-cycle at 95-digit working precision when predicted to exist. The largest reported mapping residual for the positive examples is below \(10^{-65}\). These finite computations check representative identities and are **not** an exhaustive numerical search or a substitute for the global analytic argument.

## Relationship to prior work
Goldar, Hassan, Pati, Mohsen and Izadi (2026) study this precise planar Ricker family, including the equilibrium's local flip factor and positive period-two solutions. Their treatment does not state the present necessary-and-sufficient **global** existence and uniqueness criterion in the rectangle \(0<X,Y\le2\), nor the all-parameter phase-agreement statement there. Kulakov, Neverova and Frisman (2022) study multiple coexisting in-phase and out-of-phase modes of the same model, predominantly by numerical parameter scans; these demonstrate why a rigorous region excluding out-of-phase cycles is substantive. Ryals and Sacker (2017) prove absence of period-two points in a different restricted parameter region, notably when both intrinsic logarithmic growth rates are less than two and cross-coupling coefficients less than one. This earlier absence theorem is not claimed to be new. Naderi Yeganeh and Baigent (2026) develop stronger global convergence-to-equilibrium regimes; the present result does not imply or claim convergence of all trajectories.

The exact midpoint equations and monotone amplitude reduction establish the additional assertion: an *entire, explicitly delimited two-species parameter family* has either zero or exactly one positive primitive two-cycle, with no oppositely phased orbit. This is a statement about all such orbits, not just those observed numerically or born locally. Historical priority is provisional where prior full text was not obtainable.

## Limitations
The determinant condition is not a global attractor or stability criterion. The theorem neither controls basins of attraction nor classifies other periods. Positive boundary cycles, the resonant coupling \(\alpha\beta=1\), and fixed points with \(X>2\) or \(Y>2\) are outside its asserted domain. The relation to the \(-1\) multiplier is algebraic and does not independently verify the usual nondegeneracy hypotheses for a flip bifurcation. The supporting numerical tests are finite, and independent validation has not been performed.

## References
- S. Goldar, S. S. Hassan, R. Pati, A. A. Mohsen, and M. Izadi, *Dynamics and Bifurcations in a Two-Species Ricker Competition Model With Nonmonotonic Growth*, Discrete Dynamics in Nature and Society (2026), DOI: 10.1155/ddns/7255117. First public online: 2026-09-16.
- M. Kulakov, G. Neverova, and E. Frisman, *The Ricker Competition Model of Two Species: Dynamic Modes and Phase Multistability*, Mathematics **10** (2022), 1076, DOI: 10.3390/math10071076.
- B. Ryals and R. J. Sacker, *Global stability in the 2D Ricker equation revisited*, Discrete and Continuous Dynamical Systems B **22** (2017), 585–604, DOI: 10.3934/dcdsb.2017028.
- H. Naderi Yeganeh and S. Baigent, *New global stability results for the planar Ricker model*, Journal of Difference Equations and Applications **32** (2026), 773–795, DOI: 10.1080/10236198.2026.2636481.
