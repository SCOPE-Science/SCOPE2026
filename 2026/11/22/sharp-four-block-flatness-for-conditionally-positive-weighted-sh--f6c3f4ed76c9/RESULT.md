# Sharp four-block flatness for conditionally positive weighted shifts

## Finding
Let \(W e_n=\lambda_n e_{n+1}\) be a bounded unilateral weighted shift on \(\ell^2(\mathbb N_0)\), with strictly positive real weights, and suppose that \(W\) is *conditionally positive definite* (CPD): for every vector \(h\), the numerical sequence \(\|W^n h\|^2\) is conditionally positive definite on \(\mathbb N_0\). For arbitrary integers \(p\ge1\) and \(\kappa\ge0\), define disjoint block products
\[
 b_j=\prod_{i=0}^{p-1}\lambda_{\kappa+jp+i}\quad(j=0,1,2,3).
\]
If \(b_0=b_1=b_2=b_3=d>0\), write \(r=d^{2/p}>0\). Then if \(\kappa=0\), \(\lambda_n=\sqrt r\) for **all** \(n\ge0\); if \(\kappa\ge1\), there exists \(c\in(0,1]\) with
\[
 \lambda_0=\sqrt{cr},\qquad\lambda_n=\sqrt r\quad(n\ge1).
\]
Consequently \(W\) is subnormal and its Berger measure is \((1-c)\delta_0+c\delta_r\) (take \(c=1\) when \(\kappa=0\)). Four blocks is best possible at **every** block length: three such disjoint equal products, starting at zero, need not force flatness. This includes block lengths for which no pair of individual weights is required equal in the hypothesis.

## Assumptions and scope
All products, norms, and CPD properties are for bounded Hilbert-space unilateral shifts, all weights being strictly positive. The assertion does not cover arbitrary complex phases, non-CPD shifts, or approximate equalities. The sharpness construction below uses a different shift for each integer \(p\ge1\). We use \(\gamma_0=1\) and \(\gamma_n=\prod_{j=0}^{n-1}\lambda_j^2\) for \(n\ge1\).

## Proof
**Positive second-difference measure.** The characterization in Jabłoński–Jung–Lee–Stochel, Theorem 3.1, states that for a bounded CPD unilateral weighted shift there is a finite positive measure \(\mu\) on \([0,\infty)\), of compact support, with
\[
 \Delta^2\gamma_n=\gamma_{n+2}-2\gamma_{n+1}+\gamma_n
 =\int_0^\infty t^n\,d\mu(t)\quad(n\ge0).
\]
Indeed \(\mu=2c_0\delta_1+\nu\) in their representing-triplet notation; this \(c_0\) is unrelated to the parameter \(c\) in the conclusion.

**Subsampled finite-variance collapse.** Put \(h_j=\gamma_{\kappa+jp}\). If four block products equal \(d\), then \(h_j=h_0 q^j\) for \(0\le j\le4\), where \(q=d^2=r^p\). Let \(S_p(t)=1+t+\cdots+t^{p-1}\). The telescoping identity \(\Delta_p^2\gamma_n=\sum_{a,b=0}^{p-1}\Delta^2\gamma_{n+a+b}\) gives
\[
 \Delta^2h_j=\int t^{\kappa}(S_p(t))^2(t^p)^j\,d\mu(t),\qquad j\ge0.
\]
Here the measure \(\eta(dt)=t^{\kappa}S_p(t)^2\mu(dt)\) is positive. For \(q\ne1\), its first three pushed-forward moments are \(h_0(q-1)^2(1,q,q^2)\); hence
\[
 \int (t^p-q)^2\,d\eta(t)=0.
\]
Therefore \(\mu\) is supported on \(\{r\}\) if \(\kappa=0\), and on \(\{0,r\}\) if \(\kappa\ge1\). (For \(t\ge0\), \(S_p(t)>0\), and the factor \(t^\kappa\) only vanishes at zero when \(\kappa>0\).) The same support condition yields \(\Delta^2h_j=h_0(q-1)^2q^j\) for every \(j\ge0\). Matching \(h_0,h_1\) gives \(h_j=h_0q^j\) for every \(j\ge0\).

On the original sequence, the support restriction and the second-difference equation imply \(\gamma_n=A+Bn+Cr^n\) for all \(n\ge1\), with \(C\ge0\). If \(\kappa=0\), the same form holds from \(n=0\). The infinitely many identities \(\gamma_{\kappa+jp}=h_0q^j\), together with \(q=r^p\ne1\), imply \(A=B=0\), \(C=h_0r^{-\kappa}>0\); for \(\kappa=0\), \(C=\gamma_0=1\). If \(\kappa\ge1\), the \(n=0\) second-difference identity gives \(\mu(\{0\})=1-C\), so positivity forces \(C\le1\). Thus \(\gamma_n=Cr^n\) for \(n\ge1\), giving the claimed weights. Their Berger measure is \((1-C)\delta_0+C\delta_r\).

When \(q=1\), the block products and \(h_0,h_1,h_2\) imply \(\int t^\kappa S_p(t)^2d\mu=0\). Thus \(\mu=0\) for \(\kappa=0\) and \(\operatorname{supp}\mu\subseteq\{0\}\) otherwise. Hence \(\gamma_n=A+Bn\) for \(n\ge1\), and \(h_j=h_0\) on an infinite subsequence yields \(B=0\). For \(\kappa=0\), \(\gamma_n=1\) for every \(n\); for \(\kappa\ge1\), \(\gamma_n=C\in(0,1]\) for \(n\ge1\), since \(\Delta^2\gamma_0=1-C=\mu(\{0\})\ge0\). This finishes all cases.

**Optimality of four blocks for every \(p\).** Fix \(p\ge1\), choose \(u=1/2\), \(q=1+\varepsilon\), and \(v=1+2\varepsilon\), where \(\varepsilon>0\) is sufficiently small. Define
\[
 C=\frac{(q-1)^2(v-q)}{(v-u)(u-1)^2},\quad
 D=\frac{(q-1)^2(q-u)}{(v-u)(v-1)^2},\quad
 A=1-C-D,\quad
 B=\frac{q-1-C(u-1)-D(v-1)}p.
\]
Let \(x=u^{1/p}\), \(y=v^{1/p}\), and \(\gamma_n=A+Bn+Cx^n+Dy^n\). For all sufficiently small positive \(\varepsilon\), the coefficients are strictly positive: \(C=O(\varepsilon^3)>0\), \(D\to1/4\), \(A\to3/4\), and \(Bp/\varepsilon\to1/2\). Thus \(\gamma_0=1\), all \(\gamma_n>0\), and \(\gamma_{n+1}/\gamma_n\) is bounded above (since \(\gamma_n\) is a finite sum of positive exponential and linear terms). The sequence defines strictly positive bounded weights \(\lambda_n=\sqrt{\gamma_{n+1}/\gamma_n}\). Its second differences are exactly
\[
 \Delta^2\gamma_n=C(x-1)^2x^n+D(y-1)^2y^n,
\]
so the cited CPD characterization makes this a CPD weighted shift. Direct substitution of the four coefficient equations gives \(\gamma_{kp}=q^k\) for \(k=0,1,2,3\). Consequently the first **three** \(p\)-block products are identical, equal to \(\sqrt q\). Yet the fourth cannot be equal: the induced positive measure for \(\Delta^2(\gamma_{kp})\) has two different support points \(u,v\) with positive masses, so its variance is strictly positive and \(\gamma_{4p}>q^4\). The shift is therefore not flat. Thus four cannot be replaced by three, for any \(p\).

## Verification
The proof invokes only a stated published CPD moment representation, elementary finite-difference identities, a nonnegative variance integral, and the explicit coefficient limits. The optimality construction can be checked symbolically for any specified \(p\). Its all-integer positivity and boundedness follow from positive coefficients and not from finite enumeration. No external infinite computation is assumed.

## Relationship to prior work
Jabłoński–Jung–Lee–Stochel (2021), Theorems 3.1 and 8.1–8.5, establish the CPD moment representation, four-consecutive-*individual*-weight flatness, and the sharpness of four in that individual-weight setting. The result here changes the observation to **four disjoint equal products of arbitrary fixed block length**, from an arbitrary starting index, and supplies a separate all-block-length optimality construction. The case \(p=1\) is the established special case, not a new result. Applying their flatness theorem to powers yields a related shorter route to parts of the rigidity statement, so novelty is claimed only for the combined sparse-block statement and its uniform sharpness construction.

## Limitations
This is a CPD-specific exact-rigidity theorem. It gives no stability estimate for nearly equal products, and does not address shifts with nonpositive or unbounded weights. The all-block-length sharpness construction establishes existence, not classification of every nonflat three-block example. Prior stronger results not located in the inspected corpus may affect historical priority; independent audit has not been performed.

## References
1. Z. J. Jabłoński, I. B. Jung, E. Y. Lee, J. Stochel, *Conditionally positive definite unilateral weighted shifts*, arXiv:2106.03222, first posted 2021-06-06; Theorem 3.1, Section 8. https://arxiv.org/abs/2106.03222
2. C. Benhida, R. E. Curto, G. R. Exner, *Conditional positive definiteness as a bridge between k-hyponormality and n-contractivity*, arXiv:2012.10962 (2020). https://arxiv.org/abs/2012.10962
