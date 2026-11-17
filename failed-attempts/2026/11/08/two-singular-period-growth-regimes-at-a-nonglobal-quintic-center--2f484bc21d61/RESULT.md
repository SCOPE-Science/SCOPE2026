# Two singular period-growth regimes at a nonglobal quintic center

## Finding
For \(\kappa>0\) and \(\beta\geq0\), consider the real polynomial flow
\[
\dot x=v,\qquad \dot v=-x+\kappa x^3v^2-\beta x^5.
\]
Every positive turning amplitude \(A\) determines exactly one nonconstant periodic orbit, with turning points \((\pm A,0)\). These orbits fill precisely the sublevel annulus \(0<H<H_\infty\) defined below; this center is **not global**. Its **minimal period in original physical time** satisfies
\[
\boxed{\lim_{A\to\infty}\frac{T_{\kappa,0}(A)}{A^2}=2\sqrt\kappa},\qquad
\boxed{T_{\kappa,\beta}(A)=4\sqrt{\frac\kappa\beta}\log A+O_{\kappa,\beta}(1)\quad(\beta>0).}
\]
Thus the pure velocity-feedback edge has quadratic period growth, whereas *every* positive quintic-restoring coefficient produces logarithmic growth. Furthermore,
\[
T_{\kappa,\beta}(A)=2\pi\left[1+\frac{\kappa-5\beta}{16}A^4+O_{\kappa,\beta}(A^8)\right]\quad(A\downarrow0).
\]
For \(5\beta>\kappa\), the period function therefore attains a global minimum below \(2\pi\) at one or more isolated strict local minima; every period strictly between that minimum and \(2\pi\) is realized by **at least two distinct** periodic orbits. Neither uniqueness of the critical point nor its nondegeneracy is asserted.

## Assumptions and scope
All parameters are real, with \(\kappa>0\), \(\beta\ge0\), and every turning amplitude satisfies \(A>0\). An orbit is a geometric closed trajectory, counted without phase duplication. The parameter \(\kappa\) is the **positive** coefficient of \(x^3v^2\), outside the global-center range of the motivating quintic classification. Time is never rescaled. The large-amplitude estimates fix the parameters before taking \(A\to\infty\); they are not uniform as \(\beta\downarrow0\).

Define
\[
p(x)=e^{-\kappa x^4/4},\quad V(x)=\int_0^x s(1+\beta s^4)e^{-\kappa s^4/2}\,ds,\quad H(x,v)=\tfrac12p(x)^2v^2+V(x).
\]
The even, strictly increasing positive-half-line potential has a finite ceiling
\[
H_\infty=\lim_{x\to\infty}V(x)=\frac{\sqrt{2\pi}}{4\sqrt\kappa}\left(1+\frac\beta\kappa\right).
\]

## Proof
**1. Exact annulus and first integral.** The derivative \(p'(x)/p(x)=-\kappa x^3\) gives
\[
\frac{d}{dt}\left(\tfrac12p(x)^2v^2+V(x)\right)=p(x)^2v\left[(\kappa x^3+p'/p)v^2-x(1+\beta x^4)\right]+V'(x)v=0.
\]
The potential \(V\) is even, strictly increasing for \(x>0\), and has the displayed finite ceiling, calculated by substituting \(w=\kappa s^4/2\) and evaluating two gamma integrals. For each \(0<E<H_\infty\) there is one \(A>0\) with \(V(A)=E\), and the level \(H=E\) is one smooth compact simple oval. Its vector field is nonzero everywhere; it is therefore one periodic orbit. Conversely, energies \(E\ge H_\infty\) have unbounded level components, so the center is not global. At any fixed \(A\), its minimal period is exactly
\[
T(A)=4\int_0^A\frac{p(x)\,dx}{\sqrt{2[V(A)-V(x)]}}=4\int_0^A\frac{dx}{\sqrt{S_A(x)}},\quad
S_A(x)=2\int_x^Au(1+\beta u^4)e^{-\kappa(u^4-x^4)/2}\,du. \tag{1}
\]
The four quarter traversals have equal durations by the two reflection symmetries of the energy oval. The integrable square-root turning singularity makes the period finite and continuous for every \(A>0\).

**2. Stable exact kernel representation.** The substitution \(w=\kappa(u^4-x^4)/2\) in (1) yields
\[
S_A(x)=\frac1\kappa\int_0^{h_A(x)}e^{-w}\left[(x^4+2w/\kappa)^{-1/2}+\beta(x^4+2w/\kappa)^{1/2}\right]dw,\qquad h_A(x)=\frac\kappa2(A^4-x^4). \tag{2}
\]
For \(x\to\infty\) and \(A\ge2x\), uniformly in \(A\), expanding the two bracketed terms and using exponential integrability gives
\[
S_A(x)=\frac{1+\beta x^4}{\kappa x^2}\left(1+O_{\kappa,\beta}(x^{-4})\right).\tag{3}
\]
Indeed \(h_A(x)\ge 15\kappa x^4/2\); the omitted exponential tail is smaller than any negative power, while a mean-value estimate on \(0\le w\le h_A(x)\), weighted by \(e^{-w}\), bounds the relative integrand error by a constant multiple of \(w/x^4\).

**3. Bounds through the moving turning point.** For large \(A\), let \(x_0=(A^4-2/\kappa)^{1/4}\). On \(1\le x\le x_0\) the upper integration limit in (2) is at least one. Restricting its integral to \(0\le w\le1\) proves
\[
\frac1{\sqrt{S_A(x)}}\le C_\kappa\frac{x}{\sqrt{1+\beta x^4}},\tag{4}
\]
with a constant independent of \(A\) (and one may choose it independent of \(\beta\ge0\)). On \(x_0\le x\le A\), where \(h_A(x)\le1\), we have \(x\ge A/2\) and (2) implies
\[
S_A(x)\ge c_\kappa A(1+\beta A^4)(A-x).
\]
Consequently
\[
\int_{x_0}^A\frac{dx}{\sqrt{S_A(x)}}=O_\kappa\!\left(\frac1{A^2\sqrt{1+\beta A^4}}\right).\tag{5}
\]
The piece \(0\le x\le1\) contributes uniformly \(O_{\kappa,\beta}(1)\) as \(A\to\infty\), since for \(A\ge2\) its denominator is bounded from below by the positive, integrable-on-this-interval kernel \(S_2(x)\).

**4. Quadratic edge \(\beta=0\).** At each fixed \(t\in(0,1)\), the upper limit \(h_A(At)\) tends to infinity. Equation (2), or the same dominated Laplace argument as (3), gives \(S_A(At)\sim1/(\kappa A^2t^2)\). Therefore the normalized integrand of the amplitude-rescaled period satisfies
\[
\frac1A\,\frac1{\sqrt{S_A(At)}}\longrightarrow\sqrt\kappa\,t.
\]
Inequality (4) supplies the integrable dominating function \(C_\kappa t\) off the vanishingly narrow final interval, which contributes \(o(1)\) after dividing the integral by \(A^2\) by (5). The fixed interval \(0\le x\le1\) is negligible. Dominated convergence yields
\[
\lim_{A\to\infty}\frac{T_{\kappa,0}(A)}{A^2}=4\sqrt\kappa\int_0^1t\,dt=2\sqrt\kappa.
\]

**5. Logarithmic regime \(\beta>0\).** For \(1\le x\le A/2\), (3) gives uniformly
\[
\frac1{\sqrt{S_A(x)}}=\frac{\sqrt\kappa\,x}{\sqrt{1+\beta x^4}}\left(1+O_{\kappa,\beta}(x^{-4})\right)
=\sqrt{\frac\kappa\beta}\frac1x+O_{\kappa,\beta}(x^{-5}).
\]
Its integral from 1 to \(A/2\) is \(\sqrt{\kappa/\beta}\log A+O_{\kappa,\beta}(1)\). The remaining interval \([A/2,x_0]\) contributes only \(O_{\kappa,\beta}(1)\) by (4), while (5) and the initial fixed interval contribute bounded amounts. Multiplying by four proves the announced logarithmic law including bounded additive error.

**6. Small amplitudes and critical periods.** The time-preserving odd coordinate \(z=\int_0^xp(s)\,ds=x-\kappa x^5/20+O(x^9)\) obeys \(\ddot z+h(z)=0\), where \(h(z)=z+(\beta-\kappa/5)z^5+O(z^9)\). The standard turning-point integral, expanded by \((1-u^6)/(1-u^2)=1+u^2+u^4\), gives \(T=2\pi[1-5(\beta-\kappa/5)A^4/16+O(A^8)]\). If \(5\beta>\kappa\), the period initially falls below \(2\pi\), yet step 5 makes it diverge to infinity. Continuity and analyticity for \(A>0\) imply the minimum is attained at an interior isolated strict critical point. For every \(\tau\) strictly between its global minimum and \(2\pi\), the intermediate-value theorem yields one orbit on each side of a minimizer.

## Verification
The self-contained `verify_period.py` checks the exact conserved-energy derivative and the fifth-order normal-form coefficient symbolically, verifies the kernel-substitution algebra, and independently evaluates the convergent quadrature using a stable upper-limit substitution. It passes nine algebraic and sample-value assertions, including comparisons of four physical periods. Finite numerical samples corroborate only the finite cases. The asymptotic statements follow analytically from the kernel bounds and dominated convergence, not from extrapolating samples.

## Relationship to prior work
Da Cruz and Llibre [1], Theorems 1–2, classify global and local centers of a larger quintic family. They do not provide this nonglobal annulus's physical-time period law or critical-period existence. The published note [2] proves strict period decrease and high-amplitude decay for the **opposite** sign of the velocity-squared term, \(\dot v=-x-\alpha x^3v^2-\beta x^5\) with \(\alpha\ge0\). It neither contains nor implies the present divergence theorem, which requires \(\kappa>0\). The classical period-function literature [3] studies related oscillator criteria but does not establish the two specific large-amplitude laws inspected here. The integral-factor method is standard and is not claimed as new; the focus is the exact non-global annulus, exponent transition, and forced critical periods.

## Limitations
No uniqueness or nondegeneracy of the critical period is claimed. In particular, \(5\beta>\kappa\) is a **sufficient** region for critical periods, not a necessary-and-sufficient phase boundary. The statements concern the original-time periods of the specified two-parameter quintic family and fixed-parameter amplitude limits; neither an all-six-parameter result nor a uniform \(\beta\to0\) asymptotic is asserted. An inaccessible older general Liénard article [3] creates residual priority uncertainty; its abstract concerns a different standard Liénard coordinate representation, so it does not by itself establish this exact result. Independent validation is pending.

## References
1. L. P. C. da Cruz and J. Llibre, *Global Centers in a Class of Quintic Polynomial Differential System*, arXiv:2312.05709v1, publicly posted December 9, 2023, https://arxiv.org/html/2312.05709v1 .
2. *Strict period decrease and sharp large-amplitude laws for quintic global centers*, published mathematical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-strict-period-decrease-and-sharp-large-amplitude-laws-for-quinti--ffe383da977f .
3. L.-J. Yang and X.-W. Zeng, *The period function of Liénard systems*, Proc. Roy. Soc. Edinburgh A 143 (2013), 205–221, doi:10.1017/S0308210511000096 .
