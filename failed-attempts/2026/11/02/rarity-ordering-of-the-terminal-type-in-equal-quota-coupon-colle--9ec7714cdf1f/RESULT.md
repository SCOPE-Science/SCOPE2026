# Rarity ordering of the terminal type in equal-quota coupon collection

## Finding

Let \(m\ge2\) and \(q\ge1\) be integers. On each independent draw, one of \(m\) required coupon types \(i\in\{1,\dots,m\}\) appears with probability \(p_i>0\), and an optional null type appears with probability \(p_0\ge0\), where \(p_0+\sum_i p_i=1\). Stop at the first draw \(T\) when **each required type has appeared at least \(q\) times**. Let \(J\) be the required type drawn on that final draw. Every integer \(t\ge mq\) is attainable.

**Theorem (strict terminal-type likelihood-ratio ordering).** For every pair \(i,j\) with \(p_i>p_j\), and every integer \(t\ge mq\),
\[
\Pr(J=i\mid T=t)\Pr(J=j\mid T=t+1)
>
\Pr(J=i\mid T=t+1)\Pr(J=j\mid T=t).
\]
The two sides are equal when \(p_i=p_j\). Thus longer times to meet all quotas favor the rarer *terminal* type in strict monotone likelihood-ratio order, at every finite time, with no asymptotic or near-uniform assumption.

At the shortest completion time the terminal type is exactly uniform:
\[
\Pr(J=i\mid T=mq)=\frac1m.
\]
One draw later it already distinguishes the rates:
\[
\Pr(J=i\mid T=mq+1)
=\frac{1+q p_0-p_i}{\sum_{j=1}^m(1+q p_0-p_j)}.
\]
In particular, \(J\) and \(T\) are independent **if and only if** all the required probabilities \(p_1,\ldots,p_m\) are equal. If the rates are nonuniform, then for strictly increasing \(f\) and \(g\) for which the covariance exists,
\[
\operatorname{Cov}(f(T),g(p_J))<0.
\]
For fixed \(m,q,p\), the conditional law of \(J\) given \(T=t\) also converges, as \(t\to\infty\), to the uniform law over the coupon types attaining \(\min_i p_i\).

For example, for \(m=3\), \(q=2\), \(p_0=1/10\) and \((p_1,p_2,p_3)=(1/10,3/10,5/10)\), the terminal label is uniform at \(T=6\), but has posterior probabilities \((11/27,9/27,7/27)\) at \(T=7\).

## Assumptions and scope

The draws are independent and identically distributed, with the same fixed probability vector throughout. The null outcome does not advance any quota. The quotas are a **common positive integer** \(q\); unequal quotas are not included. The stopping time is almost surely finite, because all required probabilities are strictly positive. No count of a required type is allowed to exceed its quota on the completion step except for types previously completed; the last type has exactly \(q-1\) occurrences before that step.

For a formal power series \(F\), write \([z^k]F(z)\) for its coefficient of order \(k\). Define
\[
E_q(z)=\sum_{r=q}^{\infty}\frac{z^r}{r!}
=e^z-\sum_{r=0}^{q-1}\frac{z^r}{r!}.
\]

## Proof

**1. Exact labeled completion law.** The final draw must be type \(i\). The preceding \(t-1\) draws contain exactly \(q-1\) copies of \(i\), at least \(q\) copies of every other required type, and any number of null draws. Independent multinomial enumeration therefore gives, for every \(t\ge mq\),
\[
F_i(t):=\Pr(T=t,J=i)
=\frac{(t-1)!p_i^q}{(q-1)!}
[z^{t-q}]\, e^{p_0z}\prod_{k\ne i}E_q(p_kz).
\tag{1}
\]
All terms are strictly positive for every \(t\ge mq\): start with the minimum required counts and add extra draws of any required type.

**2. Elementary total positivity lemma.** A nonnegative sequence \((a_s)_{s\ge0}\) with contiguous support is log-concave if \(a_s^2\ge a_{s-1}a_{s+1}\), with \(a_s=0\) outside its support. The Toeplitz array \(K(n,r)=a_{n-r}\), for nonnegative integer indices, has all its ordered \(2\times2\) minors nonnegative: indeed, when the four indices lie in support, successive ratios \(a_{s+1}/a_s\) decrease, and support-boundary cases have the same sign. Conversely those adjacent minors imply log-concavity. If \(a,b\) are such sequences, their convolution \(a*b\) is also log-concave: the Toeplitz array for \(a*b\) is the product of the Toeplitz arrays for \(a\) and \(b\), and the \(2\times2\) Cauchy–Binet identity expresses each minor of that product as a sum of products of nonnegative minors. For any fixed coefficient or minor all sums are finite. The support of the convolution is again an interval.

For every \(p>0\), the coefficient sequence of \(E_q(pz)\) is \(a_s=p^s/s!\) for \(s\ge q\), zero otherwise. It is log-concave, strictly inside its support. The coefficients of \(e^{p_0z}\) are log-concave when \(p_0>0\); when \(p_0=0\) they are the unit sequence concentrated at zero. Consequently, for any two distinct required indices \(i,j\), the coefficients \(a_s\) of
\[
A(z)=e^{p_0z}\prod_{k\notin\{i,j\}}E_q(p_kz)
\]
are nonnegative, log-concave, and supported from \(h=q(m-2)\) onward (or only at \(h=0\) when \(m=2,p_0=0\)). In every case \(a_h>0\) and \(a_{h-1}=0\).

**3. Strict ordered minors.** Set \(b_r=p_i^r/r!\) and \(c_r=p_j^r/r!\) for \(r\ge q\), zero below \(q\). When \(p_i>p_j\), for all \(q\le r<s\),
\[
c_rb_s-c_sb_r
=\frac{p_j^rp_i^s-p_j^sp_i^r}{r!s!}>0.
\]
Let \(u_n=(a*c)_n\) and \(v_n=(a*b)_n\), and form \(K(n,r)=a_{n-r}\). By the Toeplitz lemma, all minors of \(K\) involving increasing row and column indices are nonnegative. The \(2\times2\) Cauchy–Binet expansion therefore yields
\[
u_nv_{n+1}-u_{n+1}v_n
=\sum_{r<s}
\bigl(a_{n-r}a_{n+1-s}-a_{n-s}a_{n+1-r}\bigr)
\bigl(c_rb_s-c_sb_r\bigr)\ge0.
\tag{2}
\]
This inequality is **strict** for all \(n\ge q(m-1)\). In the summand choose \(r=n-h\) and \(s=n-h+1\); both are at least \(q\). The first parenthesis is \(a_h^2-a_{h-1}a_{h+1}=a_h^2>0\), and the second is positive. In (1), for \(n=t-q\), we have \(F_i(t)=C_t p_i^q u_n\) and \(F_j(t)=C_t p_j^q v_n\), where \(C_t=(t-1)!/(q-1)!>0\). Equation (2) becomes
\[
F_i(t)F_j(t+1)>F_i(t+1)F_j(t),
\]
which is exactly the theorem after normalizing each time slice by \(\Pr(T=t)\). Equal probabilities give equality by symmetry.

**4. Endpoints and independence.** At \(T=mq\), the \(mq-1\) earlier draws must have counts \(q-1\) for the final type and \(q\) for every other type. Hence
\[
F_i(mq)=\frac{(mq-1)!}{(q-1)!(q!)^{m-1}}\prod_{k=1}^m p_k^q,
\]
independent of \(i\). At \(T=mq+1\), the earlier \(mq\) draws have exactly one additional null draw or one additional copy of some other required type. Therefore
\[
\frac{F_i(mq+1)}{F_i(mq)}
=mq\left(p_0+\frac{\sum_{j\ne i}p_j}{q+1}\right)
=\frac{mq}{q+1}(1+q p_0-p_i).
\]
Normalization yields the displayed posterior. Uniform required rates imply independence by exchangeability. Conversely, independence forces the conditional probabilities at \(mq\) and \(mq+1\) to agree, making all \(p_i\) equal.

**5. Consequences and large time.** Order types by their probabilities. The pairwise strict determinant implies each posterior at time \(t+1\) is strictly smaller in likelihood-ratio order, except within tied-probability groups. Explicit cross multiplication shows \(\mathbb E[g(p_J)\mid T=t]\) is strictly decreasing in \(t\) for every strictly increasing \(g\), provided not all \(p_i\) are equal. The standard two-independent-copy covariance identity then makes \(\operatorname{Cov}(f(T),g(p_J))\) strictly negative whenever the stated moments exist. Finally, condition on the exactly \(q-1\) occurrences of type \(i\) in the first \(t-1\) draws. Among the remaining \(t-q\) independent draws, every other required type has positive conditional probability \(p_k/(1-p_i)\), so its quota is met with probability tending to one. Hence
\[
F_i(t)\sim \binom{t-1}{q-1}p_i^q(1-p_i)^{t-q}
\qquad (t\to\infty).
\]
The smallest \(p_i\) have the largest exponential factor, and tied minima are exchangeable. This proves the terminal-label limit.

## Verification

The standalone Python 3 program `verify.py` uses exact rational arithmetic throughout. For several unequal and equal probability profiles, with and without null outcomes, and quotas \(q=1,2,3,4\), it independently propagates all truncated coupon-count states by dynamic programming and compares their terminal-label probabilities with formula (1). It checks every successive likelihood-ratio minor over a finite range, the two first-time formulas, and conditional probability bounds. The program reports **PASS 5416 exact rational assertions**. These finite checks supplement, but do not replace, the all-parameter proof above.

## Relationship to prior work

May (2008, Sections 2–3) gives a general terminal-completion generating-function framework for nonuniform quotas, including the exact coefficient-counting background. Shank and Yang (2013) address nonuniform sampling and random quotas, particularly expectations. Anceaume, Busnel, and Sericola (2014, Sections 2 and 5) give stopping-time distributions and uniformity extremality with a null coupon. Mahmoud and Smythe (2012 volume, online 2016) analyze multivariate counts of coupons occurring specified numbers of times. These are **not** claimed as new counting formulas. The statement assessed here is the *strict conditional likelihood-ratio relation between the terminal label and the exact stopping time*, jointly for all quotas, probabilities, and null rates; the cited results do not state this relation in the material inspected. A known general theorem about log-concave convolutions supplies a useful proof ingredient, rather than the coupon-specific conclusion by itself.

## Limitations

The result assumes one coupon per independent draw, fixed positive required probabilities, and equal integer quotas. It makes no claim for heterogeneous quotas, dynamic probabilities, dependent draws, or nearly completed subcollections. The proof and independent dynamic-programming check establish mathematical correctness only within the stated model. The literature comparison is not an exhaustive historical-priority certification; in particular, a sufficiently general preexisting total-positivity treatment of quota completion could subsume the ordering, and inaccessible older literature remains a risk. No external independent audit has been performed.

## References

- R. May, *Coupon Collecting with Quotas*, Electronic Journal of Combinatorics 15 (2008), #N31, published August 18, 2008. https://doi.org/10.37236/906 ; https://www.combinatorics.org/Volume_15/PDF/v15i1n31.pdf
- N. B. Shank and H. Yang, *Coupon Collector Problem for Non-Uniform Coupons and Random Quotas*, Electronic Journal of Combinatorics 20 (2013), #P33, published May 16, 2013. https://doi.org/10.37236/3348
- E. Anceaume, Y. Busnel, and B. Sericola, *New results on a generalized coupon collector problem using Markov chains*, preprint first publicly posted February 21, 2014. https://arxiv.org/abs/1402.5245
- H. M. Mahmoud and R. T. Smythe, *On the Joint Behavior of Types of Coupons in Generalized Coupon Collection*, Advances in Applied Probability 44 (2012), 429–451, publisher online date January 4, 2016. https://doi.org/10.1239/aap/1339878719
