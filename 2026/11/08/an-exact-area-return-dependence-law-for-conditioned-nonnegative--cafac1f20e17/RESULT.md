# An exact area–return dependence law for conditioned nonnegative random walks

## Finding
Let \(S_0=0,S_1,\ldots,S_{2n}=0\) be a simple symmetric \(\pm1\) walk conditioned to stay nonnegative, with \(n\ge1\). Define its integrated height and positive-time zero-return count by
\[
 A_n=\sum_{t=0}^{2n-1}S_t,\qquad R_n=\#\{1\le t\le 2n:S_t=0\}.
\]
The final return is counted. Write \(C_n=\binom{2n}{n}/(n+1)\) and \(Q_n=4^n/C_n\). The exact finite-size covariance is
\[
 \operatorname{Cov}(A_n,R_n)=\frac{6Q_n-4n^2-14n-6}{n+2}.
\]
It is zero at \(n=1\), strictly negative for every integer \(n\ge2\), and
\[
 \operatorname{Cov}(A_n,R_n)=-4n+6\sqrt{\pi n}+O(1)\quad(n\to\infty).
\]
The dependence also has an exact conditional witness: for every \(n\ge2\),
\[
 \mathbb E[A_n\mid R_n=1]-\mathbb E[A_n\mid R_n=2]=n.
\]
Thus a single-return path has exactly \(n\) more expected integrated height than a two-return path of the same length, despite the nontrivial distributions of the individual excursion lengths.

## Assumptions and scope
All paths of \(2n\) steps with increments \(+1\) and \(-1\), starting and ending at zero without entering the negative integers, are equiprobable. This is the law of a symmetric Bernoulli walk conditioned on the stated finite event; there are \(C_n\) paths. The area \(A_n\) is the discrete integral of heights **before** each step, not the conventional square-cell Dyck-area statistic. On a path of semilength \(n\), this differs from twice that conventional statistic by the deterministic constant \(n\); consequently covariance with \(R_n\) is scaled accordingly. Conditional events \(R_n=1\) and \(R_n=2\) both have positive probability exactly when \(n\ge2\).

## Proof
Set \(C(z,q)=\sum_Pz^{|P|}q^{A(P)}\), where the sum includes the empty nonnegative bridge and \(|P|\) is semilength. Set \(F(z,q)\) for the subfamily of primitive excursions (exactly one positive-time return). A primitive path is uniquely \(UPD\), where \(P\) is any nonnegative bridge. Since \(A(UPD)=A(P)+2|P|+1\),
\[
 F(z,q)=zqC(zq^2,q),\qquad C(z,q)=\frac1{1-F(z,q)}.
\]
The trivariate generating function recording the number of primitive components is therefore
\[
 G(z,u,q)=\frac1{1-uF(z,q)}
 =\sum_P z^{|P|}u^{R(P)}q^{A(P)}.
\]
Here all identities are formal power-series identities and all derivatives below are coefficientwise. At \(q=1\), put \(C(z)=C(z,1)\), \(F(z)=zC(z)\) and \(s=\sqrt{1-4z}\). The Catalan identity gives \(C(z)=2/(1+s)\) and \(C(z)=1+zC(z)^2\). Differentiating the two equations in \(q\), with a subscript indicating evaluation at \(q=1\), gives
\[
 F_q=z\big(C+2zC'+C_q\big),\qquad C_q=C^2F_q.
\]
As \(1-zC^2=sC\) and \(C+2zC'=C/s\), this solves to
\[
 F_q=\frac z{1-4z},\qquad
 C_q=\frac{zC^2}{1-4z}=\frac1{s^2}-\frac2s+C.
\]
Differentiation in \(u\) and \(q\) yields, at \(u=q=1\),
\[
 G_u=zC^3,\qquad
 G_{uq}=C_q(2C-1)=5C+2C^2-\frac{10}s+\frac3{s^2}.
\]
The Catalan and central-binomial coefficient identities
\[
 [z^n]C=C_n,\quad [z^n]C^2=C_{n+1},\quad
 [z^n]s^{-1}=\binom{2n}{n},\quad [z^n]s^{-2}=4^n
\]
now yield, for all \(n\ge1\),
\[
 \mathbb E[A_n]=Q_n-(2n+1),\quad
 \mathbb E[R_n]=\frac{3n}{n+2},\quad
 \mathbb E[A_nR_n]=3Q_n-10n+3-\frac{12}{n+2}.
\]
Taking the covariance gives the advertised rational expression.

For its sign set \(P_n=(2n^2+7n+3)/3\). The central-binomial/Catalan ratio obeys
\[
 Q_1=P_1=4,\qquad Q_{n+1}=\frac{2(n+2)}{2n+1}Q_n,\qquad
 P_{n+1}-\frac{2(n+2)}{2n+1}P_n=\frac n3>0.
\]
Induction proves \(Q_n<P_n\) for every \(n\ge2\). Since \(\operatorname{Cov}(A_n,R_n)=6(Q_n-P_n)/(n+2)\), the sign assertions follow without numerical estimation. Stirling's formula gives \(Q_n=\sqrt{\pi}\,n^{3/2}(1+O(n^{-1}))\), establishing the asymptotic expansion.

For the conditional witness, exactly \(r\) returns correspond to \(r\) primitive components, so their ordinary count and summed area are respectively \([z^n]F^r\) and \([z^n]rF^{r-1}F_q\). In particular,
\[
 \mathbb E[A_n\mid R_n=1]=\frac{4^{n-1}}{C_{n-1}},
\]
whereas, for \(n\ge2\),
\[
 \mathbb E[A_n\mid R_n=2]=
 \frac{2[z^{n-2}]C(z)/(1-4z)}{C_{n-1}}.
\]
The elementary identity \(C/s^2=2/s^2-2/s+C\) gives the coefficient \([z^{n-2}]C/s^2=2\cdot4^{n-2}-2\binom{2n-4}{n-2}+C_{n-2}\). Therefore the difference of the two conditional means equals
\[
 \frac{4\binom{2n-4}{n-2}-2C_{n-2}}{C_{n-1}}
 =\frac{(4n-6)C_{n-2}}{C_{n-1}}=n,
\]
using \(C_{n-1}/C_{n-2}=2(2n-3)/n\). This completes the proof.

## Verification
The accompanying standalone `verify.py` uses only Python's standard library and rational arithmetic. Run `python verify.py` to check exact exhaustive enumeration of all nonnegative bridges through \(n=9\), an independently constructed height/moment dynamic program through \(n=80\), a return-conditioned dynamic program through \(n=50\), and finite exact checks of the sign super-solution. Its tests are finite corroboration; they are not substituted for the generating-function derivation and induction covering every \(n\).

## Relationship to prior work
Classical Bernoulli-excursion area work, including Takács (1991) and the Janson (2007) survey, studies area moments and continuum limits. Denisov, Kolb and Wachtel (2013 preprint; 2015 article) study local limit theorems for area in positive random-walk excursions. Deutsch (1999) enumerates return steps and many other Dyck statistics; Bandlow and Killpatrick (2001) describe the area-refined Catalan recurrence. These give separate marginal inputs and a standard first-return decomposition, but the inspected treatments do not give the present mixed area/return covariance sign law or the exact one-return versus two-return conditional gap. The derivation deliberately uses those classical tools; it is not a claim of a new generating-function method. The relationship is qualified by the possibility of older implicit joint enumerations.

## Limitations
The theorem concerns the uniformly conditioned simple symmetric nearest-neighbor walk; no result is asserted for biased increments, non-nearest-neighbor walks, unconditioned bridges, or arbitrary excursion laws. The local time is the count of returns including the endpoint, and the normalization of the integrated area is fixed above. Independent review and a comprehensive historical-priority determination have not been performed. Earlier general q-Catalan and plane-tree enumerations could imply the identities after further specialization, and not every older reference could be inspected in full.

## References
1. S. Janson, *Brownian excursion area, Wright's constants in graph enumeration, and other Brownian areas*, arXiv:0704.2289, first version April 18, 2007. https://arxiv.org/abs/0704.2289
2. D. Denisov, M. Kolb and V. Wachtel, *Local Asymptotics for the Area of Random Walk Excursions*, Oberwolfach Preprint OWP 2013-19, September 5, 2013. https://doi.org/10.14760/OWP-2013-19
3. E. Deutsch, *Dyck path enumeration*, Discrete Mathematics 204 (1999), 167–202. https://doi.org/10.1016/S0012-365X(98)00371-9
4. J. Bandlow and K. Killpatrick, *An Area-to-Inv Bijection Between Dyck Paths and 312-avoiding Permutations*, Electronic Journal of Combinatorics 8 (2001), R40. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v8i1r40
5. L. Takács, *A Bernoulli Excursion and Its Various Applications*, Advances in Applied Probability 23 (1991), 557–585. https://doi.org/10.2307/1427622
