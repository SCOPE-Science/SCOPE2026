# Two sharp stage-count barriers for noise reentrance and enhancement in a one-defect biased hopping motor

## Finding
Let \(n\ge 3\), \(p>q>0\), and \(s>0\). Consider an unwrapped nearest-neighbor continuous-time walk \(X_t\in\mathbb Z\). At sites congruent to zero modulo \(n\), its right and left hopping rates are \(sp,sq\); at all other sites the rates are \(p,q\). Define \(a=s^{-1}-1\in(-1,\infty)\), \(\delta=p-q\), \(\Sigma=p+q\), and
\[
 B_n=\frac{p-q}{p+q}\frac{p^n+q^n}{p^n-q^n},\qquad y_n=nB_n.
\]
Then the stationary-regime velocity and effective diffusion coefficient are, exactly,
\[
 v=\lim_{t\to\infty}\frac{\mathbb E X_t}{t}=\frac{n\delta}{n+a},\qquad
 D(a)=\lim_{t\to\infty}\frac{\operatorname{Var}(X_t)}{2t}=
 \frac{\Sigma n^2}{2(n+a)^3}\left(n+2a+B_na^2\right).
\]
All results below use \(p,q,n\) fixed and vary the defect factor \(s\) (or its reciprocal slowness \(a\)). For any \(-1<a<0\), \(D\) decreases strictly as \(a\) increases; speeding up a site thus raises both drift and dispersion. For \(a>0\) (a slowed site) the *entire* shape classification is:

1. **First stage-count barrier.** If \(n\le4\), \(D(a)\) decreases strictly on \((0,\infty)\). If \(n\ge5\), there is one unique bias ratio \(R_{n,4}>1\) determined by \(y_n(R_{n,4})=4\). Below it, \(D\) decreases strictly; at it, the derivative vanishes at one positive double root without changing sign; above it, \(D\) has exactly two distinct positive critical slownesses,
\[
 a_\pm=\frac{y_n-2\pm\sqrt{(y_n-1)(y_n-4)}}{B_n},\quad 0<a_-<a_+,
\]
which are, respectively, a strict local minimum and a strict local maximum.

2. **Second stage-count barrier.** A *slowed* defect achieves a strictly larger diffusivity than the completely homogeneous motor \(D(0)=\Sigma/2\) for some \(a>0\) **if and only if** \(n\ge6\) and \(y_n>5\). For \(n\ge6\), the latter is equivalent to the bias ratio exceeding the unique \(R_{n,5}>R_{n,4}\) determined by \(y_n(R_{n,5})=5\). In that regime, and only there, enhancement occurs on the single open interval
\[
 \frac n2\left(y_n-3-\sqrt{(y_n-1)(y_n-5)}\right)<a<
 \frac n2\left(y_n-3+\sqrt{(y_n-1)(y_n-5)}\right).
\]
At \(y_n=5\), the local maximum merely touches the baseline \(D(0)\) at \(a=n\) without exceeding it. Below that point every slowed defect has \(D(a)<D(0)\).

In particular, the first genuinely reentrant dispersion shape requires at least five stages; an absolute dispersion gain over a uniform motor requires at least six stages. Throughout, the drift speed decreases strictly as the defect is slowed, even when dispersion increases.

## Assumptions and scope
All rates are strictly positive, the lattice extends infinitely in both directions, \(n\ge3\) is the period of a single exceptional departure-speed site, and the external drive ratio \(p/q>1\) is held fixed during a defect scan. This is a *one-particle, Markovian, exponential-dwell* model with both hopping directions retained; it is neither an exclusion process nor a finite closed-ring displacement without winding. The limits defining \(v\) and \(D\) exist and are independent of the initial site, by the finite-state additive-functional central limit theorem. Site spacing is one; multiplication by physical step length \(\ell\) multiplies \(v\) by \(\ell\) and \(D\) by \(\ell^2\).

## Proof
**Phase invariant law.** Write \(d_0=s\), \(d_i=1\) for \(1\le i<n\). The chain of residues modulo \(n\) has generator
\[
 (Lf)(i)=d_i\left[p(f(i+1)-f(i))+q(f(i-1)-f(i))\right]
\]
with indices modulo \(n\). Its unique invariant law is \(\pi_i=d_i^{-1}/(n+a)\), because the product \(\pi_i d_i\) is constant. Thus its mean infinitesimal displacement is \(v=\delta\sum_i\pi_i d_i=n\delta/(n+a)\).

**Corrector and exact variance.** Let \(\phi\) solve \(L\phi=v-\delta d_i\), which is solvable since its right-hand side has invariant mean zero. Define \(g_i=1+\phi(i+1)-\phi(i)\). Then
\[
 pg_i-qg_{i-1}=v/d_i=v(1+a\mathbf1_{\{i=0\}}).
\]
Put \(\rho=q/p\) and \(h_i=\rho^i/[p(1-\rho^n)]\) for \(i=0,\dots,n-1\). Direct substitution with cyclic subscripts gives \(ph_i-qh_{i-1}=\mathbf1_{\{i=0\}}\), so
\[
 g_i=\frac v\delta+va h_i,
 \quad \sum_i h_i=\frac1\delta,\quad
 \sum_i h_i^2=\frac{p^n+q^n}{p^n-q^n}\frac1{\delta\Sigma}.
\]
Also \(\sum_i g_i=n\), ensuring these really are the gradients of a cyclic corrector. The corrected displacement \(X_t+\phi(X_t\bmod n)-vt\) is a martingale with jump increments \(g_i\) and \(-g_{i-1}\). Its stationary quadratic-variation rate is
\[
 2D=\sum_i\pi_i d_i\left(pg_i^2+qg_{i-1}^2\right)
 =\frac\Sigma{n+a}\sum_i g_i^2,
\]
which reduces to the announced formula. The bounded corrector does not affect long-time variance growth, by standard finite-state Markov additive-functional arguments.

**Sharp reentrant criterion.** Differentiate with respect to \(a\):
\[
 \frac{2}{\Sigma n^2}(n+a)^4 D'(a)
 =-B_na^2+(2B_nn-4)a-n=:Q_n(a).
\]
The discriminant of this concave quadratic is \(4(y_n-1)(y_n-4)\). For all finite \(p>q>0\), \(1<y_n<n\). Consequently, for \(y_n<4\) the derivative is negative everywhere, and at \(y_n=4\) it is nonpositive with exactly one double zero. For \(y_n>4\), the two roots \(a_\pm\) shown above are strictly positive and simple; the sign sequence is negative–positive–negative. There are never positive roots for \(-1<a<0\): the discriminant-negative case has no real roots and the discriminant-positive case has only positive roots. This proves all monotonicity and extremum assertions.

**Sharp enhancement criterion.** Exact subtraction gives
\[
 \frac{2D(a)}\Sigma-1
 =-\frac{a\{a^2+n(3-y_n)a+n^2\}}{(n+a)^3}.
\]
For positive \(a\), strict enhancement is equivalent to negativity of the bracketed quadratic. It has a negative interval with two distinct positive roots exactly when \(y_n>5\). Its discriminant is \(n^2(y_n-1)(y_n-5)\), giving the exact interval in the statement; at \(y_n=5\) the single root \(a=n\) gives equality alone. Since \(y_n<n\), the strict condition requires \(n\ge6\).

**Existence and uniqueness of bias boundaries.** Write \(p/q=e^{2t}\) with \(t>0\). Then
\[
 y_n(t)=n\tanh(t)\coth(nt),\qquad
 \frac{d}{dt}\log y_n(t)=\frac2{\sinh(2t)}-\frac{2n}{\sinh(2nt)}>0,
\]
where the last inequality is strict since \(\sinh(2nt)>n\sinh(2t)\) for \(n>1\). The continuous limits are \(y_n(0+)=1\) and \(y_n(+\infty)=n\), so every target \(k\) with \(1<k<n\) is crossed exactly once. Taking \(k=4,5\) gives precisely the stated finite-size and bias thresholds.

## Verification
The standalone `CHECKER.py` verifies the exact dispersion formula via an independently solved finite Markov Poisson corrector with *rational* rates, and checks the two transition discriminants and representative derivative/enhancement inequalities. It does not attempt exhaustive numerical certification of the infinite parameter range; the algebraic sign and monotonicity proofs above provide that guarantee. An illustrative six-stage motor with \(p=20\), \(q=1\) has \(y_6\approx5.42857>5\); a slowed site of slowness \(a=6\) yields \(D(6)/D(0)\approx1.05357145\), despite reducing its drift from \(19\) to \(9.5\).

## Relationship to prior work
Derrida's 1983 general-period hopping theorem (equations 46–50) already determines drift and diffusion for *arbitrary periodic transition-rate arrays*. The exact rational formula here is therefore a specialization, **not claimed as an independent new general formula**. The assessed addition is the complete, all-stage sharp *two-tier bifurcation classification* for a single defect: five stages to create two noise extrema and six stages to exceed the homogeneous baseline, with unique drive boundaries and exact enhancement intervals. Kanada, Shinagawa and Sasaki's 2018 Brownian-motor paper studies diffusion enhancement in a different potential-switching/extended-step random walk, not the finite-stage departure-speed-defect family. These precedents make the priority of the classification, rather than the starting formula, the relevant originality question.

## Limitations
No experimental observation, finite-sample inference claim, interaction effect, global optimization over the entire vector of hopping rates, or energetic cost accounting is asserted. The conclusions rely on common right/left bias at all sites and one defect which scales both outgoing rates together. They do not apply automatically to a modified bond, local affinity defect, or arbitrary rate disorder. Although related general periodic-walk formulas are published, a complete publication-priority determination would require further independent source assessment. No independent scientific audit has been performed.

## References
- B. Derrida, *Velocity and Diffusion Constant of a Periodic One-Dimensional Hopping Model*, Journal of Statistical Physics 31 (1983), pp. 433–450, equations 46–50. https://www.lps.ens.fr/~derrida/PAPIERS/1983/jsp1983-vitesse.pdf
- R. Kanada, R. Shinagawa, K. Sasaki, *Diffusion Enhancement of Brownian Motors Revealed by a Solvable Model*, arXiv:1805.07870, first posted 2018-05-21; Phys. Rev. E 98, 062110 (2018). https://arxiv.org/abs/1805.07870 ; https://link.aps.org/accepted/10.1103/PhysRevE.98.062110
