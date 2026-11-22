# Sharp axial numerical-range gaps for diagonally split coordinate flips on complex \(\ell_p^2\)

## Finding
For \(1<p<\infty\), let \(X=\ell_p^2(\mathbb C)\) and
\[
T_\delta=\begin{pmatrix}\delta&1\\1&-\delta\end{pmatrix},\qquad\delta\in\mathbb R.
\]
Write \(W_p(T_\delta)\) for its spatial numerical range, and define its *top height*, *imaginary-axis height*, and *axial gap* by
\[
M_p=\max_{z\in W_p(T_\delta)}\operatorname{Im}z,\qquad
m_p(\delta)=\max_{z\in W_p(T_\delta),\ \operatorname{Re}z=0}\operatorname{Im}z,
\qquad \Delta_p(\delta)=M_p-m_p(\delta).
\]
These maxima exist. The top height is independent of \(\delta\).

**Theorem (quantitative axial nonconvexity).** For \(p=2\), both heights and the gap are zero. For every fixed \(1<p<\infty\) with \(p\ne2\), let \(\tau_p\in(0,1)\) be the unique solution of
\[
1-(p-1)\bigl(\tau_p^{p-2}+\tau_p^p\bigr)+\tau_p^{2p-2}=0.
\]
Then
\[
M_p=\frac{|\tau_p-\tau_p^{p-1}|}{1+\tau_p^p},\qquad
\Delta_p(\delta)
=\frac{M_p}{2}\left(\frac{1-\tau_p^p}{\tau_p+\tau_p^{p-1}}\right)^2\delta^2+O_p(\delta^4)
\quad(\delta\to0).
\]
The coefficient is strictly positive. For \(\delta\ne0\) one has \(0<m_p(\delta)<M_p\), and the spatial numerical range is nonconvex. Its strongly split imaginary-axis height satisfies
\[
m_p(\delta)\sim\frac{|p-2|}{2p|\delta|}\qquad(|\delta|\to\infty).
\]

**Exact quartic specialization.** For the non-Hilbert quartic plane, every real \(\delta\) obeys
\[
\boxed{M_4=\frac1{2\sqrt2},\qquad
m_4(\delta)=\frac{1}{2\sqrt{2(1+2\delta^2)}},\qquad
\Delta_4(\delta)=\frac1{2\sqrt2}\left(1-\frac1{\sqrt{1+2\delta^2}}\right).}
\]
Thus the sharp small-split gap is \(\delta^2/(2\sqrt2)+O(\delta^4)\); this exact formula interpolates to the large-split regime without a change of branch. The maximizers for \(m_4(\delta)\) are explicitly given below. The ordinary nonconvexity conclusion for this matrix class is previously known; the quantitative gap formula and its two asymptotic laws are the focus here.

## Assumptions and scope
The scalar field is \(\mathbb C\), with the canonical complex \(\ell_p\) norm, \(1<p<\infty\). For a unit vector \(x=(x_1,x_2)\), the uniquely norming functional is \(J_p(x)=(\overline{x_j}|x_j|^{p-2})_{j=1}^2\), paired with \(T_\delta x\) by coordinate summation. Thus
\[
W_p(T_\delta)=\{J_p(x)(T_\delta x):\|x\|_p=1\}.
\]
The axis slice is nonempty (it includes zero, from vectors with equal coordinate moduli and phase difference \(\pi/2\)). The term \(O_p(\delta^4)\) has constants for each fixed exponent \(p\ne2\), not uniformly as \(p\to2\) or toward the endpoints. All exact statements are for every \(\delta\in\mathbb R\); the asymptotic statements specify their respective limits.

## Proof
**1. Elliptic orbit formula.** Multiply a unit vector by a global phase and write \(x=(a,at e^{i\theta})\), with \(a=(1+t^p)^{-1/p}\), \(t>0\), \(\theta\in[-\pi,\pi]\); the omitted zero-coordinate cases are its continuous endpoint limits. Direct evaluation gives
\[
z_{p,\delta}(t,\theta)
=\delta H_p(t)+C_p(t)\cos\theta+i S_p(t)\sin\theta,
\]
where
\[
H_p(t)=\frac{1-t^p}{1+t^p},\quad
C_p(t)=\frac{t+t^{p-1}}{1+t^p}>0,\quad
S_p(t)=\frac{t-t^{p-1}}{1+t^p},\quad B_p(t)=|S_p(t)|.
\]
Under \(t\mapsto1/t\), \(B_p\) and \(C_p\) stay fixed while \(H_p\) changes sign. Hence every positive height is attained for some \(0<t\le1\). For \(p=2\) the imaginary part vanishes identically.

**2. Unique maximum height and its witnesses.** Assume \(p\ne2\). On \(0<t<1\), \(B_p\) vanishes at both endpoints and is positive inside. Differentiation shows its derivative is \(\operatorname{sgn}(p-2)D_p(t)/(1+t^p)^2\), where
\[
D_p(t)=1-(p-1)(t^{p-2}+t^p)+t^{2p-2},\qquad
D_p'(t)=(p-1)t^{p-3}\bigl(2t^p-(p-2)-pt^2\bigr).
\]
For \(p>2\), the bracket is negative on \((0,1)\) because \(t^p<t^2\); also \(D_p(0+)=1\), \(D_p(1)=4-2p<0\). For \(1<p<2\), the bracket is positive because \(t^p>t^2\), and \(D_p(0+)=-\infty\), \(D_p(1)=4-2p>0\). Thus \(D_p\) has exactly one interior zero \(\tau_p\), a nondegenerate maximum of \(B_p\). The only maximizing modulus ratios are \(\tau_p\) and \(1/\tau_p\), with phase \(\cos\theta=0\) and sign of \(\sin\theta\) chosen for positive imaginary part. Their real parts are
\[
\pm\delta H_p(\tau_p),\qquad H_p(\tau_p)>0.
\]
For \(\delta\ne0\), their imaginary midpoint \(iM_p\) is not in the range: reaching height \(M_p\) forces one of the two nonzero real parts. This is a direct nonconvexity witness, compatible with the earlier qualitative theorem.

**3. Exact axis reduction and the small-split law.** The real-axis constraint reads \(\cos\theta=-\delta H_p(t)/C_p(t)\). It is feasible exactly when \(|\delta H_p(t)/C_p(t)|\le1\); maximizing the positive imaginary part reduces to
\[
m_p(\delta)=\max_{\substack{0<t<\infty\\|\delta H_p(t)|\le C_p(t)}}
B_p(t)\sqrt{1-\delta^2\left(\frac{H_p(t)}{C_p(t)}\right)^2}.
\]
The formula also covers \(\delta=0\) and shows positivity for finite \(\delta\), by choosing \(t\ne1\) sufficiently close to one. With \(r_p=H_p/C_p\), the two strict, nondegenerate maximizers of \(B_p\) at \(\delta=0\) persist under the smooth even perturbation for small \(\delta\), with ratio displacement \(O_p(\delta^2)\). Outside their neighborhoods the unperturbed objective has a fixed strict deficit, so no other maxima intervene. On either branch,
\[
m_p(\delta)
=M_p-\frac{M_p}{2}r_p(\tau_p)^2\delta^2+O_p(\delta^4).
\]
Reciprocal symmetry gives identical branch heights. This proves the displayed coefficient. Since \(r_p(\tau_p)>0\), it is strictly positive. Compactness and the missing top midpoint give \(m_p(\delta)<M_p\) for every nonzero split.

**4. Strong diagonal splitting.** Feasibility \(|\delta r_p(t)|\le1\) forces \(t\to1\) uniformly as \(|\delta|\to\infty\): the continuous ratio \(r_p(t)=(1-t^p)/(t+t^{p-1})\) vanishes only at one and diverges in absolute value at zero/infinity. With \(h=t-1\) one has
\[
r_p(1+h)=-\frac p2h+O_p(h^2),\qquad
B_p(1+h)=\frac{|p-2|}{2}|h|+O_p(h^2).
\]
Set \(s=p|\delta|h/2\). Feasibility restricts \(|s|\le1+O_p(|\delta|^{-1})\), and uniform expansion of the squared objective around this interval shows that its leading rescaled maximization is
\[
\frac{|p-2|}{p|\delta|}\max_{|s|\le1}|s|\sqrt{1-s^2}
=\frac{|p-2|}{2p|\delta|}.
\]
Choosing \(|s|=1/\sqrt2\) supplies the matching lower bound, completing the asymptotic.

**5. Exact quartic optimization and all extremizers.** At \(p=4\) set \(k=(1-t^2)/(1+t^2)\in[-1,1]\) and \(u=k^2\). The formula becomes
\[
H_4=\frac{2k}{1+k^2},\qquad C_4=\frac{\sqrt{1-k^2}}{1+k^2},\qquad S_4=\frac{k\sqrt{1-k^2}}{1+k^2}.
\]
The unrestricted imaginary-height square is \(u(1-u)/(1+u)^2\), maximized uniquely at \(u=1/3\) with value \(1/8\). The exact imaginary-axis constraint gives
\[
\cos\theta=-\frac{2\delta k}{\sqrt{1-k^2}},\qquad
0\le u\le\frac1{1+4\delta^2},\qquad
(\operatorname{Im}z)^2\le\frac{u[1-(1+4\delta^2)u]}{(1+u)^2}.
\]
Every feasible \(u\) realizes equality with an appropriate phase. Put \(a_\delta=1+4\delta^2\). The derivative of the right-hand side is \([1-(1+2a_\delta)u]/(1+u)^3\), so its unique maximum occurs at \(u_*=1/(3+8\delta^2)\) and equals \(1/[8(1+2\delta^2)]\). This proves the exact formulas. The extremizers are the modulus ratios
\[
t_\pm=\sqrt{\frac{1\mp k_*}{1\pm k_*}},\qquad
k_*=(3+8\delta^2)^{-1/2},
\]
with \(\cos\theta=-2\delta(\pm k_*)/\sqrt{1-k_*^2}\), and the sign of \(\sin\theta\) chosen so that \(S_4(t_\pm)\sin\theta>0\). All these unit vectors attain \(i m_4(\delta)\); no other positive-axis maximizers exist, apart from global phases. Taylor expansion yields the sharp quadratic onset and the exact formula yields the entire crossover.

## Verification
The standalone `CHECK.py` (Python standard library only) independently evaluates the norming-functional orbit, reconstructs quartic top and imaginary-axis witnesses, numerically maximizes the exact quartic rational function, and tests the local/general-exponent and large-split asymptotics. Reproduce with `python3 CHECK.py` in the extracted package. It prints `AXIAL_GAP_DIAGNOSTIC_OK 2246` after 2,246 checks. These finite tests supplement, rather than replace, the analytic proof for all exponents and splits.

## Relationship to prior work
Mandal, Bhanja, Bag and Paul, arXiv:2005.01288, Theorem 2.9 (first public 2020), already prove qualitative nonconvexity for the entire trace-zero, equal-modulus off-diagonal class, including the present family with a nonzero diagonal split. Their proof uses a topmost-orbit obstruction, not an exact imaginary-axis maximum or its quadratic coefficient. Müller and Tomilov, arXiv:2606.22693v1 (2026), give the general two-dimensional ellipse-orbit framework and nonconvex examples, without the sharp axial gap here. The publicly available note *A sharp angular transition and exact area for the quartic coordinate-flip numerical range* establishes the full convex body at \(\delta=0\) (including its vertical height), but not a positive diagonal split or the complete height crossover. Another available note, *Sharp cubic asymmetry and ellipticity rigidity of triangular numerical ranges on* \(\ell_p^2\), concerns a different (upper-triangular, always convex) family and a cubic symmetry defect, not the axial nonconvexity of a two-sided flip. The new contribution is the exact positive-split quartic gap with sharp extremizers and the general-exponent sharp quadratic perturbative and large-split laws. A missed algebraically equivalent treatment in other numerical-range literature remains a residual bibliographic risk.

## Limitations
The exact closed-form crossover is proved only for exponent \(p=4\) and the specified two-sided flip with real opposite diagonal entries; a general matrix or all-exponent closed formula is not claimed. The asymptotics for general exponents are at fixed \(p\ne2\). The axial gap measures a distinguished failure of convexity, not the Euclidean Hausdorff distance from the numerical range to its convex hull. The qualitative nonconvexity is prior art. The independent scientific review of this result has not been performed.

## References
- K. Mandal, A. Bhanja, S. Bag and K. Paul, *On the numerical range of operators on some special Banach spaces*, arXiv:2005.01288v1 (first public 4 May 2020), Section 2, especially Theorem 2.9; *Journal of Convex Analysis* 29 (2022), 371–380, https://arxiv.org/abs/2005.01288.
- V. Müller and Yu. Tomilov, *Numerical and essential numerical ranges on* \(\ell_p\), arXiv:2606.22693v1 (first public 21 June 2026), Section 2, https://arxiv.org/abs/2606.22693.
- *A sharp angular transition and exact area for the quartic coordinate-flip numerical range*, publicly available 2 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-angular-transition-and-exact-area-for-the-quartic-coordi--d48a42e49afe.
- *Sharp cubic asymmetry and ellipticity rigidity of triangular numerical ranges on* \(\ell_p^2\), publicly available 18 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-cubic-asymmetry-and-ellipticity-rigidity-of-triangular-num--5f2bca0c2bfc.
