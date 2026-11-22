# Fixed-reproduction inversion of epidemic outbreak probability and final attack size

## Finding
Consider two host types occupying fractions \(1-p\) and \(p\), where \(0<p<1\). The first type has susceptibility and infectivity equal to one. The second has susceptibility \(c\) and infectivity \(A/c\), with fixed \(A>1\) and \(1\le c\le A\). There is homogeneous mass-action mixing, exponentially distributed infectious lifetimes with common recovery rate \(\gamma>0\), and transmission coefficient \(\beta>0\). Set \(R=\beta/\gamma\) and assume \(R(1-p+pA)>1\).

**Theorem.** Throughout the entire interval \(1\le c\le A\), the basic reproduction number \(\mathcal R_0=R(1-p+pA)\) is constant. In the vanishing-seed deterministic SIR limit, the positive-branch final attack fraction \(T(c)\) is **strictly decreasing** with \(c\). In the corresponding early-stage two-type continuous-time Markov branching process, the probability \(P(c)\) of nonextinction from a single founder chosen according to the population fractions is **strictly increasing** with \(c\). Thus, for every \(1\le c_1<c_2\le A\),
\[
\boxed{T(c_1)>T(c_2),\qquad P(c_1)<P(c_2),\qquad
\mathcal R_0(c_1)=\mathcal R_0(c_2).}
\]
Both classwise directions are also exact: with increasing \(c\), the eventual infected fraction **within the low-susceptibility class decreases** and that within the high-susceptibility class increases, while major-outbreak probability from a low-type founder increases and from a high-type founder decreases.

The scalar equations and their uniquely positive solutions give an exact, numerically reproducible characterization for every admissible parameter choice:
\[
\frac1R=(1-p)f(q)+pA f(cq),\qquad f(u)=\frac{1-e^{-u}}u,\qquad
T(c)=(1-p)(1-e^{-q})+p(1-e^{-cq}),
\]
\[
\frac1R=\frac{1-p}{1+z}+\frac{pA}{1+(A/c)z},\qquad
P(c)=1-\frac{1}{AR}-\frac{(1-p)(1-A^{-1})}{1+z}.
\]
Here \(q>0\) and \(z>0\) depend on \(c\). The analytic comparison is strict for every pair of distinct admissible allocations, not merely for the two endpoints.

## Assumptions and scope
Type L and H each have a fixed population fraction \(1-p\) and \(p\). The type-specific infected and susceptible fractions \(I_L,I_H,S_L,S_H\) obey
\[
\dot S_L=-\beta S_L(I_L+(A/c)I_H),\quad
\dot S_H=-\beta cS_H(I_L+(A/c)I_H),
\]
\[
\dot I_L=-\dot S_L-\gamma I_L,\qquad
\dot I_H=-\dot S_H-\gamma I_H.
\]
There is no reinfection, migration, assortative mixing, adaptive behavior, mortality other than common removal, or changing group membership. The *deterministic* final-size result refers to the unique positive outbreak branch as initial infected mass vanishes while initial susceptible fractions approach \((1-p,p)\). A finite nonzero seed can introduce seed-composition effects and is not covered by the exact stated ordering. The *stochastic* result concerns the early-stage continuous-time two-type branching process with independent rate-\(\gamma\) removals, where a type-\(j\) infective produces type-\(i\) infections at rate \(\beta\times\text{(susceptibility of type }i\text{)}\times\text{(population fraction of type }i\text{)}\times\text{(infectivity of type }j\text{)}\). It is not an exact finite-population probability. A random founder is type H with probability \(p\), regardless of its susceptibility after it has already become infected.

The next-generation matrix is a rank-one outer product with nonzero eigenvalue \(R[(1-p)+p c(A/c)]=R(1-p+pA)\). Requiring this to exceed one makes both the deterministic positive branch and the branching survival probability nonzero.

## Proof
**1. Deterministic final-size equation and uniqueness.** Put \(q=\beta\int_0^\infty(I_L+(A/c)I_H)\,dt\). Integration of the susceptible equations gives \(S_L(\infty)=(1-p)e^{-q}\) and \(S_H(\infty)=pe^{-cq}\) in the vanishing-seed positive branch. Every newly infected individual eventually leaves infection at rate \(\gamma\), so integrating the infected equations gives
\[
q=R\big[(1-p)(1-e^{-q})+p(A/c)(1-e^{-cq})\big].
\]
For \(q>0\), divide by \(q\) to obtain the displayed equation with \(f\). Since \(f(u)=\int_0^1e^{-tu}\,dt\), \(f'(u)<0\) for nonnegative \(u\), \(f(0)=1\), and \(f(u)\to0\) as \(u\to\infty\). Therefore the right-hand side decreases strictly from \(1-p+pA>1/R\) to zero. A unique \(q>0\) exists.

**2. Strict class-resolved final-size ordering.** Let \(h=cq\), and put
\[
D=(1-p)f'(q)+pAc f'(h)<0.
\]
Implicit differentiation, with the positive solution smooth in \(c\), yields
\[
q'=-\frac{pAq f'(h)}{D}<0,\qquad
h'=\frac{(1-p)q f'(q)}{D}>0.
\]
Thus \(1-e^{-q}\) strictly decreases and \(1-e^{-h}\) strictly increases with \(c\). For the total fraction,
\[
T'=\frac{p(1-p)q}{D}
\big[-Ae^{-q}f'(h)+e^{-h}f'(q)\big].
\]
The bracket is strictly positive: \(h\ge q\), \(A>1\), and
\[
G(u)=e^u[-f'(u)]=\int_0^1t e^{(1-t)u}\,dt
\]
is strictly increasing for \(u\ge0\). Hence \(A G(h)>G(q)\). Multiplying the bracket by \(e^{q+h}>0\) gives precisely \(A G(h)-G(q)>0\); since \(D<0\), \(T'<0\).

**3. Exact early-branching survival equations.** Conditional on an infectious lifetime \(L\sim\operatorname{Exp}(\gamma)\), offspring of types L and H are independent Poisson variables with rates per unit time proportional to the founder's infectivity. Integrating the conditional generating function over \(L\) gives
\[
G_j(s_L,s_H)=\frac{1}{1+R b_j[(1-p)(1-s_L)+pc(1-s_H)]},
\]
where \(b_L=1\) and \(b_H=A/c\). This is the correct joint offspring generating function; after integrating out the shared random lifetime, the counts are generally *not* independent Poisson variables. Write \(u_L,u_H\) for survival probabilities. The fixed-point equations give
\[
u_L=\frac{z}{1+z},\quad u_H=\frac{(A/c)z}{1+(A/c)z},\quad
z=R[(1-p)u_L+pcu_H].
\]
Canceling positive \(z\) gives the displayed scalar equation. Its right-hand side is strictly decreasing from \(1-p+pA>1/R\) to zero, giving exactly one positive solution (the nonzero survival solution). At or below the critical reproduction number only zero survival is possible.

**4. Strict reversal of outbreak probabilities.** Set \(d=A/c\) and \(w=dz\). When \(c\) increases, \(d\) decreases; the quantity \((1-p)/(1+z)+pA/(1+dz)\) therefore increases at fixed \(z>0\). Since it is strictly decreasing in \(z\), its uniquely determined level-set solution \(z\) strictly increases. Alternatively, in terms of \(w\), the constraint becomes
\[
\frac1R=\frac{1-p}{1+(c/A)w}+\frac{pA}{1+w}.
\]
Its first term strictly decreases as \(c\) increases at fixed \(w\), so the level-set solution \(w\) strictly decreases. Hence low-founder survival \(z/(1+z)\) increases while high-founder survival \(w/(1+w)\) decreases.

To determine which direction dominates under population-weighted seeding, eliminate the high-type term using the scalar equation:
\[
P=(1-p)\frac{z}{1+z}+p\frac{w}{1+w}
=1-\frac1{AR}-\frac{(1-p)(1-A^{-1})}{1+z}.
\]
The coefficient of \((1+z)^{-1}\) is strictly positive because \(0<p<1\), \(A>1\). Since \(z\) increases strictly, so does \(P\). This proves the entire theorem, including endpoints by continuity.

## Verification
The standalone `verify.py` uses only the Python standard library. It checks exact rational branching roots at two endpoints, scalar residuals, an algebraically independent survival-probability identity, and every claimed strict ordering on a 1,700-point grid covering five type proportions, four reproduction products, five supercriticality levels, and seventeen allocation levels. It passes **16,816 deterministic assertions**. The strict all-parameter theorem follows from the analytic monotonicity and uniqueness arguments above, not from sampling.

At \(p=1/2\), \(A=4\), \(R=1\), the common reproduction number is \(5/2\). At \(c=1\), the branching root is exactly \(z=1/2\), giving \(P=1/2\), and the deterministic attack fraction is approximately \(0.892644753609\). At \(c=4\), the root is exactly \(z=3/2\), giving \(P=3/5\), while the final attack fraction is approximately \(0.733186926970\). These values exhibit the strict reversal at equal reproduction number. Numerically saturated infection fractions are allowed to tie after floating-point rounding at very high transmission; the analytic inequalities remain strict.

## Relationship to prior work
Mazza and coauthors introduce the two-risk-class susceptibility/infectivity structure and derive epidemic thresholds, including network and homophily effects. Their general framework is **not** new here. Harris and coauthors previously analyze covarying susceptibility and transmissibility and report both final-size and major-outbreak effects at matched reproduction number; their paper therefore prefigures the qualitative distinction between these outcomes. However, their model comparisons vary joint trait distributions and transmission normalization and do not supply the exact *individual high-type product fixed*, single-parameter, all-supercritical-rates opposite-order theorem above or its two strictly monotone root characterizations. This is a narrower analytic refinement, not the discovery that the two outcome measures can differ.

El Khalifi establishes concordance-order monotonicity of final size and outbreak survival at **fixed susceptibility and infectivity marginals**. Here the marginals themselves change with \(c\), while each high-type product stays fixed. Thus concordance order does not compare the present distribution family, and its joint monotonicity does not imply this reversal. Kawagoe and coauthors give a general heterogeneous-SIR reduction and final-size comparisons, including observations about heterogeneity at fixed reproduction number; they do not derive the present joint, exact, all-allocation *final attack versus branching survival* reversal. Nandi and Allen treat two-group transmission models separately varying susceptibility or infectivity; their equations supply context, but the exact reciprocal-factor allocation and the simultaneous opposite strict inequalities are not established in the accessible material. Prior mathematical finding records on time-varying risk and on pure cross-type Poisson branching fix different model objects or comparison constraints, so do not imply the stated theorem.

These comparisons are literature-bounded. Related general heterogeneous epidemic and branching-process results may subsume a part of this theorem without naming the reciprocal-factor family; independent historical-priority verification is still needed.

## Limitations
The mathematical claim holds for fixed class fractions, rank-one homogeneous mixing, identical exponential recovery laws, strictly supercritical infection, and the fixed high-type susceptibility–infectivity product \(A\). It does not assert a universal tradeoff in arbitrary networks, arbitrary trait couplings, assortative contacts, changing recovery rates, finite initial infection, or models with behavioral adaptation. Branching-process nonextinction is an early-epidemic infinite-population approximation; finite epidemics always terminate. The positive deterministic final-size branch corresponds to a macroscopic outbreak, not the unconditional expected finite-population size. The result provides a comparison, not a public-health intervention recommendation.

## References
- F. Mazza, G. Ricci, F. Colaiori, S. Guarino, S. Meloni, and F. Saracco, “Impact of behavioral heterogeneity on epidemic outcome and its mapping into effective network topologies,” *Physical Review E* **113** (2026), 014306, DOI: 10.1103/xps9-qqvp; public publisher release 2026-01-08; arXiv:2601.21743v1 (2026-01-29).
- J. D. Harris, E. Gallmeier, J. Dushoff, S. J. Beckett, and J. S. Weitz, “Infections are not alike: The effects of covariation between individual susceptibility and transmissibility on epidemic dynamics,” *Journal of Theoretical Biology* **613** (2025), 112211, DOI: 10.1016/j.jtbi.2025.112211. Open full text: https://drum.lib.umd.edu/bitstreams/33b27529-0a5a-4fea-bbe9-30f1579da457/download.
- M. El Khalifi, “Dependence Structure and Epidemic Outcomes in Heterogeneous SIR Models,” arXiv:2601.01549v1 (2026-01-04), https://arxiv.org/abs/2601.01549.
- K. Kawagoe, M. Rychnovsky, S. Chang, G. Huber, L. M. Li, J. Miller, R. Pnini, B. Veytsman, and D. Yllanes, “Epidemic dynamics in inhomogeneous populations and the role of superspreaders,” *Physical Review Research* **3** (2021), 033283, DOI: 10.1103/PhysRevResearch.3.033283.
- A. Nandi and L. J. S. Allen, “Stochastic two-group models with transmission dependent on host infectivity or susceptibility,” *Journal of Biological Dynamics* (2019), DOI: 10.1080/17513758.2018.1538462.
