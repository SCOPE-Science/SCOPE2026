# Two monotone Zak-resonance curves for even quadratic-Gaussian Gabor windows

## Finding
Fix the Fourier convention \(M_\xi f(t)=e^{2\pi i\xi t}f(t)\) and the quadratic-Gaussian window
\[
  g_c(t)=(t^2-c)e^{-\pi t^2},\qquad c\in\mathbb R.
\]
For every \(a>0\), choose the rectangular lattice \((a,b)\) with \(b=1/(2a)\). Introduce two absolutely convergent Gaussian-moment quotients
\[
 U(a)=\frac{a^2\sum_{k\in\mathbb Z}(k+\tfrac12)^2e^{-\pi a^2(k+1/2)^2}}
                  {\sum_{k\in\mathbb Z}e^{-\pi a^2(k+1/2)^2}},
\quad
 V(a)=\frac{4a^2\sum_{j\in\mathbb Z}(-1)^j j^2e^{-4\pi a^2j^2}}
                  {\sum_{j\in\mathbb Z}(-1)^j e^{-4\pi a^2j^2}}.
\]
Both denominators are strictly positive. The functions \(U,V:(0,\infty)\to\mathbb R\) are strictly increasing real-analytic bijections onto
\[
 U((0,\infty))=(1/(2\pi),\infty),\qquad V((0,\infty))=(-\infty,0),
\]
and satisfy the exact reciprocal-lattice duality
\[
 \boxed{V(a)=\frac1{2\pi}-U\!\left(\frac1{2a}\right).}
\]
If \(c=U(a)\) or \(c=V(a)\), then the single-window Gabor system
\[
 \mathcal G(g_c,a,1/(2a))
   =\{M_{m/(2a)}T_{na}g_c:m,n\in\mathbb Z\}
\]
is **not** a frame for \(L^2(\mathbb R)\). More precisely, its two-channel Zak energy has a common zero at \((x,\omega)=(a/2,0)\) in the first case, and at \((x,\omega)=(0,1/4)\) in the second.

Consequently, **every strictly positive window** \(g_c\) with \(c<0\) has exactly one aspect \(a>0\) at which the second distinguished resonance causes frame failure. Every \(c>1/(2\pi)\) likewise has exactly one aspect at which the first resonance causes frame failure. These uniqueness assertions concern the explicitly identified symmetry fibers, **not** a classification of all possible non-frame lattice aspects.

The two resonance fibers have the exact off-resonance energy identities
\[
 \begin{aligned}
 E_a(a/2,0)&=S(a)^2\big(c-U(a)\big)^2,\\
 E_a(0,1/4)&=2D(a)^2\big(c-V(a)\big)^2,
 \end{aligned}
\]
where \(S(a)=\sum_k e^{-\pi a^2(k+1/2)^2}>0\), \(D(a)=\sum_j(-1)^je^{-4\pi a^2j^2}>0\), and \(E_a(x,\omega)=|Z_ag_c(x,\omega)|^2+|Z_ag_c(x,\omega+1/2)|^2\). Thus the local fiber zeros are exact quadratic resonances as the polynomial coefficient varies.

## Assumptions and scope
The modulation and translation operators are \(M_\xi,T_x\) as above, with \(T_xf(t)=f(t-x)\). The Zak transform is
\[
 Z_af(x,\omega)=\sum_{k\in\mathbb Z}f(x+ak)e^{-2\pi i k\omega},
 \quad 0\le x<a,\ 0\le\omega<1.
\]
For Schwartz windows it is continuous, including at boundaries with their standard quasiperiodic identifications. At lattice product \(ab=1/2\), Fourier-series Parseval applied to the even and odd modulation cosets gives a frame if and only if the continuous function \(E_a\) has strictly positive minimum. In particular, any common zero of its two Zak terms proves non-frame behavior. No lower frame bound or classification is asserted away from the two specified fibers.

## Proof
**1. Exact Zak fibers.** Since \(g_c\) is even, terms indexed by \(k\) and \(-k-1\) cancel at \((a/2,1/2)\): \(Z_ag_c(a/2,1/2)=0\). At frequency zero, direct substitution gives
\[
 Z_ag_c(a/2,0)=S(a)(U(a)-c).
\]
At \(x=0\), \(\omega=1/4\), the positive and negative odd integer summands cancel, and the even summands \(k=2j\) contribute the factor \((-1)^j\). The identical cancellation holds at \(\omega=3/4\). Therefore
\[
 Z_ag_c(0,1/4)=Z_ag_c(0,3/4)=D(a)(V(a)-c).
\]
These equalities prove both zero criteria and the two energy identities. In the half-density Zak representation, splitting the modulations into integer and half-integer frequency cosets yields the frame-weight \(E_a\) up to a positive constant. Hence a common zero excludes a lower frame bound.

**2. Poisson duality and positivity.** Set \(q=e^{-\pi/a^2}\). Poisson summation of the shifted Gaussian gives
\[
 S(a)=a^{-1}\vartheta_4(0,q),\qquad
 \vartheta_4(0,q)=\sum_{j\in\mathbb Z}(-1)^j q^{j^2}.
\]
Jacobi's product identity
\[
 \vartheta_4(0,q)=\prod_{n\ge1}(1-q^{2n})(1-q^{2n-1})^2>0
\]
proves positivity of \(S\) and of \(D(a)=\vartheta_4(0,e^{-4\pi a^2})\). Poisson summation once more gives the exact identity
\[
 D(a)=\frac1{2a}S\!\left(\frac1{2a}\right).
\]
Writing \(U(a)=-\tfrac{a}{2\pi}\tfrac{d}{da}\log S(a)\) and \(V(a)=-\tfrac{a}{2\pi}\tfrac{d}{da}\log D(a)\), logarithmic differentiation of the last identity proves the displayed duality.

**3. Strict monotonicity of \(U\).** Put \(v=a^2\). From the product identity,
\[
 -\log\vartheta_4(0,q)=\sum_{m\ge1}A_mq^m,
 \quad A_m>0,
\]
where the power series converges absolutely on \(0<q<1\). Taking the logarithmic derivative of the Poisson formula for \(S\) yields
\[
 U(\sqrt v)=\frac1{2\pi}
    +\frac1v\sum_{m\ge1}mA_m e^{-\pi m/v}.
\]
All terms are positive, proving \(U>1/(2\pi)\). For \(0<v\le\pi\), each summand \(v^{-1}e^{-\pi m/v}\) has nonnegative derivative because \(\pi m-v\ge0\), and it is strictly positive for \(m\ge2\). Local uniform convergence with derivatives proves strict increase on this interval.

For \(v\ge\pi\), pair the half-integer lattice terms and set \(h_k=k(k+1)\) for \(k\ge0\). Their normalized probabilities are proportional to \(e^{-\pi v h_k}\); write \(\mathbb E_v\) and \(\operatorname{Var}_v\) for the corresponding mean and variance. Then
\[
 U(\sqrt v)=v\big(\tfrac14+\mathbb E_vh\big),\qquad
 \frac{d}{dv}U(\sqrt v)=\tfrac14+\mathbb E_vh-\pi v\operatorname{Var}_v(h).
\]
With \(r=e^{-2\pi v}\), the elementary bounds \(h_k\ge2k\), \(h_k^2\le4k^4\), and \(\sum_{k\ge1}k^4r^k=r(1+11r+11r^2+r^3)/(1-r)^5<2r\) for \(0<r\le1/100\) give
\[
 \pi v\operatorname{Var}_v(h)
 \le4\pi v\sum_{k\ge1}k^4r^k
 <8\pi ve^{-2\pi v}
 \le8\pi^2e^{-2\pi^2}<\tfrac14.
\]
Here \(r\le e^{-2\pi^2}<1/100\), and the last bound follows, for example, from \(3<\pi<4\) and \(e>2\). Thus \(U\) increases strictly also for \(v\ge\pi\), completing its global proof.

**4. Exact ranges and uniqueness.** At small \(a\), the positive power-series formula gives
\[
 U(a)=\frac1{2\pi}+\frac2{a^2}e^{-\pi/a^2}
   +O\big(a^{-2}e^{-2\pi/a^2}\big).
\]
At large \(a\), direct half-grid Gaussian comparison gives
\[
 U(a)=\frac{a^2}{4}+2a^2e^{-2\pi a^2}
   +O\big(a^2e^{-4\pi a^2}\big).
\]
These show \(U(a)\downarrow1/(2\pi)\) as \(a\downarrow0\) and \(U(a)\to\infty\) as \(a\to\infty\). Its derivative is everywhere positive, so it is a bijection onto the claimed open range. Since \(a\mapsto1/(2a)\) is strictly decreasing, the duality makes \(V\) strictly increasing from \(-\infty\) to \(0\). Both are analytic because their Gaussian series and denominators are analytic and uniformly convergent on compact positive intervals.

**5. A positive-window obstruction outside positive Gaussian-scale mixing.** For every \(c<0\), \(g_c(t)=(t^2+|c|)e^{-\pi t^2}>0\) for all real \(t\). Since \(V\) is a bijection onto \((-\infty,0)\), there is exactly one \(a\) with \(V(a)=c\), proving the asserted non-frame construction for every such strictly positive window. This is not a consequence of positive Gaussian-scale-mixture theorems: the function \(y\mapsto(y+|c|)e^{-\pi y}\) fails complete monotonicity, since for any integer \(n>\pi|c|\) its \(n\)-th derivative has \((-1)^nf^{(n)}(0)=\pi^n(|c|-n/\pi)<0\). Every positive mixture of \(e^{-sy}\) is completely monotone where its derivatives exist.

## Verification
Run `python3 CHECK.py` with the Python standard library. The checker independently evaluates the relevant Zak series on multiple aspects, checks both simultaneous zeros, compares Poisson-dual formulas, confirms the exact off-resonance quadratic fiber energies, and tests a finite grid of monotonicity inequalities. It gives 1,011 supplementary checks. The all-aspect and all-coefficient conclusions rest on the proof, not on finite tests.

## Relationship to prior work
Lemvig's November 2026 degree-based sufficient frame criterion establishes frames at irrational products and at rational \(p/q\) when \(q-p\) exceeds the degree of the polynomial. At the present product \(1/2\) and polynomial degree two, the deficit is only one; that criterion does not imply frames or nonframes here. Ulanovskii and Zlotnikov construct general parity-based polynomial-Gaussian nonframes at product \(1/(N+1)\) using polynomials of degree at most \(N\), but their specified even-quadratic family at \(N=2\) concerns product \(1/3\), not the present half-density two-curve classification. Older pure-Hermite results concern special polynomial coefficients, rather than both strictly monotone coefficient-to-aspect resonances across all \(a>0\).

Previously published results for **affine** Gaussian polynomials at half-density establish a contrasting stability phenomenon: every nonzero Gaussian component restores a frame to the first-Hermite mixture. They do not address even quadratic polynomials. A published positive *Gaussian-scale-mixture* Zak-zero theorem likewise does not apply to the positive quadratic-Gaussian windows considered here, as shown by the complete-monotonicity obstruction in the proof. The novelty assertion is the exact two-branch arithmetic/analytic resonance and strict global parameter uniqueness for these specific fibers, not the Zak criterion or Jacobi product themselves.

## Limitations
Only two symmetry-enforced Zak fibers and the corresponding resonance curves are classified. There may be other simultaneous Zak zeros, nonframe aspects, or frame obstructions, including outside these curves; none are excluded by the theorem. The coefficient \(c\) is real, the Gaussian scale is fixed, the lattice is rectangular with area exactly \(1/2\), and no extension to arbitrary complex quadratic coefficients or higher degrees is claimed. The historical priority of the precise theta-quotient monotonicity and its use in Gabor theory remains susceptible to a previously uncatalogued equivalent theta identity. No external independent validation is claimed.

## References
1. A. Ulanovskii and I. Zlotnikov, *Periodic Non-uniqueness Sets for Shift-invariant Spaces and Parity-Based Obstructions to the Frame Property for Gabor Systems*, arXiv:2606.31450v1, first public 30 June 2026, https://arxiv.org/abs/2606.31450.
2. J. Lemvig, *On the Gabor frame set of polynomial–Gaussian windows*, arXiv:2611.05337v1, first public 3 November 2026, https://arxiv.org/abs/2611.05337.
3. J. Lemvig, *On some Hermite series identities and their applications to Gabor analysis*, arXiv:1509.04701, https://arxiv.org/abs/1509.04701.
4. M. Faulhuber and P. Petersen, *The frame set of the first Hermite function*, arXiv:2609.02610, https://arxiv.org/abs/2609.02610.
5. A. J. E. M. Janssen, *On Generating Tight Gabor Frames at Critical Density*, Journal of Fourier Analysis and Applications 9 (2003), 175–214, https://doi.org/10.1007/s00041-003-0011-3.
