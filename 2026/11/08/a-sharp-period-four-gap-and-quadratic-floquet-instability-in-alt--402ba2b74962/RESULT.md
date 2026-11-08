# A sharp period-four gap and quadratic Floquet instability in alternating logistic feedback

## Finding
For the alternating-feedback logistic map
\[
x_{n+1}=(r+y_n)x_n(1-x_n),\qquad
 y_{n+1}=y_n+(-1)^n a(x_n-1/2),
\]
with \(r\in\mathbb R\), \(a>0\), and initial parity chosen positive, the only *full-state* period-two orbits are the boundary family \(x=0\) with alternating feedback levels and the interior orbit \(x=1/2,\ y=2-r\), both considered with the alternating parity as part of the state. Every nonconstant periodic population sequence entirely in \((0,1)\) has even least period at least four; the bound is attained for \(r=3\), \(a=6\) by a rigorously enclosed four-cycle that also keeps every effective logistic parameter strictly between zero and four.

The two-step multipliers at the interior period-two orbit are exactly
\[
\lambda_\pm(a)=\frac{1\pm\sqrt{1+a^2/4}}{2}.
\]
The positive multiplier exceeds one for all \(a>0\), and the local unstable e-folding time measured in single updates obeys
\[
\frac{2}{\log\lambda_+(a)}\sim\frac{32}{a^2}\quad(a\downarrow0).
\]
The interior orbit is a saddle for \(0<a<4\sqrt2\), has a multiplier \(-1\) and an expanding multiplier at \(a=4\sqrt2\), and has two expanding multipliers for \(a>4\sqrt2\). The boundary orbits have a neutral multiplier one along their one-parameter family, so none is an isolated attracting period-two orbit.

## Assumptions and scope
The autonomous state is \((x,y,s)\) with \(s\in\{+1,-1\}\), advanced by
\[
F(x,y,s)=((r+y)x(1-x),\ y+s a(x-1/2),\ -s).
\]
Period means exact return of all three coordinates, not an apparent periodic pattern after projecting away parity. The universal period restrictions concern periodic trajectories with \(0<x_n<1\) at every time. The period-two census also allows the invariant boundary \(x=0\). No globally bounded-orbit assumption is made. The proof of a nonconstant four-cycle supplies an additional explicit witness with all \(r+y_n\in(0,4)\).

## Proof
**1. Full period-two census.** A two-step return satisfies
\[
y_2-y_0=a(x_0-x_1)=0,
\]
so \(x_0=x_1=u\). Both population updates then require
\[
u=(r+y_0)u(1-u)=(r+y_1)u(1-u).
\]
If \(u=0\), every \(Y=y_0\) gives the boundary orbit with feedback \(Y,Y-a/2\). If \(u\ne0\), then \(u\ne1\) because a logistic update from one is zero. Subtracting the two equations gives \(y_1=y_0\). Since \(y_1-y_0=a(u-1/2)\) and \(a>0\), \(u=1/2\); the logistic equation gives \(r+y_0=2\). Thus the only interior period-two orbit is \((1/2,2-r,s)\), with constant \((x,y)\) and alternating parity. The other initial parity gives the same cycle in reverse order.

At the interior orbit the two one-step derivative matrices, in the order \(s=+1,-1\), are
\[
J_+=\begin{pmatrix}0&1/4\\ a&1\end{pmatrix},\quad
J_-=\begin{pmatrix}0&1/4\\ -a&1\end{pmatrix}.
\]
Their product is
\[
K=J_-J_+=\begin{pmatrix}a/4&1/4\\a&1-a/4\end{pmatrix},
\quad\operatorname{tr}K=1,\quad\det K=-a^2/16.
\]
Solving its characteristic equation yields the stated multipliers. In particular \(\lambda_+>1\). The second has absolute value less than one exactly when \(a<4\sqrt2\). A Taylor expansion gives \(\log\lambda_+=a^2/16+O(a^4)\), which proves the two-update-to-single-update e-folding conversion. At a boundary orbit, the two-step derivative is triangular with diagonal \(((r+Y)(r+Y-a/2),1)\), so its continuum of periodic states precludes isolated attraction.

**2. Odd periods are impossible for nonconstant population dynamics.** If a periodic population orbit stays in \((0,1)\) and has least period \(p\), then the logistic update determines the feedback variable uniquely:
\[
y_n=\frac{x_{n+1}}{x_n(1-x_n)}-r.
\]
Consequently \(y_n\) is also \(p\)-periodic. If \(p\) were odd, comparing the feedback increments at times \(n\) and \(n+p\) would give
\[
 a(-1)^n(x_n-1/2)=-a(-1)^n(x_n-1/2),
\]
so \(x_n=1/2\) for every \(n\), contradicting nonconstancy. The period-two census rules out nonconstant least period two, and therefore the least possible nonconstant population period is four.

**3. Four is attained.** Set \(r=3\), \(a=6\) and let \(H(x,y)=\pi_{x,y}F^4(x,y,+1)-(x,y)\). Consider the exact-decimal rational center
\[
c=\left(0.584659370623430440690721939042858948322863116678,\;-1.41236581213595531877756480186345406366138289085\right)
\]
and the rational square \(B=c+[-10^{-8},10^{-8}]^2\). The included pure-Python verifier evaluates \(H(c)\) and the entire interval enclosure \(DH(B)\) using exact rational interval arithmetic. With \(C=DH(c)^{-1}\), it checks that the Newton-type self-map \(\mathcal T(z)=z-CH(z)\) sends \(B\) strictly inside itself and has infinity-norm Lipschitz constant less than \(1.893\times10^{-5}\). Hence the Banach contraction theorem gives a unique exact zero of \(H\) in \(B\); no root-finding convergence assumption is needed. Propagating that same interval box through four updates produces strictly separated population intervals, respectively contained in
\[
(0.58465936,0.58465939),\ (0.38552962,0.38552966),\ (0.49643805,0.49643817),\ (0.69556764,0.69556805).
\]
The verifier also bounds all four effective parameters \(3+y_n\) strictly between zero and four. Thus this is a genuine least-period-four orbit in the physical population strip, proving sharpness.

## Verification
Run `python3 verify.py` in a standard Python 3 installation; no third-party dependencies are needed. The script uses exact `fractions.Fraction` interval arithmetic to establish the box self-mapping and contraction inequalities, the invertibility of the point Jacobian, and disjoint population coordinates. It also directly checks the algebraic trace and determinant formulas at nine positive rational couplings. A successful execution prints `CERTIFIED_PERIOD_FOUR` followed by a contraction bound below \(1.893\times10^{-5}\), then `VERIFY_OK rational_interval_existence=1 analytic_floquet_cases=9`. The period-two and odd-period classifications follow from the symbolic arguments above; finite computations alone would not establish them for all parameters.

## Relationship to prior work
Chai and Kantz (2026) introduced the alternating-feedback system and established a mechanism for stochastic motion, periodic-window quasi-cycles, and long-lived transients. Their exact model equations and Appendix 5.2 analyze approximate cycle-to-cycle cancellation; they do not state a full-state period-two census, the exact two-step Floquet spectrum, or a certified strict period-four existence example. The present result distinguishes strict periodicity from the quasi-periodic trapping used there. Earlier static alternating-sign generalized logistic maps and standard periodically switched linear stability theory are not the same dynamically coupled feedback system. These comparisons support originality relative to the inspected material but do not establish exhaustive historical priority.

## Limitations
The \(a^{-2}\) time law is the **local linear unstable e-folding time near one specific orbit**, not an assertion about global transient lifetimes or escape-rate asymptotics. The four-cycle witness uses \(a=6\), so it does not establish a four-cycle for arbitrarily weak feedback. Its existence is certified within one rational box, not a count of all period-four orbits. No global attraction, all-period classification, or statistical escape theorem is asserted. Historical priority beyond inspected sources remains provisional.

## References
1. M. Chai and H. Kantz, *A general feedback mechanism unifying stochasticity, long transients, and resilience*, arXiv:2610.21834v1, first posted 2026-10-15, https://arxiv.org/abs/2610.21834 (model, analysis of quasi-periodic windows and Appendix 5.2).
2. N. M. A. Sayed, *Design of Positive, Negative, and Alternating Sign Generalized Logistic Maps*, *Discrete Dynamics in Nature and Society* (2015), DOI: 10.1155/2015/586783 (distinct static family of logistic maps).
3. The accompanying `verify.py` supplies exact rational interval enclosures and the finite Floquet identity checks.
