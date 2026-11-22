# Exact cooperation basin and universal critical decay in a feedback–punishment game

## Finding

For the infinite-population **global state-feedback public-goods replicator** of Wang, Chen and Szolnoki [1], the entire strictly interior phase portrait has an explicit initial-condition threshold: either all defectors ultimately prevail or all defectors vanish. The exact dividing curve is a one-variable maximization of two decaying exponentials, and every trajectory on that curve converges to the *same* marginally stable full-contribution mixture. On the dividing curve, the residual defector share has a universal inverse-square law, despite generic full-contribution trajectories having exponential relaxation.

Here is a precise statement. Let the group size be an integer \(n\ge2\), contribution cost \(c>0\), baseline multiplication factor \(r_0>1\), global feedback \(k>0\), punishment fine \(\beta>0\), and punishment cost \(0<\gamma<\beta\), with \(r_0+k<n\). Put
\[
 a=\frac{c(n-r_0)}n,\quad b=\frac{ck}{n},\quad h=\gamma(n-1),\quad B=(\beta+\gamma)(n-1),\quad A=a-b>0,\quad D=\beta(n-1)-A.
\]
For strictly positive initial cooperator, defector and punisher shares \(x_0,y_0,z_0\) summing to one, define \(p_0=x_0+z_0\in(0,1)\) and \(q_0=z_0/p_0\in(0,1)\). The critical punisher share on the full-contribution edge is \(q_*=A/[\beta(n-1)]\).

If \(q_*\ge1\), or if \(q_*<1\) but \(q_0\le q_*\), then every such trajectory converges to complete defection. Otherwise \(0<q_*<q_0<1\); set
\[
 s_* =\frac1h\log\!\left(\frac{q_0D}{(1-q_0)A}\right)>0
\]
and
\[
 H(q_0)= (1-q_0)\left[\frac ba+\left(1-\frac ba\right)e^{-as_*}\right]
 +q_0\left[\frac{b+B}{a+h}+\left(1-\frac{b+B}{a+h}\right)e^{-(a+h)s_*}\right].
\]
Then \(H(q_0)>1\), and the following exhaustive sharp trichotomy holds:

1. If \(p_0<1/H(q_0)\), then \((x(t),y(t),z(t))\to(0,1,0)\).
2. If \(p_0>1/H(q_0)\), then \(y(t)\to0\) exponentially and \((x(t),z(t))\) tends to a full-contribution mixture with a punisher fraction strictly above \(q_*\).
3. If \(p_0=1/H(q_0)\), then \((x(t),y(t),z(t))\to(1-q_*,0,q_*)\) with the exact universal limits
\[
 \boxed{\lim_{t\to\infty}t^2y(t)=\frac{2\beta}{\gamma A D},\qquad
 \lim_{t\to\infty}t(z(t)-q_*)=\frac{2}{\beta(n-1)}.}
\]
The limits in the last line are **independent of the initial point on the separating curve**. In particular, the border itself approaches full contribution, but with algebraic rather than exponential relaxation. This is a global interior classification; it makes no claim about mutation, finite-population fixation or empirical behavior.

## Assumptions and scope

Let \(x\), \(y=1-x-z\), and \(z\) denote frequencies of ordinary contributors, defectors and contributing punishers. The deterministic equations are exactly the source's global-feedback system (7):
\[
 \dot x=xy[-a+b(x+z)+Bz],\qquad
 \dot z=zy[-a+b(x+z)+Bz-h].
\]
All parameters and strictly interior data satisfy the inequalities in the Finding; thus \(a>b>0\), \(h>0\), and \(B>h\). In the case \(D\le0\), there is no cooperating basin in the open simplex. In the case \(D>0\), \(q_*\in(0,1)\). The threshold \(H\) applies only where \(q_0>q_*\); outside that region complete defection follows without evaluating it.

## Proof

**1. A nonsingular exposure coordinate.** Write \(p=x+z\), \(q=z/p\) and let
\[s(t)=\int_0^t[1-p(\tau)]\,d\tau.\]
While the trajectory is interior, \(s'(t)=1-p(t)>0\), and a direct subtraction of the two replicator log-derivatives gives
\[
 \frac{dq}{ds}=-h q(1-q),\qquad
 \frac{dp}{ds}=p[-a+bp+(Bp-h)q].
\]
Thus the logistic composition is explicit:
\[
 q(s)=\frac{q_0e^{-hs}}{1-q_0+q_0e^{-hs}}.
\]

**2. Exact linearizing identity.** Define \(R(s)=1/p(s)\), \(M(s)=e^{-as}(1-q_0+q_0e^{-hs})\). Since \(R'=(a+hq)R-(b+Bq)\), differentiation gives
\[
 \frac{d}{ds}[M(s)R(s)]=-e^{-as}\big[b(1-q_0)+(b+B)q_0e^{-hs}\big].
\]
Integration yields the exact identity
\[
 R(s)-1=\frac{R_0-F(s)}{M(s)},\quad R_0=1/p_0,
\]
where
\[
 F(s)=(1-q_0)\left[\frac ba+\left(1-\frac ba\right)e^{-as}\right]
 +q_0\left[\frac{b+B}{a+h}+\left(1-\frac{b+B}{a+h}\right)e^{-(a+h)s}\right].
\]
In particular \(F(0)=1<R_0\). The physical evolution can continue for all exposure times \(s\ge0\) while \(R(s)>1\). If \(R\) first reaches one at a finite \(s_b\), then the corresponding physical trajectory approaches the invariant full-contribution edge as \(t\to\infty\); it cannot cross that edge in finite physical time.

**3. Exact maximization and the basin split.** Set \(A=a-b>0\), \(D=b+B-a-h=\beta(n-1)-A\). Differentiating gives
\[
 F'(s)=-(1-q_0)A e^{-as}+q_0D e^{-(a+h)s}.
\]
If \(D\le0\), or if \(D>0\) and \(q_0\le A/(A+D)=q_*\), then \(F'(s)<0\) for all \(s>0\). Consequently \(F(s)\le1<R_0\) and the trajectory never reaches the full-contribution edge. Since \(M(s)\to0\), \(R_0-F(s)\) stays positive, and the exact identity gives \(p\to0\), hence complete defection.

If \(D>0\) and \(q_0>q_*\), then \(F'(0)>0\), and its unique positive zero is \(s_*\) as stated. The function rises strictly from one to \(F(s_*)=H(q_0)>1\) and then decreases. When \(R_0>H\), \(R(s)>1\) for every \(s\ge0\), and \(p\to0\) as above. When \(1<R_0<H\), a unique first root \(s_b\in(0,s_*)\) of \(R_0=F(s_b)\) exists, and \(R(s_b)=1\) with a simple zero of \(R-1\). Hence \(p\to1\) and \(q\to q(s_b)>q(s_*)=q_*\); the linear simple zero and \(ds/dt=1-p\) give exponential convergence.

**4. Critical inverse-square law.** At \(R_0=H=F(s_*)\), \(F'(s_*)=0\). The strict maximum has
\[
 F''(s_*)=-h(1-q_0)A e^{-as_*}<0.
\]
Using the identity in Step 2, as \(s\uparrow s_*\),
\[
 1-p(s)=K(s_*-s)^2+O((s_*-s)^3),
 \qquad K=\frac{-F''(s_*)}{2M(s_*)}
 =\frac{hAD}{2(A+D)}>0.
\]
Because \(ds/dt=1-p\), integration of the last expansion proves \(s_*-s(t)\sim1/(Kt)\), and thus \(t^2y(t)\to 1/K=2\beta/(\gamma A D)\). The logistic expression gives \(q(s_*)=A/(A+D)=q_*\) and
\[
 q(s)-q_* =h q_*(1-q_*)(s_*-s)+O((s_*-s)^2).
\]
Therefore \(t[q(t)-q_*]\to 2/(A+D)=2/[\beta(n-1)]\). Since \(z=pq\) and \(t(1-p)\to0\), the same limit holds for \(t[z(t)-q_*]\). This proves the trichotomy and both universal coefficients.

**5. Exact admissible example.** Take \(n=5\), \(c=1\), \(r_0=2\), \(k=1\), \(\beta=1/5\), \(\gamma=1/10\). Then \(a=3/5\), \(b=1/5\), \(h=2/5\), \(A=D=2/5\), and \(q_*=1/2\). With \(q_0=3/4\),
\[
 s_*=\frac52\log3,\qquad
 H=\frac{17}{15}+\frac{1}{45\sqrt3},\qquad
 p_{\mathrm{crit}}=\left(\frac{17}{15}+\frac{1}{45\sqrt3}\right)^{-1}.
\]
Thus \(p_0=4/5\) is in the defection basin, \(p_0=9/10\) is in the contribution basin, and exactly at \(p_{\mathrm{crit}}\) one has \(t^2y(t)\to25\) and \(t[z(t)-1/2]\to5/2\).

## Verification

The enclosed standalone `CHECKER.py` symbolically differentiates the exact first integral and the proposed threshold, verifies the unique maximizer and the critical coefficients, and checks the admissible rational example. Its execution is a check of the displayed calculations, not a replacement for the global arguments above. The proof is analytic for every allowed group size and positive parameter choice, and does not rest on finite sampling.

## Relationship to prior work

Wang, Chen and Szolnoki [1], Sections II–III and Appendices A–C, derive the replicator system and the local stability threshold on its full-contribution edge, and illustrate basin areas numerically. Their critical punisher share agrees with \(q_*\) above, but the accessible paper does not present the global initial-condition separatrix, its exact two-exponential maximization, or the inverse-square decay and universal coefficient at its marginal branch. The earlier literature on punishment-driven transitions [2] addresses transition phenomena and hysteresis in a different finite-population game, not the present deterministic integrable flow. General replicator reductions and Riccati equations are standard techniques; the new content is their specific complete global application, exact separating curve, and the resulting critical decay law in this model.

## Limitations

The conclusions are for the infinite-population deterministic replicator with **global**, not local, state feedback, positive punishment cost, and strictly interior initial frequencies. Endpoints such as initially absent contributors/punishers, mutation, network structure, demographic noise, and switching environments are excluded. The coefficient on the critical curve depends on the model parameters, but not on where that critical curve is entered. No empirical claim is made and historical priority is not independently certified.

## References

[1] Q. Wang, X. Chen, A. Szolnoki, *Evolutionary dynamics in state-feedback public goods games with peer punishment*, arXiv:2504.16659v1 (first public April 23, 2025). https://arxiv.org/pdf/2504.16659

[2] A. Hintze, C. Adami, *Punishment in public goods games leads to meta-stable phase transitions and hysteresis*, Physical Biology 12 (2015), 046005. https://doi.org/10.1088/1478-3975/12/4/046005
