# Local cycle–record covariance in a uniformly random permutation

## Finding

Let \(\Pi\) be uniform on permutations of \(\{1,\ldots,n\}\). Let \(C_n\) be its number of disjoint cycles, including fixed points, and let \(I_{n,i}\) indicate that its entry at position \(i\) is strictly larger than all preceding entries. For **every** integer \(n\ge2\) and every \(1\le i\le n\),

\[
\operatorname{Cov}(C_n,I_{n,i})=\frac{i-1}{i^2\binom ni}.
\]

In particular, with \(R_n=\sum_{i=1}^n I_{n,i}\),

\[
\operatorname{Cov}(C_n,R_n)=\sum_{i=2}^n\frac{i-1}{i^2\binom ni}>0.
\]

More precisely, as \(n\to\infty\),

\[
\operatorname{Cov}(C_n,R_n)=\frac1n+\frac1{2n^2}+O\!\left(\frac{\log n}{n^3}\right),\qquad
\operatorname{Corr}(C_n,R_n)\sim\frac1{n\log n}.
\]

The two whole statistics have the **same marginal distribution** (the unsigned Stirling distribution), yet their same-permutation covariance is positive and asymptotically small. Every nonnegative weighted record score whose weight is positive at at least one position \(i\ge2\) has positive covariance with \(C_n\).

## Assumptions and scope

The permutation \(\Pi\) is uniformly sampled from the \(n!\) bijections of \(\{1,\ldots,n\}\). Its one-line form is \((\Pi(1),\ldots,\Pi(n))\). An upper record occurs at \(i\) if \(\Pi(i)=\max_{1\le j\le i}\Pi(j)\); the first entry is a deterministic record. The count \(C_n\) is for the ordinary disjoint-cycle decomposition **of this same bijection**, not of a Foata-transformed permutation. Write \(H_m=\sum_{j=1}^m 1/j\), with \(H_0=0\), and \((a)_{\underline k}=a(a-1)\cdots(a-k+1)\). All finite identities are exact; no limiting random-permutation model is assumed.

## Proof

**1. Expose the first \(i\) images.** Let \(\mathcal F_i\) be the information in \(\Pi(1),\ldots,\Pi(i)\). Draw those directed arrows from their domain labels to their images. The resulting partial permutation digraph consists of complete directed cycles and paths; denote by \(K_i\) the count of completed cycles. Exactly \(n-i\) path components remain, each with one missing outgoing arrow and one missing incoming arrow. A uniformly random completion is a uniformly random matching between path ends and starts, equivalently a uniformly random permutation of \(n-i\) path components. Its cycles correspond bijectively to the further completed cycles. Thus

\[
\mathbb E[C_n\mid\mathcal F_i]=K_i+H_{n-i}.
\]

This also holds at \(i=n\), where there are no uncompleted paths. As \(I_{n,i}\) is \(\mathcal F_i\)-measurable,
\(\operatorname{Cov}(C_n,I_{n,i})=\operatorname{Cov}(K_i,I_{n,i})\).

**2. Count completed cycles.** For each \(1\le k\le i\), the number of distinct directed cycles of length \(k\) supported on vertices in \(\{1,\ldots,i\}\) is \((i)_{\underline k}/k\). The probability that any one prescribed cycle appears in a uniform permutation is \(1/(n)_{\underline k}\). By linearity,

\[
\mathbb E K_i=\sum_{k=1}^i\frac{(i)_{\underline k}}{k(n)_{\underline k}}.
\]

Also \(\mathbb P(I_{n,i}=1)=1/i\).

**3. Count completed cycles jointly with the record event.** Fix a prescribed completed \(k\)-cycle. If it uses the domain position \(i\) and \(k\ge2\), it makes \(I_{n,i}=1\) impossible: an earlier domain inside that cycle takes the value \(i\), greater than the value at \(i\). If its support lies entirely in \(\{1,\ldots,i-1\}\), all its images are below \(i\). Among the remaining \(i-k\) prefix-image positions at least one takes a value \(\ge i\), hence the largest prefix image is at one of these positions. By symmetry of the unconstrained positions, its probability of being at position \(i\) is \(1/(i-k)\).

There is one exceptional completed cycle using position \(i\): the fixed point \(\Pi(i)=i\). It is a record exactly when all \(i-1\) preceding images are less than \(i\). The joint probability of these events equals \(1/[i\binom ni]\). Summing contributions of prescribed cycles yields

\[
\begin{aligned}
\mathbb E[K_iI_{n,i}]
&=\sum_{k=1}^{i-1}\frac{(i-1)_{\underline k}}{k(n)_{\underline k}(i-k)}+\frac1{i\binom ni}\\
&=\frac1i\sum_{k=1}^{i-1}\frac{(i)_{\underline k}}{k(n)_{\underline k}}+\frac1{i\binom ni}.
\end{aligned}
\]

The final \(k=i\) term of \(\mathbb E K_i\) equals \(1/[i\binom ni]\). Subtracting \(\mathbb E K_i/i\) therefore gives

\[
\operatorname{Cov}(K_i,I_{n,i})
=\left(1-\frac1i\right)\frac1{i\binom ni}
=\frac{i-1}{i^2\binom ni},
\]

including \(i=1\), for which both sides vanish. Summation proves the global covariance and positivity claims.

**4. Asymptotics and marginal comparison.** The \(i=n\) contribution is \((n-1)/n^2\), the \(i=n-1\) contribution is \((n-2)/[n(n-1)^2]=n^{-2}+O(n^{-3})\), and the \(i=2\) contribution is \(1/[2n(n-1)]=(2n^2)^{-1}+O(n^{-3})\). For \(3\le i\le n-2\), split off the terminal \(i=n-2\) term (which is \(O(n^{-3})\)). On the interior \(3\le i\le n-3\), the binomial coefficient is at least \(\binom n3\), and \((i-1)/i^2\le1/i\), so the total interior contribution is \(O((\log n)/n^3)\). These estimates give the displayed expansion (the finitely many small \(n\) do not matter).

The classical Foata bijection implies that \(C_n\) and \(R_n\) separately have the unsigned-Stirling distribution; equivalently each has the distribution of a sum of independent Bernoulli variables with success probabilities \(1,1/2,\ldots,1/n\). Hence

\[
\operatorname{Var}(C_n)=\operatorname{Var}(R_n)=H_n-H_n^{(2)}\sim\log n,
\]

where \(H_n^{(2)}=\sum_{i=1}^n i^{-2}\). Combining this with the covariance expansion proves the correlation asymptotic. Linear covariance and the strict positivity at all \(i\ge2\) establish the weighted-score assertion.

## Verification

Run `python3 verify.py` from the folder containing this document and the standalone verifier. It uses only the Python standard library, exact integer and rational arithmetic, exhaustively enumerates all permutations for \(1\le n\le9\), compares all position-specific covariances and their totals, and independently checks the conditional path-completion identity for every exposed prefix injection through \(n=6\). The executed verifier reported **2472 exact assertions passed**. The unrestricted theorem rests on the combinatorial proof above, not on finite enumeration.

## Relationship to prior work

Foata's fundamental transformation equates the *marginal* counts of cycles and upper records but transforms one permutation into another; that equidistribution does not identify the joint behavior of these two statistics on the **same** permutation. Mahmoud's discussion of records and cycles explicitly distinguishes this point. Gnedin's record-statistic constructions and Gnedin–Gorin's record-dependent measures exploit the classical record/cycle correspondence but study different distributional and coherence questions. Neither inspected statement gives the displayed local cross-covariance or position-dependent concentration. The difference from a previously known cycle–inversion covariance is also substantive: a record event is a maximum across a whole prefix, not one pairwise inversion indicator.

## Limitations

This concerns uniform permutations only; it does not establish the same formula under Ewens, Mallows, or other nonuniform measures. The covariance result does not imply positive association or a stochastic ordering for arbitrary nonlinear functions of the cycle count and full record process. The historical novelty comparison is qualified: a general multivariate enumeration of both statistics might implicitly contain the formula even if it is not explicitly identified in the references consulted. No independent audit is claimed.

## References

1. A. Gnedin, *Coherent random permutations with record statistics*, arXiv:math/0611538v1, first public 17 November 2006; especially §§1–2. https://arxiv.org/pdf/math/0611538
2. A. Gnedin and V. Gorin, *Record-dependent measures on the symmetric groups*, arXiv:1202.3680, first public 16 February 2012; introduction and record-dependent distributions. https://arxiv.org/pdf/1202.3680
3. H. M. Mahmoud, *Sorting: A Distribution Theory*, Wiley, 2000; §1.10 on records, cycles, and Foata's fundamental correspondence, Propositions 1.8–1.9. ISBN 0-471-32710-7.
4. R. A. Fisher and F. Yates, *Statistical Tables for Biological, Agricultural and Medical Research*, 1938, for foundational permutation sampling context (not used as a novel theorem premise).
