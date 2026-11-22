# A sharp reset-rate threshold and reentrant spring-energy fluctuations in a retained-memory Brownian bath

## Finding

In a thermally driven probe coupled by a harmonic spring to an auxiliary bath coordinate, with **only the probe** reset to zero at independent Poisson times, define the signed spring-energy jump \(W=U(0,Y)-U(X,Y)=XY-X^2/2\) at a stationary reset event, with \(U(x,y)=(x-y)^2/2\). For dimensionless reset rate \(r>0\) and bath friction ratio \(g>0\), the mean is
\[
\mathbb{E}W=\frac{g+1}{r(gr+2g+1)}>0.
\]
The squared coefficient of variation \(C_r(g)=\operatorname{Var}(W)/(\mathbb{E}W)^2\) has the exact endpoint laws
\[
\lim_{g\downarrow0}C_r(g)=2r+5,\qquad
\lim_{g\to\infty}C_r(g)=\frac{2r^4+14r^3+28r^2+21r+8}{r+4}.
\]
The difference, second endpoint minus first, is
\[
\frac{2(r^4+7r^3+13r^2+4r-6)}{r+4}.
\]
It changes sign exactly once at the unique positive zero \(r_*\) of the quartic, with \(0.49168<r_*<0.49169\). Therefore increasing bath friction from the fast-bath to the slow-bath regime **lowers** relative spring-jump variance for \(0<r<r_*\), and **raises** it for \(r>r_*\).

More strongly, for **every** \(1/2\le r\le3/5\), \(g\mapsto C_r(g)\) has exactly two critical points on \((0,\infty)\): a strict local maximum \(0<g_-(r)<1\) and a strict local minimum \(g_+(r)>1\), and no other stationary points. At \(r=1/2\), the two locations lie respectively in \((0.38,0.39)\) and \((16.1,16.2)\). This is an exact nonmonotonicity theorem, not a numerical interpolation.

## Assumptions and scope

The two independent standard Brownian motions \(B^X,B^Y\) drive
\[
dX_t=(Y_t-X_t)\,dt+\sqrt2\,dB_t^X,\qquad
dY_t=\frac{X_t-Y_t}{g}\,dt+\sqrt{\frac2g}\,dB_t^Y,
\]
between Poisson events of rate \(r\). At each event \(X\mapsto0\) instantaneously while \(Y\) is continuous. All parameters are strictly positive. The stationary pre-event distribution equals the time-stationary distribution because the external reset clock is independent of the system state. \(W\) is specifically the spring-energy *difference across a mathematical instantaneous reset*, not the complete thermodynamic cost of implementing a physical return protocol. It is signed; its mean is positive, while individual events can release energy.

The stationary distribution exists uniquely and has finite polynomial moments. Indeed, sample the retained bath coordinate just after resets. Over an independent inter-reset interval \(T>0\), its conditional mean contraction coefficient is \((g+e^{-(1+1/g)T})/(g+1)\), strictly between zero and one; the innovation is centered Gaussian with finite moments. The associated affine recursion is contractive and supplies a unique stationary reset-epoch law with all finite moments, whence the stationary continuous-time law.

## Proof

Write \(M_{ij}=\mathbb E(X^iY^j)\) in the stationary distribution and \(M_{00}=1\). Ito's formula and the reset generator give, for integers \(i,j\ge0\) with \(i+j>0\),
\[
0=-\left(i+\frac jg+r\mathbf1_{i>0}\right)M_{ij}
+iM_{i-1,j+1}+\frac jgM_{i+1,j-1}
+i(i-1)M_{i-2,j}+\frac{j(j-1)}gM_{i,j-2},
\]
where terms with negative indices vanish. This is a closed linear system separately at every even total degree, forced by the previous even degree. Solve the three equations of total degree two and the five equations of total degree four. In terms of their solutions,
\[
\mu=M_{11}-\tfrac12M_{20},\qquad
\mathbb E W^2=M_{22}-M_{31}+\tfrac14M_{40},\qquad
C_r(g)=\frac{\mathbb EW^2}{\mu^2}-1.
\]
In particular, direct elimination gives \(\mu=(g+1)/[r(gr+2g+1)]\). For an explicit, positive-denominator rational certificate, put \(C_r(g)=A(r,g)/[(g+1)^2 B(r,g)]\), where
\[
\begin{aligned}
B(r,g)={}&(r^3+9r^2+26r+24)g^3+(6r^2+31r+36)g^2\\
&+(11r+24)g+6,\\
A(r,g)={}&(2r^6+24r^5+110r^4+245r^3+281r^2+166r+48)g^5\\
&+(16r^5+140r^4+456r^3+724r^2+607r+240)g^4\\
&+(48r^4+309r^3+753r^2+891r+456)g^3\\
&+(68r^3+338r^2+613r+414)g^2\\
&+(46r^2+175r+180)g+(12r+30).
\end{aligned}
\]
All coefficients of \(B\) are positive when \(r>0\). Taking \(g\downarrow0\) and \(g\to\infty\) yields both endpoint formulas; subtraction yields the quartic. Its derivative \(4r^3+21r^2+26r+4\) is positive for all positive \(r\), and the quartic is negative at zero and positive at infinity, proving the unique threshold. Direct rational substitutions at \(r=0.49168\) and \(r=0.49169\) bracket it.

For the stronger reentrant statement, differentiate \(A/[(g+1)^2B]\), clear the positive denominator, and denote the resulting polynomial numerator by \(N_r(g)\), degree seven. The exact script `verify.py` reconstructs \(A,B,N\) *from the generator*, not from a numerical fit. On the entire parameter interval \(r=1/2+t/10\) with \(0\le t\le1\), transform each coefficient of the polynomial in \(t\) to the Bernstein basis on \([0,1]\). The rational Bernstein coefficients establish the strict sign pattern
\[
[g^7,g^6,g^5,g^4,g^3,g^2,g,1]:\quad (+,\text{unrestricted},-,-,-,+,+,+)
\]
and \(N_r(1)<0\). The smallest *signed* Bernstein coefficients for the \(g^7,g^5,g^4,g^3,g^2,g^1,g^0\) coefficients, in that order, are respectively
\[
\frac{54075}{128},\ \frac{126400338}{15625},\ \frac{131263578}{15625},\ \frac{463806}{3125},\ \frac{2461}{2},\ 1086,\ 180,
\]
and for \(-N_r(1)\) the minimum is \(14591839608/1953125\). The unrestricted \(g^6\) sign can alter neither the number of sign variations nor these inequalities. Thus Descartes' rule bounds the number of positive roots by two, counted with multiplicity. Since \(N_r(0)>0\), \(N_r(1)<0\), and the leading coefficient is positive, the intermediate value theorem supplies two distinct positive roots on opposite sides of one. They must be simple, exhaust all positive roots, and have the asserted maximum/minimum signs. Exact rational endpoint substitutions bracket the two roots at \(r=1/2\).

## Verification

Run `python verify.py` using Python 3 and SymPy. It reconstructs the stationary moment solutions, compares the displayed mean and endpoint identities symbolically, verifies the strict threshold bracket, checks that the entire derivative denominator has positive coefficients, and certifies every Bernstein-sign inequality by exact rational arithmetic. It also independently substitutes the solved moments into all degree-two and degree-four generator identities for two rational parameter pairs. A separate `simulate.py` implements exact conditional Gaussian propagation between Poisson events; its Monte Carlo output is corroborative only, never part of the proof. The proof is symbolic and covers all positive \(r,g\) for the endpoint theorem and every \(r\) in the full closed interval for the two-extremum theorem.

## Relationship to prior work

Santra and Das (2026) introduced exactly this probe-only resetting and bath-memory model and derived its general mixed-moment hierarchy and position cumulants. Consequently the recurrence itself is **prior work**, not claimed as new. The new statement concerns the spring-energy jump observable and its sharp bath-memory phase structure, including a global one-parameter threshold and an interval of provable double turning points. Olsen and Gupta (2024) studied thermodynamic work of *implemented* partial resetting in a different one-coordinate model; that cost is not identical to the signed spring-energy difference considered here. Earlier viscoelastic resetting studies address positional statistics and correlations rather than this exact energy-jump fluctuation classification. The derivation is an explicit algebraic specialization of the published moment method; priority for an unindexed equivalent energy calculation remains open.

## Limitations

Only instantaneous probe-only resets with an unreset Gaussian single-coordinate bath are covered. The endpoint limits require taking the stationary state at each finite positive \(g\) before taking \(g\to0\) or \(g\to\infty\); they do not assert existence of a stationary state at exactly infinite friction. The squared coefficient of variation quantifies per-event *signed spring-energy change*, not complete mechanical control work or long-time cumulative-work variance. The two-extrema classification is proved on \([1/2,3/5]\), not on every reset rate. The symbolic proofs and computations were reviewed within this study; no independent audit has been performed.

## References

1. I. Santra and D. Das, *Resetting in a viscoelastic bath: the bath remembers*, arXiv:2603.17027v1, 17 March 2026. https://arxiv.org/html/2603.17027v1
2. K. S. Olsen and D. Gupta, *Thermodynamic work of partial resetting*, arXiv:2401.11919v2, 2024. https://arxiv.org/html/2401.11919v2
3. A. Biswas et al., *A resetting particle embedded in a viscoelastic bath*, arXiv:2412.09260, 2024. https://arxiv.org/abs/2412.09260
