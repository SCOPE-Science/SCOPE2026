# Half-normal sum limit for optimal no-feedback guessing after multiple riffle shuffles

## Finding
Fix an integer \(k\ge2\), and put \(a=2^k\). Independently perform \(k\) Gilbert–Shannon–Reeds riffle shuffles on the initially ordered deck \(1,\ldots,n\). Predict every card without feedback, permitting repeated guesses, and write \(X_{n,k}\) for the number correctly predicted by any expectation-optimal deterministic strategy. Then, as \(n\to\infty\),

\[
\frac{X_{n,k}}{\sqrt n}\ \Longrightarrow\ \frac{|Z_1|+|Z_2|}{\sqrt{2(a-1)}}
\ \stackrel d=\ \frac{\max(|Z'_1|,|Z'_2|)}{\sqrt{a-1}},
\]

where the four displayed standard normal variables may be taken independent within each pair. Every fixed positive integer moment converges. In particular, for \(x\ge0\),

\[
\lim_{n\to\infty}\Pr(X_{n,k}/\sqrt n\le x)=
\operatorname{erf}\!\left(x\sqrt{\frac{a-1}{2}}\right)^2,
\qquad
\lim_{n\to\infty}\frac{\operatorname{Var}(X_{n,k})}{n}
=\frac{1-2/\pi}{a-1}.
\]

For \(x<0\) the limiting distribution function is zero. The mean limit is \(2/\sqrt{\pi(a-1)}\), agreeing with the previously established leading optimal expectation.

## Assumptions and scope
The parameter \(k\) is fixed as \(n\to\infty\). A GSR riffle has a binomial half-deck cut followed by an order-preserving uniform interleaving. Different shuffles are independent. Guesses are fixed in advance; repeated values are allowed. The optimal prediction sequence, proved for sufficiently large \(n\) in Krityakierne–Aek Thanatipanonda (2026, Theorem 1.1), is

\[
g_n(i)=\begin{cases}
\lfloor i/a\rfloor+1,&1\le i\le h,\\
n-\lfloor(n+1-i)/a\rfloor,&h<i\le n,
\end{cases}\qquad h=\lfloor(n+1)/2\rfloor.
\]

Their Corollary 4.1 establishes that, for \(k\ge2\) and large \(n\), another expectation-optimal strategy can differ from this one only at the middle card of an odd deck. Such a change alters the score by at most one, so the theorem covers every deterministic expectation-optimal strategy. Randomizing independently between optimal strategies does not change the limit either.

## Proof
**1. Packet representation and localization.** The composition law for GSR shuffles makes \(k\) independent binary riffles one \(a\)-packet riffle. Equivalently, assign output positions independent uniform packet labels \(R_1,\ldots,R_n\in\{0,\ldots,a-1\}\), and fill the output in the order prescribed by those labels, maintaining the initial order inside each packet. Define

\[
N_r=\#\{i:R_i=r\},\quad P_r=\sum_{s<r}N_s,\quad C_r(i)=\#\{t\le i:R_t=r\}.
\]

If \(R_i=r\), the original card at position \(i\) is exactly \(P_r+C_r(i)\). This packet description has the marginal generating function (2.1)–(2.2) of the cited 2026 source; it can also be verified directly from the GSR composition law.

For every \(i\le h\), the proposed guess is at most \(\lfloor h/a\rfloor+1\). On the event \(N_0>\lfloor h/a\rfloor+1\), all these guesses belong to the first original packet, so a correct top-half guess necessarily has \(R_i=0\). By reflection, on \(N_{a-1}>\lfloor(n-h)/a\rfloor+1\) every correct bottom-half guess necessarily has \(R_i=a-1\). Since each count has the binomial law \(\mathrm{Bin}(n,1/a)\) and the thresholds are asymptotic to \(n/(2a)\), a Chernoff bound gives for their joint good event \(E_n\)

\[
\Pr(E_n^c)\le C_a e^{-c_an}\quad\text{for constants }C_a,c_a>0.
\]

Consequently the difference between the total score and the sum of first-packet top-half hits and last-packet bottom-half hits vanishes in every fixed moment after division by \(\sqrt n\): it is at most \(n\mathbf1_{E_n^c}\).

**2. Exact discrete occupation representation.** Read the independent labels in the top half from left to right. The waiting times \(G_1,G_2,\ldots\) between successive occurrences of label zero are independent geometric random variables on \(\{1,2,\ldots\}\) with success probability \(p=1/a\). Write \(T_j=G_1+\cdots+G_j\). The \(j\)th original card in the first packet is correctly predicted exactly when its position satisfies \(\lfloor T_j/a\rfloor+1=j\), or

\[
W_j=T_j-aj\in A_a=\{-a,-a+1,\ldots,-1\}.
\]

For \(J_n=\lfloor h/a\rfloor\), every such match with \(j\le J_n\) occurs within the top half, and any further match has \(j=J_n+1\). Thus the top-half extreme-packet contribution differs by at most one from

\[
L_{J_n}=\sum_{j=1}^{J_n}\mathbf1_{\{W_j\in A_a\}}.
\]

Reverse the labels in the last \(n-h\) output positions. An identical formula holds for the last-packet contribution, with \(J'_n=\lfloor(n-h)/a\rfloor\), and with a new geometric waiting sequence. These two contributions are independent because they are functions of disjoint sets of iid output labels.

**3. Occupation moment lemma.** Let \(G_j\) be iid geometric with mean \(a\ge2\), and \(W_j=\sum_{s=1}^j(G_s-a)\). Put \(\sigma^2=\operatorname{Var}(G_1-a)=a(a-1)\). Then for any fixed nonempty finite set \(A\subset\mathbb Z\) of cardinality \(b\),

\[
\frac1{\sqrt J}\sum_{j=1}^{J}\mathbf1_{\{W_j\in A\}}
\ \Longrightarrow\ \frac b\sigma |Z|,
\]

with convergence of all fixed positive integer moments, where \(Z\) is standard normal.

Here is a direct moment proof, including the needed local limit estimate. The increment characteristic function is

\[
\phi(t)=\frac{e^{-iat}pe^{it}}{1-(1-p)e^{it}},\qquad p=1/a.
\]

Its only unit-modulus point in \([-\pi,\pi]\) is zero, and \(\phi(t)=1-\sigma^2t^2/2+O(|t|^3)\) there. Fourier inversion, splitting into a small neighborhood of zero and its complement, gives uniformly over fixed integers \(z\)

\[
\Pr(W_m=z)=\frac{1+o(1)}{\sigma\sqrt{2\pi m}},
\qquad \sup_z\Pr(W_m=z)\le \frac C{\sqrt m}\quad(m\ge1).
\]

For each fixed \(r\ge1\), expand the falling factorial moment of the occupation count over strictly increasing times \(1\le t_1<\cdots<t_r\le J\) and states \(x_1,\ldots,x_r\in A\). The Markov property makes the summand a product of transition probabilities at the \(r\) time gaps. The uniform \(Cm^{-1/2}\) bound dominates contributions with small gaps, while the local limit applies when every gap is a positive fraction of \(J\). A Riemann sum then yields

\[
\lim_{J\to\infty}\frac{\mathbb E[(L_J)_r]}{J^{r/2}}
=\frac{r!b^r}{\sigma^r(2\pi)^{r/2}}
\int_{0<t_1<\cdots<t_r<1}
\frac{dt_1\cdots dt_r}{\sqrt{t_1(t_2-t_1)\cdots(t_r-t_{r-1})}}
=\frac{r!b^r}{\sigma^r2^{r/2}\Gamma(1+r/2)}.
\]

The Dirichlet integral equals \(\pi^{r/2}/\Gamma(1+r/2)\). Terms corresponding to repeated visit times contribute \(O(J^{(r-1)/2})\), by the same local bound. Therefore these are also the limiting ordinary moments. As \(\mathbb E|Z|^r=r!/[2^{r/2}\Gamma(1+r/2)]\), the limiting moments are those of \((b/\sigma)|Z|\). The half-normal law is moment-determinate (it has a finite moment-generating function near zero), proving the lemma and moment convergence.

**4. Independent halves and the distribution function.** Apply the lemma with \(A=A_a\), hence \(b=a\). As \(J_n/n\to1/(2a)\) and \(J'_n/n\to1/(2a)\), the two independent contributions divided by \(\sqrt n\) converge jointly, with moments, to two independent \(|Z|/\sqrt{2(a-1)}\) variables. The localization error in Step 1 and the at-most-one boundary discrepancies vanish in all scaled moments. This establishes the asserted sum limit.

For independent standard normals \(Z_1,Z_2\), an orthogonal rotation gives
\( |Z_1|+|Z_2|\stackrel d=\sqrt2\max(|Z'_1|,|Z'_2|)\), which implies the squared-error-function distribution. Direct half-normal moments give the stated mean and variance coefficient.

## Verification
`CHECKER.py` uses the original source's finite-sample marginal mixture formula and exact rational arithmetic to compare the packet-label representation with exhaustive output-label enumeration for three small instances. It additionally checks the pathwise occupation identity on fixed-seed simulated decks for \(a=2,4,8\), and compares simulated means and variances with their exact asymptotic targets. Run `python3 CHECKER.py` using only the Python standard library. The deterministic finite checks corroborate the representation and normalization; the proof above supplies the infinite-sample conclusion.

## Relationship to prior work
Krityakierne–Aek Thanatipanonda (2026) prove the optimal prediction rule and expected-score asymptotic for every fixed number of riffle shuffles; their Section 6 explicitly presents the score distribution for fixed \(k\ge2\) as an open question. The present result settles the fixed-\(k\) first-order distribution by exploiting a joint packet-label representation rather than combining the one-position marginals. Kuba–Panholzer (2024) obtain a one-riffle distributional limit; this is the known \(k=1\) boundary case and is not claimed new. The 2025 generating-function paper provides marginal distributions, not this dependence-level law. The standard Fourier/local-time moment argument is a classical method; the contribution is the rigorous reduction of the optimal multishuffle guessing score to two independent occupations and its explicit distributional identification.

## Limitations
The number of shuffles \(k\) must remain fixed as \(n\to\infty\); the result does not cover \(k\) growing with deck size, feedback strategies, non-GSR shuffles or the exact finite-sample score distribution. The proof relies on the cited optimal-strategy theorem for sufficiently large decks, and on usual GSR composition. The finite checker is not a substitute for the proof. Broader historical equivalence in card-guessing literature remains a possible priority risk. No independent audit or external validation has been performed.

## References
1. T. Krityakierne and T. A. Thanatipanonda, *Optimal no-feedback card guessing after a fixed number of riffle shuffles* (2026), arXiv:2611.04339v1, https://arxiv.org/html/2611.04339v1, first publicly posted 2026-11-03. Especially Theorem 1.1, Corollary 4.1, equations (2.1)–(2.2), and Section 6.
2. M. Kuba and A. Panholzer, *On card guessing games: Limit law for no feedback one-time riffle shuffle*, Advances in Applied Mathematics 156 (2024), 102689, https://doi.org/10.1016/j.aam.2024.102689; preprint https://arxiv.org/abs/2308.15782.
3. T. Krityakierne and T. A. Thanatipanonda, *A generating function framework for the no-feedback card guessing game after riffle shuffles*, AIMS Mathematics 10 (2025), 24257–24269, https://doi.org/10.3934/math.20251075.
4. D. Bayer and P. Diaconis, *Trailing the dovetail shuffle to its lair*, Annals of Applied Probability 2 (1992), 294–313, https://doi.org/10.1214/aoap/1177005705.
