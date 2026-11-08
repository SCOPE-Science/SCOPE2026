# Sharp two-term power-regularity laws for finite-support convex unilateral shifts

## Finding
Let \(S\) be the unilateral shift on \(H^2(\mathbb D)\). Let \((p_j)_{j=0}^d\) be a finite probability distribution on nonnegative integers with \(p_0>0\) and at least one positive \(p_j\) for \(j\ge1\). Put \(P(z)=\sum_{j=0}^d p_jz^j\) and \(T=P(S)\). Write \(\mu=\mathbb E X>0\), \(v=\operatorname{Var}(X)>0\), and \(m_r=\mathbb E X^r\) for the corresponding integer-valued random variable. Write \(\kappa_4=\mathbb E(X-\mu)^4-3v^2\). Define
\[
B=\frac{\kappa_4}{24v^2}+\frac{m_2^2}{8\mu^2v}-\frac{m_3}{6\mu v}.
\]
For every **fixed integer** \(k\ge1\), as \(n\to\infty\),
\[
\boxed{\left\|T^n(I-T)^k\right\|=\mu^k\left(\frac{k}{evn}\right)^{k/2}\left(1+\frac{k^2B}{n}+O_{P,k}(n^{-2})\right).}
\]
The correction \(B\) can have either sign. For every nondegenerate two-point law supported on \(\{0,h\}\), \(B=-1/4\), independently of the mass and of the positive integer \(h\). For the symmetric three-point law \((p_0,p_1,p_2)=(1/4,1/2,1/4)\), \(B=-5/16\); for \((p_0,p_1,p_2,p_3,p_4)=(1/30,14/15,0,0,1/30)\), \(B=145661/1401856>0\).

## Assumptions and scope
The space is complex \(H^2(\mathbb D)\) with the standard orthonormal monomial basis. The polynomial \(P\) has finitely many real nonnegative coefficients summing to one. The hypothesis \(p_0>0\) ensures that every peripheral point of \(P(\mathbb T)\) equals one. The integer \(k\) is fixed before \(n\to\infty\), not allowed to grow with \(n\). This result is an operator norm statement (not a Schatten estimate) and concerns the forward unilateral shift. The coefficient \(B\) depends on the distribution through moments of orders at most four.

## Proof
**1. Exact scalar reduction.** The unilateral shift is multiplication by \(z\) on \(H^2\). The multiplier-norm identity gives
\[
\|T^n(I-T)^k\|=\max_{|z|=1}|P(z)|^n|1-P(z)|^k.
\]
Let \(d_0=\gcd\{j\ge1:p_j>0\}\). Equality in the triangle inequality, using \(p_0>0\), shows that \(|P(e^{i\theta})|=1\) precisely at the \(d_0\)-th roots of unity. At all these points \(P=1\). Near any such point the objective is identical to the one near \(\theta=0\), because every supported exponent is divisible by \(d_0\). Away from small disjoint neighborhoods of these roots, \(|P|\le q<1\), so the objective is exponentially small.

**2. Local expansions.** Because \(P(e^{i\theta})=\mathbb E e^{i\theta X}\), the cumulant expansion (valid analytically near zero) gives
\[
\log|P(e^{i\theta})|=-\frac{v\theta^2}{2}+\frac{\kappa_4\theta^4}{24}+O(\theta^6).
\]
The direct Taylor expansion \(P(e^{i\theta})=1+i\mu\theta-m_2\theta^2/2-im_3\theta^3/6+O(\theta^4)\) gives
\[
|1-P(e^{i\theta})|^2=\mu^2\theta^2+\left(\frac{m_2^2}{4}-\frac{\mu m_3}{3}\right)\theta^4+O(\theta^6).
\]
For \(\theta\ne0\) small, this implies
\[
\log|1-P(e^{i\theta})|=\log(\mu|\theta|)+\frac12\left(\frac{m_2^2}{4\mu^2}-\frac{m_3}{3\mu}\right)\theta^2+O(\theta^4).
\]
Evenness of both moduli justifies the stated even-order remainders.

**3. Location of global maximizers.** The strict off-root inequality from step 1 and \(\log|P(e^{i\theta})|\le-c\theta^2\), \(|1-P(e^{i\theta})|\le C|\theta|\) near each root imply that all maximizers satisfy \(\theta=O(n^{-1/2})\) relative to some root. In fact, after the rescaling \(x=\sqrt n|\theta|\), contributions for \(x\to0\) and \(x\to\infty\) vanish relative to the leading maximum, by the upper bound \(C x^k e^{-cx^2}\). Thus relevant maximizers lie in a fixed compact interval separated from zero. In that interval, the logarithm of the rescaled objective is
\[
\log\!\bigl(n^{k/2}|P(e^{ix/\sqrt n})|^n|1-P(e^{ix/\sqrt n})|^k\bigr)
=k\log\mu+k\log x-\frac{vx^2}{2}
+\frac1n\left[\frac{\kappa_4x^4}{24}+\frac{kx^2}{2}\left(\frac{m_2^2}{4\mu^2}-\frac{m_3}{3\mu}\right)\right]+O(n^{-2}).
\]
The expansion and its first two derivatives are uniform on the compact interval. The leading log-profile has its unique positive maximum at \(x_0=\sqrt{k/v}\), with strictly negative second derivative. The implicit function theorem and the strict leading gap show that the rescaled maximizer equals \(x_0+O(n^{-1})\). Its shift changes the maximized log-value only by \(O(n^{-2})\).

**4. Coefficient and boundaries.** Inserting \(x_0\) in the order-\(n^{-1}\) term gives precisely \(k^2B\). Exponentiation gives the displayed two-term formula with \(O_{P,k}(n^{-2})\). The two-point identity follows alternatively by optimizing \((1-4q(1-q)y)^{n/2}(2qy^{1/2})^k\) over \(0\le y\le1\), where \(q\) is the mass at \(h\). For all sufficiently large \(n\), the maximizer is \(y=k/[4q(1-q)(n+k)]\) and hence
\[
\|T^n(I-T)^k\|=\left(\frac{q}{1-q}\right)^{k/2}\left(\frac{k}{n+k}\right)^{k/2}\left(\frac{n}{n+k}\right)^{n/2},
\]
which confirms \(B=-1/4\) independently of \(q\) and \(h\). The other two rational coefficients follow by exact substitution into the formula for \(B\).

## Verification
Run `python3 checks/check_power_norms.py` with Python 3. The standalone checker uses exact rational arithmetic for the three displayed correction coefficients, compares the independently derived two-point exact optimization formula against numerical maximization, and performs finite-scale checks of the rescaled corrections for the two three-point laws. These checks are finite corroborations, not substitutes for steps 1–4.

## Relationship to prior work
Katznelson and Tzafriri (1986) characterize qualitative decay of \(\|T^n(I-T)\|\) for contractions in terms of peripheral spectrum. Dungey (2008) characterizes the order \(O(n^{-1/2})\) for general power-bounded operators. Arnold (2026) develops resolvent-based decay estimates for \(\|T^n(I-T)^k\|\). His Section 6.1 already finds the exact scalar optimizer for \(P(z)=(1+z)/2\), the equal-weight two-point case; that special formula is prior work and not claimed independently as new. The present exact first and second coefficients apply to the concrete class of positive finite-polynomial unilateral-shift multipliers and distinguish coefficient laws with opposite finite-time correction signs. These general estimates are not claimed as new.

## Limitations
The distribution is fixed, finite, nonnegative, and supported on integers including zero; \(k\) is fixed. No uniformity over distributions approaching zero variance or over growing \(k\) is established. No statement about the corresponding norms on other Banach spaces, or about Ritt membership, is inferred. The originality comparison is qualified because the full texts of some relevant general operator-semigroup papers were inaccessible; the result has not undergone independent audit.

## References
1. L. Arnold, *Rates of Decay for \((\alpha,\beta)\)-Ritt-Kreiss Operators*, first submitted 2026-06-12, arXiv:2606.14323, https://arxiv.org/abs/2606.14323.
2. N. Dungey, *On time regularity and related conditions for power-bounded operators*, Proc. London Math. Soc. 97 (2008), 97–116, doi:10.1112/plms/pdm058.
3. Y. Katznelson and L. Tzafriri, *On power bounded operators*, J. Funct. Anal. 68 (1986), 313–328, doi:10.1016/0022-1236(86)90101-1.
