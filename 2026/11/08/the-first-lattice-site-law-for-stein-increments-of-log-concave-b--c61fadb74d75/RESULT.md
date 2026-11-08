# The first-lattice-site law for Stein increments of log-concave birth–death targets

## Finding

Let \(p=(p_j)_{j\ge0}\) be a strictly positive log-concave probability mass function on the nonnegative integers, let \(w>0\), and put \(r_j=p_j/p_{j-1}\) for \(j\ge1\). For each subset \(A\) of the nonnegative integers, let \(g_A\) be the bounded solution, normalized by \(g_A(0)=0\), of

\[
w g_A(j+1)-d(j)g_A(j)=\mathbf1_A(j)-\Pr(Z\in A),\qquad d(0)=0,\quad d(j)=w\frac{p_{j-1}}{p_j}\ (j\ge1),
\]

where \(Z\) has law \(p\) and \(\Delta g_A(j)=g_A(j+1)-g_A(j)\). Then the **exact** global indicator first-difference factor is

\[
\boxed{\sup_{A}\sup_{j\ge1}|\Delta g_A(j)|=\frac{1-p_0}{w}.}
\]

More precisely, for every integer \(j\ge1\),

\[
\boxed{
\sup_A |\Delta g_A(j)|
=\frac{1-p_0}{w}-\frac1w\sum_{i=0}^{j-1}p_i(r_{i+1}-r_j).
}
\]

The pointwise supremum is attained by \(A=\{j\}\) and its complement. In the global supremum, \(j=1\) always attains equality, and \(j\ge2\) does so exactly when \(r_1=\cdots=r_j\). Thus for strictly log-concave \(p\), the unique maximizing index among \(j\ge1\) is \(j=1\).

For the discrete Bessel law \(\mathrm{Bes}(k,a)\), \(k\in\mathbb Z_{\ge0}\), \(a>0\), and \(\nu=a^2/4\), the exact factor from the same theorem is

\[
\boxed{
\Lambda_{k,\nu}=\frac{1}{\nu}\left(1-\frac{(a/2)^k}{k!\,I_k(a)}\right).
}
\]

Here \(I_k(a)=\sum_{n\ge0}(a/2)^{2n+k}/(n!(n+k)!)\). For fixed \(k\), this equals \((1+o(1))/\nu\) as \(\nu\to\infty\).

## Assumptions and scope

The support is the entire set \(\mathbb Z_{\ge0}\): every \(p_j>0\), \(\sum_jp_j=1\), and \(p_j^2\ge p_{j-1}p_{j+1}\) for all \(j\ge1\). Equivalently, the positive ratios \(r_1,r_2,\ldots\) are nonincreasing. These assumptions imply a geometric upper bound on the eventual right tail, hence existence of all moments and a bounded solution for every bounded test function. The scale \(w\) is arbitrary but fixed and positive. The factor concerns indicator test functions and *first differences* of their density-form Stein solutions, not the supremum norm of the solutions themselves, and not the derivative of a differently normalized Stein operator. Indices in the main norm satisfy \(j\ge1\), consistent with the motivating Bessel factor definition.

## Proof

**1. The bounded solution.** Detailed balance gives \(d(j)p_j=wp_{j-1}\). Multiplying the Stein equation by \(p_j\) and summing from zero through \(m\), with \(g_A(0)=0\), yields

\[
 g_A(m+1)=\frac1{wp_m}\sum_{i=0}^m p_i\bigl(\mathbf1_A(i)-\Pr(Z\in A)\bigr).
\]

The full centered sum vanishes, so the numerator can equivalently be written as the negative tail sum over \(i\ge m+1\). Since a positive summable log-concave sequence eventually has \(r_j\le q<1\), the ratio of this tail to \(p_m\) is eventually at most \(q/(1-q)\); finitely many smaller \(m\) do not affect boundedness. For the homogeneous equation, its state-zero equation forces \(g(1)=0\), and detailed balance then forces \(g(m)=0\) for every \(m\ge1\). With the stated \(g(0)=0\) normalization, uniqueness follows.

**2. The pointwise indicator envelope.** Fix \(j\ge1\), define \(F_j=\sum_{i=0}^jp_i\), \(G_j=\sum_{i=j}^{\infty}p_i\), and expand \(w\Delta g_A(j)\) linearly in \(\mathbf1_A(i)\). The coefficient \(c_{j,i}\) is

\[
 c_{j,i}=\begin{cases}
 p_i\bigl(G_{j+1}/p_j-G_j/p_{j-1}\bigr),&i<j,\\
 G_{j+1}+r_jF_{j-1},&i=j,\\
 p_i\bigl(F_{j-1}/p_{j-1}-F_j/p_j\bigr),&i>j.
 \end{cases}
\]

Because \(r_{m+1}\le r_j\) for all \(m\ge j\), summing \(p_{m+1}\le r_jp_m\) gives \(G_{j+1}\le r_jG_j\); thus the coefficients for \(i<j\) are nonpositive. Similarly, \(r_{i+1}\ge r_j\) for \(0\le i<j\), so summing \(p_{i+1}\ge r_jp_i\) gives \(F_j-p_0\ge r_jF_{j-1}\), and the coefficients for \(i>j\) are nonpositive. The coefficient at \(i=j\) is positive. Since the coefficients sum to zero (the full-set test has identically zero Stein solution), the maximal absolute sum over subsets is exactly this positive coefficient. Therefore

\[
 w\sup_A|\Delta g_A(j)|=G_{j+1}+r_jF_{j-1}.
\]

Choosing \(A=\{j\}\) realizes the positive extremum, and choosing its complement realizes the negative one.

**3. The exact deficit and maximizers.** Subtract the pointwise expression from \(1-p_0=G_{j+1}+\sum_{i=1}^jp_i\):

\[
 (1-p_0)-w\sup_A|\Delta g_A(j)|
 =\sum_{i=0}^{j-1}\bigl(p_{i+1}-r_jp_i\bigr)
 =\sum_{i=0}^{j-1}p_i(r_{i+1}-r_j)\ge0.
\]

At \(j=1\) the sum is zero. Since all \(p_i>0\) and the ratios are nonincreasing, the sum vanishes for any \(j\ge2\) exactly when all ratios \(r_1,\ldots,r_j\) coincide. This proves the global equality and the optimizer classification. (Under the chosen normalization, the excluded boundary index \(j=0\) also has factor \((1-p_0)/w\).)

**4. Bessel specialization.** For \(\mathrm{Bes}(k,a)\), the mass satisfies \(p_n=(a/2)^{2n+k}/(n!(n+k)!I_k(a))\), with strictly decreasing adjacent ratios \(r_j=\nu/(j(j+k))\), and \(d(j)=j(j+k)\) with \(w=\nu\). The theorem gives the displayed exact formula and unique positive-index maximizer \(j=1\). From the defining series, \(I_k(a)\ge (a/2)^k/k!\,[1+\nu/(k+1)]\), so \(p_0\le[1+\nu/(k+1)]^{-1}\to0\) at fixed \(k\); this proves the asserted asymptotic without an unproved local limit approximation.

## Verification

The standalone standard-library Python program `verify_stein.py` reconstructs Stein solutions for every indicator on 59 finite log-concave test profiles, compares direct first differences with the local formula in exact rational arithmetic, tests the ratio-gap identity and optimizer characterization, and checks the zero-boundary increment. It also runs finite-prefix diagnostics for a highly concentrated log-concave family. The extracted program reported **21,970 passed assertions**. Finite-support checks are diagnostic only: the proof above establishes the infinite full-support statement, without treating a finite prefix or computation as an exhaustive proof.

Run: `python3 verify_stein.py` from the extracted folder; no third-party dependencies.

## Relationship to prior work

The general density-form Stein solution and its pointwise indicator envelope have precedents in Brown–Xia (2001), in the discrete treatment of Eichelsbacher (2026, Proposition 2.1), and in DeSalvo (2026, Theorems 2.3 and 2.5). **Those formulas are not claimed as new.** DeSalvo's Open Problems 8.1 and 8.2 explicitly ask for, respectively, the sharp Bessel first-difference factor and a \(1/w\) bound under log-concavity, and give only weaker closed estimates. The contribution here is the optimized **global equality** \((1-p_0)/w\) throughout the full-support log-concave class, the explicit nonnegative gap decomposition and complete maximizing-index characterization. In particular this identifies an exact Bessel constant rather than only the asymptotic observed numerically.

## Limitations

The result does not bound the zeroth-order factor \(\sup_A\|g_A\|\), does not prove the other conjectured \(C\sigma/w\) estimate in DeSalvo's Open Problem 8.2, and does not treat general non-log-concave laws or finite-support birth-rate boundary changes. The original Brown–Xia article could not be inspected in full in this investigation; a global optimizer identity implicit or explicit in that earlier work would affect historical priority. The proof and its computational checks are not independent mathematical certification.

## References

1. Stephen DeSalvo, *Two moments suffice for Bessel approximation: conditioned differences, contingency tables, and probabilistic divide-and-conquer*, arXiv:2611.00263v1, first posted 2026-10-30. https://arxiv.org/abs/2611.00263
2. Peter Eichelsbacher, *Stein Solution Factors via Mills Ratios: Affine Birth Rates and Symmetric Potential Distributions*, arXiv:2609.25380, first posted 2026-09-21. https://arxiv.org/abs/2609.25380
3. Timothy C. Brown and Aihua Xia, *Stein's Method and Birth-Death Processes*, Annals of Probability 29 (2001), 1373–1403, https://doi.org/10.1214/aop/1015345606.
4. Bertrand Cloez and Claire Delplancke, *Intertwinings and Stein's magic factors for birth-death processes*, arXiv:1609.08390, 2016; published in Annales de l'Institut Henri Poincaré Probabilités et Statistiques 55 (2019). https://arxiv.org/abs/1609.08390
