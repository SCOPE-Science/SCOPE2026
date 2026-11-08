# Four species are necessary and sufficient for two reversals in expected species accumulation rankings

## Finding
For each integer \(S\ge1\), compare two strictly positive abundance vectors \(\mathbf p,\mathbf q\in(0,1)^S\), each summing to one. Draw \(n\) individuals independently with replacement from either community, and let \(R_{\mathbf p}(n)\) be the expected number of distinct species observed. Define *two strict ranking reversals* to mean the existence of integers \(2\le n_1<n_2<n_3\) such that the two differences \(R_{\mathbf p}(n_1)-R_{\mathbf q}(n_1)\), \(R_{\mathbf p}(n_2)-R_{\mathbf q}(n_2)\), and \(R_{\mathbf p}(n_3)-R_{\mathbf q}(n_3)\) are all nonzero and alternate in sign.

**Theorem.** Such two reversals are possible **if and only if** \(S\ge4\). For \(S\le2\), the ranking is fixed at all sample sizes. For \(S=3\), the curves can reverse their strict ranking at most once as the sample size increases, even under continuous interpolation to every real \(t>1\). Four species achieve two reversals already at sample sizes \(n=2,5,12\). For every larger \(S\), a strictly positive rational abundance-vector pair achieves the same three alternating signs.

An explicit four-species pair, with coordinate order irrelevant, is
\[
\mathbf p=(1,5,5,11)/22,\qquad \mathbf q=(2,2,9,9)/22.
\]
For this pair the exact scaled difference is
\[
22^n\bigl(R_{\mathbf p}(n)-R_{\mathbf q}(n)\bigr)
=2(20^n+13^n)-21^n-2\cdot17^n-11^n,
\]
and the values at \(n=2,5,12\) are respectively \(-2\), \(57720\), and \(-285614243977922\).

## Assumptions and scope
The populations have the **same** true species richness \(S\), all abundances are positive, and individual draws are independent with replacement. The ranking is of *expected sampled richness*, not of realized random sample richness or of Shannon or Simpson diversity. Nonzero alternating signs at three increasing integer sizes count as two strict reversals, without any claim about crossings at further sample sizes. The formula interpolates analytically from integer \(n\) to real \(t\ge0\), with \(0<1-p_i<1\) for \(S\ge2\).

## Proof
**1. Expected richness identity.** A species of mass \(p_i\) remains unobserved after \(n\) independent draws with probability \((1-p_i)^n\). Summing the species-detection indicators gives
\[
R_{\mathbf p}(n)=S-\sum_{i=1}^S(1-p_i)^n.
\]
For real \(t\ge0\), define the same analytic expression \(R_{\mathbf p}(t)\). All pairs satisfy \(R_{\mathbf p}(1)=1\); with equal support sizes, \(R_{\mathbf p}(0)=0\) as well.

**2. A zero-count lemma.** If \(\lambda_1<\cdots<\lambda_m\) are distinct reals and nonzero real \(c_1,\ldots,c_m\) have \(v\) sign changes, then the nonzero exponential polynomial \(f(t)=\sum_{j=1}^m c_j e^{\lambda_jt}\) has at most \(v\) real zeros, counted with multiplicity. Here is a self-contained induction. Divide by \(e^{\lambda_1t}\). The resulting \(g\) tends to \(c_1\) as \(t\to-\infty\). Its derivative is an exponential polynomial whose ordered coefficients have exactly the sign changes of \((c_2,\ldots,c_m)\). If \(c_1\) and \(c_2\) have opposite signs, Rolle's theorem (including multiplicities) gives \(N(g)\le N(g')+1\), exactly the extra allowable sign change. If they have the same sign, \(g\) and \(g'\) both initially have the sign of \(c_1\). Before the first zero of \(g\), its derivative must change sign, producing one additional derivative zero; Rolle's theorem supplies the rest. Hence \(N(g)\le N(g')\), with no extra sign change. This proves the lemma by induction, including ties after equal exponent terms are combined.

**3. Three-species obstruction.** For \(S=2\), any two abundance vectors are comparable under majorization. Since \(x\mapsto(1-x)^t\) is convex on \([0,1]\) for \(t>1\), their richness ranking cannot reverse. The same argument applies for \(S=3\) whenever the two vectors are comparable by majorization. Otherwise, after sorting their entries increasingly and possibly swapping the two vectors, their extremes must satisfy \(p_1<q_1\) and \(p_3<q_3\); the equal-sum condition gives \(q_2<p_2\). Thus
\[
p_1<q_1\le q_2<p_2\le p_3<q_3.
\]
The signed exponential sum \(F(t)=\sum_i(1-p_i)^t-\sum_i(1-q_i)^t\) has coefficient signs \(+,-,-,+,+,-\) when its exponent bases are ordered by the corresponding masses, or the reversed sequence when ordered by increasing exponential exponents. There are at most three sign changes, and merging any tied exponents cannot increase this count. Unless \(F\) is identically zero (when the multisets coincide), the lemma therefore gives at most three real zeros. Two are forced at \(t=0\) and \(t=1\) by equality of species counts and total masses. At most one zero remains in \((1,\infty)\), so two strict ranking reversals are impossible for three species. For \(S=1\), richness is identically one at positive sample sizes.

**4. Exact four-species witness.** The formula in Finding follows by substituting the two four-entry abundance vectors. Direct integer exponentiation yields the three displayed scaled differences. Consequently \(R_{\mathbf p}-R_{\mathbf q}\) has signs \(-,+,-\) at \(n=2,5,12\). By continuity there are at least two distinct real crossings between those three sample sizes.

**5. Every larger richness, explicitly.** For any integer \(S>4\), fix \(\varepsilon=1/10000\). Multiply each of the four original masses in both communities by \(1-\varepsilon\), and append \(S-4\) equal species masses \(\varepsilon/(S-4)\) to both. Both vectors remain strictly positive and normalized. The appended species contribute identically to the two richness expectations. For \(0\le x\le1\) and integer \(n\ge1\), the mean-value theorem gives
\[
\bigl|(1-(1-\varepsilon)x)^n-(1-x)^n\bigr|\le n\varepsilon x.
\]
Summing over four entries in each community bounds the change in their richness *difference* by \(2n\varepsilon\). The absolute four-species witness differences at \(n=2,5,12\) are respectively \(2/22^2\), \(57720/22^5\), and \(285614243977922/22^{12}\), each strictly larger than \(2n/10000\) at its corresponding \(n\). Their alternating signs survive for every \(S>4\), completing the sharp classification. Because the witness inequalities are strict, two reversals also hold in an open neighborhood of each displayed pair of abundance vectors.

## Verification
A standard-library-only Python checker, `checker.py`, recomputes all three integer differences; independently builds the distribution of sets of seen species by exact weighted dynamic programming, rather than using the species-detection formula; verifies all three strict margins needed for the larger-species construction; and performs supplementary complete finite checks over integer three-species probability vectors with modest denominators. The finite checks illustrate but do not replace the all-real-parameter proof above. Run `python3 checker.py` from the directory containing this document and the checker.

## Relationship to prior work
The Good–Hurlbert species-accumulation identity and the sampling-effort ranking problem are classical. Lande, DeVries, and Walla (2000) analyze intersections in particular when the assemblage with fewer total species has greater Simpson diversity. Thompson and Withers (2003) document a crossing between two simulated communities with the same 24 species under different trapping and regression protocols, without a minimal-support or two-reversal statement. Chao and Jost (2012) establish a correspondence between crossings of size-based and coverage-based species-richness curves, while Chao and colleagues (2014) develop general rarefaction/extrapolation methods. These works establish why crossings matter; the result here distinguishes a different precise question: the least **equal true richness** allowing **two strict sample-size ranking reversals**. The obstruction for at most three species and explicit stable four-species construction together give that exact support threshold. The underlying exponential-polynomial sign-variation lemma is classical and is not claimed as a new general theorem.

## Limitations
This concerns independent, identically distributed sampling *with replacement* and exact true abundance vectors; it is not a hypothesis test or an inference result under unknown abundances. Actual sample-richness rankings fluctuate and may cross differently. The classification answers existence of two strict reversals, **not** the maximum number of crossings for all larger species counts. A broad historical-priority risk remains because multiple crossings are already recognized in the ecological literature; the claimed distinction is the sharp four-species support cutoff, which may have an unlocated earlier formulation. Independent scientific audit has not been performed.

## References
1. Lande, R., DeVries, P. J., and Walla, T. R. (2000). *When species accumulation curves intersect: implications for ranking diversity using small samples*. Oikos 89, 601–605. https://doi.org/10.1034/j.1600-0706.2000.890320.x (publisher reports first online 2003-04-17; issue year 2000).
2. Chao, A. and Jost, L. (2012). *Coverage-based rarefaction and extrapolation: standardizing samples by completeness rather than size*. Ecology 93, 2533–2547. https://doi.org/10.1890/11-1952.1.
3. Chao, A. et al. (2014). *Rarefaction and extrapolation with Hill numbers: a framework for sampling and estimation in species diversity studies*. Ecological Monographs 84, 45–67. https://doi.org/10.1890/13-0133.1. Lawful full text: https://www.robertkcolwell.org/publications/6842.pdf.
4. Thompson, G. G. and Withers, P. C. (2003). *Effect of species richness and relative abundance on the shape of the species accumulation curve*. Austral Ecology 28, 355–360. https://doi.org/10.1046/j.1442-9993.2003.01294.x.
