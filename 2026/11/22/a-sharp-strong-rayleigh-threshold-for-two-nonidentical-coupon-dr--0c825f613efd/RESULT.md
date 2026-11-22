# A sharp strong-Rayleigh threshold for two nonidentical coupon draws

## Finding
Take two independent draws from three labeled coupon types. For a parameter \(t>0\), let the first draw have probabilities \((t,t,1)/(2t+1)\) and the second have probabilities \((1,t,t)/(2t+1)\). Let \(I_i\) indicate whether coupon type \(i\) appears in at least one draw, and let \(\mu_t\) be the distribution of \((I_1,I_2,I_3)\).

**Theorem.** The occupancy law \(\mu_t\) is strongly Rayleigh if and only if
\[
0<t\leq 2+\sqrt 7.
\]
For every \(t>2+\sqrt 7\), the occupancy indicators remain strictly pairwise negatively correlated, and their sum is distributed as one plus a Bernoulli variable, although the full occupancy law is not strongly Rayleigh. In the class of independent categorical draws with probability vectors permitted to change between rounds, failure of the strongly Rayleigh property requires at least three types and at least two draws; hence this example has the smallest possible numbers of types and draws.

The threshold is exact, includes the equality case, and holds for the complete three-coordinate distribution, not only for its cardinality marginal.

## Assumptions and scope
The two draws are independent and take exactly one coupon type apiece. Both categorical distributions have strictly positive masses for \(t>0\). No deletion, replacement of an already seen coupon, conditioning, or limiting process is involved. The occupancy-generating polynomial is
\[
P_t(x,y,z)=\mathbb E[x^{I_1}y^{I_2}z^{I_3}].
\]
A probability law on \(\{0,1\}^3\) is *strongly Rayleigh* when its multiaffine probability-generating polynomial is real stable (nonzero whenever every argument has strictly positive imaginary part). The standard real-multiaffine stability criterion states that this is equivalent to nonnegativity, at every point of \(\mathbb R^3\), of all three Rayleigh differences \(\partial_iP\,\partial_jP-P\,\partial_{ij}P\). We use this established characterization [2,3].

## Proof
Write \(Z=(2t+1)^2\) and \(f=ZP_t\). Enumerating the nine ordered pairs of draw outcomes and using a single factor for any coupon seen twice gives exactly
\[
\begin{split}
f(x,y,z)={}&tx+t^2y+tz+(t^2+t)xy\\
&+(t^2+1)xz+(t^2+t)yz.
\end{split}
\]
The six coefficients are nonnegative and sum to \(Z\). Because scaling by a positive constant preserves both real stability and the sign of every Rayleigh difference, we work with \(f\).

Define \(R_{ij}=\partial_i f\,\partial_j f-f\,\partial_{ij}f\). Direct expansion yields
\[
\begin{split}
R_{xy}(z)&=t\left[(t^3+t^2+t+1)z^2+(t^3+t)z+t^2\right],\\
R_{yz}(x)&=t\left[(t^3+t^2+t+1)x^2+(t^3+t)x+t^2\right],\\
R_{xz}(y)&=t^2\left[(t+1)^2y^2+(-t^2+2t+1)y+1\right].
\end{split}
\]
For each quadratic, its leading coefficient is strictly positive when \(t>0\), and its ordinary discriminant (including the displayed outer factor) is
\[
\Delta(t)=t^4(t^2+1)(t^2-4t-3).
\]
A real quadratic with positive leading coefficient is nonnegative for **every real input** if and only if its discriminant is nonpositive. Thus all Rayleigh differences are nonnegative at every real point exactly when \(t^2-4t-3\leq0\), namely \(0<t\leq2+\sqrt7\). The cited multiaffine stability criterion proves the claimed if-and-only-if statement, including the double-root transition.

For a concrete negative witness beyond the boundary, take \(t=5\) and \(y=7/36\). Then the unnormalized Rayleigh difference satisfies
\[
R_{xz}(7/36)=-325/36<0,
\]
so the complete generating polynomial is not real stable. For every \(t>2+\sqrt7\), the strictly positive discriminant similarly produces a real point with a negative Rayleigh difference. This proves failure throughout that interval, without appealing to floating-point root computation.

For any pair of distinct types \(i,j\), let \(a_i,b_i\) be their probabilities in the respective two draws. The indicators of their *absence* obey
\[
\begin{split}
\Pr(i,j\text{ absent})&=(1-a_i-a_j)(1-b_i-b_j),\\
\Pr(i\text{ absent})\Pr(j\text{ absent})
&=(1-a_i)(1-a_j)(1-b_i)(1-b_j).
\end{split}
\]
The first expression is strictly smaller than the second because all the coupon masses are positive. Complementing the two indicators leaves their covariance unchanged, so \(\operatorname{Cov}(I_i,I_j)<0\) for every pair, including above the strong-Rayleigh threshold. Meanwhile, \(K=I_1+I_2+I_3\) equals one when the draws agree and two otherwise. Hence
\[
K\stackrel{d}=1+\operatorname{Bernoulli}\!\left(1-\frac{t^2+2t}{(2t+1)^2}\right).
\]
Its univariate probability-generating polynomial is therefore real-rooted for every \(t>0\), even when the multivariate one is not stable.

For minimality, with a single categorical draw from any number of types, the occupancy polynomial is a positive linear form and hence stable. For at most two types and any positive number of independent categorical draws, the nonempty occupancy set is one of \(\{1\},\{2\},\{1,2\}\). Its generating polynomial is \(Ax+By+Cxy\) for nonnegative \(A,B,C\), and its only Rayleigh difference is \(AB\geq0\) at every real argument. The criterion again gives stability. Zero rounds produces the deterministic empty set, which is also stable. Thus both the type count three and draw count two are individually minimal for failure.

## Verification
The standalone `verify.py` uses SymPy with exact symbolic and rational arithmetic. It independently enumerates all nine ordered draw outcomes, verifies the generating polynomial and its normalization, expands the three Rayleigh differences, factors all three discriminants, tests an exact rational negative witness, checks the equality boundary, and tests pairwise covariance and the two-point occupancy-count generating function across eight rational parameter values. Execute with `python verify.py` in a Python 3 environment with SymPy installed. The recorded run passed 50 assertions; the universal result follows from the algebraic proof rather than from finite diagnostic cases.

## Relationship to prior work
Berend and Sher [1] study **uniform** group coupon draws and their asymptotics, providing a motivating occupancy framework, not the present time-varying weighted two-round law. Borcea, Brändén and Liggett [2] introduce strongly Rayleigh measures and establish the stability framework; their general characterization (also presented explicitly in [3]) is used here, not claimed as new. The published finding [4] proves strong Rayleigh for independent **uniform** coupon packets of varying sizes; its proof explicitly assumes permutation invariance within each packet and does not imply stability for different nonuniform probability vectors in successive rounds. The present result identifies the exact failure boundary for a natural three-type, two-draw weighted deformation, together with the strict separation between pairwise negative dependence and multivariate stability. An unidentified earlier computation of an equivalent polynomial could affect priority; no claim of global bibliographic uniqueness is made.

## Limitations
This is an exact classification of the specified one-parameter, three-type, two-draw model, not a classification of all nonuniform coupon sampling schemes or of arbitrary numbers of rounds. It does not refute negative association in general, only strong Rayleigh stability for the indicated parameter range; the pairwise covariances here remain negative. The total occupancy count has only two possible values and therefore retains a trivial Poisson-binomial form. The proof depends on the established multiaffine real-stability/Rayleigh-difference equivalence. Priority and broader relevance remain subject to independent literature assessment.

## References
1. D. Berend and T. Sher, *Asymptotic Results for Uniform Group Drawing in the Coupon Collector's Problem*, arXiv:2605.06953, first posted 2026-05-07, https://arxiv.org/abs/2605.06953.
2. J. Borcea, P. Brändén and T. M. Liggett, *Negative dependence and the geometry of polynomials*, arXiv:0707.2340; *J. Amer. Math. Soc.* 22 (2009), 521–567, https://arxiv.org/abs/0707.2340.
3. N. Anari, *Geometry of Polynomials*, Lecture 3, Berkeley Math 270 (2015), Theorem 3.2 and Definition 3.1, https://math.berkeley.edu/~nikhil/courses/270/lec3.pdf.
4. *Poisson-binomial vacancy law for heterogeneous group coupon drawings*, public mathematical record (2026-10-13), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-poisson-binomial-vacancy-law-for-heterogeneous-group-coupon-draw--6614ecd26c48.
