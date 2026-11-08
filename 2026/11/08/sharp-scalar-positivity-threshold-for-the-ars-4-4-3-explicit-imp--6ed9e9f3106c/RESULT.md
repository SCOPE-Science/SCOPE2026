# Sharp scalar positivity threshold for the ARS(4,4,3) explicit–implicit–null diffusion step

## Finding
For the unmodified third-order ARS(4,4,3) explicit–implicit–null (EIN) method on scalar positive decay, there is a **sharp, step-size-independent threshold** for positivity of the completed numerical step. Write \(r=a/a_0>0\) for the ratio between the physical diffusion coefficient and the implicit stabilizer, and put \(t=h a_0\mu\ge0\), where \(\mu>0\) is the positive scalar spatial eigenvalue. Let \(R(t,r)\) denote the one-step amplification of \(\dot u=-a\mu u\), using the EIN split \(-a_0\mu u-(a-a_0)\mu u\). If \(\rho\) is the unique root in \((0,1)\) of
\[
7\rho^3+36\rho^2-90\rho+18=0,
\qquad\rho=0.220231574305911\ldots,
\]
then
\[
\boxed{R(t,r)\ge0\text{ for every }t\ge0\quad\Longleftrightarrow\quad0<r\le\rho.}
\]
Equivalently, unconditional **completed-step scalar positivity** holds exactly for \(a_0/a\ge 1/\rho=4.540674983\ldots\). For \(\rho<r<1\), arbitrarily large steps give negative amplification; for every \(r\ge1\), the finite step \(t=4\) is already negative. At \(a_0=a\), the method returns the explicit counterexample \(R(4,1)=-17/243\), although the exact scalar semigroup is positive and the numerical absolute value is below one.

## Assumptions and scope
Fix \(a>0\), \(a_0>0\), \(\mu>0\), \(h\ge0\), and a scalar initial value \(u^n>0\). The differential equation is \(\dot u=-a\mu u\), with explicit part \(f_E(u)=-(a-a_0)\mu u\) and implicit part \(f_I(u)=-a_0\mu u\). The method has the classical five-row realization of ARS(4,4,3), with the old value as row zero and four implicit solves. For reproducibility its *complete* explicit and implicit arrays are
\[
A^E=\begin{pmatrix}
0&0&0&0&0\\
\frac12&0&0&0&0\\
\frac{11}{18}&\frac1{18}&0&0&0\\
\frac56&-\frac56&\frac12&0&0\\
\frac14&\frac74&\frac34&-\frac74&0
\end{pmatrix},\qquad
A^I=\begin{pmatrix}
0&0&0&0&0\\
0&\frac12&0&0&0\\
0&\frac16&\frac12&0&0\\
0&-\frac12&\frac12&\frac12&0\\
0&\frac32&-\frac32&\frac12&\frac12
\end{pmatrix}.
\]
The method is globally stiffly accurate: both output weight vectors equal the final rows, so the step value equals stage four. The result concerns *endpoint* nonnegativity \(u^{n+1}\ge0\), not positivity of intermediate stages, maximum principles for spatially coupled systems, or nonlinear equations. A single interior node of the standard centered-difference Dirichlet heat discretization realizes this scalar problem with \(\mu=2/(\Delta x)^2\).

## Proof
**1. Exact amplification.** Normalize the old value as \(Y_0=1\). At every implicit stage \(i=1,2,3,4\), the tableau gives
\[
Y_i=\frac{1-t\sum_{j=0}^{i-1}\bigl(A^I_{ij}+(r-1)A^E_{ij}\bigr)Y_j}{1+t/2}.
\]
Every denominator is strictly positive for \(t\ge0\). Because the final row equals both output vectors, \(R(t,r)=Y_4\). With \(x=t/(t+2)\in[0,1)\), exact substitution and cancellation give the *quartic polynomial*
\[
R(x,r)=\frac{18-36rx-36rx^2-36rx^3+36r^2x^2+72r^2x^3+18r^2x^4-24r^3x^3-5r^3x^4-7r^4x^4}{18}.
\]
Here \(R(x,r)\) abbreviates \(R(2x/(1-x),r)\).

**2. Sufficiency by a positive Bernstein certificate.** The degree-four Bernstein expansion is
\[
R(x,r)=\sum_{k=0}^4B_k(r)\binom4k x^k(1-x)^{4-k},
\]
with exact coefficients
\[
\begin{aligned}
B_0&=1,\\
B_1&=(2-r)/2,\\
B_2&=(3-r)(1-r)/3,\\
B_3&=\bigl(3-r(r-3)^2\bigr)/3,\\
B_4&=(1-r)(7r^3+36r^2-90r+18)/18.
\end{aligned}
\]
The cubic \(c(r)=7r^3+36r^2-90r+18\) has exactly one root \(\rho\) in \((0,1)\): its derivative \(21r^2+72r-90\) has just one critical point on this interval, a minimum, and \(c(0)=18>0\), \(c(1)=-29<0\). Rational evaluation gives \(c(22/100)>0\), \(c(221/1000)<0\), hence \(0<\rho<1/3\). For \(0<r\le\rho\), the first three coefficients and \(B_4\) are nonnegative; also \(r(3-r)^2\le9r<3\) implies \(B_3>0\). All Bernstein basis functions on \([0,1]\) are nonnegative. Thus \(R(t,r)\ge0\) for every finite nonnegative \(t\). In fact \(R(t,r)>0\) for finite \(t\), because \(B_0(1-x)^4>0\).

**3. Sharp necessity below unit ratio.** Taking \(t\to\infty\) in the exact formula gives
\[
\lim_{t\to\infty}R(t,r)=B_4(r)=\frac{(1-r)c(r)}{18}.
\]
The derivative and endpoint argument above shows \(c(r)<0\) for all \(\rho<r<1\). Hence \(B_4(r)<0\) there; by continuity, a sufficiently large *finite* step has negative amplification.

**4. Sharp necessity at and above unit ratio.** Evaluating the completed step at \(t=4\) yields
\[
R(4,r)=-\frac{H(r)}{729},\qquad
H(r)=56r^4+328r^3-1656r^2+2052r-729.
\]
The positivity of \(H\) for every \(r\ge1\) has an exact rational certificate. On \(1\le r\le3/2\), put \(v=2(r-1)\in[0,1]\). The five degree-four Bernstein coefficients of \(H(1+v/2)\) are
\[
(51,\ 89/2,\ 24,\ 27/4,\ 27/2),
\]
all strictly positive. On \(r\ge3/2\), set \(u=r-3/2\ge0\); the polynomial becomes
\[
H(r)=56u^4+664u^3+576u^2+54u+27/2>0.
\]
Thus \(R(4,r)<0\) for all \(r\ge1\), completing the if-and-only-if classification. Direct substitution at \(r=1\) yields \(R(4,1)=-17/243\).

## Verification
The companion `verify.py` reconstructs both Butcher arrays with exact rational entries, checks their common abscissae, derives all four stage values independently, expands the step as a polynomial in \(x=t/(t+2)\), checks each Bernstein coefficient, isolates the critical cubic root, verifies the large-step formula and the two positive certificates for \(H\), and checks 77 additional rational parameter-step identities. It returns `VERIFY_OK` with SymPy 1.12 or newer. Run `python verify.py`; no external input files are required. The finite evaluations are supplemental; the analytic polynomial certificates supply the proof for **all** admissible parameters and step sizes.

## Relationship to prior work
Ascher, Ruuth and Spiteri (1997) defined the ARS(4,4,3) pair and studied IMEX linear stability. Tan, Cheng and Shu (2022) investigated stability of EIN finite-difference and local DG discretizations and reported an effective stabilizer near \(0.54\) times the relevant coefficient in their tests, a *stability* observation rather than a scalar positivity guarantee. Wu and Shu (arXiv:2610.34539v1, §§3–4.6) established nonlinear *energy* estimates for several EIN methods and observed that the ARS(4,4,3) pair fails the sufficient stage-matrix criterion; they explicitly do not deduce energy instability. Neither statement implies preservation of the sign of positive data. The present assertion identifies the separate necessary-and-sufficient **completed-step scalar positivity** boundary, using the same named ARS tableau. It does not assert that generic nonlinear or matrix-valued EIN implementations inherit this threshold.

Related SSP and positivity-preserving integrator literature establishes general step restrictions and approaches using modified schemes or limiters. The exact scalar frontier above applies to the *unmodified* named pair with the specified physical/stabilizing split; a general SSP theorem or a different method's positivity radius does not supply the displayed cubic without specializing and analyzing this pair. Classical Bernstein polynomial theory is used as a proof device, not claimed as new.

## Limitations
This is a scalar endpoint statement. It neither proves nor disproves positivity of each internal stage, nor does it guarantee positivity for arbitrary multi-node Dirichlet discretizations, general graph Laplacians, state-dependent diffusion, or modified filtered/limited integrators. Its explicit counterexample shows that a one-node positive heat semidiscretization can lose sign for parameter choices outside the stated ratio. Negative amplification need not mean failure of energy contraction: at \(r=1,t=4\), its magnitude is \(17/243<1\). There is no assertion of optimal error constants, of positivity across all spatial meshes, or of historical exclusivity beyond the inspected literature. Classical method coefficients and positivity theory are acknowledged.

## References
1. Y. Wu and C.-W. Shu, *Energy stability of explicit–implicit–null time discretizations for nonlinear degenerate parabolic equations with state-dependent coefficients*, arXiv:2610.34539v1, first public 25 October 2026; especially §§3, 4.6. https://arxiv.org/abs/2610.34539
2. U. Ascher, S. Ruuth and R. Spiteri, *Implicit-Explicit Runge-Kutta Methods for Time-Dependent Partial Differential Equations*, Applied Numerical Mathematics 25 (1997), 151–167, DOI:10.1016/S0168-9274(97)00056-1. Author-hosted full text: https://steveruuth.org/wp-content/uploads/2020/10/ars.pdf
3. M. Tan, J. Cheng and C.-W. Shu, *Stability of high order finite difference and local discontinuous Galerkin schemes with explicit-implicit-null time marching for high-order dissipative and dispersive equations*, Journal of Computational Physics (2022), DOI:10.1016/j.jcp.2022.111314. https://bpb-us-w2.wpmucdn.com/sites.brown.edu/dist/0/348/files/2022/05/Stability-of-high-order-finite-difference-and-local-discontinuous-Galerkin-schemes.pdf
4. H. Hu, C.-W. Shu and X. Zhang, *Asymptotic-preserving and positivity-preserving implicit-explicit schemes for the stiff BGK equation*, SIAM Journal on Numerical Analysis (2018), DOI:10.1137/17M1144362 (methodologically related positivity preservation, but a distinct scheme).
5. *Uniform Accuracy of Implicit-Explicit Runge-Kutta Methods for Linear Hyperbolic Relaxation Systems*, Journal of Scientific Computing (2025), DOI:10.1007/s10915-025-02972-4 (Appendix A.2 reproduces the ARS(4,4,3) tableau). https://link.springer.com/article/10.1007/s10915-025-02972-4
