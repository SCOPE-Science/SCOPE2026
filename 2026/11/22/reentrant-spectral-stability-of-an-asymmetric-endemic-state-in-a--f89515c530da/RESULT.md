# Reentrant spectral stability of an asymmetric endemic state in an opinion–SIS model

## Finding

In the two-opinion infection-induced-switching SIS model of Götz, Krüger, Niedzielewski, Schneider and Pabjan, specialize to equal susceptibility and zero infectivity for the second infectious opinion class. For any positive asymmetric endemic equilibrium whose susceptible-opinion ratio is \(0<z<1\), all eigenvalues of the simplex linearization have strictly negative real parts if and only if the following **quadratic inequality** holds in the dimensionless endemic-prevalence parameter \(u>0\):
\[
P_z(u):=A(z)u^2+B(z)u+C(z)>0,
\]
where
\[
\begin{aligned}
A(z)&=(1-z)^2(z^2-3z+1),\\
B(z)&=(z+1)(z^4-3z+1),\\
C(z)&=z(z+1)^2(2z^2-2z+1).
\end{aligned}
\]
Thus \(P_z(u)>0\) implies local exponential stability within the simplex, and \(P_z(u)<0\) implies instability. Equality gives one negative eigenvalue and a nonzero purely imaginary conjugate pair; no nonlinear stability verdict is made at equality. A ratio \(z\) permits exactly **two distinct positive spectral crossings** along this fixed-ratio family if and only if \(A(z)>0\), \(B(z)<0\), and \(B(z)^2>4A(z)C(z)\). These conditions characterize a region of the two-parameter endemic family, not merely an isolated numerical experiment.

For the exact ratio \(z=3/8\),
\[
P_{3/8}(u)=\frac{200u^2-4741u+12342}{32768}.
\]
Writing
\[
u_\pm=\frac{4741\pm11\sqrt{104161}}{400}
\quad (u_-\approx2.97715458419,\quad u_+\approx20.7278454158),
\]
there is a stable–unstable–stable sequence as \(u\) increases: stable for \(0<u<u_-\) and for \(u>u_+\), unstable for \(u_-<u<u_+\), and exactly a transversal imaginary-pair crossing at each endpoint. Both model parameters vary positively along the family, with \(R=u+11/8\) and \(p=64uR^2/33\). No assertion about the existence, uniqueness or nonlinear stability of periodic orbits is made.

## Assumptions and scope

Normalize time by the recovery rate and denote by \(S_A,S_B,I_A,I_B\) the fractions of susceptible and infectious people in two opinion classes. They are nonnegative and sum to one. Consider the source model's equations with \(\alpha=0\) (the second infectious class contributes no infection), \(\delta=1\) (equal susceptibility), \(R=\beta/\gamma>0\), and \(p=\widetilde p/\gamma>0\):
\[
\begin{aligned}
\dot S_A&=-RS_AI_A+pS_AS_B(S_A-S_B)+I_A,\\
\dot S_B&=-RS_BI_A+pS_AS_B(S_B-S_A)+I_B,\\
\dot I_A&=RS_BI_A-I_A,\\
\dot I_B&=RS_AI_A-I_B.
\end{aligned}
\]
The analysis is for the deterministic, homogeneously mixed, three-dimensional population simplex, without demography. The local stability notion is stability **within this simplex**. Here \(\dot{}\) means derivative in normalized time. Introduce \(x=S_A\), \(y=S_B\), \(v=I_A\), and \(I_B=1-x-y-v\). Then
\[
\dot x=-Rxv+pxy(x-y)+v,\quad
\dot y=-Ryv+pxy(y-x)+1-x-y-v,\quad
\dot v=(Ry-1)v.
\]

Every strictly positive, asymmetric endemic equilibrium with \(x<y\) can be parameterized uniquely by its susceptible ratio \(z=x/y\in(0,1)\) and \(u=R-1-z>0\):
\[
R=1+z+u,\qquad
p=\frac{R^2u}{z(1+z)},\qquad
(S_A,S_B,I_A,I_B)=\frac1R\left(z,1,\frac{u}{1+z},\frac{zu}{1+z}\right).
\]
Conversely these formulas yield a strictly positive feasible endemic equilibrium for every \(0<z<1\), \(u>0\). In the fixed-\(z\) experiment the model's two positive control parameters \(R\) and \(p\) vary together; it is **not** claimed that one can vary \(R\) alone while keeping \(p\) fixed and obtain the same threshold formula.

## Proof

**Equilibrium parameterization.** At any endemic equilibrium \(v>0\), the third reduced equation forces \(Ry=1\). Put \(x=z/R\) with \(0<z<1\). From the fourth compartment's stationary equation \(I_B=Rxv=zv\), and mass conservation gives \((1+z)v=(R-1-z)/R\). Positivity gives \(u=R-1-z>0\) and \(v=u/[R(1+z)]\). The first stationary equation becomes
\[
0=(1-z)\left(v-\frac{pz}{R^3}\right).
\]
Because \(z\ne1\), this forces exactly \(p=R^2u/[z(1+z)]\). Direct substitution then verifies the second stationary equation. All four coordinates are positive and sum to one.

**Exact Jacobian and Hurwitz determinant.** Differentiating the reduced three-equation field and substituting these equilibrium parameters gives
\[
J_{z,u}=\begin{pmatrix}
\frac{u(z-1)}{z(z+1)}&\frac{u(z-2)}{z+1}&1-z\\
\frac{u(1-2z)-z(z+1)}{z(z+1)}&\frac{u(1-z)-(z+1)}{z+1}&-2\\
0&\frac{u}{z+1}&0
\end{pmatrix}.
\]
Its trace and determinant are
\[
\operatorname{tr}J=-\frac{u(1-z)^2+z(z+1)}{z(z+1)}<0,\qquad
\det J=\frac{u(z-1)[u(2z+1)+z(z+1)]}{z(z+1)^2}<0.
\]
Writing \(S_2(J)\) for the sum of principal two-by-two minors,
\[
S_2(J)=\frac{u\{u(z^2-3z+1)+z^3+1\}}{z(z+1)^2},
\]
and the third Hurwitz determinant factors **exactly** as
\[
H:=(-\operatorname{tr}J)S_2(J)+\det J
=\frac{u}{z^2(z+1)^3}\,P_z(u).
\]
For a real cubic characteristic polynomial \(\lambda^3+a_1\lambda^2+a_2\lambda+a_3\), the Routh–Hurwitz criterion for all roots to have negative real parts is \(a_1>0\), \(a_3>0\), \(a_1a_2>a_3\). Here \(a_1=-\operatorname{tr}J>0\), \(a_3=-\det J>0\), and \(a_1a_2-a_3=H\). The last inequality also enforces \(a_2>0\), so no additional sign hypothesis is needed. This proves the exact Hurwitz criterion \(P_z(u)>0\). For \(P_z(u)=0\), the characteristic polynomial factors as \((\lambda-\operatorname{tr}J)(\lambda^2+S_2(J))\); since both trace and determinant are negative, \(S_2(J)=\det J/\operatorname{tr}J>0\), proving the asserted imaginary pair. Conversely, a root on the imaginary axis cannot be zero (since \(a_3>0\)); substitution of \(i\omega\) with \(\omega\ne0\) forces \(a_2=\omega^2\) and \(a_3=a_1a_2\). Therefore \(P_z(u)<0\) gives a root in the open right half-plane. The equilibrium is interior, so the linearized stability and instability theorems apply in the reduced simplex coordinates for the strict signs, but do not decide nonlinear stability when \(P_z(u)=0\).

**Two-crossing classification.** For every \(0<z<1\), \(C(z)>0\), since \(2z^2-2z+1=2(z-1/2)^2+1/2>0\). A quadratic \(A u^2+B u+C\) with \(C>0\) has two distinct *positive* zeros exactly when \(A>0\), \(B<0\), and \(B^2-4AC>0\): the discriminant gives real distinct roots, and their positive sum and product force both roots positive. In the two-root case both are simple. At any such simple positive zero, \(H'(u)\ne0\) by the positive prefactor of \(P_z(u)\), and the implicit differentiation formula below shows transversality. Conversely any imaginary-pair crossing must be a zero of \(H\). This proves the parameter-domain statement.

**Exact reentrance.** At \(z=3/8\) direct rational substitution yields
\[
\begin{aligned}
\operatorname{tr}J&=-\frac{25u+33}{33},\\
\det J&=-\frac{5u(112u+33)}{363},\\
S_2(J)&=\frac{u(8u+539)}{363},\\
H&=\frac{u(200u^2-4741u+12342)}{11979}.
\end{aligned}
\]
The quadratic has discriminant \(11^2\cdot104161>0\), positive leading coefficient and positive constant, with two distinct positive zeros \(u_-\) and \(u_+\) stated above. Therefore \(H\) is positive below the first zero and above the second, and negative strictly between. Since \(S_2(J)>0\) everywhere on this family, the unstable interval has a right-half-plane complex conjugate pair, not a positive real eigenvalue. At either zero the pair is nonzero imaginary, and the third eigenvalue equals the negative trace.

For transversality, use \(a_1=-\operatorname{tr}J\), \(a_2=S_2(J)\) and \(H=a_1a_2-a_3\). This argument applies at fixed \(z\) to any zero of \(H\) with \(u>0\). The root \(i\sqrt{a_2}\) is simple, since the factorization separates it from the other two roots. Implicit differentiation of the characteristic polynomial there gives
\[
\left.\frac{d}{du}\operatorname{Re}\lambda\right|_{H=0}
=-\frac{H'(u)}{2(a_1^2+a_2)}.
\]
The derivative \(H'(u_\pm)\) is nonzero because \(u_\pm>0\) are distinct roots of the quadratic. It is negative at \(u_-\), positive at \(u_+\). Accordingly the pair crosses to positive real part at \(u_-\) and back to negative real part at \(u_+\). This establishes both strict transitions without inferring nonlinear periodic-orbit bifurcation properties.

## Verification

The included `verify.py` requires Python, SymPy and NumPy. Running `python verify.py` checks the four-state equilibrium residuals, feasible mass balance, the entire symbolic Jacobian, trace, determinant, principal-minor identity, factorization of the Hurwitz determinant, the special rational family, the exact algebraic roots and their nonzero discriminant, and eigenvalue signs at three rational parameter points.

For \(z=3/8\), the exact rational checks at \(u=1,10,30\) give respectively \(200u^2-4741u+12342=7801,-15068,50112\); their linear-stability classifications are stable, unstable with two positive-real-part eigenvalues, and stable. The exact all-parameter proof is algebraic; these three finite numerical spectral tests are diagnostics, not its justification. No trajectory simulations or extrapolation from finite tests are used as infinite-time evidence.

## Relationship to prior work

Götz et al. (2025 preprint, 2026 journal) introduce the four-compartment opinion–epidemic model, derive the asymmetric endemic branch for \(\alpha=0,\delta=1\), and state a negative-trace criterion and determinant sign condition. Their preprint, Section 3, page 7, explicitly leaves the remaining fifth-order Routh–Hurwitz inequality unanalyzed and instead displays numerical stability heatmaps (Figure 2). The journal's Appendix A.3 likewise describes that inequality but does not supply this fixed-ratio quadratic factorization or the exact reentrant thresholds. Their numerical work may already display aspects of nonmonotone stability: the contribution here is the exact model-specific algebraic criterion, all-ratio two-crossing condition and rigorous transversal endpoints, not the first suggestion that such epidemic models can oscillate.

The classical Routh–Hurwitz criterion and general local spectral-crossing methods are standard background; they do not themselves imply the factored polynomial or its sign classification for this specific endemic branch. Earlier adaptive SIS and opinion–epidemic studies address different state variables and different feedback equations. The claim is a quantitative completion of one source-model stability question, not a universal theorem for adaptive SIS systems.

## Limitations

This is a deterministic, homogeneous-mixing, \(\alpha=0,\delta=1\) result. It does not describe cases with \(\alpha>0\), unequal susceptibility, stochastic finite populations, spatial spread, or global basins. It concerns the nonbalanced endemic branch with \(0<z<1\); other equilibria may coexist, including a stable disease-free state. The sign test does not determine nonlinear stability on the neutral locus \(P_z(u)=0\). Imaginary-pair transversality alone does **not** establish nonzero first Lyapunov coefficients, branch direction, actual periodic orbit existence, stability of oscillations, or global dynamical outcomes. Historical-priority comparison is literature-bounded.

## References

1. T. Götz, T. Krüger, K. Niedzielewski, J. Schneider and B. Pabjan, *Coupling opinion dynamics and epidemiology*, arXiv:2512.10612v1, first public December 11, 2025, https://arxiv.org/abs/2512.10612; especially equations (3)–(8), Section 3 and Figure 2. Journal version: *Scientific Reports* (2026), https://doi.org/10.1038/s41598-026-66686-9, Appendix A.3.
2. M. A. Achterberg and M. Sensi, *A minimal model for adaptive SIS epidemics*, *Nonlinear Dynamics* 111 (2023), https://doi.org/10.1007/s11071-023-08498-4 (a different two-variable adaptive-contact model).
3. S. Samadi, J. I. Caiza, S. Gracy and P. E. Paré, *A Networked SIS Epidemic–Opinion Model with Higher-Order Interactions*, arXiv:2608.31032 (different community-network and group-transmission mechanisms), https://arxiv.org/abs/2608.31032.
