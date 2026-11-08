# Protected stability plateau for Gaussian and second-Hermite ambiguity inversion

## Finding
Let \(h_0(t)=2^{1/4}e^{-\pi t^2}\) and \(h_2(t)=2^{-1/2}(4\pi t^2-1)h_0(t)\) be the unit-normalized zeroth and second Hermite windows. Let \(s=\pi(x^2+y^2)\) be the dimensionless radial ambiguity variable, and put
\[
L(s)=1-2s+\tfrac12s^2,\qquad
F_w(s)=e^{-s}\big[(1-w)+wL(s)^2\big],\qquad
\Gamma(T)=\max_{0\le w\le1}\min_{0\le s\le T}F_w(s).
\]
Here \(w\) is the share of a fixed *squared-channel precision budget* allocated to the second-Hermite spectrogram, with the remaining share allocated to the Gaussian. The criterion is the worst-case squared gain of pointwise *linear ambiguity inversion* on the closed disk \(\pi(x^2+y^2)\le T\), not a claim about global nonlinear phase-retrieval stability.

There is a uniquely defined number \(T_*\in(8,10)\), numerically \(T_*=8.83273551863978\ldots\), which is the unique solution in \((8,10)\) of
\[
3+L(T_*)^2=4e^{T_*-4}.
\]
The exact optimum has the following regimes.

* For \(0<T<4\), \(\Gamma(T)=e^{-T}\). The Gaussian-only weight \(w=0\) is the unique optimizer except at \(T=2\); at that isolated radius all weights in \([0,\eta]\) optimize, where
\[
\eta=\min_{0<s<2}\frac{4(1-e^{s-2})}{s(4-s)(s-2)^2}
=0.74518236184\ldots.
\]
* At \(T=4\), \(\Gamma(4)=e^{-4}\), and precisely \(0\le w\le1/4\) are optimal.
* Throughout the **protected plateau** \(4<T\le T_*\), one has \(\Gamma(T)=e^{-4}\), with the **unique** optimal choice \(w=1/4\). Enlarging the ambiguity disk by more than a factor of two in \(s\) incurs *no loss whatsoever* in the optimal worst-case squared gain.
* For every \(T>T_*\), the optimizer \(w_T\in(1/4,1)\) is unique. Set \(s_+=2+\sqrt2\) and
\[
D(s)=1+2L(s)(s-2)-L(s)^2.
\]
The unique \(s_T\in(s_+,4)\) and \(w_T\in(1/4,1)\) satisfying
\[
D(s_T)=1/w_T,\qquad F_{w_T}(s_T)=F_{w_T}(T)
\]
determine the optimum exactly, with \(\Gamma(T)=F_{w_T}(s_T)=F_{w_T}(T)\). Both equalized radii are active. As \(T\to\infty\),
\[
w_T\uparrow1,\qquad 1-w_T\sim e^{s_+-T}L(T)^2,\qquad
\Gamma(T)\sim\tfrac14 T^4e^{-T}.
\]
For example, \(T=10\) gives \(w_T\approx0.3882014174\) and \(\Gamma(T)\approx0.016964744328\). The fixed Gaussian-only margin there is \(e^{-10}\approx0.00004539993\), so optimal joint inversion has over 370 times the squared worst-case gain.

## Assumptions and scope
The complex short-time Fourier transform is \(V_hf(x,y)=\int_{\mathbb R}f(t)\overline{h(t-x)}e^{-2\pi iyt}\,dt\). The centered ambiguity function is
\[
\mathcal A_h(x,y)=\int_{\mathbb R}h(t+x/2)\overline{h(t-x/2)}e^{-2\pi iyt}\,dt.
\]
Both windows have unit \(L^2(\mathbb R)\)-norm. With two transformed spectrogram-intensity channels of independent equal baseline noise, a total precision budget split as \((1-w,w)\) gives a pointwise least-squares squared multiplier \((1-w)|\mathcal A_{h_0}|^2+w|\mathcal A_{h_2}|^2\); its minimum on the disk is precisely \(\min_{0\le s\le T}F_w(s)\). The same mathematical optimization is meaningful without a stochastic noise interpretation. All claims quantify over real \(T>0\) and real \(w\in[0,1]\).

## Proof
The classical normalized Hermite ambiguity identity gives
\[
\mathcal A_{h_n}(x,y)=e^{-s/2}L_n(s),\qquad s=\pi(x^2+y^2).
\]
For orders zero and two, \(L_0(s)=1\) and \(L_2(s)=L(s)\). Direct Gaussian integration also verifies this normalization. In particular,
\[
L(s)^2-1=\tfrac14s(s-4)(s-2)^2,\qquad
F_w(s)=e^{-s}\left[1+\tfrac w4s(s-4)(s-2)^2\right]. \tag{1}
\]
For \(0<T<4\), \(T\ne2\), equation (1) implies \(F_w(T)<F_0(T)=e^{-T}\) whenever \(w>0\), while \(\min_{[0,T]}F_0=e^{-T}\). This proves the first regime and uniqueness. For \(T=2\) all \(F_w(2)=e^{-2}\); the necessary and sufficient inequalities \(F_w(s)\ge e^{-2}\) for \(0<s<2\) are exactly \(w\le4(1-e^{s-2})/[s(4-s)(s-2)^2]\), proving the stated sharp interval. The minimum defining \(\eta\) is attained in \((0,2)\), since the expression tends to infinity at both ends.

For all \(w\), differentiation yields
\[
\frac{d}{ds}F_w(s)=e^{-s}[-1+wD(s)],\qquad
D'(s)=-(s-1)(s^2-8s+14). \tag{2}
\]
At the exceptional weight \(w=1/4\), an exact factorization is
\[
F'_{1/4}(s)=-\frac{e^{-s}}{16}(s-4)(s^3-8s^2+12s-8). \tag{3}
\]
The cubic in (3) has exactly one real zero \(r\in(6,7)\). Indeed, its discriminant is negative (\(-1984\)); its values at \(6,7\) have opposite signs. Consequently, \(F_{1/4}\) strictly decreases on \([0,4]\), increases on \((4,r)\), and strictly decreases on \((r,\infty)\). In particular \(F_{1/4}(4)=e^{-4}\), and there is a unique \(T_*>r\) where the descending branch returns to \(e^{-4}\). Equation (1) at this crossing gives the displayed defining equation; evaluating at \(8\) and \(10\) locates \(T_*\in(8,10)\). This proves \(F_{1/4}(s)\ge e^{-4}\) for all \(0\le s\le T_*\). Since \(F_w(4)=e^{-4}\) for every \(w\), this bound is optimal whenever \(4\le T\le T_*\).

For uniqueness: at \(T=4\), equation (1) gives \(F_w(s)\ge F_{1/4}(s)\ge e^{-4}\) for \(0\le w\le1/4\), \(0\le s\le4\). For \(w>1/4\), \(F'_w(4)>0\) by (2), so a point just *left* of \(4\) has gain below \(e^{-4}\). If \(4<T\le T_*\) and \(w<1/4\), then \(F'_w(4)<0\), so a point just *right* of \(4\) has gain below \(e^{-4}\); if \(w>1/4\) the previous left-point argument applies. Thus \(w=1/4\) is uniquely optimal for \(T>4\) throughout the plateau.

It remains to classify \(T>T_*\). Put \(s_+=2+\sqrt2\), the larger zero of \(L\). Because \(L(4-s)=L(s)\), for every \(0\le s<2\) one has \(F_w(4-s)<F_w(s)\) unless the common bracket vanishes, so the minimum on \([0,4]\) can be located in \([2,4]\). On \([2,s_+]\), \(D(s)\le1\); on \([s_+,4]\), \(D\) is strictly increasing from \(1\) to \(4\), as follows from (2). For each \(w\in(1/4,1)\), equation \(D(s)=1/w\) therefore has exactly one root \(s_w\in(s_+,4)\), and the derivative in (2) changes there from negative to positive on \([2,4]\). Thus
\[
I(w):=\min_{0\le s\le4}F_w(s)=F_w(s_w).
\]
This is a strictly decreasing continuous function of \(w\in[1/4,1]\), with endpoint values \(I(1/4)=e^{-4}\) and \(I(1)=0\). Strictness on the interior follows from \(L(s_w)^2<1\). For \(s\ge4\), \(D(s)\) first increases to its sole maximum there at \(4+\sqrt2\), then decreases to \(-\infty\); hence for \(w>1/4\), \(F_w\) increases then decreases on \([4,\infty)\). Its minimum on \([4,T]\) is therefore at \(4\) or \(T\). As \(I(w)\le e^{-4}=F_w(4)\),
\[
\min_{0\le s\le T}F_w(s)=\min\{I(w),E_T(w)\},\quad E_T(w):=F_w(T),\quad\tfrac14\le w\le1.
\]
For \(T>4\), equation (1) shows \(E_T\) is strictly increasing in \(w\). At \(w=1/4\), \(E_T(1/4)<I(1/4)\) because \(T>T_*\); at \(w=1\), \(I(1)=0<E_T(1)\). There is exactly one crossing of the strictly decreasing \(I\) and increasing \(E_T\). This crossing is the unique maximum of their lower envelope. For \(w<1/4\), the gain cannot exceed \(E_T(w)<E_T(1/4)\), so such weights cannot improve it. The equations in the finding are exactly this unique crossing.

Finally, \(\sup_{0\le w\le1}E_T(w)=e^{-T}L(T)^2\to0\) as \(T\to\infty\). Since \(I(w)>0\) for every \(w<1\), the crossing forces \(w_T\to1\), hence \(s_T\to s_+\). The stationary envelope has the expansion \(I(w)=e^{-s_+}(1-w)+O((1-w)^2)\), while \(E_T(w_T)\sim e^{-T}L(T)^2\). Equating these and using \(L(T)^2\sim T^4/4\) gives both claimed asymptotics.

## Verification
Run `python3 CHECK.py` with Python 3. The checker verifies equation (1), both derivatives and the polynomial factorization using exact rational arithmetic. It independently integrates the actual normalized second-Hermite centered ambiguity function for five off-axis points. It locates \(T_*\), tests the protected plateau, equalized active radii, sampled competing weights and large-radius asymptotics; the reported terminal message is `ALL_SECOND_HERMITE_PLATEAU_CHECKS_PASSED`. Numerical sampling is supplementary: the proof above, not the grid, establishes optimization for all \(T\) and \(w\).

## Relationship to prior work
Alaifari and Yang (first public preprint October 7, 2024) give the Gaussian/Hermite ambiguity formula and motivate multiwindow coverage as a way to stabilize direct STFT phase retrieval. Bertolini, de Dios Pont, Pineau, Ramos and Taylor (May 19, 2026) analyze local \(L^2\)-stability for Gaussian/Hermite STFT phase retrieval but not the present weighted, diskwise linear-inversion minimax. The new analysis determines a **protected plateau**, an exact nonalgebraic exit radius, the complete optimizer structure and the fourth-power far-radius law for the particular Gaussian/second-Hermite pair. It is not implied by known coverage descriptions, individual-window stability results, or the previously studied Gaussian/first-Hermite allocation, whose Laguerre polynomial is different and lacks this plateau geometry.

## Limitations
The result addresses a two-channel **linear ambiguity-domain conditioning criterion** under a fixed squared-channel precision budget. It does not imply any finite-data, discretization, finite-noise statistical, or global nonlinear phase-retrieval stability theorem. The high-radius margin still decays exponentially, although it is polynomially better than Gaussian-only. The comparison with the published literature is not a proof of publication priority; an independently discovered equivalent optimal-design theorem could exist.

## References
1. S. Bertolini, J. de Dios Pont, B. Pineau, J. P. G. Ramos and M. A. Taylor, *\(L^2\)-Stability for STFT phase retrieval*, arXiv:2605.20527, first version May 19, 2026, https://arxiv.org/html/2605.20527v1.
2. R. Alaifari and Y. Yang, *Multi-Window Approaches for Direct and Stable STFT Phase Retrieval*, arXiv:2410.05486, first version October 7, 2024, https://arxiv.org/abs/2410.05486; subsequent SIAM J. Appl. Math. 85 (2025), 2376–2398, DOI 10.1137/24M1701332.
