# Pinching limit of genus-two sine-Gordon waves to kink-breather on cnoidal background

## Context
The sine-Gordon equation u_tt-u_xx+sin(u)=0 admits real finite-gap (Baker-Akhiezer) solutions built from nonsingular hyperelliptic curves Gamma with admissible divisors. A natural degeneration question is what happens when one spectral gap pinches to a double point while the remaining branch points stay fixed. For KdV, partial degeneration to solitons on an elliptic background was developed in detail (Bertola-Jenkins-Tovbis); for sine-Gordon, the multiscale limit was used for topological charge (Grinevich-Kaipa) with diverging frequencies and no limiting solution. The target here is the complementary fixed-background single-gap pinching with a quantitative uniform rate.

## Definitions
- Gamma_delta: mu^2=prod_{j=1}^6(E-E_j(delta)), nonsingular real hyperelliptic genus-two curve; E_2(delta),E_3(delta)->E_s with |E_2-E_3|~delta; other four branch points fixed at distance >=d_0>0 from E_s and each other.
- D_delta: real nonspecial admissible divisor of degree 2, continued continuously in the stable degeneration as A(D_delta)=alpha(delta)+sigma*B_{.2}(delta)/2 with sigma in {0,1} and alpha(delta)->alpha_0 finite.
- u_delta(x,t): real Baker-Akhiezer solution via Its-Matveev reconstruction u_delta=F_delta(Z_delta), Z_delta=U(delta)x+V(delta)t+A(D_delta)+K_delta, F_delta=2i log[Theta(Z+D^+)/Theta(Z+D^-)].
- u_cn: pure genus-one cnoidal background from pinched curve Gamma_0.
- u_0: dressed limit (7)-(9): one-gap theta ratio with one exponential factor e^{phi}, phi=2 pi i(kappa x+nu t)+phi_0.

## Result
On every fixed compact K in R^2_{x,t}, u_delta converges uniformly to the explicit kink-breather on genus-one cnoidal background u_0 given by formula (9):
u_0=2i log[(Theta_1(z_1^0+D^+_1)+e^{phi}Theta_1(z_1^0-b+D^+_1))/(Theta_1(z_1^0+D^-_1)+e^{phi}Theta_1(z_1^0-b+D^-_1))],
with sup_K|u_delta-u_0|<=C(K)delta for 0<delta<=delta_0(K), C(K)=L[C_Theta+C_Z(1+diam K)+C_B] from (12), explicit from separation data, theta majorants, and m_K^{-1}. The sigma=0 divisor case converges at the same rate to the pure background endpoint (phi_0->+-infinity). Hence no pinching family gives failure of convergence or a limit outside the stated dressed family.

## Proof / Evidence
Lemma 1 (period plumbing): B_11=tau+O(delta^2), B_12=b+O(delta^2), B_22=(1/pi i)log delta+c_0+O(delta) so q=exp(pi i B_22)=c_*delta(1+O(delta)); U_2->kappa, V_2->nu with O(delta); other components O(delta^2). Via normalized a-period matrix and split b_2 integral (log part plus bounded exterior).
Lemma 2 (Fay degeneration): exact identity Theta_2=sum_n e^{pi i n^2 B_22+2 pi i n z_2}Theta_1(z_1+nB_12); with z_2=zeta+sigma B_22/2+c, for sigma=1 the n=0,-1 terms give the dressed two-term form (7) with O(delta) remainder (in fact O(delta^2)); for sigma=0 both n=+-1 are O(delta). Gaussian majorants sum|q|^{n^2}e^{2pi|n|M} uniform on compacts.
Lemma 3 (reconstruction stability): away from theta divisor (|denom|>=m_K>0 for real admissible data), log-ratio is Lipschitz with L(m_K^{-1},max|Theta|); phase error |Z_delta-Z^0|<=C_1 delta(1+|x|+|t|) and modulus error O(delta) combine to C(K)delta.
Numerical confirmation (not proof): genus-2 theta first-order distance/delta=0.414 constant over delta in {0.2,0.1,0.05,0.025}; dressed remainder ~delta^2 (5.9e-6 to 1.4e-9); field proxy error 1.1e-5 to 2.8e-9.

## Limitations
Compact-local only: C(K) grows with diam(K) and m_K^{-1}; no uniform-in-R^2 claim. Divisor needs definite sigma in {0,1}. Constant is explicit via formula (12) computable from branch-point data, exhibited numerically as order unity on model compact rather than one closed-form number. Standard real-smoothness and Rauch-type plumbing used with proof sketches and uniform estimates.

## Reproducibility
Run python3 output/artifacts/num_check.py (theta Fay truncation scaling) and python3 output/artifacts/field_check.py (reconstruction-level error scaling), pure standard library.

## References
- Bertola, Jenkins, Tovbis, Partial degeneration of finite gap solutions to KdV (arXiv:2210.01350).
- Grinevich, Kaipa, Multiscale limit for finite-gap sine-Gordon solutions (arXiv:0904.4520; DOI 10.1134/S0081543809030031).
- Ala, Heun-Wronskian Analysis of the Lax Spectrum for Sine-Gordon Kink-Breather Solutions (DOI 10.53570/jnt.1833273).
- Krichever; Its-Matveev; Belokolos-Bobenko-Enolskii-Its-Matveev; Zakharov-Takhtadji-Faddeev; Fay.
