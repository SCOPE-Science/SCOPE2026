# A sharp all-period dosing-frequency sign law for two-state drug tolerance

## Finding

In a two-phenotype linear drug-tolerance population, the sign of the change in asymptotic growth caused by making an on/off dosing cycle finite rather than infinitely rapid is **independent of the cycle period**. It is determined by one explicit scalar computed from the two dose-specific transition matrices. Both signs occur within biologically admissible rates; in particular, rapid averaging can predict growth although sufficiently long treatment cycles lead to decline.

## Assumptions and scope

The population is a column vector \(z(t)=(z_0(t),z_1(t))^{\mathsf T}\) of drug-sensitive and drug-tolerant cells. At drug dose \(c\), its dynamics are \(\dot z=M(c)z\), with
\[
 M(c)=\begin{pmatrix}\lambda_0(c)-\mu(c)&\nu(c)\\\mu(c)&\lambda_1-\nu(c)\end{pmatrix},
\]
where both transition rates \(\mu(c),\nu(c)\) are strictly positive, while the net cell-growth rates can be arbitrary real numbers. Let \(A=M(c)\), \(B=M(0)\), \(0<\varphi<1\), and let the on-drug and off-drug phases last \(\varphi T\) and \((1-\varphi)T\), respectively, for every cycle of length \(T>0\). Its principal Floquet exponent is
\[
 \Lambda(T)=\frac1T\log\rho\big(e^{\varphi T A}e^{(1-\varphi)TB}\big).
\]
The order does not affect the eigenvalues of the two-factor product. Write \(\alpha(M)\) for the largest real part of the eigenvalues of \(M\). The rapid-cycle comparator is \(\Lambda(0):=\alpha(\varphi A+(1-\varphi)B)\).

Define \(A_0=A-\tfrac12\operatorname{tr}(A)I\), \(B_0=B-\tfrac12\operatorname{tr}(B)I\), \(a=\sqrt{\operatorname{tr}(A_0^2)/2}>0\), \(b=\sqrt{\operatorname{tr}(B_0^2)/2}>0\), and the dimensionless contrast
\[
 h=\frac{\operatorname{tr}(A_0B_0)}{2ab}>-1.
\]
The strict positivity of off-diagonal entries is used throughout. The same rate matrices are held fixed while \(T\) changes; the total fraction of time spent at either dose is fixed.

## Proof

**Theorem.** For every such \(A,B,\varphi,T\),
\[
 \operatorname{sgn}(\Lambda(T)-\Lambda(0))=\operatorname{sgn}(1-h).
\]
In particular, if \(h=1\), every finite-period growth rate equals the rapid-cycle rate. Also,
\[
 \lim_{T\to\infty}\Lambda(T)=\varphi\alpha(A)+(1-\varphi)\alpha(B).
\]
For \(q=\sqrt{(a\varphi)^2+[b(1-\varphi)]^2+2h ab\varphi(1-\varphi)}>0\), the local correction is
\[
 \Lambda(T)-\Lambda(0)=\frac{(1-h^2)a^2b^2\varphi^2(1-\varphi)^2}{6q}\,T^2+O(T^4).
\]

**Derivation.** Since a real traceless \(2\times2\) matrix with positive off-diagonals squares to a positive scalar multiple of the identity, \(A_0^2=a^2I\) and \(B_0^2=b^2I\). Thus
\[
 e^{tA}=e^{t\operatorname{tr}(A)/2}\big(\cosh(at)I+a^{-1}\sinh(at)A_0\big),
\]
and similarly for \(B\). For \(u=a\varphi\) and \(v=b(1-\varphi)\), the determinant and trace of the monodromy matrix give the **exact formula**
\[
 \Lambda(T)=\frac{\operatorname{tr}(\varphi A+(1-\varphi)B)}2+\frac1T\operatorname{arcosh}\left(\cosh(uT)\cosh(vT)+h\sinh(uT)\sinh(vT)\right).
\]
The displayed arcosh argument is at least one because the propagator is strictly positive and has positive determinant. Moreover, \(h>-1\): writing \(A_0=\begin{psmallmatrix}d_A&p_A\\q_A&-d_A\end{psmallmatrix}\) and likewise for \(B_0\), with every \(p,q>0\), gives \(ab>|d_A d_B|\), whereas \(ab h=d_A d_B+(p_Aq_B+q_Ap_B)/2\).

Put \(f_T(x)=\cosh(T\sqrt{x})\) for nonnegative \(x\). Its power series has positive coefficients at every power and it is strictly convex on \([0,\infty)\) when \(T>0\). If \(w=(1+h)/2>0\), then the arcosh argument is exactly
\[
 C(T)=w f_T((u+v)^2)+(1-w)f_T((u-v)^2),
\]
whereas the corresponding argument for the rapid-cycle eigenvalue is \(f_T(q^2)\), with \(q^2=w(u+v)^2+(1-w)(u-v)^2\). If \(-1<h<1\), strict Jensen gives \(C(T)>f_T(q^2)\). If \(h>1\), strict convexity outside the secant interval gives the reverse strict inequality. At \(h=1\) there is equality. Since arcosh is strictly increasing on \([1,\infty)\), these three cases prove the theorem. Expanding the hyperbolic functions through order four gives the stated quadratic correction. Since \(h>-1\), the positive coefficient of \(\cosh((u+v)T)\) dominates as \(T\to\infty\), establishing the long-cycle limit.

**An exact drug-response counterexample.** Let \(\delta=227/200\), with off-drug rates \(\lambda_0(0)=2-\delta\), \(\lambda_1=-\delta\), \(\mu(0)=1\), \(\nu(0)=3\); at dose \(c=2\), let \(\lambda_0(2)=1-\delta\), \(\mu(2)=1\), \(\nu(2)=1\). These values arise from the valid Michaelis–Menten laws \(\lambda_0(c)=2-\delta-\tfrac32 c/(c+1)\) and \(\nu(c)=3-3c/(c+1)\), with constant forward switching \(\mu(c)=1\). Both selected dose-specific transition rates are positive.

Then \(A=\begin{psmallmatrix}0&1\\1&-1\end{psmallmatrix}-\delta I\), \(B=\begin{psmallmatrix}1&3\\1&-3\end{psmallmatrix}-\delta I\), \(\varphi=1/2\), and direct arithmetic gives \(a^2=5/4\), \(b^2=7\), \(h=6/\sqrt{35}>1\). Hence finite cycling *always* reduces the rapid-limit growth rate. More strongly,
\[
 \Lambda(0)=\frac{\sqrt{57}-3}4-\delta>0,\qquad
 \lim_{T\to\infty}\Lambda(T)=\frac{\sqrt5+2\sqrt7-3}4-\delta<0.
\]
The inequalities are exact: \((7.54)^2<57\), whereas \(\sqrt5<2.237\), \(\sqrt7<2.646\), and \(2.237+2(2.646)<7.54\). Continuity guarantees a finite period where the linear population changes from growing to declining. At \(T=4\), numerical evaluation gives \(\Lambda(4)\approx-0.00136062649\), while \(\Lambda(0)\approx0.00245860882\).

## Verification

The standalone `checker.py` uses exact symbolic arithmetic for all matrices, radicals, and rational comparison inequalities, checks the two long/short-period growth signs, and compares the exact hyperbolic-trace Floquet formula against directly computed matrix exponentials in 500 deterministic sampled two-state systems. It also checks the displayed \(T=4\) numerical sign. Run with `python checker.py` using Python, SymPy, NumPy and SciPy. The proof, rather than the finite tests, establishes the all-period and all-parameter statements.

## Relationship to prior work

Gunnarsson (2026) defines the identical drug-sensitive/tolerant two-state generators and optimizes the rapid-cycle averaged spectral growth. His stated limit assumes arbitrarily short treatment cycles, so it does not provide the finite-cycle, all-period sign classification or the exact counterexample. Clairambault, Gaubert and Perthame (2007) provide a general Floquet lower bound based on an *arithmetico-geometric* average, not the arithmetic matrix average used in the present comparison. Patra and Klumpp (2015) analyze periodic phenotype switching and selection of switching rates; their accessible abstract supports related motivation, but their full text was not confirmed to exclude an equivalent period comparison. Elementary \(2\times2\) matrix-exponential identities and convexity are prior tools and are not claimed as new. The claimed contribution is the application-specific sharp all-period phase distinction and extinction/growth reversal in admissible drug response.

## Limitations

The classification is for a deterministic two-phenotype, irreducible linear model under exact square-wave on/off exposure, with fixed treatment fraction; it is not a result for nonlinear tumor burden, drug pharmacokinetics, finite-time clearance, accumulated toxicity, or clinical efficacy. The period \(T=4\) value is an auxiliary numerical check; existence of a finite period giving decline is proved analytically. Broader published results on periodic positive matrices may subsume the exact criterion; historical priority is not independently established.

## References

- E. B. Gunnarsson, *Sharp transitions between optimal therapy regimes reveal robust dosing strategies against drug-induced persistence*, arXiv:2611.00295v1 (2026-10-30), https://arxiv.org/html/2611.00295v1.
- J. Clairambault, S. Gaubert and B. Perthame, *An inequality for the Perron and Floquet eigenvalues of monotone differential systems and age structured equations*, C. R. Math. 345 (2007), 549–554, https://doi.org/10.1016/j.crma.2007.10.001.
- P. Patra and S. Klumpp, *Emergence of phenotype switching through continuous and discontinuous evolutionary transitions*, Phys. Biol. 12 (2015), 046004, https://doi.org/10.1088/1478-3975/12/4/046004.
