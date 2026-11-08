# Unique optimal search and the weak-contraction Ornstein–Uhlenbeck limit under partial resetting

## Finding

A Brownian particle can regain a finite, optimally short target-search time even when each Poissonian reset removes an arbitrarily small fraction of its current displacement, provided the event rate increases appropriately. The exact optimal scaling and limiting search cost are universal. For the process defined below, the optimal rate is unique for every \(0\le a<1\), and

\[
\lim_{a\uparrow1}(1-a)\frac{L^2r_*(a)}D=b_*^2=1.64065482984135052863976\ldots,
\qquad
\lim_{a\uparrow1}\frac{D}{L^2}\min_{r>0}\mathbb E_0\tau_L
=1.99986485198958112393564\ldots.
\]

The universal \(b_*=1.28088049006976077394812\ldots\) uniquely minimizes the mean time to hit level \(1\), starting at \(0\), for the Ornstein–Uhlenbeck diffusion with generator \(\mathcal L_b=\partial_{xx}-b^2x\partial_x\). The full, suitably rescaled target-search objective converges locally uniformly to this limiting objective.

## Assumptions and scope

Fix \(D,L>0\), a reset multiplier \(a\in[0,1)\), and a reset rate \(r>0\). Between independent rate-\(r\) Poisson events the position solves \(dX_t=\sqrt{2D}\,dW_t\); each event instantaneously replaces \(X_t\) by \(aX_t\). The initial position is \(X_0=0\). The target is the positive level \(L\), absorbing at the first continuous hitting time \(\tau_L\). A jump cannot overshoot this target from a point strictly below it because \(a\ge0\).

Write \(\beta=L\sqrt{r/D}\), \(\epsilon=1-a\), and \(F_a(\beta)=r\mathbb E_0\tau_L\). The known exact positive-rescaling formula of Biroli et al. [1, equations (36), (42), (44)–(45)] is

\[
F_a(z)=\sum_{n=1}^{\infty}\frac{C_{2n}(a)z^{2n}}{(2n)!}
+R(a)\sum_{n=0}^{\infty}\frac{C_{2n+1}(a)z^{2n+1}}{(2n+1)!},
\]

\[
C_{2n}(a)=\prod_{j=1}^{n-1}(1-a^{2j}),\quad
C_{2n+1}(a)=\prod_{j=0}^{n-1}(1-a^{2j+1}),\quad
R(a)=\frac{\prod_{j=1}^{\infty}(1-a^{2j})}{\prod_{j=0}^{\infty}(1-a^{2j+1})}.
\]

Empty products equal one, and \(R(0)=1\). For all admissible \(a\), the objective is \(D\mathbb E_0\tau_L/L^2=F_a(\beta)/\beta^2\). Source [1] supplies this starting identity, not the new uniqueness proof or the singular optimized limit.

## Proof

**1. Uniqueness at every fixed partial-reset multiplier.** Set \(F_a(z)=\sum_{k\ge1}c_k(a)z^k\). All coefficients are strictly positive. In particular \(c_1(a)=R(a)>0\), \(c_2(a)=1/2\), and \(c_3(a)=R(a)(1-a)/6>0\). The derivative of \(F_a(z)/z^2\) has the sign of

\[
\frac{zF_a'(z)-2F_a(z)}z=-R(a)+\sum_{k\ge3}(k-2)c_k(a)z^{k-1}.
\]

This is strictly increasing on \((0,\infty)\), begins negative, and tends to infinity (even the \(k=3\) contribution suffices). Thus there is precisely one stationary point, with negative derivative before it and positive derivative after it. The first term of the objective diverges as \(R(a)/z\) near zero, and its positive fourth-degree term forces divergence as \(z\to\infty\). Hence the stationary point is the unique global minimizer. The map between \(z=\beta\) and \(r\) is bijective, proving uniqueness of \(r_*(a)\).

**2. Weak-contraction coefficients.** Let \(q=a^2\). The standard \(q\)-gamma identity [4, equations 5.18.4 and 5.18.10] gives, for \(0<a<1\),

\[
R(a)=\frac{\Gamma_{a^2}(1/2)}{\sqrt{1-a^2}},\qquad
\lim_{a\uparrow1}\sqrt{1-a}\,R(a)=\sqrt{\pi/2}.
\]

For each fixed positive integer \(n\), elementary product limits yield

\[
\frac{C_{2n}(a)}{\epsilon^{n-1}}\longrightarrow 2^{n-1}(n-1)!,\qquad
\frac{C_{2n+1}(a)}{\epsilon^n}\longrightarrow(2n-1)!!,
\]

with \((-1)!!=1\). The inequalities \(0\le1-a^m\le m\epsilon\) imply coefficient bounds \(C_{2n}\le(2\epsilon)^{n-1}(n-1)!\) and \(C_{2n+1}\le\epsilon^n(2n-1)!!\). Since \(\sqrt\epsilon R(a)\) is bounded near one, these bounds dominate both rescaled power series and their derivatives on compact sets by convergent entire series.

**3. Convergence of the complete objective.** With \(b=\sqrt\epsilon\,\beta\), the rescaled objective

\[
\Phi_a(b):=\frac{F_a(b/\sqrt\epsilon)}{(b/\sqrt\epsilon)^2}
=\frac{\epsilon F_a(b/\sqrt\epsilon)}{b^2}
\]

converges locally uniformly on \(b>0\) (as do its derivatives) to \(\Phi(b)=F_*(b)/b^2\), where

\[
F_*(b)=\sum_{n=1}^{\infty}\frac{2^{n-1}(n-1)!}{(2n)!}b^{2n}
+\sqrt{\frac\pi2}\sum_{n=0}^{\infty}\frac{b^{2n+1}}{(2n+1)2^nn!}.
\]

**4. Identification of the Ornstein–Uhlenbeck boundary problem.** The finite mean \(u_b(x)\) of first hitting one, for the generator \(u_b''-b^2xu_b'\), solves \(u_b''(x)-b^2xu_b'(x)=-1\), \(u_b(1)=0\), with the nonexplosive solution at the negative natural boundary. Integrating the first-order equation for \(u_b'\) gives

\[
\Phi(b)=u_b(0)=\int_0^1e^{b^2y^2/2}\left(\int_{-\infty}^{y}e^{-b^2z^2/2}\,dz\right)dy.
\]

To verify equality with the series in Step 3, split the inner integral at zero. Its negative-half-line contribution is \(\sqrt{\pi/2}/b\) and generates the odd series after expanding the outer exponential. The positive-side double integral expands using \(\int_0^1(1-t^2)^n\,dt=2^{2n}(n!)^2/(2n+1)!\) and generates the even series. All interchanges follow by nonnegative terms or uniform convergence on finite intervals. Thus this is an equality of complete functions, not merely a diffusion heuristic.

**5. The unique limiting optimum and convergence of minimizers.** The same positive-coefficient derivative argument applied to \(F_*\) proves that \(\Phi\) has a unique minimizer \(b_*>0\). To exclude escape of the finite-\(a\) minimizers as \(a\uparrow1\), use the two positive terms of the objective to obtain, for every \(b>0\),

\[
\Phi_a(b)\ge\frac{\sqrt\epsilon\,R(a)}b,
\qquad
\Phi_a(b)\ge\frac{1+a}{24}b^2.
\]

Both inequalities are valid simultaneously. For \(a\) sufficiently near one, \(\sqrt\epsilon R(a)\) is bounded below by a positive constant, while \(\Phi_a(1)\) is bounded above by locally uniform convergence. Consequently every minimizing \(b_a=\sqrt\epsilon\,\beta_*(a)\) belongs to one fixed compact subinterval of \((0,\infty)\). Every accumulation point minimizes \(\Phi\) by uniform convergence; uniqueness forces \(b_a\to b_*\). Substituting \(r_*(a)=D\beta_*(a)^2/L^2\) yields the asserted rate limit, and taking objective values yields the asserted optimized-time limit.

## Verification

A standalone `checker.py` evaluates the exact finite-\(a\) series and its derivatives at 55-digit precision, solves each scalar first-order condition by bisection, and compares the limiting power series against an independent Gaussian-integral evaluation of the Ornstein–Uhlenbeck mean hitting time. It passed 33 assertions across six fixed multipliers and four independent limiting-integral values. The numerical root is

\[
b_*=1.28088049006976077394812111141\ldots,\quad
b_*^2=1.64065482984135052863976377311\ldots,
\quad\Phi(b_*)=1.99986485198958112393563664933\ldots.
\]

For example, at \(a=0.99\), the computed optimum is \(\sqrt{1-a}\,\beta_*=1.284590667453147\ldots\) and the minimized dimensionless mean time is \(1.995421058878432\ldots\). These calculations corroborate finite parameter values; uniqueness, uniform convergence, and limit exchange are established in the proof rather than inferred from tests. Numerical decimals are approximations, not certified interval enclosures.

## Relationship to prior work

Biroli et al. [1] derive the exact series for \(\mathbb E_0\tau_L\) and graph its apparent optimum, but do not establish a rigorous uniqueness theorem or the joint weak-contraction/optimized-rate limit with its universal constants. Pierce [2] formulates a proportional-reset first-passage equation without solving this optimization problem. Tal-Friedman, Roichman, and Reuveni [3] prove a weak-reset Gaussian limit for stationary **position distributions**, not this absorbing target-search problem. The limiting Ornstein–Uhlenbeck mean hitting-time integral is standard; the new statement is its rigorous appearance as the optimized singular limit of the published partial-reset objective, including convergence of the global minimizers. Existing results about complete resetting or independent reset-position draws do not imply this statement without analyzing the history-dependent partial-reset mechanism.

## Limitations

The theorem requires one-dimensional drift-free Brownian motion, independent Poisson reset epochs, deterministic \(a\in[0,1)\), and a fixed positive target with initial position zero. It does not cover negative multipliers, finite-rate \(a=1\), resetting costs, state-dependent event rates, or any uniform rate of convergence in \(a\). It uses the previously established exact mean-first-passage series, and an unindexed mathematical derivation of the same optimized singular limit remains a potential prior-art risk. Independent validation has not been performed.

## References

1. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar, and G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387v1 (first public 2024-06-12), https://arxiv.org/html/2406.08387v1, Sec. III.1.
2. J. K. Pierce, *An advection-diffusion process with proportional resetting*, arXiv:2204.07215v1 (2022), https://arxiv.org/html/2204.07215v1, Sec. IV.2.
3. O. Tal-Friedman, Y. Roichman, and S. Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363v2 (2022), https://arxiv.org/html/2205.03363v2, Secs. II and III.
4. NIST Digital Library of Mathematical Functions, Sec. 5.18(ii), equations 5.18.4 and 5.18.10, https://dlmf.nist.gov/5.18.
