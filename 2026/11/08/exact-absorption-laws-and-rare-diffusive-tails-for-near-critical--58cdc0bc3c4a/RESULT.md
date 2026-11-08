# Exact absorption laws and rare diffusive tails for near-critical simple sticky walks

## Finding

Consider \(m\ge2\) players whose nonzero card holdings are integers and whose sum is preserved. At each step one of the currently active players is chosen uniformly; if there are \(r\) active players, the chosen player gains \(r-1\) cards and every other active player loses one. Players with zero cards never return. The clock stops when just one player remains.

Start with \(k\) players holding two cards each and \(m-k\) holding one, for \(0\le k\le m\). Write \(\tau_{m,k}\) for the number of steps to absorption, and put \(N=m+k\). For the ordinary symmetric random walk on \(\{0,\ldots,N\}\), let \(G_{N,a}\) be its time to reach either endpoint when started at \(a\), with \(0<a<N\). Put \(q_N(a,t)=\Pr(G_{N,a}>t)\).

**Theorem (complete finite law and critical regimes).** If \(2\le k\le m\), for every integer \(t\ge2\),
\[
\Pr(\tau_{m,k}>t)=\frac{k-1}{m}q_N(k,t-2)+\frac{k(m-k)}{m(k+1)}q_N(k+1,t-2),
\]
with the second term zero when \(k=m\). The initial survival values are \(\Pr(\tau_{m,k}>0)=\Pr(\tau_{m,k}>1)=1\). For \(k=1\), the same formula holds for \(t\ge2\) (its first term vanishes), but \(\Pr(\tau_{m,1}>1)=(m-1)/m\). For \(k=0\), absorption occurs after exactly one step.

For \(0<z\le1\), set \(\eta=\operatorname{arcosh}(1/z)\), and
\[
H_{N,a}(z)=\mathbb E[z^{G_{N,a}}]
=\frac{\cosh((N-2a)\eta/2)}{\cosh(N\eta/2)}.
\]
The exact probability-generating function is, for \(2\le k\le m\),
\[
\mathbb E[z^{\tau_{m,k}}]=\frac{z^2}{m}\left(1+(k-1)H_{N,k}(z)+\frac{m-k}{k+1}(1+kH_{N,k+1}(z))\right).
\]
The term involving \(H_{N,k+1}\) is omitted at \(k=m\). For \(k=1\),
\[
\mathbb E[z^{\tau_{m,1}}]=\frac zm+\frac{m-1}{m}zH_{m+1,1}(z),
\]
and for \(k=0\) the generating function is \(z\).

In particular,
\[
\mathbb E\tau_{m,k}=
\begin{cases}
1,&k=0,\\
m,&k=1,\\
2+k(m-2)+k^2/m,&2\le k\le m.
\end{cases}
\]

If \(m\to\infty\) and \(k/m\to\alpha\in(0,1]\), then
\[
\frac{\tau_{m,k}}{m^2}\ \Longrightarrow\ \mathcal T_\alpha,
\quad
\mathbb E e^{-s\mathcal T_\alpha}
=\frac{\cosh((1-\alpha)\sqrt{2s}/2)}{\cosh((1+\alpha)\sqrt{2s}/2)}\qquad(s\ge0),
\]
where \(\mathcal T_\alpha\) is the exit time of standard Brownian motion from \([0,1+\alpha]\), started at \(\alpha\). Also \(\mathbb E\tau_{m,k}/m^2\to\alpha\).

In contrast, for any integer sequence \(1\le k=o(m)\),
\[
\mathbb E\tau_{m,k}\sim mk,\qquad
\frac{\tau_{m,k}}{mk}\xrightarrow{\mathbb P}0,
\]
while the rare diffusive time tail has the *nonzero* universal profile
\[
\boxed{\quad
\lim_{m\to\infty}\frac mk\Pr\!\left\{\tau_{m,k}>\lfloor tm^2\rfloor\right\}
=\Phi(t):=4\sum_{j=0}^\infty e^{-(2j+1)^2\pi^2t/2}
\quad}\qquad(t>0).
\]
The series is absolutely convergent for every positive \(t\), and \(\int_0^\infty\Phi(t)\,dt=1\). Thus the dominant contribution to the mean in the sparse-excess regime comes from rare paths lasting on the diffusive \(m^2\) time scale, even though the typical value divided by the mean tends to zero.

## Assumptions and scope

The winner is uniformly chosen among currently nonempty players at *each* discrete round, independently conditional on the current state. The initial holdings differ by at most one, and their values are exactly one or two. Time counts every round, including the last absorbing round. The finite formulas cover all \(m\ge2\), \(0\le k\le m\). The Brownian theorem assumes a fixed positive limit of \(k/m\); the rare-event theorem assumes \(1\le k=o(m)\), allowing bounded \(k\).

## Proof

**1. Complete two-round reduction.** If \(k=0\), the first winner receives every card. Suppose \(k\ge1\). If a two-card player wins the first round (probability \(k/m\)), this winner has \(m+1\) cards and \(k-1\) other players have one card each. If \(k=1\), the game is already absorbed. If \(k\ge2\), the first winner wins round two with conditional probability \(1/k\), again causing immediate absorption. Otherwise a one-card player wins round two with conditional probability \((k-1)/k\); all other singletons disappear, leaving a pair with holdings \((m,k)\). The unconditional probability of this last branch is \((k-1)/m\).

If a one-card player instead wins the first round (probability \((m-k)/m\)), that winner has \(m\) cards and there remain \(k\) one-card players. At round two, with conditional probability \(1/(k+1)\) the large player wins and the game absorbs, while with probability \(k/(k+1)\) a singleton wins and a pair with holdings \((m-1,k+1)\) remains. The latter branch has unconditional probability \(k(m-k)/(m(k+1))\). The probability of both nonabsorbed branches plus their complementary immediate absorption events is one. Every later move of the pair changes the first holding by \(+1\) or \(-1\) with equal probability and stops at \(0\) or \(N\), so it is precisely gambler's ruin. The cases \(k=1\) and \(k=m\) follow by omitting branches whose counts vanish. This proves the exact survival mixture and the first-round exceptions.

**2. Transforms and finite expectations.** The ruin transform \(H_a=\mathbb E z^{G_{N,a}}\) solves \(H_a=(z/2)(H_{a-1}+H_{a+1})\) for interior \(a\), with boundary values \(H_0=H_N=1\). Solving the characteristic equation with \(\cosh\eta=1/z\) gives the displayed hyperbolic-cosine expression, including its continuous value at \(z=1\). Multiplying the absorption probabilities by \(z\) or \(z^2\) and conditioning on the branches yields the generating functions. The classical stopped-martingale calculation gives \(\mathbb EG_{N,a}=a(N-a)\): indeed the difference equation \(u_a=1+(u_{a-1}+u_{a+1})/2\) with \(u_0=u_N=0\) has the unique solution \(u_a=a(N-a)\). Thus for \(k\ge2\),
\[
\mathbb E\tau_{m,k}
=2+\frac{k-1}{m}\,km
 +\frac{k(m-k)}{m(k+1)}\,(k+1)(m-1)
=2+k(m-2)+\frac{k^2}{m}.
\]
For \(k=1\), absorption at time one has probability \(1/m\); otherwise the time is \(1+G_{m+1,1}\), and its mean is \(m\).

**3. Positive-density diffusion.** With \(k/m\to\alpha\in(0,1]\) and \(z=e^{-s/m^2}\), the parameter \(\eta=\operatorname{arcosh}(e^{s/m^2})\) satisfies \(m\eta\to\sqrt{2s}\). Both surviving ruin branches have initial scaled positions tending to \(\alpha\) inside an interval of scaled length \(1+\alpha\). Their total probability tends to one, while their two-round instant-absorption complement tends to zero. The exact transform from Step 2 therefore converges, for all \(s\ge0\), to the displayed Brownian-exit Laplace transform. The continuity theorem for Laplace transforms yields convergence in distribution; the explicit finite mean gives the stated mean limit. This is the Brownian motion with generator \(\tfrac12\,d^2/dx^2\), fixing the diffusion normalization.

**4. Spectral survival formula.** The transition matrix \(K_N\) of the symmetric walk killed at \(0,N\) has sine eigenvectors \(\sin(\pi ja/N)\) and eigenvalues \(\cos(\pi j/N)\), for \(1\le j<N\). Orthogonality and the finite sine sum give the exact identity
\[
q_N(a,h)=\frac2N
\sum_{\substack{1\le j<N\\j\ \mathrm{odd}}}
\sin\!\frac{\pi j a}{N}\,
\cot\!\frac{\pi j}{2N}\,
\left(\cos\!\frac{\pi j}{N}\right)^{h}.
\]
Here the even-index terms vanish because the sum of their eigenvector coordinates is zero. If \(a=a_N\ge1\), \(a_N/N\to0\), and integer \(h_N/N^2\to t>0\), then
\[
\frac{N}{a_N}q_N(a_N,h_N)\to\Phi(t).
\]
For each fixed odd \(j\), multiplying its summand by \(N/a_N\) and taking the limit gives \(4e^{-\pi^2j^2t/2}\). For \(j\le N/2\), \(|\sin(\pi ja_N/N)|\le\pi ja_N/N\) and \(\cot(\pi j/(2N))\le2N/(\pi j)\), so the scaled coefficients have absolute value at most four. The eigenvalue factors are bounded, for all sufficiently large \(N\), by \(e^{-ctj^2}\) with an absolute \(c>0\). This is a summable majorant. For \(j>N/2\), write \(j=N-r\). Then \(\cot(\pi j/(2N))=\tan(\pi r/(2N))\le Cr/N\), while the sine factor is bounded by \(\pi r a_N/N\) because \(a_N\) is integral. Thus the scaled coefficients are \(O(r^2/N^2)\), and the absolute eigenvalue powers are bounded by \(e^{-ct r^2}\). Their entire sum tends to zero. Dominated convergence proves the scaled ruin-survival limit, including the negative-eigenvalue modes.

**5. Rare-event transfer and typical-time collapse.** Suppose \(1\le k=o(m)\). For \(h=\lfloor tm^2\rfloor-2\), Step 4 applies with \(N=m+k\), starting from \(a=k\) or \(a=k+1\). In the exact mixture, after multiplication by \(m/k\), the first branch contributes \(o(1)\), because its scaled prefactor is bounded and \(q_N(k,h)=O(k/N)\). The second branch contributes \(\Phi(t)\), since its prefactor is asymptotic to \(k/(k+1)\) before the survival factor, and \(q_N(k+1,h)\sim(k+1)\Phi(t)/N\). This proves the rare-event tail. The exact expectations from Step 2 imply \(\mathbb E\tau_{m,k}\sim mk\).

For any \(a\ge1\), the reflection principle and the central-binomial estimate for symmetric walk imply the elementary half-line survival bound \(\Pr_a(G_{N,a}>h)\le\Pr_a(T_0>h)\le C a/\sqrt{h+1}\), uniformly in \(N\) and integer \(h\ge1\), with an absolute constant \(C\). Taking \(h=\lfloor\varepsilon mk\rfloor-2\) (which grows for any \(k\ge1\)), this bounds the two-branch mixture by \(O(k/m)+O(\sqrt{k/m})\to0\) for every fixed \(\varepsilon>0\). Hence \(\tau_{m,k}/(mk)\to0\) in probability. Finally, termwise integration by Tonelli and \(\sum_{j\ge0}(2j+1)^{-2}=\pi^2/8\) yields \(\int_0^\infty\Phi(t)dt=1\).

## Verification

A separate Python 3 standard-library checker, `verify_sticky.py`, constructs the **unreduced** finite Markov chain on all reachable positive-holding multisets, including exactly absorbing transitions. It compares complete exact-rational survival probabilities through 32 steps for every \(2\le m\le10\) and \(0\le k\le m\). For every \(2\le m\le8\) and every such \(k\), it also independently solves the full transient-state linear system at two rational transform arguments and the linear mean-time system, comparing the outcomes to the theorem. It returned `EXACT_CHECKS_OK 2205 survival m<=10, t<=32; pgf and mean m<=8`. These are finite diagnostic confirmations; the full-range and limit statements are established by the preceding proof.

Run `python3 verify_sticky.py` with Python 3. The checker needs no external packages, network requests or data files.

## Relationship to prior work

Adjei, Krishnan and Mossel introduced the simple sticky walk and proved general quadratic expected-duration bounds under hypotheses excluding the nearly one-card-per-player regime [1, Definition 2.1 and Corollary 2.4]. Their Remark 3.4 [1, pp. 13–14] already describes the first-two-round reduction **qualitatively**, notes that gambler's ruin controls the endgame, and predicts the \(mk\) scale when \(k=o(m)\). Neither the two-round mechanism nor the classical gambler's-ruin formulas are offered as original facts here. The new statement is the complete finite law and exact means, the continuous-density Brownian limit, and the unusual explicit sparse-excess survival profile showing non-uniform integrability at the mean scale. The primary source's simulation and approximation sections do not provide these statements or their proofs. Bhatia, Chin, Mani and Mossel [2] study the two-player game of War and its gambling-ruin equivalence; the present analysis uses that standard equivalence rather than reclaims it.

## Limitations

The exact formula assumes initial holdings only one or two, uniform winner selection, and all players active initially. It does not establish analogous formulas for three-card starting states, nonuniform winning mechanisms or general sticky random walks. The sparse-excess tail limit holds for each fixed \(t>0\), not uniformly down to \(t=0\), and the Brownian limit excludes \(\alpha=0\), which has a different rare-event scaling. The proof gives no rates for the limiting approximations. Historical priority beyond the inspected literature is not independently certified.

## References

[1] A. Adjei, N. Krishnan, E. Mossel, *Multiplayer Games of War*, arXiv:2409.05201, first posted 8 September 2024, later version 29 June 2026. https://arxiv.org/abs/2409.05201 . Relevant parts: §2.1 (definition), Remark 3.4 (two-round observations), §§4–5 (simulations and approximation), and further directions.

[2] M. Bhatia, B. Chin, N. Mani, E. Mossel, *When Will (Game) Wars End?*, arXiv:2302.03535, first posted 7 February 2023. https://arxiv.org/abs/2302.03535 .
