# Sharp fixed-mean first-passage Laplace and variance envelopes for distributed Brownian resetting

## Finding

**Theorem (sharp all-frequency envelope, complete extremizers, and exact law-identification).** Fix a diffusion coefficient \(D>0\), a Poisson resetting rate \(r>0\), a target \(x_T\in\mathbb R\), and distances \(0<a<b<\infty\). At time zero and after every independent rate-\(r\) reset, draw an independent position \(Y\) from the same probability measure \(\mu\), and absorb the particle on first reaching the target. Restrict admissible reset laws by \(a\le |Y-x_T|\le b\) almost surely and by a prescribed mean first-passage time.

Set
\[
\lambda=\sqrt{r/D},\quad U=e^{-\lambda|Y-x_T|},\quad u_-=e^{-\lambda b},\quad u_+=e^{-\lambda a},\quad p=\mathbb E U\in(u_-,u_+),\quad \theta=\frac{p-u_-}{u_+-u_-}.
\]
The prescribed mean is \(m=(1-p)/(rp)\). For every \(s>0\), put \(\alpha_s=\sqrt{1+s/r}>1\), \(J_-(s)=p^{\alpha_s}\), \(J_+(s)=\theta u_+^{\alpha_s}+(1-\theta)u_-^{\alpha_s}\), and \(G_s(j)=(r+s)j/(s+rj)\). Then
\[
\boxed{G_s(J_-(s))\le\mathbb E[e^{-sT}]\le G_s(J_+(s))\quad(s>0).}
\]
Both bounds hold *simultaneously for all positive* \(s\) and are sharp over all admissible laws, including discrete ones. Equality in either bound at even one \(s>0\) characterizes its unique *distance distribution*: the lower extremizer has \(|Y-x_T|=z_*=-(\log p)/\lambda\) almost surely; the upper extremizer has distances \(a,b\) with respective probabilities \(\theta,1-\theta\). Physical reset locations can be reflected about the target without changing the law.

The corresponding sharp and simultaneous variance interval is
\[
\boxed{\frac{1-p^2+p\log p}{r^2p^2}\le \operatorname{Var}(T)\le
\frac{1-p^2+\theta u_+\log u_+ +(1-\theta)u_-\log u_-}{r^2p^2}.}
\]
The variance has the same unique distance-law extremizers. In particular, any nonconstant reset-distance law with the same mean as its equivalent single-point reset has *strictly larger variance*, even though the two processes have the same mean first-passage time.

For any two reset measures at the same \(r,D,x_T\), without requiring a common finite distance interval, the *entire* first-passage-time laws agree **if and only if** their reset-distance laws agree. Thus equality of just the mean does not imply equality of the first-passage laws.

An explicit strict witness is \(D=r=1\) with target \(x_T=4\): process A always resets to \(Y=2\), while B resets to \(Y=3\) with probability \(1/(e+1)\) and \(Y=1\) with probability \(e/(e+1)\). Both have \(\mathbb E T=e^2-1\), whereas
\[
\operatorname{Var}(T_A)=e^4-2e^2-1,\qquad
\operatorname{Var}(T_B)=e^4-\frac{e^2(e+3)}{e+1}-1,
\]
so the positive variance gap is exactly \(e^2(e-1)/(e+1)\).

## Assumptions and scope

The position evolves as Brownian motion with generator \(D\partial_{xx}\) between jumps; each resetting clock is exponential with rate \(r\), independent of all trajectories and independent i.i.d. reset locations. Each initial location also follows the reset distribution. The target is perfectly absorbing and the process ends on first contact. There is no travel time or penalty for resetting. Fixing \(r,D,x_T,a,b\), fixing \(m\in((1-u_+)/(ru_+),(1-u_-)/(ru_-))\) is equivalent to fixing the indicated \(p\). The sharp interval assertions include general probability measures on the allowed distance set, not only distributions with a density. The exact law-identification assertion allows any probability reset laws for which the renewal construction is defined, with possible immediate target absorption; the stated interval guarantees finite moments for the quantitative part.

## Proof

**1. Exact renewal identity.** For a Brownian attempt started at target distance \(z\ge0\), let \(H_z\) be its first target-hitting time. Brownian reflection/first-passage theory gives \(\mathbb E[e^{-vH_z}]=e^{-z\sqrt{v/D}}\) for \(v>0\). Let \(E_r\) be an independent exponential reset time. With \(Z=|Y-x_T|\), set \(I(v)=\mathbb E[e^{-Z\sqrt{v/D}}]\). The discounted success-before-reset contribution is \(A(s)=\mathbb E[e^{-sH_Z};H_Z<E_r]=I(s+r)\). By integrating the exponential reset density up to \(H_Z\), the discounted reset-before-success contribution is \(B(s)=r(1-I(s+r))/(s+r)\). The next attempt is independent and has the same initial law; hence if \(F(s)=\mathbb E[e^{-sT}]\), then \(F(s)=A(s)+B(s)F(s)\). Solving gives
\[
F(s)=\frac{(r+s)I(r+s)}{s+rI(r+s)},\qquad
\frac{1-F(s)}s=\frac{1-I(r+s)}{s+rI(r+s)}.
\]
The second identity is the averaged-survival transform appearing in the motivating paper, while the first follows from it. For \(I(r)=p>0\), differentiate at \(s=0\) to get \(\mathbb ET=(1-p)/(rp)\). The bounded-distance setup has a geometric number of attempts with positive one-attempt success probability, so the needed moments exist.

**2. Convexity and sharp transform envelopes.** Since \(I(r+s)=\mathbb E[U^{\alpha_s}]\) and \(\alpha_s>1\), strict Jensen convexity gives \(\mathbb E[U^{\alpha_s}]\ge p^{\alpha_s}\). The graph of the same strictly convex function lies below its chord on \([u_-,u_+]\), giving \(\mathbb E[U^{\alpha_s}]\le\theta u_+^{\alpha_s}+(1-\theta)u_-^{\alpha_s}\). Furthermore \(G_s'(j)=(r+s)s/(s+rj)^2>0\) for \(s>0\). Combining proves the boxed bounds. Jensen equality forces \(U=p\) almost surely. Strict chord inequality forces \(U\in\{u_-,u_+\}\) almost surely; the fixed mean then forces weights \(1-\theta\) and \(\theta\), respectively. The same distributions work for every \(s\), so bounds are simultaneous, exact, and globally characterized.

**3. Variance and strict minimum.** Differentiate \(I\) at \(r\):
\[
2rI'(r)=\mathbb E[U\log U]=:q.
\]
Twice differentiating \(F\), or equivalently once differentiating its survival transform, gives
\[
\operatorname{Var}(T)=\frac{1-p^2+q}{r^2p^2}.
\]
The function \(h(u)=u\log u\) has \(h''(u)=1/u>0\) for \(u>0\), so Jensen and its endpoint chord give \(p\log p\le q\le\theta u_+\log u_+ +(1-\theta)u_-\log u_-\). Equality cases are exactly those in step 2. This proves the variance bounds, including strictly larger variance for every nonconstant distance distribution relative to its mean-equivalent single-site distribution.

**4. Full distributional identifiability.** Given the complete first-passage Laplace transform \(F(s)\) for all \(s>0\), the exact renewal relation inverts to
\[
I(r+s)=\frac{sF(s)}{s+r-rF(s)}.
\]
Consequently, equal first-passage laws force equal \(\mathbb E[e^{-tZ}]\) for all \(t>\sqrt{r/D}\). Choose any \(t_0>\sqrt{r/D}\); the finite tilted measures \(e^{-t_0z}\,\Pr(Z\in dz)\) then have the same ordinary Laplace transform for all positive arguments. Uniqueness of Laplace transforms of finite measures identifies these tilted measures and, on multiplying back by \(e^{t_0z}\), the original distance measures. Conversely, the law of \(Z\) determines \(I\), then \(F\), hence the entire hitting-time law. Reflection about the target changes \(Y\) without changing \(Z\).

**5. Explicit strict witness.** For A, \(p=e^{-2}\) and \(q=-2e^{-2}\). For B,
\[
 p=\frac{e^{-1}+e\,e^{-3}}{e+1}=e^{-2},\qquad
 q=-\frac{e^{-1}+3e\,e^{-3}}{e+1}=-e^{-2}\frac{e+3}{e+1}.
\]
Substitution into the exact mean and variance formulas proves the claimed equality of means, the two unequal variances and the strictly positive exact gap.

## Verification

The standalone `verify.py` reproduces the renewal transform algebra numerically, verifies transform inversion, checks the strict convexity bounds for multiple frequencies and fixed-mean mixtures, evaluates the exact two-model witness, and checks the moment identities by numerical differentiation. The proof of the quantified all-frequency statements uses strict convexity and Laplace-transform uniqueness, not finite numerical sampling. Run `python3 verify.py` with the Python standard library. The test program and all necessary mathematical definitions are contained in this package.

## Relationship to prior work

Méndez, Flaquer-Galmés and Campos, arXiv:2401.01125v1 (2024), Eqs. (14)–(16), establish the mean and the full averaged survival-transform formula, and Eq. (60) gives the variance for a specified resetting distribution. Their Sec. II.A text following Eq. (16) claims that the common mean determines identical full first-passage statistics; their Sec. VI introduces the mean-equivalent resetting point. The present theorem retains their correct renewal identities while showing that equality of the mean fixes only \(I(r)\), not \(I(r+s)\) for all \(s>0\). It supplies a strict exact counterexample, a corrected iff classification and sharp mean-constrained all-frequency/variance envelopes with equality cases.

Julián-Salgado, Dagdug and Boyer, arXiv:2311.11897v1 (2023), study two-site reset-rate optimization and its phase transitions, including the initial reset distribution. Toledo-Marín and Boyer, arXiv:2206.14387v1 (2022), study distributed-reset mean first passage and information costs. Their analyzed results do not imply the stated universal fixed-mean bounds or equality classification. Classical Jensen/chord inequalities and Laplace uniqueness are standard ingredients; novelty is claimed only for the precise resetting-law theorem and its physical implication, not for these ingredients or for the published renewal formula.

## Limitations

The Laplace-transform inequalities are inequalities between transforms, not assertions of stochastic dominance of hitting times. The location law is identifiable only after taking its distance to the target; reflecting reset positions cannot be distinguished. The fixed-mean sharp optimization requires known \(r,D\), a known allowable distance interval with \(a>0\), and iid positions at time zero and resets. The work does not give confidence bounds from finite data, nor extend the result to renewal-reset clocks, reset costs, resetting with memory, or fixed initial positions different from the reset law. Numerical checks do not prove the infinite family of bounds. General unindexed convex-order results could imply portions of the argument and warrant external priority review.

## References

1. V. Méndez, R. Flaquer-Galmés and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125v1, first publicly posted January 2, 2024, https://arxiv.org/abs/2401.01125. Relevant sections: II, II.A, VI and VII, Eqs. (14)–(16), (48), (60).
2. P. Julián-Salgado, L. Dagdug and D. Boyer, *Diffusion with two resetting points*, arXiv:2311.11897v1, first publicly posted November 20, 2023, https://arxiv.org/abs/2311.11897. Relevant sections: II, III and V.
3. J. Q. Toledo-Marín and D. Boyer, *First passage time and information of a one-dimensional Brownian particle with stochastic resetting to random positions*, arXiv:2206.14387v1, first publicly posted June 29, 2022, https://arxiv.org/abs/2206.14387.
4. The standard Brownian first-passage Laplace identity, strict Jensen inequality, supporting-line/chord convexity and uniqueness of Laplace transforms are used as classical facts.
