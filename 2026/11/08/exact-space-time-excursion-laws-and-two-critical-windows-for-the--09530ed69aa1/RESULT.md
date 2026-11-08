# Exact space-time excursion laws and two critical windows for the Fibonacci bimodal comparison map

## Finding

Fix \(0<\lambda<1\). For the specific auxiliary piecewise-affine interval map \(T_\lambda\) defined below, sampling uniformly in a natural four-level base yields **exact first-return and maximum-excursion distributions for every parameter**, and two different near-critical scaling windows: the time window has width \(N^{-1/2}\), while the height window has width \(L^{-1}\). The theorem is about the auxiliary comparison map, **not** about the original Fibonacci bimodal map or its induced system.

Write
\[
\alpha_\lambda=\frac{\lambda^4(1+\lambda^2-2\lambda^3)}{1-\lambda^4},\qquad
r_\lambda(z)=\frac{1-\sqrt{1-4\lambda(1-\lambda)z}}{2\lambda},\qquad q=\frac{1-\lambda}{\lambda}.
\]
For the first positive return \(\tau\) and maximum excursion height \(M\) specified below, their exact laws are
\[
\mathbb E_\lambda[z^\tau;\tau<\infty]
=z\left(1-\alpha_\lambda+\alpha_\lambda\frac{(1-\lambda)r_\lambda(z)}{1-\lambda r_\lambda(z)}\right),\quad 0\le z\le1,
\]
\[
\Pr_\lambda(M\ge L)=\alpha_\lambda\frac{q^2-1}{q^{L+1}-1},\quad L\ge1,
\qquad
\Pr_\lambda(\tau=\infty)=\Pr_\lambda(M=\infty)
=\alpha_\lambda\frac{(2\lambda-1)_+}{\lambda^2}.
\]
At \(\lambda=1/2\), the quotient in the maximum law is interpreted continuously: \(\Pr(M\ge L)=2/[15(L+1)]\). The exact finite-return law at this critical value is
\[
\Pr(\tau=1)=\frac{14}{15},\qquad
\Pr(\tau=n)=\frac{2}{15}\frac{\binom{2n}{n}}{4^n(2n-1)}\quad(n\ge2),
\]
with \(\Pr(\tau>n)\sim2/(15\sqrt{\pi n})\). For \(\lambda<1/2\), \(\mathbb E\tau=1+\alpha_\lambda/(1-2\lambda)\); at criticality return is almost sure but the mean is infinite.

For every fixed \(u\in\mathbb R\), the **temporal crossover** is
\[
\boxed{\lim_{N\to\infty}\sqrt N\,\Pr_{1/2+u/\sqrt N}(\tau>N)
=\frac{2}{15}\left[\frac{e^{-4u^2}}{\sqrt\pi}+2u\operatorname{erfc}(-2u)\right].}
\]
The distinct **spatial crossover** is
\[
\boxed{\lim_{L\to\infty}L\,\Pr_{1/2+u/L}(M\ge L)
=\begin{cases}\displaystyle\frac{8u}{15(1-e^{-4u})},&u\ne0,\\[3pt]\displaystyle\frac{2}{15},&u=0.\end{cases}}
\]
The family parameters are understood to lie in \((0,1)\), which holds eventually for every fixed \(u\).

## Assumptions and scope

Let \(V_j=(\lambda^j,\lambda^{j-1}]\) for integers \(j\ge1\). The reference map, defined up to irrelevant branch endpoints, is
\[
T_\lambda(x)=\begin{cases}
(x-\lambda)/(1-\lambda),&x\in V_1,\\
(x-\lambda^2)/[\lambda(1-\lambda)],&x\in V_2,\\
(x-\lambda^3)/[\lambda^2(1-\lambda)],&x\in V_3,\\
(x-\lambda^4)/[\lambda^2(1-\lambda)],&x\in V_4,\\
(x-\lambda^j)/[\lambda(1-\lambda)],&x\in V_j,\ j\ge5.
\end{cases}
\]
This is the comparison map in Ji and Ma, Section 5.1, **which their paper explicitly notes is not semiconjugate** to the induced map \(F_\lambda\).

Set \(B=\bigcup_{j=1}^4V_j=(\lambda^4,1]\) and draw \(X_0\) with distribution \(\operatorname{Leb}(\cdot\cap B)/(1-\lambda^4)\). Let \(J_k=j\) when \(T_\lambda^k(X_0)\in V_j\), ignoring the null set of ambiguous endpoints. Set \(\tau=\inf\{k\ge1:J_k\le4\}\), with \(\inf\varnothing=\infty\). If \(\tau=1\), put \(M=0\). Otherwise let \(M=\sup\{J_k-4:1\le k<\tau\}\); on an unbounded nonreturning excursion set \(M=\infty\). Every probability refers to the stated **initial Lebesgue sampling**, not an invariant distribution on the infinite partition.

## Proof

**1. Exact level transitions and the entrance law.** On \(V_1,V_2,V_3\) the affine branches cover \((0,1]\); on \(V_4\) the image is \((0,\lambda]\); and on \(V_j\) for \(j\ge5\) it is \((0,\lambda^{j-2}]\). Each is increasing affine, hence a uniform conditional location in one partition interval gives a uniform image over its branch range. In particular, if the current level is \(j\), then the next level \(i\) has probability
\[
\Pr(J_{k+1}=i\mid J_k=j)=
(1-\lambda)\lambda^{i-b_j},\qquad i\ge b_j,
\]
where \(b_j=1\) for \(j\in\{1,2,3\}\), \(b_4=2\), and \(b_j=j-1\) for \(j\ge5\). The conditional uniformity is preserved after every finite itinerary, so these are the true transitions for the specified Lebesgue ensemble.

The initial level weights are \(\Pr(J_0=j)=(1-\lambda)\lambda^{j-1}/(1-\lambda^4)\), for \(1\le j\le4\). The chance to depart to \(J_1\ge5\) given a source level \(j\) is \(\lambda^{5-b_j}\). Their weighted sum is
\[
\begin{aligned}
\alpha_\lambda
&=\frac{1-\lambda}{1-\lambda^4}
\left(\lambda^4+\lambda^5+\lambda^6+\lambda^6\right)\\
&=\frac{\lambda^4(1-\lambda)(1+\lambda+2\lambda^2)}{1-\lambda^4}
=\frac{\lambda^4(1+\lambda^2-2\lambda^3)}{1-\lambda^4}.
\end{aligned}
\]
Conditional on departure \(H=J_1-4\) is geometric:
\[
\Pr(H=h\mid J_1\ge5)=(1-\lambda)\lambda^{h-1},\qquad h=1,2,\ldots.
\]

**2. Renewal and exact first return.** While outside \(B\), the nonnegative level height changes by \(K-1\), where the independent \(K\) have \(\Pr(K=k)=(1-\lambda)\lambda^k\), \(k=0,1,\ldots\). Thus the chain is skip-free downward. The generating function \(r_\lambda(z)\) of the first passage from height one to zero is the minimal nonnegative solution of
\[
r_\lambda(z)=\frac{z(1-\lambda)}{1-\lambda r_\lambda(z)}.
\]
By the skip-free property, the passage time \(T_h\) from height \(h\) to zero has generating function \(r_\lambda(z)^h\), even when infinite hitting times have positive probability. Lagrange inversion yields for integers \(m\ge h\ge1\)
\[
\Pr(T_h=m)=\frac{h}{m}\binom{2m-h-1}{m-h}
(1-\lambda)^m\lambda^{m-h}.
\]
Mixing over geometric \(H\) and including the initial departure step gives the claimed return generating function. At criticality \(r_{1/2}(z)=(1-\sqrt{1-z})\), and its geometric mixture gives the stated central-binomial coefficients by the identity \(1-\sqrt{1-z}=\sum_{m\ge1}\binom{2m}{m}z^m/[4^m(2m-1)]\). The first moment below criticality follows from \(\mathbb E T_1=(1-\lambda)/(1-2\lambda)\) and \(\mathbb E H=1/(1-\lambda)\); at criticality the square-root singularity gives the infinite mean and sharp tail.

**3. Maximum and nonreturn.** Put \(q=(1-\lambda)/\lambda\). The function \(h\mapsto q^h\) is harmonic for the level-height walk. Before reaching zero or height at least \(L\), the overshoot above \(L\), conditional on reaching the upper boundary, is geometric with distribution \(\Pr(\Delta=k)=(1-\lambda)\lambda^k\); hence \(\mathbb E[q^\Delta]=q\). Bounded stopping at the two barriers (or the corresponding elementary finite difference equation) therefore gives
\[
\Pr_h(\text{visit height}\ge L\text{ before }0)
=\frac{q^h-1}{q^{L+1}-1},\qquad 1\le h<L.
\]
For \(h\ge L\), this probability is one. Averaging over the initial geometric height gives \(\Pr(M\ge L)=\alpha_\lambda(q^2-1)/(q^{L+1}-1)\) for \(q\ne1\), and taking the limit \(q\to1\) gives \(\alpha_{1/2}2/(L+1)=2/[15(L+1)]\). Taking \(L\to\infty\), together with the random-walk law of large numbers on escaping paths, gives the nonreturn mass and equality of the infinite-height and infinite-time events.

**4. Temporal near-critical window.** Fix \(u\in\mathbb R\) and let \(\lambda_N=1/2+u/\sqrt N\). For each fixed positive integer \(h\), Stirling's formula applied to the exact coefficient above, uniformly for \(m/N\) in compact subsets of \([1,\infty)\), gives
\[
\Pr_{\lambda_N}(T_h=m)
\sim \frac{h}{2\sqrt\pi}m^{-3/2}
\exp(-4u^2m/N).
\]
For \(u>0\) the never-return probability from height \(h\) is \(1-[(1-\lambda_N)/\lambda_N]^h\sim4uh/\sqrt N\). Hence the sum of the return-time mass beyond \(N\), including the atom at infinity, converges after multiplying by \(\sqrt N\) to
\[
\frac{h}{2\sqrt\pi}\int_1^\infty t^{-3/2}e^{-4u^2t}\,dt+4u_+h
=h\left[\frac{e^{-4u^2}}{\sqrt\pi}+2u\operatorname{erfc}(-2u)\right].
\]
For \(u<0\) the integral evaluation uses \(\operatorname{erfc}(2|u|)\); the displayed continuous expression applies in all cases. A uniform bound proportional to \(h+1\) on the scaled survival probability, obtained from the ballot coefficient upper bound and the possible nonreturn mass for bounded \(u\), allows dominated convergence over geometric \(H\). Since \(\mathbb E H\to2\) and \(\alpha_{\lambda_N}\to1/15\), the claimed prefactor is \(2/15\). Shifting \(N\) to \(N-1\) for the initial departure step does not change the limit.

**5. Spatial near-critical window.** If \(\lambda_L=1/2+u/L\), then \(q_L=1-4u/L+O(L^{-2})\), \(q_L^{L+1}\to e^{-4u}\), and \(L(q_L^2-1)\to-8u\). Substitution into the *exact* maximum distribution proves the claimed spatial scaling, with its continuous value at \(u=0\).

## Verification

Run `python3 verify_excursions.py` in the same directory as this document (Python standard library only). The program cross-checks the exact return masses against independent interval-level Markov propagation for four rational parameter values through nine steps, compares the maximum-height law against exact rational finite-state linear systems through height seven, verifies 28 critical binomial coefficients and 19 critical maximum values, and checks both rescaled crossover formulas at explicitly reported large finite indices. Output ends with `SPACE_TIME_EXCURSION_VERIFICATION_OK`. Finite experiments are corroboration only: the all-parameter identities and infinite limits rely on the proof above.

## Relationship to prior work

Ji and Ma (2023), Section 5.1, introduce the same auxiliary countably piecewise-affine map and use its transition structure to establish a conservative/dissipative phase transition. Their paper explicitly distinguishes that auxiliary map from the original dynamical family; its results do not give the complete Lebesgue-first-return generating function, the exact maximum-height distribution for every parameter, or the two simultaneous parameter-size crossover functions derived here. Earlier random-walk and branching-process work includes general skip-free hitting formulas; the classical formulas are methods, not asserted as new. The object-specific initial Lebesgue mixture, explicit parameter-dependent laws, and comparison of two critical windows are the contribution. A prior calculation of the *critical-only, different-start* first-return/maximum-height law is not claimed as new or independently rediscovered here; the current theorem emphasizes the complete parameter family and the two critical windows.

## Limitations

Only the **auxiliary** map \(T_\lambda\), initial normalized Lebesgue measure on \(B\), the first-return clock of that map, and the specified level-height maximum are treated. No identity of distributions or physical clocks is claimed for the Fibonacci bimodal map \(f_\lambda\), its induced map \(F_\lambda\), or other observables. Earlier general branching/skip-free random-walk identities may imply some intermediate steps and special cases; whether a broader theorem subsumes all object-specific two-window formulas is a residual literature-priority risk. Numerical cutoff tests are not proofs of limits. Independent expert examination has not been undertaken.

## References

1. H. Ji and W. Ma, *Phase transition for piecewise linear fibonacci bimodal map*, AIMS Mathematics **8** (2023), 8403–8430; published 2023-02-03; DOI: 10.3934/math.2023424. Full open-access PDF: https://www.aimspress.com/aimspress-data/math/2023/4/PDF/math-08-04-424.pdf. Particularly Section 5.1 and the adjacent Markov transition discussion.
2. H. Bruin and M. Todd, *Transience and thermodynamic formalism for infinitely branched interval maps*, Journal of the London Mathematical Society (2012); arXiv:1104.5452. Background on recurrence/transience in distinct countably branched maps; not an identical-map result.
