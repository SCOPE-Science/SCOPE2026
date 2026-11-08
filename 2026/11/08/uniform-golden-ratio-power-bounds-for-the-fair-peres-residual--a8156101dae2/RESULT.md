# Uniform golden-ratio power bounds for the fair Peres residual

## Finding

Let \(X\) be uniformly distributed on the \(N\)-bit strings and let \(R(X)\) be the residual left by the exhaustive binary Peres transformation, as specified below. Set
\[
\varphi=\frac{1+\sqrt5}{2},\qquad \alpha=\log_2\varphi.
\]
For every integer \(N\ge1\), the expected residual length \(a_N=\mathbb E|R(X)|\) satisfies the explicit, uniform inequalities
\[
\boxed{\frac{N^\alpha+1}{2}\le a_N\le2N^\alpha-1.}
\]
Consequently, \(a_N=\Theta(N^\alpha)\); equivalently, the expected number of fair bits produced from \(N\) independent unbiased bits is \(N-\Theta(N^\alpha)\). The constants apply at every positive integer input length, with no asymptotic qualifier. This statement concerns *mean residual length*, not the worst-case number of residual ones or a limit of \(a_N/N^\alpha\).

## Assumptions and scope

The input is an independent uniform binary word, with alphabet \(\{0,1\}\). On a word of length \(m\), set \(n=\lfloor m/2\rfloor\), pair the first \(2n\) symbols, and form: \(u\), the \(n\) pairwise XORs; \(v\), the second components of equal pairs; \(y\), the second components of unequal pairs; and \(r\), the one unpaired terminal symbol if \(m\) is odd, or the empty word otherwise. The exhaustive Peres output uses the fair bits from the recursive calls on \(u\) and \(v\), together with \(y\); its residual is the concatenation of the respective recursive residuals followed by \(r\). Words of length zero or one terminate, with their entire contents residual. The recursion strictly decreases length for \(m\ge2\).

Conditional on the number \(B\) of equal pairs, the word \(v\) consists of \(B\) independent unbiased bits, while \(u\) has length \(n\) and is uniform; \(B\sim\operatorname{Bin}(n,1/2)\). Therefore, writing \(a_0=0\), \(a_1=1\), we have the exact identity
\[
 a_{2n+\rho}=a_n+\mathbb E\,a_B+\rho,
 \quad n\ge1,\ \rho\in\{0,1\},\quad B\sim\operatorname{Bin}(n,1/2).
\]
In particular, \(a_{2n+1}=a_{2n}+1\). This identity is also the known recurrence for the extraction cost of Peres's algorithm on a fair input.

## Proof

First, \(0<\alpha<1\), \(\alpha>1/2\), and \(2^\alpha=\varphi\). From \(\varphi^2=\varphi+1\),
\[
(2n)^\alpha=n^\alpha+(n/2)^\alpha. \tag{1}
\]

**Binomial concavity-deficit lemma.** If \(B\sim\operatorname{Bin}(n,1/2)\), \(n\ge1\), then
\[
0\le (n/2)^\alpha-\mathbb E B^\alpha\le1-2^{-n}.\tag{2}
\]
The left inequality is Jensen's inequality. To prove the other, note that for every real \(z\ge0\) and \(0<\alpha<1\),
\[
z^\alpha\ge1+\alpha(z-1)-(z-1)^2.\tag{3}
\]
For \(z\in[0,1]\), put \(t=1-z\). In the binomial series for \((1-t)^\alpha\), every coefficient after the linear term is nonpositive and their absolute values sum to \(1-\alpha\); since \(t^j\le t^2\) for \(j\ge2\), (3) follows. For \(z\in[1,2]\), Taylor's theorem and \(\alpha(1-\alpha)z^{\alpha-2}\le1\) yield a quadratic error at most \((z-1)^2/2\). For \(z\ge2\), the right-hand side of (3) is at most \(1\), hence at most \(z^\alpha\). Thus (3) holds for the full nonnegative range, including zero.

Apply (3) to \(z=B/(n/2)\) and take expectations. The linear term vanishes and \(\operatorname{Var}(B)=n/4\), so
\[
 (n/2)^\alpha-\mathbb E B^\alpha
 \le(n/2)^{\alpha-2}\frac n4
 =\frac12(n/2)^{\alpha-1}.\tag{4}
\]
If \(n\ge2\), this is at most \(1/2<1-2^{-n}\). If \(n=1\), the deficit is \(2^{-\alpha}-1/2<1/2=1-2^{-1}\). This proves (2).

**Lower bound.** Define \(L_0=0\) and \(L_m=(m^\alpha+1)/2\) for \(m\ge1\). At \(m=1\), \(a_1=L_1=1\). Suppose inductively that \(a_j\ge L_j\) for every \(j<m\). For \(m=2n\), with \(n\ge1\) and \(P=\Pr(B>0)=1-2^{-n}\), the recurrence and (2) give
\[
\begin{aligned}
a_{2n}&\ge\frac{n^\alpha+1}{2}+\frac{\mathbb E B^\alpha+P}{2}\\
&\ge\frac{n^\alpha+(n/2)^\alpha+1}{2}=L_{2n},
\end{aligned}
\]
using (1). For \(m=2n+1\), \(a_{2n+1}=a_{2n}+1\ge L_{2n}+1\ge L_{2n+1}\), because \((2n+1)^\alpha-(2n)^\alpha\le1\) by concavity. The lower bound follows by strong induction.

**Upper bound.** Define \(U_0=0\) and \(U_m=2m^\alpha-1\) for \(m\ge1\); again \(a_1=U_1=1\). Under the analogous induction, Jensen and (1) imply
\[
\begin{aligned}
a_{2n}&\le (2n^\alpha-1)+2\mathbb E B^\alpha-P\\
&\le2(2n)^\alpha-1-P=U_{2n}-P.
\end{aligned}
\]
Hence \(a_{2n+1}\le2(2n)^\alpha-P\). To compare this with \(U_{2n+1}\), observe that \(\alpha>1/2\) and for \(t\ge1\), \(\alpha t^{\alpha-1}\ge\tfrac12t^{-1/2}\). Therefore
\[
\begin{aligned}
2\bigl((2n+1)^\alpha-(2n)^\alpha\bigr)
&\ge2\bigl(\sqrt{2n+1}-\sqrt{2n}\bigr)\\
&>\frac1{\sqrt{2n+1}}\ge2^{-n}=1-P.
\end{aligned}
\]
The final inequality follows from \(4^n\ge2n+1\) for all \(n\ge1\). Thus \(a_{2n+1}\le U_{2n+1}\), closing the induction.

Both bounds hold for all \(N\ge1\), giving \(a_N=\Theta(N^\alpha)\).

## Verification

The accompanying standalone `checker.py` independently implements the exhaustive transformation and the exact rational binomial recurrence. It confirms agreement between exhaustive enumeration of every binary input for lengths zero through twelve and the recurrence, and checks the proposed inequalities for lengths one through 150. No numerical test is used to infer the infinite assertion; that assertion follows from (1)–(4) and induction.

Run with `python3 checker.py` using only the Python standard library. For example, the first residual means are \(a_1=1\), \(a_2=3/2\), \(a_3=5/2\), \(a_4=19/8\). The assertions in the checker distinguish exact recurrence/enumeration checks from floating-point tests of the explicit inequalities.

## Relationship to prior work

Lim, Liao and Yao (2020) studied the fair-coin cost \(g(N)=N-\mathbb E|A_P(N)|\) of Peres extraction, obtained the same recurrence and established \(\lim_{N\to\infty}\log g(N)/\log N=\log_2\varphi\). Their stated conclusion notes that even convergence of \(g(N)/N^\alpha\) is unknown. That logarithmic limit alone permits unbounded subpower multipliers and does not imply \(g(N)=\Theta(N^\alpha)\). The present inequalities strengthen the earlier exponent law to a uniform constant-factor order with explicit universal bounds.

Garivier (2026) defines an exhaustive Peres residual and records the identical recurrence for its **mean length** in the open-problems discussion; the golden-ratio exponent is presented as a heuristic for the mean. The paper's worst-case sublinear bound concerns the *number of residual ones* and is a different quantity. The present result determines the correct uniform power order for the fair-input **expected residual length**; it does not resolve the maximal residual-weight problem.

## Limitations

The theorem assumes independent unbiased binary input. It gives neither a limit for \(a_N/N^\alpha\), nor regular variation, nor bounds of this order for all biased Bernoulli sources. It does not improve the worst-case exponent for the number of residual ones, the full residual's description length, or arbitrary-input pointwise coding guarantees. The bounds are explicit but not asserted to have optimal constants. The originality assessment is literature-relative; independent expert validation and exhaustive priority confirmation have not been performed.

## References

- Z. G. Lim, C. Liao and Y. Yao, *Asymptotic Analysis of Peres' Algorithm for Random Number Generation*, *Probability in the Engineering and Informational Sciences* (2020), DOI: https://doi.org/10.1017/S0269964820000510 ; lawful manuscript https://staff.stat.sinica.edu.tw/yao/file/manuscript_rO8dvd2dHxCS4O0TbsiCioz2.pdf (Proposition 2 and Section 4).
- Aurélien Garivier, *The Exhaustive Peres Transform: Extraction and Universal Coding*, first public arXiv version dated 2026-10-19, arXiv:2610.26396, https://arxiv.org/abs/2610.26396 ; open full text https://xsci.com/preprint/doi/10.66977/xsci.2610.002f.pdf (Section 8, open problems).
- Yuval Peres, *Iterating von Neumann's procedure for extracting random bits*, *Annals of Statistics* 20 (1992), 590–597. https://doi.org/10.1214/aos/1176348543
