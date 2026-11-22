# Two sharp defector-taxis Hopf thresholds without stationary patterns in a spatial public-goods model

## Finding

For the three-field spatial public-goods model of Zhao, Zhu, Zhang and Cooney, increasing *only defector attraction toward public good* creates two successive, strictly oscillatory spatial instabilities although equal diffusion and stationary instabilities never destabilize the coexistence state. For the exact positive calibration below, mode \(k=1\) destabilizes at
\[
w_1=\frac{1297}{18},
\]
mode \(k=2\) destabilizes at
\[
w_2=\frac{1477}{6},
\]
and no larger spatial mode can destabilize for any nonnegative attraction parameter. The two crossings have exact imaginary-frequency squares \(3431/144\) and \(797/3\).

## Assumptions and scope

On the interval \(0\le x\le\pi\) impose zero normal flux and consider the three reactions
\[
\begin{aligned}
\partial_t u&=D_u\partial_{xx}u+u[r_u\phi-c-\gamma(u+v)-\mu_u],\\
\partial_t v&=D_v\partial_x(\partial_xv-2wv\partial_x\phi)+v[r_v\phi-\gamma(u+v)-\mu_v],\\
\partial_t\phi&=D_\phi\partial_{xx}\phi+cu-\kappa(u+v)\phi-\delta\phi.
\end{aligned}
\]
Here \(u,v\) represent cooperators and defectors, \(\phi\) represents the shared good, and \(w\ge0\) is defectors' directed-motion sensitivity. The corresponding general model allows cooperator taxis as well, but it is fixed to zero here. Choose
\[
(r_u,r_v,c,\gamma,\mu_u,\mu_v,\kappa,\delta)=(12,13,5,8,1,7,1,1/2),\qquad D_u=D_v=D_\phi=1/4.
\]
Every reaction coefficient other than the allowed zero cooperator taxis is strictly positive. The constant coexistence solution is \((u_*,v_*,\phi_*)=(1/4,1/2,1)\). We classify the spectra of the linearization on the cosine Neumann modes \(k\in\mathbb Z_{\ge0}\) at this equilibrium, with all parameters fixed except \(w\).

## Proof

**1. Exact physical equilibrium.** Substitution gives
\[
12-5-8(3/4)-1=0,\quad13-8(3/4)-7=0,\quad5/4-3/4-1/2=0.
\]
The linearized matrix for the \(k\)-th Neumann mode, with \(q=k^2\), is
\[
M(q,w)=\begin{pmatrix}
-2-q/4&-2&3\\
-4&-4-q/4&13/2+qw/4\\
4&-1&-5/4-q/4
\end{pmatrix}.
\]
Its characteristic polynomial is \(\lambda^3+A\lambda^2+B\lambda+C\), where direct expansion gives
\[
\begin{aligned}
A&=(3q+29)/4,\\
B&=(3q^2+4qw+58q+32)/16,\\
C&=(q^3+4q^2w+29q^2+160qw+32q+320)/64.
\end{aligned}
\]
Thus \(A,B,C>0\) for every \(q\ge0,w\ge0\). The zero spatial mode \(q=0\) is strictly stable since its Routh–Hurwitz margin is \(AB-C=19/2>0\). Notice that \(C>0\) excludes any zero-eigenvalue stationary crossing for any spatial mode and attraction value.

**2. Exact Routh–Hurwitz margin and all-mode classification.** The remaining cubic stability criterion is \(AB>C\). Algebra yields
\[
H(q,w):=AB-C=\frac{4q^3+116q^2+873q+304+2q(2q-11)w}{32}.
\]
For every \(k\ge3\), \(q=k^2\ge9\), so both the constant and attraction-dependent terms are strictly positive. Those modes are exponentially stable for every \(w\ge0\). For \(k=1\) and \(k=2\), respectively,
\[
H(1,w)=\frac{1297-18w}{32},\qquad
H(4,w)=\frac{5908-24w}{32}.
\]
The critical values are therefore precisely \(w_1=1297/18\) and \(w_2=1477/6\). Their order follows from \(1297\cdot6<1477\cdot18\). With positive \(A,B,C\), the cubic Routh–Hurwitz criterion shows strict stability when \(H>0\) and strict instability when \(H<0\). No positive real eigenvalue can arise because its characteristic polynomial is positive on the nonnegative real axis. Consequently each unstable mode contains a conjugate pair with strictly positive real part; there are no other unstable modes.

**3. Purely oscillatory, transverse crossings.** At \(H=0\), the polynomial factors as
\[
(\lambda+A)(\lambda^2+B),
\]
with \(A,B>0\). The critical frequencies squared are \(B(1,w_1)=3431/144\) and \(B(4,w_2)=797/3\). For a simple imaginary root, implicit differentiation of the cubic gives
\[
\frac{d\,\mathrm{Re}\,\lambda}{dw}=-\frac{\partial_wH}{2(A^2+B)}.
\]
Because \(\partial_wH(1,w)=-18/32<0\) and \(\partial_wH(4,w)=-24/32<0\), both crossings are transverse into the unstable half-plane. At each threshold the other mode remains strictly on its indicated side and all higher modes remain stable.

## Verification

The standalone `VERIFY.py` uses exact symbolic rational computations to reconstruct the equilibrium, modal matrix, characteristic polynomial, Routh–Hurwitz margin, threshold factors and both critical frequency squares. It also checks example eigenvalues numerically as a supplementary diagnostic. Run it from the extracted package with `python VERIFY.py` (requires Python and SymPy). The algebraic proof above, not a finite mode enumeration, establishes the all-mode assertion for the infinite Neumann spectrum.

## Relationship to prior work

Zhao et al. (2026) derived this three-field model and its spatial linearization; they focused on stationary Turing modes under enhanced defector diffusion and on directed-motion instabilities driven by cooperators' movement sensitivity. Their discussion identifies the wider classification of oscillatory instabilities with differential motion as an open direction. The same general use of three-field characteristic polynomials and Routh–Hurwitz conditions is prior mathematics, not newly claimed. A related indexed result gives an isolated oscillatory mode with *diffusion alone* and distinct parameters, but does not imply this exact equal-diffusivity, defector-taxis-driven two-threshold phase diagram. Funk and Hauert (2019) study directed migration in a different spatial ecological public-goods model, while Cheng et al. (2024) study Turing–Hopf behavior in a distinct replicator/resource feedback system. Historical priority outside the inspected sources remains uncertain.

## Limitations

This is a fixed-calibration, linear spectral result; the model does not become equivalent to a universal phase theorem over all ecological parameters. It establishes no nonlinear stable periodic orbit, periodic pattern, long-time dynamics, or ecological benefit/harm. A pure imaginary pair at equality is neutral at linear order, not an exponentially stable mode. The cooperator taxis coefficient is exactly zero, and equality of the three diffusion rates is essential to this stated formula. Independent scientific validation has not been performed.

## References

1. Zhao, Y., Zhu, K., Zhang, Y., Cooney, D. B., *Pattern Formation in a Spatial Public Goods Dilemma due to Diffusive or Directed Motion*, arXiv:2603.21025v1, first public March 22, 2026. https://arxiv.org/abs/2603.21025 ; https://doi.org/10.1007/s11538-026-01733-0 .
2. Funk, F., Hauert, C., *Directed migration shapes cooperation in spatial ecological public goods games*, PLoS Computational Biology 15 (2019), e1006948. https://doi.org/10.1371/journal.pcbi.1006948 .
3. Cheng, H. et al., *Evolution of Cooperation in Spatio-Temporal Evolutionary Games with Public Goods Feedback*, Bulletin of Mathematical Biology 86 (2024), article 67. https://doi.org/10.1007/s11538-024-01296-y .
