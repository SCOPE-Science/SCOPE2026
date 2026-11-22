# Sharp dyadic tail-efficiency phases of the Sierpiński copula

## Finding

Let \(\mathcal P\) be the set of joint laws of \((U_1,U_2,U_3)\) with all three coordinates uniform on \([0,1]\) and every pair independent. Put
\[
M(t)=\sup_{\pi\in\mathcal P}\Pr_\pi(U_1\ge t,U_2\ge t,U_3\ge t),\qquad 0\le t\le1.
\]
Let \(S(t)\) be the corresponding probability under the canonical *Sierpiński coupling*: independent uniform \(X,Y\) and \(Z=1-(X\oplus Y)\), where \(\oplus\) is bitwise binary exclusive-or, interpreted outside the probability-zero dyadic ambiguity set.

**Theorem (complete diagonal phase law).** At every real threshold \(0\le t\le1\),
\[
M(t)=\begin{cases}1-3t+3t^2,&0\le t\le\tfrac12,\\(1-t)^2,&\tfrac12\le t\le1.\end{cases}
\]
For \(0\le t\le1/2\), \(S(t)=M(t)\). For \(p=1-t\in[2^{-(k+1)},2^{-k}]\), \(k\ge1\),
\[
S(t)=4^{-k}-3\,2^{-k}p+3p^2,
\quad M(t)-S(t)=2\bigl(p-2^{-(k+1)}\bigr)\bigl(2^{-k}-p\bigr).
\]
These formulas agree on shared endpoints, and \(S(1)=M(1)=0\). Thus the Sierpiński coupling attains the optimal diagonal tail exactly for \(t\in[0,1/2]\), for \(t=1-2^{-k}\), \(k\ge1\), and trivially at \(t=1\). At every other threshold it is strictly suboptimal. Moreover the **sharp relative efficiency** is
\[
\inf_{0\le t<1}\frac{S(t)}{M(t)}=\frac34,
\]
attained at every \(t=1-\frac23\,2^{-k}\), \(k\ge1\).

Suboptimality persists for an explicit smooth, strictly increasing score, not just discontinuous threshold indicators. In particular, set
\[
f(x)=\frac1{1+\exp(-512(x-5/8))}.
\]
There exists \(\pi\in\mathcal P\) such that
\[
\mathbb E_\pi\prod_{i=1}^3f(U_i)-\mathbb E_{\mathrm{Sierpiński}}\prod_{i=1}^3f(U_i)>\frac1{128}.
\]

## Assumptions and scope

The marginal law of each coordinate is exactly Lebesgue-uniform on \([0,1]\), and each of the three two-dimensional projections is the independent uniform product measure. No joint independence, density, exchangeability, or conditional-independence hypothesis is imposed. All probabilities are taken with respect to the specified joint law; \(t\) ranges over the entire closed unit interval. The Sierpiński law is the **maximizing** (odd-bit-parity) version \(Z=1-(X\oplus Y)\), rather than the distinct minimizing (even-parity) version \(Z=X\oplus Y\).

## Proof

**1. Sharp general upper tail.** Let \(B_i=\mathbf1_{\{U_i\ge t\}}\) and \(p=1-t\). These Bernoulli variables have common success probability \(p\) and every two are independent. Put \(r=\Pr(B_1=B_2=B_3=1)\). Pair independence gives \(r\le p^2\), while inclusion–exclusion and \(\Pr(B_1=B_2=B_3=0)\ge0\) give \(r\le1-3p+3p^2\). These bounds cross at \(p=1/2\).

Both are attained. For either value \(r=\min\{p^2,1-3p+3p^2\}\), assign the following probabilities to each binary pattern \(b\in\{0,1\}^3\), according to its Hamming weight \(|b|\):
\[
\Pr(B=b)=\begin{cases}
r,&|b|=3,\\ p^2-r,&|b|=2,\\p-2p^2+r,&|b|=1,\\1-3p+3p^2-r,&|b|=0.
\end{cases}
\]
For \(0\le p\le1/2\), the four per-pattern values reduce to \(p^2,0,p(1-p),(1-p)(1-2p)\); for \(1/2\le p\le1\), they become \(1-3p+3p^2,(1-p)(2p-1),(1-p)^2,0\). Thus each is nonnegative, the total mass is one, each one-variable success probability is \(p\), and each two-variable success probability is \(p^2\).

Conditionally on this binary vector, sample the three coordinates independently, with coordinate \(i\) uniform on \([t,1]\) when \(B_i=1\), and on \([0,t)\) otherwise (using the obvious degenerate limiting interpretation at \(t=0,1\)). The individual marginals are uniform, and each pair is independent because its indicator pair is independent and the conditional draws factor. The resulting coupling attains the upper bound. Substituting \(p=1-t\) proves the formula for \(M(t)\).

**2. Sierpiński diagonal.** Outside binary-expansion null sets, write \(X=\sum_{j\ge1}2^{-j}X_j\) and \(Y=\sum_{j\ge1}2^{-j}Y_j\), where all \(X_j,Y_j\) are independent fair bits. The binary digits of \(Z=1-(X\oplus Y)\) are \(Z_j=1-(X_j\oplus Y_j)\). Hence the vectors \((X_j,Y_j,Z_j)\) are independent across \(j\), and each is uniform on \(\{111,100,010,001\}\). This construction proves the one- and two-coordinate uniform independence of the canonical law.

If \(0\le t\le1/2\), the event \(X<t,Y<t,Z<t\) has probability zero: it would require the forbidden initial digit triple \(000\). Pairwise independence and inclusion–exclusion therefore yield \(S(t)=1-3t+3t^2\).

If \(1/2\le t<1\), all three coordinates exceeding \(t\) forces the first digit triple to be \(111\), an event of probability \(1/4\). Conditional on this event, the remaining rescaled binary tails have the original joint law, independently of the first digits. Consequently
\[
S(t)=\frac14 S(2t-1),\qquad 1/2\le t\le1.
\]
For \(p=1-t\in[2^{-(k+1)},2^{-k}]\), iterate this recursion \(k\) times. The resulting threshold is \(1-2^kp\in[0,1/2]\), so
\[
S(t)=4^{-k}\bigl[1-3(1-2^kp)+3(1-2^kp)^2\bigr]
=4^{-k}-3\,2^{-k}p+3p^2.
\]
Subtracting from \(M(t)=p^2\) gives the factored quadratic deficit. It is strictly positive in the interior of every dyadic interval and zero at both endpoints. The independent final-value event at \(t=1\) has probability zero.

**3. Exact worst relative deficit.** On one dyadic interval put \(a=2^{-(k+1)}\), \(p=au\), with \(1\le u\le2\). Then
\[
\frac{M(t)-S(t)}{M(t)}=\frac{2(u-1)(2-u)}{u^2}
=-2+\frac6u-\frac4{u^2}.
\]
Its derivative is \((-6u+8)/u^3\), so the unique maximum is \(1/4\) at \(u=4/3\). Therefore \(S(t)/M(t)\ge3/4\), with equality precisely at \(p=(2/3)2^{-k}\). On the lower-threshold region the ratio equals one.

**4. Analytic strict counterexample.** At \(t_0=5/8\), \(p_0=3/8\), the exact formulas give \(M(t_0)=9/64\) and \(S(t_0)=7/64\), a gap of \(1/32\). Let \(\pi_\star\) be the attaining coupling from Step 1 at this threshold, let \(h=\mathbf1_{[5/8,1]}\), and let \(f\) be the stated logistic function. The logistic is real-analytic and strictly increasing on \([0,1]\) and takes values in \((0,1)\). The elementary inequalities \(1/(1+e^v)<e^{-v}\) for \(v>0\) on either side of the threshold show
\[
\int_0^1|f(x)-h(x)|\,dx<\frac2{512}.
\]
For every coupling in \(\mathcal P\), telescoping a product of three factors in \([0,1]\) gives
\[
\left|\mathbb E\prod_{i=1}^3f(U_i)-\mathbb E\prod_{i=1}^3h(U_i)\right|
\le\sum_{i=1}^3\mathbb E|f(U_i)-h(U_i)|<\frac6{512}.
\]
Subtract this bound for \(\pi_\star\) and for the Sierpiński law from the threshold gap. Their analytic-score expectations differ by strictly more than \(1/32-12/512=1/128\). This completes the proof.

## Verification

Run the included `checker.py` using Python 3. The checker uses only the standard library and rational arithmetic. It exhaustively enumerates the binary first-\(m\)-digit Sierpiński law at every dyadic threshold of level \(m\le6\), compares with both analytic formulas, checks the attaining Bernoulli table's exact pairwise moments and nonnegativity, and tests the relative-efficiency equality across sixteen dyadic scales. The current replay reports 1,504 successful rational assertions. The finite enumerations are diagnostics; the proof above is the argument for all real thresholds and the analytic-score inequality.

## Relationship to prior work

Gladkov, Kolesnikov and Zimin (2018) identified the Sierpiński coupling, including its maximizing odd-parity orientation, as an optimum for the *linear* product score \(xyz\). Omladič, Vuk and Zalar (first public November 10, 2026; primary MSC2020 62H05) develop a general finite-grid copula interpolation and feasibility framework. Those works establish the relevant model and support, but do not assert the complete sharp diagonal exceedance comparison, its dyadic equality set, the optimal \(3/4\) efficiency, or the quantitative analytic-score counterexample. Gvozdev and Kolesnikov (first public November 16, 2026, hence a later comparison rather than the initiating source) give sufficient classes of dyadic score functions for which Sierpiński remains optimal; the present logistic is outside the asserted dyadic linear-score class. General trivariate diagonal-section literature concerns unrestricted copula feasibility rather than this fixed pairwise-independent subclass and its canonical fractal coupling.

## Limitations

The theorem treats three uniform marginals with all pairs independent and a **common** upper threshold, not arbitrary thresholds, higher dimensions, or arbitrary scores. The attaining dependence coupling can vary with the threshold. There is no claim of uniqueness of the attaining law, nor of an exact optimizer for the logistic score: only a rigorous explicit improvement over Sierpiński is shown. Historical priority outside the inspected sources is not certified, and the full text of some older general diagonal-plane copula research was not accessible during the literature comparison. The standalone checker supplies finite exact tests but is not a computer proof of the continuum theorem.

## References

1. M. Omladič, M. Vuk and A. Zalar, *A linear programming approach to finite copula interpolation*, arXiv:2611.14008v1 (first public 2026-11-10), https://arxiv.org/abs/2611.14008.
2. N. A. Gladkov, A. V. Kolesnikov and A. P. Zimin, *On multistochastic Monge-Kantorovich problem, bitwise operations, and fractals*, arXiv:1803.10447 (first public 2018-03-28), https://arxiv.org/abs/1803.10447.
3. D. V. Gvozdev and A. V. Kolesnikov, *On Pairwise Independent and Strongly Correlated Random Variables*, arXiv:2611.20365v1 (first public 2026-11-16; subsequent comparison), https://arxiv.org/html/2611.20365v1.
4. F. Durante, J. Fernández-Sánchez, J. J. Quesada-Molina and M. Úbeda-Flores, *Diagonal plane sections of trivariate copulas*, Information Sciences 333 (2016), 81–87, https://doi.org/10.1016/j.ins.2015.11.024.
