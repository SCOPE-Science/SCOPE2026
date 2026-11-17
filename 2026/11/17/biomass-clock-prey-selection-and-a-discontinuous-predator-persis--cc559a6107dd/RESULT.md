# Biomass-clock prey selection and a discontinuous predator-persistence boundary

## Finding

In a symmetric two-prey, one-predator Lotka–Volterra system, prey selection is governed by an **exact biomass clock** independent of predator activity. Every strictly positive initial state converges to a fully identified equilibrium. An exact logarithmic formula gives the entire accumulated transient excess competition over the eventual competitive regime. When direct cross-competition exceeds within-prey competition, a sharp range of predator efficiencies produces a discontinuous fate: the predator persists from *every* unequal positive prey composition but becomes extinct from the exactly balanced composition.

More precisely, let \(r,c,a,b>0\), and consider
\[
\dot x=x(r-rx-cy-az),\qquad
\dot y=y(r-ry-cx-az),\qquad
\dot z=z[b(x+y)-1]
\]
with \(x(0),y(0),z(0)>0\). Set \(s=x+y\), \(q=(x-y)/(x+y)\), and \(B(t)=\int_0^t s(u)\,du\). Then \(B(t)\to\infty\) and
\[
\frac{q(t)}{\sqrt{1-q(t)^2}}=
\frac{q(0)}{\sqrt{1-q(0)^2}}e^{-(r-c)B(t)/2}.
\]
For \(q(0)=0\), the right-hand side and \(q(t)\) are identically zero. Define \(q_\infty=0\) if \(r>c\); \(q_\infty=q(0)\) if \(r=c\); and, if \(r<c\), define \(q_\infty=\operatorname{sgn}q(0)\) for nonzero \(q(0)\), and \(q_\infty=0\) otherwise. With
\[
d(q)=\frac{r+c+(r-c)q^2}{2},\quad d_\infty=d(q_\infty),\quad
s_\infty=\min\left\{\frac r{d_\infty},\frac1b\right\},\quad
z_\infty=\frac{r-d_\infty s_\infty}{a},
\]
we have \(s(t)\to s_\infty\), \(z(t)\to z_\infty\), and
\[
(x(t),y(t))\to \tfrac12 s_\infty(1+q_\infty,1-q_\infty).
\]
In particular, \(z_\infty>0\) exactly when \(br>d_\infty\).

The total transient competition penalty is the absolutely convergent integral
\[
\boxed{\ \int_0^\infty s(t)[d(q(t))-d_\infty]\,dt
=\begin{cases}
-\tfrac12\log(1-q(0)^2),&r>c,\\
-\log|q(0)|,&r<c,\ q(0)\ne0,\\
0,&r=c\text{ or }q(0)=0.
\end{cases}\ }
\]
It depends solely on initial prey composition, not on predator parameters or the overall initial biomasses.

For \(c>r\) and \(1<b\le (r+c)/(2r)\), **all** strictly positive initial data with \(x(0)\ne y(0)\) yield predator persistence and exclusion of the initially rarer prey. But \(x(0)=y(0)\) instead implies \(z(t)\to0\), with both prey tending to \(r/(r+c)\). This discontinuity is with respect to the long-time outcome, not finite-time solution dependence.

## Assumptions and scope

All coefficients and all three initial populations are strictly positive and finite. The two prey are exchange-symmetric in intrinsic growth, self-limitation, cross-competition, predator loss and predator gain. There is no noise, migration, delay, predator saturation, or immigration. Claims are global for positive initial data within this precisely specified ordinary differential equation, including the neutral case \(c=r\) and the predator invasion threshold \(br=d_\infty\).

## Proof

**1. Global positivity, boundedness and clock divergence.** The vector field preserves each nonnegative coordinate face. For positive initial data, each coordinate stays positive on every finite interval. The variables \(s\) and \(q\) satisfy
\[
\dot s=s[r-d(q)s-az],\quad \dot q=-\frac{r-c}{2}s q(1-q^2),\quad \dot z=z(bs-1).
\]
The coefficient satisfies \(0<d_{\min}\le d(q)\le d_{\max}\), where \(d_{\min}=\min\{r,(r+c)/2\}\), \(d_{\max}=\max\{r,(r+c)/2\}\). Logistic comparison gives \(0<s(t)\le\max\{s(0),r/d_{\min}\}\). For \(L=s+(a/b)z\),
\[
\dot L=rs-d(q)s^2-(a/b)z\le -L+\frac{(r+1)^2}{4d_{\min}}.
\]
Thus \(s,z\) are bounded and the solution exists for every positive time. If \(B(t)\) had a finite limit, then \(z(t)=z(0)e^{bB(t)-t}\to0\). For sufficiently large time, \(\dot s\ge s(r/2-d_{\max}s)\); logistic comparison would force \(\liminf s(t)\ge r/(2d_{\max})>0\), a contradiction. Therefore \(B(t)\to\infty\).

**2. Exact selection and integrated penalty.** Divide the \(q\)-equation by \(\dot B=s\) to get \(dq/dB=-(r-c)q(1-q^2)/2\). Its logarithmic primitive gives the displayed clock identity, and hence every stated \(q_\infty\). For \(r>c\), put \(Q=q^2/(1-q^2)\); then \(Q(B)=Q(0)e^{-(r-c)B}\) and
\[
\int_0^\infty s[d(q)-d_\infty]dt
=\frac{r-c}{2}\int_0^\infty\frac{Q(B)}{1+Q(B)}dB
=\tfrac12\log(1+Q(0))=-\tfrac12\log(1-q(0)^2).
\]
For \(r<c\) and \(q(0)\ne0\), use \(P=(1-q^2)/q^2\); then \(P(B)=P(0)e^{-(c-r)B}\) and
\[
\int_0^\infty s[d(q)-d_\infty]dt
=\frac{c-r}{2}\int_0^\infty\frac{P(B)}{1+P(B)}dB
=\tfrac12\log(1+P(0))=-\log|q(0)|.
\]
The remaining invariant cases give zero integrand. In every case \(d(q(t))\ge d_\infty\), and \(\int_0^\infty s[d(q)-d_\infty]dt\) is finite.

**3. Global convergence.** Put \(s_*=s_\infty>0\), \(z_*=z_\infty\), and \(\delta(t)=d(q(t))-d_\infty\ge0\). If \(z_*>0\), then \(bs_*=1\) and \(r=d_\infty s_*+az_*\). Use
\[
V=s-s_*-s_*\log(s/s_*)+(a/b)[z-z_*-z_*\log(z/z_*)].
\]
Its exact derivative is \(\dot V=-d_\infty(s-s_*)^2-\delta(t)s(s-s_*)\). If \(z_*=0\), then \(r=d_\infty s_*\), \(bs_*\le1\), and with \(V=s-s_*-s_*\log(s/s_*)+(a/b)z\) the derivative is
\[
\dot V=-d_\infty(s-s_*)^2-\delta(t)s(s-s_*)-(a/b)(1-bs_*)z.
\]
Both potentials are bounded below, and the error \(|\delta s(s-s_*)|\) is integrable by Step 2 and boundedness of \(s\). Integrating yields \(\int_0^\infty(s-s_*)^2dt<\infty\). Because \(\dot s\) is bounded and \(s\) is uniformly continuous, \(s-s_*\) is uniformly continuous; Barbalat's lemma yields \(s\to s_*\). The bounded polynomial vector field gives bounded \(\ddot s\), hence convergence of \(s\) implies \(\dot s\to0\). From \(\dot s/s=r-d(q)s-az\), and \(s_* >0\), conclude \(z\to (r-d_\infty s_*)/a=z_*\). The limits for \(x,y\) follow from \(q\to q_\infty\).

**4. Sharp predator boundary.** When \(c>r\) and \(q(0)\ne0\), Step 2 forces \(q_\infty=\pm1\), so \(d_\infty=r\) and \(z_\infty>0\) iff \(b>1\). When \(q(0)=0\), the diagonal is invariant and \(d_\infty=(r+c)/2\), so \(z_\infty>0\) iff \(b>(r+c)/(2r)\). Combining the strict and equality cases gives the stated exact parameter strip. Moreover, \(B(t)/t\to s_*>0\), which makes minority-to-majority prey ratios decay exponentially when \(c>r\) and the initial composition is unequal.

## Verification

Run the standalone `verify.py` with Python, SymPy, NumPy and SciPy. It checks the mass-frequency differential identities symbolically, the exact biomass-clock identity at multiple finite times, the integrated-penalty formula, and nine long-time equilibrium cases (including two states with the same coefficients but different equality of initial prey abundances). The expected output starts with `VERIFY_OK`. The infinite-time and all-parameter conclusions are analytical; numerical trajectories corroborate only sampled cases.

## Relationship to prior work

Huang and Yang (2026) investigate the same general two-prey/one-predator Lotka–Volterra equations, but their main generic classification assumes the *strict* apparent-competition ordering \(r_1a_{23}>r_2a_{13}\) (Section 3). The present exact exchange-symmetric specialization satisfies equality, and its biomass-clock identity, globally quantified predator-persistence separatrix and cumulative competition penalty are not statements of that generic classification. Cruz and Neves (2026) study predator-dependent replicator dynamics for a different frequency-dependent system; the known replicator transformation itself is not claimed as new. Earlier general Lotka–Volterra global-stability and competitive-exclusion results motivate but do not directly furnish this precise all-parameter quantitative penalty or the sharp initial-composition discontinuity. This is an assessment of available literature, not a certification of historical priority.

## Limitations

The result requires exact exchange symmetry; unequal prey mortality or predator attack rates generally remove the closed frequency equation. Predator persistence means a positive deterministic limit, not survival in finite stochastic populations. The predator-persistence dichotomy is a discontinuity of the long-time limit across an invariant separatrix, while solutions depend continuously on initial data at each finite time. Full historical priority has not been independently validated. This is not an assertion about the entire asymmetric eight-parameter model.

## References

1. M. Huang and T. Yang, *Direct and Indirect Competition in a Two-Prey-One-Predator System – Global Dynamics, Chaos, and the Paine Conjecture*, arXiv:2611.02246v1, posted 2026-11-01. https://arxiv.org/html/2611.02246v1
2. H. M. Cruz and A. G. M. Neves, *Predator-dependent replicator dynamics or a predator-prey model with two prey types and frequency dependence*, arXiv:2607.13281, posted 2026-07-14. https://arxiv.org/abs/2607.13281
3. M. L. Zeeman and P. van den Driessche, *Three-Dimensional Competitive Lotka–Volterra Systems with no Periodic Orbits*, SIAM J. Appl. Math. 58 (1998), DOI 10.1137/S0036139995294767 (background context; different competitive sign structure).
