# A sharp sparse Fourier-notch gap on the circle

## Finding

Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\). Every nonzero finite positive Borel measure \(\mu\) on \(\mathbb T\) with \(\widehat\mu(1)=\widehat\mu(2)=\widehat\mu(6)=0\) has every open support-free circular arc of length at most
\[
G_*=2\pi-2\arccos\!\left(\frac{2\sqrt5-3\sqrt{30}}{20}\right)
=1.859643058424608\ldots.
\]
The bound is attained, and the attaining measures are, up to positive scaling and rotation, **exactly one six-atom measure** described below. Thus the sharp largest empty arc is strictly shorter than the \(2\pi/3\) bound from the first two vanishing Fourier moments alone.

Put
\[
S=\frac{3\sqrt{30}}{20},\quad h=\frac{\sqrt5}{10},\quad
R=\frac{\sqrt{14}}4,\qquad
c=-S+h,\quad b=\frac{S-R}{2},\quad d=\frac{S+R}{2}.
\]
These satisfy \(-1<c<b<0<d<1\). For the ordered nodes \((x_0,x_1,x_2)=(c,b,d)\), define
\[
w_i=\frac{1/2+x_jx_k}{(x_i-x_j)(x_i-x_k)},
\quad\{i,j,k\}=\{0,1,2\}.
\]
All \(w_i\) are strictly positive and sum to one. Writing \(\theta_i=\arccos x_i\), the unique normalized equality measure (in the rotation putting its largest gap around angle \(\pi\)) is
\[
\mu_* = \frac12\sum_{i=0}^2w_i(\delta_{\theta_i}+\delta_{-\theta_i}).
\]
Its six sites are distinct. Every equality measure is a positive scalar multiple of a rotation of \(\mu_*\).

## Assumptions and scope

The Fourier–Stieltjes transform is \(\widehat\mu(k)=\int_{\mathbb T}e^{-ik\theta}\,d\mu(\theta)\); all three specified moments must vanish as complex numbers. Measures need not be discrete or symmetric. An empty arc is an open connected circular arc disjoint from the **closed support** of \(\mu\). Its length is in radians in \((0,2\pi)\). Other Fourier coefficients are unrestricted. Primary mathematical classification: MSC2020 42A05.

The chosen gap pattern is motivated rather than arbitrary: after vanishing at frequencies \(1\) and \(2\), the regular three-point rule gives the sharp gap \(2\pi/3\) and also annihilates the extra frequencies \(4\) and \(5\). Frequency \(6\) is the first *nonconsecutive* added harmonic that does not vanish on this equilateral rule, so this is the first sparse one-notch test of whether the sharp gap genuinely decreases.

## Proof

**1. Exact dual polynomial.** Let \(T_m\) denote the Chebyshev polynomial \(T_m(\cos\theta)=\cos(m\theta)\), and define
\[
P(x)=\left(x^2-Sx-\frac1{20}\right)^2
      \left(x^2+2Sx+\frac58\right).
\]
An exact expansion gives
\[
P(x)=\frac1{32}T_6(x)-\frac{21}{640}T_2(x)
       +\frac{81\sqrt{30}}{8000}T_1(x).
\tag{1}
\]
The quadratic factor \(x^2-Sx-1/20\) has roots \(b,d\), while \(x^2+2Sx+5/8\) has roots \(c=-S+h\) and \(e=-S-h<-1\). Direct radical inequalities give \(-1<c<b<0<d<1\). Consequently
\[
P(x)=(x-c)(x-e)(x-b)^2(x-d)^2\ge0
\quad(c\le x\le1),
\tag{2}
\]
with zeros within \([c,1]\) exactly \(c,b,d\). For every probability measure satisfying the prescribed Fourier zeros, the real cosine moments at \(1,2,6\) vanish, so (1) yields \(\int P(\cos\theta)\,d\mu=0\).

**2. Universal sharp gap bound.** If an empty open arc had length greater than \(G_*\), rotate so that the closed support lies in \([-\alpha,\alpha]\) with \(\alpha<\arccos c\). Then \(\cos\theta>c\) on the support. Since (2) is nonnegative and has integral zero, the cosine pushforward of \(\mu\) would be supported on \(\{b,d\}\). But the first and second Fourier zeros impose
\[
\mathbb E x=0,\quad\mathbb E x^2=\frac12,
\qquad x=\cos\theta.
\]
For any probability distribution on \(\{b,d\}\) having mean zero, \(\mathbb E x^2=-bd=1/20\), a contradiction. Thus no empty arc is longer than \(G_*\).

**3. The positive equality rule.** At the boundary \(\alpha=\arccos c\), (2) forces the cosine pushforward onto \(\{c,b,d\}\). Solving the three independent equations \(\mathbb E1=1\), \(\mathbb Ex=0\), \(\mathbb E x^2=1/2\) by Lagrange interpolation gives precisely the displayed \(w_i\). They are positive: \(bd=-1/20\); \(c<b<0<d\); \(cd<-1/2\), as follows for example from \(c<-59/100\) and \(d>7/8\). The signs of each Lagrange denominator establish positivity. Exact identities give
\[
\sum_iw_i=1,\quad\sum_iw_ix_i=0,\quad
\sum_iw_ix_i^2=\frac12.
\]
All three nodes are zeros of \(P\), so using (1) shows \(\sum_iw_i T_6(x_i)=0\). The symmetric lift \(\mu_*\) therefore has zero *complex* Fourier coefficients at \(1,2,6\). Its two extreme sites \(\pm\arccos c\) have positive masses, leaving an open complementary arc of length exactly \(G_*\).

**4. Rigidity even without assumed symmetry.** Any equality measure supported in the boundary arc has cosine pushforward weights \(w_i\) as above. Its masses at the two sites \(\pm\theta_i\) may at first differ; let the differences be \(\Delta_i\). The imaginary vanishing moments imply
\[
\sum_i\Delta_i\sin(k\theta_i)=0,\qquad k\in\{1,2,6\}.
\]
Put \(U_5(x)=\sin(6\arccos x)/\sqrt{1-x^2}=32x^5-32x^3+6x\). Factoring \(\sin\theta_i\) from the three columns, the determinant of this sine system, up to the nonzero factor \(2\prod_i\sin\theta_i\prod_{i<j}(x_j-x_i)\), equals the second divided difference
\[
U_5[c,b,d]=\frac85(9h-S)>0.
\]
This identity is exact (expand the degree-five polynomial and use the three elementary symmetric functions of \(c,b,d\)). Thus \(\Delta_i=0\) for all \(i\), and the equality measure must be \(\mu_*\). Undoing normalization and rotation proves the classification.

## Verification

The accompanying `CHECK.py` (Python and SymPy) checks (1) and the complete factorization symbolically, the strict radical ordering, positivity of the weights, the first/second/sixth exact moments, and the nonzero sine determinant via the divided-difference identity. Run `python CHECK.py` after installing the version specified in `requirements.txt`. Its exact symbolic tests independently check the finite algebraic certificate; the universal quantifier over positive Borel measures follows from the written integral argument, not from a finite numerical sample.

## Relationship to prior work

Tan and Zhang (2026), Section 2, prove a sharp gap bound and equality classification from **consecutive** Fourier zeros \(1,\ldots,r-1\). At \(r=3\), their bound is \(2\pi/3\), whose equality rule has a nonzero sixth Fourier moment, so it neither proves nor contradicts the strictly smaller gap here. Their \(r=7\) result assumes the extra missing zeros \(3,4,5\), hence cannot be applied to the present sparse hypothesis. Kunis (2026), Section 3, studies covering-radius bounds for positive quadratures exact over complete frequency bands (and higher-dimensional variants), not the exact sparse \(\{1,2,6\}\) threshold or uniqueness. Peherstorfer (2010) characterizes positive trigonometric quadrature exact through a consecutive degree via orthogonal polynomials on the unit circle; this does not imply an exact gap constant for the present nonconsecutive moment set. The methods are classical duality and moment interpolation, but the explicit sparse constant and its rigid six-atom equality case were not found in the inspected sources.

## Limitations

The result fixes exactly the required *vanishing constraints* at frequencies \(1,2,6\); it does not give a formula for arbitrary sparse sets, noisy approximate moment zeros, or a stability modulus near equality. It does not require other moments to be nonzero. No independent external validation or priority certification is claimed. Earlier sparse-moment or nonnegative-trigonometric-polynomial results could contain an equivalent formulation; some older broad-titled papers were only available through metadata and remain residual priority risks.

## References

- Hu Tan and Ying Zhang, *Sharp Diameter Bounds for Nonnegative Cyclotomic Multiples*, arXiv:2609.07646, v1 September 7, 2026, especially Section 2. https://arxiv.org/abs/2609.07646
- Stefan Kunis, *Positive quadrature and mobile sampling of multivariate trigonometric polynomials*, arXiv:2608.11915, v1 August 12, 2026, especially Section 3. https://arxiv.org/abs/2608.11915
- Franz Peherstorfer, *Positive trigonometric Quadrature Formulas and quadrature on the unit circle*, arXiv:1001.2451, January 14, 2010. https://arxiv.org/abs/1001.2451
- A. D. Gilbert and C. J. Smyth, *Zero-Mean Cosine Polynomials which are Non-Negative for as Long as Possible*, J. London Math. Soc. 62 (2000), 489–504, doi:10.1112/S0024610700001216 (abstract inspected).
- M. Goldstein and J. N. McDonald, *An Extremal Problem for Non-Negative Trigonometric Polynomials*, J. London Math. Soc. 29 (1984), 81–88, doi:10.1112/jlms/s2-29.1.81 (metadata only; full text unavailable during review).
