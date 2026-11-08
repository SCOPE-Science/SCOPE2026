# Winner-conditioned transport for competing Bernoulli runs

## Finding

Let \(r\ge 2\) be an integer and \(0<p<1\), \(q=1-p\). In an infinite sequence of independent Bernoulli trials, let \(\tau_r\) be the first time at which either \(r\) consecutive heads or \(r\) consecutive tails occurs, and let \(C\in\{H,T\}\) indicate which run wins. Define
\[
S_r(s)=\sum_{j=0}^{r-1}s^j,\qquad
\mu_r(s)=\frac{\sum_{j=0}^{r-1}j s^j}{S_r(s)}.
\]
There is a single nonnegative integer-valued random variable \(W_r\) such that, on a suitable common coupling,
\[
\tau_r\mid (C=H)\ \overset{d}=\ r+W_r+Z_q,
\qquad
\tau_r\mid (C=T)\ \overset{d}=\ r+W_r+Z_p,
\]
where \(W_r\) is independent of \(Z_q,Z_p\), and \(\Pr(Z_s=j)=s^j/S_r(s)\) for \(j=0,\ldots,r-1\). For \(p>q\), the first conditional time is strictly smaller in ordinary stochastic order. The exact one-Wasserstein distance, using absolute time difference as its transport cost, is
\[
\boxed{W_1\bigl(\mathcal L(\tau_r\mid C=H),\mathcal L(\tau_r\mid C=T)\bigr)
=\left|\mu_r(p)-\mu_r(q)\right|<\frac{r-1}{2}.}
\]
The uniform upper bound is sharp as a supremum over \(0<p<1\): it is approached as \(p\uparrow 1\) or \(p\downarrow 0\), but not attained for interior probabilities. At \(p=q\), the conditional laws coincide.

## Assumptions and scope

The trials are i.i.d., the two forbidden runs have the same length \(r\ge 2\), and both letter probabilities are strictly positive. The random time includes the terminal trial; the winner is unambiguous. The conditional distributions are proper because any one of the disjoint blocks of \(r\) trials can terminate the process with uniformly positive probability. The theorem does not claim the same ordering for unequal run lengths, dependent trials or more than two competing patterns.

## Proof

Put
\[
A(z)=\sum_{j=1}^{r-1}(pz)^j,\qquad B(z)=\sum_{j=1}^{r-1}(qz)^j,
\qquad a=A(1),\ b=B(1).
\]
Any prefix strictly before the winning head-run consists of alternating maximal short head- and tail-runs. Its short-run sequence is either \((HT)^k\) or \(T(HT)^k\), where \(k\ge0\), and every indicated run has length between \(1\) and \(r-1\). Thus a unique block decomposition gives the marked probability generating functions
\[
G_H(z)=\mathbb E[z^{\tau_r}\mathbf1_{\{C=H\}}]
=\frac{(pz)^r(1+B(z))}{1-A(z)B(z)},
\qquad
G_T(z)=\frac{(qz)^r(1+A(z))}{1-A(z)B(z)}.
\]
These rational generating functions, and the marked waiting-time method itself, are known in broader competing-pattern theory; their derivation here isolates a consequence about the *conditional transport order*.

Since
\[
ab=(1-p^{r-1})(1-q^{r-1})<1,
\]
normalization at \(z=1\) is legitimate, and
\[
\Pr(C=H)=\frac{p^r(1+b)}{1-ab},\qquad
\Pr(C=T)=\frac{q^r(1+a)}{1-ab}.
\]
To identify the common factor, take an integer-valued \(J\) with
\[
\Pr(J=k)=(1-ab)(ab)^k,\quad k\ge0,
\]
and independent random variables \(U_i,V_i\in\{1,\ldots,r-1\}\) with
\[
\Pr(U_i=j)=\frac{p^j}{a},\qquad
\Pr(V_i=j)=\frac{q^j}{b},\quad 1\le j\le r-1.
\]
All variables in these families are mutually independent. Set \(W_r=\sum_{i=1}^J(U_i+V_i)\), with the empty sum zero. Its generating function is
\[
\mathbb E[z^{W_r}]
=\frac{1-ab}{1-A(z)B(z)}.
\]
For each \(s\), define \(Z_s\) with generating function \((1+\sum_{j=1}^{r-1}(sz)^j)/S_r(s)\), choosing the pair \((Z_p,Z_q)\) independently of \(W_r\); the two residuals need not be mutually independent. Dividing \(G_H,G_T\) by their values at one proves the two asserted conditional distributional identities, with the **same** \(W_r\).

For \(s>t>0\), the likelihood ratio
\[
\frac{\Pr(Z_s=j)}{\Pr(Z_t=j)}
=\frac{S_r(t)}{S_r(s)}\left(\frac{s}{t}\right)^j
\]
is strictly increasing in \(j\). Therefore \(Z_s\) strictly dominates \(Z_t\) in ordinary stochastic order. The quantile coupling allows \(Z_p\ge Z_q\) almost surely if \(p>q\), with strict inequality with positive probability. Add the same independent \(r+W_r\) to both variables. Strict distributional ordering follows: already at time \(r\), the first conditional cumulative probability is larger when \(p>q\).

For one-Wasserstein distance, any coupling must have expected absolute difference at least the absolute difference of means. Our ordered common-noise coupling achieves this lower bound. Because the common summand cancels, the distance is exactly \(|\mathbb E Z_p-\mathbb E Z_q|=|\mu_r(p)-\mu_r(q)|\). The function \(\mu_r(s)\) is strictly increasing on \(s>0\), since
\[
\frac{d}{d\log s}\mu_r(s)=\operatorname{Var}(Z_s)>0
\]
for \(r\ge2\). Moreover \(0<\mu_r(s)<(r-1)/2\) for \(0<s<1\): at \(s=1\) the distribution is uniform on \(\{0,\ldots,r-1\}\), while for \(s<1\) it is strictly stochastically smaller. The stated sharp bound and limiting equality as \(p\to1\), \(q\to0\) follow.

For context, when \(p>q\) is fixed and \(r\to\infty\), \(1-ab\sim p^{r-1}\) and \(\mathbb E(U_i+V_i)\to1/(pq)\); hence both conditional means grow as \(1/(qp^r)\), whereas their exact difference converges to \((p-q)/(pq)\). Thus even exponentially long waiting times can differ by a bounded, explicitly quantified number of trials after conditioning on the winning run.

## Verification

The accompanying standalone \(\texttt{verify.py}\) constructs an absorbing-state dynamic program tracking the live terminal run, independently of the alternating-block derivation. It compares the resulting rational probabilities with coefficient extraction from the displayed marked generating functions for \(2\le r\le7\) and seven rational choices of \(p\), through time \(34\). It separately enumerates all binary strings up to length \(10\) for specified smaller parameter cases and checks conditional stochastic order, winner normalization, and rational sharp-bound examples. Execution produced **4,657 passing exact assertions**. These finite checks supplement, but do not replace, the infinite-parameter proof above.

Run with standard Python 3: \(\texttt{python3 verify.py}\). No third-party dependencies are required.

## Relationship to prior work

Marked probability generating functions and conditioned means for first-occurring patterns are already covered by Ostaszewska and Zajkowski (2013, Theorem 2.3 and Proposition 2.6), by earlier generating-function methods of Uchida (1998), and by prior success/failure run work. Freiberg, Heuberger and Prodinger (2015) give general waiting-time generating-function tools via Smirnov words. The narrower contribution assessed here is the **common-random-summand factorization and its exact sharp winner-conditioned Wasserstein/stochastic-order consequence**, not a new solution of the generic sooner-waiting-time problem. The related 2001 book chapter on sooner/later run occurrences, which advertises conditional distributions, could not be examined in full, and may contain implicit or explicit overlap.

## Limitations

The stochastic comparison is established only for equal target run lengths under independent identically distributed binary trials. No result is asserted for the likelihood-ratio order after adding \(W_r\), and the upper bound on Wasserstein distance is a strict supremum, not an attained maximum at an admissible parameter. The claim of literature distinctness is qualified by inaccessible historical conditional-run material; an independent audit has not been performed.

## References

- U. Ostaszewska and K. Zajkowski, *On the waiting time till some patterns occur in i.i.d. sequences* (2013), arXiv:1302.4859v1, https://arxiv.org/html/1302.4859v1 (public 2013-02-20).
- M. Uchida, *On Generating Functions of Waiting Time Problems for Sequence Patterns of Discrete Random Variables*, Ann. Inst. Statist. Math. **50** (1998), 655–671, https://www.ism.ac.jp/editsec/aism/pdf/050_4_0655.pdf.
- S. Aki, N. Balakrishnan and S. G. Mohanty, *Sooner and later waiting time problems for success and failure runs in higher order Markov dependent trials*, Ann. Inst. Statist. Math. **48** (1996), 773–787, https://www.ism.ac.jp/editsec/aism/pdf/048_4_0773.pdf.
- U. Freiberg, C. Heuberger and H. Prodinger, *Application of Smirnov Words to Waiting Time Distributions of Runs* (2015), arXiv:1503.08096, https://arxiv.org/abs/1503.08096.
- N. Balakrishnan and M. V. Koutras, *Runs and Scans with Applications* (2001), chapter “Sooner/Later Run Occurrences”, DOI:10.1002/9781118150467.ch6 (chapter full text not inspected).
