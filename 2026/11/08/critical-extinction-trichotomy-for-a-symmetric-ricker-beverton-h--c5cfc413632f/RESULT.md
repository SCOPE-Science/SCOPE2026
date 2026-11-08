# Critical-extinction trichotomy for a symmetric Ricker–Beverton–Holt map

## Finding
For every real \(k>0\), consider the positive-quadrant map
\[
F_k(y,z)=\left(\frac{z e^{-y}}{1+kz},\frac{y e^{-z}}{1+ky}\right).
\]
For every \(y_0,z_0>0\), its iterates converge to \((0,0)\), but their **normalized extinction profiles undergo a sharp transition at \(k=1\)**:

**Synchronizing phase, \(k>1\).** Regardless of the initial ratio,
\[
\lim_{n\to\infty}n y_n=\lim_{n\to\infty}n z_n=\frac1{k+1}.
\]

**Critical phase, \(k=1\).** There is an orbit-dependent \(w\in(0,1)\) such that
\[
\lim_{m\to\infty}(2m)y_{2m}=w,\qquad
\lim_{m\to\infty}(2m)z_{2m}=1-w,
\]
\[
\lim_{m\to\infty}(2m+1)y_{2m+1}=1-w,\qquad
\lim_{m\to\infty}(2m+1)z_{2m+1}=w.
\]
Here \(w=1/2\) exactly on the diagonal \(y_0=z_0\); otherwise \(w-1/2\) has the sign of \(y_0-z_0\). Thus there is a continuum of limiting even/odd extinction compositions, though extinction itself is global.

**Alternating-selection phase, \(0<k<1\).** If \(y_0=z_0\), the diagonal remains invariant and both normalized populations converge to \(1/(1+k)\). If \(y_0>z_0\), then
\[
\lim_{m\to\infty}(2m)y_{2m}
=\lim_{m\to\infty}(2m+1)z_{2m+1}=\frac1k,
\]
while there is a finite \(C=C(k,y_0,z_0)>0\) such that
\[
\lim_{m\to\infty}m^{1/k}z_{2m}
=\lim_{m\to\infty}m^{1/k}y_{2m+1}=C.
\]
For \(y_0<z_0\), exchange \(y,z\) throughout the preceding formulas. In particular, the minority component decays strictly faster than \(n^{-1}\), with exponent \(1/k>1\), and the dominant component alternates between species at successive times.

## Assumptions and scope
The map is the exact symmetric critical-production slice \(a=b=1\), \(p=q=k\) of the two-population Ricker–Beverton–Holt fishery model
\[
 y_{n+1}=\frac{a z_n}{1+pz_n}e^{-y_n},\qquad
 z_{n+1}=\frac{b y_n}{1+qy_n}e^{-z_n}.
\]
The product of linearized recruitment factors is \(ab=1\); the origin has multipliers \(+1\) and \(-1\). All initial coordinates and \(k\) are strictly positive. This theorem does not claim a trichotomy for unequal recruitment or harvesting coefficients, nor for nonpositive initial data. Every asymptotic limit uses the original discrete time; \(m\) counts pairs of steps.

## Proof
**1. Global extinction and two-step size.** Each coordinate of \(F_k(y,z)\) is strictly below the *other* input coordinate. Hence \(y_{n+2}<y_n\) and \(z_{n+2}<z_n\) for every positive orbit. Even subsequences converge. Continuity of \(F_k^2\), together with strict decrease of every positive coordinate under \(F_k^2\) at any nonzero nonnegative point, forces their limits to be zero; odd subsequences then tend to zero as well.

Write \(x_m=y_{2m}\), \(t_m=z_{2m}\), \(S_m=x_m+t_m\). A uniform Taylor expansion near the origin gives
\[
\begin{aligned}
 x_{m+1}&=x_m\bigl(1-2k x_m-2t_m+O_k(S_m^2)\bigr),\\
 t_{m+1}&=t_m\bigl(1-2x_m-2k t_m+O_k(S_m^2)\bigr).
\end{aligned}
\tag{1}
\]
Indeed the first iterate is \(y'=z(1-y-kz+O_k((y+z)^2))\), \(z'=y(1-z-ky+O_k((y+z)^2))\); substituting these in the second iterate yields (1), including a uniform remainder after factoring out the input coordinate. Consequently
\[
 S_{m+1}=S_m-2k(x_m^2+t_m^2)-4x_mt_m+O_k(S_m^3).
\tag{2}
\]
For all nonnegative \(x,t\), the quadratic term in (2) lies between \(c_k(x+t)^2\) and \(C_k(x+t)^2\) for positive constants \(c_k,C_k\). Since \(S_m\to0\), telescoping the increments of \(1/S_m\) gives \(S_m=\Theta_k(m^{-1})\). In particular \(\sum_m S_m=\infty\) and \(\sum_m S_m^2<\infty\). The corresponding one-step sums satisfy the same statements.

**2. Exact ratio identity.** Put \(L_n=\log(y_n/z_n)\) and \(\phi_k(u)=u-\log(1+ku)\). Direct division gives
\[
 L_{n+1}=-L_n-[\phi_k(y_n)-\phi_k(z_n)].
\tag{3}
\]
The map reverses strict coordinate order at every step: \(L_{n+1}\) has sign opposite to \(L_n\), because
\[
 \frac{d}{du}\bigl(\log u+\phi_k(u)\bigr)
 =1+\frac1{u(1+ku)}>0.
\]
Thus with \(M_n=\max(y_n,z_n)\) and \(h_n=\min(y_n,z_n)\), equation (3) yields the exact identity
\[
 |L_{n+1}|-|L_n|=\phi_k(M_n)-\phi_k(h_n),
 \qquad
 \phi'_k(u)=\frac{1-k+ku}{1+ku}.
\tag{4}
\]

**3. \(k>1\).** Once both coordinates are smaller than \((k-1)/(2k)\), the derivative in (4) is bounded above by a negative constant. Thus \(|L_n|\) eventually decreases. If its limit were positive, the identity \(|y_n-z_n|/(y_n+z_n)=\tanh(|L_n|/2)\) would give \(M_n-h_n\ge c(y_n+z_n)\) eventually. Summing (4) would then contradict \(\sum_n(y_n+z_n)=\infty\). Hence \(L_n\to0\), so \(x_m/t_m\to1\). From (2), \(S_{m+1}=S_m-(k+1)S_m^2+o(S_m^2)\). Therefore \(mS_m\to1/(k+1)\), and each even coordinate satisfies \((2m)x_m,(2m)t_m\to1/(k+1)\). The first-iterate equations imply the same limit at odd times.

**4. \(k=1\).** For every \(u>0\), \(0<\phi'_1(u)=u/(1+u)<u\). Thus (4) shows that \(|L_n|\) is strictly increasing for unequal initial coordinates, yet its total increase is bounded by \(\sum_n(y_n+z_n)^2<\infty\). It converges to a finite number, positive when the initial coordinates differ. Hence \(x_m/t_m\to R\in(0,\infty)\), where \(R=1\) only for diagonal initial data. Equation (2) simplifies to \(S_{m+1}=S_m-2S_m^2+O(S_m^3)\), giving \(mS_m\to1/2\). Put \(w=R/(1+R)\). Then \((2m)x_m\to w\), \((2m)t_m\to1-w\). Since the first iterate swaps the two coordinates up to a factor \(1+o(1)\), the claimed odd-time limits follow.

**5. \(0<k<1\).** In this range \(\phi'_k(u)\ge1-k>0\) for all \(u\ge0\). If the initial coordinates are unequal, (4) makes \(|L_n|\) strictly increasing. A finite limit would imply \(M_n-h_n\ge c(y_n+z_n)\) eventually, and its increments in (4) would sum to infinity, a contradiction. Thus \(|L_n|\to\infty\). Suppose \(y_0>z_0\). Order alternation implies \(t_m/x_m\to0\); equation (1) then gives \(x_{m+1}=x_m-2k x_m^2+o(x_m^2)\), hence \(m x_m\to1/(2k)\). It also gives
\[
 \log t_{m+1}-\log t_m=-2x_m-2k t_m+O_k(S_m^2).
\tag{5}
\]
Therefore \(\log t_m/\log m\to-1/k\), i.e. \(t_m=m^{-1/k+o(1)}\). Since \(1/k>1\), there exists \(\epsilon>0\) with \(t_m=O(m^{-1-\epsilon})\). Taking reciprocals in the first equation of (1) yields
\[
 \frac1{x_{m+1}}-\frac1{x_m}=2k+\frac{2t_m}{x_m}+O_k(S_m).
\]
Using \(x_m\asymp m^{-1}\) and the preceding estimate, one obtains
\[
 x_m=\frac1{2km}+O(m^{-1-\epsilon'}+m^{-2}\log m)
\]
for some \(\epsilon'>0\). In particular \(\sum_m|x_m-1/(2km)|<\infty\). Equation (5) now shows that
\[
\sum_{m\ge1}\left|\log\frac{t_{m+1}}{t_m}+\frac1{km}\right|<\infty.
\]
Comparison with the harmonic series implies \(m^{1/k}t_m\to C\in(0,\infty)\). The original one-step equations transfer the dominant asymptotics to \(z_{2m+1}\) and the minority asymptotics to \(y_{2m+1}\). The other ordering follows by symmetry. On the invariant diagonal the scalar recurrence is \(u_{n+1}=u_ne^{-u_n}/(1+ku_n)=u_n-(1+k)u_n^2+O_k(u_n^3)\), so \(n u_n\to1/(1+k)\). For the critical \(k=1\) family, varying the positive initial ratio produces uncountably many distinct \(w\): when \(y_0+z_0=arepsilon\downarrow0\), the summable increment bound in (4) gives \(|L_\infty-L_0|=O(arepsilon)\) uniformly on compact initial-ratio intervals. Consequently \(w\) approaches the freely chosen initial proportion, and continuity of the uniform limit supplies an interval of \(w\) values. This completes the proof.

## Verification
The supplied `check.py` implements the exact recurrence, checks the sign-reversal and increment identities of (3)–(4), compares second-order two-step Taylor expressions with computed iterates, and checks representative long-run profiles for \(k<1\), \(k=1\), and \(k>1\). Run `python3 check.py` with the Python standard library. The recorded execution passed 68 checks. These finite computations are supplementary: the proof establishes every quantified infinite-time conclusion.

## Relationship to prior work
Ouyang, Zhang and Chen introduced the two-population Ricker–Beverton–Holt combination in *Balanced harvesting of dynamical discrete Ricker & Beverton–Holt system* (first indexed online 2023-03-28), and explicitly report extinction when \(ab\le1\) and global stability conditions for coexistence. The present result treats the critical equality \(ab=1\) on the biologically natural symmetric parameter section and resolves **normalized rates, time-parity selection and a saturation threshold** that are not present in the accessible source abstract and indexed mathematical statements. Streipert and Wolkowicz's 2022 work analyzes complete global dynamics of other planar population maps using next-iterate operators, not this two-step critical normal form. The exact competition between \(2k\) self-damping and \(2\) cross-damping in (1) produces the trichotomy.

## Limitations
The paper of Ouyang, Zhang and Chen was not accessible in full through the available lawful routes: a full authorized copy could not be obtained by lawful access routes. This creates a **material residual publication-priority risk**: an unstated equivalent normalization result in the full article cannot be ruled out. The assessed originality is therefore provisional, not independently certified. The theorem is restricted to positive starts and the symmetric critical-production slice. The exceptional limiting parameter \(w\) is defined dynamically, not claimed to have an elementary formula. The numerical program does not prove asymptotics or uniqueness.

## References
1. M. Ouyang, Q. Zhang, Z. Chen, *Balanced harvesting of dynamical discrete Ricker & Beverton–Holt system*, Chaos, Solitons & Fractals **170** (2023), 113384. DOI: 10.1016/j.chaos.2023.113384. First indexed public date 2023-03-28; bibliographic source OpenAlex W4361294196.
2. S. H. Streipert, G. S. K. Wolkowicz, *An augmented phase plane approach for discrete planar maps: Introducing next-iterate operators*, arXiv:2210.07943, first submitted 2022-10-11. Distinct competition/map setting.
