# Critical fractional-power collapse of sharp spherical Fourier-extension stability

## Finding
Fix an integer \(d\ge3\), write \(\nu=d/2-1\), \(q_c=2d/(d-1)\), and, for \(q>q_c\), define the spherical Fourier–Bessel moments
\[
I_k(q)=\int_0^\infty |J_{\nu+k}(r)|^q r^{d-1-\nu q}\,dr,\qquad k=0,1,\ldots.
\]
Let \(\Gamma_{d,q}\) be the best quadratic stability coefficient in the radial–angular mixed Fourier extension inequality, with **unnormalized surface measure**, Fourier phase \(e^{-ix\cdot\omega}\), and the norms specified below. The following improper integral exists as a finite, strictly positive number:
\[
\Delta_d=\lim_{R\to\infty}\int_0^R
r^{d-1-\nu q_c}\Bigl(|J_\nu(r)|^{q_c}-|J_{\nu+1}(r)|^{q_c}\Bigr)\,dr>0.
\]
Put
\[
m(s)=\frac{\Gamma((s+1)/2)}{\sqrt\pi\,\Gamma((s+2)/2)},
\qquad B_d=\frac{2}{d-1}\left(\frac2\pi\right)^{q_c/2}m(q_c).
\]
Then the **exact sharp boundary asymptotics**, as \(q\downarrow q_c\), are
\[
\boxed{\displaystyle
\lim_{q\downarrow q_c}\frac{\Gamma_{d,q}}{(q-q_c)^{1/d}}
=(2\pi)^d\frac{d-1}{d}\,B_d^{-1/d}\Delta_d>0.}
\]
In addition, if \(C_{d,q}\) denotes the sharp mixed-extension norm, its squared value diverges as
\[
C_{d,q}^2\sim(2\pi)^d B_d^{(d-1)/d}(q-q_c)^{-(d-1)/d},
\]
while the **relative** optimal stability gap has the dimension-independent linear order
\[
\frac{\Gamma_{d,q}}{C_{d,q}^2}\sim
\frac{d-1}{d}\frac{\Delta_d}{B_d}(q-q_c).
\]
The first-harmonic direction remains the unique sharp nonconstant degree for every \(q>q_c\), as established in the motivating source. The fractional-power and relative-linear limits above are the assertions here.

## Assumptions and scope
Use \(\mathbb S^{d-1}\subset\mathbb R^d\) with the usual *unnormalized* area measure \(\sigma\). For \(f\in L^2(\mathbb S^{d-1},d\sigma)\) define
\[
\widehat{f\sigma}(x)=\int_{\mathbb S^{d-1}}e^{-ix\cdot\omega}f(\omega)\,d\sigma(\omega),
\qquad
\|F\|_{L^q_{\mathrm{rad}}L^2_{\mathrm{ang}}}
=\left(\int_0^\infty\left[\int_{\mathbb S^{d-1}}|F(r\theta)|^2\,d\sigma(\theta)\right]^{q/2}r^{d-1}dr\right)^{1/q}.
\]
The sharp norm \(C_{d,q}\) is the smallest constant satisfying \(\|\widehat{f\sigma}\|\le C_{d,q}\|f\|_2\), and \(\Gamma_{d,q}\) is the largest nonnegative constant in
\[
C_{d,q}^2\|f\|_2^2-\|\widehat{f\sigma}\|^2
\ge \Gamma_{d,q}\|f-P_0f\|_2^2,
\]
where \(P_0\) is the orthogonal projection onto the constant spherical harmonics. For \(d\ge3\) and \(q>q_c\), Xu's modal-ordering and stability theorems give
\[
C_{d,q}^2=(2\pi)^d I_0(q)^{2/q},\qquad
\Gamma_{d,q}=(2\pi)^d\bigl(I_0(q)^{2/q}-I_1(q)^{2/q}\bigr).
\]
The critical exponent \(q=q_c\) is excluded from the extension inequality: each individual \(I_k(q_c)\) diverges. The critical **difference** is an ordinary conditionally convergent improper integral, not the difference of two separately assigned divergent integrals. All limits fix the dimension \(d\); no dimension-uniform remainder is asserted.

## Proof
**1. Common pole of each modal moment.** Let \(\beta=(d-1)/2\), \(\phi_\nu=\pi\nu/2+\pi/4\), and write \(q=q_c+\delta\) with \(\delta>0\). For either fixed \(k=0\) or \(k=1\), the classical fixed-order Hankel expansion yields, uniformly for \(q\) in a small compact interval above \(q_c\),
\[
\begin{aligned}
r^{d-1-\nu q}|J_{\nu+k}(r)|^q
={}&\left(\frac2\pi\right)^{q/2}r^{-1-\beta\delta}
\left|\cos\left(r-\phi_\nu-\frac{k\pi}{2}\right)\right|^q
+O_d(r^{-2-\beta\delta}),\quad r\ge1.
\end{aligned}
\]
Uniformity of the error follows from the usual \(O_d(r^{-1})\) relative oscillatory remainder and the locally uniform Lipschitz bound for \(z\mapsto |z|^q\), even at cosine zeros. The \(\pi\)-periodic leading profile has mean
\[
m(q)=\frac1\pi\int_0^\pi|\cos u|^qdu.
\]
Its mean-zero part has a uniformly bounded periodic primitive, so integrating against the decreasing weight \(r^{-1-\beta\delta}\) gives a uniformly \(O_d(1)\) contribution by integration by parts. The region \(0<r<1\) is uniformly integrable by the ascending Bessel series. Consequently, for each \(k\in\{0,1\}\),
\[
I_k(q)=\frac{(2/\pi)^{q/2}m(q)}{\beta\delta}+O_d(1)
=\frac{B_d}{\delta}+O_d(1).
\]
In particular, \(\delta I_k(q)\to B_d\), with the same positive residue for both modes.

**2. Finite positive difference across the critical pole.** The phase shift by \(\pi/2\) gives the function
\[
g_q(r)=|\cos(r-\phi_\nu)|^q-|\sin(r-\phi_\nu)|^q,
\]
which is \(\pi\)-periodic and has zero mean for every \(q>0\). Subtracting the two modal Hankel expansions gives the uniform tail representation
\[
F_q(r):=r^{d-1-\nu q}(|J_\nu(r)|^q-|J_{\nu+1}(r)|^q)
=\left(\frac2\pi\right)^{q/2}r^{-1-\beta\delta}g_q(r)+O_d(r^{-2-\beta\delta}).
\]
A uniformly bounded primitive of \(g_q\) and integration by parts give, uniformly for small \(\delta\ge0\),
\[
\left|\int_R^\infty F_q(r)dr\right|\le\frac{K_d}{R},\qquad R\ge1.
\]
The integrals of \(F_q\) on any fixed finite interval depend continuously on \(q\). Uniform tails therefore show both conditional convergence at \(q=q_c\) and
\[
\lim_{q\downarrow q_c}(I_0(q)-I_1(q))=\Delta_d.
\]
Strict positivity follows from the *positive-cell* statement in Xu, arXiv:2610.19648, Theorem 3.9: for every \(s>2\), \(\nu\ge0\), and each cell bounded by consecutive zeros of \(J_{\nu+1}\), the integral of \(r^{2\nu+1}(|r^{-\nu}J_\nu|^s-|r^{-\nu}J_{\nu+1}|^s)\) is strictly positive. This statement is applicable at \(s=q_c>2\). In that source the critical step is the flux identity (3.54), followed by the reflected-Wronskian inequalities (3.59)–(3.62), which establish positivity *cell by cell* without assuming global integrability of either moment. Since the present tail estimate proves convergence of the sum of these strictly positive cell contributions, \(\Delta_d\) is at least the first positive cell contribution and is strictly positive.

**3. Fractional-power sharp stability.** The elementary identity
\[
a^t-b^t=t(a-b)\int_0^1\bigl(b+\lambda(a-b)\bigr)^{t-1}d\lambda\qquad(a,b>0,t>0)
\]
is used with \(a=I_0(q)\), \(b=I_1(q)\), \(t=2/q\). Step 1 gives \(a,b\sim B_d/\delta\), step 2 gives \(a-b\to\Delta_d>0\), and \(2/q\to(d-1)/d\). Thus
\[
I_0(q)^{2/q}-I_1(q)^{2/q}
\sim\frac{d-1}{d}\,\Delta_d B_d^{-1/d}\delta^{1/d}.
\]
Substituting Xu's *sharp* spectral formula yields the stated limit for \(\Gamma_{d,q}\). The corresponding expression for \(C_{d,q}^2\) comes from step 1. Dividing the two proves the relative linear law. This completes the proof.

## Verification
The proof uses a fixed-order Hankel expansion with an error uniform in the exponent on compact sets, the zero-mean cancellation between cosine and sine profiles, and the positive-cell theorem cited above. The supplementary script `numeric_probe.py` computes several finite radial cell integrals at Bessel zeros for \(d=3,4,5\) and verifies their strict growth; these are consistency checks, not proofs of either conditional convergence or global positivity. All symbolic normalizations in the proof are explicit; no numerical fit is used to infer the exponent.

## Relationship to prior work
Xu, *Sharp radial--angular mixed norm Fourier extension and global stability on spheres* (arXiv:2610.19648, first posted 2026-10-14), establishes the exact mode ordering for \(q>q_c\), the optimal stability formula, and the stronger positive-cell lemma used here. Xu's source does **not** state the sharp \(q\downarrow q_c\) law, the critical conditionally convergent difference, its explicit coefficient, or the two different endpoint exponents for absolute and relative stability. The new argument needs uniform cancellation *at* the singular exponent and a singular-power expansion; it is not a change of notation in the finite-exponent formula.

Carneiro, Oliveira e Silva and Sousa (arXiv:1710.10365; *Advances in Mathematics* 341 (2019)) developed the sharp mixed norm spherical restriction framework and earlier modal estimates. The related 2024 work of Carneiro, Negro and Oliveira e Silva studies **ordinary weighted adjoint extension \(L^4(\mathbb R^d)\)**, not this radial–angular singular endpoint. The earlier two-dimensional circular critical moment-gap computation uses \(q_c=4\) and integer-order Bessel functions; it does not imply the \(d\ge3\) fractional-power coefficient or conditional integral here.

## Limitations
The constant \(\Delta_d\) is given by a convergent Bessel-difference integral, not a claimed closed gamma-formula. Directly subtracting the two divergent critical moments is invalid. The theorem concerns fixed integer \(d\ge3\), not \(d=2\), and provides a leading asymptotic rather than explicit finite-exponent error bounds or a dimension-uniform estimate. It relies on Xu's established positive-cell Bessel comparison and mode-ordering theorems; it does not independently re-prove those original theorems. No independent external audit has been performed.

## References
1. Zewei Xu, *Sharp radial--angular mixed norm Fourier extension and global stability on spheres*, arXiv:2610.19648v1 (first public release 2026-10-14), https://arxiv.org/abs/2610.19648. Theorems 1.2, 1.3, and 3.9; equations (3.54), (3.59)–(3.62), and (4.4).
2. E. Carneiro, D. Oliveira e Silva, M. Sousa, *Sharp mixed norm spherical restriction*, arXiv:1710.10365v3, *Advances in Mathematics* 341 (2019), 583–608, https://arxiv.org/abs/1710.10365. Definitions and Theorem 1.
3. E. Carneiro, G. Negro, D. Oliveira e Silva, *Stability of Sharp Fourier Restriction to Spheres*, *Journal of Fourier Analysis and Applications* 30 (2024), article 70, https://doi.org/10.1007/s00041-024-10120-z. Different ordinary \(L^4\) setting.
4. G. N. Watson, *A Treatise on the Theory of Bessel Functions*, 2nd edition (1944), Chapter VII (fixed-order asymptotics) and Chapter XV (zeros and interlacing).
