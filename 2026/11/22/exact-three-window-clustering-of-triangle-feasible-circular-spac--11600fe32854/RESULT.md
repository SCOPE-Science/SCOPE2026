# Exact three-window clustering of triangle-feasible circular spacings

## Finding

Choose \(n\ge3\) independent uniform points on a circle. Enumerate their clockwise gaps \(G_1,\ldots,G_n\), cyclically, and let \(I_i\) indicate that the lengths \(G_i,G_{i+1},G_{i+2}\) form a **nondegenerate triangle**. Put \(T_n=\sum_{i=1}^{n}I_i\); every subscript is interpreted modulo \(n\).

The exact one-window and overlapping two-window probabilities, whenever the relevant windows use respectively three, four, or five distinct gaps, are
\[
\Pr(I_i=1)=\frac14,\qquad
\Pr(I_iI_{i+1}=1)=\frac19\quad(n\ge4),\qquad
\Pr(I_iI_{i+2}=1)=\frac2{27}\quad(n\ge5).
\]
For three consecutive windows, the genuinely third-order overlap has the further exact value
\[
\boxed{\Pr(I_i=I_{i+1}=I_{i+2}=1)=\frac{232}{4725}\qquad(n\ge5).}
\]
Thus \(\Pr(I_{i+2}=1\mid I_i=I_{i+1}=1)=232/525\), exceeding the unconditional \(1/4\): two adjacent successful triangles predict substantially increased third-window success.

For every \(n\ge3\),
\[
\boxed{\mathbb ET_n=\frac n4,\qquad
\operatorname{Var}(T_n)=\begin{cases}
27/16,&n=3,\\
4/3,&n=4,\\
133n/432,&n\ge5.
\end{cases}}
\]
Moreover, as \(n\to\infty\),
\[
\boxed{\frac{T_n-n/4}{\sqrt{133n/432}}\Longrightarrow N(0,1).}
\]
The large-sample variance is \(133/81\) times the binomial-independence benchmark \(3n/16\). The value \(133/81\) is a variance inflation factor, not a correlation.

## Assumptions and scope

Uniform sampling is with respect to arclength. A random cyclic root may be chosen among the sampled points; the statistic is unchanged by this choice. The cyclic-gap vector is Dirichlet with all parameters equal to one, so it has the distribution of \((X_i/\sum_j X_j)_{i=1}^n\), where the \(X_i\) are independent rate-one exponential variables. The triangle event is homogeneous and can therefore be tested using \(X_i,X_{i+1},X_{i+2}\) directly. The strict inequalities exclude degenerate triangles, which occur with probability zero.

The exact third-window probability requires \(n\ge5\) so that five distinct exponential variables appear. The three-window count is meaningful for \(n=3\) and \(4\), but those small cycles have additional repeated overlaps which are treated separately. The result concerns consecutive **cyclic positions**, not consecutive **size ranks**.

## Proof

**Single window.** For independent exponentials \(A,B,C\), failure of the triangle inequalities means one variable exceeds the sum of the other two. The three failure events are disjoint almost surely, and each has probability
\[
\Pr(A>B+C)=\mathbb Ee^{-B-C}=\frac14.
\]
Hence success probability is \(1-3/4=1/4\).

**Two common gaps.** Given the shared values \(b,c\), the missing independent exponential \(a\) completes a triangle precisely if \(|b-c|<a<b+c\). Its conditional success probability is
\[
q(b,c)=e^{-|b-c|}-e^{-b-c}.
\]
The two outer missing exponentials in two adjacent windows are conditionally independent. Therefore, splitting the positive quadrant into \(b<c\) and \(c<b\),
\[
\Pr(I_iI_{i+1}=1)=\int_0^\infty\!\int_0^\infty e^{-b-c}q(b,c)^2\,db\,dc
=2\left(\frac16-\frac2{12}+\frac1{18}\right)=\frac19.
\]

**One common gap.** Given the single shared value \(c\), two independent exponentials \(a,b\) complete a triangle with conditional probability
\[
g(c)=\Pr(|A-B|<c<A+B)
=e^{-c}(1+c)-e^{-c}=ce^{-c}.
\]
(The first term is the survival probability of a Gamma\((2,1)\) sum, the second that of the absolute difference of two independent exponentials.) The two non-overlapping outer pairs are independent given \(c\); hence
\[
\Pr(I_iI_{i+2}=1)=\int_0^\infty e^{-c}g(c)^2\,dc
=\int_0^\infty c^2e^{-3c}\,dc=\frac2{27}.
\]

**Three consecutive windows.** Write the five independent gaps as \(a,b,c,d,e\). Given \((b,c,d)\), the outer windows succeed independently with probabilities \(q(b,c)\) and \(q(c,d)\). The middle succeeds precisely if \(|b-d|<c<b+d\). Consequently the desired probability equals
\[
\int_{(0,\infty)^3}e^{-b-c-d}
\mathbf1\{|b-d|<c<b+d\}q(b,c)q(c,d)\,db\,dc\,dd.
\]
Partition by the six strict orders of \(b,c,d\). On every order let \(u<v<w\) be their sorted values; the middle triangle condition becomes \(w<u+v\). Expanding the product \(q(b,c)q(c,d)\) gives four signed exponentials with linear exponents. The elementary exact integral for each term is
\[
\int_{0<u<v<w<u+v} e^{-\alpha u-\beta v-\gamma w}\,du\,dv\,dw
=\frac1{(\beta+\gamma)(\alpha+\beta+\gamma)(\alpha+\beta+2\gamma)}.
\]
The resulting contributions from orders \(b<c<d\) and \(d<c<b\) are each \(16/1575\); from \(b<d<c\) and \(d<b<c\) each \(38/4725\); and from \(c<b<d\) and \(c<d<b\) each \(2/315\). Their sum is \(232/4725\). This is an exact integration over all possible triples, not a numerical approximation.

**Finite moments.** Individual indicators have variance \(3/16\). At cyclic distances one and two the covariances are, respectively,
\[
\frac19-\frac1{16}=\frac7{144},\qquad
\frac2{27}-\frac1{16}=\frac5{432};
\]
indicators depending on disjoint exponential triples are independent. For \(n\ge5\), summing all ordered cyclic pairs yields
\[
\operatorname{Var}(T_n)=n\left(\frac3{16}+2\frac7{144}+2\frac5{432}\right)
=\frac{133n}{432}.
\]
For \(n=4\), every two distinct windows share two gaps, so the variance is \(4(3/16)+12(7/144)=4/3\). For \(n=3\), all three indicators coincide, giving \(9(3/16)=27/16\). The expectation is always \(n/4\).

**Gaussian limit.** For an infinite independent exponential sequence define the stationary bounded sequence \(Y_i=\mathbf1\{(X_i,X_{i+1},X_{i+2})\text{ forms a triangle}\}-1/4\). It is two-dependent: collections separated by at least three indices are independent. Its long-run variance is \(\sigma^2=3/16+2(7/144)+2(5/432)=133/432>0\). To obtain the normal limit without an unproved dependence assertion, divide a long linear sum into blocks of length \(\lfloor n^{1/3}\rfloor\), separated by gaps of two indices. Block sums are independent. The deleted centered indicators have variance \(O(n^{2/3})=o(n)\), by bounded two-dependence; the retained blocks have total variance \(n\sigma^2+o(n)\). Every centered retained block is bounded by \(O(n^{1/3})=o(\sqrt n)\), proving the Lindeberg condition. The independent-block central limit theorem follows. The cyclic and corresponding linear sums differ in at most two bounded end indicators, hence share the same limit.

## Verification

The standalone `check_triangle.py` uses only the Python standard library. It verifies the exact rational overlap moments, all three finite-size variance regimes, the six cone contributions to the three-window joint event, and the variance inflation factor; it also runs independently seeded numerical experiments for selected sample sizes and for the third-order probability. Run it with `python check_triangle.py`. Its simulations are diagnostics, not proofs of finite exact identities or the infinite Gaussian limit.

## Relationship to prior work

The Dirichlet/exponential representation is classical; a dated source is Le Caër's 2009 Pearson–Dirichlet analysis. The one-triple success probability \(1/4\) is the classical broken-stick probability and is not claimed as new. General central limit theorems for stationary dependent sequences, including Işlak (2013), establish Gaussian limits under much broader hypotheses. Mirakhmedov (2024) treats general sum-functions of successive circular spacings and supplies generic expectation/variance/CLT machinery. Those general results are acknowledged as covering the **abstract** normal-limit mechanism and variance-template approach, rather than being rebranded here.

The specific claimed contribution is the **explicit all-size local geometric calibration**, particularly the exact third-order joint event \(232/4725\), its conditional cluster probability \(232/525\), and the complete rational finite-size covariance and variance formulas for this defined triangle motif. Published related results on triangle-free independent Pareto sticks and sorted-size broken-stick triples concern different sampling objects and events. No retrieved primary statement evaluated these particular overlapping triangle events. This is a bounded literature comparison, not a proof of historical uniqueness.

## Limitations

No exact full probability mass function for \(T_n\), finite-sample concentration theorem, or local central limit theorem is claimed. The statistical significance asserted is calibration of this particular natural local geometry count, not a new general dependent-sum central limit theorem. The 2009 and 2013 sources provide foundational tools, while the 2024 general spacings paper raises a real risk that aspects of this specialization may be regarded as consequences of its general machinery. Unknown earlier evaluations of the same three-window integrals remain a priority risk. Independent validation has not been performed.

## References

- G. Le Caër, *A Pearson-Dirichlet random walk*, arXiv:0912.3500, initially public 2009-12-17, https://arxiv.org/abs/0912.3500.
- Ü. Işlak, *Asymptotic Normality of Random Sums of m-dependent Random Variables*, arXiv:1303.2386, initially public 2013-03-10, https://arxiv.org/abs/1303.2386.
- S. M. Mirakhmedov, *The central limit theorem for sum-functions of m-tuples of spacings*, arXiv:2404.09581, initially public 2024-04-15, https://arxiv.org/abs/2404.09581.
