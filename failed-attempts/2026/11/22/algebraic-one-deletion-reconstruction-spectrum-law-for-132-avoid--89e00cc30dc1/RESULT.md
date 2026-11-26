# Algebraic one-deletion reconstruction-spectrum law for \(132\)-avoiding permutations

## Finding

Let \(\mathcal A_n\) be the set of permutations of \(\{1,\ldots,n\}\) avoiding the classical pattern \(132\). For \(\pi\in\mathcal A_n\), let \(D(\pi)\) be the set of **distinct standardized** permutations obtained by removing exactly one entry. This set, not a positional multiset, models the one-deletion reconstruction sphere. Define the number of *bonds* by
\[
b(\pi)=\#\{i:1\le i<n,\ |\pi_{i+1}-\pi_i|=1\}.
\]
For every \(n\ge1\) and every permutation \(\pi\),
\[
|D(\pi)|=n-b(\pi).
\]
Define the complete finite-length spectrum
\[
A(z,u)=\sum_{n\ge1}\sum_{\pi\in\mathcal A_n}z^nu^{b(\pi)}.
\]
The series \(A(0,u)=0\) is the **unique** solution over \(\mathbb Z[u][[z]]\) of
\[
\boxed{zA^2-\bigl(1-z(1+u)-z^2(u-1)\bigr)A+z\bigl(1+z(u-1)\bigr)=0.}
\]
Consequently the coefficient of \(z^n u^{n-k}\) counts exactly the sources whose one-deletion spheres have size \(k\). For each \(n\ge2\), a uniformly chosen source in \(\mathcal A_n\) has
\[
\boxed{\mathbb E|D(\pi)|=n-\frac{(n+1)(3n-2)}{4(2n-1)}.}
\]
Its full sphere-volume distribution is asymptotically normal:
\[
\boxed{\frac{|D(\pi)|-5n/8}{\sqrt{17n/128}}\ \xrightarrow{d}\ \mathcal N(0,1),\qquad
\operatorname{Var}(|D(\pi)|)=\frac{17}{128}n+O(1).}
\]
The mean is \(5n/8+O(1)\). For \(n=1\), the unique source has one deletion output, the empty permutation; for \(n=0\), one-deletion output is undefined and \(n=0\) is excluded from the spectrum.

## Assumptions and scope

An occurrence of \(132\) is a triple of positions \(i<j<k\) with \(\pi_i<\pi_k<\pi_j\). Standardizing a list of distinct integers means replacing entries with their relative ranks. The reconstruction channel has exactly one deleted position, knows the input length, and reports all distinct standardized one-deletion outputs. Competing source permutations need not avoid \(132\), but the sphere count is a property of the specified source. Throughout the exact formulae, \(n\) ranges over integers \(n\ge1\), and all generating functions are formal at the origin. The asymptotic statement concerns a uniformly sampled \(\pi\in\mathcal A_n\) as \(n\to\infty\).

## Proof

**1. Distinct deletion patterns and bonds.** For any permutation \(\pi\) and adjacent positions \(i,i+1\), deleting the entry at \(i\) or \(i+1\) yields the same standardized permutation precisely when their values differ by one. More generally, if deletions at positions \(i<j\) agree, comparing relative ranks of surviving entries in order forces \(\pi_i,\pi_{i+1},\ldots,\pi_j\) to be a monotone string of consecutive integers, hence each intervening pair is a bond. Conversely all deletions along such a string agree, since replacing any one term leaves the same relative order after ranking. Thus equivalence classes of deletion positions are exactly the connected components of the path on positions with edges at bonds; a path with \(n\) vertices and \(b(\pi)\) present edges has \(n-b(\pi)\) components. This classical deletion-pattern observation is included to fix the channel normalization; its standalone identity is not claimed new.

**2. Catalan decomposition and the bivariate equation.** Every nonempty \(132\)-avoider has a unique decomposition \(\pi=L\,n\,R\), in which all entries of \(L\) are greater than all entries of \(R\), and the standardized nonempty portions are themselves \(132\)-avoiders. Let \(E(z,u)\) count nonempty avoiding permutations ending with their maximum. The bonds entirely inside \(L\) and \(R\) are counted by \(A\). If \(L\) is nonempty, the boundary immediately before \(n\) contributes an additional bond exactly when \(L\) ends with its maximum; if \(L\) is empty, the boundary immediately after \(n\) contributes a bond exactly when \(R\) starts with its maximum. Permutations beginning with their maximum obey the same endpoint recurrence as permutations ending with their maximum: removing that maximum leaves an arbitrary smaller avoiding permutation, and an additional bond appears precisely when the remaining permutation begins (respectively ends) with its maximum. Both endpoint series therefore solve the same formal equation with zero constant term and are equal. Therefore
\[
E=z\bigl(1+A+(u-1)E\bigr),\qquad
A=E+z\bigl(A+(u-1)E\bigr)(1+A).
\]
The first equation gives \(E=z(1+A)/(1-z(u-1))\); substitution into the second, clearing the invertible denominator, gives precisely the boxed quadratic. The coefficient of \(A\) in that equation has constant term \(-1\), so its solution with zero constant term exists and is uniquely determined coefficient by coefficient. Equivalently, letting \(A_0=0\) and \(A_n(u)=[z^n]A(z,u)\),
\[
A_n(u)=\boldsymbol{1}_{n=1}+(1+u)A_{n-1}(u)
+(u-1)\bigl(\boldsymbol{1}_{n=2}+\boldsymbol{1}_{n\ge3}A_{n-2}(u)\bigr)
+\sum_{i=1}^{n-2}A_i(u)A_{n-1-i}(u),
\]
where out-of-range summands vanish and the term involving \(A_{n-2}\) is used only when \(n\ge3\). This recurrence is an exact all-length executable description of every deletion-sphere size.

**3. Mean.** Setting \(u=1\) gives \(A(z,1)=C(z)-1\), where \(C(z)=(1-\sqrt{1-4z})/(2z)\) is the Catalan series. Differentiating the quadratic in \(u\) and using that specialization gives
\[
\partial_u A(z,1)=\frac{1-z}{2\sqrt{1-4z}}-\frac{1+z}{2}.
\]
For \(n\ge2\), taking coefficients yields
\[
\sum_{\pi\in\mathcal A_n}b(\pi)
=\frac12\binom{2n}{n}-\frac12\binom{2n-2}{n-1}.
\]
Division by \(C_n=\binom{2n}{n}/(n+1)\) and \(|D|=n-b\) proves the stated exact mean.

**4. Gaussian asymptotics.** The discriminant of the quadratic is
\[
\Delta(z,u)=\bigl(1-z(1+u)-z^2(u-1)\bigr)^2
-4z^2\bigl(1+z(u-1)\bigr).
\]
At \(u=1\), its unique dominant positive singularity is the simple root \(\rho(1)=1/4\), with \(\partial_z\Delta(1/4,1)=-4\). By the implicit-function theorem, the dominant root \(\rho(u)\) and the nonzero square-root coefficient are analytic in a complex neighborhood of \(u=1\), and there is a uniformly separated next singularity. Uniform algebraic singularity transfer then gives
\[
[z^n]A(z,u)=c(u)n^{-3/2}\rho(u)^{-n}(1+O(n^{-1}))
\]
locally uniformly near \(u=1\), with \(c(1)\ne0\). Differentiating \(\Delta(\rho(u),u)=0\) twice shows
\[
\rho'(1)=-\frac3{32},\qquad \rho''(1)=\frac{49}{512}.
\]
For the moment generating function of \(b\), set \(u=e^t\). The analytic quasi-powers theorem, applied to the last coefficient asymptotic divided by \(C_n\), gives mean growth \(-\rho'(1)/\rho(1)=3/8\) and variance growth
\[
-\frac{\rho''(1)+\rho'(1)}{\rho(1)}+
\left(\frac{\rho'(1)}{\rho(1)}\right)^2=\frac{17}{128}>0.
\]
Thus the centered, scaled bond count is asymptotically standard Gaussian. Since \(|D|=n-b\), negation preserves the Gaussian limit and variance while changing the mean slope from \(3/8\) to \(5/8\). Uniform singular expansion also provides the stated \(O(1)\) variance error.

## Verification

Run `python3 verify.py` with Python 3 and no third-party packages. It derives the spectrum polynomial recurrence independently, enumerates every \(132\)-avoider through length eight, explicitly constructs all distinct standardized deletion outputs, checks \(|D|=n-b\) for each, and compares every coefficient of the recurrence with the enumeration. It also checks the exact means and Catalan totals through length twelve. Example bond-count polynomials begin
\[
A_1(u)=1,\quad A_2(u)=2u,\quad A_3(u)=3u+2u^2,
\quad A_4(u)=5u+7u^2+2u^3.
\]
The program's finite agreement is reproducibility evidence, not a substitute for the formal recurrence proof or the singularity argument. Derivatives of the discriminant are also explicitly recorded in the proof for independent analytic checking.

## Relationship to prior work

Kitaev and Remmel, *The 1-box pattern on pattern avoiding permutations* (first public arXiv:1305.6970, 2013), derive a bivariate distribution on \(132\)-avoiders for the **number of positions touched by at least one bond**. That is a different variable from the number of bond edges used here: the avoiding permutations \(1234\) and \(2134\) both have four positions touched by bonds but have respectively three and two bond edges. Thus the prior one-box enumerator does not, by itself, imply this full deletion-sphere distribution. Its Fibonacci and other pre-existing numerical columns are not claimed as new. In particular the bond-count-two coefficient is associated with a previously catalogued sequence (OEIS A212338); no claim of a new numerical sequence is made. Bevan, Homberger and Tenner, *Prolific permutations and permuted packings* (first public arXiv:1608.06931, 2016), characterize maximally distinct deletion patterns and hence the zero-bond case in the unrestricted setting; that characterization neither enumerates the whole \(132\)-avoiding volume spectrum nor supplies its Gaussian law. Work on marked mesh patterns and big descents of avoiding permutations studies related but different statistics. The contribution here is the constrained-source full spectrum and its asymptotic distribution, not the Catalan decomposition, the bond/deletion identity, or any pre-existing sequence column.

## Limitations

The result covers the classical \(132\)-avoiding class, exactly one deletion, and standardization of each output; it is not a two-read confusability graph, does not correct arbitrary numbers of deletions, and does not determine the largest zero-error code among these sources. The proof establishes a one-variable spectrum of sphere cardinality, not a pairwise intersection distribution or a reconstruction-capacity theorem. The originality assessment is a best-knowledge comparison to inspected literature and searchable records; an unindexed equivalent bond statistic distribution could narrow that assessment. The Gaussian statement is asymptotic as length grows and does not assert exact finite-length normality. Independent mathematical audit has not been performed.

## References

- S. Kitaev and J. Remmel, *The 1-box pattern on pattern avoiding permutations*, first public version 2013-05-29, https://arxiv.org/abs/1305.6970 ; complete journal text https://cs.uwaterloo.ca/journals/JIS/VOL17/Kitaev/kitaev4.pdf .
- D. Bevan, C. Homberger and B. E. Tenner, *Prolific permutations and permuted packings*, first public version 2016-08-24, https://arxiv.org/abs/1608.06931 .
- S. Kitaev, J. Remmel and M. Tiefenbruck, *Quadrant marked mesh patterns in 132-avoiding permutations I*, first public version 2012-01-30, https://arxiv.org/abs/1201.6243 .
- OEIS A212338, https://oeis.org/A212338 , prior numerical column, not claimed as novel.
