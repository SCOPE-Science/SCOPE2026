# Sharp variance-deficit crossover for unequal-rate Poisson maxima

## Finding

Let \(X_t\) and \(Y_t\) be independent Poisson counts of means \(at\) and \(bt\), respectively, where \(a\ge b>0\), \(t>0\), and let \(M_t=\max(X_t,Y_t)\). Put
\[
D_{a,b}(t)=\mathbb E M_t-\operatorname{Var}(M_t),\quad
E_t=\mathbb E[(Y_t-X_t)_+].
\]
The following **exact identity** holds at every positive intensity:
\[
\boxed{D_{a,b}(t)=\mathbb E[X_t\mathbf 1_{\{X_t=Y_t\}}]+E_t\bigl((a-b)t+E_t\bigr)>0.}
\]
It yields the low-intensity, two-source collision coefficient
\[
D_{a,b}(t)=2ab\,t^2+O_{a,b}(t^3)\qquad(t\downarrow0).
\]
For unequal rates \(a>b>0\), the high-intensity deficit has the **sharp asymptotic equivalent**
\[
\boxed{D_{a,b}(t)\sim
\frac{a^{3/4}b^{1/4}}{\sqrt\pi(\sqrt a-\sqrt b)}
\sqrt t\,\exp\{-t(\sqrt a-\sqrt b)^2\}}
\qquad(t\to\infty).
\]
At the equal-rate boundary \(a=b\), instead
\[
\boxed{D_{a,a}(t)\sim at/\pi.}
\]
Thus the maximum remains strictly underdispersed at every scale, but its absolute variance deficit is exponentially small for distinct rates and linear in intensity when the rates coincide. In particular, the Fano ratio tends to \(1\) when \(a>b\), whereas it tends to \(1-1/\pi\) at equality. The unequal-rate asymptotic is not uniform as \(b\uparrow a\).

A complementary exact identity holds for any finite collection \(X_1,\ldots,X_m\) of independent positive-mean Poisson counts, \(m\ge2\). With \(M=\max_i X_i\), \(R=\sum_iX_i-M\), and \(T\) denoting a tie for the maximum,
\[
\mathbb EM-\operatorname{Var}(M)
=\mathbb E[M\mathbf1_T]+\operatorname{Cov}(M,R)
\ge\mathbb E[M\mathbf1_T]>0.
\]
This complementary fact explains the tie-and-association mechanism; the novel quantitative assertion is the sharp unequal/equal-rate asymptotic dichotomy above.

## Assumptions and scope

All Poisson variables are independent. The parameters \(a,b\) are fixed positive real numbers and \(t\) varies over positive reals. The symbol \(x_+\) means \(\max(x,0)\). For the two-rate statements, labels are chosen so that \(a\ge b\). The variance is the ordinary population variance. No continuity in the rates at the high-intensity limit is asserted. The modified Bessel function \(I_k(z)\) is defined for nonnegative integers \(k\) by
\[
I_k(z)=\sum_{j=0}^{\infty}\frac{(z/2)^{2j+k}}{j!(j+k)!}.
\]

## Proof

**1. Finite-product Poisson identity.** Write \(S=\sum_iX_i\), \(M=\max_iX_i\), and \(R=S-M\). The Poisson size-bias identity gives, with \(e_i\) the unit increment,
\[
\operatorname{Cov}(M,S)
=\sum_i\lambda_i\mathbb E[M(X+e_i)-M(X)]
=\sum_i\lambda_i\Pr\{X_i\ge\max_{j\ne i}X_j\}.
\]
The last sum equals \(\mathbb E[M\mathbf1_{T^c}]\): for each coordinate \(i\), the Poisson recurrence \(k\Pr(X_i=k)=\lambda_i\Pr(X_i=k-1)\) transforms the contribution from the event where \(i\) is the unique maximum into the displayed probability. On the other hand, \(\operatorname{Cov}(M,S)=\operatorname{Var}(M)+\operatorname{Cov}(M,R)\). Rearrangement gives the general identity. Both \(M\) and \(R\) are nondecreasing in every coordinate, since increasing coordinate \(i\) by one increases \(M\) by zero or one and \(R\) by the complementary amount. Independent coordinates are associated (by iterated one-dimensional monotone covariance), so \(\operatorname{Cov}(M,R)\ge0\). For \(m\ge2\) with positive means, the event that exactly two specified counts equal one and all others equal zero has positive probability and contributes positively to \(\mathbb E[M\mathbf1_T]\). Thus the deficit is strictly positive. More quantitatively, for means \(\lambda_i>0\),
\[
\mathbb EM-\operatorname{Var}(M)
\ge e^{-\sum_i\lambda_i}\sum_{i<j}\lambda_i\lambda_j.
\]

**2. Exact two-count decomposition.** In the two-count case, put \(\Delta=(Y_t-X_t)_+\). Then \(M_t=X_t+\Delta\) and \(R_t=\min(X_t,Y_t)=Y_t-\Delta\). Independence gives
\[
\begin{aligned}
\operatorname{Cov}(M_t,R_t)
&=\operatorname{Cov}(\Delta,Y_t-X_t)-\operatorname{Var}(\Delta)\\
&=\mathbb E[\Delta^2]-\mathbb E\Delta\,(b-a)t
  -\bigl(\mathbb E[\Delta^2]-(\mathbb E\Delta)^2\bigr)\\
&=E_t\bigl((a-b)t+E_t\bigr).
\end{aligned}
\]
The only tie with positive weight in the general identity occurs when \(X_t=Y_t\ge1\), so its term is \(\mathbb E[X_t\mathbf1_{\{X_t=Y_t\}}]\). This proves the stated exact identity, positivity and its domain of validity.

**3. Small intensity.** Let \(A=at\), \(B=bt\). The event \(X_t=Y_t=1\) has probability \(ab t^2+O_{a,b}(t^3)\) and contributes \(ab t^2+O(t^3)\) to the tie term. The event \(Y_t=1,X_t=0\) contributes \(bt+O_{a,b}(t^2)\) to \(E_t\), whence \(E_t=bt+O_{a,b}(t^2)\). Therefore
\[
E_t\bigl((a-b)t+E_t\bigr)=ab t^2+O_{a,b}(t^3),
\]
proving the coefficient \(2ab\). The unlisted configurations have total weighted contribution of order at most \(t^3\), controlled by factorial moments of the Poisson sum.

**4. Unequal-rate sharp asymptotic.** Assume \(a>b>0\). Set \(q=\sqrt{b/a}\in(0,1)\), \(z=2t\sqrt{ab}\), and \(c=(\sqrt a-\sqrt b)^2>0\). The standard Skellam probability formula, obtained by summing the two Poisson mass functions, reads
\[
\Pr\{Y_t-X_t=k\}=e^{-(a+b)t}q^kI_k(z),\qquad k=0,1,\ldots .
\]
Consequently,
\[
E_t=e^{-(a+b)t}\sum_{k\ge1}kq^k I_k(z),\quad
\mathbb E[X_t\mathbf1_{\{X_t=Y_t\}}]
=t\sqrt{ab}\,e^{-(a+b)t}I_1(z).
\]
For each fixed nonnegative integer \(k\), \(I_k(z)\sim e^z/\sqrt{2\pi z}\) as \(z\to\infty\). Also \(0\le I_k(z)\le I_0(z)\), for example by the cosine-integral representation of integer-order Bessel functions. Since \(\sum_{k\ge1}kq^k=q/(1-q)^2\), dominated convergence yields
\[
E_t\sim\frac{e^{-ct}}{\sqrt{4\pi t\sqrt{ab}}}\frac q{(1-q)^2}
\quad\text{and}\quad
\mathbb E[X_t\mathbf1_{\{X_t=Y_t\}}]
\sim\frac{t\sqrt{ab}\,e^{-ct}}{\sqrt{4\pi t\sqrt{ab}}}.
\]
The square \(E_t^2\) is negligible relative to \(tE_t\). Substituting into the exact identity and combining the prefactors gives
\[
\begin{aligned}
D_{a,b}(t)
&\sim\frac{t e^{-ct}}{\sqrt{4\pi t\sqrt{ab}}}
\left[\sqrt{ab}+(a-b)\frac{q}{(1-q)^2}\right]\\
&=\frac{a^{3/4}b^{1/4}}{\sqrt\pi(\sqrt a-\sqrt b)}
\sqrt t\,e^{-ct}.
\end{aligned}
\]
Every interchange of the infinite sum is justified by the summable majorant \(kq^k\). This proves a full asymptotic equivalent, not merely a logarithmic decay rate.

**5. Equal-rate boundary and Fano limits.** When \(a=b\), the exact identity becomes
\[
D_{a,a}(t)=t a\,e^{-2at}I_1(2at)+(E_t)^2.
\]
The first term is \(O_a(\sqrt t)\). By the central limit theorem and uniform integrability (the normalized difference has uniformly bounded second moment),
\[
\frac{E_t}{\sqrt t}\longrightarrow
\mathbb E[(\sqrt a\,Z_2-\sqrt a\,Z_1)_+]
=\sqrt{a/\pi},
\]
where the two \(Z_j\) are independent standard normals. Therefore \(D_{a,a}(t)\sim at/\pi\). Finally \(\mathbb EM_t\sim at\) for both \(a=b\) and \(a>b\): the larger-rate Poisson coordinate has mean \(at\), and the excess \(E_t\) is at most of order \(\sqrt t\) at equality and exponentially small when unequal. Dividing the deficits by \(\mathbb EM_t\) proves the two Fano limits.

## Verification

Run `python checker.py` (standard library) for two- and three-count direct enumeration, the exact tie/covariance decomposition, the low-intensity coefficient and both high-intensity regimes. An optional high-precision reproduction of the asymptotic prefactor is `python verify_asymptotic.py` (requires `mpmath`). The numerical scripts use explicit truncations; the proof above establishes the assertions for every real \(t>0\) and the limits as \(t\to\infty\). The high-precision ratio of the exact expression to its leading asymptotic for \((a,b)=(2,1)\) is approximately \(0.93328809\) at \(t=100\) and \(0.96453522\) at \(t=200\), consistently approaching one.

## Relationship to prior work

Badiella, del Castillo and Puig (2023) proved ultra-log-concavity and underdispersion for order statistics of **identically distributed** Poisson counts. Briggs, Song and Prellberg (2009) investigated the location of the maximum's mode in large samples of fixed common Poisson intensity; their full text concerns a different asymptotic regime. This paper's starting observation is not presented as novel. Classical Poisson Poincaré inequalities also imply the qualitative underdispersion bound for a maximum directly; accordingly, the positivity statement alone is not claimed as an original contribution. Established Skellam and modified-Bessel formulas underlie the calculations and are not claimed as new. The substantive additional assertion is the **exact unequal-rate sharp exponential equivalent with its prefactor**, contrasted with the linear equal-rate deficit and tied to the explicit tie-covariance decomposition.

## Limitations

The sharp exponential equivalent requires fixed \(a>b>0\); it is not uniform as the rates coalesce. The theorem concerns independent Poisson maxima, not sums, minima, shared-shock dependent counts, or arbitrary integer-valued parents. The two-rate result does not classify finite-\(t\) monotonicity of the deficit or the Fano ratio. Previously known identical-rate asymptotics and standard Poisson/Bessel identities remain prior work; the historical novelty of the exact unequal-rate prefactor requires independent literature verification. Numerical calculations cannot replace the all-parameter proof.

## References

1. L. Badiella, J. del Castillo, P. Puig (2023), "Ultra log-concavity of discrete order statistics", *Statistics & Probability Letters* 201, 109900. First online 26 June 2023. https://doi.org/10.1016/j.spl.2023.109900 . Open access: https://ddd.uab.cat/pub/artpub/2023/283158/StaProLet_a2023v201n109900.pdf .
2. P. Puig, J. Valero, A. Fernández-Fontelo (2024), "Some mechanisms leading to underdispersion: Old and new proposals", *Scandinavian Journal of Statistics* 51, 245–267, first online 7 August 2023. https://doi.org/10.1111/sjos.12677 .
3. K. M. Briggs, L. Song, T. Prellberg (2009), "A note on the distribution of the maximum of a set of Poisson random variables", arXiv:0903.4373. https://arxiv.org/abs/0903.4373 .
4. J. G. Skellam (1946), "The frequency distribution of the difference between two Poisson variates belonging to different populations", *Journal of the Royal Statistical Society*, Series A 109, 296. Standard distributional identity used in the proof.
