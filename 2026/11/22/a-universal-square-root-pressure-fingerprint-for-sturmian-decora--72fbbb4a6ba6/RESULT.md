# A square-root pressure fingerprint for Sturmian-decorated renewal shifts

## Finding and scope

Fix an irrational \(0<\alpha<1\), and let \(Y_\alpha\) be the bilateral Sturmian shift whose symbol \(2\) has frequency \(\alpha\). Let \(X_\alpha\) be the closure of the bilateral concatenations of words \(0u\) with \(u\) any finite factor of \(Y_\alpha\), including the empty factor. Thus markers may be adjacent. Write \(P_\alpha(x,t)\) for the topological pressure of \(\varphi_{x,t}=(\log x)\mathbf 1_{[0]}+t\mathbf 1_{[2]}\) with \(x>0\) and \(t\in\mathbb R\), using natural logarithms. This potential has a unique equilibrium measure \(\mu_{x,t}\). Its pressure is the unique \(P>\alpha t\) solving

\[
 1=x\sum_{n\ge0} e^{-(n+1)P}\sum_{u\in\mathcal L_n(Y_\alpha)} e^{t|u|_2}.
\]

For fixed real \(t\), as \(x\downarrow0\), set \(C_\alpha(t)=e^{-\alpha t/2}\,2\sinh(t/2)/t\) and \(L(t)=\coth(t/2)-2/t\). The hyperbolic quotient and \(L\) take values \(1\) and \(0\), respectively, at zero by continuity. The pressure and composition laws are

\[
 \begin{aligned}
 P_\alpha(x,t)&=\alpha t+C_\alpha(t)\sqrt x+o(\sqrt x),\\
 \rho_{x,t}:=\mu_{x,t}([0])&\sim \tfrac12 C_\alpha(t)\sqrt x,\\
 \mu_{x,t}([2])&=\alpha+\rho_{x,t}(L(t)-\alpha)+o(\rho_{x,t}).
 \end{aligned}
\]

For all \(x>0\), \(P_\alpha(x,0)=2\operatorname{arsinh}(\sqrt x/2)\) and \(\rho_{x,0}=\sqrt{x}/\sqrt{4+x}\). Hence the entire marker-only pressure curve agrees for all irrational slopes, whereas the first colored pressure coefficient recovers the slope by \(\alpha=-2(\log C_\alpha)'(0)\). The field is fixed in the limit; there is no assertion of uniformity in unbounded \(t\), a convergence rate in the slope, or a conjugacy theorem.

## Proof

**Induced pressure and uniqueness.** The marker-free part of \(X_\alpha\) is \(Y_\alpha\): every finite nonmarker word in an approximating concatenation occurs within one decoration, and every finite Sturmian word can be put in a single return block. This subsystem has zero entropy by factor complexity \(n+1\), and all its invariant measures have frequency \(\alpha\) by balance. Thus the free energy there is \(\alpha t\).

Now consider an **ergodic** invariant measure with positive marker mass. Almost every point then has infinitely many markers in both directions. Its induced process on the countable alphabet of blocks \(c=0u\) is stationary, with mean block length \(\bar\ell\) finite by Kac's formula, and the blocks concatenate without restrictions. Let \(k(c)=|u|_2\) and \(\ell(c)=|u|+1\). The entropy of its one-block marginal \(p\) is finite: a finite mean length bounds the length entropy by comparison with a geometric law, and at each length the conditional entropy is bounded by \(\log \ell\). By Abramov's formula and integrating the potential over the block, the free energy is \((h(\eta)+\log x+t\mathbb E_\eta k)/\bar\ell\), where \(\eta\) is the induced law. (For a nonergodic measure with marker-free mass one first uses ergodic decomposition, not the full-measure return formula.)

For \(P>\alpha t\), write \(\pi_P(c)=xe^{tk(c)-P\ell(c)}\). Since \(|k(c)-\alpha(\ell(c)-1)|<1\) and there are \(n+1\) length-\(n\) decorations, \(\sum_c\pi_P(c)\) converges, is continuous and strictly decreasing in \(P\), diverges as \(P\downarrow\alpha t\), and tends to zero as \(P\to\infty\). For the unique root \(\sum_c\pi_P(c)=1\), the law \(\pi_P\) has finite mean and exponential length tails. The entropy bound \(h(\eta)\le H(p)\) gives

\[
 h(\eta)+\log x+t\mathbb E_\eta k-P\bar\ell\le -D(p\|\pi_P)\le0.
\]

Equality requires \(p=\pi_P\) and independence of the blocks: equality of entropy rate and finite one-block entropy forces the conditional law given each finite past to be the marginal. The iid law has a stationary renewal lift obtained by biasing the block containing the origin by length and placing the origin uniformly within it. This lift has free energy \(P\), and the inducing construction recovers any maximizing ergodic law from the same iid law. Since the marker-free part has strictly smaller free energy, the variational principle and ergodic decomposition prove the pressure and uniqueness claims.

**Distinct factors and a centered-weight limit.** Under mechanical coding with intercept \(\theta\in[0,1)\), the digit marking symbol \(2\) at time \(i\) is \(\lfloor(i+1)\alpha+\theta\rfloor-\lfloor i\alpha+\theta\rfloor\). For \(n\ge1\), the distinct length-\(n\) factors are in bijection with the \(n+1\) cells whose left endpoints are \(-k\alpha\bmod1\), \(0\le k\le n\). Put \(q_n=\{n\alpha\}\). The centered count \(|u|_2-n\alpha\) is \(-q_n\) or \(1-q_n\); the heavy cells lie in \([1-q_n,1)\). If \(r_n\) counts them, the uniform interval discrepancy of an irrational rotation gives \(r_n/(n+1)=q_n+o(1)\). To see why the moving interval is permitted, approximate both endpoints by a fixed finite mesh and use equidistribution on the finitely many mesh intervals, then send the mesh to zero.

Define

\[
 Q_n(t)=\sum_{u\in\mathcal L_n(Y_\alpha)}e^{t(|u|_2-\alpha n)},\quad
 G_t(q)=(1-q)e^{-tq}+q e^{t(1-q)},\quad
 H_t(\delta)=\sum_{n\ge0}Q_n(t)e^{-n\delta}.
\]

Then \(Q_n(t)=(n+1)[G_t(q_n)+o(1)]\), and \(\partial_t Q_n(t)=(n+1)[\partial_tG_t(q_n)+o(1)]\), directly by substituting the two counts. Irrational equidistribution makes the Cesàro averages of the bracketed sequences tend to \(I(t)\) and \(I'(t)\), respectively, where

\[
 I(t)=\int_0^1 G_t(q)\,dq=\int_{-1}^1(1-|y|)e^{ty}\,dy
 =\left(\frac{2\sinh(t/2)}{t}\right)^2.
\]

The triangular density is the limiting distribution of the centered count when averaging distinct factors over the length parameter, not the distribution of the count under the Sturmian invariant measure at a fixed length. Abel summation yields

\[
 \delta^2 H_t(\delta)\to I(t),\qquad
 -\delta^3\partial_\delta H_t(\delta)\to 2I(t),\qquad
 \delta^2\partial_t H_t(\delta)\to I'(t).
\]

For these limits, subtract the Cesàro means and let the centered partial sums be \(o(n)\). When weighted by a polynomial of degree \(k=1\) or \(2\) times \(e^{-n\delta}\), summation by parts bounds the tail by an arbitrarily small constant times \(\sum_{n\ge1}(n^k+\delta n^{k+1})e^{-n\delta}=O(\delta^{-k-1})\); any fixed prefix is negligible on this scale. The uncentered polynomial sums give the factors \(1\) and \(2\) by Riemann sums. These are scaled limits, in particular the last is valid when \(I'(t)=0\). Derivatives in \(t\) here hold \(\delta\) fixed.

**Pressure and occupation laws.** For \(\delta=P_\alpha(x,t)-\alpha t\), the root equation reads \(1=xe^{-\alpha t-\delta}H_t(\delta)\). Its root has \(\delta\downarrow0\) as \(x\downarrow0\), since on a positive range bounded away from zero the renewal sum is bounded. Hence \(\delta^2\sim xe^{-\alpha t}I(t)\). Under \(\pi_P\) the mean block length is \(1-\partial_\delta H_t/H_t\sim2/\delta\), and the mean centered count is \(\partial_t H_t/H_t\to I'(t)/I(t)=L(t)\). The lift therefore has marker density \(\rho=1/\bar\ell\) and color density \(\alpha(1-\rho)+\rho\,\partial_t H_t/H_t\); substitution gives the stated corrections. At zero field, the root equation becomes \(1=xe^{-P}/(1-e^{-P})^2\), or \(x=4\sinh^2(P/2)\). The return mean yields the stated exact marker density. The even factor \(2\sinh(t/2)/t\) gives the slope identity by differentiation at zero.

## Reproducibility and relationship to prior work

The accompanying `verify.py` uses only the Python 3 standard library. It compares direct Sturmian factor enumeration with the rotation partition for lengths up to twelve, then compares truncated renewal sums with all-field leading and zero-field exact laws at selected parameters. These are finite checks and do not prove the limits.

- C. Ramirez and A. Somers, *\((S,w)\)-Gap Shifts and Their Entropy*, [arXiv:2501.08438](https://arxiv.org/abs/2501.08438), Theorem 1.1: the unweighted entropy equation gives the specialization \(x=1,t=0\).
- F. Haydarov, S. Kadyrov, M. Makhmudov and K. Mamayusupov, *Effective Intrinsic Ergodicity for Renewal-Type Potentials on S-Gap Shifts*, [arXiv:2606.17031](https://arxiv.org/abs/2606.17031): uniqueness via renewal mechanisms for classical binary shifts, not a computation of distinct Sturmian factors with a color field.
- G. Fici, F. Mignosi and J. Shallit, *Abelian-Square-Rich Words*, [arXiv:1701.00948](https://arxiv.org/abs/1701.00948), Proposition 14: the heavy/light partition characterization used above.
- *Periodic zeta rationality versus Sturmian nonsoficity in decorated gap shifts*, public research record (2026-10-25): the unweighted periodic-point data agree across slopes and do not encode the color weights.

The distinction here is the evaluated colored critical coefficient, with the accompanying occupation law and separation of slopes despite exact agreement of the uncolored pressure curve. It is not a claim of new return-map entropy theory or a new heavy/light description of Sturmian words. Historical priority beyond the compared material is not certified.
