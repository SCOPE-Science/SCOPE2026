# Sharp majority-occupancy law for median rank-one lattice quadrature

## Finding

Fix an odd prime \(p\geq3\), an odd repetition count \(r\geq1\), and \(s=p-1=2d\). Consider independent unshifted prime rank-one lattice rules in two variables, with generators \(z_1,\ldots,z_r\) drawn uniformly and independently from \(\{1,\ldots,p-1\}^2\). For each generator, put \(S_\ell=z_{\ell,2}z_{\ell,1}^{-1}\pmod p\), represented in \(\{1,\ldots,s\}\), and let \(n_j=\#\{\ell:S_\ell=j\}\). Write the occupancies in descending order as \(n_{(1)}\geq\cdots\geq n_{(s)}\), put \(m=(r+1)/2\), and define

\[
q=\min\left\{k\geq1:\sum_{a=1}^{k}n_{(a)}\geq m\right\}.
\]

On the natural real Fourier-slope subspace

\[
\mathcal T_p=\left\{f_c(x_1,x_2)=\sqrt2\sum_{j=1}^{s}c_j\cos\bigl(2\pi(x_2-jx_1)\bigr):c\in\mathbb R^s\right\},
\]

all functions have exact integral zero, and \(\|f_c\|_{L^2([0,1]^2)}=\|c\|_2\). Let \(M_r(f)\) be the ordinary sample median of the \(r\) lattice integration values. Its **exact realized worst-case absolute error** is

\[
\boxed{\sup_{f\in\mathcal T_p,\ \|f\|_{L^2}\leq1}|M_r(f)|=\sqrt{\frac2q}.}
\]

This yields a full finite-sample distribution: for each integer \(1\leq k\leq\min\{m,d\}\),

\[
\Pr(q=k)=\frac{r!}{s^r}\!\sum_{\substack{a_1+\cdots+a_s=r,\ a_j\geq0\\ A_{k-1}<m\leq A_k}}\frac1{a_1!\cdots a_s!},
\qquad A_k=\sum_{i=1}^{k}a_{(i)},\quad A_0=0,
\]

where \(a_{(i)}\) are the ordered occupancies. In particular, the probability of the maximal error is the exact, disjoint binomial tail

\[
\boxed{\Pr\left(\sup|M_r|=\sqrt2\right)=s\sum_{j=m}^{r}\binom rj\left(\frac1s\right)^j\left(1-\frac1s\right)^{r-j}.}
\]

Every realization satisfies \(q\leq d\), so the realized error is at least \(2/\sqrt s\), regardless of how many generators are drawn. Coupling all repetition counts by prefixes of one infinite independent generator sequence, as odd \(r\to\infty\) this lower bound is attained eventually almost surely:

\[
\boxed{\sup|M_r|\longrightarrow\frac2{\sqrt{p-1}}\quad\text{almost surely}.}
\]

For \(p\geq5\) the probability of not yet attaining this limiting value has the **sharp** exponential decay rate

\[
\boxed{\lim_{\substack{r\to\infty\\r\ \mathrm{odd}}}-\frac1r\log\Pr(q<d)=-\frac12\log\left(1-\frac4{(p-1)^2}\right).}
\]

There is also a fixed, not adaptively selected, smooth integrand displaying the exact breakdown at a half-good generator pool: for any prescribed \(J\subseteq\{1,\ldots,s\}\) with \(|J|=d\), let

\[
f_J=\sqrt{\frac2d}\sum_{j\in J}\cos\bigl(2\pi(x_2-jx_1)\bigr).
\]

It has unit \(L^2\)-norm and integral zero, yet for **every odd \(r\)**,

\[
\boxed{\Pr\!\left(|M_r(f_J)|=\frac2{\sqrt s}\right)=\frac12,\qquad
\Pr(M_r(f_J)=0)=\frac12.}
\]

Thus repeating independent generators cannot decrease this integrand's failure probability below one half at this fixed lattice size. For fixed odd \(r\) and primes \(p\to\infty\), the worst-case error instead tends in probability to \(\sqrt{2/m}\); the probability of no repeated slope, sufficient for exact equality, is \(\prod_{j=0}^{r-1}(1-j/s)\) when \(s\geq r\).

## Assumptions and scope

The target is the **unshifted** \(p\)-node rank-one lattice average

\[
Q_{p,z}(f)=\frac1p\sum_{t=0}^{p-1}f\left(\left\{\frac{tz_1}p\right\},\left\{\frac{tz_2}p\right\}\right),
\quad z_1,z_2\in\{1,\ldots,p-1\}.
\]

There are exactly \(p-1\) admissible slope classes; because both generator coordinates are sampled independently and uniformly from nonzero residues, each slope has probability \(1/(p-1)\), independently across repetitions. The supremum in the realized worst-case error is taken **after** generators are drawn. All Fourier functions in the test subspace are smooth, but its normalized class is the finite-dimensional \(L^2\)-unit ball, **not** a uniformly bounded weighted Korobov ball as \(p\) varies. No randomized lattice shifts, random prime choices, or coefficient-reconstruction algorithm are assumed.

## Proof

**Character reduction.** For \(1\leq j\leq p-1\), the finite root-of-unity sum gives

\[
\frac1p\sum_{t=0}^{p-1}\cos\!\left(\frac{2\pi t(z_2-jz_1)}p\right)
=\mathbf1_{\{z_2\equiv jz_1\pmod p\}}.
\]

The different cosine modes are pairwise orthogonal in \(L^2([0,1]^2)\), and each has squared norm \(1/2\). Consequently \(Q_{p,z}(f_c)=\sqrt2\,c_S\), where \(S\) is its slope class.

**Sharp median variational bound.** Fix the sample and suppose its median of \(c_{S_1},\ldots,c_{S_r}\) is \(v>0\). At least \(m\) sampled coordinates are at least \(v\), and by the definition of \(q\), these samples require at least \(q\) distinct indices. Hence \(\|c\|_2^2\geq qv^2\). Apply the same reasoning to \(-c\) for a negative median. Conversely, take the \(q\) most occupied slope classes, set their coefficients to \(1/\sqrt q\), and set all others to zero. This has coefficient norm one and median \(1/\sqrt q\); multiplying by \(\sqrt2\) proves the exact sharp formula.

**Finite law and the one-class atom.** Occupancy vectors are multinomial, with probability \(r!/(s^r\prod a_j!)\). Summing those meeting the displayed inequalities gives the finite law. Since \(r\) is odd, at most one class contains at least \(m\) draws, so the events of a majority in individual classes are disjoint. Each class count is binomial \(\mathrm{Bin}(r,1/s)\), proving the stated one-class probability.

**Deterministic floor and long-repetition asymptotics.** The largest \(d=s/2\) occupancies sum to at least half the total \(r\), hence to at least \(m\) because \(r\) is odd. Therefore \(q\leq d\). For a fixed \(s\), the strong law gives \(n_j/r\to1/s\) simultaneously. The total of any \(d-1\) classes then tends to \((d-1)/s<1/2\), so eventually no \(d-1\) classes contain a majority: \(q=d\) eventually almost surely.

For the sharp deviation exponent, let \(a=(d-1)/s=1/2-1/s\). The event \(q<d\) is precisely that **some** subset of \(d-1\) slope classes captures at least \(m\) samples. Every fixed such subset has binomial count \(\mathrm{Bin}(r,a)\), hence

\[
\Pr(\mathrm{Bin}(r,a)\geq m)\leq\Pr(q<d)
\leq\binom{s}{d-1}\Pr(\mathrm{Bin}(r,a)\geq m).
\]

For \(s\geq4\), Stirling's formula applied to the binomial tail (or the elementary binomial large-deviation theorem) yields decay exponent \(D(1/2\|a)=-\tfrac12\log[4a(1-a)]=-\tfrac12\log(1-4/s^2)\). The fixed multiplicative factor does not affect the exponent. For \(s=2\), \(q=d=1\) deterministically.

**Half-pool obstruction and large-prime limit.** For \(|J|=d\), the character identity gives \(Q_{p,z}(f_J)=(2/\sqrt s)\mathbf1_{\{S\in J\}}\). Its indicators are independent fair Bernoulli variables. The median is nonzero precisely when at least \(m\) of the \(r\) draws hit \(J\), an event of probability exactly \(1/2\) by odd-binomial symmetry. Finally, for fixed \(r\), no collisions among \(r\) independent uniform slopes has probability \(\prod_{j=0}^{r-1}(1-j/s)\to1\). On that event the minimum covering majority is exactly \(q=m\), establishing the large-prime statement.

## Verification

The standalone file `verify.py` checks actual finite lattice character sums for primes \(3,5,7,11\), independently computes the minimum majority covering number by exhaustive subset enumeration for small prime/repetition combinations, checks the finite-binomial atom and rational example probabilities, and confirms the exact half-pool binomial symmetry. It prints `PASS: 19584 independent finite assertions` using the Python standard library. These checks are finite diagnostics; the general and asymptotic conclusions follow from the proof above, not from extrapolation of test cases.

For example, at \(p=5,r=3\), \(\Pr(q=1)=5/8\). At \(p=7,r=5\), \(\Pr(q=1)=23/108\) and \(\Pr(q=3)=5/54\). Both are checked by complete enumeration of the underlying finite slope samples.

## Relationship to prior work

Goda and L'Ecuyer (2022) define the same independent-generator median rank-one lattice integration rule and prove high-probability worst-case bounds in weighted Korobov spaces. Their Lemma 4 gives the Fourier character aliasing identity used here, and Theorem 5 supplies a smoothness-dependent probabilistic **upper bound**. The current result instead concerns a particular \(p\)-dependent finite Fourier subspace with the \(L^2\)-norm and gives its **exact realized nonlinear worst-case**, complete occupancy law, sharp repetition exponent and fixed-integrand half-pool obstruction. Neither theorem is claimed to contradict the other.

Goda and Krieg (2024) additionally randomize the prime lattice size and study worst-case and randomized integration in weighted Korobov classes. Goda and Suzuki (2025) exhibit a failure of median improvement for a different digital-net scrambling mechanism. Pan and collaborators (2026) study median aggregation for **Fourier-coefficient approximation**, not this integration functional. These works motivate careful distinctions between randomization schemes and error quantifiers; their inspected assertions do not give the present occupancy identity. The underlying character sum, binomial facts and median combinatorics are classical and are not claimed new separately.

## Limitations

The theorem does not establish a lower bound of constant order for any fixed smoothness-normalized Korobov ball as \(p\to\infty\). The test space changes with \(p\), and the high-frequency coefficients may incur substantial smoothness norm. For a fixed \(p\), repeated sampling accesses only \(p-1\) slope classes. The result applies to two dimensions, nonzero-coordinate prime generators, unshifted lattice averages and odd medians only. Its publication novelty is subject to specialist checking of earlier finite-frequency median sampling literature. 

## References

1. T. Goda and P. L'Ecuyer, *Construction-free median quasi-Monte Carlo rules for function spaces with unspecified smoothness and general weights*, arXiv:2201.09413, first public 2022-01-24. https://arxiv.org/abs/2201.09413
2. T. Goda and D. Krieg, *A simple universal algorithm for high-dimensional integration*, arXiv:2411.19164, first public 2024-11-28. https://arxiv.org/abs/2411.19164
3. T. Goda and K. Suzuki, *The median trick does not help for fully nested scrambling*, arXiv:2507.04297, first public 2025-07-06. https://arxiv.org/abs/2507.04297
4. Z. Pan, M. Cai, J. Dick, T. Goda and P. Kritzer, *Worst-case \(L_p\)-approximation of periodic functions using median lattice algorithms*, arXiv:2603.05271, first public 2026-03-05. https://arxiv.org/abs/2603.05271
