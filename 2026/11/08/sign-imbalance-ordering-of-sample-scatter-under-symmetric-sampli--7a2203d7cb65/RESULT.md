# Sign-imbalance ordering of sample scatter under symmetric sampling

## Finding

Let \(n\ge 2\), let \(X_1,\ldots,X_n\) be independent and identically distributed real random variables symmetric about zero, with \(\Pr(X_1=0)=0\) and \(0<\mathbb E[X_1^4]<\infty\). Define the sign count \(K=\#\{i:X_i>0\}\), its imbalance \(h=2K-n\), and the centered sum of squares
\[
Q=\sum_{i=1}^n(X_i-\overline X)^2.
\]
Write \(Y=|X_1|\) and \(a=\mathbb EY\), \(b=\mathbb EY^2\), \(c=\mathbb EY^3\), \(f=\mathbb EY^4\). Define
\[
V=\frac{n-1}{n}\bigl((n-1)f-(n-3)b^2\bigr),\qquad
A=\frac{2a^4(n-1)}n,
\]
\[
B=\frac{4a}{n^2}\left((n-2)\mathbb E[Y(Y-a)^2]+\operatorname{Cov}(Y^2,Y)\right).
\]
For every \(k\in\{0,\ldots,n\}\), taking \(h=2k-n\),
\[
\boxed{\mathbb E[Q\mid K=k]=(n-1)b+\frac{a^2}{n}(n-h^2),}
\]
\[
\boxed{\operatorname{Var}(Q\mid K=k)=V-A+B(n-h^2).}
\]
In particular, conditional mean decreases strictly as \(|h|\) grows. If \(Y\) is not almost surely constant, then \(B>0\) and conditional variance also decreases strictly with \(|h|\). When \(Y\) is constant, its conditional variance is identically zero. The fraction of the variance in \(Q\) explained by optimal prediction from \(K\) is exactly
\[
\boxed{\frac{\operatorname{Var}(\mathbb E[Q\mid K])}{\operatorname{Var}(Q)}
=\frac{2a^4}{(n-1)f-(n-3)b^2}.}
\]
Although \(\operatorname{Cov}(Q,K)=0\), with \(H=(2K-n)^2\) one has
\[
\operatorname{Cov}(Q,H)=-2a^2(n-1),\qquad
\operatorname{Corr}(Q,H)=-\sqrt{\frac{2a^4}{(n-1)f-(n-3)b^2}}.
\]
For Gaussian observations \(X_i\sim N(0,\sigma^2)\), the explained fraction is \(4/(\pi^2n)\) and the latter correlation is \(-2/(\pi\sqrt n)\). When \(Y\) is nonconstant, the explained fraction is asymptotic to \(2a^4/(n(f-b^2))\). When \(Y\) is constant it equals one for every \(n\).

## Assumptions and scope

All identities are exact for every integer \(n\ge2\). Symmetry means \(X_1\overset{d}{=}-X_1\). The no-atom-at-zero assumption is needed for an independent fair sign and magnitude representation, including for discrete symmetric laws. Only the fourth absolute moment is needed. The conditional variance monotonicity is strict between attainable distinct values of \(|2k-n|\) when the magnitude law is nonconstant; conditioning on \(K=k\) always has positive probability. The scatter \(Q\) is \((n-1)\) times the unbiased empirical variance, and the explained-variance ratio is unchanged by that scaling.

## Proof

Write \(X_i=\varepsilon_iY_i\), where the \(\varepsilon_i\) are independent fair signs, the \(Y_i\) are independent copies of \(Y>0\), and the two arrays are independent. Consequently \(K\sim\operatorname{Bin}(n,1/2)\). Condition on a fixed sign vector with sum \(h\); exchangeability makes the ensuing formulas depend only on \(h\). Put \(S=\sum_i\varepsilon_iY_i\) and \(T=\sum_iY_i^2\). Then \(Q=T-S^2/n\). Direct expansion gives
\[
\mathbb ET=nb,\qquad \mathbb E[S^2\mid\varepsilon]=nb+a^2(h^2-n),
\]
which proves the conditional-mean identity.

For the conditional-variance identity let \(v=b-a^2\), \(r=c-3ab+2a^3\), and \(w=f-4ac+6a^2b-3a^4-3v^2\). The first four cumulants of \(S\) conditional on the signs are
\[
\kappa_1=ah,\qquad\kappa_2=nv,\qquad\kappa_3=hr,\qquad\kappa_4=nw.
\]
The fourth-moment expansion, valid without a normality assumption, gives
\[
\operatorname{Var}(S^2\mid\varepsilon)
=4a^2h^2nv+4ah^2r+2n^2v^2+nw.
\]
Independence of the magnitudes and enumeration of intersecting indices give
\[
\operatorname{Var}(T)=n(f-b^2),\qquad
\operatorname{Cov}(T,S^2\mid\varepsilon)
=n(f-b^2)+2(h^2-n)a(c-ab).
\]
Substitution in \(\operatorname{Var}(T-S^2/n\mid\varepsilon)\) shows that its coefficient of \(h^2\) is \(-B\). To determine the constant, note that the unconditional i.i.d. zero-mean fourth-moment identity gives
\[
\operatorname{Var}(Q)=\frac{n-1}{n}\bigl((n-1)f-(n-3)b^2\bigr)=V.
\]
Since \(h\) is a sum of \(n\) independent fair signs, \(\mathbb Eh^2=n\) and \(\operatorname{Var}(h^2)=2n(n-1)\). The conditional mean therefore has variance \(A=2a^4(n-1)/n\). The law of total variance forces the conditional variance intercept to equal \(V-A+Bn\), proving the second boxed identity.

For \(Y>0\) that is not almost surely constant,
\[
\operatorname{Cov}(Y^2,Y)
=\tfrac12\mathbb E[(Y-Y')^2(Y+Y')]>0,
\]
where \(Y'\) is independent of \(Y\), and \(\mathbb E[Y(Y-a)^2]\ge0\). Hence \(B>0\). If the magnitude is constant, both terms in \(B\) vanish. The conditional mean is an even affine function of \(h^2\), so its covariance with \(K\) vanishes by the symmetry \(K\overset d= n-K\). The variance fraction follows by dividing \(A\) by \(V\); the remaining covariance and correlation follow from the same regression and \(\operatorname{Var}(h^2)=2n(n-1)\). Gaussian and asymptotic specializations are obtained by substituting the corresponding moments.

## Verification

Run \(\texttt{python3 checker.py}\) using the Python standard library. The program exhaustively enumerates finite symmetric samples with magnitude laws supported on one, two, or three positive values, using exact rational probabilities; it compares each conditional first and second moment, the unconditional moments, and the explained-variance formula with the theorem. It reports 516 exact rational assertions, including samples up to eight observations for the two-magnitude case and up to five for the three-magnitude case. These finite checks are corroboration only: the proof above establishes the all-sample-size claim.

## Relationship to prior work

Dixon and Mood's sign test establishes the classical use of counts of positive and negative observations. Ekström and Jammalamadaka study a different spacing-based symmetry test and its asymptotic variance; their author-hosted full text (including results and appendix) does not give the finite conditional scatter moments here. Standard half-normal moment tables supply the Gaussian specialization but do not describe sign-count-conditioned scatter. The present statement isolates a distribution-uniform monotonicity in both conditional mean and conditional variance and an exact nonlinear explained-variance ratio, rather than merely an unconditional sample-variance formula.

## Limitations

The theorem concerns independent identically distributed observations symmetric about a known zero. The number of positive observations about an estimated center, distributions with positive mass at zero, or asymmetric distributions are outside scope. The strict conditional variance ordering requires a nonconstant magnitude distribution, and all conditional variance formulas require the fourth moment. No stochastic ordering of full conditional distributions or optimality of a statistical test is claimed. General quadratic-form moment methods may implicitly contain equivalent consequences; a complete historical priority determination is not claimed.

## References

1. W. J. Dixon and A. M. Mood, *The Statistical Sign Test*, Journal of the American Statistical Association 41 (1946), 557–566, https://doi.org/10.1080/01621459.1946.10501898. Bibliographic month December 1946; exact first day not asserted.
2. M. Ekström and S. R. Jammalamadaka, *An asymptotically distribution-free test of symmetry*, Journal of Statistical Planning and Inference 137 (2007), 799–810, https://doi.org/10.1016/j.jspi.2006.06.009. First verified public online date 18 July 2006; author-hosted manuscript https://jammalam.faculty.pstat.ucsb.edu/html/research%20publication_files/symmetry.pdf.
3. R. H. Byers, *Half-Normal Distribution*, Wiley StatsRef, first published 29 September 2014, https://doi.org/10.1002/9781118445112.stat05864.
4. NIST/SEMATECH, *Sign Test*, https://www.itl.nist.gov/div898/software/dataplot/refman1/auxillar/signtest.htm.
5. E. W. Weisstein, *Half-Normal Distribution*, MathWorld, https://mathworld.wolfram.com/Half-NormalDistribution.html.
