# Two reset-rate first-passage profiles uniquely reconstruct drift and diffusivity

## Finding

For a smooth, uniformly nondegenerate diffusion on a finite interval with an absorbing target and a reflecting opposite boundary, the **two spatially resolved mean absorption-time profiles at any two distinct positive Poisson resetting rates** determine *both* the unknown spatial diffusivity and drift. The inverse denominator is strictly positive everywhere inside the interval; one rate never suffices without further coefficient restrictions.

Precisely, let \(0<r_1<r_2\). For a fixed reset location \(x_\star\) and starting position \(x\), write \(m_i(x)=\mathbb E_x\tau_{r_i}\), where \(\tau_{r_i}\) is the first absorption time when the position is returned to \(x_\star\) at rate \(r_i\). Set

\[
q_i(x)=r_i\bigl(m_i(x)-m_i(x_\star)\bigr)-1,
\qquad
W(x)=m_1''(x)m_2'(x)-m_2''(x)m_1'(x).
\]

Then for every \(0<x<L\), \(m_i'(x)>0\), \(W(x)>0\), and

\[
\boxed{
D(x)=\frac{q_1(x)m_2'(x)-q_2(x)m_1'(x)}{W(x)},\qquad
b(x)=\frac{m_1''(x)q_2(x)-m_2''(x)q_1(x)}{W(x)}.}
\]

Endpoint values are uniquely recovered by continuity. The positivity of \(W\), rather than merely a generic nondegeneracy assumption, is the essential theorem.

## Assumptions and scope

The state space is \([0,L]\), \(L>0\). The unreset reflected diffusion has backward generator \(\mathcal L f=D(x)f''+b(x)f'\), with \(D,b\in C^2([0,L])\), \(\inf D>0\), absorption at \(0\), and normal reflection at \(L\). Resetting is an independent Poisson process of positive known rate \(r\), replacing the position by the single known point \(x_\star\in(0,L)\), without changing the two generator coefficients. Measurements consist of exact, continuously spatially resolved mean absorption-time functions at two known distinct rates. All probabilities and expectations refer to these processes; the theorem does not assert reconstruction from finitely many noisy starting positions.

## Proof

**1. Resolvent and renewal identity.** Let \(T_0\) be the unreset time to hit \(0\), and \(\phi_r(x)=\mathbb E_x[e^{-rT_0}]\). On this compact reflected interval, \(T_0<\infty\) almost surely. Standard stopped-diffusion boundary-value theory gives the unique solution

\[
D\phi_r''+b\phi_r'=r\phi_r,\quad
\phi_r(0)=1,\quad\phi_r'(L)=0.
\]

A cycle that starts at \(x\) ends on absorption or on the independent exponential reset. Its mean duration is \((1-\phi_r(x))/r\) and its probability of resetting before absorption is \(1-\phi_r(x)\). Renewal at \(x_\star\) therefore yields

\[
m_r(x)=\frac{1-\phi_r(x)}{r\phi_r(x_\star)}.
\tag{1}
\]

Let \(p(x)=\exp(\int_0^x b(z)/D(z)\,dz)\). Since \((p\phi_r')'=r(p/D)\phi_r\) and \(\phi_r'(L)=0\), integration proves the exact positive-kernel identity

\[
-p(x)\phi_r'(x)=r\int_x^L\frac{p(y)}{D(y)}\phi_r(y)\,dy>0
\quad(0\le x<L).
\tag{2}
\]

Consequently \(\phi_r'(x)<0\) and, by (1), \(m_r'(x)>0\) throughout \((0,L)\).

**2. Strict ordering of logarithmic slopes.** Define \(H_r(x)=r\phi_r(x)/[-\phi_r'(x)]>0\) for \(0<x<L\). Divide (2) by \(r\phi_r(x)\) to obtain

\[
\frac1{H_r(x)}=\frac1{p(x)}\int_x^L\frac{p(y)}{D(y)}\frac{\phi_r(y)}{\phi_r(x)}\,dy.
\tag{3}
\]

For any \(y>x\), path continuity and the strong Markov property at the first hit of \(x\) give

\[
\frac{\phi_r(y)}{\phi_r(x)}
=\mathbb E_y[e^{-rT_x}],\qquad T_x=\inf\{t\ge0:X_t=x\}.
\]

Because \(T_x>0\) almost surely for \(y>x\) and \(T_x\) is almost surely finite on this compact reflected interval, the ratio is strictly decreasing in \(r\). Every weight in (3) is positive, so \(1/H_r(x)\) is strictly decreasing, and hence \(H_r(x)\) strictly increasing, in \(r\). The ODE then implies

\[
\frac{m_r''(x)}{m_r'(x)}=\frac{\phi_r''(x)}{\phi_r'(x)}
=-\frac{b(x)}{D(x)}-\frac{H_r(x)}{D(x)}.
\]

For \(r_1<r_2\), it follows that

\[
W(x)=\frac{m_1'(x)m_2'(x)}{D(x)}
\bigl(H_{r_2}(x)-H_{r_1}(x)\bigr)>0.
\tag{4}
\]

This proves **unconditional** linear independence of the two measured derivative pairs inside the domain, including for drift fields changing sign.

**3. Explicit inverse.** First-step conditioning or the generator equation for the reset process gives

\[
D(x)m_i''(x)+b(x)m_i'(x)
=r_i\bigl(m_i(x)-m_i(x_\star)\bigr)-1=q_i(x),
\]

with \(m_i(0)=0\), \(m_i'(L)=0\). The determinant of this two-equation linear system is precisely \(W(x)>0\). Cramer's rule proves both displayed inverse formulas. By continuity of \(D,b\) the endpoint values are determined by their interior limits. Every diffusion satisfying the assumptions and yielding the same two profiles consequently has the same coefficients.

**4. Sharp one-rate insufficiency.** Given one admissible rate \(r>0\) and its profile \(m\), take any nonzero smooth function \(\eta\) supported in a compact subinterval of \((0,L)\). For all sufficiently small real \(\epsilon\), set \(D_\epsilon=D+\epsilon\eta>0\) and \(b_\epsilon=b-\epsilon\eta m''/m'\) in the interior, equal to the originals elsewhere. Since \(m'>0\) on the compact support, the new drift is smooth and the same function \(m\) satisfies the *same* resetting backward equation and the same absorbing/reflecting boundary conditions. Uniqueness of the mean-equation solution (positive killing rate and absorbing boundary) shows that the perturbed coefficients produce exactly the same measured profile. Arbitrarily many distinct coefficient pairs are thus indistinguishable at one reset rate.

## Verification

`CHECK.py` numerically solves the Laplace boundary-value problem for \(D(x)=1+x/4\), \(b(x)=-0.3+0.5x\), \(L=1\), \(x_\star=0.43\), and rates \((0.4,2.0)\), reconstructing coefficients on 185 interior points. It separately checks three constant-coefficient cases. This tests normalization, signs, derivatives, strict positivity, and inverse formulas, but the universal result follows from the exact proof above, not the finite tests.

## Relationship to prior work

Keidar, Reuveni, and Sokolov (2026) solve an inverse mean-first-passage profile problem with a known constant diffusivity and no Poisson resetting. Their source motivates asking how independent external resetting controls can resolve **both** spatially varying transport coefficients. Bal and Chou (2004) study recovery from full first-exit *time distributions observed at one fixed starting location*, using spectral inverse techniques and partial prior knowledge. Their introduction explicitly notes classical determination from different spatial exit probabilities and mean times; that is a different dataset. Neither inspected paper gives two **reset-rate-indexed spatial mean profiles** with an everywhere strictly positive two-profile Wronskian and sharp one-rate insufficiency. The classical backward ODE and renewal ingredients are acknowledged, not claimed as original.

## Limitations

The theorem requires exact twice-differentiable continuum observations for each rate, unchanged coefficients between experiments, known reset rates/location, and a compact interval with absorption/reflection. Since \(m_i'(L)=0\), the determinant tends to zero as \(x\uparrow L\), so differentiation and coefficient recovery can be ill-conditioned near that endpoint; no uniform noisy-data stability estimate is asserted. No claim is made for unknown reset locations, non-Poisson resets, unbounded domains, or partial observation windows. General inverse diffusion theory might imply the result indirectly; comprehensive independent priority assessment has not been performed.

## References

1. T. D. Keidar, S. Reuveni, and I. M. Sokolov, *The Inverse Mean First-Passage Time Problem* (2026), arXiv:2611.03831, first publicly submitted 2026-11-02. https://arxiv.org/abs/2611.03831 ; lawful full text https://arxiv.cnoctave.top/pdf/2611.03831 .
2. G. Bal and T. Chou, *On the reconstruction of diffusions from first-exit time distributions*, Inverse Problems **20** (2004), 1053–1065, doi:10.1088/0266-5611/20/4/004. Author-posted full text https://www.stat.uchicago.edu/~guillaumebal/PAPERS/FirstExit.pdf .
3. P.-W. Fok, *Drift reconstruction from first passage time data using the Levenberg–Marquardt method* (2013). A drift-only inverse formulation for different observations; source abstract was available but its full text was not independently inspected.
