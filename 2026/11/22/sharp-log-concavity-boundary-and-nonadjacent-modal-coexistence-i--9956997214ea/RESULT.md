# Sharp log-concavity boundary and nonadjacent modal coexistence in generalized Poisson–Lindley counts

## Finding

Consider the Poisson–generalized Lindley count law of Atikankul (2023), equivalent under a one-unit shape reparameterization to the earlier generalized Poisson–Lindley law. Its mass sequence is *not* always log-concave or unimodal on the published parameter domain. The following sharp statements hold.

Write \(a=\alpha-1>0\) and \(t=\theta>0\). Define
\[
a_c(t)=\frac{t+\sqrt{t^2+8(t+1)}}{2(t+2)}.
\]

**Exact curvature phase.** The mass sequence is log-concave at every index if and only if \(a\ge a_c(t)\), with strict log-concavity except for equality at the first curvature index when \(a=a_c(t)\). When \(0<a<a_c(t)\), the successive mass ratios are initially strictly increasing and eventually strictly decreasing, with exactly one possible transition index (and at most one equality).

**Complete peak-shape restriction.** Every member has at most two separated local peaks: the count probabilities can decrease, then increase, then decrease, but cannot oscillate further. Which pattern occurs is determined exactly by the sign of one concave quadratic in the count index, displayed below. In the strict two-peak case, zero and the subsequent interior peak are the only candidates for the global mode.

**Nonadjacent global-mode coexistence.** At \(\alpha=5/3\), let \(t_*\) be the unique positive root of
\[
9t^3+36t^2+40t-7=0.
\]
Then \(153/1000<t_*<154/1000\), and precisely the two nonadjacent counts \(0\) and \(2\) are global modes. Throughout the open interval \(153/1000<t<154/1000\), the only candidates for the global mode are \(0\) and \(2\); the unique mode changes from \(2\) to \(0\) as \(t\) crosses \(t_*\). In particular, the open two-local-peak regime is genuine, not an isolated numerical artifact.

## Assumptions and scope

The random count \(Y\) takes values in \(\{0,1,2,\ldots\}\), and its probabilities are
\[
p_j=\frac{t^{\alpha}\,\Gamma(j+\alpha-1)\,[j+(\alpha-1)(t+2)]}{\Gamma(\alpha)\,\Gamma(j+1)\,(t+1)^{j+\alpha+1}},\qquad j\ge0,\quad \alpha>1,\ t>0.
\]
The positivity and normalization follow from the original mixed-Poisson construction, or from the mixture of Gamma distributions with common rate \(t\), shapes \(a\) and \(a+1\), and respective weights \(t/(t+1)\) and \(1/(t+1)\). There is no restriction that \(\alpha\) be integral.

A sequence is log-concave if \(p_{j+1}^2\ge p_jp_{j+2}\) for every integer \(j\ge0\). A local peak means a count with probability at least as high as its existing immediate neighbors; the assertion about two *separated* peaks permits an adjacent equality at a transition boundary. The global modes are the counts attaining the greatest probability over all nonnegative integers. All statements are exact for the full infinite support.

## Proof

Put \(b=a(t+2)\). Cancelling the positive normalization gives the exact neighboring ratio
\[
R_j:=\frac{p_{j+1}}{p_j}=\frac{(j+a)(j+b+1)}{(t+1)(j+1)(j+b)}.
\tag{1}
\]
Therefore the sign of \(R_j-1\) is the sign of
\[
N(j)=-tj^2+[a-t(a(t+2)+1)]j+a[a(t+2)-t^2-3t-1].
\tag{2}
\]
This is a strictly concave quadratic in the real variable \(j\), with \(N(j)\to-\infty\). Consequently its positive set on the nonnegative integers is either empty or one contiguous finite interval of indices. Thus the probabilities cannot exhibit more than one block of increases, proving the complete peak-shape restriction; after the last positive-ratio index they decrease forever. If a positive block begins strictly after zero, the only separated peak candidates are zero and the right edge of this block. Zeros of \(N\) give explicit adjacent ties and are handled by retaining both neighboring counts.

A direct second ratio calculation yields
\[
R_{j+1}-R_j=\frac{-a\,H(j)}{(t+1)(j+1)(j+2)(j+b)(j+b+1)},
\tag{3}
\]
where
\[
H(j)=j^2+[2a(t+2)-2t-1]j+a(t+2)[a(t+2)-t]-2(t+1).
\tag{4}
\]
All factors in the denominator of (3) are strictly positive. At zero,
\[
H(0)=(t+2)^2a^2-t(t+2)a-2(t+1).
\tag{5}
\]
Its one positive root in \(a\) is \(a_c(t)\). To prove that \(H(0)\ge0\) is sufficient for \(H(j)\ge0\) *at every integer*, define \(a_v=(2t+1)/[2(t+2)]\). The coefficient of \(j\) in (4) is positive when \(a>a_v\), while substitution of \(a=a_v\) in (5) gives \(-(6t+7)/4<0\). Since the quadratic (5) in \(a>0\) has only one positive root, \(a_c(t)>a_v\). Thus when \(a\ge a_c(t)\), (4) is strictly increasing for real \(j\ge0\) and nonnegative at zero, with equality only at \(j=0,a=a_c(t)\). Equation (3) proves the stated global log-concavity and its equality case.

If \(0<a<a_c(t)\), then \(H(0)<0\), and the monic quadratic (4) has exactly one positive real root because the product of its two real roots is negative. Hence its signs are negative before that root and positive afterward. Equation (3) proves the claimed single curvature transition and failure of global log-concavity already at \(j=0\). This exhausts the entire two-parameter domain.

For the nonadjacent global-mode construction set \(a=2/3\), corresponding to \(\alpha=5/3\). Formula (1) gives
\[
R_0=\frac{2t+7}{3(t+1)(t+2)},\quad
R_1=\frac{5(t+5)}{3(t+1)(2t+7)},\quad
R_2=\frac{4(2t+13)}{9(t+1)(t+5)}.
\]
Consequently
\[
\frac{p_2}{p_0}-1=R_0R_1-1
=-\frac{9t^3+36t^2+40t-7}{9(t+1)^2(t+2)}.
\tag{6}
\]
The numerator polynomial is strictly increasing for \(t>0\), is negative at \(153/1000\), and positive at \(154/1000\). It therefore has exactly one positive root \(t_*\) in this interval. For *every* \(t\) in that interval, exact rational endpoint inequalities and monotonicity of the respective quadratics imply \(R_0<1\), \(R_1>1\), and \(R_2<1\): explicitly, the controlling positive-denominator numerators are \(3t^2+7t-1>0\), \(3t^2+11t-2<0\), and \(9t^2+46t-7>0\). As \(N(1)>0>N(2)\) and \(N\) is strictly concave, \(N(j)<0\) for every integer \(j\ge2\). Thus \(p_0>p_1<p_2>p_3>p_4>\cdots\), and the only global candidates are \(0,2\). Equation (6) establishes the root tie and the strict global-mode switch on opposite sides. No finite truncation or numerical root finder is used to assert the infinite tail inequalities.

## Verification

Running `python VERIFY.py` provides exact-rational checks of the ratio identities (1)–(4), the cubic factorization (6), the endpoint signs, and numerous sampled curvature identities. The independent parameter-grid diagnostics are useful error checks only; the analytical arguments above, particularly quadratic sign and monotonicity, prove the infinite-index assertions.

The unique root is approximately \(t_*=0.15309761114522854659\), calculated only for orientation. The proof uses the rational bracket and strict polynomial monotonicity.

## Relationship to prior work

Atikankul (2023, Theorem 1 and the discussion following its mass-ratio formula) derived (essentially) the mass law and asserted universal log-concavity and unimodality. The 2022 treatment by Papageorgiou and Vardaki reproduces the equivalent earlier generalized Poisson–Lindley probability-generating function of Mahmoudi and Zakerzadeh (2010). Lawal (2025) explicitly identifies the reparameterization between the older family and the 2023 family. The law itself and its mixed-Poisson representation are therefore *not* claimed as new. The new point is the exact global log-concavity parameter boundary, the nonoscillation classification of neighboring ratios, and a proved pair of nonadjacent simultaneous global modes, which contradict blanket unimodality for the admitted shape range.

Related analyses of log-concavity and multimodality in other mixed-Poisson laws do not imply the present threshold: their kernels, mixing components, parameter spaces, and neighboring-ratio numerators differ. The concrete formulas above allow statement-level comparison rather than reliance on titles.

## Limitations

The result classifies the mass-sequence curvature and peak candidates, not the failure-rate function in the non-log-concave region. Loss of log-concavity alone does not establish failure of increasing hazard rate. The source paper of Mahmoudi and Zakerzadeh (2010) could not be fully inspected through available channels, although its equivalent probability mass formula is reproduced in accessible later primary literature. Thus exhaustive historical priority remains open; no claim of independent audit or literature uniqueness is made.

## References

- Y. Atikankul, “A New Poisson Generalized Lindley Regression Model,” *Austrian Journal of Statistics* 52(1), 39–50, publicly published 7 March 2023. https://doi.org/10.17713/ajs.v52i1.1344
- E. Mahmoudi and H. Zakerzadeh, “Generalized Poisson–Lindley Distribution,” *Communications in Statistics – Theory and Methods* 39(10), 1785–1798 (2010). https://doi.org/10.1080/03610920902898514
- H. Papageorgiou and M. Vardaki, “Bivariate Discrete Poisson–Lindley Distributions,” *Journal of Statistical Theory and Practice* 16, 30 (2022), especially Section 2.4. https://doi.org/10.1007/s42519-022-00261-z
- M. R. Irshad et al., “Bivariate Poisson Generalized Lindley Distributions and the Associated BINAR(1) Processes,” *Austrian Journal of Statistics* 53(1), 1–28 (2024), especially Section 2. https://doi.org/10.17713/ajs.v53i1.1551
- B. H. Lawal, “Comparative Analyses of the Poisson-Exponential-Gamma to Selected Discrete Distributions with Applications,” *Asian Journal of Probability and Statistics* 27(2), 73–96 (2025), especially Sections 2.2 and 2.4. https://doi.org/10.9734/ajpas/2025/v27i2714
