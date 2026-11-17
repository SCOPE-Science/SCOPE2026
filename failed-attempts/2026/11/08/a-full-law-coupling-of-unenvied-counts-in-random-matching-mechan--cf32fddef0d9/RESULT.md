# A full-law coupling of unenvied counts in random matching mechanisms

## Finding

For every integer \(n\ge 1\), consider \(n\) students with independent uniformly random complete strict preferences over \(n\) schools. For each allocation, count the students whose assigned school is not strictly preferred by any other student to that other student's own assignment. Write the count as \(U_n\).

**Theorem.** The entire distribution of \(U_n\) is the same under random serial dictatorship (RSD) and under student-proposing deferred acceptance (DA), even when DA's complete strict school priorities are fixed arbitrarily and independently of the students' preferences. The common law is also exactly the law of the number of coupon types seen precisely once when independent uniform coupons are sampled until all \(n\) types have been seen. In particular, for \(1\le u\le n\),

\[
\Pr(U_n=u)=u\binom{n}{u}\int_0^\infty x^{u-1}(e^x-1-x)^{n-u}e^{-nx}\,dx.
\]

The integral is the *previously known* coupon-singleton distribution of Myers and Wilf, now identified with both matching mechanisms. The common random count has exact mean and variance

\[
\mathbb E U_n=H_n,\qquad
\operatorname{Var}(U_n)=H_n^2+2H_n^{(2)}-3H_n,
\]

where \(H_n=\sum_{j=1}^n j^{-1}\) and \(H_n^{(2)}=\sum_{j=1}^n j^{-2}\). More importantly, its relative fluctuations do not disappear:

\[
\frac{U_n}{\log n}\ \xrightarrow{\mathrm d}\ \operatorname{Exp}(1)\qquad(n\longrightarrow\infty).
\]

Here \(\operatorname{Exp}(1)\) is the mean-one exponential law. The exponential limit applies to the number of unenvied students under *both* mechanisms; it does not assert identical assignments, identical envy graphs, or identical distributions of other welfare measures.

## Assumptions and scope

The market is square and one-to-one. Students' rankings are mutually independent, uniformly distributed over all \(n!\) strict orders, complete, and independent of all school priority orders. Under RSD, the priority order of students is fixed in advance or drawn independently; by exchangeability, its unconditional count law is the same. Under DA, schools have arbitrary complete strict priorities fixed before student preferences are drawn (or random priorities independent of them). The two mechanisms run to complete matchings. An agent \(i\) is unenvied exactly when for all \(j\ne i\), student \(j\) prefers her own allocated school to the school allocated to \(i\).

The result concerns an ex-post *count* sampled across random student preferences, not ex-ante envy-freeness. There are no ties, unfilled seats, unacceptable assignments, unequal capacities, or correlated student rankings. The logarithmic normalization is relevant for \(n\ge 2\).

## Proof

**1. RSD produces an exact count Markov chain.** Fix an ordering of the students and expose preferences one student at a time. After the first \(j-1\) allocations, suppose exactly \(r\) of the already assigned students have not been envied by any earlier student. There are \(m=n-j+1\) schools still available. The next student chooses her best school from these \(m\); she destroys the provisional unenvied status of exactly those of the \(r\) prior students whose schools she ranks above her own chosen school. Since her complete preference is independent and uniformly random, the relative order of the \(m\) available schools and the \(r\) distinguished earlier schools is uniformly random. If \(h\) old unenvied students are destroyed, the first \(h\) objects in this restricted random order are distinguished schools and the next object is available. The exact probability is

\[
q_{m,r}(h)=\frac{m\,(r)_h}{(m+r)_{h+1}},\qquad 0\le h\le r,
\]

with falling factorials \((v)_h=v(v-1)\cdots(v-h+1)\) and \((v)_0=1\). All earlier students are unable to envy the new student, because their selected schools were best among sets containing her later school. Therefore the new provisional unenvied count is \(r+1-h\). With \(R_1=1\), this gives an exact finite transition law for every \(j=2,\ldots,n\).

**2. Coupon singletons have exactly the same transition law.** Independently draw coupons uniformly from \(n\) types. View the process only at successive first appearances of new coupon types. Just after the first appearance of the \((j-1)\)-st distinct type, suppose \(r\) types have appeared exactly once; \(m=n-j+1\) types remain unseen. Until the first unseen type is drawn, previously seen non-singletons can be ignored because additional copies cannot restore singleton status. Discarding those irrelevant draws, the order of *first appearance* among the \(m\) unseen types and the \(r\) singleton types is a uniform random permutation of these \(m+r\) distinct types. Thus the number \(h\) of singleton types hit before the first unseen type has precisely probability \(q_{m,r}(h)\). That new unseen type starts as a singleton. Consequently the number of coupon singletons after successive distinct-type discoveries follows the same chain as the provisional unenvied RSD count, with the same initial state. At discovery number \(n\), both terminal counts therefore have identical distributions.

**3. The DA coupon identification is pathwise.** An independent uniformly random strict student ranking can be generated from an infinite stream of independent uniformly drawn schools by retaining their first appearances in order. Run student-proposing DA sequentially and, whenever a student needs her next preference, read her stream until a school she has not proposed to appears. The concatenation of all raw draws requested by the adaptive algorithm is i.i.d. uniform: each next draw is fresh and independent even when the proposing student is selected adaptively. The algorithm terminates exactly when every school has first received a proposal, which is also the first time that every school has appeared among the raw draws. A school with only one student proposal is unenvied: no other student ranks it above her eventual placement. A school with at least two distinct proposers is envied by a rejected proposer. Finally, if a student makes a discarded repeat raw draw, a second proposer must previously have displaced that student at the corresponding school, so such repeats cannot occur at a school with only one proposer. Thus the unenvied schools are exactly the coupon types seen once among all raw draws before completion. This argument uses the strict priorities to determine rejections but not their distribution. It holds for every fixed priority profile. Combined with step 2, it proves the equality in full distribution.

**4. Finite law and moments.** Myers and Wilf determined the displayed exact integral distribution for singleton coupons. To verify the new matching identity independently of that integral, fix \(1\le i_1<\cdots<i_r\le n\), denoting RSD positions. In the next student's ranking, avoidance of envy toward \(t\) distinguished earlier positions occurs with conditional probability \(m/(m+t)\), where \(m\) is the number of still available schools. Multiply these factors over all later chooser positions. They telescope to

\[
\Pr(i_1,\ldots,i_r\text{ all unenvied})
=\frac{r!}{\prod_{s=1}^r(n-i_s+s)}.
\]

Taking \(r=1\) gives \(\mathbb E U_n=H_n\). Taking \(r=2\), setting \(a=n-i_1+1\) and \(b=n-i_2+1\), and using \(\sum_{a=1}^n H_a/a=(H_n^2+H_n^{(2)})/2\), yields

\[
\mathbb E (U_n)_2
=4\sum_{a=2}^{n}\sum_{b=1}^{a-1}\frac{1}{a(b+1)}
=2H_n^2+2H_n^{(2)}-4H_n.
\]

Since \(\operatorname{Var}(U_n)=\mathbb E(U_n)_2+\mathbb E U_n-(\mathbb E U_n)^2\), the stated variance follows.

**5. Exponential weak limit.** For each fixed positive integer \(r\), summing the joint probabilities in step 4 over ordered distinct positions gives

\[
\mathbb E(U_n)_r=(r!)^2
\sum_{n\ge a_1>\cdots>a_r\ge1}
\prod_{s=1}^{r}\frac{1}{a_s+s-1}.
\]

The shifted factors differ from \(\prod_s a_s^{-1}\) by a total sum of at most \(O_r((\log n)^{r-1})\): telescope the products and use \(\sum_{a\ge1}a^{-2}<\infty\) for any factor containing a shift. The unshifted sum is the \(r\)-th elementary symmetric polynomial in \(1,1/2,\ldots,1/n\), equal to \((\log n)^r/r!+O_r((\log n)^{r-1})\) because terms with repeated indices contribute at most \(O_r((\log n)^{r-2})\). Hence

\[
\mathbb E(U_n)_r=r!(\log n)^r+O_r((\log n)^{r-1}).
\]

Ordinary and falling-factorial moments of fixed order have the same leading asymptotics, so \(\mathbb E[(U_n/\log n)^r]\to r!\) for every \(r\ge1\). These are the moments of \(\operatorname{Exp}(1)\), a moment-determinate probability law (for example, by Carleman's criterion). The method of moments proves the claimed distributional convergence. No unproved interchange of an infinite limit with a finite experiment is used.

## Verification

The accompanying standalone Python program `verify.py` performs exact rational arithmetic. It compares the RSD transition recurrence against an independently expanded version of Myers–Wilf's coupon-singleton integral for \(1\le n\le9\), verifies all factorial moments through order \(5\), and enumerates all \((n!)^n\) complete student preference profiles for RSD for \(1\le n\le4\) (including all \(331{,}776\) profiles at \(n=4\)). It independently enumerates DA with all school priority profiles for \(1\le n\le3\), and confirms the common law separately for each of the \(216\) strict three-school priority profiles. It reported `PASS 285 independent distribution, moment and exhaustive comparisons`. These finite checks support, but are not substitutes for, the analytic arguments for arbitrary \(n\).

For example, the complete common distributions are \(\Pr(U_3=1,2,3)=(7/18,7/18,2/9)\) and \(\Pr(U_4=1,2,3,4)=(97/288,97/288,67/288,3/32)\).

## Relationship to prior work

Ortega, Ziegler, Arribillaga and Zhao (2026) prove that DA and RSD each have expected unenvied count \(H_n\). Their DA proof couples unenvied schools to singleton types in a uniform coupon-collection process, whereas their RSD analysis separately proves the expectation by telescoping conditional probabilities. The full *law* of RSD is not established there, and equality of the complete DA and RSD distributions does not follow from equality of means. The present result supplies the missing transition-law identification. Their primary text was checked across the introduction, Sections 2–4 and the comparison with RSD.

Myers and Wilf (2003/2006), Section 4, already established the coupon-singleton distribution and its expectation. The integral is therefore **not** claimed as a new coupon-collector formula. The new mathematical assertion is the exact distributional coupling to RSD (and hence the equality with DA); the explicit variance and exponential scaling are consequences worked out here. The earlier article's Section 4, including the distribution formula and references, was examined. General references on stochastic assignment and matching do not imply equality of envy-count laws without this coupling.

## Limitations

The assertion fails to address dependent or nonuniform student preferences, non-square markets, multiple seats per school, weak preferences, or arbitrary adaptive priority selection correlated with preferences. The limiting exponential distribution is a weak limit, not a finite-market identity or a concentration result. Although published primary texts and relevant research records were searched, absence of an indexed equivalent cannot guarantee publication priority; independent scientific validation remains outstanding. The source-coupon formula and the mean \(H_n\) are explicitly credited as prior results.

## References

1. J. Ortega, G. Ziegler, R. P. Arribillaga and G. Zhao, *The Distribution of Envy in Matching Markets*, Economics Letters 263 (2026), article 112936, first online March 12, 2026. https://doi.org/10.1016/j.econlet.2026.112936 ; open preprint https://arxiv.org/abs/2603.23385 .
2. A. N. Myers and H. S. Wilf, *Some New Aspects of the Coupon-Collector's Problem*, arXiv:math/0304229 (2003), Section 4; SIAM Review 48 (2006), 549–565. https://arxiv.org/abs/math/0304229 ; https://doi.org/10.1137/060654438 .
3. J. Ortega, G. Ziegler, R. P. Arribillaga and G. Zhao, *The Large and Likely Inefficiency of Stable Matching Mechanisms*, arXiv:2407.19831 (2024, subsequent revisions), background on envy digraphs, https://arxiv.org/abs/2407.19831 .
