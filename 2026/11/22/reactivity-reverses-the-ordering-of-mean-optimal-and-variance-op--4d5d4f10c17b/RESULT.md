# Reactivity reverses the ordering of mean-optimal and variance-optimal run-and-tumble search speeds

## Finding

Let \(a>0\) be dimensionless target reactivity and \(v>0\) dimensionless propulsion speed in the symmetric one-dimensional run-and-tumble search model specified below. Write \(m_a(v)=\mathbb E[T]\) and \(s_a^2(v)=\operatorname{Var}(T)\). The mean has a unique global minimizer \(v_M(a)\) for **every** \(a>0\). The variance has a unique global minimizer \(v_V(a)\) for all sufficiently small and all sufficiently large \(a>0\). Put \(c=(4/3)^{1/3}\). As \(a\downarrow0\),

\[
\begin{aligned}
v_M(a)&=c a^{1/3}+\frac{c^2}{8}a^{2/3}+O(a),\\
v_V(a)&=c a^{1/3}+\frac{c^2}{5}a^{2/3}+O(a),\\
v_V(a)-v_M(a)&=\frac{3c^2}{40}a^{2/3}+O(a)>0.
\end{aligned}
\]

As \(a\to\infty\),

\[
\frac{a}{v_M(a)}=\log(2a/3)+o(1),\qquad
\frac{a}{v_V(a)}=\log a+o(1),
\]

and hence

\[
v_M(a)-v_V(a)\sim \frac{a\log(3/2)}{(\log a)^2}>0.
\]

Thus the speed minimizing **absolute search-time variance** is higher than the mean-optimal speed for weak capture but lower for strong capture. No assertion is made about uniqueness of a finite intermediate reactivity at which their order changes, nor about uniqueness of the variance minimizer at arbitrary intermediate reactivities.

## Assumptions and scope

The particle occupies \([-L,L]\), moves with velocity \(\pm v_{\rm phys}\), reverses direction at independent exponential waiting times of rate \(\lambda>0\), and remains attached to a hard boundary until its orientation reverses. The target at the origin absorbs independently on each crossing with probability \(1-e^{-k/v_{\rm phys}}\), where \(k>0\) is the point-sink absorption strength. The initial position is uniform in \((-L,L)\), and each initial orientation has probability \(1/2\). Time is in units \(\lambda^{-1}\), and the dimensionless parameters are \(v=v_{\rm phys}/(\lambda L)\) and \(a=k/(\lambda L)\). These are the exact conventions of Jeon--Go--Kim [1]. The theorem concerns the mean and **unstandardized** variance over the full absorption time, not variance divided by squared mean, and varies \(v\) at fixed \(a\).

Set \(q(z)=(e^z-1)^{-1}\), \(Q(z)=q(z)(1+q(z))\), and \(z=a/v\). The established moment identities [1, Eqs. (28), (113)] are

\[
m_a(v)=\frac12+\frac{3}{2v}+\frac{2}{3v^2}+q(z)\left(1+\frac2v\right),
\]

\[
\begin{aligned}
s_a^2(v)={}&\frac34+\frac2v+\frac{37}{12v^2}+\frac5{2v^3}+\frac{28}{45v^4}\\
&+q(z)\left(1+\frac2v+\frac4{v^2}+\frac8{3v^3}\right)
+Q(z)\left(1+\frac2v\right)^2.
\end{aligned}
\]

These two moment identities are prior work, not findings claimed here.

## Proof

**1. Existence and uniqueness for the mean.** Both objective functions tend to infinity as \(v\downarrow0\) and as \(v\to\infty\) for each fixed \(a>0\), so global minimizers exist. Let \(t=1/v\), \(z=at\). Since \(q'(z)=-Q(z)\) and \(q''(z)=Q(z)(1+2q(z))\), direct differentiation gives

\[
\frac{d^2m_a(1/t)}{dt^2}=\frac43+a Q(z)\{(a+2z)\coth(z/2)-4\}.
\]

For every \(z>0\), \(z\coth(z/2)>2\), so the bracket is strictly positive. Thus the mean is strictly convex in \(t>0\); its derivative runs from negative to positive, and its minimizing \(t\), equivalently \(v\), is unique.

**2. Coercive weak-reactivity bounds.** The elementary hyperbolic inequalities

\[
q(z)\ge z^{-1}-\tfrac12,\qquad
Q(z)\ge z^{-2}-\tfrac1{12}\quad(z>0)
\]

follow from \(\coth x\ge1/x\) and from the fact that \(x^{-2}-\sinh^{-2}x\) decreases from \(1/3\) to \(0\). To see the latter, differentiate: the required sign follows from \(\sinh^3x>x^3\cosh x\); that inequality follows by differentiating \(3\log(\sinh x/x)-\log\cosh x\), reducing positivity to \(y(2+\cosh y)>3\sinh y\), whose derivative is \(2\sinh(y/2)[y\cosh(y/2)-2\sinh(y/2)]>0\).

Substituting the inequalities into the two exact moment formulas yields, globally,

\[
m_a(v)\ge\frac2a+\frac va+\frac{2}{3v^2}-\frac12
\]

and

\[
s_a^2(v)\ge\frac4{a^2}+\frac{4v}{a^2}+\frac8{3av^2}.
\]

The second bound follows by expanding the positive-coefficient expression

\[
\frac16+\frac{2}{3v}+\frac3{4v^2}+\frac7{6v^3}+\frac{28}{45v^4}
+\frac{v+2+4/v+8/(3v^2)}a+\frac{v^2+4v+4}{a^2}.
\]

Consequently, for \(\varepsilon=a^{1/3}\), comparison with the trial choice \(v=c\varepsilon\) confines **every** minimizing value of \(s=v/\varepsilon\) to a compact subset of \((0,\infty)\), uniformly for sufficiently small \(a\).

**3. Sharp weak-reactivity splitting.** On every compact interval \(s\in(0,\infty)\), Taylor expansion of \(q(a/v)\) and \(Q(a/v)\), including two derivatives in \(s\), gives

\[
\begin{aligned}
\varepsilon^2\{m_{\varepsilon^3}(\varepsilon s)-2\varepsilon^{-3}\}
 &= f(s)+\varepsilon g(s)+O(\varepsilon^2),\\
\varepsilon^5\{s_{\varepsilon^3}^2(\varepsilon s)-4\varepsilon^{-6}\}
 &=4f(s)+\varepsilon h(s)+O(\varepsilon^2),
\end{aligned}
\]

with

\[
f(s)=s+\frac2{3s^2},\quad g(s)=\frac1{2s},\quad
h(s)=s^2+\frac4s+\frac{28}{45s^4}.
\]

The strictly convex \(f\) has its sole minimizer \(c=(4/3)^{1/3}\) and \(f''(c)=4/c^4\). Coercivity in Step 2 plus uniform \(C^2\) expansion gives a sole global minimizer for each objective for sufficiently small \(\varepsilon\). By the implicit function theorem, the minimizing \(s\) has first perturbative shifts \(-g'(c)/f''(c)=c^2/8\) for the mean and \(-h'(c)/(4f''(c))=c^2/5\) for the variance. Multiplication by \(\varepsilon\) proves the two claimed expansions and positive weak-reactivity gap.

**4. Strong-reactivity localization.** Use \(z=a/v\), so \(t=z/a\), and write the variance as \(P(t)+q(z)A(t)+Q(z)B(t)\), where

\[
\begin{aligned}
P(t)&=\tfrac34+2t+\tfrac{37}{12}t^2+\tfrac52t^3+\tfrac{28}{45}t^4,\\
A(t)&=1+2t+4t^2+\tfrac83t^3,\quad B(t)=(1+2t)^2.
\end{aligned}
\]

At the trial point \(z=\log a\), the mean is \(1/2+O((\log a)/a)\) and the variance is \(3/4+O((\log a)/a)\). The globally valid bounds

\[
m_a(a/z)\ge\tfrac12+q(z)+\tfrac{3z}{2a},\qquad
s_a^2(a/z)\ge\tfrac34+2q(z)+\tfrac{2z}{a}
\]

imply that at **every** global minimum, \(z=\log a+O(\log\log a)\) from below and \(z=O(\log a)\) from above. Therefore \(q(z)=O((\log a)/a)\) and \(z/a=o(1)\) throughout the region containing all minimizers.

Differentiating with respect to \(z\), uniformly over that localization region, gives

\[
\begin{aligned}
\partial_z m_a(a/z)&=-e^{-z}(1+o(1))+\frac{3}{2a}+o(a^{-1}),\\
\partial_z s_a^2(a/z)&=-2e^{-z}(1+o(1))+\frac2a+o(a^{-1}).
\end{aligned}
\]

At any minimizing critical point this forces \(ae^{-z_M}\to3/2\), \(ae^{-z_V}\to1\). The mean is already globally uniquely minimized. For the variance all global minima consequently satisfy \(z_V=\log a+o(1)\), where \(\partial_z^2 s_a^2=2e^{-z}(1+o(1))+O(a^{-2})>0\). Thus all variance minima lie in one strictly convex neighborhood and the variance minimizer is unique for all sufficiently large \(a\). Subtracting the two reciprocal-speed formulas gives the stated positive strong-reactivity gap.

## Verification

Run `python3 check.py` using the standard Python library. The checker evaluates the original two moment functions in high-precision decimal arithmetic, solves their first-derivative stationarity equations, checks the predicted low- and high-reactivity scales, and independently verifies moment reconstruction from the geometric sum of first-passage and return times. These are numerical consistency checks; the global and asymptotic conclusions are proved above, not certified by numerical enumeration.

## Relationship to prior work

Jeon, Go and Kim [1] derive the mean [Eq. (28)] and variance [Appendix C, Eq. (113)] of this exact reactive-center model, prove leading mean-optimal asymptotic scales, and discuss the statistical resolution of speed filters. The new statement is a **comparison between two different global optimization criteria**, including the next-order weak-reactivity separation and the opposite strong-reactivity gap. Their known leading mean-optimal scales and the moment formulas are explicitly acknowledged and are not represented as new.

Mercado-Vásquez and Boyer [2] study first-passage fluctuations for a *stochastically gated* center, a different target mechanism with extra transition parameters; their ballistic optimum in the gated model does not imply the present mean-versus-variance reversal for a fixed crossing capture probability. A separately published sticky-wall escape analysis [3] also distinguishes mean- and variance-optimal tumbling rates, but controls a different rate and different boundary capture dynamics; its fixed optimizer ordering does not imply this center-reaction speed reversal.

## Limitations

This proves uniqueness of the variance optimum only for sufficiently small and sufficiently large target reactivity, not for the entire intermediate range. It does not prove uniqueness or locate the possible intermediate crossover. It assumes two-state Poisson tumbling, no translational Brownian noise, sticky hard walls, and uniformly distributed initial positions and orientations. It concerns absolute variance rather than coefficient of variation; numerical values of any intermediate crossing are illustrative only. Novelty remains provisional pending independent literature evaluation, especially in unindexed analytic optimization studies.

## References

[1] E. Jeon, B. Go and Y. W. Kim, *Searching for a partially absorbing target by a run-and-tumble particle in a confined space*, arXiv:2310.04016v1 (first posted 2023-10-06), https://arxiv.org/html/2310.04016v1 ; Physical Review E **109**, 014103 (2024).

[2] G. Mercado-Vásquez and D. Boyer, *First hitting times between a run-and-tumble particle and a stochastically-gated target*, arXiv:2102.11787v1 (2021), https://arxiv.org/abs/2102.11787 ; Physical Review E **103**, 042139 (2021).

[3] *Sharp mean–variance Pareto frontier and relative-risk optimum in sticky active escape*, publicly indexed research record dated 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-mean-variance-pareto-frontier-and-relative-risk-optimum-in--4cc6a1bceac3 (full text not accessible during this comparison; statement compared using indexed scientific summary only).
