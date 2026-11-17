# Sharp nonlinear invasion-boundary threshold for a discrete two-stage contagion map

## Finding
For the finite-round two-stage contagion map with turnover, the linear invasion boundary divides into a locally attracting and a locally repelling segment at a unique explicit probability \(p_*(\nu,\tau)\). On the attracting segment, the adopter fraction decays at the exact rate \(a_n\sim K/n\), with a universal prefactor \(K\) depending only on the model parameters. The nonlinear transition differs from its continuous-time limit for positive round lengths.

Set \(m=\nu\tau\), \(h=1-e^{-m}\), \(\kappa=1-e^{-(1+\nu)\tau}\), and \(H=1-(1+m)e^{-m}\). Define
\[
\Psi(p)=(1-p)^2-\frac{H}{h}p-\left(\frac{h}{\kappa}+\frac1{1+\nu}\right)p^2.
\]
Then \(\Psi\) has exactly one root \(p_*\in(0,1)\). Along the linear invasion boundary \(\rho=(1+\nu)m/(ph)\), the disease-free state attracts all sufficiently nearby biological states when \(p>p_*\), and for \(a_0>0\) the following sharp limit holds:
\[
\lim_{n\to\infty}n a_n=\frac{p^2h}{\kappa^2[-\Psi(p)]}.
\]
For \(0<p<p_*\) the same state is Lyapunov unstable relative to biological states. For fixed \(\nu>0\), \(p_*\to1/2\) as \(\tau\downarrow0\).

## Assumptions and scope
The dimensionless parameters are \(\nu=\mu/\gamma>0\) (turnover), \(\rho=\beta/\gamma>0\) (contact), \(\tau>0\) (round length in units of \(1/\gamma\)), and \(p\in(0,1]\). Let \(s_0,s_1,a,r\ge0\) be naive, primed, adopter, and recovered fractions, with \(s_0+s_1+a+r=1\). Define
\[
 C=\frac{\rho\kappa}{1+\nu},\qquad Q(a)=\frac{Ca}{Ca+m}\,[1-e^{-(Ca+m)}].
\]
The published deterministic large-population map can be expressed in coordinates \((s_1,a,r)\), with \(s_0=1-s_1-a-r\), as
\[
\begin{aligned}
 s_1'&=(1-p)Q(a)s_0+e^{-m-Ca}s_1,\\
 a'&=pQ(a)s_0+Q(a)s_1+e^{-(1+\nu)\tau}a,\\
 r'&=e^{-m}r+\frac{\kappa}{1+\nu}a.
\end{aligned}
\]
These formulas preserve the biological simplex and the disease-free state \((s_1,a,r)=(0,0,0)\). We restrict the main theorem to the exact linear invasion boundary \(\rho=(1+\nu)m/(ph)\), where one eigenvalue is one and the other two are \(e^{-m}\).

## Proof
**1. Critical linearization and stable directions.** At the stated boundary, differentiation gives \(q_1=Q'(0)=\kappa/p\). A right center eigenvector normalized to its adopter component one is \((A,1,R)\), where
\[
 A=\frac{(1-p)\kappa}{ph},\qquad R=\frac{\kappa}{(1+\nu)h}.
\]
The remaining multipliers equal \(e^{-m}\in(0,1)\). Standard local center-manifold and stable-foliation theorems for smooth finite-dimensional maps apply. In particular the center manifold has \(s_1=Aa+O(a^2)\), \(r=Ra+O(a^2)\); for \(0<p<1\) and small \(a>0\) this manifold lies inside the simplex. The endpoint \(p=1\) has \(A=0\) and the physical one-stage invariant slice \(s_1=0\).

**2. Exact quadratic coefficient.** Expansion of the exponential risk gives
\[
Q(a)=\frac{\kappa}{p}a-\frac{\kappa^2H}{p^2h^2}a^2+O(a^3).
\]
Using \(s_0=1-s_1-a-r\) in the adopter update, the restriction to the center manifold becomes
\[
a'=a+c_2a^2+O(a^3),\qquad c_2=\frac{\kappa^2}{p^2h}\Psi(p).
\]
Only the first derivatives \(A\) and \(R\) of the center graph are needed for this quadratic coefficient. In particular it is independent of the choice of local center manifold.

**3. Exactly one transition.** Since \(H>0\), \(h>0\), and \(\kappa>0\), one has \(\Psi(0)=1\), \(\Psi(1)=-H/h-h/\kappa-1/(1+\nu)<0\), and
\[
\Psi'(p)=-2(1-p)-\frac{H}{h}-2p\left(\frac{h}{\kappa}+\frac1{1+\nu}\right)<0\qquad(0\le p\le1).
\]
Thus its unique root lies strictly between zero and one.

**4. Local dynamics and sharp amplitude.** When \(c_2<0\), the positive half of the center direction is attracting; the two transverse multipliers are strictly contracting. Center-manifold stability reduction gives local asymptotic stability relative to the invariant biological simplex. For positive adopter seeds, no finite iterate reaches \(a=0\), because the adopter update contains its positive linear survival term. The attracting center recursion and exponential transverse tracking give \(a_{n+1}=a_n+c_2a_n^2+o(a_n^2)\). Consequently \(a_n\to0\) and
\[
 \frac1{a_{n+1}}-\frac1{a_n}=-c_2+o(1),
\]
so Cesàro summation yields \(n a_n\to-1/c_2\), as claimed. For \(c_2>0\), the small positive center branch moves away from zero; this proves Lyapunov instability within the biological simplex.

**5. Continuous-round comparison.** For fixed \(\nu>0\), as \(\tau\downarrow0\), \(H/h\to0\) and \(h/\kappa\to\nu/(1+\nu)\), so \(\Psi(p)\to1-2p\) uniformly on \([0,1]\). Uniqueness of the root then gives \(p_*\to1/2\).

## Verification
The self-contained Python checker \(`verify_cm.py`\) evaluates the two independent formulas for the quadratic coefficient and compares them with finite differences computed directly from the original map. It also checks monotonicity and uniqueness of the nonlinear transition numerically at several nondegenerate parameter pairs. These are finite corroborations; the proof of the theorem for arbitrary positive parameters is analytical.

## Relationship to prior work
Muñoz, Nuño, and Meacci derive the synchronous-round map and determine its *linear* invasion threshold, as well as endemic and Neimark–Sacker phenomena. Their Proposition 4 yields the one-dimensional multiplier used here, but does not calculate the quadratic center reduction or the sharp critical decay. Katriel's earlier continuous-time two-stage contagion analysis establishes analogous forward/backward transition phenomena in the ordinary differential equation, not the explicit finite-round probability threshold \(p_*(\nu,\tau)\) or the round-count decay coefficient. The finite-round result recovers the continuous-time boundary \(p=1/2\) only in the vanishing-round limit. Generic center-manifold theory supplies the tool, but not the model-specific transition equation or its parameter dependence.

## Limitations
The theorem is local and deterministic. It makes no assertion about a global basin, the measure of finite-population extinction times, the nonlinear character exactly at \(p=p_*\), or the dynamics off the linear invasion boundary. The strong-stable invariant set with adopter coordinate identically zero is excluded from the positive-seed asymptotic. The result has undergone only self-review; independent audit and definitive historical-priority assessment are not available.

## References
1. F. J. Muñoz, J. C. Nuño, L. Meacci, *From elementary processes to chaos: a discrete-time two-stage contagion model and its continuous limit* (2026), arXiv:2611.08353v1, first public November 5, 2026. https://arxiv.org/abs/2611.08353
2. G. Katriel, *The dynamics of two-stage contagion* (2018 preprint; 2019 publication), arXiv:1812.08867. https://arxiv.org/abs/1812.08867
3. Y. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, third edition, Springer (2004), standard center-manifold theory for maps.
