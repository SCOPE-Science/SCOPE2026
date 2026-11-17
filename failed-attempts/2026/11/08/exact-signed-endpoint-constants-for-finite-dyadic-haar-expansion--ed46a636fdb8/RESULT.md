# Exact signed endpoint constants for finite dyadic Haar expansions

## Finding
For every integer \(d\geq0\), let \(\mathcal H_d\) be the constant function and all real \(L^2[0,1]\)-normalized dyadic Haar functions on intervals of levels \(0,\ldots,d-1\). For signs \(\varepsilon_0,\varepsilon_I\in\{-1,1\}\), let \(T_\varepsilon\) change those Haar coefficients by their corresponding signs and annihilate the orthogonal complement of their span. The sharp *signed* endpoint constant is
\[
U_d:=\max_\varepsilon\|T_\varepsilon\|_{L^\infty[0,1]\to L^\infty[0,1]}
=\frac{2d}{3}+\frac59+\frac49\left(-\frac12\right)^d.
\]
This is also the exact signed unconditionality constant of the \(2^d\)-dimensional space of functions constant on level-\(d\) dyadic cells. In particular, \(U_d=\frac23d+\frac59+O(2^{-d})\), with the displayed finite-depth parity correction exact. Every maximal row is obtained by the explicit sign-selection rule in the proof, and the corresponding sign of its kernel is a norming input.

## Assumptions and scope
Work over real functions with Lebesgue measure on \([0,1]\). All dyadic cells are half-open except for an immaterial endpoint. For \(I\) of length \(2^{-j}\), put \(h_I=|I|^{-1/2}(\mathbf1_{I_L}-\mathbf1_{I_R})\). Define
\[
T_\varepsilon f=\varepsilon_0\int_0^1 f(y)\,dy+
\sum_{j=0}^{d-1}\sum_{|I|=2^{-j}}\varepsilon_I
\left(\int_0^1f(y)h_I(y)\,dy\right)h_I.
\]
The endpoint norm is the essential-supremum operator norm; the maximum is over all \(2^{2^d}\) sign assignments to the constant term and the \(2^d-1\) Haar coefficients. The equality statement includes \(d=0\), for which \(T_\varepsilon\) is signed averaging and \(U_0=1\). The signed constant is not identified with a coefficient-suppression constant using \(0/1\) multipliers.

## Proof
**1. Reduction to one dyadic path.** The sign of the constant coefficient can be fixed to \(+1\), since simultaneous reversal of every sign replaces the operator by its negative without changing the norm. For fixed terminal dyadic cell \(x\), denote by \(\sigma_j\) the multiplier on its unique ancestor at level \(j\). The integral kernel is
\[
K_\varepsilon(x,y)=1+\sum_{j=0}^{d-1}\sum_{|I|=2^{-j}}\varepsilon_Ih_I(x)h_I(y).
\]
If \(y\) first separates from \(x\) at level \(j\), every earlier ancestor contributes \(+\sigma_k2^k\), the level-\(j\) ancestor contributes \(-\sigma_j2^j\), and all later contributions vanish. Writing \(\alpha_j=1+\sum_{k<j}\sigma_k2^k\), the kernel is \(\alpha_j-\sigma_j2^j\) on a set of measure \(2^{-j-1}\). It equals \(\alpha_d\) on the terminal cell, of measure \(2^{-d}\). Therefore the exact \(L^1\) row norm is
\[
R_d(\sigma)=\sum_{j=0}^{d-1}2^{-j-1}|\alpha_j-\sigma_j2^j|
+2^{-d}|\alpha_d|.
\]
Signs outside the ancestor path do not enter this row. All rows are symmetrically available, and a norm-one step function with signs equal to those of the row kernel attains its row sum. Hence \(U_d=\max_\sigma R_d(\sigma)\), with no comparison loss.

**2. Dynamic programming.** Set \(b_j=2^{-j}\alpha_j\). Then \(b_0=1\), \(b_{j+1}=(b_j+\sigma_j)/2\), and \(-1\le b_j\le1\). Consequently,
\[
R_d(\sigma)=\sum_{j=0}^{d-1}\frac{1-\sigma_jb_j}{2}+|b_d|.
\]
For \(b\in[-1,1]\) and \(h\ge0\), define the maximum over \(h\) future signs by
\[
F_0(b)=|b|,\qquad
F_h(b)=\max_{\sigma=\pm1}\left\{\frac{1-\sigma b}{2}+
F_{h-1}\left(\frac{b+\sigma}{2}\right)\right\}.
\]
Inductively \(F_h(b)=a_h+c_h|b|\). The initial values are \(a_0=0,c_0=1\). Since \(|b+\sigma|=1+\sigma b\), if \(0\le c_{h-1}\le1\) then the two terms in the maximum are
\[
a_{h-1}+\frac{1+c_{h-1}}2+
\sigma b\frac{c_{h-1}-1}2.
\]
Thus
\[
a_h=a_{h-1}+\frac{1+c_{h-1}}2,
\qquad c_h=\frac{1-c_{h-1}}2.
\]
These recurrences preserve \(0\le c_h\le1\), so the induction is valid for every \(h\). Their solutions are
\[
c_h=\frac13+\frac23\left(-\frac12\right)^h,
\qquad
a_h=\frac{2h}{3}+\frac29\left(1-\left(-\frac12\right)^h\right).
\]
Taking \(b=1\) gives \(U_d=F_d(1)=\frac{2d}{3}+\frac59+\frac49(-\frac12)^d\), proving the claimed sharp identity for every \(d\ge0\).

**3. Complete sign-path rule and norming inputs.** For every state \(b\ne0\), the maximizing sign is \(-\operatorname{sgn}(b)\) whenever at least two stages remain; at one stage the two signs tie because \(c_0=1\). For \(d\ge2\), this forces \(\sigma_0=-1\), hence \(b_1=0\), where either sign is admissible. From the second nonzero state onward, the choice alternates against the current state's sign until the final stage, where either sign is admissible. For \(d=1\), either root sign is optimal; for \(d=0\), the signed averaging operator attains norm one. Any multipliers off the chosen ancestor chain are free. Conversely these are exactly the maximizing decisions in the recurrence. For any such transform and target cell, the step function equal to \(\operatorname{sgn}K_\varepsilon(x,\cdot)\) where the row kernel is nonzero (arbitrary of modulus at most one on its zero set) realizes the norm. Any norming input for a fixed transform must align with at least one maximal row in this way, by equality in the integral triangle inequality.

## Verification
The standalone `verify.py` checks the formula by exhaustive sign-path enumeration for all depths \(0\le d\le12\), using exact rational arithmetic (8,191 paths); separately builds 2,016 full row kernels for depth \(1\le d\le6\) with randomly sampled independent signs at every Haar node, comparing their exact \(\ell^1\) sums with the path reduction; and checks 170 Bellman-value identities by exhaustive controls on a rational grid. It is executable with Python 3 standard-library modules and no external data. These are finite consistency tests, not substitutes for the general induction just proved.

## Relationship to prior work
Classical Haar-unconditionality results and martingale-transform inequalities establish uniform \(L^p\) bounds for \(1<p<\infty\), but not a bounded unconditional basis on the full \(L^\infty\) space. Osękowski (2013) proves sharp restricted weak-type bounds for Haar projections and martingale transforms with a different norm and quantification. Osękowski (2016) obtains sharp weak-type \(L^1\) inequalities. Astashkin, Huang, Pliev, Sukochev and Zanin (2022) obtain optimal *infinite-horizon* rearrangement estimates and symmetric-space ranges for selected Haar martingale transforms. None of these inspected statements yields the exact finite-depth signed \(L^\infty\)-to-\(L^\infty\) maximum, its oscillatory correction, or its full optimizing-path rule. Their qualitative conclusions and Bellman-function perspective are antecedents, not claimed as novel. Choi (1992) concerns the sharp \(L^p\) unconditional constants for finite \(p\), not fixed-depth \(L^\infty\) constants.

## Limitations
This result is for balanced dyadic splits, real Haar coefficient signs, and the complete first \(d\) generations. It does not give exact constants for \(0/1\) suppression multipliers, incomplete dyadic subtrees, nonbinary filtrations, nonuniform branch probabilities, or nontrivial weighted measures. Possible implicit or unindexed priority coverage of this exact elementary Bellman recurrence cannot be ruled out by literature searches alone. No independently conducted mathematical review is claimed.

## References
- A. Osękowski, *Sharp Inequalities for the Haar System and Fourier Multipliers*, Journal of Function Spaces and Applications, article 646012 (2013), DOI: 10.1155/2013/646012 (first published 2013-12-05).
- A. Osękowski, *Sharp inequalities for the Haar system and martingale transforms*, Probability and Mathematical Statistics 36 (2016), 147–164, https://www.math.uni.wroc.pl/~pms/files/36.1/Article/36.1.11.pdf.
- S. Astashkin, J. Huang, M. Pliev, F. Sukochev, D. Zanin, *Optimal range of Haar martingale transforms and its applications*, arXiv:2202.07154 (2022), https://arxiv.org/html/2202.07154v1.
- K. P. Choi, *A sharp inequality for martingale transforms and the unconditional basis constant of a monotone basis in \(L^p(0,1)\)*, Transactions of the American Mathematical Society 330 (1992), 509–529, DOI: 10.2307/2153920.
