# An inverse-size total-variation rate for critical random-to-top fixed points

## Finding

Fix \(c>0\). From the ordered deck \((1,\ldots,n)\), perform \(r_n=\lfloor cn\rfloor\) independent moves, each choosing a card uniformly by label and placing it first. Let \(F_n\) count the cards in their original positions after these moves. Put \(a=1-e^{-c}\), let \(X\sim\operatorname{Poisson}(a)\), and independently let \(Y\) be geometric on \(\{0,1,\ldots\}\) with \(\Pr(Y=j)=a(1-a)^j\). There is a finite constant \(C_c\), depending only on \(c\), such that for every sufficiently large integer \(n\),
\[
\boxed{d_{\mathrm{TV}}\bigl(\mathcal L(F_n),\mathcal L(X+Y)\bigr)\le C_c/n.}
\]
This is a quantitative total-variation strengthening of the previously established weak convergence to the same Poisson–geometric convolution. The proof identifies cancellation of the first-order fluctuation of the number of distinct cards moved; directly replacing that random number by its mean yields only a weaker square-root error.

## Assumptions and scope

Here \(d_{\mathrm{TV}}(P,Q)=\frac12\sum_{j\ge0}|P\{j\}-Q\{j\}|\). The moves are by *uniformly selected labels* with replacement, the initial deck is the identity, \(c\in(0,\infty)\) is held fixed, and \(n\to\infty\). The geometric variable counts failures before the first success. The constant need not be uniform as \(c\downarrow0\). Neither a sharp leading error constant nor an extension to biased move-to-front walks is asserted.

## Proof

**1. Exact conditional representation.** Let \(K\) be the number of distinct card labels selected during the \(r_n\) moves. Conditional on \(K=k\), the selected labels occupy the first \(k\) positions in a uniform random order and constitute a uniformly chosen \(k\)-subset of \([n]\); all other labels occur increasingly. Write \(J=n-\max\{\text{selected labels}\}\) and let \(H\) count fixed positions among the first \(k\). Then \(F_n=H+J\) exactly. For integers \(0\le j\le n-k\),
\[
 \Pr(J=j\mid K=k)=\frac{\binom{n-j-1}{k-1}}{\binom nk}.
\]
For \(j<n-k\), the largest selected label \(m=n-j>k\) cannot occupy a fixed position. Removing it leaves a uniform injection of \(t=k-1\) entries into \([m-1]\), and its number of fixed coordinates has exactly the conditional law of \(H\). In the endpoint case \(j=n-k\), the selected set is \([k]\) and the prefix is a uniform permutation of length \(k\).

**2. Uniform partial-injection Poisson lemma.** For integers \(1\le t\le m\), let \(V_{t,m}\) be the number of fixed coordinates in a uniform injective word of length \(t\) over \([m]\), and put \(\lambda=t/m\). Its falling-factorial moments satisfy
\[
 \mathbb E (V_{t,m})_s=(t)_s/(m)_s\quad(0\le s\le t),
\]
with moment zero for \(s>t\). For every \(s\ge0\),
\[
 0\le\lambda^s-\mathbb E(V_{t,m})_s\le
 \frac{s(s-1)}{2t}\lambda^s.
\]
Indeed, for \(s\le t\), factor the ratio into \(\prod_{i=0}^{s-1}(1-i/t)/(1-i/m)\): each factor is in \([0,1]\) and differs from one by at most \(i/t\); use the union bound for the product. If \(s>t\), the displayed upper bound holds because \(s(s-1)/(2t)\ge1\). Inclusion-exclusion inversion for factorial moments and the triangle inequality give
\[
 d_{\mathrm{TV}}\bigl(\mathcal L(V_{t,m}),\operatorname{Poisson}(\lambda)\bigr)
 \le \frac12\sum_{s\ge0}\frac{2^s}{s!}\left|\mathbb E(V_{t,m})_s-\lambda^s\right|
 \le \frac{\lambda^2e^{2\lambda}}{t}\le \frac{e^2}{t}.
\]
This argument also covers uniform full permutations when \(t=m\).

**3. Geometric coupling and conditional error.** Put \(p=k/n\) and \(q=1-p\). Given \(J\ge j\), the probability that \(J\ge j+1\) is \((n-k-j)/(n-j)\) for \(j<n-k\). Couple this sequence of survival tests to those of a zero-index geometric variable \(Y_p\) with survival probability \(q\) using common uniforms. The discrepancy in the test at index \(j\) is \(pj/(n-j)\le j/n\). Summing under the geometric survival law yields
\[
 d_{\mathrm{TV}}(\mathcal L(J\mid K=k),\mathcal L(Y_p))
 \le \frac1n\sum_{j\ge0}j q^j=\frac{q}{np^2}.
\]
For \(2\le k<n\) and \(j<n-k\), the lemma approximates \(H\mid(J=j,K=k)\) by \(\operatorname{Poisson}((k-1)/(n-j-1))\) with error at most \(e^2/(k-1)\). The Poisson-law total-variation distance is at most the difference between its parameters, and
\[
\left|\frac{k-1}{n-j-1}-\frac{k}{n}\right|\le \frac{j+2}{n}.
\]
Furthermore \(\mathbb E[J\mid K=k]=(n-k)/(k+1)\le n/k\), and the exceptional endpoint event has probability \(1/\binom nk\le1/n\). Consequently, by conditional coupling, for \(2\le k<n\),
\[
 d_{\mathrm{TV}}\bigl(\mathcal L(F_n\mid K=k),Q_p\bigr)
 \le \frac{q}{np^2}+\frac{e^2}{k-1}+\frac1k+\frac3n,
 \qquad Q_p:=\operatorname{Poisson}(p)*\operatorname{Geom}(p).
\]
For \(k=n\), the ordinary permutation Poisson bound \(e^2/n\) gives the same coarse upper estimate. In particular, uniformly over \(k\ge an/2\) and sufficiently large \(n\), the conditional error is at most
\[
 \frac1n\left(\frac4{a^2}+\frac{4e^2+2}{a}+3\right).
\]

**4. Occupancy concentration.** Let \(P=K/n\). Standard occupancy indicators give
\[
 \mathbb EP=1-(1-1/n)^{r_n},\qquad
 |\mathbb EP-a|\le\frac{1+c}{n},\qquad
 \operatorname{Var}(P)\le\frac1{4n}.
\]
The variance bound uses the nonpositive covariance between occupancy indicators of distinct boxes. The mean bound follows from \(0\le-\log(1-1/n)-1/n\le 1/[2n(n-1)]\) and \(|r_n/n-c|\le1/n\). In particular, for sufficiently large \(n\), Chebyshev gives
\[
 \Pr(P<a/2)\le\frac4{a^2n}.
\]
Averaging the conditional bound in step 3, bounding total variation trivially by one on \(P<a/2\), shows
\[
 d_{\mathrm{TV}}\bigl(\mathcal L(F_n),\mathbb E Q_P\bigr)
 \le\frac1n\left(\frac8{a^2}+\frac{4e^2+2}{a}+3\right).
\]
The notation \(\mathbb E Q_P\) denotes the probability measure obtained by averaging the masses of \(Q_P\) over the distribution of \(P\).

**5. First-order cancellation in the occupancy mixture.** Regard \(Q_p\) as an \(\ell^1(\mathbb Z_{\ge0})\)-valued differentiable function of \(p\in(0,1]\). For Poisson masses \(h_p\), \(\|h_p'\|_1\le2\) and \(\|h_p''\|_1\le4\), by convolution with \(\delta_1-\delta_0\). For geometric masses \(g_p(j)=p(1-p)^j\), direct differentiation yields \(\|g_p'\|_1\le2/p\) and \(\|g_p''\|_1\le4/p^2\). Therefore
\[
 \|Q_p'\|_1\le2+2/p,\qquad
 \|Q_p''\|_1\le4+8/p+4/p^2.
\]
Set \(\Delta=P-a\) and \(M_a=4+16/a+16/a^2\). On \(P\ge a/2\), Taylor's theorem in \(\ell^1\) gives
\[
 \|Q_P-Q_a-\Delta Q_a'\|_1\le\tfrac12 M_a\Delta^2.
\]
On its complement, the same remainder is at most \(4+2/a\), since \(|\Delta|\le1\). **The linear term is averaged, not bounded by its absolute value:**
\[
 \mathbb E[\Delta Q_a']=(\mathbb EP-a)Q_a'=O_c(n^{-1}).
\]
Moreover \(\mathbb E\Delta^2\le [1/4+(1+c)^2]/n\). Hence
\[
 d_{\mathrm{TV}}(\mathbb E Q_P,Q_a)
 \le\frac1n\left[(1+1/a)(1+c)
 +\frac{M_a}{4}\bigl(1/4+(1+c)^2\bigr)
 +(2+1/a)\frac4{a^2}\right].
\]
Combining steps 4 and 5 proves the theorem. For example, the sum of the two displayed coefficients is a valid explicit \(C_c\) for all sufficiently large \(n\). Every expectation and inequality is uniform in the relevant integer parameters; finite computations are not needed for the infinite bound.

## Verification

The self-contained Python standard-library program `checks/verify.py` compares exact shuffle-history distributions with the occupancy-mixture/partial-injection formula, exhaustively checks suffix and fixed-point conditional laws for all ordered partial permutations through eight labels, verifies the partial-injection Poisson inequality on sampled sizes, and computes exact finite fixed-point distributions at several critical shuffle counts. Run `python checks/verify.py` from this directory; expected output is in `checks/output.txt`. The finite assertions corroborate the exact combinatorics, while the proof in steps 2–5 supplies the uniform asymptotic total-variation bound.

## Relationship to prior work

Clay [1], Sections 4–5, gives the exact uniform-prefix shuffle representation and establishes the Poisson–geometric *weak limit* at \(r_n\sim cn\); Section 8 explicitly identifies the convergence rate as an interesting open direction. The present contribution is the inverse-size **total-variation** estimate for the same natural limit and a proof that uses the cancellation of occupancy fluctuations. A published result, *Four-way rare–Gaussian factorization and a hidden covariance in random-to-top shuffling* [2], strengthens the joint qualitative limit but explicitly does not supply a convergence rate, and a published study of descent–inversion fluctuations [3] treats other observables. A related fixed-step Luce-ranking result [5] gives total-variation convergence to a Poisson law for a different fully sampled permutation measure, but no quantitative rate for the present partially moved deck. Pehlivan [4] studies card-guessing and finite-time positional/expectation questions without deriving this distributional rate. These comparisons concern implication of actual statements, not merely matching titles; they do not establish global priority against unindexed literature.

## Limitations

The bound holds for each fixed positive \(c\) under uniform moves from the identity. The constant can become large for small \(c\); the statement does not claim a sharp coefficient, optimality of the exponent, a uniform-in-\(c\) theorem, a multivariate rate, or extension to biased card-selection probabilities.

## References

1. A. Clay, *On the statistics of random-to-top shuffles*, arXiv:2603.09008v1, first publicly submitted 2026-03-09, https://arxiv.org/html/2603.09008v1. Material examined: Sections 1, 4–5, and 8.
2. *Four-way rare–Gaussian factorization and a hidden covariance in random-to-top shuffling*, publicly accessible mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-four-way-rare-gaussian-factorization-and-a-hidden-covariance-in--a1f81953daaa. Material examined: full RESULT.md, especially Finding, Proof, and Limitations.
3. *Occupancy-mediated joint Gaussian fluctuations of descents and inversions in random-to-top shuffles*, publicly accessible mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-occupancy-mediated-joint-gaussian-fluctuations-of-descents-and-i--7cc85a6a6c85. Material examined: full RESULT.md.
4. L. Pehlivan, *No Feedback Card Guessing for Top to Random Shuffles*, arXiv:1006.1321 (2010), https://arxiv.org/abs/1006.1321; and the 2009 doctoral work referenced in [1].
5. *Poisson fixed points for finite-step Luce rankings*, publicly accessible mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-poisson-fixed-points-for-finite-step-luce-rankings--54d919a68dd2. Material examined: full RESULT.md.
