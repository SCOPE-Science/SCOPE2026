# An exact first-hit law for optimal no-feedback riffle guessing

## Finding

Fix an integer \(k\geq1\), put \(a=2^k\), and consider an initially ordered deck of \(n\) distinct cards after \(k\) independent Gilbert–Shannon–Reeds riffle shuffles. Use the canonical no-feedback guessing sequence whose guesses in the top half are \(g_i=\lfloor i/a\rfloor+1\); for each fixed \(k\), this is an expected-score-optimal sequence for all sufficiently large \(n\), by Krityakierne and Thanatipanonda (2026). Let \(T_{n,k}\) be the index of the first correct guess anywhere in this sequence, with \(T_{n,k}=n+1\) if no guess is correct. Define, for every integer \(t\geq0\),

\[
h_a(t)=\binom{t}{\lfloor t/a\rfloor}\left(\frac1a\right)^{\lfloor t/a\rfloor}
\left(1-\frac1a\right)^{t-\lfloor t/a\rfloor}.
\]

**Exact-prefix approximation.** For every \(n\geq1\) and integer \(0\leq t\leq\lfloor n/2\rfloor\), the canonical sequence satisfies

\[
\left|\Pr(T_{n,k}>t)-h_a(t)\right|\leq \exp\left(-\frac{n}{8a}\right).
\]

**Sharp first-hit tail.** With \(k\) fixed, uniformly along every integer sequence \(t=t(n)\to\infty\) with \(t\leq\lfloor n/2\rfloor\),

\[
\Pr(T_{n,k}>t)\sim\frac{a}{\sqrt{2\pi(a-1)t}}.
\]

In particular, for \(H_n=\lfloor n/2\rfloor\),

\[
\Pr(T_{n,k}>H_n)\sim\frac{a}{\sqrt{\pi(a-1)n}},\qquad
\mathbb E\min(T_{n,k},H_n)\sim\frac{a}{\sqrt{\pi(a-1)}}\sqrt n.
\]

These asymptotics distinguish a first correct guess that is tight in probability from its diverging square-root-order expected waiting time when observed only up to the middle of an increasingly large deck.

**Exact auxiliary law.** Let \(D_1,D_2,\ldots\) be independent uniform packet labels in \(\{0,\ldots,a-1\}\), let \(S_i=\sum_{j\leq i}\mathbf1_{\{D_j=0\}}\), and define \(T_a=\inf\{i\geq1:D_i=0,\ S_i=\lfloor i/a\rfloor+1\}\). Then \(\Pr(T_a>t)=h_a(t)\) **exactly for every integer** \(t\geq0\). Consequently \(T_a\) is almost surely finite but has infinite mean. At each positive multiple of \(a\), its point mass is zero; all other point masses are obtained from \(h_a(t-1)-h_a(t)\).

## Assumptions and scope

The shuffle law is the standard unbiased GSR riffle shuffle; repeated guesses are allowed, and the player receives no feedback. The cutoff \(\lfloor n/2\rfloor\) keeps the analysis in the canonical top-half portion of the optimal sequence. The finite-deck inequalities apply to the specified canonical sequence at every \(n\); for \(n\) above the source's fixed-\(k\) optimality threshold they describe an optimal expected-score strategy. The result does not assert that a strategy maximizing the *probability of an early correct guess* is identical to the expected-total-score-optimal strategy. For \(k=1\), other expected-score-optimal tie choices exist, and are not covered by the asserted waiting-time law.

## Proof

**1. Independent packet words and an exponentially rare obstruction.** The convolution property of the GSR shuffle identifies \(k\) successive binary riffles with one unbiased \(a\)-packet riffle. Generate the latter by independent uniform marks \(D_1,\ldots,D_n\) in \(\{0,\ldots,a-1\}\). Conditional on the packet sizes, the marked output word interleaves the \(a\) initially consecutive, individually ordered packets uniformly. Write \(N_0=\#\{i:D_i=0\}\); then \(N_0\sim\operatorname{Bin}(n,1/a)\).

Fix \(0\leq t\leq\lfloor n/2\rfloor\), and put \(r=\lfloor t/a\rfloor\). On \(\{N_0>r\}\), every card from packet \(1\) or later has label at least \(N_0+1>r+1\), whereas all first-\(t\) guesses have labels at most \(r+1\). Thus a correct guess during these positions must come from packet \(0\). At position \(i\) its actual label is \(S_i\), so it matches exactly if \(D_i=0\) and \(S_i=\lfloor i/a\rfloor+1\).

The integer-valued walk \(B_i=i-aS_i\), started at \(B_0=0\), has increments \(+1\) on a nonzero mark and \(-(a-1)\) on a zero mark. The first crossing into \(B_i<0\) is precisely the first indicated match: before a crossing one has \(S_{i-1}\leq\lfloor(i-1)/a\rfloor\), and an increase by one can exceed \(\lfloor i/a\rfloor\) only by exactly one. Hence the event of no first-\(t\) match agrees on \(\{N_0>r\}\) with \(\{B_i\geq0\text{ for every }1\leq i\leq t\}\).

Since \(r\leq n/(2a)\), the standard binomial multiplicative Chernoff inequality gives

\[
\Pr(N_0\leq r)\leq\Pr\left(N_0\leq\frac{n}{2a}\right)
\leq\exp\left(-\frac{n}{8a}\right).
\]

The auxiliary walk uses only the first \(t\) independent marks, which have exactly the same law as the corresponding prefix of the length-\(n\) marked word. The required error estimate therefore follows once its survival probability has been evaluated.

**2. A generalized ballot count.** For integers \(a\geq2\), \(t\geq0\), and \(0\leq j\leq\lfloor t/a\rfloor\), put \(h=t-aj\geq0\). The number of length-\(t\) words with exactly \(j\) steps \(-(a-1)\), all other steps \(+1\), and every partial sum nonnegative is

\[
N_{t,j}=\frac{h+1}{t+1}\binom{t+1}{j}.
\]

Indeed, prepend a \(+1\) to turn such a nonnegative path into a length-\(t+1\) path with **strictly positive** partial sums and final height \(h+1\). Conversely, any such strictly positive path must start with \(+1\) and can be reduced in this way. The classical cycle lemma for integer steps bounded above by \(+1\) says that among cyclic rotations of a word with total sum \(h+1>0\), exactly \(h+1\) rotations have strictly positive partial sums (counting rotations with their starting indices). Averaging over all \(\binom{t+1}{j}\) words yields the stated formula. This combinatorial lemma is classical; no novelty is asserted for it independently of its application.

**3. Exact critical survival identity.** Put \(p=1/a\), \(q=1-p\), and \(r=\lfloor t/a\rfloor\). Weighting the count by the independent marks gives

\[
\begin{aligned}
\Pr(B_i\geq0\ \forall i\leq t)
&=\sum_{j=0}^{r}\frac{t-aj+1}{t+1}\binom{t+1}{j}p^j q^{t-j}\\
&=\frac1q\left[\Pr(X_{t+1}\leq r)-\Pr(X_t\leq r-1)\right],
\end{aligned}
\]

where \(X_s\sim\operatorname{Bin}(s,p)\) and the second equality uses \(ap=1\) and the binomial identity for truncated first moments. Coupling \(X_{t+1}=X_t+Y\) for an independent \(\operatorname{Bernoulli}(p)\) variable \(Y\), the difference in brackets equals \(q\Pr(X_t=r)\). This proves

\[
\Pr(B_i\geq0\ \forall i\leq t)=\Pr(X_t=r)=h_a(t).
\]

Combining with step 1 gives the finite-deck claim. The same equality for an infinite iid packet word is exact, since no finite-packet obstruction exists in the definition of \(T_a\).

**4. Tails and mean.** With \(r=\lfloor t/a\rfloor\), the deviation between \(r\) and the binomial mean \(t/a\) is bounded by one. Stirling's formula (equivalently the local binomial central limit theorem) therefore yields, for each fixed \(a\),

\[
h_a(t)=\frac{1+o(1)}{\sqrt{2\pi t(1/a)(1-1/a)}}
=\frac{a(1+o(1))}{\sqrt{2\pi(a-1)t}}.
\]

Because \(t\leq n/2\), the exponentially small error is negligible compared with the binomial point probability as \(t\to\infty\). At \(H_n=\lfloor n/2\rfloor\), substitute \(t=H_n\). For the mean use \(\mathbb E\min(T_{n,k},H_n)=\sum_{t=0}^{H_n-1}\Pr(T_{n,k}>t)\), the uniform error bound from step 1, and \(\sum_{t=1}^{H-1}t^{-1/2}\sim2\sqrt H\). In the infinite-word version, \(h_a(t)\to0\) implies \(T_a<\infty\) almost surely, whereas the divergent sum \(\sum_t h_a(t)\) implies \(\mathbb ET_a=\infty\).

Finally, for \(t=am-1\), the ratios of the two binomial point probabilities give \(h_a(am-1)=h_a(am)\) for every \(m\geq1\). Therefore the infinite-word first-hit probability at time \(am\) is zero, as claimed.

## Verification

The accompanying self-contained Python program \(\texttt{verify.py}\) checks independent dynamic-programming path counts against the cycle-lemma formula and the binomial atom, checks the zero-hazard residue class, and exhaustively enumerates small direct packet shuffles to compare actual finite-deck first-hit probabilities with their binomial reference and packet-size obstruction. It uses exact integers and rational arithmetic; no floating-point test is used as a proof of the infinite statements. Invoke \(\texttt{python verify.py}\) with Python 3. Analytical steps 1–4 above establish the theorem for the stated full ranges.

## Relationship to prior work

Krityakierne and Thanatipanonda, arXiv:2611.04339v1 (November 3, 2026), establish the canonical optimal guess locations and the expected total score for fixed shuffle depth. Their earlier AIMS Mathematics paper (2025) supplies marginal generating functions. Krityakierne et al. (2022/2023) and Kuba–Panholzer (2023/2024) derive moments and score-limit laws; Kuba–Panholzer explicitly identify waiting times for correct guesses as a possible further question in their conclusion. These results do not state the sharp first-correct waiting-time law, its exact binomial-atom representation, or its uniform finite-deck error.

The generalized cycle lemma and local central limit theorem are classical inputs, not claimed new. In particular the ordinary ballot path count already covers the auxiliary two-step walk; the new connection is the precise identification of that walk with the canonical shuffle-guessing first hit, together with the finite-packet coupling and quantitative consequences. Existing results for unique-label guesses or complete-feedback games concern different guessing policies. A previously unpublished or unlocated equivalent first-hit evaluation remains possible.

## Limitations

The results require fixed shuffle depth when asserting optimality, unbiased riffles, the specified tie choice in the top half, and cutoffs no later than the top-half midpoint. They do not classify first-hit behavior beyond the midpoint, for adaptive or alternate optimal strategies, or when shuffle depth grows with deck size. The all-time exact identity applies to the auxiliary infinite packet word; for a finite deck the stated error is explicit but generally not zero. No independent mathematical audit has been performed.

## References

1. T. Krityakierne and T. A. Thanatipanonda, *Optimal no-feedback card guessing after a fixed number of riffle shuffles*, arXiv:2611.04339v1, first posted November 3, 2026, https://arxiv.org/html/2611.04339v1.
2. T. Krityakierne and T. A. Thanatipanonda, *A generating function framework for the no-feedback card guessing game after riffle shuffles*, AIMS Mathematics 10 (2025), 24257–24269, https://doi.org/10.3934/math.20251075.
3. M. Kuba and A. Panholzer, *On card guessing games: Limit law for no feedback one-time riffle shuffle*, arXiv:2308.15782v1 (August 30, 2023), https://arxiv.org/pdf/2308.15782; Advances in Applied Mathematics 156 (2024), 102689.
4. T. Krityakierne, P. Siriputcharoen, T. A. Thanatipanonda and C. Yapolha, *No-feedback Card Guessing Game: Moments and distributions under the optimal strategy*, arXiv:2209.04276v2, https://arxiv.org/pdf/2209.04276.
5. T. Krityakierne and T. A. Thanatipanonda, *No Feedback? No Worries! The art of guessing the right card*, arXiv:2205.08793v1, https://arxiv.org/pdf/2205.08793.
6. M. Ciucu, *No-feedback card guessing for dovetail shuffles*, Annals of Applied Probability 8 (1998), 1251–1269, https://doi.org/10.1214/aoap/1028903379.
7. A. Dvoretzky and Th. Motzkin, *A problem of arrangements*, Duke Mathematical Journal 14 (1947), 305–313, https://doi.org/10.1215/S0012-7094-47-01423-3 (cycle lemma).
