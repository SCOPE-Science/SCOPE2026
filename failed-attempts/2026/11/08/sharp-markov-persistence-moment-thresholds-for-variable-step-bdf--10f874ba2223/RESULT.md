# Sharp Markov-persistence moment thresholds for variable-step BDF2 on reciprocal random meshes

## Finding
Fix a step-ratio contrast \(r\ge1\), a persistence probability \(0\le p<1\), and any nonzero deterministic startup difference \(d=y_1-y_0\). Run variable-step BDF2 on \(y'=0\) with positive time steps satisfying \(h_n/h_{n-1}=R_n\) for \(n\ge2\). The stationary symmetric two-state Markov chain \(R_n\in\{r,r^{-1}\}\) repeats its current state with probability \(p\) and changes state with probability \(1-p\). Initial states have probability \(1/2\) each. Define
\[
a=\frac{r^2}{1+2r},\qquad b=\frac1{r(r+2)},\qquad c=1+\sqrt2.
\]
The BDF2 values converge to a finite random limit \(Y_\infty\) almost surely for every \(r\ge1\), \(0\le p<1\). For every real \(s>0\), its *startup amplification* \(Z=(Y_\infty-y_0)/d\), which is positive almost surely, has the complete moment classification
\[
\mathbb E[Z^s]<\infty\quad\Longleftrightarrow\quad
\begin{cases}
\text{always},&1\le r\le c,\\
p<p_s(r),&r>c,
\end{cases}
\qquad
p_s(r)=\frac{1-(ab)^s}{a^s+b^s-2(ab)^s}.
\]
At the boundary \(p=p_s(r)\), the moment is infinite. For \(r>c\), \(0<p<1\) the trajectory converges almost surely but has at least one divergent finite-order moment. In contrast, deterministic alternation \(p=0\) has bounded startup amplification at every \(r\ge1\). The model is a zero-test-equation, infinite-iteration statement, not a classical fixed-terminal-time convergence claim.

In particular, at \(r=3\),
\[
a=9/7,\quad b=1/15,\quad p_1(3)=24/31,\quad p_2(3)=171/283.
\]
Thus \(p=7/10\) gives finite mean amplification but infinite second moment, despite almost-sure convergence of the discretization.

## Assumptions and scope
The time grid starts from any \(h_1>0\). Conditional on the initial equally likely ratio state, subsequent ratio transitions follow the specified time-homogeneous Markov rule, independently of the deterministic \(y_0,y_1\). The BDF2 recurrence uses exact arithmetic; no physical finite-time horizon, truncation errors, or roundoff errors are asserted. Because time steps are formed recursively from ratios, the total physical time may be unbounded and the mesh need not form a refinement of a fixed interval. These facts are essential limits of the interpretation. The symbol \(s\) denotes any positive real moment exponent, not an integer-only moment.

For \(p=0\), alternate ratios deterministically with a random initial phase. For \(0<p<1\), the chain is stationary and ergodic. The excluded case \(p=1\) has an absorbing high-ratio state and fails almost-sure finiteness when \(r>c\).

## Proof
**1. Exact BDF2 reduction.** The variable-step BDF2 formula for \(y'=0\) reads
\[
\frac{1+2R_n}{1+R_n}\frac{y_n-y_{n-1}}{h_n}
-\frac{R_n}{1+R_n}\frac{y_{n-1}-y_{n-2}}{h_{n-1}}=0.
\]
Writing \(\Delta_n=y_n-y_{n-1}\) and using \(h_n=R_nh_{n-1}\), we obtain exactly
\[
\Delta_n=q(R_n)\Delta_{n-1},\qquad q(u)=\frac{u^2}{1+2u}.
\]
On the two ratio states this multiplier is \(a\) or \(b\). Therefore, defining \(Q_j=q(R_{j+1})\),
\[
y_n=y_0+d\sum_{k=0}^{n-1}\prod_{j=1}^{k}Q_j,
\qquad
Z=\sum_{k=0}^{\infty}\prod_{j=1}^{k}Q_j,
\]
where empty products equal one.

**2. Almost-sure convergence.** Direct multiplication gives
\[
ab=\frac{r}{(1+2r)(r+2)}<1\quad(r\ge1).
\]
For \(0<p<1\) the finite-state ergodic theorem shows
\[
\lim_{n\to\infty}\frac1n\log\Big(\prod_{j=1}^{n}Q_j\Big)
=\frac12\log(ab)<0\quad\text{almost surely}.
\]
For \(p=0\), deterministic alternation gives the same limit by pairing successive multipliers. Thus the positive series defining \(Z\) converges almost surely and \(Y_\infty=y_0+dZ\) exists.

**3. A moment criterion proved without an external perpetuity theorem.** For \(s>0\), define the positive matrix
\[
M_s=\begin{pmatrix}pa^s&(1-p)a^s\\(1-p)b^s&pb^s\end{pmatrix}.
\]
For each initial ratio state \(i\in\{+,-\}\), the \(s\)-th moment of a \(k\)-fold multiplier product is a corresponding component of \(M_s^{k-1}(a^s,b^s)^{\mathsf T}\). If \(\rho(M_s)<1\), these moments decay exponentially, and the positive series for \(Z\) converges in \(L^s\): for \(s\ge1\) apply Minkowski to its partial sums; for \(0<s\le1\) apply \((u+v)^s\le u^s+v^s\). This proves sufficiency.

For necessity, condition on the first Markov state and let \(Z_i\) be the resulting series. The distributional relation is \(Z_i=1+q_iZ_J\), where \(q_+=a\), \(q_-=b\) and \(J\) has transition probabilities given by the appropriate row of the Markov matrix. If both conditional \(s\)-th moments \(m_i\) were finite, strict positivity would give \(m>M_sm\) componentwise. For \(0<p<1\), \(M_s\) is strictly positive, so multiplication by its positive left Perron eigenvector yields \(\rho(M_s)<1\). This contradicts \(\rho(M_s)\ge1\). At \(p=0\) the same conclusion follows using the strictly positive left Perron vector of the irreducible nonnegative two-cycle matrix. Since both Markov states have positive initial probability, the unconditional moment is finite if and only if \(\rho(M_s)<1\).

**4. Exact frontier.** The identity
\[
\det(I-M_s)=1-(ab)^s-p\big(a^s+b^s-2(ab)^s\big)
\]
is linear in \(p\). When \(1\le r\le1+\sqrt2\), \(a\le1\), \(b<1\); for every \(p<1\) the irreducible Markov switching ensures \(\rho(M_s)<1\) (at \(p=0\) use \(\sqrt{ab}<1\)). When \(r>1+\sqrt2\), we have \(a>1>b\) and \(ab<1\). At \(p=0\), \(\rho(M_s)=(ab)^{s/2}<1\); as \(p\uparrow1\), \(\rho(M_s)\to a^s>1\). The displayed determinant has exactly one zero in \((0,1)\), because \(a^s+b^s-2(ab)^s>0\), and this is precisely \(p_s(r)\). Continuity and Perron-Frobenius therefore give \(\rho(M_s)<1\) exactly when \(p<p_s(r)\). At equality the strict-moment argument proves divergence. Finally, for fixed \(0<p<1\) and \(r>1+\sqrt2\), arbitrarily long repetitions of the amplifying state force \(\mathbb E[Z^s]=\infty\) for sufficiently large \(s\) (e.g. choose \(s\) such that \(pa^s>1\)).

**5. Exact instance.** Setting \(r=3\) yields \(a=9/7\), \(b=1/15\), \(ab=3/35\), and substitution into the frontier gives \(p_1=24/31\), \(p_2=171/283\). Since \(171/283<7/10<24/31\), the example follows. No finite numerical test is used in these infinite-iteration arguments.

## Verification
Run `python3 checker.py` using Python standard library. Its exact rational tests establish the BDF2 difference identity at several time-step patterns and the rational frontiers in the example; its Perron-root tests check classification signs over several nontrivial rational contrasts and real moment exponents. These are checks, not substitutes for the preceding proof.

## Relationship to prior work
Söderlind, Fekete and Faragó (2018), Section 4, give the variable-step BDF2 extraneous recursion and analyze zero stability on smoothly varying meshes. Li and Liao (2022), Section 2, prove a different mesh-robust, fixed-horizon stability bound with a startup-derivative term on arbitrary grids. Yue, Liao and Liu (2024) extend that framework to deferred-correction schemes and report finite-grid random-mesh tests. These works establish important general stability principles but do not supply the present Markov-persistence, all-real-moment boundary for the unscaled infinite-step startup amplification. The Perron-matrix technique for Markov multiplicative recursions is standard; no general priority for it is asserted here.

## Limitations
The exact formula concerns the deliberately specified symmetric reciprocal-ratio chain and the scalar zero test equation. It does not establish instability of variable-step BDF2 for fixed terminal-time ODE integration, refute mesh-robust estimates with normalized startup derivatives, or yield error bounds for nonzero right-hand sides. No finite-precision or truncation error is included. Results for other ratio distributions, adaptive controllers or fixed-horizon conditioned grids require separate study. Publication-precedence checks were conducted for the directly relevant primary texts, but an equivalent Markov-perpetuity specialization may exist outside the inspected corpus.

## References
1. G. Söderlind, I. Fekete, I. Faragó, *On the zero-stability of multistep methods on smooth nonuniform grids*, BIT Numerical Mathematics **58** (2018), 1125–1143, https://doi.org/10.1007/s10543-018-0716-y (public version published July 10, 2018).
2. Z. Li, H.-l. Liao, *Stability of variable-step BDF2 and BDF3 methods*, arXiv:2201.00527 (first posted January 3, 2022), https://arxiv.org/abs/2201.00527.
3. J. Yue, H.-l. Liao, N. Liu, *Mesh-robust stability and convergence of variable-step deferred correction methods based on the BDF2 formula*, arXiv:2402.06129 (first posted February 9, 2024), https://arxiv.org/abs/2402.06129.
