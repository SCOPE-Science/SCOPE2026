# Four species are sharp for two Hill-diversity ranking reversals

## Finding
For any integer \(S\ge1\), let \(\mathbf p=(p_1,\ldots,p_S)\) and \(\mathbf r=(r_1,\ldots,r_S)\) be strictly positive probability vectors, each with \(S\) species. Their Hill-diversity profiles at orders \(q>0\) are
\[
D_{\mathbf p}(q)=\begin{cases}(\sum_i p_i^q)^{1/(1-q)},&q\ne1,\\\exp(-\sum_i p_i\log p_i),&q=1.\end{cases}
\]
A *strict ranking reversal* means that as \(q\) increases there are three orders \(0<q_1<q_2<q_3\) for which the strict signs of \(D_{\mathbf p}(q_j)-D_{\mathbf r}(q_j)\) alternate. Then:

1. No pair of communities with \(S\le3\) can have two strict ranking reversals on \(q>0\).
2. For \(S=4\), the two exact profiles
\[
\mathbf p=\frac{(1,9,12,18)}{40},\qquad
\mathbf r=\frac{(3,5,16,16)}{40}
\]
have exactly two intersections on \(q>0\), both strict crossings, one in \((2,3)\) and the other in \((3,4)\). In particular, the Hill-diversity ranking at orders \(2,3,4\) alternates: \(D_{\mathbf p}(2)<D_{\mathbf r}(2)\), \(D_{\mathbf p}(3)>D_{\mathbf r}(3)\), and \(D_{\mathbf p}(4)<D_{\mathbf r}(4)\).
3. For every integer \(S>4\), strictly positive \(S\)-species profiles with exactly these two strict crossings exist.

Thus four species are necessary and sufficient for at least two reversals (and the displayed family has exactly two). This is a statement about population abundance probabilities, not estimated sample diversity.

## Assumptions and scope
All components of both community vectors are strictly positive and sum to one. The two vectors have the same finite richness \(S\). Diversity order \(q\) ranges continuously over \((0,\infty)\), including the removable Shannon limit \(q=1\); \(q=0\) is a fixed common richness endpoint, not a ranking reversal. A crossing is a sign change of the difference of Hill numbers, rather than a mere equality or tangency. Relabeling the species has no effect.

The proof uses a standard elementary fact about exponential polynomials, proved below: for real \(\lambda_1<\cdots<\lambda_k\) and nonzero real \(c_j\), the function \(\sum_{j=1}^{k}c_j e^{\lambda_j x}\) has at most as many real zeros, counted with multiplicity, as the number of coefficient sign changes in \((c_1,\ldots,c_k)\). Equal exponents must first be combined and zero coefficients discarded.

## Proof
**1. Exponential sign-variation lemma.** Proceed by induction on the number of terms. Multiplying by \(e^{-\lambda_1 x}\), reduce the sum to \(g(x)=c_1+\sum_{j=2}^k c_j e^{(\lambda_j-\lambda_1)x}\). Its derivative has the signs of \(c_2,\ldots,c_k\), and \(g(x)\to c_1\) as \(x\to-\infty\). Rolle's theorem, including the usual multiplicity count, bounds the zeros of \(g\) by the zeros of \(g'\) plus one. When \(c_1\) and \(c_2\) have opposite signs, the extra one is exactly the additional coefficient sign change. When they have the same sign, \(g'\) initially has the same sign as \(g\), whereas approaching any first zero of \(g\) from the left forces its derivative to take the opposite sign somewhere. Consequently \(g'\) has at least one additional zero before the first zero of \(g\), so the extra-one allowance is unnecessary. The induction establishes the lemma. The argument equally handles multiple zeros by counting the derivative's multiplicity at each zero.

**2. Lower bound for \(S\le3\).** Sort both probability vectors in nonincreasing order. For \(S\le2\), one vector majorizes the other, so convexity or concavity of the power function makes their Hill order independent of \(q>0\). For \(S=3\), if one vector has both a no-smaller largest coordinate and a no-greater smallest coordinate than the other, it majorizes the other; all Hill numbers are Schur-concave and their rankings cannot reverse. Ties in either extreme are covered by the same comparison, or both vectors are permutations.

The only remaining case, after possibly exchanging the vectors, is
\[
p_1>r_1\ge r_2>p_2\ge p_3>r_3,
\]
which follows from \(p_1>r_1\), \(p_3>r_3\) and equality of the coordinate sums. Define the exponential polynomial
\[
F(q)=\sum_{i=1}^3p_i^q-\sum_{i=1}^3r_i^q.
\]
Along its descending distinct bases the nonzero coefficient signs, before coalescing repeated bases, are \(+,-,-,+,+,-\). Coalescing equal bases cannot increase sign variation, so the lemma gives at most three real zeros counted with multiplicity. Yet \(F(0)=0\) (equal richness) and \(F(1)=0\) (equal total probability). For \(q\ne1\), the sign of the Hill difference equals the sign of \(F(q)/(1-q)\); at \(q=1\) the quotient extends continuously, with its sign determined by the Shannon-entropy difference. Therefore at most one additional zero, counting a possible extra multiplicity of the zero at \(q=1\), can cause a strict change of Hill ranking. Two are impossible.

**3. Four-species witness and exact number of crossings.** Let
\[
F(q)=40^{-q}\left(1^q+9^q+12^q+18^q-3^q-5^q-2(16^q)\right).
\]
Direct integer arithmetic gives
\[
40^2F(2)=4,\qquad40^3F(3)=-54,\qquad40^4F(4)=496.
\]
For \(q>1\), the sign of the Hill difference is opposite that of \(F(q)\). Continuity therefore gives one strict reversal in \((2,3)\) and one in \((3,4)\). To prove there are *exactly* two, arrange the bases in descending order: \(18,16,12,9,5,3,1\). Their coefficients are \(+1,-2,+1,+1,-1,-1,+1\), with exactly four sign changes. The lemma bounds the total number of distinct real zeros by four. They already include \(q=0\), \(q=1\), one zero in \((2,3)\), and one in \((3,4)\), so all four are simple, with no others. In particular \(q=1\) is a removable nonzero comparison of the two Hill profiles rather than an extra crossing.

**4. Larger richness.** For any \(S>4\), choose any \(t\in(0,1)\) and append \(S-4\) identical positive components \((1-t)/(S-4)\) to each of the two vectors after scaling their original four components by \(t\). Their difference of power sums is exactly \(t^qF(q)\) for every real \(q\). Thus the four real zeros, and the two actual Hill-diversity crossings, are unchanged. All components remain strictly positive and sum to one.

## Verification
The standalone `check.py` uses Python's integer and rational arithmetic; it rechecks the three integer moment differences, the four sign variations in the seven-base exponential polynomial, the exact four-component sums, and the scaling identity for several higher richnesses. It independently tests all nonidentical pairs of sorted positive integer three-species abundance vectors with a common total of 40, confirming that their signed moment differences cannot exhibit two reversals over orders \(2\) through \(8\). This finite test is supplementary: the analytic exponential-polynomial lemma and majorization proof, not the finite census, establish the all-real and all-profile statements. Decimal approximations for the two crossings (not used for proof) are \(2.4396978\) and \(3.8423214\).

## Relationship to prior work
Hill (1973) defined the continuous effective-species family that is the object of the theorem. Tóthmérész (1995) compares order-dependent ecological diversity indices and explicitly illustrates an intersection of two diversity profiles (using communities with five and six species), but its studied examples and comparison of graphical methods do not establish the present sharp four-species minimum or a double crossing at orders between two and four. Chao and Jost (2015) explain the scientific significance of crossings and study sampling-based estimators for diversity profiles; their full text supplies no sharp minimum for two crossings of population Hill profiles. The three results are consistent: known order-dependence and single-profile crossings do not imply the sharp threshold, proof, or witness here. The related power-sum, Rényi-entropy, and majorization formulations are mathematically equivalent ways to compare population Hill profiles, not independent discoveries.

## Limitations
The theorem assumes an exact finite probability vector. It does not address sampling variability, the reliability of high-order empirical estimates, unequal species richness, diversity based on phylogenetic or functional distances, or the maximum possible number of crossings for all pairs with \(S\ge5\). The zero-count lemma is classical; novelty, if any, is the sharp ecological four-species statement and its exact multi-crossing construction. A literature search, including full-text inspection of the three named primary papers, cannot by itself establish worldwide historical priority; in particular older literature on power majorization or unpublished data sets could contain equivalent special cases.

## References
1. Hill, M. O. (1973), *Diversity and Evenness: A Unifying Notation and Its Consequences*, Ecology 54, 427–432. https://doi.org/10.2307/1934352 . Full text: https://ricottalab.com/wp-content/uploads/2015/10/hill-1973.pdf . First public journal release recorded as 1973-03-01.
2. Tóthmérész, B. (1995), *Comparison of Different Methods for Diversity Ordering*, Journal of Vegetation Science 6, 283–290. https://doi.org/10.2307/3236223 . Full text: https://ecoevol.ufg.br/adrimelo/div/Tothmeresz1995.pdf .
3. Chao, A. and Jost, L. (2015), *Estimating Diversity and Entropy Profiles via Discovery Rates of New Species*, Methods in Ecology and Evolution 6, 873–882. https://doi.org/10.1111/2041-210X.12349 . First publicly available manuscript recorded as 2015-01-28; full text: https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210x.12349 .
