# Logarithmic zero-deletion trace coverage and a heavy-tailed Dirichlet limit

## Finding
Fix an integer \(k\ge1\). Choose a binary length-\(n\) source with exactly \(k\) ones uniformly, where \(n\ge k+1\), and independently repeat the following read: select one of the \(N=n-k\) zero positions uniformly and delete it. Let \(T_{n,k}\) be the number of reads required to observe **every distinct output attainable by one such zero deletion**. Set \(m=k+1\) and \(H_j=\sum_{r=1}^j1/r\), with \(H_0=0\). Then

\[
\begin{aligned}
\mathbb E T_{n,k}={}&m(m-1)\log N+m(m-1)(\gamma-H_{m-2})\\
&+(m-1)(m-1-mH_{m-1})+o_k(1),\qquad N\to\infty.
\end{aligned}
\]

The unconditional distribution, by contrast, converges to an integer-valued random variable \(T_m\) with
\[
\Pr(T_m>t)=1-\frac{\binom{t-1}{m-1}}{\binom{t+m-1}{m-1}},\qquad t\ge1,
\]
where a binomial coefficient vanishes if its upper argument is smaller than its lower argument, and \(\Pr(T_m>0)=1\). Moreover
\[
\Pr(T_m>t)=\frac{m(m-1)}{t}+O_m(t^{-2}),\quad \mathbb E T_m=\infty.
\]
Thus a sequence of *finite* expected read counts diverges logarithmically while the read counts converge in distribution to a proper infinite-mean law.

A finite exact formula is also available. For \(1\le s<m\), write
\[
A_{m,s}(N)=\frac{1}{\binom{N+m-1}{m-1}}\sum_{u=s}^{N}
\frac{\binom{u-1}{s-1}\binom{N-u+m-s-1}{m-s-1}}{u};
\]
for \(s=m\), set
\[
A_{m,m}(N)=\frac{\boldsymbol 1_{N\ge m}}{N}
\frac{\binom{N-1}{m-1}}{\binom{N+m-1}{m-1}}.
\]
Then, exactly for all admissible \(n,k\),
\[
\mathbb E T_{n,k}=N\sum_{s=1}^{m}(-1)^{s+1}\binom ms A_{m,s}(N).
\]
As a simple case, \(k=1\) gives exactly \(\mathbb E T_{n,1}=[2NH_N-(N-1)]/(N+1)\).

## Assumptions and scope
Reads are independent conditional on the initial source. Only zero positions are deleted, so all output words retain exactly \(k\) ones; this is equivalent to conditioning a uniformly selected one-deletion read on deleting a zero. The source is drawn once, prior to the repeated reads, and is uniformly distributed over fixed-weight binary words. The number \(k\) is fixed for the asymptotic assertions. Outputs are ordinary linear words, not rotation classes. No claim is made for simultaneously growing \(k\), noisy outputs, or deletions of both symbols.

## Proof
Every such word is uniquely specified by its \(m=k+1\) zero gaps \(G=(G_1,\ldots,G_m)\), separated by its \(k\) ones, with each \(G_i\ge0\) and \(\sum_iG_i=N\). Uniform fixed-weight sampling makes \(G\) uniform on the \(\binom{N+m-1}{m-1}\) weak compositions. Removing a zero in positive gap \(i\) decreases exactly that gap by one. For distinct positive gaps \(i\), these are distinct outputs, each with conditional probability \(p_i=G_i/N\). Hence \(T_{n,k}\) is the cover time of the nonzero coordinates of \(G\).

For a fixed composition \(G\), inclusion-exclusion over the nonempty subsets of its positive coordinates yields
\[
\mathbb E(T_{n,k}\mid G)
=\sum_{\varnothing\ne S\subseteq\{i:G_i>0\}}(-1)^{|S|+1}
\frac{N}{\sum_{i\in S}G_i}.
\]
Indeed the geometric-series sum of the probability that at least one output has not been observed after \(t\) reads is the right-hand side. By symmetry, for a given subset of \(s\) coordinates, the number of gap vectors for which all selected gaps are positive and their sum is \(u\) is
\(\binom{u-1}{s-1}\binom{N-u+m-s-1}{m-s-1}\) when \(s<m\), and is \(\binom{N-1}{m-1}\) at \(u=N\) when \(s=m\). Averaging therefore gives the exact finite formula above, including the cases where some gaps are zero.

For each fixed \(m\), the vector \(G/N\) converges weakly to the uniform simplex law \(\operatorname{Dirichlet}(1,\ldots,1)\). For fixed \(t\), the probability of full coupon coverage in \(t\) draws is a polynomial in the category probabilities, and a zero gap has probability \(O_m(1/N)\). Consequently, \(T_{n,k}\) converges in distribution to the coverage time under that Dirichlet mixture. Under the mixture, every weak composition of the \(t\) draw counts into \(m\) categories has equal probability: integration of the multinomial likelihood gives \(t!(m-1)!/(t+m-1)!\). There are \(\binom{t+m-1}{m-1}\) count vectors, of which \(\binom{t-1}{m-1}\) have every count positive. This gives the displayed tail formula. Expanding the product ratio as \(t\to\infty\) gives \(m(m-1)/t+O_m(t^{-2})\), and the tail-sum identity proves infinite expectation.

It remains to derive the finite-size mean constant, since distributional convergence alone cannot do so. The one-coordinate marginal is \(\Pr(G_1=u)=\binom{N-u+m-2}{m-2}/\binom{N+m-1}{m-1}\), and therefore
\[
N A_{m,1}(N)=(m-1)\left(\log N+\gamma-H_{m-2}\right)+o_m(1).
\]
One proof splits the sum at \(u=\varepsilon N\), uses the polynomial ratio approximation there, and then lets \(\varepsilon\downarrow0\); equivalently, the finite polynomial \(\binom{N-u+m-2}{m-2}\) admits a harmonic-sum expansion, whose constant is \(-H_{m-2}\). For \(2\le s<m\), the normalized sum of the \(s\) positive coordinates converges to a \(\operatorname{Beta}(s,m-s)\) variable. Uniform integrability of its reciprocal for \(s>1\), obtained from the near-zero bound \(\Pr(\sum_{i=1}^{s}G_i\le\varepsilon N,\,G_i>0)=O_m(\varepsilon^s)\), gives \(N A_{m,s}(N)\to(m-1)/(s-1)\). The same limit for \(s=m\) is \(1\). Finally
\[
\sum_{s=2}^{m}(-1)^{s+1}\frac{\binom ms}{s-1}
=m-1-mH_{m-1},
\]
by integrating the binomial identity or expanding \((1-x)^m\). Combining the limits gives the asserted two-term asymptotic expansion. For \(m=2\), summing the exact formula directly produces the given closed form.

## Verification
The companion standalone program `verify.py` independently enumerates the literal one-zero-deletion outputs of 702 distinct source words and computes their exact rational coupon cover-time expectations by a second method. It compares those values against the finite gap-composition formula, tests the one-marker closed form, verifies 75 exact Dirichlet-tail identities by independent factorial-moment inclusion-exclusion, and checks the trend of the asymptotic correction. Run `python verify.py` using only Python's standard library; the expected final line begins `VERIFY_OK`. These finite experiments check normalization and boundary cases but are not substituted for the all-length proof.

## Relationship to prior work
The standard unequal-probability coupon collector and its inclusion-exclusion expectation are established tools. Du Boisberranger, Gardy and Ponty study the broader weighted-words coupon collector, including integral formulas and growing-alphabet asymptotics, but not this fixed-marker one-zero-deletion source mixture or its explicit logarithmic correction. Liron and Langberg determine numbers of subsequences generated by deletions, not repeated-read collection times. Singhvi and collaborators examine deletion-channel input and output entropy, rather than time to observe the full conditional output support. The present claim is the joint fixed-source-mixing law: a universal heavy-tailed distributional limit together with a sharp finite-size mean and exact finite formula. A logically equivalent formulation within older general Dirichlet/Pólya-urn coupon literature remains possible; the elementary Dirichlet-multinomial mixture identity itself is not independently claimed new.

## Limitations
Only zero deletions are sampled. The heavy-tail limiting mean cannot be interchanged with the finite-size expectation. The fixed-\(k\) assumption is essential in the asymptotic argument. The explicit finite formula is a finite sum rather than a simplified rational expression for arbitrary \(k\). Earlier literature on Dirichlet-mixed coupon collectors could imply some or all of the distributional component; the claim's priority depends particularly on the deletion-source identification and the constant-order mean expansion.

## References
1. J. Du Boisberranger, D. Gardy, Y. Ponty, *The weighted words collector*, arXiv:1202.0920 (first publicly posted 2012-02-04), https://arxiv.org/abs/1202.0920.
2. Y. Liron, M. Langberg, *A characterization of the number of subsequences obtained via the deletion channel*, arXiv:1202.1644 (2012), https://arxiv.org/abs/1202.1644.
3. A. Singhvi et al., *The Input and Output Entropies of the k-Deletion/Insertion Channel*, arXiv:2202.03024 (2022), https://arxiv.org/abs/2202.03024.
