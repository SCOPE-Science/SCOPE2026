# Exponential local tilt forces maximal logarithmic global bias
## Finding
Let \\(\\alpha\\) be an irrational of bounded type and define the half-interval discrepancy by
\\[
D_N(\\alpha)=\\#\\{{0\\le j\\le N-1:\\{{j\\alpha\\}}\\in[0,1/2)\\}}-N/2.
\\]
Suppose the sequence is exponentially tilted with nonzero parameter \\(t\\), meaning that for all \\(\\xi_1,\\xi_2\\in \\tfrac12\\mathbb Z\\),
\\[
\\frac{\\#\\{{1\\le N\\le n:D_N(\\alpha)=\\xi_1\\}}}{\\#\\{{1\\le N\\le n:D_N(\\alpha)=\\xi_2\\}}}
\\longrightarrow e^{{t(\\xi_1-\\xi_2)}}.
\\]
Write \\(\\beta=2\\alpha-1=[2m_0;2m_1,2m_2,\\ldots]\\) for its even continued fraction expansion and set
\\[
S_k=\\sum_{{j=1}}^k\\bigl(\\operatorname{{sgn}}(m_{{2j}})-\\operatorname{{sgn}}(m_{{2j-1}})\\bigr).
\\]
Then there are constants \\(c,C>0\\) and \\(k_0\\) such that
\\[
c k\\le \\operatorname{{sgn}}(t)S_k\\le C k\\qquad(k\\ge k_0).
\\]
Consequently the centering from Theorem 1.10 of the source satisfies
\\[
A_n=\\frac14S_{{\\nu_n}}=\\operatorname{{sgn}}(t)\\,\\Theta(\\log n),
\\qquad \\nu_n\\asymp\\log n,
\\]
and, because \\(B_n\\asymp\\sqrt{{\\log n}}\\),
\\[
\\frac{{A_n}}{{B_n}}\\longrightarrow \\operatorname{{sgn}}(t)\\,\\infty.
\\]
Thus exponential local bias forces not merely global bias, but maximal-order logarithmic displacement of the temporal discrepancy histogram.

## Assumptions and scope
The statement concerns the symmetric interval \\([0,1/2)\\), exactly as in Theorems 1.9 and 1.10 of the source. The irrational \\(\\alpha\\) is assumed to be of bounded type. The tilt parameter \\(t\\) is finite and nonzero. No periodicity or quadratic-irrational hypothesis is imposed.

The conclusion concerns the specific admissible centering \\(A_n\\) from Theorem 1.10. As usual for a central limit theorem, other centerings differing from it by \\(o(B_n)\\) yield the same normalized limit; the logarithmic order and sign therefore persist for every such asymptotically equivalent centering.

## Proof
The source identifies discrepancy values with visits of a linear flow on the infinite staircase: the level \\(D_N(\\alpha)=k/2\\) corresponds to the horizontal rectangle \\(R_k\\). Hence exponential tilt with parameter \\(t\\) gives, for every \\(k,\\ell\\in\\mathbb Z\\), a staircase occupation ratio
\\[
\\frac{{\\operatorname{{time}}(R_k)}}{{\\operatorname{{time}}(R_\\ell)}}\\longrightarrow
 e^{{(t/2)(k-\\ell)}}.
\\]
By Theorem 1.25, the corresponding staircase point is therefore generic for the invariant measure with pressure parameter
\\[
\\eta=t/2\\ne0.
\\]

For the Markov pressure functions \\(P_n\\), Proposition 8.9 and Lemma 11.5 give
\\[
P_n'(0)=O(1).
\\]
Proposition 8.10 gives variance \\(V_n\\asymp n\\), and Lemma 11.5 then yields, on every fixed bounded parameter interval,
\\[
c_0n\\le P_n''(u)\\le C_0n
\\]
for all sufficiently large \\(n\\), with constants \\(c_0,C_0>0\\). Theorem 1.25 together with Proposition 11.7 supplies parameters \\(\\eta_n\\to\\eta\\) satisfying
\\[
P_n'(\\eta_n)=z_n,
\\]
where \\(z_n\\) is the renormalized staircase height relevant to the initial discrepancy orbit. By the mean value theorem,
\\[
z_n=P_n'(0)+\\eta_n P_n''(\\theta_n)
\\]
for some \\(\\theta_n\\) between \\(0\\) and \\(\\eta_n\\). Since \\(\\eta\\ne0\\), eventually \\(\\eta_n\\) has sign \\(\\eta\\) and magnitude at least \\(|\\eta|/2\\). Therefore there are \\(c_1,C_1>0\\) such that
\\[
c_1n\\le \\operatorname{{sgn}}(t)z_n\\le C_1n
\\]
for all sufficiently large \\(n\\).

Theorem 4.5 gives the exact twist identity
\\[
z_n=\\frac12\\sum_{{j=1}}^{{nN_0}}
\\bigl(\\operatorname{{sgn}}(m_{{2j}})-\\operatorname{{sgn}}(m_{{2j-1}})\\bigr)
=\\frac12S_{{nN_0}},
\\]
where \\(N_0\\) is the fixed renormalization block length. Thus \\(S_{{nN_0}}\\) has fixed sign and magnitude comparable to \\(n\\). Each summand defining \\(S_k\\) lies in \\([-2,2]\\), so passing from a general \\(k\\) to the nearest multiple of \\(N_0\\) changes \\(S_k\\) by only \\(O(1)\\). Hence
\\[
c k\\le \\operatorname{{sgn}}(t)S_k\\le C k
\\]
for all sufficiently large \\(k\\).

Finally, Theorem 1.10 states that one may take \\(A_n=\\tfrac14S_{{\\nu_n}}\\) with \\(\\nu_n\\asymp\\log n\\), while Theorem 1.9 gives \\(B_n\\asymp\\sqrt{{\\log n}}\\). Substitution proves the asserted logarithmic centering and divergence of \\(A_n/B_n\\).

## Verification
The proof is analytic. The critical chain was checked directly against the source statements: Definition 1.1 and the staircase coding fix the factor \\(\\eta=t/2\\); Theorem 1.25 converts occupation ratios into convergence of pressure parameters; Proposition 8.9 controls \\(P_n'(0)\\); Proposition 8.10 and Lemma 11.5 give uniform linear-in-\\(n\\) curvature; Proposition 11.7 transfers between the geometric and Markov pressure equations; and Theorem 4.5 identifies the renormalized height with the even-continued-fraction sign sum. No finite computation is used as evidence for an infinite statement.

## Relationship to prior work
Dolgopyat and Sarig prove for arbitrary bounded-type irrationals that local bias implies global bias, and they exhibit a globally biased but locally unbiased example whose continued-fraction sign sum grows like \\(n^{{2/3}}\\). They also prove that any tilt in the bounded-type setting is exponential and construct every exponential tilt parameter. Their stated results do not give the stronger quantitative conclusion above: nonzero exponential tilt forces eventual one-sided linear drift of the sign sum and hence logarithmic centering of maximal possible order.

For quadratic irrationals, the source already notes that the relevant sign sum equals a constant times \\(n\\), up to \\(O(1)\\), so logarithmic centering is classical in that periodic setting. The contribution here is the implication for the full bounded-type exponential-tilt class, including nonquadratic examples supplied by the 2026 construction. Earlier work of Avila, Dolgopyat, Duryev, and Sarig treats the quadratic-renormalizable staircase setting and does not state this all-bounded-type implication.

## Limitations
The result does not claim an exact coefficient for \\(A_n/\\log n\\); the pressure curvature can vary with the nonstationary continued-fraction environment, so the proof yields two-sided order bounds and the eventual sign. It also does not assert that every globally biased or every merely locally biased bounded-type irrational has logarithmic-order centering; the source explicitly shows that global bias can occur at smaller continued-fraction drift scales. A bibliographic residual risk remains that an equivalent all-bounded-type implication may appear in older literature under different pressure or cocycle terminology.

## References
1. D. Dolgopyat and O. Sarig, *Generic Points on the Staircase and Irregularities in Uniform Distribution*, arXiv:2609.33590v1, 2026. Relevant statements: Definition 1.1; Theorems 1.3, 1.4, 1.9, 1.10, 1.25, 4.5; Propositions 8.9, 8.10, 11.7; Lemma 11.5; Corollary 1.12.
2. A. Avila, D. Dolgopyat, E. Duryev, and O. Sarig, *The visits to zero of a random walk driven by an irrational rotation*, Israel Journal of Mathematics 207 (2015), 653--717, doi:10.1007/s11856-015-1186-4.
