# Joint least-multiplicity-gap laws for regular partitions

## Finding
Fix integers \(\ell\ge2\) and \(R\ge2\). Let \(\mathcal P_\ell(n)\) be the partitions of \(n\) with no part divisible by \(\ell\), and choose \(\lambda\in\mathcal P_\ell(n)\) uniformly. For each \(r\ge1\), define \(M_r(\lambda)\) as the smallest permitted part size \(a\) (meaning \(\ell\nmid a\)) whose multiplicity in \(\lambda\) is less than \(r\). These random variables are finite and satisfy \(M_1\ge M_2\ge\cdots\).

**Exact finite-size joint count.** Put \(A_\ell(t)=\sum_{1\le a\le t,\ \ell\nmid a}a\) for integral \(t\ge0\). For any thresholds \(t_1,\ldots,t_R\in\mathbb Z_{\ge0}\), let
\[
S_\ell(t_1,\ldots,t_R)=\sum_{j=1}^R A_\ell\!\left(\max_{j\le r\le R}t_r\right).
\]
Then the number of \(\lambda\in\mathcal P_\ell(n)\) satisfying \(M_r(\lambda)>t_r\) simultaneously for all \(1\le r\le R\) is exactly
\[
\boxed{\ p_\ell\big(n-S_\ell(t_1,\ldots,t_R)\big)\ },
\]
where \(p_\ell(m)=|\mathcal P_\ell(m)|\) for \(m\ge0\), and \(p_\ell(m)=0\) for negative \(m\).

**Joint scaling limit.** Set
\[
\alpha_\ell=\frac{\pi}{2\sqrt6}\left(1-\frac1\ell\right)^{3/2}.
\]
For all fixed \(x_1,\ldots,x_R\ge0\),
\[
\boxed{
\lim_{n\to\infty}\Pr\big\{M_r>x_r n^{1/4}\text{ for every }1\le r\le R\big\}
=\exp\left[-\alpha_\ell\sum_{j=1}^R\left(\max_{j\le r\le R}x_r\right)^2\right].
}
\]
Equivalently, if \(E_1,\ldots,E_R\) are independent exponential variables of rate \(\alpha_\ell\), then
\[
\boxed{\left(\frac{M_r^2}{\sqrt n}\right)_{r=1}^R\ \Longrightarrow\ \left(\min_{1\le j\le r}E_j\right)_{r=1}^R.}
\]
The law captures non-independent gaps at different multiplicity levels, including the positive probability that different limiting levels coincide.

## Assumptions and scope
All limits are as \(n\to\infty\), with \(\ell,R\), and the nonnegative real thresholds \(x_r\) held fixed. The partition measure is uniform over \(\mathcal P_\ell(n)\). Every allowed positive part is unlimited in multiplicity. The limit does not assert a uniform approximation when \(R\) or \(\ell\) grows with \(n\). The exact finite-size identity holds for all \(n\ge0\) and any nonnegative integer thresholds; for \(n=0\), the all-empty partition is allowed. For \(x_r\ge0\), \(M_r>x_r n^{1/4}\) is equivalent to \(M_r>\lfloor x_r n^{1/4}\rfloor\).

## Proof
**1. Combinatorial shift.** For each permitted part \(a\), the collection of simultaneous events \(M_r>t_r\) forces the multiplicity of \(a\) to be at least
\[
h(a)=\max\big(\{r\in\{1,\ldots,R\}:a\le t_r\}\cup\{0\}\big).
\]
Subtract precisely \(h(a)\) copies of each \(a\) from \(\lambda\). This is a bijection onto \(\mathcal P_\ell(n-S)\), where \(S=\sum_{\ell\nmid a}a h(a)\). The layer-cake identity \(h(a)=\sum_{j=1}^R\mathbf1\{h(a)\ge j\}\), combined with \(h(a)\ge j\iff a\le\max_{r\ge j}t_r\), yields \(S=S_\ell(t_1,\ldots,t_R)\). Thus the finite-size formula is exact for arbitrary, even nonmonotone, thresholds.

**2. Restricted partition asymptotic.** Let \(\rho_\ell=1-1/\ell\). The partition generating function is
\[
F_\ell(q)=\sum_{n\ge0}p_\ell(n)q^n=\frac{\prod_{a\ge1}(1-q^{\ell a})}{\prod_{a\ge1}(1-q^a)}.
\]
The classical Euler-product estimate as \(t\downarrow0\) gives
\[
F_\ell(e^{-t})\sim\ell^{-1/2}\exp\!\left(\frac{\mu_\ell}{t}\right),\qquad
\mu_\ell=\frac{\pi^2\rho_\ell}{6}.
\]
The coefficients \(p_\ell(n)\) are nonnegative and nondecreasing: adding a part of size one is injective. Therefore the standard Ingham coefficient Tauberian theorem applies and gives
\[
p_\ell(n)\sim\frac{\mu_\ell^{1/4}}{2\sqrt{\pi\ell}}n^{-3/4}\exp(2\sqrt{\mu_\ell n}).
\]
In particular, for each nonnegative integer sequence \(S_n=O(\sqrt n)\) with \(S_n/\sqrt n\to s\), the quotient of the two asymptotics gives
\[
\frac{p_\ell(n-S_n)}{p_\ell(n)}\longrightarrow e^{-\sqrt{\mu_\ell}s}.
\]
Here \(n-S_n\to\infty\), so the asymptotic formula applies to both arguments. This step needs no local-limit assumption beyond the quoted coefficient asymptotic.

**3. Joint exponent.** With \(h=\lfloor t/\ell\rfloor\), one has exactly
\[
A_\ell(t)=\frac{t(t+1)}2-\frac{\ell h(h+1)}2
=\frac{\rho_\ell t^2}{2}+O_\ell(t+1).
\]
Take \(t_r(n)=\lfloor x_r n^{1/4}\rfloor\). For every fixed \(j\),
\[
\frac{A_\ell(\max_{r\ge j}t_r(n))}{\sqrt n}\longrightarrow
\frac{\rho_\ell}{2}\left(\max_{r\ge j}x_r\right)^2.
\]
Consequently \(S_n/\sqrt n\to(\rho_\ell/2)\sum_j(\max_{r\ge j}x_r)^2\). Substituting into step 2 and using \(\sqrt{\mu_\ell}\rho_\ell/2=\alpha_\ell\) gives the claimed joint survivor.

**4. Distributional representation.** Let \(E_j\) be independent exponentials of rate \(\alpha_\ell\). The event \(\min_{k\le r}E_k>x_r^2\) for every \(r\) is equivalent to \(E_j>\max_{r\ge j}x_r^2\) for every \(j\). Independence gives exactly the same joint survivor. Upper-orthant survivors determine the law on \([0,\infty)^R\); their convergence at continuity points proves joint convergence in distribution. The positive tie mass in the limiting vector is descriptive only: convergence of probabilities of *exact finite-size equality events* is not claimed.

## Verification
The standalone `verify_joint.py` enumerates partitions independently for each \(n\le24\), each \(2\le\ell\le7\), and all sixty-four threshold triples with entries in \(\{0,1,2,3\}\). It compares 9,600 direct survivor counts with the shifted partition counts. It also tests the layer-cake identity with nonmonotone thresholds and displays illustrative convergence checks for larger \(n\). Run `python verify_joint.py`. The expected output is provided in `verification_output.txt`. This finite evidence supports the exact identity but does not establish the infinite limit; steps 2–4 above provide that proof.

## Relationship to prior work
Bhowmick and Meher (first posted September 25, 2026; arXiv:2609.31104) develop moments of the least \(r\)-gap in unrestricted partitions, at a fixed multiplicity threshold. Wagner (2011) proves a Rayleigh/Weibull limiting law for each single fixed multiplicity threshold, including general admissible-part sets; the one-threshold marginal here is therefore **not new**. The present assertion is the simultaneous dependence between several thresholds, presented as an exact joint shifted count and an explicit exponential-running-minimum law. Neither a formula for this joint survivor nor this coupling was identified in the examined relevant sources. Fristedt's earlier small-part limit theory is a potential source of implicit consequences; its relevance is a historical-priority risk rather than evidence of independence.

## Limitations
The result treats fixed \(\ell\ge2\) and fixed finite \(R\); growing-index regimes, sharp rates of convergence, and finite-size exact tie probabilities are not addressed. The Ingham coefficient asymptotic and Euler-product estimate are classical inputs, not new. The result has not been independently audited. A potentially relevant full text of the September 2026 moment paper was not accessible for exhaustive comparison; its indexed abstract was inspected and the residual overlap risk is recorded in the review.

## References
- S. Bhowmick and N. K. Meher, *On the Moments of Least r-Gaps of Partitions and a Conjecture of Baruah and Talukdar*, arXiv:2609.31104, first posted 2026-09-25, https://arxiv.org/abs/2609.31104.
- S. Wagner, *Limit distributions of smallest gap and largest repeated part in integer partitions*, Ramanujan Journal 25 (2011), 229–246, https://doi.org/10.1007/s11139-010-9264-z; open full text https://www.finanz.math.tugraz.at/~wagner/limitdist.pdf.
- B. Fristedt, *The structure of random partitions of large integers*, Transactions of the American Mathematical Society 337 (1993), 703–735, https://doi.org/10.1090/S0002-9947-1993-1094553-1.
- A. E. Ingham, *A Tauberian theorem for partitions*, Annals of Mathematics 42 (1941), 1075–1090.
