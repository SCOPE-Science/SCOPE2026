# All-feedback uniqueness and monotone prevalence in the prevalence-driven SIRCm model
## Finding
For the prevalence-driven SIRCm system of Ramírez-Gutiérrez, Lóczi, Muñoz-Moncayo, and Ketcheson (arXiv:2610.01111v1), restrict to diagonal feedback \(\varepsilon_1=\varepsilon_2=\varepsilon\ge 0\), positive rates \(\mu,\beta,\alpha,\delta,\gamma>0\), \(\sigma\in[0,1]\), and \(\mathcal R_0=\beta/(\mu+\alpha)>1\). Then for every \(\varepsilon\ge0\) there is exactly one endemic equilibrium, and its endemic prevalence \(I^*(\varepsilon)\) is strictly increasing in \(\varepsilon\). This claim concerns equilibrium existence, uniqueness, and prevalence monotonicity only; it does not assert local or global stability.

## Assumptions and scope
The model is the prevalence-driven specialization \(g(x)=I\) of the SIRCm system in arXiv:2610.01111v1,
\[
\dot S=\mu(1-S)-\beta SI+(1+\varepsilon I)\gamma C,
\]
\[
\dot I=\beta SI+\sigma\beta CI-(\mu+\alpha)I,
\]
\[
\dot R=(1-\sigma)\beta CI+\alpha I-\mu R-(1+\varepsilon I)\delta R,
\]
\[
\dot C=(1+\varepsilon I)\delta R-\beta CI-\mu C-(1+\varepsilon I)\gamma C.
\]
Assume \(\mu,\beta,\alpha,\delta,\gamma>0\), \(\sigma\in[0,1]\), \(\varepsilon\ge0\), and \(\mathcal R_0=\beta/(\mu+\alpha)>1\). The state lies in the unit simplex. Put \(r=\mathcal R_0^{-1}=(\mu+\alpha)/\beta\) and \(I_\infty=1-r>0\).

## Proof
At any endemic equilibrium \(I>0\), the infected balance gives \(S+\sigma C=r\). Set \(h=1+\varepsilon I\) and
\[
\Delta=\beta I(\mu+\sigma\delta h)+(\mu+\delta h)(\mu+\gamma h)>0.
\]
Solving the \(R\)- and \(C\)-balance equations gives
\[
R=\frac{\alpha I(\beta I+\mu+\gamma h)}{\Delta},\qquad
C=\frac{\alpha I\delta h}{\Delta}.
\]
Hence
\[
R+(1-\sigma)C=I H(I,h),\qquad
H(I,h)=\frac{\alpha[\beta I+\mu+h(\gamma+(1-\sigma)\delta)]}{\Delta}>0.
\]
Using conservation with \(S=r-\sigma C\), every endemic equilibrium is therefore equivalent to a root of
\[
\Phi_\varepsilon(I):=I[1+H(I,1+\varepsilon I)]=I_\infty.
\]
The endpoints satisfy \(\Phi_\varepsilon(0)=0<I_\infty\) and \(\Phi_\varepsilon(I_\infty)>I_\infty\).

To prove strict monotonicity in \(I\), write \(t=h-1=\varepsilon I\). Direct differentiation and simplification give
\[
\Phi_\varepsilon'(I)=1+\frac{\alpha[A_0+2tB_1+t^2B_2]}{\Delta^2}>1,
\]
where
\[
\begin{aligned}
A_0={}&I^2\beta^2(\mu+\delta\sigma)+2I\beta(\delta\gamma+\delta\mu+\gamma\mu+\mu^2)\\
&+\delta^2(\gamma+\mu)(1-\sigma)+\delta\gamma^2+\delta\gamma\mu(3-\sigma)\\
&+\delta\mu^2(2-\sigma)+\gamma^2\mu+2\gamma\mu^2+\mu^3,
\end{aligned}
\]
\[
\begin{aligned}
B_1={}&I\beta[\delta\gamma+\delta\mu(1-\sigma)+\gamma\mu]+\delta^2(\gamma+\mu)(1-\sigma)\\
&+\delta\gamma^2+\delta\gamma\mu(2-\sigma)+\delta\mu^2(1-\sigma)+\gamma^2\mu+\gamma\mu^2,
\end{aligned}
\]
and
\[
B_2=\delta^2(\gamma+\mu)(1-\sigma)+\delta\gamma^2+\delta\gamma\mu(1-\sigma)+\gamma^2\mu.
\]
Every displayed summand is nonnegative under the assumptions, and each coefficient is strictly positive because the rate parameters are positive. Thus \(\Phi_\varepsilon\) is strictly increasing and crosses \(I_\infty\) exactly once in \((0,I_\infty)\).

The resulting root is a physical equilibrium. The formulas above give \(R,C>0\). If \(\sigma=0\), then \(S=r>0\). If \(\sigma>0\), then \(\Delta>\beta I\sigma\delta h\) and \(\mu+\alpha>\alpha\), so \(\beta\sigma\alpha I\delta h<(\mu+\alpha)\Delta\), which is equivalent to \(\sigma C<r\); hence \(S=r-\sigma C>0\). The scalar equation gives conservation, the \(I\)-balance follows from \(S+\sigma C=r\), and the remaining balance equations hold by construction.

Finally, at fixed \(I>0\),
\[
\partial_h H=-\frac{\alpha\delta Q}{\Delta^2}<0,
\]
with
\[
Q=\sigma\beta^2I^2+2\beta\gamma hI+2\sigma\beta\mu I+(1-\sigma)\delta\gamma h^2+\gamma^2h^2+2\gamma\mu h+\sigma\mu^2>0.
\]
Therefore increasing \(\varepsilon\) strictly decreases \(\Phi_\varepsilon(I)\) at every fixed positive \(I\). Since each \(\Phi_\varepsilon\) is strictly increasing and all roots meet the same level \(I_\infty\), the unique root \(I^*(\varepsilon)\) is strictly increasing in \(\varepsilon\).

## Verification
The bundled `verify.py` reconstructs \(R\), \(C\), \(H\), and \(\Delta\) symbolically; verifies both equilibrium balance identities; verifies \(R+(1-\sigma)C=IH\); checks the displayed formula for \(\Phi_\varepsilon'(I)\); and checks the displayed formula for \(\partial_hH\). Running it with SymPy prints `VERIFY_OK`. Positivity and uniqueness use the sign assumptions stated above and are proved analytically, not by finite sampling.

## Relationship to prior work
Ramírez-Gutiérrez et al. prove existence of an endemic equilibrium for arbitrary feedback strength when \(\mathcal R_0>1\), and prove uniqueness in weak- and strong-feedback regimes. For prevalence-driven feedback, their Remark 4.4 reduces the equilibrium problem to a cubic and gives \(\varepsilon\le1\) as a sufficient uniqueness condition; the paper also presents numerical continuation through intermediate feedback. The argument above closes that intermediate diagonal-feedback gap by replacing coefficient-sign control of the cubic with a globally monotone scalar balance. Casagrandi et al. study the zero-feedback SIRC model and do not imply this state-dependent all-feedback result.

## Limitations
The proof is restricted to prevalence-driven feedback with equal strengths \(\varepsilon_1=\varepsilon_2\). It does not prove uniqueness for unequal feedback strengths, transmission-driven feedback, or other feedback functions. It also does not establish local stability, global attraction, absence of Hopf bifurcation, or monotonicity of the other compartments.

## References
1. D. R. Ramírez-Gutiérrez, L. Lóczi, C. Muñoz-Moncayo, and D. I. Ketcheson, “Compartmental epidemiological models with infection-driven immune escape,” arXiv:2610.01111v1, first public 2026-10-01. In particular, Theorem 3.1, Lemma 3.14, Section 4, and Remark 4.4.
2. R. Casagrandi, L. Bolzoni, S. A. Levin, and V. Andreasen, “The SIRC model and influenza A,” Mathematical Biosciences 200 (2006), DOI 10.1016/j.mbs.2005.12.029.
