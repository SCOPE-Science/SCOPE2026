# Sharp finite-dose identifiability of waning immunity in an age-structured SIRVS model

## Finding
Consider the endemic equilibrium in the non-Markovian susceptible–infected–recovered–vaccinated–susceptible (SIRVS) model of Yang, Saldaña and Scoglio [1]. Assume the reproduction number \(R>1\), mean infectious duration \(a>0\), and mean vaccine-induced immunity duration \(b>0\) are known. Let the recovered-immunity survival function be \(S(t)\), and let \(\Phi(v)>0\) denote the equilibrium force of infection under a constant vaccination rate \(v\in(0,(R-1)/b)\). The response determines the transformed recovery-immunity duration exactly:
\[
K(v):=\int_0^\infty e^{-vt}S(t)\,dt
=\frac{(R-1-bv)/\Phi(v)-a}{1+bv}.
\]

**Sharp finite-dose identification.** Suppose recovered-immunity durations have a hyperexponential law with at most \(k\) distinct positive rates: \(S(t)=\sum_{j=1}^{r}p_j e^{-\lambda_jt}\), where \(1\le r\le k\), \(p_j>0\), \(\sum_j p_j=1\), and \(\lambda_j>0\) are pairwise distinct. The values of \(\Phi\) at **any \(2k-1\) distinct subcritical positive vaccination rates** uniquely determine every component rate and weight, up to permutation. This number is optimal in the following strong sense: for each \(k\ge2\), any collection of only \(2k-2\) distinct subcritical rates admits a continuous family of distinct exactly \(k\)-component hyperexponential immunity laws with identical responses at every observed rate, even with \(R,a,b\) fixed. For \(k=1\), one rate is necessary and sufficient.

**Unrestricted-law boundary.** On the larger class of smooth strictly positive recovered-immunity densities with finite mean and smooth strictly positive waning hazard, equality of the complete response curves on any nonempty open subinterval of the endemic vaccination range forces equality of the recovery-duration laws. In contrast, for every finite set of positive subcritical rates there are distinct such smooth laws with identical responses at those rates **and the same mean immunity duration**. Thus no finite number of exact endemic measurements identifies a general waning distribution without a finite-dimensional assumption.

These assertions concern exact equilibrium observations and known \(R,a,b\). They are not statements about finite noisy data, transient infection observations, stability of inverse recovery, or the feasibility of experimentally maintaining infinitely many equilibria.

## Assumptions and scope
Take the original age-structured SIRVS equations [1], with a closed well-mixed population, vaccination of susceptible and recovered individuals at identical constant rate \(v\), vaccine-induced immunity loss according to a fixed distribution of finite positive mean \(b\), arbitrary admissible age-dependent infectivity and recovery with reproduction number \(R\) and mean infectious duration \(a\), and recovered-immunity duration \(T\) with \(S(t)=\Pr(T>t)\). We require the ordinary equilibrium formula of [1] and the endemic range \(0<v<(R-1)/b\). For the hyperexponential theorem, \(S(t)=\sum_jp_j e^{-\lambda_jt}\); it has continuous positive hazard \(\delta(t)=-S'(t)/S(t)\) and belongs to the original model. The general-law theorem restricts to smooth positive densities with positive smooth hazards and finite means, so it also remains inside that model. No atomic duration distribution is required in either theorem. The integer \(k\ge1\) is an a priori upper bound on the *number of distinct exponential-rate components*, not on the number of agents, infection compartments or measured time points.

## Proof
**1. Equilibrium transform.** The positive-equilibrium relation, derived in [1, Eq. (4)], is
\[
\Phi(v)=\frac{R-1-bv}{a+(1+bv)K(v)},\qquad
K(v)=\int_0^\infty\exp(-vt)S(t)\,dt.
\]
Indeed, the infected boundary flux is \(S^*\Phi\), the endemic susceptible fraction is \(1/R\), the infected compartment size is its boundary flux times \(a\), the recovered size is its boundary flux times \(K(v)\), and the vaccinated size is the vaccination influx times \(b\). Mass conservation gives this displayed identity. Its denominator is positive in the specified range, so it can be inverted pointwise for \(K(v)\) as stated.

**2. Sufficiency at \(2k-1\) doses.** In the hyperexponential subclass,
\[
K(v)=\sum_{j=1}^{r}\frac{p_j}{v+\lambda_j}.
\]
Suppose two laws with at most \(k\) components agree at \(2k-1\) distinct positive vaccination rates. Put the two rational functions over the product of their denominators (degree at most \(2k\)). The numerator of their difference has degree at most \(2k-2\): the leading terms in their large-\(v\) expansions both equal \(1/v\) because each set of weights sums to one, so the \(1/v\) term cancels. A nonzero polynomial of degree at most \(2k-2\) cannot vanish at \(2k-1\) distinct points. Therefore the rational functions coincide identically. Their simple poles at the negative component rates and their residues determine the distinct rates \(\lambda_j\) and positive weights \(p_j\) uniquely, up to component ordering. This argument covers unknown actual component count \(r\le k\).

**3. Sharp necessity within the hyperexponential subclass.** Fix any \(k\ge2\), any \(m=2k-2\) distinct vaccination rates \(v_1,\ldots,v_m>0\), and one interior parameter vector with \(k\) distinct rates \(\lambda_i>0\) and positive weights \(p_i\). Regard the \(2k\) unconstrained coordinates as the weights and rates and define
\[
F_0=\sum_{i=1}^{k}p_i,\qquad
F_j=\sum_{i=1}^{k}\frac{p_i}{v_j+\lambda_i}\quad(1\le j\le m).
\]
The Jacobian of these \(m+1=2k-1\) functions has full row rank. Otherwise a nonzero linear combination of its rows yields coefficients \(a_0,\ldots,a_m\) and a rational function \(Q(x)=a_0+\sum_{j=1}^m a_j/(v_j+x)\) with both \(Q(\lambda_i)=0\) and \(Q'(\lambda_i)=0\) for every \(i\) (the weight-column and rate-column equations). Multiplication by \(\prod_{j=1}^m(v_j+x)\) produces a polynomial of degree at most \(m<2k\) with \(k\) distinct double zeros, so it must vanish identically. Distinct poles then force every \(a_j=0\), a contradiction. By the implicit-function theorem, the level set of these \(2k-1\) constraints is locally a smooth one-dimensional manifold through the chosen parameters. In a sufficiently small neighborhood, all weights remain positive, rates remain distinct and positive, and their ordering can be fixed. Hence infinitely many genuinely different \(k\)-component laws have the same normalization and the same \(m\) observations. For fewer observations, select a subset of these constraints. When \(k=1\), \(K(v)=1/(v+\lambda)\) identifies \(\lambda\) from one observation but normalization alone does not.

**4. An open dose interval identifies an unrestricted law.** Integration by parts gives the Laplace transform of the recovered-immunity duration distribution:
\[
L(v):=\mathbb E[e^{-vT}]=1-vK(v)\qquad(v>0).
\]
The function \(L\) is analytic on the complex right half-plane. If two exact response curves agree on an open interval within the endemic range, their \(K\), and hence \(L\), agree there. The identity theorem makes the Laplace transforms equal at every real \(v>0\). To recover the law without invoking an inverse-integral formula, set \(X=e^{-T}\in(0,1]\). Then the transforms at positive integers give all moments \(\mathbb E[X^n]\), while normalization gives the zeroth moment. Polynomials are dense in continuous functions on \([0,1]\), so the probability law of \(X\), and hence that of \(T\), is unique.

**5. Every finite dose panel leaves smooth laws indistinguishable.** Fix arbitrary \(m\ge1\) subcritical rates \(v_1,\ldots,v_m\). Choose \(m+3\) nonzero \(C^\infty\) nonnegative bump functions \(b_j\) with pairwise disjoint supports strictly inside \((1,2)\). Form the real \((m+2)\)-by-\((m+3)\) matrix whose rows are the integrals of \(b_j(t)\), \(t b_j(t)\), and \(e^{-v_i t}b_j(t)\) for each \(i\). A nonzero null vector exists. Let \(h\) be the corresponding nonzero signed smooth combination of bumps. For sufficiently small \(\varepsilon>0\), the functions \(f_{\pm}(t)=e^{-t}\pm\varepsilon h(t)\) are distinct strictly positive smooth probability densities on \([0,\infty)\). They have identical means and identical Laplace transforms at all \(v_i\). Their survival functions remain positive, their hazards \(f_{\pm}/S_{\pm}\) are positive and smooth, and beyond \(t=2\) both coincide with the unit exponential hazard. Consequently they are fully admissible in the model, have equal transformed \(K(v_i)\) and exact endemic responses \(\Phi(v_i)\), but different immunity laws.

**6. Infectiousness information is fundamentally distinct.** The source equilibrium relation itself depends on the infectivity profile only through \(R\) and \(a\). For example, fix a constant recovery hazard \(1/a\), any \(R>1\), and contact rate \(c>2R/a\). The two admissible infectivity profiles \(\beta_1(t)=R/(ca)\) and \(\beta_2(t)=2Re^{-t/a}/(ca)\) yield respective intrinsic generation-time densities \(e^{-t/a}/a\) and \(2e^{-2t/a}/a\). Both have the same \(R\) and \(a\), and therefore give exactly the same entire equilibrium vaccination response for any chosen recovered-immunity law. The response can identify the immunity distribution as above but cannot distinguish these infection-generation profiles.

## Verification
The standalone `check.py` verifies an exact rational example of two different duration laws whose normalizations, means and Laplace values at two rates coincide; it checks the algebraic recovery of the transformed duration from endemic force of infection, and tests the stated infectivity-profile distinction. The analytic results above do not depend on this finite example. The critical uniqueness lemma is the cancellation of the leading rational-transform coefficient in Step 2; the critical nonuniqueness lemma is the confluent-Cauchy/double-root Jacobian argument in Step 3. Both are proved in full above. Verification requires Python 3 and its standard library; invoke `python3 check.py` alongside this document.

## Relationship to prior work
Yang, Saldaña and Scoglio [1] formulate the full age-structured SIRVS model and derive the forward endemic response formula, which is explicitly credited and not claimed as new. Their work stresses transient differences across generation-time distributions, but does not develop an inverse vaccination-panel identifiability theorem. The present contribution is the sharp \(2k-1\) exact-dose identification/ambiguity boundary for hyperexponential waning, its general smooth-law impossibility at any finite panel, and the contrast with complete-curve identification. Classical uniqueness of Laplace transforms and rational partial-fraction techniques are used rather than claimed as new. Alahakoon, McCaw and Taylor [2] address inference of waning rates from stochastic outbreak time series, not exact equilibria sampled at controlled vaccination rates. El Khalifi and Britton [3] study gradual immunity decay and vaccination demands rather than the forward/inverse dose-panel boundary of [1].

## Limitations
All identification claims are *structural* and assume noiseless, exact equilibria, known model coefficients \(R,a,b\), and an unchanged recovered-immunity law as vaccination policy varies. They do not bound statistical sample sizes, condition numbers, the time needed to reach equilibria, or sensitivity to uncertain coefficients. Hyperexponential count \(k\) is an assumed upper bound and represents a finite-dimensional subclass; exact reconstruction does not automatically yield a numerically stable algorithm when rates are close. The finite-panel nonidentifiability of general smooth laws remains even with known mean immunity, but additional parametric information or direct transient measurements can change the inference problem. No claim of uniqueness for unknown \(R,a,b\) is made.

## References
[1] Q. Yang, J. Saldaña, and C. Scoglio, "Generalized epidemic model incorporating non-Markovian infection processes and waning immunity," arXiv:2303.15326, first posted 2023-03-27; Phys. Rev. E 108, 014405 (2023). https://arxiv.org/abs/2303.15326 ; https://doi.org/10.1103/PhysRevE.108.014405

[2] P. Alahakoon, J. M. McCaw, and P. G. Taylor, "Improving estimates of waning immunity rates in stochastic SIRS models with a hierarchical framework," Infectious Disease Modelling 8 (2023), 1127–1137. https://doi.org/10.1016/j.idm.2023.10.002

[3] M. El Khalifi and T. Britton, "Extending susceptible-infectious-recovered-susceptible epidemics to allow for gradual waning of immunity," Journal of the Royal Society Interface 20 (2023), 20230042. https://doi.org/10.1098/rsif.2023.0042
