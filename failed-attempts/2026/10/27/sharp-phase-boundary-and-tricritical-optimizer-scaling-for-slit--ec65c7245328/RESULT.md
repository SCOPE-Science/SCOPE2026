# Sharp phase boundary and tricritical optimizer scaling for slit-confined run-and-tumble diffusion

## Finding
Consider the exact four-direction, wall-mobile diffusivity of Pietrangeli et al. (2024), Eq. (27), in dimensionless units. Write the mean run time as \(t>0\), the rotational persistence time as \(r>0\), the tumble-decorrelation factor as \(a=1-\alpha>0\), the inverse wall-escape efficiency as \(\eta\ge1\), and the squared wall-to-bulk speed ratio as \(b=(\bar v/v_0)^2\ge0\). Define
\[
D_b(t)=\frac{rt\big[t+r+\eta bt(t+ar)\big]}{(t+r)(t+ar)(\eta t+2)},\quad L=\eta r+2,\quad \delta=(1-a)\eta r-2a.
\]
The large-run-time plateau is \(\lim_{t\to\infty}D_b(t)=rb\). The **complete finite-versus-infinite optimal-run-time phase boundary** is as follows.

When \(\delta\le0\), the threshold is \(b_c=L^{-1}\). For \(0\le b<b_c\), \(D_b\) has at least one finite global maximizer whose value strictly exceeds \(rb\); for \(b\ge b_c\), every finite \(t\) satisfies \(D_b(t)<rb\), so the global supremum \(rb\) is attained only as \(t\to\infty\). Every finite global maximizer \(t_m(b)\) diverges as \(b\uparrow b_c\). More precisely, with \(\varepsilon=b_c-b\downarrow0\),
\[
t_m(b)\sim\begin{cases}
\dfrac{-2r\delta}{L^2}\,\varepsilon^{-1}, &\delta<0,\\[5pt]
\dfrac{r\sqrt{6a}}{L}\,\varepsilon^{-1/2}, &\delta=0.
\end{cases}
\]
Thus the equality surface \(\delta=0\) is a **tricritical crossover** with optimizer exponent \(1/2\), distinct from the generic exponent \(1\).

When \(\delta>0\), set
\[
t_c=\frac{r\big(2a+\sqrt{2a(1-a)\eta r}\big)}{\delta},\quad
P(t)=Lt^2+r(a\eta r+2a+2)t+2ar^2,\quad
b_c=\frac{t_c(t_c+r)}{P(t_c)}.
\]
Then \(b_c>L^{-1}\). For \(b<b_c\), the global optimum exceeds the plateau and is attained at finite \(t\); as \(b\uparrow b_c\), all finite global maximizers tend to \(t_c\). At \(b=b_c\), the finite point \(t_c\) and the infinite-run plateau have equal global value \(rb_c\), and \(t_c\) is the **unique finite** global maximizer. For \(b>b_c\), all finite values lie strictly below \(rb\). Consequently the optimal run time has a discontinuous jump to infinity at \(b_c\).

In the source paper's discontinuous example \(a=1/2,\eta=2,r=10\), the exact formulas give \(t_c\approx4.6247529557426\) and \(\sqrt{b_c}\approx0.24025307335204\), refining its numerical transition near \(0.24\).

## Assumptions and scope
The claim is about the exact rational transport coefficient displayed above, corresponding to the four-direction slit model with one particle, run-time \(t>0\), rotational time \(r>0\), \(a=1-\alpha\in(0,2]\) (equivalently \(-1\le\alpha<1\)), \(\eta\ge1\), and wall speed ratio \(\sqrt b\ge0\). All denominators are positive on this domain. Physical wall speeds up to the bulk speed are encompassed; the critical ratios satisfy \(b_c<1\). The perfect-persistence singular endpoint \(a=0\), zero rotational time, and stochastic continuous-orientation model are not claimed. An "infinite optimum" means a supremum in the extended parameter \(t\in(0,\infty]\), not a finite attainable maximum. If multiple finite maximizers occur subcritically, the stated convergence and asymptotic law apply to **each** choice of global maximizer.

## Proof
Put
\[
P(t)=Lt^2+r(a\eta r+2a+2)t+2ar^2,\qquad h(t)=\frac{t(t+r)}{P(t)}.
\]
Direct exact algebra yields the decisive plateau comparison
\[
D_b(t)-rb=\frac{rP(t)}{(t+r)(t+ar)(\eta t+2)}\big(h(t)-b\big).
\]
The prefactor is strictly positive, \(h(0+)=0\), and \(h(\infty)=L^{-1}\). The derivative simplifies to
\[
h'(t)=\frac{r[-\delta t^2+4ar\,t+2ar^2]}{P(t)^2}.
\]
If \(\delta\le0\), the derivative is positive everywhere, and \(h(t)<L^{-1}\) at every finite \(t\). Therefore at and above \(b_c=L^{-1}\) no finite value reaches the plateau. If \(b<b_c\), some finite \(t\) satisfies \(h(t)>b\), yielding \(D_b(t)>rb\); continuity and the endpoint limits \(D_b(0+)=0\) and \(D_b(\infty)=rb\) force an interior maximum. As \(b\uparrow b_c\), finite maximizing points cannot have a bounded subsequence: otherwise a limit point would attain at least \(rb_c\), contradicting the strict inequality at \(b=b_c\). They also cannot tend to zero because \(D_b(0+)=0\) uniformly near \(b_c\). Thus all maximizing run times diverge.

If \(\delta>0\), the derivative numerator is a concave quadratic, positive at zero and negative at infinity. Its unique positive zero is precisely \(t_c\). Hence \(h\) rises to its unique finite maximum \(b_c=h(t_c)\) and then decreases to \(L^{-1}<b_c\). The plateau comparison gives all three optimality cases. To prove the left-limit statement for the jump, take any sequence \(b\uparrow b_c\) with finite global maximizing \(t_m(b)\). For \(b\) sufficiently close to \(b_c\), \(h(t)>b\) is possible only in a fixed compact neighborhood of \(t_c\); any maximizing point must satisfy that inequality since the optimal value exceeds \(rb\). Every limit point therefore maximizes \(h\), and uniqueness forces \(t_m(b)\to t_c\). At equality \(h=b_c\) is possible only at \(t_c\), proving finite uniqueness. Finally \(P(t)-t(t+r)\) has strictly positive coefficients for \(t>0\), so \(h(t)<1\) and \(b_c<1\).

For the continuous critical asymptotics put \(z=1/t\), \(\varepsilon=L^{-1}-b\), \(K=a\eta r+2a+2\), and calculate
\[
\frac{D_b(1/z)}r-b=\frac{Az+Bz^2+Cz^3}{(1+rz)(1+arz)(\eta+2z)},
\quad A=L\varepsilon,\quad B=r(1-bK),\quad C=-2abr^2.
\]
At \(b=L^{-1}\), \(B_0=r\delta/L\) and \(C_0=-2ar^2/L<0\). At any finite interior maximizer \(z_m=1/t_m\), the derivative in \(z\) vanishes. Since \(z_m\to0\), if \(\delta<0\), the derivative equation becomes
\[
0=L\varepsilon+\frac{2r\delta}{L}z_m+O(z_m^2+\varepsilon z_m).
\]
The implicit-function theorem about \((\varepsilon,z)=(0,0)\) gives \(z_m\sim-L^2\varepsilon/(2r\delta)\), hence the stated exponent \(1\) and coefficient. When \(\delta=0\), the quadratic coefficient vanishes exactly, and the derivative equation becomes
\[
0=L\varepsilon-\frac{6ar^2}{L}z_m^2+O(\varepsilon z_m+z_m^3).
\]
Because \(z_m\to0\) and \(\varepsilon>0\), this implies \(z_m\sim L\sqrt{\varepsilon}/(r\sqrt{6a})\); a dominant-balance bound follows directly by moving the error terms to the opposite side and absorbing them for small \((\varepsilon,z_m)\). This proves the exponent \(1/2\). The \(\delta<0\) coefficient is equivalent to Appendix C's leading law after converting \(b=(\bar v/v_0)^2\); the \(\delta=0\) law and exact discontinuous branch are not supplied there.

## Verification
A standalone symbolic verifier is provided as `verification/check.py`. It checks the plateau identity, the exact derivative of \(h\), the reciprocal-time polynomial identity, the critical quadratic coefficient, and symbolic finite coexistence for the source's discontinuous parameters. It reproduces the continuous prefactor \(0.25\), tricritical prefactor \(0.43301270189222\), and discontinuous coexistence values above. The checker uses exact symbolic equalities for its algebraic assertions. These finite computations support but do not replace the global sign/compactness and limiting arguments in the proof. Run using `python verification/check.py` with SymPy installed.

## Relationship to prior work
Pietrangeli, Ybert, Cottin-Bizonne and Detcheverry (2024) derive the exact coefficient used here (their Eq. (27)), identify two optimization scenarios in Figures 6 and 7, and in Appendix C give a sufficient strict condition \(2a-\alpha\eta r>0\) for the continuous scenario, together with its conventional inverse-linear divergence. The present result gives a **necessary-and-sufficient** scenario boundary, closed-form discontinuous jump point and critical speed, and the previously untreated equality case with a different exponent. It does not rederive the underlying stochastic transport coefficient. The 2025 paper by Pietrangeli et al. on porous-medium dispersal develops a broader multimodal stochastic modeling framework, including surface sliding, but does not state this exact phase classification or the equality exponent for the 2024 four-direction slit coefficient. Distinct prior work on optimization in crowded environments concerns different random-walk/obstacle dynamics and does not supply an implication for the stated exact rational coefficient.

## Limitations
The theorem is an exact optimization result for a specified four-direction transport law, not a dynamical theorem for continuous-orientation swimmers or arbitrary porous media. It does not assert subcritical uniqueness of the finite maximizer, nor extend to \(a=0\), \(r=0\), or modified surface boundary kinetics. The applicability of parameter values to a particular microorganism and the approximation accuracy of the four-direction model require separate physical validation. Although relevant published source texts and related work were compared, an unindexed algebraic rederivation cannot be logically excluded by literature search alone; independent scientific assessment remains outstanding.

## References
- T. Pietrangeli, C. Ybert, C. Cottin-Bizonne, F. Detcheverry, *Optimal run-and-tumble in slit-like confinement*, Physical Review Research **6**, 023028 (2024), DOI: 10.1103/PhysRevResearch.6.023028; preprint arXiv:2404.07680v1, https://arxiv.org/pdf/2404.07680 (Sec. IV A 2, Figs. 6–7, Appendix C).
- T. Pietrangeli, R. Foffi, R. Stocker, C. Ybert, C. Cottin-Bizonne, F. Detcheverry, *Universal law for the dispersal of motile microorganisms in porous media*, arXiv:2503.03273v1 (2025), https://arxiv.org/pdf/2503.03273 (main text, multimodal motion and surface sliding).
- T. Bertrand, Y. Zhao, O. Bénichou, J. Tailleur, R. Voituriez, *Optimized Diffusion of Run-and-Tumble Particles in Crowded Environments*, Physical Review Letters **120**, 198103 (2018), arXiv:1711.05209, https://arxiv.org/abs/1711.05209 (different obstacle and motion dynamics).
