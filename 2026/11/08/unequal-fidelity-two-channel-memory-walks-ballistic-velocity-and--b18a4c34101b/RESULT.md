# Unequal-fidelity two-channel memory walks: ballistic velocity and inverse identification

## Finding

**Theorem.** Let \(p_1,p_2\in(1/2,1)\), \(a=2p_1-1\), \(b=2p_2-1\), and \(s=(a+b)/2>3/4\). Define the random walk precisely below. Write \(X_n\) for its signed displacement, \(Z_n\) for the proportion of zero increments, and

\[
 v=\sqrt{\frac{(2s-1)(4s-3)}{ab\,s^2}}>0.
\]

Then, for a random sign \(\varepsilon\) with \(\mathbb P(\varepsilon=1)=\mathbb P(\varepsilon=-1)=1/2\),

\[
 (Z_n,X_n/n)\longrightarrow (1/s-1,\varepsilon v)
 \qquad\text{almost surely}.
\]

The two limiting observables identify the *unordered* pair of channel fidelities. Indeed, if \(z=\lim Z_n\) and \(w=\lim |X_n|/n\), then

\[
 s=(1+z)^{-1},\quad
 d=ab=\frac{(2s-1)(4s-3)}{s^2 w^2},\quad
 \{p_1,p_2\}=\left\{\frac{1+s+\sqrt{s^2-d}}2,\frac{1+s-\sqrt{s^2-d}}2\right\}.
\]

At fixed mean persistence \(s\), the zero fraction is unchanged, while the speed strictly increases with \(|a-b|\):

\[
 v^2=\frac{(2s-1)(4s-3)}{s^2\{s^2-(a-b)^2/4\}}.
\]

## Assumptions and scope

Take \(\sigma_1,\sigma_2\) as independent fair random signs. For every \(n\ge2\), independently choose indices \(I_{n+1},J_{n+1}\) uniformly from \(\{1,\ldots,n\}\), **with replacement**, and signs \(\eta_{1,n+1},\eta_{2,n+1}\) independent of the history and of each other, having probabilities \(\mathbb P(\eta_{i,n+1}=1)=p_i\). Put

\[
\sigma_{n+1}=\max\{-1,\min\{1,\eta_{1,n+1}\sigma_{I_{n+1}}+\eta_{2,n+1}\sigma_{J_{n+1}}\}\},\qquad X_n=\sum_{j=1}^n\sigma_j,
\]

and \(Z_n=n^{-1}\sum_{j=1}^n\mathbf 1\{\sigma_j=0\}\). These assumptions, including replacement and unequal fixed fidelities, are part of the theorem. The probabilities are strictly interior and the mean-fidelity inequality is strict.

## Proof

**1. Conditional transition law.** Define \(x_n=X_n/n\), \(q_n=1-Z_n\), \(c_n=Z_n\). After memory-channel signs are applied, the probabilities of \(+1,-1,0\) in channel one are respectively \((q_n+a x_n)/2,(q_n-a x_n)/2,c_n\); in channel two replace \(a\) by \(b\). Independence and clipping give

\[
\begin{split}
 \mathbb E(\sigma_{n+1}\mid\mathcal F_n)&=s(1+c_n)x_n,\\
 \mathbb P(\sigma_{n+1}=0\mid\mathcal F_n)&=c_n^2+\tfrac12(q_n^2-ab x_n^2),\\
 \mathbb P(\sigma_{n+1}\ne0\mid\mathcal F_n)&=2q_n-\tfrac32q_n^2+\tfrac{ab}2x_n^2.
\end{split}
\]

Consequently \((x_n,q_n)\) is a bounded stochastic approximation with steps \(1/(n+1)\), bounded martingale differences and deterministic drift

\[
 F(x,q)=\big(x[(2s-1)-s q],\ q-\tfrac32 q^2+\tfrac{ab}{2}x^2\big)
\]

on the compact triangle \(\{(x,q):0\le q\le1,|x|\le q\}\).

**2. Equilibria and phase portrait.** The zeros of \(F\) in the triangle consist of \((0,0)\), \((0,2/3)\), and \((\pm v,q_*)\), with \(q_*=2-1/s\) and \(v\) as stated. Since \((1-a)(1-b)>0\), \(ab>2s-1\); moreover \((2s-1)^2-(4s-3)=4(1-s)^2>0\). Hence \(0<v<q_*<1\). At the symmetric equilibrium \((0,2/3)\), the eigenvalues are \(-1\) and \(4s/3-1>0\). At either nonsymmetric equilibrium the Jacobian has trace \(1-3q_*<0\) and determinant \(sab v^2>0\); these are asymptotically stable.

The flow has \(\dot q\ge q(1-3q/2)\), so each ODE orbit initially with \(q>0\) eventually remains within \(q>1/2\). On either sign half-plane of \(x\), the Bendixson–Dulac multiplier \(1/x\) (or its negative) has divergence of fixed nonzero sign, proportional to \((1-3q)/x\). Thus there are no periodic cycles or enclosing homoclinic loops in the eventual region. The invariant line \(x=0\) has only the saddle and the origin as equilibria, and the stable equilibria have no outgoing orbit. Therefore the planar ODE has no nontrivial chain-recurrent cycles; its internally chain-transitive compact sets are single equilibria.

**3. Exclusion of the zero-activity equilibrium.** Write \(B_n=nq_n\), the nonzero-step count. Initially \(B_2=2\) and it is nondecreasing. If \(q_n\le1/4\), the last conditional probability in step 1 is at least \(13 B_n/(8n)\). Since \(B_n\ge2\), direct conditional expectation yields

\[
 \mathbb E\left(\frac{n+1}{B_{n+1}}\middle|\mathcal F_n\right)
 =\frac{n+1}{B_n}\left(1-\frac{\mathbb P(\sigma_{n+1}\ne0\mid\mathcal F_n)}{B_n+1}\right)
 \le\frac{n}{B_n}.
\]

For each deterministic index at which the process is in this region, stop at its next exit. The nonnegative stopped process \(n/B_n\) is a supermartingale and converges to a finite limit almost surely. On the event \(q_n\to0\) there is a deterministic index, among a countable collection, after which there is no exit, but \(n/B_n=1/q_n\to\infty\), a contradiction. Hence \(\mathbb P(q_n\to0)=0\).

**4. Almost-sure selection of a ballistic attractor.** Standard bounded-noise stochastic-approximation convergence (the asymptotic-pseudotrajectory and internally chain-transitive limit-set theorem) applied to the phase portrait of step 2 implies that \((x_n,q_n)\) converges almost surely to one of the four equilibria. Step 3 excludes the origin. At \((0,2/3)\), the unstable \(x\)-direction has positive exponent \(4s/3-1\); the new increment takes both signs with conditional probability tending to \(1/3\) each. The nonconvergence-to-linearly-unstable-equilibria theorem for stochastic approximation therefore excludes this saddle. Hence the only possible limits are \((v,q_*)\) and \((-v,q_*)\). Sign reversal of all increments leaves the law invariant and swaps these limits, giving probability one-half for each. Since \(Z_n=1-q_n\), the asserted almost-sure law follows.

**5. Identification.** The limit \(1-q_*=1/s-1\) identifies \(s\). The strictly positive squared speed identifies \(d=ab\). Since \(a+b=2s\), the unordered \(a,b\) are the roots of \(u^2-2su+d\); solving gives the stated formulas. Continuity also gives strongly consistent plug-in estimates of the unordered fidelities from \((Z_n,|X_n|/n)\) (with any harmless finite-sample truncation of a negative numerical discriminant). The fixed-sum comparison follows from \(ab=s^2-(a-b)^2/4\).

## Verification

Run `python3 verify.py` from the package directory. The standalone exact-rational checker enumerates every three-color count configuration of sizes one through twelve for twenty-five rational parameter pairs, checks the three conditional transition probabilities, both drift identities, the interior-equilibrium equations, admissibility, and the inversion identity. It reports 45,420 exact-rational assertions. These finite checks do not prove the stochastic-approximation limit; steps 2–4 are the infinite-time proof.

## Relationship to prior work

Maulik, Roy and Sadhukhan (2025), Theorems 2.1 and 4.2, rigorously establish the corresponding **equal-fidelity** ballistic limit, where both channels have one common parameter. The present unequal-fidelity chain is not distributionally the same as the chain with the average fidelity: the conditional zero-step probability contains \(ab x_n^2\), not \(s^2 x_n^2\). Its inverse recovery of two distinct parameters from one infinite path, and the fixed-average heterogeneity comparison, are not statements in that paper. The later recurrence/transience study by Nguyen Ngoc (2026) concerns the common-parameter model. General multi-drawing urn stochastic-approximation results of Lasmar, Mailler and Selmi (2018) supply methodological context but do not by themselves calculate this two-parameter phase portrait or inverse law.

## Limitations

This theorem covers only fixed \(p_1,p_2\in(1/2,1)\) with \(p_1+p_2>7/4\), two independent history choices with replacement, and fair initial signs. It does not assert a limit at the critical surface, a full subcritical phase diagram, convergence rates, or asymptotic normality of parameter estimators. The distinct channel labels cannot be recovered because the model is invariant under their interchange. Historical priority remains provisional against more general nonlinear-urn theorems; no independent audit has been performed.

## References

1. K. Maulik, P. Roy, and T. Sadhukhan, *Phase Transitions for Elephant Random Walks with Two memory Channels*, arXiv:2509.10225v1, 12 September 2025, https://arxiv.org/html/2509.10225v1 .
2. N. P. N. Ngoc, *Recurrence, Transience, and the Rate of Escape for Elephant Random Walks with Two Memory Channels*, arXiv:2609.06641, 6 September 2026, https://arxiv.org/abs/2609.06641 .
3. N. Lasmar, C. Mailler, and O. Selmi, *Multiple drawing multi-colour urns by stochastic approximation*, J. Appl. Probab. 55 (2018), 254–281, https://doi.org/10.1017/jpr.2018.16 .
4. R. Pemantle, *Nonconvergence to unstable points in urn models and stochastic approximations*, Ann. Probab. 18 (1990), 698–712, https://doi.org/10.1214/aop/1176990853 .
5. M. Benaïm, *Dynamics of stochastic approximation algorithms*, Séminaire de Probabilités XXXIII (1999), 1–68.
