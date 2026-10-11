# Conditioning on high complexity preserves probabilistic-randomness decay regimes
## Finding

Let \(\mathbf m\) be the universal semimeasure on \(\mathbb N\), extended additively to subsets as in Vovk, and let \(K\) denote prefix complexity. Put
\[
H_a=\{\omega\in\mathbb N:K(\omega)\ge a\}.
\]
For any set \(E\subseteq\mathbb N\), define its normalized universal share among high-complexity objects by
\[
\mathbf Q_a(E)=\frac{\mathbf m(E\cap H_a)}{\mathbf m(H_a)}.
\]

Let \(g:\mathbb N\to[0,\infty)\) be computable and increasing, with
\[
g(k)\le k
\]
for all sufficiently large \(k\). Then there is a constant \(c>0\) such that, for every computable increasing function
\[
h:\mathbb N\to[1,\infty),
\qquad
h(a)\to\infty,
\]
we have
\[
\boxed{
\mathbf Q_a\!\left(\left\{\omega:\beta_\omega(g(K(\omega)))>c\right\}\right)
=
o\!\left(
h(a)\sum_{k\ge a}2^{-g(k)}
\right).
}
\]

Thus passing from Vovk's absolute universal-measure bounds to the literal conditional proportion among objects satisfying \(K(\omega)\ge a\) costs less than **any prescribed computable divergent factor**.

This preserves the qualitative decay regimes of the source.

If
\[
g(k)=\theta k,
\qquad
0<\theta<1,
\]
then for every rational \(\varepsilon\) with
\[
0<\varepsilon<\theta
\]
we have
\[
\boxed{
\mathbf Q_a\!\left(\beta_\omega(\theta K(\omega))>c\right)
=
o\!\left(2^{-(\theta-\varepsilon)a}\right).
}
\]

If
\[
g(k)=k^\theta,
\qquad
0<\theta<1,
\]
then for every rational
\[
0<\varepsilon<1
\]
we have
\[
\boxed{
\mathbf Q_a\!\left(\beta_\omega(K(\omega)^\theta)>c\right)
=
o\!\left(a^{1-\theta}2^{-(1-\varepsilon)a^\theta}\right).
}
\]

For the logarithmic-power regime
\[
g(k)=(\log k)^\theta,
\qquad
\theta>1,
\]
then the conditional bad share remains superpolynomially small: for every fixed rational \(p>0\),
\[
\mathbf Q_a\!\left(\beta_\omega((\log K(\omega))^\theta)>c\right)
=
o(a^{-p}).
\]

Finally, if
\[
g(k)=\theta\log k,
\qquad
\theta>1,
\]
then for every rational
\[
0<\varepsilon<\theta-1
\]
we have
\[
\boxed{
\mathbf Q_a\!\left(\beta_\omega(\theta\log K(\omega))>c\right)
=
o\!\left(a^{-(\theta-1-\varepsilon)}\right).
}
\]

The source describes probabilistically nonrandom objects as a negligible minority among high-complexity objects. The theorem above makes that statement literally conditional and quantifies the normalization loss.

## Assumptions and scope

The notation \(\beta_\omega\) is Vovk's best-fit function. The universal measure \(\mathbf m\) is the additive extension of a fixed universal lower semicomputable semimeasure on \(\mathbb N\). Its tail is
\[
\tau(a)=\mathbf m(\{n:n>a\}).
\]

The statement uses two results proved in Vovk's 2026 notes.

First, the high-complexity population satisfies
\[
\frac{\tau(a)}{c_1}
\le
\mathbf m(H_a)
\le
c_1\tau(a)
\]
for an absolute constant \(c_1>1\).

Second, for every computable increasing \(g\) with \(g(k)\le k\) eventually, Vovk's master theorem gives constants \(c_2,c_3>0\) such that
\[
\mathbf m\!\left(
\left\{\omega:K(\omega)\ge a,\ \beta_\omega(g(K(\omega)))>c_2\right\}
\right)
\le
c_3\sum_{k\ge a}2^{-g(k)}.
\]

The companion note proves the exceptional slowness of \(\tau\): if \(f:\mathbb N\to(0,\infty)\) is computable, decreasing, and tends to zero, then
\[
\frac{\tau(a)}{f(a)}\to\infty.
\]

All logarithms are binary, as in the source.

The theorem is asymptotic. It does not give effective thresholds at which the displayed little-\(o\) bounds begin, because the universal-semimeasure tail itself is noncomputably slow.

## Proof

Define
\[
B_g(a)=
\left\{\omega:K(\omega)\ge a,\ \beta_\omega(g(K(\omega)))>c_2\right\}.
\]
Vovk's master theorem gives
\[
\mathbf m(B_g(a))
\le
c_3 S_g(a),
\qquad
S_g(a):=\sum_{k\ge a}2^{-g(k)}.
\]

By the high-complexity tail comparison,
\[
\mathbf m(H_a)\ge\frac{\tau(a)}{c_1}.
\]
Therefore
\[
\mathbf Q_a(B_g(a))
=
\frac{\mathbf m(B_g(a))}{\mathbf m(H_a)}
\le
c_1c_3\frac{S_g(a)}{\tau(a)}.
\]

Now let \(h:\mathbb N\to[1,\infty)\) be any computable increasing function with \(h(a)\to\infty\), and set
\[
f(a)=\frac1{h(a)}.
\]
Then \(f\) is computable, positive, decreasing, and tends to zero. The companion-note tail lemma gives
\[
\frac{\tau(a)}{f(a)}\to\infty.
\]
Equivalently,
\[
\frac1{\tau(a)}=o(h(a)).
\]
Substituting this into the previous inequality proves
\[
\mathbf Q_a(B_g(a))
=
o\!\left(h(a)S_g(a)\right).
\]
This is the master conditional estimate.

For the linear regime
\[
g(k)=\theta k,
\]
Vovk sums a geometric series to obtain
\[
S_g(a)=O(2^{-\theta a}).
\]
Taking
\[
h(a)=2^{\varepsilon a}
\]
proves
\[
\mathbf Q_a(B_g(a))
=
o\!\left(2^{-(\theta-\varepsilon)a}\right).
\]

For
\[
g(k)=k^\theta,
\qquad
0<\theta<1,
\]
the source proves
\[
S_g(a)=O\!\left(a^{1-\theta}2^{-a^\theta}\right).
\]
Taking
\[
h(a)=2^{\varepsilon a^\theta}
\]
gives
\[
\mathbf Q_a(B_g(a))
=
o\!\left(a^{1-\theta}2^{-(1-\varepsilon)a^\theta}\right).
\]

For
\[
g(k)=(\log k)^\theta,
\qquad
\theta>1,
\]
the source's bound is
\[
S_g(a)
=
O\!\left(a^{1-(\log a)^{\theta-1}}\right).
\]
For any prescribed rational \(p>0\), choose an integer \(q>p\) and take
\[
h(a)=a^q.
\]
Then
\[
h(a)S_g(a)
=
O\!\left(a^{q+1-(\log a)^{\theta-1}}\right)
=
o(a^{-p}),
\]
so the normalized bad share is still superpolynomially small.

Finally, for
\[
g(k)=\theta\log k,
\qquad
\theta>1,
\]
the source proves
\[
S_g(a)=O(a^{1-\theta}).
\]
Taking
\[
h(a)=a^\varepsilon
\]
with rational
\[
0<\varepsilon<\theta-1
\]
gives
\[
\mathbf Q_a(B_g(a))
=
o\!\left(a^{-(\theta-1-\varepsilon)}\right).
\]

## Verification

The proof was reconstructed directly from the exact statements of Proposition 1 and Theorem 2 in the September 2026 note and Lemma 2 in the August 2026 companion note.

The only normalization step is
\[
\frac{\mathbf m(B_g(a))}{\mathbf m(H_a)}
\le
c_1c_3\frac{S_g(a)}{\tau(a)}.
\]
The companion lemma then applies to
\[
f=1/h.
\]
No estimate of \(\tau\) by a particular elementary function is assumed. This is important: \(\tau\) decays more slowly than **every** computable decreasing function tending to zero, not merely more slowly than logarithmic examples.

The four specialized rates use exactly the series estimates appearing in Vovk's Corollaries 3--6. The superpolynomial specialization is checked by observing that
\[
(\log a)^{\theta-1}\to\infty,
\]
so the exponent
\[
q+1-(\log a)^{\theta-1}
\]
eventually lies below every prescribed negative constant.

No finite experiment or empirical estimate of Kolmogorov complexity is used.

## Relationship to prior work

Vovk's September note gives absolute universal-measure bounds for the bad high-complexity set and explicitly says that the “vast majority” of high-complexity objects are probabilistically random. It also contrasts the fast decay of the bad-set measure with the extremely slow decay of the total high-complexity measure.

The note does not divide those quantities to state a normalized conditional theorem. Its Proposition 1 points to the companion note for the behavior of the tail \(\tau\), while the companion note's Lemma 2 proves that \(\tau\) dominates every computable decreasing-to-zero rate.

Combining those two ingredients yields a stronger interpretation of “vast majority”: after conditioning on \(K(\omega)\ge a\), the normalization penalty is smaller than every prescribed computable divergent factor. In particular, exponential and stretched-exponential decay retain arbitrarily close exponents, superpolynomial decay remains superpolynomial, and polynomial decay retains every strictly smaller exponent.

Targeted searches using the source title, best-fit-function terminology, conditional universal measure, high-complexity conditioning, and the universal-semimeasure tail did not locate this normalized statement.

## Limitations

The theorem does not improve Vovk's absolute numerator bounds. It extracts a conditional consequence by combining them with the unusually slow denominator tail.

The little-\(o\) bounds are generally noneffective. The universal-semimeasure tail has no computable asymptotic decay rate of the usual kind.

The conditional result does not make the source's upper bounds sharp. The optimality results in the September note remain subject to the same gaps already discussed there.

The theorem is stated for Vovk's structureless setting, prefix complexity, and best-fit functions. Analogous normalized statements for plain complexity, structure functions, MDL functions, or probability-measure models require separate verification of the corresponding numerator and denominator estimates.

## References

[1] Vladimir Vovk, “The universal measure of probabilistically nonrandom objects,” arXiv:2609.13513, first posted 11 September 2026.

[2] Vladimir Vovk, “The universal measure of nonstochastic objects,” arXiv:2608.27098, first posted 27 August 2026.

[3] Alexander Shen, Vladimir A. Uspensky, and Nikolai Vereshchagin, *Kolmogorov Complexity and Algorithmic Randomness*, American Mathematical Society, 2017.
