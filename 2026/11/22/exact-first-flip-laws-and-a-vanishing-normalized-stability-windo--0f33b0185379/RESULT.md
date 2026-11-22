# Exact first-flip laws and a vanishing normalized stability window in a generalized rational logistic map

## Finding
For the family
\[
G_{\rho,\beta}(x)=\frac{\rho x(1-x)^\beta}{1+x},\qquad 0\le x\le1,\quad\beta\ge2,
\]
the first loss of stability of the positive fixed point occurs at the exact parameter
\[
p_\beta=\frac{\sqrt{1+8/(\beta+1)}-1}{2},\qquad
\rho_\beta=\frac{1+p_\beta}{(1-p_\beta)^\beta}.
\]
For \(1<\rho<\rho_\beta\), the positive fixed point attracts locally at an exponential rate; at \(\rho=\rho_\beta\) it remains locally attracting with sharp inverse-square relaxation; for \(\rho>\rho_\beta\) it is repelling. The flip creates a locally unique stable prime-two orbit on the larger-parameter side. Its amplitudes and return multiplier have exact first-order coefficients given below. Although \(\rho_\beta\) grows toward the finite constant \(e^2\), its fraction of the admissible parameter range goes to zero as \(e/\beta\). The rescaled near-flip amplitudes have the exact Ricker-map limit.

## Assumptions and scope
Fix a real exponent \(\beta\ge2\). Define \(h_\beta(x)=x(1-x)^\beta/(1+x)\) and the largest self-map parameter
\[
\rho_{\max}(\beta)=\left(\max_{x\in[0,1]}h_\beta(x)\right)^{-1}.
\]
The unique interior positive fixed point for each \(\rho>1\) is \(p(\rho)\), characterized by \(\rho=(1+p)/(1-p)^\beta\). The critical state \(p=p_\beta\) and parameter \(\rho_\beta\) are defined above. Put
\[
L_\beta=\frac{1+2p}{(1-p)(1+p)^2}>0,
\qquad
C_\beta=\frac{(p+2)(1+3p+p^2-4p^3)}{3p^2(1-p)^2(1+p)^4}>0,
\qquad K_\beta=\frac{L_\beta}{C_\beta}.
\]
The theorem is local near the positive fixed point, except for the exact fixed-point-stability threshold and parameter-range asymptotics. No global attraction or assertion about all periodic orbits is made.

## Proof
**1. Fixed-point multiplier and location of the flip.** The equation for a positive fixed point is \(\rho=(1+p)/(1-p)^\beta\), strictly increasing in \(p\in(0,1)\). Differentiating gives the multiplier
\[
\lambda(p)=G'_{\rho,\beta}(p)=\frac{1}{1+p}-\frac{\beta p}{1-p}.
\]
For fixed \(\beta\), \(\lambda(p)\) strictly decreases from \(1\), crosses \(-1\) exactly once, and solving \(\lambda=-1\) gives \((\beta+1)p(p+1)=2\). Thus its unique solution is \(p_\beta\) as asserted. On \(0<p<p_\beta\), \(-1<\lambda<1\); on \(p>p_\beta\), \(\lambda<-1\).

**2. The critical parameter is admissible for every \(\beta\ge2\).** Let \(R(p)=\log(1+p)-[2/(p(1+p))-1]\log(1-p)\). Direct differentiation simplifies to
\[
R'(p)=\frac{2[p^3+2p^2+p+(2p+1)\log(1-p)]}{p^2(1+p)^2}<0,
\]
since \(\log(1-p)<-p-p^2/2\). Also \(R(p)\to2\) as \(p\downarrow0\); hence \(\rho_\beta<e^2<8\). For \(\beta\ge2\), \(h_\beta(x)\le h_2(x)\). Further
\[
1+x-8x(1-x)^2=1-7x+16x^2-8x^3>0\quad(0\le x\le1),
\]
because its only critical point inside \([0,1]\) is \((8-\sqrt{22})/12\), at which its value equals \(29/27-11\sqrt{22}/54>0\). Thus \(\max h_\beta<1/8\), whence \(\rho_{\max}(\beta)>8>\rho_\beta\).

**3. Nondegenerate supercritical flip.** Differentiate \(G\) at \((p,\rho_\beta)\). Writing \(u=x-p\), its Taylor expansion at the critical parameter is \(G(p+u)-p=-u+A_\beta u^2+B_\beta u^3+O(u^4)\), with
\[
A_\beta=-\frac{1+p+p^2}{(1-p)(1+p)^2},\qquad
A_\beta^2+B_\beta=C_\beta>0.
\]
The last equality follows by differentiating the logarithmic derivative \(1/x-\beta/(1-x)-1/(1+x)\) twice and substituting \((\beta+1)p(p+1)=2\). The factor \(1+3p+p^2-4p^3\) is positive for \(0<p<1\), because \(p^2-4p^3\ge-3p^2\) and \(1+3p-3p^2>0\). For \(\delta=\log(\rho/\rho_\beta)\), differentiation of \(\lambda(p(\rho))\) gives \(\lambda=-1-L_\beta\delta+O(\delta^2)\). Expansion of the second iterate about the moving fixed point is
\[
G^{\circ2}(p(\rho)+u)-p(\rho)-u
=2L_\beta\delta\,u-2C_\beta u^3+O(|\delta|^2|u|+|\delta|u^2+|u|^4).
\]
Divide by \(u\) and apply the implicit-function theorem with \(u=\sqrt{\delta}\,v\). The two nonzero roots satisfy \(u_\pm=\pm\sqrt{K_\beta\delta}+O_\beta(\delta)\) for positive \(\delta\); there are no such small nonzero real roots for negative \(\delta\). The two roots are interchanged by \(G\), hence form one prime-two orbit. The return multiplier is \(1-4L_\beta\delta+O_\beta(\delta^{3/2})\), in \((-1,1)\) for small positive \(\delta\). This proves the local uniqueness and supercritical attraction.

At \(\delta=0\), \(G^{\circ2}(p+u)-p=u-2C_\beta u^3+O(u^4)\). The map is attracting from both sides in a small neighborhood and its even-index deviations obey \((u_{2n+2})^{-2}-(u_{2n})^{-2}\to4C_\beta\). Telescoping yields \(n u_{2n}^2\to1/(4C_\beta)\), and for the original iteration index \(N\) both parities satisfy
\[
\lim_{N\to\infty}N\,[G^{\circ N}(x_0)-p]^2=\frac{1}{2C_\beta}
\]
for each sufficiently close \(x_0\ne p\).

**4. Large-exponent transition.** Put \(u=1/\beta\). Expansion of the exact radical gives \(p_\beta=2u-6u^2+O(u^3)\); hence \(\log\rho_\beta=2-2u+O(u^2)\) and \(\rho_\beta=e^2(1-2u+O(u^2))\). The maximum of \(h_\beta\) occurs at the positive root of \(\beta x^2+(\beta+1)x-1=0\), which equals \(u+O(u^2)\); consequently \(\max h_\beta\sim1/(e\beta)\). Thus \(\rho_{\max}(\beta)\sim e\beta\) and
\[
\frac{\rho_\beta}{\rho_{\max}(\beta)}\sim\frac e\beta.
\]
The exact formulae above give \(L_\beta\to1\), \(p_\beta^2 C_\beta\to2/3\), \(\beta p_\beta\to2\), and therefore \(\beta^2K_\beta\to6\). The rescaled map
\[
H_{\rho,\beta}(t)=\beta G_{\rho,\beta}(t/\beta)
=\frac{\rho t(1-t/\beta)^\beta}{1+t/\beta}
\]
converges in \(C^3\) on any fixed compact interval of nonnegative \(t\) to the Ricker map \(R_\rho(t)=\rho t e^{-t}\). Its first flip occurs at \((\rho,t)=(e^2,2)\) with cubic normal-form coefficient \(1/6\), agreeing with the limit \(\beta^2K_\beta\to6\). These last limits are taken by fixing \(\beta\), performing the local flip expansion, and then letting \(\beta\to\infty\); no uniform double-parameter error bound is asserted.

## Verification
A standalone Python standard-library checker (`CHECK.py`) evaluates the exact algebraic derivative formula against independent logarithmic derivatives at several integer exponents, computes the critical parameter and the admissible map maximum, and solves the nearby prime-two equations by high-precision decimal bisection on both sides of the moving fixed point. It compares the observed amplitude and return multiplier with their derived asymptotic coefficients and tests the large-exponent ratios. The checker is finite diagnostic corroboration; the analytic proof above establishes the quantifiers for all real \(\beta\ge2\).

## Relationship to prior work
Renu, Ashish and Chugh (2024) introduced and explored this exact family, establishing fixed-point properties and reporting graphical first-flip thresholds around \(4.95\) for \(\beta=2\) and \(5.35\) for \(\beta=3\), as well as longer numerical period-doubling sequences. The first two exact thresholds here are \(\rho_2\approx4.950746157860388\) and \(\rho_3\approx5.360967922884919\). The present theorem addresses the all-exponent first-flip branch, the signed cubic coefficient, sharp critical relaxation, and the singular large-exponent relative-width law. The \(\beta=1\) predecessor of Kumar et al. (2022) and its separately studied second flip are different regimes. Ricker-map local flip behavior and general flip normal-form methods are classical; novelty is not claimed for either abstract technique.

## Limitations
The theorem does not classify cycles remote from the first flip, global attraction basins, parameter regimes outside the interval self-map range, ergodic entropy, or cryptographic behavior. Although the original analysis also uses superior-iteration terminology, the theorem concerns the explicitly stated ordinary compositional dynamics. The source priority comparison includes the primary open-access article, its predecessor's accessible HTML description, and indexed related findings, but unindexed equivalent work may exist. No independent mathematical audit has been performed.

## References
1. Renu, Ashish, and Renu Chugh, *Discrete superior dynamics of a generalized chaotic system*, Arabian Journal of Mathematics 13 (2024), 369–387, published 2024-07-01, https://doi.org/10.1007/s40065-024-00464-1 (open-access full text https://link.springer.com/article/10.1007/s40065-024-00464-1).
2. Amit Kumar et al., *Dynamical properties of a novel one dimensional chaotic map*, Mathematical Biosciences and Engineering 19 (2022), 2489–2505, https://doi.org/10.3934/mbe.2022115.
3. Published mathematical records on the second flip of the rational \(\beta=1\) map and a separate Ricker-competition flip: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-second-flip-boundary-and-local-attracting-four-cycle-in-a--c832b5af1161 ; https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-composition-controlled-flip-criticality-on-a-neutral-ricker-comp--2a5a09a48e5b.
