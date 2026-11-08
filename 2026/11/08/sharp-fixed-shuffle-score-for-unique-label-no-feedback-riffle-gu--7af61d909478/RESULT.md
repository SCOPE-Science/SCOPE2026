# Sharp fixed-shuffle score for unique-label no-feedback riffle guesses

## Finding

Fix an integer \(k\ge 1\), put \(m=2^k\), and perform \(k\) independent Gilbert–Shannon–Reeds riffle shuffles of the initially ordered \(n\)-card deck. In a no-feedback game, a guess sequence must use every one of the \(n\) labels exactly once. If \(J_i\) is the actual label at position \(i\), define

\[
V_{n,k}=\max_{g\in\mathfrak S_n}\sum_{i=1}^{n}\Pr(J_i=g(i)).
\]

Put \(q_t=t/m\) and \(a_t=q_t(1-q_t)\), for \(0\le t\le m\). Then

\[
\boxed{\lim_{n\to\infty}\frac{V_{n,k}}{\sqrt n}
=C_m=\frac{2}{m^2\sqrt{2\pi}}\sum_{t=0}^{m-1}
\frac1{\sqrt{a_t}+\sqrt{a_{t+1}}}.}
\]

In particular, for one shuffle \(C_2=\sqrt{2/\pi}\), while for two shuffles \(C_4\approx0.337225694841\). An explicit block-interleaved permutation of guesses attains this leading constant; an optimal finite-\(n\) permutation is not claimed.

## Assumptions and scope

The underlying deck contains distinct labels \(1,\ldots,n\), arranged initially in increasing order. Each riffle is unbiased and follows the standard GSR binomial-cut/proportional-interleaving distribution. There is no feedback. The guessing rule is a *permutation*: exactly one guess at each position and no label guessed twice, regardless of earlier outcomes. The number \(k\) of shuffles is fixed as \(n\to\infty\); no uniformity as \(k\) grows is asserted.

For a constructive strategy, write \(n=mL+r_0\), where \(0\le r_0<m\). For every \(0\le t<m\) and \(1\le r\le L\), place guess \(tL+r\) at position \(m(r-1)+t+1\). Place the remaining \(r_0\) labels \(mL+1,\ldots,n\) in the remaining positions in their natural order. The prescribed guesses form a permutation.

## Proof

**1. Exact marginal components.** For \(1\le i,j\le n\), let \(p_{t,i}(j)\) be the mass at \(j\) of

\[
Z_{t,i}=1+\operatorname{Bin}(n-i,q_t)+\operatorname{Bin}(i-1,q_{t+1}),
\]

with the two binomials independent. The GSR position-marginal generating-function identity of Krityakierne and Thanatipanonda gives

\[
A_{i,j}:=\Pr(J_i=j)=\frac1m\sum_{t=0}^{m-1}p_{t,i}(j).
\]

For each component,

\[
\mu_{t,i}=1+\frac{t(n-1)+i-1}{m},\qquad
\sigma^2_{t,i}=(n-i)a_t+(i-1)a_{t+1}.
\]

For \(x\in[0,1]\) set \(v_t(x)=(1-x)a_t+xa_{t+1}\). Its interior is strictly positive, including for endpoint components \(t=0,m-1\). As \(n\to\infty\), a standard Fourier proof of the lattice local central limit theorem for independent bounded Bernoulli arrays yields the following *uniform* facts for every fixed \(\eta>0\): if \(i/n\in[\eta,1-\eta]\) and \(j-\mu_{t,i}=O(1)\), then

\[
p_{t,i}(j)=\frac{1+o(1)}{\sqrt{2\pi n v_t(i/n)}};
\]

and in the same row range \(\sup_j p_{t,i}(j)\le (1+o(1))/\sqrt{2\pi n v_t(i/n)}\). For the latter, note that no individual Bernoulli variance exceeds the total, and the characteristic function obeys \(|1-p+pe^{iu}|^2=1-4p(1-p)\sin^2(u/2)\); Fourier inversion controls the noncentral frequencies. The \(o(1)\) is uniform for the indicated compact ranges of the finitely many \(t\).

**2. Sharp upper bound from column capacities.** A guessing permutation uses each label once, hence

\[
V_{n,k}\le\sum_{j=1}^{n}\max_{1\le i\le n}A_{i,j}.
\]

Fix \(\varepsilon\in(0,1/(4m))\), and restrict to labels for which \(j/n\in(q_t+\varepsilon,q_{t+1}-\varepsilon)\) for exactly one \(t\). Put \(x_j=mj/n-t\), which belongs to \([m\varepsilon,1-m\varepsilon]\). For every competing component \(s\ne t\), the mean \(\mu_{s,i}\) is at distance at least \(\varepsilon n-O(1)\) from \(j\), uniformly over rows \(i\). Hoeffding's inequality therefore bounds its point mass by \(2e^{-c_\varepsilon n}\).

Within the target component, if \(|i/n-x_j|>n^{-2/5}\), its mean is at distance at least a constant times \(n^{3/5}\) from \(j\), and its mass is at most \(2e^{-c_m n^{1/5}}\). Otherwise \(v_t(i/n)=v_t(x_j)+o(1)\). The uniform peak estimate from step 1 and a row with \(i/n=x_j+O(1/n)\), where \(j-\mu_{t,i}=O(1)\), show uniformly over these labels that

\[
\max_i A_{i,j}=
\frac{1+o(1)}{m\sqrt{2\pi n v_t(x_j)}}.
\]

Summing over these interior labels and passing to Riemann sums gives the coefficient

\[
\frac1{m\sqrt{2\pi}}\sum_{t=0}^{m-1}
\int_{q_t}^{q_{t+1}}\frac{dy}{\sqrt{v_t(my-t)}}
=\frac1{m^2\sqrt{2\pi}}\sum_{t=0}^{m-1}\int_0^1\frac{dx}{\sqrt{v_t(x)}}.
\]

Here the integral formula remains valid when an endpoint variance is zero because the singularity is integrable.

**3. Interface columns do not contribute to the leading order.** The two endpoint mixture components are shifted ordinary binomials:

\[
p_{0,i}(j)=\Pr\{\operatorname{Bin}(i-1,1/m)=j-1\},
\]

\[
p_{m-1,i}(j)=\Pr\{\operatorname{Bin}(n-i,1/m)=n-j\}.
\]

For fixed success probability \(1/m\), taking the maximum over the number of trials in the binomial probability and using Stirling's bound proves \(\sup_h\Pr\{\operatorname{Bin}(h,1/m)=r\}\le K_m/\sqrt{r+1}\). Each interior component \(1\le t\le m-2\) has variance at least \(c_m n\) for all rows, so its point masses are uniformly \(O_m(n^{-1/2})\) by Fourier inversion. Consequently

\[
\max_i A_{i,j}\le K_m\bigl(j^{-1/2}+(n-j+1)^{-1/2}+n^{-1/2}\bigr).
\]

The set of labels at distance at most \(\varepsilon n\) from one of the finitely many boundaries \(nq_t\), for \(0\le t\le m\), therefore contributes at most \(O_m((\sqrt\varepsilon+\varepsilon)\sqrt n+1)\) to the column-capacity sum. Taking \(n\to\infty\) and then \(\varepsilon\downarrow0\) proves the desired limsup.

**4. Explicit matching lower bound.** For the permutation described in the assumptions, take \(i=m(r-1)+t+1\) and \(j=tL+r\). In component \(t\), its mean is exactly \(\mu_{t,i}=j+tr_0/m\), differing from \(j\) by at most \(m\). Also, when \(r/L\) stays in a compact subinterval of \((0,1)\), \(i/n=r/L+O_m(n^{-1})\) and \(\sigma^2_{t,i}=n v_t(r/L)+O_m(1)\). The local central limit theorem therefore gives

\[
A_{i,j}\ge \frac{1+o(1)}{m\sqrt{2\pi n v_t(r/L)}}.
\]

Summing over \(t\) and over \(r\) with \(r/L\in[\varepsilon,1-\varepsilon]\), and recalling \(L/n\to1/m\), yields a liminf of at least

\[
\frac1{m^2\sqrt{2\pi}}\sum_{t=0}^{m-1}
\int_\varepsilon^{1-\varepsilon}\frac{dx}{\sqrt{v_t(x)}}.
\]

All omitted score contributions are nonnegative, so monotone convergence as \(\varepsilon\downarrow0\) gives the full integral and matches step 3.

**5. Evaluation of the coefficient.** Since \(v_t(x)=(1-x)a_t+xa_{t+1}\), elementary integration gives

\[
\int_0^1 v_t(x)^{-1/2}\,dx
=\frac2{\sqrt{a_t}+\sqrt{a_{t+1}}},
\]

including the endpoint cases with one zero value by continuity. This proves the displayed finite-sum constant. \(\square\)

## Verification

The included standard-library checker `checks/verify.py` independently builds exact rational position-marginal matrices from the two-binomial mixture, verifies all their row and column normalizations, optimizes the assignment by subset dynamic programming on small decks, and compares the explicit block-interleaved strategy against finite optima and column-capacity upper bounds. It also checks the leading constant in the one-shuffle case and numerical values for several fixed shuffle counts. The finite checks do not certify the uniform local central limit theorem or the infinite asymptotic theorem; those are proved above.

## Relationship to prior work

Krityakierne and Thanatipanonda (2025) supply the exact GSR marginal mixture; their no-feedback strategies allow guesses to be repeated, and hence optimize row by row. Their subsequent November 3, 2026 preprint settles the repeated-guess optimal score at fixed shuffle count, \(2\sqrt{n/((m-1)\pi)}+O_m(1)\), again using unrestricted repeated labels. The present rule instead requires *one use of every label*, coupling choices across positions. Its answer is the new column-capacity/matching constant \(C_m\), approached by an explicit interleaved assignment. For one shuffle the new leading coefficient \(\sqrt{2/\pi}\) is strictly below the repeated-guess coefficient \(2/\sqrt\pi\). Kuba and Panholzer (2024), following Ciucu (1998), likewise analyze the unrestricted no-feedback game rather than this bijective strategy restriction. The local central limit and binomial concentration ingredients are classical and are not claimed as new.

## Limitations

The theorem assumes fixed \(k\) and the standard unbiased GSR model, and proves only first-order expected-score asymptotics. It does not characterize the exact finite-deck optimal matching or the distribution of the number of correct guesses. Generic assignment algorithms can find the finite optimum but do not by themselves prove the displayed asymptotic constant. Historical-priority risk remains from potential earlier equivalent results for constrained guessing or special probability-matrix matchings; no complete uniqueness claim is made.

## References

- T. Krityakierne and T. A. Thanatipanonda, *A generating function framework for the no-feedback card guessing game after riffle shuffles*, AIMS Mathematics **10** (2025), 24257–24269, DOI: https://doi.org/10.3934/math.20251075. First publicly published 2025-10-23.
- T. Krityakierne and T. A. Thanatipanonda, *Optimal no-feedback card guessing after a fixed number of riffle shuffles*, arXiv:2611.04339v1, first posted 2026-11-03. https://arxiv.org/html/2611.04339v1.
- M. Kuba and A. Panholzer, *On card guessing games: Limit law for no feedback one-time riffle shuffle*, Advances in Applied Mathematics **156** (2024), 102689, DOI: https://doi.org/10.1016/j.aam.2024.102689.
- M. Ciucu, *No-feedback card guessing for dovetail shuffles*, Annals of Applied Probability **8** (1998), 1251–1269, DOI: https://doi.org/10.1214/aoap/1028903379.
