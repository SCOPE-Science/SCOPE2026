# Sharp transverse stabilization of a coupled implicit two-cycle cusp

## Finding
In the planar two-phase implicit recurrence of Oliveira (2026, Section 8.4), consider the natural zero-bias slice \(a=0\) and the family of equal-deviation period-two solutions. There are three such real period-two solutions for every \(b<0\): the central orbit and a pair of nonzero orbits. The central orbit is a locally attracting sink for every \(b<0\). The nonzero pair is locally attracting **if and only if**
\[
b<b_*:=\frac{419-39\sqrt{1241}}{800}=-1.19360670799633\ldots.
\]
At equality both nonzero orbits have a simple two-step Floquet multiplier \(+1\), while their other multiplier lies strictly between zero and one. For \(b_*<b<0\), where the forward steps are regular, neither nonzero orbit is attracting. There are two isolated exceptional parameters at which one of the defining next-state Jacobians is singular, so local stability of that forward branch is not defined. Consequently the recurrence has **at least three distinct locally attracting period-two orbits** whenever \(b<b_*\). At \(b=b_*\), each nonzero equal-deviation orbit also meets a local family of unequal-deviation period-two solutions, a second branch not detected by the local cusp reduction at the origin.

## Assumptions and scope
Let \(x_j=(u_j,y_j)\in\mathbb R^2\), with \(\delta_0=u_0\), \(\delta_1=u_1-1\). With \(a=0\), put \(\mathcal N(s)=bs+2s^3+s^5\). The implicit equations, with alternating phase \(0,1\), are
\[
F_0(x_0,x_1)=\begin{pmatrix}\delta_1-\delta_0-\mathcal N(\delta_1)-y_1\\y_1-\tfrac12 y_0-\tfrac12\delta_1^3\end{pmatrix}=0,
\qquad
F_1(x_1,x_0)=\begin{pmatrix}\delta_0-\delta_1-\mathcal N(\delta_0)-y_0\\y_0-\tfrac13 y_1-\tfrac23\delta_0^3\end{pmatrix}=0.
\]
For a period-two solution, local attraction means both eigenvalues of the derivative of the two-step local forward return lie strictly inside the open unit disk, with the next-state Jacobians invertible. This is a local assertion about the forward branches; it does not presume global single-valuedness of the implicit recurrence.

For every \(b<0\), define \(z=(-3+\sqrt{9-4b})/2>0\) and \(t=\sqrt z\). The three *equal-deviation* phase-ordered solutions are
\[
X_0=((0,0),(1,0)),\qquad
X_\pm=((\pm t,\pm t^3),(1\pm t,\pm t^3)).
\]
The exceptional positive squared amplitudes are
\[
z_-=\frac{\sqrt{41}-5}{8},\qquad z_+=\frac{\sqrt{145}-9}{16},
\]
corresponding to singularities of the second-argument Jacobians. They satisfy \(0<z_-<z_+<z_*\), where
\[
z_*:=\frac{\sqrt{1241}-21}{40}>0,\qquad b_*=-3z_*-z_*^2.
\]
No claim is made that all other possible period-two solutions are classified or that all basins of attraction have been determined.

## Proof
**1. The three equal-deviation orbits.** Direct substitution of \(\delta_0=\delta_1=t\), \(y_0=y_1=t^3\) into both equations gives the single scalar condition \(bt+3t^3+t^5=0\). For \(b<0\), this has exactly the three real roots \(t=0\) and \(t=\pm\sqrt z\), since \(z^2+3z+b=0\) has exactly one positive root. The phase states of each orbit are distinct.

**2. The exact two-step linearization.** On \(X_\pm\), let \(z=t^2\) and set \(p=1-b-6z-5z^2=1-3z-4z^2\). Differentiating \(F_0\) and \(F_1\) with respect to their next-state arguments gives
\[
B_0=\begin{pmatrix}p&-1\\-3z/2&1\end{pmatrix},\qquad
B_1=\begin{pmatrix}p&-1\\-2z&1\end{pmatrix}.
\]
Their determinants are respectively \(p-3z/2\) and \(p-2z\), and the current-state derivatives are \(-\operatorname{diag}(1,1/2)\) and \(-\operatorname{diag}(1,1/3)\). Therefore, when the two determinants are nonzero, the local step derivatives are \(J_0=B_0^{-1}\operatorname{diag}(1,1/2)\) and \(J_1=B_1^{-1}\operatorname{diag}(1,1/3)\). Their product \(M=J_1J_0\) has trace and determinant
\[
\operatorname{tr}M=\frac{N(z)}{D(z)},\qquad \det M=\frac1{D(z)},
\]
where
\[
D(z)=3(4z^2+5z-1)(8z^2+9z-2),\qquad
N(z)=(1-3z-4z^2)^2+9z+6.
\]
The singular step parameters are exactly \(z=z_-\) and \(z=z_+\). At \(t=0\), the two eigenvalues instead simplify to \((1-b)^{-2}\) and \([6(1-b)^2]^{-1}\), which are strictly between zero and one for \(b<0\).

**3. Exact sharp Schur boundary.** For a real two-by-two matrix with trace \(T\) and determinant \(\Delta\), the two eigenvalues lie in the open unit disk exactly when \(1-T+\Delta>0\), \(1+T+\Delta>0\), and \(1-\Delta>0\). Polynomial expansion yields the exact identities
\[
D-N+1=2z(2z+3)(20z^2+21z-10),
\]
\[
D+N+1=2(56z^4+126z^3+44z^2-27z+7).
\]
The latter numerator is strictly positive for \(z\ge0\): its last three terms contain the strictly positive quadratic \(44z^2-27z+7\), whose discriminant is negative, and all higher terms are nonnegative. The two positive zeros of \(D\) are \(z_-<z_+\). Hence \(D>0\) on \((0,z_-)\cup(z_+,\infty)\), while \(D<0\) on \((z_-,z_+)\).

The quadratic \(20z^2+21z-10\) has exactly one positive zero \(z_*\). On every regular \(0<z<z_*\) with \(D>0\), the first Schur inequality fails. For \(z_-<z<z_+\), the second inequality fails because \((D+N+1)/D<0\). At \(z=z_*\), \(D=N-1>1\) and the two multipliers are \(1\) and \(1/D\). For \(z>z_*\), both factors in \(D\) are positive and strictly increasing, so \(D>D(z_*)>1\); all three Schur inequalities hold. The critical multiplier crosses \(+1\) transversely because \(20z^2+21z-10\) has a simple positive zero. As \(b=-3z-z^2\) is strictly decreasing in \(z>0\), the exact attracting condition is \(b<b_*\).

**4. An unequal-deviation branch at the threshold.** Eliminating the auxiliary variables from the phase-two equations yields
\[
y_0=\frac{\delta_1^3+4\delta_0^3}{5},\qquad
y_1=\frac{2\delta_0^3+3\delta_1^3}{5}.
\]
Write \(u=\delta_0=m+d\) and \(v=\delta_1=m-d\). Subtracting the remaining two equations and factoring \(u-v\) shows that any unequal-deviation solution satisfies
\[
b=B(m,d):=2-\frac{36}{5}m^2-\frac{12}{5}d^2-5m^4-10m^2d^2-d^4.
\]
Their sum, on \(a=0\), is the equation
\[
H(m,d):=5B(m,d)(u+v)+16u^3+14v^3+5(u^5+v^5)=0.
\]
At \(m_*=\sqrt{z_*}\), \(d=0\), one has \(B(m_*,0)=b_*\), \(H(m_*,0)=0\) and \(\partial_dH(m_*,0)=6z_*>0\). Thus the implicit function theorem produces a smooth curve \(d=d(m)\) of unequal-deviation periodic solutions through this point. Moreover,
\[
\partial_mH(m_*,0)=-4z_*(21+40z_*)\ne0,
\qquad
\partial_mB(m_*,0)=-m_*(72/5+20z_*)\ne0.
\]
Therefore \(d'(m_*)\ne0\), and \(b=B(m,d(m))\) is a valid local curve parameter. Except at the crossing itself, the nearby solutions satisfy \(u\ne v\). Replacing \((m,d)\) by \((-m,-d)\) gives the corresponding branch through the negative-amplitude orbit. Both next-state Jacobians remain invertible near the crossings since \(z_*>z_+\). This proves the claimed transverse branch crossings.

## Verification
Running `python CHECK.py` with Python 3 and SymPy checks the rational trace/determinant identities, the factorizations of the Schur expressions, the unequal-deviation elimination and transversality identities, and four numerical stability examples. The proof above supplies the global inequalities; finite symbolic and numerical checks corroborate but do not replace them.

## Relationship to prior work
Henrique M. Oliveira, *Lyapunov–Schmidt reduction for periodic orbits of implicit discrete dynamical systems*, arXiv:2611.03336v1 (first posted 2026-11-02), Section 8.4, defines precisely the two-phase coupled model and determines its local cusp and equal-deviation fold locus near \((a,b)=(0,0)\). Its analysis is local at the cusp and does not supply the nonlocal transverse Floquet transition on \(a=0\), the exact sink threshold, the three-sink regime or the unequal-deviation branch at that threshold. General Lyapunov–Schmidt and Schur conditions explain the methods but do not by themselves establish this model-specific global-in-amplitude calculation.

## Limitations
The theorem concerns the displayed explicit equal-deviation period-two solutions and a local bifurcating unequal-deviation family. The implicit relation may have multiple forward branches; two isolated amplitudes lose forward regularity, and no stability label is assigned there. There is no complete census of unequal-deviation or higher-period trajectories, no global basin theorem, and no claim that the three attracting orbits are the only attractors. Earlier unindexed calculations of this particular model remain a possible priority risk. Independent mathematical validation has not been performed.

## References
Oliveira, H. M. (2026), *Lyapunov–Schmidt reduction for periodic orbits of implicit discrete dynamical systems*, arXiv:2611.03336v1, https://arxiv.org/abs/2611.03336, especially Section 8.4, equations (106)–(114).

Kuznetsov, Y. A. (2004), *Elements of Applied Bifurcation Theory*, 3rd ed., Springer, for standard discrete stability and local bifurcation criteria.
