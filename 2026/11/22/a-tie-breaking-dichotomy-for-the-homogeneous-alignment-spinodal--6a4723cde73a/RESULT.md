# A tie-breaking dichotomy for the homogeneous alignment spinodal of a seven-site lattice gas

## Finding

Two natural tie-handling conventions for a three-orientation, seven-site, occupancy-diluted majority-update model yield **qualitatively different low-density linear stability**. With uniformly random resolution of every tied plurality, the homogeneous disordered state is linearly stable even at zero noise whenever the occupancy lies below a strictly positive threshold \(\rho_* = 0.212447606903894\ldots\). With incumbent-preserving resolution of ties at zero noise, the same disordered state is linearly unstable at **every** positive occupancy, however small. Both statements are exact for the annealed, homogeneous, independent-neighbor closure specified below; neither claims a phase boundary for the full spatial particle process.

Define the rational polynomials

\[
P(\rho)=\frac{729-1458\rho+10935\rho^2-24300\rho^3+27135\rho^4-14634\rho^5+2923\rho^6}{729},
\]

\[
T(\rho)=\frac{1458\rho-7290\rho^2+17820\rho^3-23490\rho^4+15930\rho^5-4348\rho^6}{729}.
\]

The linear growth rates of either of the two homogeneous polarization modes are, respectively,

\[
\lambda_{\mathrm R}(\rho,\eta)=\left(1-\frac{3\eta}{2}\right)P(\rho)-1,
\qquad
\lambda_{\mathrm I}(\rho,\eta)=\left(1-\frac{3\eta}{2}\right)P(\rho)+(1-\eta)T(\rho)-1.
\]

Here R and I denote random ties and incumbent-preserving ties. The unique root \(\rho_*\in(0,1)\) is specified **exactly** by

\[
2923\rho_*^5-14634\rho_*^4+27135\rho_*^3-24300\rho_*^2+10935\rho_*-1458=0.
\]

For \(\rho>\rho_*\), the random-tie threshold is \(\eta_{\mathrm R}(\rho)=\frac23(1-P(\rho)^{-1})\); for \(0<\rho\leq\rho_*\), there is no positive-noise linear instability. For every \(\rho>0\), the incumbent-tie threshold exists and equals

\[
\eta_{\mathrm I}(\rho)=\frac{P(\rho)+T(\rho)-1}{\frac32P(\rho)+T(\rho)}>0,
\qquad
\eta_{\mathrm I}(\rho)\sim\frac{10}{3}\rho^2\quad(\rho\downarrow0).
\]

The thresholds agree with their stated stability interpretation: a strictly negative growth rate gives linear asymptotic stability in the homogeneous orientation simplex; a strictly positive rate gives instability; equality is marginal and is **not** classified nonlinearly. At complete occupancy the two thresholds are exactly \(601/1995\) and \(681/2075\), respectively.

## Assumptions and scope

Fix \(0<\rho\leq1\), \(0\leq\eta\leq1\), and orientation fractions \(f=(f_1,f_2,f_3)\) in the probability simplex. Sample a central occupied particle with orientation \(C\sim f\), and six independent adjacent sites. Each adjacent site is empty with probability \(1-\rho\), or carries orientation \(i\) with probability \(\rho f_i\). Among the occupied central and adjacent sites, call \(i\) a *unique plurality* if its count strictly exceeds both other counts; otherwise call the event a tie. The central particle reorients independently of displacement as follows:

* On a unique plurality \(i\), choose \(i\) with probability \(1-\eta\) and each other orientation with probability \(\eta/2\).
* Under rule R, any tied plurality chooses each of the three orientations with probability \(1/3\), irrespective of its former orientation and \(\eta\).
* Under rule I, any tied plurality preserves the central orientation with probability \(1-2\eta/3\), and chooses either other orientation with probability \(\eta/3\).

Let \(F_{\mathrm R/I}(f;\rho,\eta)\) be the resulting orientation law. The continuous-time annealed homogeneous dynamics is \(\dot f=F_{\mathrm R/I}(f;\rho,\eta)-f\), with fixed occupancy. The spatial hopping and excluded-volume correlations of the underlying triangular-lattice particle model are **not** part of these dynamics. This is an exact result for two specified annealed closures, not an assertion that their predictions agree with the spatially resolved mean-field equations or Monte Carlo phase diagrams.

The random-tie rule matches the local particle-algorithm prescription in Dias–Dickman–Rosembach (2026, Sec. II). The incumbent-tie rule matches that paper's separate noise-dependent no-majority contribution in its mean-field reorientation equations. The two prescriptions should not be conflated.

## Proof

**1. Symmetric linearization.** At \(f_*=(1/3,1/3,1/3)\), permutation symmetry gives \(F(f_*)=f_*\) under both rules, and the Jacobian of \(\dot f\), restricted to the two-dimensional tangent space \(\sum_i\delta f_i=0\), is scalar. To obtain that scalar, set \(f_1=1/3+\delta\), \(f_2=1/3-\delta\), \(f_3=1/3\), and differentiate the first component of \(F\) at \(\delta=0\).

Given \(k\) occupied neighbors, the \(m=k+1\) orientations (including the central particle) are independent with common law \(f\). At the symmetric point a count vector \((n_1,n_2,n_3)\), with sum \(m\), has probability \(p(n)=\frac{m!}{n_1!n_2!n_3!}3^{-m}\), and the derivative of this probability in the stated direction is \(3(n_1-n_2)p(n)\). Consequently the derivative of the probability that orientation 1 is the unique plurality is

\[
a_m=3\!\sum_{n_1+n_2+n_3=m}\!p(n)(n_1-n_2)\,\mathbf1_{\{n_1>\max(n_2,n_3)\}}.
\]

The derivative of the probability that orientation 1 was held by the central particle **and** that the sample is tied is

\[
b_m=3\!\sum_{n_1+n_2+n_3=m}\!p(n)(n_1-n_2)\frac{n_1}{m}\,
\mathbf1_{\{\text{at least two counts share the maximum}\}}.
\]

Here the factor \(n_1/m\) follows by exchangeability, conditioning on the sample count vector. Direct finite multinomial sums give the complete values for \(1\leq m\leq7\):

| \(m\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|
| \(a_m\) | \(1\) | \(2/3\) | \(4/3\) | \(4/3\) | \(40/27\) | \(140/81\) | \(1330/729\) |
| \(b_m\) | \(0\) | \(1/3\) | \(0\) | \(2/9\) | \(2/27\) | \(10/81\) | \(80/729\) |

With \(k\sim\operatorname{Bin}(6,\rho)\), the binomial mixtures \(\sum_{k=0}^6\binom6k\rho^k(1-\rho)^{6-k}a_{k+1}\) and the corresponding mixture of \(b_{k+1}\) are precisely \(P(\rho)\) and \(T(\rho)\) displayed above. By exchange symmetry the derivative of total tie probability is zero. A unique plurality therefore contributes \((1-3\eta/2)P\) to \(\partial_\delta F_1\); a tie contributes zero under R and \((1-\eta)T\) under I. Subtracting the identity contribution yields the claimed tangent eigenvalues, each of multiplicity two.

**2. Exact random-tie threshold.** Polynomial division gives

\[
P(\rho)-1=\frac{\rho}{729}G(\rho),\quad
G(\rho)=2923\rho^5-14634\rho^4+27135\rho^3-24300\rho^2+10935\rho-1458.
\]

Under the strictly increasing substitution \(s=\rho/(1-\rho)\) for \(0\leq\rho<1\),

\[
(1+s)^5G\left(\frac{s}{1+s}\right)
=-1458+3645s+4860s^2+5265s^3+3186s^4+601s^5.
\]

This is strictly increasing for \(s\geq0\), negative at zero, and positive at large \(s\), hence has exactly one root on \([0,\infty)\). It yields \(\rho_*\in(0,1)\), with \(G(1/5)<0\) and \(G(1/4)>0\). Thus \(P<1\) for \(0<\rho<\rho_*\), and \(P>1\) for \(\rho>\rho_*\). Every \(a_m\) is positive, so \(P>0\); on the physically allowed \(\eta\in[0,1]\), the sign of \(\lambda_{\mathrm R}\) follows by solving the displayed affine equation in \(\eta\). In particular nonzero noise cannot destabilize the low-density state.

**3. Incumbent-tie obstruction disappears.** The exact positive factorization is

\[
P(\rho)+T(\rho)-1=\frac{\rho^2}{243}H(\rho),
\quad H(\rho)=1215-2160\rho+1215\rho^2+432\rho^3-475\rho^4.
\]

For \(0\leq\rho\leq1\),

\[
H(\rho)=1215(\rho-8/9)^2+255+\rho^3(432-475\rho)\geq212>0,
\]

because \(\rho^3(432-475\rho)\geq-43\). Hence \(\lambda_{\mathrm I}(\rho,0)>0\) at every positive occupancy. The denominator \(B=\frac32P+T\) is positive, because both \(P\) and \(T\) are binomial mixtures of nonnegative \(a_m\) and \(b_m\). Moreover \(B-(P+T-1)=1+P/2>0\), so the unique incumbent-tie noise threshold lies strictly between zero and one. Expanding the positive numerator as \(5\rho^2+O(\rho^3)\), and the denominator as \(3/2+O(\rho)\), proves \(\eta_{\mathrm I}\sim(10/3)\rho^2\). Substitution at \(\rho=1\) gives the stated rational endpoints.

## Verification

The standalone file `verify.py` recomputes all fourteen voter-count coefficients by exact multinomial sums; enumerates independently every central state and all \(4^6\) neighbor configurations for five rational densities and three rational noise strengths under **both** rules (thirty exact Jacobian comparisons); checks both rational polynomials, the transformed-root polynomial, the positive incumbent factorization and complete-occupancy thresholds. Run `python3 verify.py` with an ordinary Python 3 installation; it requires no nonstandard packages. The checker returned PASS. These finite arithmetic checks independently corroborate the identities; the arguments above prove the all-parameter sign assertions.

## Relationship to prior work

Dias, Dickman and Rosembach's 2026 seven-site active-lattice-gas study specifies a uniform choice among all three headings on a tied plurality in its *particle algorithm*, while describing an \(\eta\)-dependent incumbent-preserving contribution to its *mean-field equation* (Sec. II, Eqs. (3)–(5)). Those **rules** are the explicit objects compared here. The source numerically investigates spatially structured bands and traffic jams, not this exact, paired homogeneous linear stability classification. Its spatial dynamics and notation are credited, but its numerical phase diagrams cannot be identified with the present local annealed thresholds.

Rosembach, Dias and Dickman (2024) previously studied the 19-site, perception-noise version through Monte Carlo simulation. Kwak, Lee and Kim (2026) study a three-state majority-vote model on a fully occupied cubic lattice. Neither directly supplies the six-neighbor dilution polynomial or the tie-dependent comparison proved here. Related published finite-ring active-exclusion spinodal and deterministic majority-rule fixed-state results concern different generators, dimensions and stability questions, so their conclusions do not imply this dichotomy.

## Limitations

Only the homogeneous **orientation** tangent modes are classified. No spatial Fourier perturbations, density-orientation coupling, excluded-volume dynamics, nonlinear bifurcations, full-lattice stationary distributions, finite-size effects, or metastable coexistence are proved. The two stochastic tie rules must remain distinct: the original 2026 paper does not derive the present two-closure comparison, and its implementation choices may not match either stand-alone homogeneous simplification in every detail. Marginal cases are not asserted stable or unstable nonlinearly. An equivalent unindexed derivation may exist; priority is not externally certified.

## References

1. A. L. N. Dias, R. Dickman, T. V. Rosembach, *Mean-Field Theory for the Three-State Active Lattice Gas Model*, arXiv:2604.22536v2 (2026), first version 2026-04-24. https://arxiv.org/html/2604.22536v2 ; https://doi.org/10.1103/xgn6-78vz
2. T. V. Rosembach, A. L. N. Dias, R. Dickman, *Three-state active lattice gas: a discrete Vicsek-like model with excluded volume*, arXiv:2312.09492 (2023), Phys. Rev. E 110, 014109 (2024). https://arxiv.org/abs/2312.09492
3. W. Kwak, J. H. Lee, J. M. Kim, *Three-state majority-vote model on a simple cubic lattice*, Phys. Rev. E 113, 044105 (2026). https://doi.org/10.1103/6vh3-fx7f
