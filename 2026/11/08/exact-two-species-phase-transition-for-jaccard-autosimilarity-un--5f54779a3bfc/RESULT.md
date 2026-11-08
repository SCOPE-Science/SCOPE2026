# Exact two-species phase transition for Jaccard autosimilarity under repeated sampling

## Finding
Let two independently collected samples each contain exactly \(n\ge1\) individuals drawn with replacement from the same two-species community, with species probabilities \(p\) and \(1-p\), where \(0<p<1\). Let \(J_n(p)\) be the expectation of the incidence Jaccard index of the two *observed species sets*. Define
\[
 p_* = \frac{1+\sqrt{\sqrt{41}-6}}{2}=0.8174603272\ldots.
\]
Writing \(r=\max\{p,1-p\}\), the complete discrete sampling-effort phase law is:

1. For \(1/2\le r<p_*\), \(J_n(p)\) is strictly increasing for every integer \(n\ge1\). At \(r=p_*\), the only equality of successive values is \(J_3(p)=J_2(p)\); all other increments are positive.
2. For \(p_*<r<1\), \(J_2(p)>J_1(p)\), but \(J_3(p)<J_2(p)\). Thereafter exactly one transition from negative to positive successive differences occurs: there is one discrete trough, possibly with two adjacent equally minimal values, and no further reversals.
3. For every \(0<p<1\), \(\lim_{n\to\infty}J_n(p)=1\). As \(r\to1\), the first peak \(J_2(p)\to1\), whereas an appropriately growing sample size has \(J_n(p)\to3/4\). Thus the interim drop in expected autosimilarity can approach \(1/4\) despite both samples coming from the same stationary community.

4. Nonmonotonicity is not confined to two-species communities: for every integer \(S\ge2\) there is a strictly positive \(S\)-species abundance vector for which expected Jaccard autosimilarity strictly increases from \(n=1\) to \(n=2\), decreases from \(n=2\) to \(n=3\), and also decreases from \(n=6\) to \(n=7\) before increasing from \(n=7\) to \(n=8\). This extension asserts these four inequalities, not a complete multi-species shape classification.

This is a phase law for the *expectation of the ratio*; it does not equate that expectation with a ratio of expected overlap and union sizes.

## Assumptions and scope
A species set contains a species if at least one individual of that species is sampled. Both size-\(n\) samples are independent and identically distributed; within each sample the \(n\) individuals are iid, with replacement and perfectly observed. Each species has strictly positive mass and the two masses sum to one. The Jaccard similarity of two nonempty finite sets \(A,B\) is \(|A\cap B|/|A\cup B|\). Since \(n\ge1\), the denominator is always nonzero. All assertions about increases, decreases, and extrema refer to integer sample size \(n\) and to expected Jaccard similarity, not realized paths. The model does not assert universal behavior for three or more species, non-iid detection, or sampling without replacement.

## Proof
Put \(q=1-p\), \(a=p^n\), and \(b=q^n\). A sample records only species 1 with probability \(a\), only species 2 with probability \(b\), and both species with probability \(c=1-a-b\). For two independent samples the Jaccard indices are 1 for equal singleton sets or two complete sets, \(1/2\) for a complete-set/singleton pair, and 0 for opposite singleton sets. Consequently
\[
 J_n(p)=a^2+b^2+c^2+c(a+b)
       =1-p^n-q^n+p^{2n}+q^{2n}. \tag{1}
\]
Let \(\Delta_n=J_{n+1}-J_n\). Direct subtraction gives
\[
 \Delta_n=q p^n[1-(1+p)p^n]+p q^n[1-(1+q)q^n]. \tag{2}
\]
The first two increments simplify, with \(t=pq\), to
\[
 \Delta_1=2t^2>0,\qquad
 \Delta_2=t(-2t^2+7t-1). \tag{3}
\]
The only root of \(-2t^2+7t-1\) in \(0<t\le1/4\) is
\[
 t_*=(7-\sqrt{41})/4.
\]
Because \(r(1-r)\) decreases strictly on \(1/2<r<1\), equation (3) makes \(\Delta_2<0\) exactly when \(r>p_*\), with the announced closed form for \(p_*\).

It remains to prove there are no additional alternating phases. By symmetry assume \(p=r\ge q\). Let \(\rho\) be the unique positive root of \(\rho^3+\rho^2=1\). If \(p\le\rho\), then for all integers \(n\ge2\), \((1+p)p^n\le(1+p)p^2\le1\), while \((1+q)q^n<1\) because \(q\le1/2\). Both terms in (2) are nonnegative and the second is strictly positive. Hence every \(\Delta_n>0\) for \(n\ge2\) in this regime.

For \(p>\rho\), divide (2) by the positive factor \(qp^n\), and set
\[
 H_n=\frac{\Delta_n}{qp^n}=1-(1+p)p^n+
 \frac{p}{q}\left(\frac{q}{p}\right)^n
 \left[1-(1+q)q^n\right]. \tag{4}
\]
For all integers \(n\ge2\), writing \(u=q/p\) and \(v=q^2/p\), subtraction yields
\[
 H_{n+1}-H_n=(1+p)qp^n-
 \frac{p}{q}(1-u)u^n+
 \frac{p}{q}(1+q)(1-v)v^n. \tag{5}
\]
The last term is strictly positive since \(0<v<1\). The first two terms have strictly positive sum precisely when
\[
 (1+p)q^2\left(\frac{p^2}{q}\right)^n>p-q. \tag{6}
\]
Since \(p>\rho\), \(p^2>q\), so the left side increases with \(n\). At \(n=2\), (6) is equivalent to
\[
 (1+p)p^4-(2p-1)
 =(p^2+p-1)(p^3+p-1)>0. \tag{7}
\]
Indeed, at \(p=\rho\), \(p^2+p-1=p-p^3>0\) and \(p^3+p-1=p-p^2>0\), and both factors increase with \(p\). It follows that \(H_n\) increases strictly for all \(n\ge2\). Moreover \(H_n\to1\) because \(p<1\) and \(q/p<1\). Thus the signs of the successive increments \(\Delta_n\), for \(n\ge2\), can change at most once, and can change only from negative to positive. Together with (3), this proves the full phase law, including the possibility of a single zero increment at the trough.

Finally, (1) gives \(J_n\to1\) for fixed \(0<p<1\). Let \(p\to1\), \(q=1-p\), and choose the positive integer
\[
 n(p)=\left\lfloor\frac{\log(1/2)}{\log p}\right\rfloor.
\]
Then \(n(p)\to\infty\), \(p^{n(p)}\to1/2\), and \(q^{n(p)}\to0\), so (1) gives \(J_{n(p)}\to3/4\). But \(J_2\to1\) as \(p\to1\), proving the final assertion.

For the extension, fix any integer \(S\ge3\) and let \(\varepsilon>0\) be sufficiently small. Give the first two species masses \((9/10)[1-(S-2)\varepsilon]\) and \((1/10)[1-(S-2)\varepsilon]\), and the other \(S-2\) species mass \(\varepsilon\) each. For each fixed sample size, expected incidence Jaccard is a finite polynomial in the species masses (sum over all ordered pairs of draw sequences). Hence it is continuous as \(\varepsilon\downarrow0\). The four strict inequalities at sample sizes \(1,2,3,6,7,8\) already hold in the limiting two-species law \(p=9/10\) by (1), so all persist for sufficiently small strictly positive \(\varepsilon\). The case \(S=2\) is the witness itself.

## Verification
The exact standalone Python 3 checker `check_autosimilarity.py` verifies (1) independently by enumerating ordered draw sequences in both samples, for seven rational abundance vectors and sample sizes 1 through 8; it also checks (2), (3), the polynomial identity (7), the threshold approximation, and the rational witness. It completed 512 exact checks, including strictly positive three-, four-, five-, and seven-species approximations for the four sign inequalities. No floating-point estimate is used to prove an infinite or universal statement; inequalities (5)–(7) provide the all-parameter analytic step.

With \(p=9/10\), the exact values are
\[
 J_1=41/50,\quad J_2=4181/5000,\quad
 J_3=400721/500000,
\]
so the initial rise and subsequent decline are strict. Furthermore \(J_6>J_7<J_8\), and equation (5) rules out later additional downturns.

## Relationship to prior work
Wolda (1981) investigated random-sample similarity, expected maximum indices, and dependence on sample size and diversity using finite log-series assemblages; that work motivates studying similarity of two replicate samples, but it does not establish the exact two-species parameter threshold or the all-effort one-trough phase theorem identified here. Cao, Williams and Larsen (2002) explicitly introduce average Jaccard autosimilarity among replicate ecological samples for assessing representativeness. Their accessible abstract reports empirical and simulated sampling relationships but supplies no all-parameter result of the form (1)–(7); the complete paper was not accessible for inspection and remains the principal priority risk. Chao, Chazdon, Colwell and Shen (2005) analyze sensitivity of incidence Jaccard similarity to sample size and propose corrected abundance-based indices, which are different estimands; their full primary PDF was inspected in relevant sections. Chase et al. (2011) analyze a uniform species-pool null model and expected Jaccard similarity conditional on local richness; their equally likely species setting does not imply this skew-abundance with-replacement phase law. None of the inspected available primary statements supplies the closed threshold or its global discrete sign classification; this negative search result is not an independent uniqueness certificate.

## Limitations
This theorem addresses one particular stochastic two-species sample model. Observational heterogeneity, spatial clustering, nonreplacement sampling, fixed detected richness, and multi-species communities are not covered. The ratio of expected shared and pooled richness differs from the expected Jaccard ratio and is not analyzed. The exact phase classification applies only to two species; for larger species numbers we establish existence of the specified reversal pattern by continuity, not uniqueness of extrema. The theorem is mathematically proved under the stated assumptions, but novelty relative to all historical literature has not been independently certified. Full inspection of Cao et al. (2002) was blocked by access limitations, so stronger overlapping results in its inaccessible material remain possible.

## References
- Wolda, H. (1981), *Similarity indices, sample size and diversity*, Oecologia 50:296–302, DOI: https://doi.org/10.1007/BF00344966 . Author-accessible PDF: https://ecoevol.ufg.br/adrimelo/div/Wolda1981.pdf .
- Cao, Y., Williams, D. D. and Larsen, D. P. (2002), *Comparison of ecological communities: The problem of sample representativeness*, Ecological Monographs 72:41–56. First published 2002-02-01. DOI: https://doi.org/10.1890/0012-9615(2002)072[0041:COECTP]2.0.CO;2 .
- Chao, A., Chazdon, R. L., Colwell, R. K. and Shen, T.-J. (2005), *A new statistical approach for assessing similarity of species composition with incidence and abundance data*, Ecology Letters 8:148–159. First online 2004-12-17. https://doi.org/10.1111/j.1461-0248.2004.00707.x . Author-provided PDF: https://www.robertkcolwell.org/publications/7597.pdf .
- Chase, J. M., Kraft, N. J. B., Smith, K. G., Vellend, M. and Inouye, B. D. (2011), *Using null models to disentangle variation in community dissimilarity from variation in α-diversity*, Ecosphere 2(2), art. 24. First published 2011-02-28. https://doi.org/10.1890/ES10-00117.1 .
