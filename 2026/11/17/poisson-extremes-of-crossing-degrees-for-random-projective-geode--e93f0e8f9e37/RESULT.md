# Poisson extremes of crossing degrees for random projective geodesic arcs

## Finding

Give the round real projective plane \(\mathbb{RP}^2\) curvature one, so each complete projective geodesic has length \(\pi\). Independently choose \(n\) geodesic arcs as follows: sample a projective geodesic with its invariant probability measure, a uniform midpoint along that geodesic, and a length \(L\in(0,\pi/2)\), independently of the other choices. The distribution function \(F\) of \(L\) has mean \(\mu>0\) and obeys, for some \(c>0\) and \(\alpha>1\),
\[
 F(t)=c t^{\alpha}+o(t^{\alpha})\qquad(t\downarrow0).
\]
Join vertices \(i,j\) of the crossing graph when the interiors of their arcs intersect transversely, and write \(K_i^{(n)}\) for the degree of vertex \(i\). Put \(b_n=n^{1-1/\alpha}\). Then the *entire point process of lower crossing degrees* has the weak vague limit
\[
 \sum_{i=1}^{n}\delta_{K_i^{(n)}/b_n}
 \ \Longrightarrow\ \operatorname{PPP}\left(\alpha c
 \left(\frac{\pi^2}{\mu}\right)^\alpha x^{\alpha-1}\,dx\right)
 \quad\text{on }[0,\infty).
\]
In particular, if \(K_{(r)}^{(n)}\) is the \(r\)-th smallest degree, then for every integer \(r\ge1\) and \(x\ge0\),
\[
 \Pr\left\{K_{(r)}^{(n)}>xb_n\right\}
 \longrightarrow e^{-\Lambda(x)}\sum_{j=0}^{r-1}\frac{\Lambda(x)^j}{j!},
 \qquad\Lambda(x)=c\left(\frac{\pi^2x}{\mu}\right)^\alpha.
\]
For every fixed nonnegative integer \(k\), the rare exact-degree probabilities satisfy
\[
 \Pr\{K_i^{(n)}=k\}\sim
 \frac{\alpha c\,\Gamma(k+\alpha)}{k!}
 \left(\frac{\pi^2}{\mu n}\right)^\alpha.
\]
These are consequences of the *same* extreme-degree theorem: low-degree vertices are created by the shortest random arcs, despite the strong dependence of different crossing-graph edges.

**Independent uniform endpoint specialization.** If each arc is the unique shortest geodesic between independent uniformly distributed points of \(\mathbb{RP}^2\), then \(F(t)=1-\cos t\), \(\mu=1\), \(\alpha=2\), \(c=1/2\). Consequently
\[
 \sum_{i=1}^n\delta_{K_i^{(n)}/\sqrt n}
 \Longrightarrow\operatorname{PPP}(\pi^4x\,dx),\qquad
 \Pr\{K_{(1)}^{(n)}/\sqrt n>x\}\longrightarrow e^{-\pi^4x^2/2},
\]
\[
 \Pr\{K_i^{(n)}=k\}\sim\frac{(k+1)\pi^4}{n^2}.
\]

## Assumptions and scope

The projective plane is round, with distance measured in radians and Haar-uniform supporting projective lines and phases. Arc lengths are strictly shorter than \(\pi/2\), ensuring unique minimizing arcs. Lengths are independent and identically distributed with an arbitrary law satisfying the stated small-length regular variation; no density or smoothness is assumed in the general theorem. All random choices are independent across different arcs. Transverse intersection is understood in the intrinsic projective plane, where two distinct complete projective lines have one intersection. The limiting process is locally finite; the claimed vague convergence includes neighborhoods of zero.

## Proof

**1. Exact projective crossing kernel.** Conditional on a fixed arc of length \(\ell\), the supporting line of a second isotropic arc meets its supporting line at a point uniform on the latter's full projective circumference \(\pi\). The chance that this point belongs to the fixed arc is \(\ell/\pi\). Conditional on the second arc's length \(s\) and supporting line, its uniform phase places that intersection in its interior with probability \(s/\pi\). Hence the conditional crossing probability given both lengths is \(\ell s/\pi^2\), and, given the fixed arc alone, it is \(\mu\ell/\pi^2\). All other arcs are independent conditional on the fixed arc, so exactly
\[
 K_i^{(n)}\mid(L_i=\ell)\sim
 \operatorname{Bin}\left(n-1,\frac{\mu\ell}{\pi^2}\right).
 \tag{1}
\]
This is a projective, not spherical, Crofton calculation: a projective geodesic has circumference \(\pi\), and its two antipodal lifts represent one point. As \(\mu<\pi/2\), the success parameter is strictly less than one.

**2. Extremes of independent lengths.** From the assumed tail, for every fixed \(t>0\),
\[
 n\Pr\{n^{1/\alpha}L_i\le t\}\longrightarrow c t^\alpha.
\]
Independence and the multinomial-to-independent-Poisson limit on finitely many disjoint intervals imply that the point process \(\sum_i\delta_{n^{1/\alpha}L_i}\) converges vaguely on \([0,\infty)\) to a Poisson point process of intensity \(\alpha c t^{\alpha-1}dt\). This step needs only the distribution-function asymptotic, not a density.

**3. Low degrees track short lengths jointly.** Let \(m_i=(n-1)\mu L_i/\pi^2\). For every fixed \(B,\varepsilon>0\), the number of vertices with \(L_i\le Bn^{-1/\alpha}\) is tight, while by (1),
\[
 \operatorname{Var}(K_i^{(n)}\mid L_i)\le m_i=O_B(b_n)
 \quad\text{on that event}.
\]
Conditional Chebyshev followed by an expectation/union bound proves
\[
 \max_{i:L_i\le Bn^{-1/\alpha}}
 \left|\frac{K_i^{(n)}}{b_n}
 -\frac{\mu}{\pi^2}n^{1/\alpha}L_i\right|
 \xrightarrow{\Pr}0.
 \tag{2}
\]
No independence between different degrees is assumed here.

It remains essential to rule out spurious low degrees of long arcs. Fix \(C>0\) and choose \(B>4C\pi^2/\mu\). When \(L_i>Bn^{-1/\alpha}\), its conditional binomial mean exceeds \(2Cb_n\) for all sufficiently large \(n\). The multiplicative Chernoff bound gives a constant \(a_B>0\) such that
\[
 \Pr\{K_i^{(n)}\le Cb_n\mid L_i>Bn^{-1/\alpha}\}
 \le e^{-a_B b_n}.
\]
The union bound \(n e^{-a_B b_n}\to0\) holds precisely because \(\alpha>1\). Thus every degree point in a fixed bounded interval is, with probability tending to one, close to the rescaled length point specified in (2). The continuous mapping of the length Poisson process by \(t\mapsto\mu t/\pi^2\) proves the claimed joint degree point-process limit and its intensity. Its cumulative intensity on \([0,x]\) is \(\Lambda(x)\), proving the order-statistic formulas.

**4. Fixed-degree asymptotics.** From (1), for \(0\le k\le n-1\),
\[
 \Pr\{K_i^{(n)}=k\}
 =\binom{n-1}{k}\int_{(0,\pi/2)}
 \left(\frac{\mu\ell}{\pi^2}\right)^k
 \left(1-\frac{\mu\ell}{\pi^2}\right)^{n-1-k}
 \,dF(\ell).
\]
Scale \(t=n\mu\ell/\pi^2\). Regular variation of \(F\) gives vague convergence of the scaled Stieltjes measure to \(\alpha c(\pi^2/\mu)^\alpha t^{\alpha-1}\,dt\). The binomial kernel converges to \(t^ke^{-t}/k!\). Uniform exponential bounds outside a bounded scaled interval, followed by a near-zero truncation and the regular-variation bound, justify passage to the limit. The integral \(\int_0^\infty t^{k+\alpha-1}e^{-t}dt=\Gamma(k+\alpha)\) proves the stated coefficient.

**5. Uniform projective endpoints.** Represent two independent Haar projective points by independent uniform unit sphere lifts. Their absolute inner product is uniform on \([0,1]\); hence their projective distance has distribution \(F(t)=1-\cos t\) for \(0\le t\le\pi/2\), density \(\sin t\), and mean \(\int_0^{\pi/2}t\sin t\,dt=1\). Thus \(F(t)\sim t^2/2\). Substitution into the general formulas proves the displayed \(\pi^4\) intensity, Rayleigh-type minimum, and \((k+1)\pi^4\) rare-degree constant.

## Verification

The standalone `verify.py` carries out independent projective endpoint sampling with direct three-dimensional great-circle intersection tests, verifies the projective length law and conditional-degree predictions, checks the fixed-degree constants by independent numerical integration for several sample sizes, and checks a second family of power-law length distributions with exponents \(3/2\) and \(3\). It also compares the exact shortest-length survival with the claimed Rayleigh limit. The checker completed with `PROJECTIVE_EXTREME_DEGREE_CHECKS_OK` and `POWER_LAW_EXTREMES_CHECKS_OK`. Computations are finite corroborations; the Crofton identity, Chernoff exclusion, and Poisson-process argument above supply the infinite proof.

## Relationship to prior work

Acan (arXiv:1501.01489, first posted January 7, 2015) studies degree distributions and connectivity in uniformly random combinatorial chord matchings. Those chords have dependent endpoint pairings and a different low-degree regime; the paper does not prove projective shortest-geodesic extreme-degree limits. The January 6, 2014 spherical random-geodesic crossing discussion establishes a spherical pair-crossing probability, not a projective global minimum-degree process. Bonamy, Mohar and Wesolek (arXiv:2008.10459, 2020) investigate crossing graphons for spherical complete-graph drawings with shared endpoints, and do not determine the present extremes. The publicly available result *Geodesic-needle crossing networks: exact star spectrum and a variance transition* (2026) does give conditional binomial degrees for iid isotropic arcs on the **sphere**, as well as normalized degree and edge-count limits. Its conditional-degree idea is credited. Neither its theorem nor those other inspected results supply the joint lowest-degree Poisson process, the projective coefficient, or the sharp fixed-degree spectrum. The standard Poisson rare-event and Chernoff steps are not claimed as newly invented techniques.

## Limitations

The theorem is specific to independent isotropic arc sampling on the round projective plane, power-law short-length tails with exponent strictly greater than one, and transversal intersections. It does not cover the critical or subcritical exponents, nonuniform line directions, nonround projective metrics, or the full graph connectivity distribution. No finite-sample convergence rate, independent mathematical review, or definitive historical-priority certification is claimed. The cited public literature was searched on a bounded basis.

## References

1. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489, first posted 2015-01-07. https://arxiv.org/abs/1501.01489
2. G. Bor, response to *Probability of random geodesics on the round sphere intersecting*, MathOverflow, 2014-01-06. https://mathoverflow.net/questions/153700/probability-of-random-geodesics-on-the-round-sphere-intersecting
3. M. Bonamy, B. Mohar and A. Wesolek, *Limiting crossing numbers for geodesic drawings on the sphere*, arXiv:2008.10459, first posted 2020-08-24. https://arxiv.org/html/2008.10459v1
4. *Geodesic-needle crossing networks: exact star spectrum and a variance transition*, published research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-geodesic-needle-crossing-networks-exact-star-spectrum-and-a-vari--157858c14e30
