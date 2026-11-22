# Exact asymmetric-Markov subsequence growth and its sharp correlation ordering

## Finding

Let \(X_1,X_2,\ldots\) be a stationary binary first-order Markov chain with transition probabilities \(p=\Pr(X_{i+1}=1\mid X_i=0)\) and \(q=\Pr(X_{i+1}=0\mid X_i=1)\), where \(0<p,q\le1\). For each \(n\ge0\), let \(D_n\) be the number of **distinct nonempty scattered-subsequence words** of \(X_1\cdots X_n\), not the number of their embeddings. Write \(s=p+q\), \(v=pq\), and \(L(z)=1-(1-s)z\). Then the exact expectation at **every** length is given by the rational generating function

\[
\boxed{\sum_{n\ge0}\mathbb E[D_n]z^n=
\frac{zL(z)\big[s+(s^2-2s+2v)z-s(s-1)z^2\big]}
{s(1-z)\big[(1-z)^2L(z)^2-vz^2\big]}.}
\]

In particular its exponential growth rate exists, is explicit, and has no quartic radicals:

\[
\boxed{\Lambda(p,q):=\lim_{n\to\infty}(\mathbb E[D_n])^{1/n}
=1+\frac{\sqrt{(s-\sqrt v)^2+4\sqrt v}-(s-\sqrt v)}{2}.}
\]

Fix any stationary one-frequency \(\theta\in(0,1)\). All stationary two-state chains with this frequency have \(p=\theta s\), \(q=(1-\theta)s\), and \(0<s\le s_*=1/\max\{\theta,1-\theta\}\). **The growth rate is strictly increasing in \(s\)**. Consequently its unique maximum at fixed \(\theta\) occurs at \(s=s_*\), where the less frequent symbol cannot repeat consecutively (or both symbols alternate when \(\theta=1/2\)). The i.i.d. source has \(s=1\): every positively correlated chain with the same stationary frequency (\(s<1\)) has a lower growth rate, and every negatively correlated one (\(s>1\)) has a higher rate.

This is one integrated theorem: a closed expectation law for the asymmetric source and a sharp ordering of its exponential diversity at fixed stationary composition.

## Assumptions and scope

A subsequence is obtained by deleting zero or more positions without reordering the retained symbols. Different embeddings of the same subsequence string are counted once. The empty subsequence is excluded. The Markov chain starts in its unique stationary law \(\pi_0=q/s\), \(\pi_1=p/s\). The transition parameters are real and strictly positive, with self-transition probabilities \(1-p\) and \(1-q\), possibly zero. All expectations are over the random host word; no almost-sure statement about individual hosts is asserted.

The parameter \(s\) is the sum of the two one-step switch probabilities, not the stationary probability of switching at any particular time; the latter equals \(2pq/(p+q)\). At a fixed stationary one-frequency \(\theta\), however, both quantities are strictly increasing with \(s\). The stationary lag-one eigenvalue of the letter chain is \(1-s\), so the inequality \(s<1\) means persistence and \(s>1\) means antipersistence.

## Proof

**1. Deterministic subsequence state.** For a binary word \(w\), let \(e_0(w)\) and \(e_1(w)\) count distinct nonempty subsequence strings ending in the respective bit. Every subsequence ending in a newly appended bit \(b\) can be written uniquely as a prior (possibly empty) subsequence *string* followed by \(b\). Therefore

\[
(e_0(w0),e_1(w0))=(1+e_0(w)+e_1(w),e_1(w)),
\quad
(e_0(w1),e_1(w1))=(e_0(w),1+e_0(w)+e_1(w)).
\]

This counts distinct strings, not choices of positions. In particular \(D_n=e_0(X_1\cdots X_n)+e_1(X_1\cdots X_n)\).

**2. Four conditional expectations.** Write

\[
u_n=(\mathbb E[e_0\mathbf1_{\{X_n=0\}}],\mathbb E[e_1\mathbf1_{\{X_n=0\}}],\mathbb E[e_0\mathbf1_{\{X_n=1\}}],\mathbb E[e_1\mathbf1_{\{X_n=1\}}])^T,
\]

where the subsequence counts refer to the prefix of length \(n\). Conditioning on the previous symbol and using stationarity gives

\[
\boxed{u_{n+1}=Tu_n+f,\qquad u_1=f,}
\]

with

\[
T=\begin{pmatrix}
1-p&1-p&q&q\\
0&1-p&0&q\\
p&0&1-q&0\\
p&p&1-q&1-q
\end{pmatrix},\qquad
f=\begin{pmatrix}q/s\\0\\0\\p/s\end{pmatrix}.
\]

Thus \(u_n=\sum_{j=0}^{n-1}T^jf\) and \(\mathbb E[D_n]=(1,1,1,1)u_n\). The formal power-series identity

\[
\sum_{n\ge0}\mathbb E[D_n]z^n
=\frac{z}{1-z}(1,1,1,1)(I-zT)^{-1}f
\]

is exact for every \(n\) (the zero-length expectation vanishes).

**3. Exact scalar transfer and spectral factorization.** Direct four-by-four elimination gives

\[
\det(I-zT)=(1-z)^2[1-(1-s)z]^2-vz^2.
\]

Multiplying the inverse by the initial and observation vectors gives

\[
(1,1,1,1)(I-zT)^{-1}f=
\frac{L(z)[s+(s^2-2s+2v)z-s(s-1)z^2]}
{s[(1-z)^2L(z)^2-vz^2]},
\]

proving the generating function. Both rational identities are reproducible by symbolic multiplication in `verify_markov.py`.

Put \(t=\lambda-1\). The characteristic polynomial has the *exact* non-generic factorization

\[
\det(\lambda I-T)=t^2(t+s)^2-v(t+1)^2
=\big[t(t+s)-\sqrt v(t+1)\big]
\big[t(t+s)+\sqrt v(t+1)\big].
\]

For positive \(p,q\), \(T\) is an irreducible nonnegative matrix; it is primitive unless \(p=q=1\), in which case the two-step periodic decomposition is elementary. Its Perron eigenvalue is the unique solution \(\lambda>1\) of

\[
(\lambda-1)(\lambda-1+s)=\sqrt v\,\lambda.
\]

Indeed \(t>0\) is the sole positive root of \(t^2+(s-\sqrt v)t-\sqrt v=0\). Positivity of \(f\) on two states, accessibility of all states and positivity of the observation vector ensure that the expectation grows with nth-root rate this Perron eigenvalue. In the deterministic-alternating boundary \(p=q=1\), either parity has the same exponential base. Solving the quadratic proves the displayed radical expression.

**4. Sharp fixed-composition ordering.** Let \(\theta=p/s\) be fixed and set \(c=\sqrt{\theta(1-\theta)}\), so \(\sqrt v=cs\) and \(0<c\le1/2\). Write \(t(s)=\Lambda(s\theta,s(1-\theta))-1>0\). The Perron equation becomes

\[
t^2+s(1-c)t-cs=0.
\]

Implicit differentiation yields

\[
\frac{dt}{ds}=\frac{c-(1-c)t}{2t+s(1-c)}
=\frac{t^2}{s[2t+s(1-c)]}>0,
\]

using the equation once again in the second equality. Since \(p,q\le1\), the admissible interval has upper endpoint \(s_*=\min\{1/\theta,1/(1-\theta)\}\). Hence this endpoint is the unique maximizing chain. At \(s=1\), the chain is independent and \(\Lambda=1+\sqrt{\theta(1-\theta)}\); all other admissible rates are strictly ordered around it. This proves the optimality and correlation conclusions.

## Verification

Run `python verify_markov.py` from the directory containing that file. The checker independently enumerates distinct scattered-subsequence *sets* for all binary hosts through length nine, weights each host by its exact rational stationary Markov probability, and compares the expected counts against both the four-state conditional recursion and the claimed rational function.

The executed check passed 67 positive rational transition pairs, 603 length/parameter expectations and 68,474 exactly weighted host instances. It also confirmed, by exact symbolic identities, both the characteristic-polynomial factorization and the full scalar generating-function numerator. The script performs these symbolic checks when SymPy is available; the core independent enumeration uses Python's standard library alone. The examples at \(\theta=3/10\) have growth rates approximately \(1.253375\), \(1.458258\), and \(1.509920\) for switch intensities \(s=1/5\), \(1\), and \(10/7\), respectively.

## Relationship to prior work

Biers-Ariel, Godbole and Kelley (2017/2018) proved the biased-independent result and gave a four-variable recurrence for the Markov-dependent binary source. Their Section 3.2 does not solve the asymmetric recurrence into a scalar closed expression; Section 4(c) explicitly names solving these recurrences and computing exponential growth rates as a problem of interest. Their matrix recurrence already determines the expectation algorithmically, and that prior contribution is not claimed as new. The present theorem extracts the special square-root factorization and establishes strict optimality at fixed stationary symbol frequency.

The separately published symmetric-Markov calculation *Exact length spectrum of distinct subsequences in a symmetric binary Markov source* gives a two-variable generating function and the growth rate only for \(p=q\). Setting \(p=q\) in the present rate recovers its symmetric formula; it does not entail the asymmetric fixed-composition ordering. Collins's earlier exact uniform-independent calculation is another specialization, not an asymmetric Markov theorem.

## Limitations

The theorem concerns expected total numbers of distinct nonempty scattered subsequences and their exponential growth, not length-by-length subsequence profiles, variance, typical almost-sure host complexity, or optimal codes. It does not extend to nonstationary symbol laws or arbitrary finite alphabets. At the formal limit of zero switching, the stationary chain becomes a mixture of two constant words and the growth-rate limit is one; the displayed rational generating function is stated only for positive transitions. Searches and comparisons cannot rule out unindexed equivalent work. No independent mathematical audit is claimed.

## References

1. Y. Biers-Ariel, A. Godbole and E. Kelley, *Expected Number of Distinct Subsequences in Randomly Generated Binary Strings*, arXiv:1704.08661 (first public 2017-04-27), Discrete Mathematics & Theoretical Computer Science 19(2), 2018. https://arxiv.org/html/1704.08661v3
2. M. J. Collins, *The Number of Distinct Subsequences of a Random Binary String*, arXiv:1310.7288 (2013). https://arxiv.org/html/1310.7288v1
3. *Exact length spectrum of distinct subsequences in a symmetric binary Markov source*, publicly indexed mathematical note, November 2026, identifier `c9e7de297805`.
