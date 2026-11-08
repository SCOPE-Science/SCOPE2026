# An order-independent cherry–external-length covariance in Kingman's coalescent

## Finding

In the standard Kingman \(n\)-coalescent with independent rate-one exponential clocks on unordered pairs of extant lineages, let \(C_n\) count cherries (mergers of two singleton lineages) in the resulting rooted binary genealogy, and let \(E_n\) be the sum of the \(n\) external branch lengths. For every integer \(n\ge4\),

\[
\operatorname{Cov}(C_n,E_n)=-\frac{2}{9}.
\]

More finely, let \(S_{n,k}\) be the number of singleton lineages while the process has exactly \(k\) extant lineages. For all integers \(n\ge4\), \(2\le k\le n\),

\[
\boxed{\operatorname{Cov}(C_n,S_{n,k})=
-\frac{k(k-1)(n-k)(n-k-1)}{3(n-1)(n-2)(n-3)}.}
\]

The profile is strictly negative for \(2\le k\le n-2\), and zero for \(k=n-1,n\). The aggregate covariance is nonzero yet independent of sample size. At \(n=2,3\), the cherry count is deterministically one and the covariance is zero.

Using known marginal variance laws, the corresponding correlation satisfies
\[
\operatorname{Corr}(C_n,E_n)\sim-\frac{\sqrt5}{6\sqrt{\log n}}
\quad(n\to\infty).
\]

## Assumptions and scope

Start from \(n\) distinct singleton lineages. At each epoch with \(k\ge2\) lineages, wait \(\tau_k\sim\mathrm{Exp}(\binom{k}{2})\), then merge a uniformly chosen unordered pair of lineages. The waiting times are mutually independent and independent of all merger choices. A singleton lineage contains exactly one original sample leaf; a cherry is created when two such singleton lineages merge, and remains a cherry in the final rooted genealogy. Let \(S_{n,k}\) count singleton lineages *before* the \(k\to k-1\) merger. Thus \(S_{n,n}=n\) and \(E_n=\sum_{k=2}^n S_{n,k}\tau_k\), with each external branch counted until its first merger. Clock rates are not rescaled by population size. The result does not assert a distributional identity or independence.

Write \((x)_{\underline r}=x(x-1)\cdots(x-r+1)\), and \(M_{k,r}=\mathbb E[(S_{n,k})_{\underline r}]\). Throughout the proof \(n\ge4\), and all expectations refer to the same coalescent.

## Proof

**1. Singleton factorial moments.** For \(r\in\{1,2,3\}\), the probability that specified \(r\) initial leaves remain singleton at epoch \(k\) is the product, from \(j=n\) down to \(k+1\), of \(\binom{j-r}{2}/\binom j2\). Hence
\[
M_{k,r}=\frac{(k)_{\underline r}(k-1)_{\underline r}}
{(n-1)_{\underline r}},\qquad 2\le k\le n.
\]
In particular, \(M_{k,1}=k(k-1)/(n-1)\). Falling factorials are zero at the appropriate small-\(k\) boundaries.

**2. Expected future cherries.** Given \(k\) extant lineages of which \(s\) are singleton, define \(f_k(s)\) to be the expected number of cherries created in future mergers. By exchangeability and the pair-choice rule, \(f_k(s)=a_k\binom{s}{2}\). Indeed a merger creates a cherry with probability \(2\binom{s}{2}/[k(k-1)]\), and a specified pair of singleton lineages survives as a pair of singletons until the next epoch with probability \((k-2)(k-3)/[k(k-1)]\). Therefore
\[
a_k=\frac{2}{k(k-1)}+\frac{(k-2)(k-3)}{k(k-1)}a_{k-1},\qquad a_2=1,
\]
and direct induction gives \(a_k=2/[3(k-1)]\) for every \(k\ge3\). At \(k=2\) reached from \(n\ge3\), \(s\le1\), so \(f_2(s)=0\) and the formula \(2\binom{s}{2}/[3(k-1)]\) is also valid on accessible states. Initially \(k=s=n\), yielding \(\mathbb E C_n=n/3\).

**3. Cherries already formed.** Let \(C_k^{\mathrm{past}}\) count cherries formed before epoch \(k\), and put \(A_k=\mathbb E[C_k^{\mathrm{past}} S_{n,k}]\). Clearly \(A_n=0\). Given \(S_{n,k}=s\), a specified singleton survives the next merger with probability \((k-2)/k\); when two singleton lineages merge, the newly created cherry contributes exactly \(s-2\) to the next singleton count. Thus
\[
A_{k-1}=\frac{k-2}{k}A_k+\frac{M_{k,3}}{k(k-1)}.
\]
Dividing by \(M_{k-1,1}\) and summing this first-order recurrence gives
\[
A_k=\frac{k(k-1)}{n-1}\left[
\frac{n-1}{3}-\frac{(k-2)(k-1)(k-3)}{3(n-2)(n-3)}\right].
\]
This expression includes \(k=2\); no division by zero occurs for \(n\ge4\).

**4. The complete mixed singleton profile.** The conditional future mean from step 2 gives, using \(s\binom s2=((s)_{\underline3}+2(s)_{\underline2})/2\),
\[
\mathbb E[C_n S_{n,k}]=A_k+
\frac{M_{k,3}+2M_{k,2}}{3(k-1)}.
\]
Subtracting \((n/3)M_{k,1}\), inserting the three factorial-moment formulas, and simplifying yields
\[
\operatorname{Cov}(C_n,S_{n,k})=
-\frac{k(k-1)(n-k)(n-k-1)}{3(n-1)(n-2)(n-3)}.
\]
Its boundary values and signs follow immediately.

**5. Integrating coalescent epochs.** Independence of waiting times from the entire merger history gives
\[
\begin{aligned}
\operatorname{Cov}(C_n,E_n)
&=\sum_{k=2}^n \mathbb E[\tau_k]\operatorname{Cov}(C_n,S_{n,k})\\
&=-\frac{2}{3(n-1)(n-2)(n-3)}
\sum_{r=0}^{n-2}r(r-1)\\
&=-\frac{2}{9},
\end{aligned}
\]
since \(\mathbb E\tau_k=2/[k(k-1)]\) and the displayed finite sum equals \((n-2)(n-1)(n-3)/3\). At \(n=2,3\), \(C_n=1\), so the covariance vanishes.

For the correlation, the published marginal formulas \(\operatorname{Var}(C_n)=2n/45\) for \(n\ge7\) and \(\operatorname{Var}(E_n)\sim8\log n/n\) imply the stated asymptotic coefficient. This is only a consequence of the finite covariance identity.

## Verification

The standalone Python 3 standard-library script `verify_kingman.py` independently propagates the probability distribution of (singleton count, cherries formed), retaining exact expected accumulated external length, for each order \(2\le n\le30\). It also enumerates *all ordered coalescent merger histories* for \(4\le n\le8\), checking every epoch's covariance formula and the external-length covariance using exact rational arithmetic. Run `python3 verify_kingman.py`. Exhaustive finite checks support but are not substituted for the all-\(n\) proof.

## Relationship to prior work

Janson and Kersting [1] derived the external-length urn representation and its marginal asymptotics and moments. Disanto and Wiehe [2] derived cherry-count distributions and, for sufficiently large orders, their variance. These two separate marginal results do not give a mixed covariance without accounting for the dependence of completed cherry formation and the changing singleton-lineage count. Alimpiev and Rosenberg [3] analyze correlations among six length/time statistics but not this shape–length pairing. Disanto and Wiehe [4] investigate discrete rankings of external branches rather than the present continuous-time cherry–external-total covariance. Blum and François [5] study minimal clades of a *marked leaf* and its external branch, a different indexing and aggregate. François and Mioland [6] examine the *total height of cherries*, not the **number** of cherries, together with external length; their full text was unavailable for an implication comparison. The new ingredient is the exact mixed singleton-epoch profile, which collapses after weighting by coalescence times to a sample-size-independent constant. Priority should not be inferred from absence of an exact string match; uninspected historical mixed-moment studies remain a limitation.

## Limitations

The formulas require the standard neutral binary Kingman coalescent with constant rate one for each pair, no simultaneous multiple mergers, and independently sampled exponential waiting times. Other time normalizations multiply the covariance by the time-scale factor. It is not claimed that cherry count and external length are independent, or that their joint distribution is determined. Full historical priority remains subject to additional expert literature review, particularly potentially implicit mixed-moment recurrences. The computation does not constitute an infinite proof or independent review.

## References

1. S. Janson and G. Kersting, *The external lengths in Kingman's coalescent*, arXiv:1004.5011, first submitted 2010-04-28 UTC; journal version *On the total external length of the Kingman coalescent*, Electronic Journal of Probability 16 (2011), 2203–2218. https://arxiv.org/abs/1004.5011
2. F. Disanto and T. Wiehe, *Exact enumeration of cherries and pitchforks in ranked trees under the coalescent model*, arXiv:1112.1295, first submitted 2011-12-06 UTC; Mathematical Biosciences 242 (2013), 195–200. https://arxiv.org/abs/1112.1295
3. E. Alimpiev and N. A. Rosenberg, *A compendium of covariances and correlation coefficients of coalescent tree properties*, arXiv:2103.13467, 2021. https://arxiv.org/abs/2103.13467
4. F. Disanto and T. Wiehe, *Measuring the external branches of a Kingman tree: A discrete approach*, Theoretical Population Biology 134 (2020), 92–105. https://doi.org/10.1016/j.tpb.2020.05.002
5. M. G. B. Blum and O. François, *Minimal clade size and external branch length under the neutral coalescent*, Advances in Applied Probability 37 (2005), 647–662. Abstract inspected; full text not obtained. https://doi.org/10.1239/aap/1127483740
6. O. François and C. Mioland, *Gaussian approximations for phylogenetic branch length statistics under stochastic models of biodiversity*, Mathematical Biosciences 209 (2007), 108–123. Abstract inspected; full text not obtained. https://doi.org/10.1016/j.mbs.2007.01.005
