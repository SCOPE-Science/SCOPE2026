# Three sharp reset-budget thresholds for stationary purity of a clocked qubit

## Finding

Let a qubit be prepared as \(\lvert +\rangle=(\lvert0\rangle+\lvert1\rangle)/\sqrt2\). At every tick without resetting it undergoes the phase gate \(S=\operatorname{diag}(1,i)\); at a reset tick it is re-prepared as \(\lvert+\rangle\). Independent positive-integer reset intervals have arbitrary common law \(L\) with fixed, finite mean \(\mu=\mathbb EL\ge1\). Take the stationary **equilibrium-renewal phase** of this clock process, rather than assuming that a process initialized at a reset converges at every tick.

Set
\[
 f_{-}(\mu)=\begin{cases}
 1+(2-\mu)^2,&1\le\mu\le\tfrac32,\\
 (4-\mu)^2/5,&\tfrac32\le\mu\le4,\\
 0,&\mu\ge4,
 \end{cases}
 \qquad
 f_{+}(\mu)=\begin{cases}
 2+2(\mu-1)^2,&1\le\mu\le2,\\
 4,&\mu\ge2.
 \end{cases}
\]
Then **every** reset law with this mean has stationary ensemble purity in the **complete, closed and sharp interval**
\[
 \boxed{\quad\operatorname{tr}(\rho_*^2)\in
 \left[\frac12+\frac{f_-(\mu)}{4\mu^2},\,
 \frac12+\frac{f_+(\mu)}{4\mu^2}\right].\quad}
\]
All intermediate purities occur for some positive-integer reset law of the same mean.

The exact attaining laws, including the boundary cases, are as follows. For \(1\le\mu\le3/2\), the **unique** minimum-purity reset law places probabilities \((3-\mu)/2\) and \((\mu-1)/2\) at intervals \(1\) and \(3\). For \(3/2\le\mu\le4\), the **unique** minimum-purity law puts probabilities \(3(4-\mu)/10\), \((4-\mu)/10\), and \((2\mu-3)/5\) at intervals \(1,3,4\) respectively. For \(\mu\ge4\), all and only laws supported on \(\{4,8,12,\ldots\}\) with mean \(\mu\) minimize purity, attaining complete dephasing. The prescriptions agree at \(\mu=3/2\) and \(\mu=4\).

For \(1\le\mu\le2\), the **unique** maximum-purity law places probabilities \(2-\mu\) and \(\mu-1\) at intervals \(1,2\). For \(\mu\ge2\), all and only laws supported on \(\{2,6,10,\ldots\}\) with mean \(\mu\) maximize purity. These prescriptions agree at \(\mu=2\).

Thus the minimizing protocol changes support at \(\mu=3/2\), the maximizing protocol enters a fixed phase-residue class at \(\mu=2\), and exact total dephasing first becomes possible at \(\mu=4\). These thresholds arise from an integer-tick restriction, not from a continuum waiting-time approximation.

## Assumptions and scope

The clock has discrete time \(t\in\mathbb Z\); a full inter-reset interval \(L\) is an integer \(\ge1\), independent from cycle to cycle. Immediately after a reset the state is \(\lvert+\rangle\langle+\rvert\). After \(a\) consecutive gate ticks, where \(a\ge0\), the state is \(S^a\lvert+\rangle\langle+\rvert(S^\dagger)^a\). The one-tick updating convention is fixed by the fact that a cycle of length \(n\) visits the ages \(0,1,\ldots,n-1\), then resets.

Since \(0<\mu<\infty\), a stationary two-sided equilibrium renewal process exists. At the observation tick its backward age \(A\) has \(\Pr(A=a)=\Pr(L>a)/\mu\) for \(a\in\mathbb Z_{\ge0}\). Thus \(\rho_*\) denotes the density matrix averaged at one tick under this stationary law. When the interval support has nontrivial period, \(\rho_*\) need not be the pointwise large-time limit when starting at a synchronized reset tick; the theorem explicitly makes no such claim. The statement concerns ideal instantaneous resets and an exact phase gate, not noisy hardware.

## Proof

**1. Equilibrium renewal and coherence.** The age law is normalized because \(\sum_{a\ge0}\Pr(L>a)=\mathbb EL=\mu\). Taking \(z=\mathbb E[i^A]\), the finite geometric sum within each random reset cycle gives
\[
 z=\frac1\mu\sum_{a\ge0}\Pr(L>a)i^a
 =\frac{1-\mathbb E[i^L]}{\mu(1-i)}.
\]
The stationary qubit state has diagonal entries \(1/2\) and off-diagonal entries \(\overline z/2\) and \(z/2\). Consequently,
\[
 \operatorname{tr}(\rho_*^2)=\frac12+\frac{|z|^2}{2}
 =\frac12+\frac{|1-\mathbb E[i^L]|^2}{4\mu^2}.
\]
It suffices to characterize \(F=|1-\mathbb E[i^L]|^2\) under the sole constraint \(\mathbb EL=\mu\).

**2. Lower bound for \(1\le\mu\le3/2\).** Put \(u=2-\mu\in[1/2,1]\), and write \(w=1-\mathbb E[i^L]=w_R+iw_I\). For every positive integer \(n\),
\[
 1-\cos(\pi n/2)+u\sin(\pi n/2)\ \ge\ 1+2u-un.
\]
Indeed equality holds for \(n=1,3\); for \(n=2\), the two sides are \(2\) and \(1\); for \(n=4\), they are \(0\) and \(1-2u\le0\); for \(n\ge5\), the left is nonnegative and the right is nonpositive. Taking expectation and using \(\mathbb EL=\mu\) yields
\[
 w_R-u w_I\ge1+2u-u\mu=1+u^2.
\]
Cauchy--Schwarz implies \(F\ge1+u^2=f_-(\mu)\). The law on \(\{1,3\}\) specified in the finding has \(w=(1,-u)\), attaining equality. Equality in the pointwise inequality and Cauchy--Schwarz forces this law; at \(u=1/2\), the additional pointwise equality \(n=4\) cannot have positive mass because the required \(w_R=1\) rules it out. Thus the minimizer is unique.

**3. Lower bound for \(3/2\le\mu\le4\).** For every integer \(n\ge1\),
\[
 2\bigl(1-\cos(\pi n/2)\bigr)+\sin(\pi n/2)\ \ge\ 4-n.
\]
Equality holds exactly at \(n=1,3,4\). Directly checking \(n=2\) gives a strict inequality; for \(n\ge5\) the left is nonnegative while \(4-n<0\). Expectation gives \(2w_R-w_I\ge4-\mu\). Cauchy--Schwarz therefore gives
\[
 F=w_R^2+w_I^2\ge\frac{(4-\mu)^2}{5}.
\]
The law on \(\{1,3,4\}\) claimed above has \(w=\frac{4-\mu}{5}(2-i)\), attaining equality. Equality in both inequalities restricts support to \(1,3,4\) and \(w\) to the ray through \(2-i\); normalization and mean then determine the three displayed weights uniquely for \(\mu<4\). At \(\mu=4\), equality \(F=0\) forces \(\mathbb E i^L=1\), so \(L\) must be a multiple of four; the mean-four condition forces \(L=4\) almost surely. For \(\mu>4\), nonnegative \(F\) is minimal at zero, attainable if and only if all reset lengths are positive multiples of four. Any real \(\mu\ge4\) can be realized by mixing the adjacent multiples of four that bracket it.

**4. Upper bounds and all maximizers.** First suppose \(1\le\mu\le2\). Put \(d=\mu-1\in[0,1]\) and \(w_1=1-i\), so
\[
 w=w_1+\delta,\qquad \delta=\mathbb E[i-i^L].
\]
For each integer \(n\ge1\), the real inner product \(\operatorname{Re}(\overline{w_1}(i-i^n))\le0\), and \(|i-i^n|\le\sqrt2(n-1)\); the last inequality is an equality only for \(n=1\) or \(n=2\). Thus \(\operatorname{Re}(\overline{w_1}\delta)\le0\) and \(|\delta|\le\sqrt2(\mu-1)\), whence
\[
 F=|w|^2\le|w_1|^2+|\delta|^2\le2+2(\mu-1)^2.
\]
Equality forces support on \(\{1,2\}\), and the mean fixes the displayed probabilities. For every \(\mu\ge2\), the triangle inequality gives \(F=|1-\mathbb E i^L|^2\le4\), with equality if and only if \(i^L=-1\) almost surely, i.e., every reset length is congruent to two modulo four. Any \(\mu\ge2\) can be realized by mixing adjacent lengths in this residue class.

**5. Full range.** The classes of laws with a fixed mean are convex. Mixing any lower- and upper-extremizing laws preserves the mean and traces a continuous path in the complex plane for \(w\), and thus a continuous purity path. Since the extremal values are attained and all laws obey the bounds, the intermediate-value theorem proves that **no purity values inside the stated interval are missing**. This finishes the proof, including the endpoint and uniqueness assertions.

## Verification

Run \(\texttt{python3 checker.py}\) alongside this file. The standalone standard-library checker uses rational arithmetic, reconstructs stationary coherence in two independent ways (by cycle moments and by the equilibrium age law), tests every weak composition of seven into twelve reset lengths, verifies the optimizer formulas at 400 rational means, and checks the elementary dual inequalities over a finite diagnostic range. It reports 69,251 assertion groups on the embedded version. The checker is diagnostic only: the universal quantifiers and all equality conditions follow from the preceding analytical proof, not finite enumeration.

For a geometric reset interval law with success probability \(1/2\) per tick, \(\mu=2\), the stationary purity is \(3/5\). The proven sharp interval at the same mean is \([11/20,3/4]\). The lower endpoint is achieved by reset intervals \(1,3,4\) with probabilities \(3/5,1/5,1/5\); the upper endpoint uses interval \(2\) deterministically. This provides a physically interpretable exact benchmark at one common reset budget.

## Relationship to prior work

Wald, Yao, Platini, Hooley and Carollo [1], first circulated in October 2024, give a general discrete-time quantum resetting framework, exact results for geometric-clock resets, resonance structure, and a study of when nongeometric protocols converge. Their detailed non-Poissonian analysis does not give the fixed-mean sharp attainable purity interval and equality-case classification for the quarter-turn single-qubit gate. In particular, their nonconvergence observation for deterministic synchronous resets is respected by the stationary equilibrium-phase formulation here.

Sevilla and Valdés-Hernández [2] formulate general continuous-time quantum renewal resetting and purity expressions. Their continuous-time model allows reset intervals that are arbitrarily close to zero; the tick-constrained optimizer boundaries found here are therefore **not** implied by the continuous-time class's lower envelope. Standard geometric-series and equilibrium-age identities supply the reduction, and are not presented as novel. The contribution is the sharp lattice-constrained extremal classification and the three reset-budget transitions.

## Limitations

The theorem is for the ideal quarter-turn gate and a fixed equatorial reset pure state; it does not treat arbitrary gates, gate errors, measurements, feedback, or constraints on the variance of reset durations. The stationary equilibrium-phase ensemble is not automatically the pointwise long-time state of a clock synchronized at its first reset, particularly for periodic optimal laws. No hardware or finite-sample guarantees are asserted, and external independent scientific validation has not been conducted. Publication priority remains conditional on unindexed specialized results or more general exact lattice-moment optimization theorems that may imply this classification.

## References

1. S. Wald, L. H. Yao, T. Platini, C. Hooley, and F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497, first posted 2024-10-15; later in *Quantum* 9, 1742 (2025). https://arxiv.org/abs/2410.11497.
2. F. J. Sevilla and A. Valdés-Hernández, *Dynamics of closed quantum systems under stochastic resetting*, arXiv:2209.05643, first posted 2022-09-12; https://arxiv.org/abs/2209.05643.
