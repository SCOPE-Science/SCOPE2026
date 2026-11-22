# One downstream reversal in a lateral-diffusion and mortality tradeoff

## Finding

**Theorem (complete two-design classification and sharp crossover scales).** Fix a lateral crossing distance \(w>0\). For each design \(i\in\{1,2\}\), let a larva travel downstream at a deterministic speed \(v_i>0\), disperse laterally as \(X_i(t)=\sqrt{2D_i}\,B_i(t)\) with \(D_i>0\) and standard Brownian motion \(B_i\), and have an independent exponential mortality clock of rate \(\mu_i>0\). A larva reaching the downstream nursery gate at distance \(L>0\) qualifies if its **lateral position at that arrival time** is on the nursery side \(X_i(L/v_i)\ge w\) and it has survived the entire travel time. Set
\[
\alpha_i=\frac{\mu_i}{v_i}>0,\qquad
\beta_i=w\sqrt{\frac{v_i}{4D_i}}>0.
\]
The exact successful-delivery probability is
\[
P_i(L)=\frac12e^{-\alpha_iL}\operatorname{erfc}\!\left(\frac{\beta_i}{\sqrt L}\right).
\]
If \(\alpha_1\le\alpha_2\) and \(\beta_1\le\beta_2\), with at least one inequality strict, design 1 is strictly better for every \(L>0\). Reversing both inequalities reverses the dominance. When the rankings conflict, there is **exactly one** positive crossover distance. Specifically, if
\[
\beta_1<\beta_2,\qquad \delta:=\alpha_1-\alpha_2>0,
\]
there exists exactly one \(L_*(\delta,\beta_1,\beta_2)>0\) with \(P_1(L_*)=P_2(L_*)\), and \(P_1>P_2\) strictly before it, \(P_1<P_2\) strictly after it. The crossing is transversal, with the logarithmic probability ratio strictly decreasing in \(L\). At fixed \(\beta_1<\beta_2\), \(L_*\) strictly decreases as \(\delta\) increases; at fixed positive \(\delta\), it decreases with \(\beta_1\) and increases with \(\beta_2\). The scales are sharp:
\[
L_*\sim\left(\frac{2(\beta_2-\beta_1)}{\sqrt\pi\,\delta}\right)^{2/3}
\quad(\delta\downarrow0),\qquad
L_*\sim\sqrt{\frac{\beta_2^2-\beta_1^2}{\delta}}
\quad(\delta\to\infty).
\]
In the opposite conflicting case \(\beta_2<\beta_1\) and \(\alpha_2>\alpha_1\), interchange the indices. If both effective parameter pairs coincide, the probabilities coincide at every distance. Equalities in only one coordinate produce strict all-distance dominance by the other coordinate, not an isolated crossover.

## Assumptions and scope

All quantifiers are over real \(w,L,v_i,D_i,\mu_i>0\). The lateral process is Brownian motion on the full real line, with **no reflecting outer bank or finite-width cross-section**. Arrival downstream is deterministic at \(L/v_i\); settlement eligibility is tested by **final lateral position at that downstream gate**, not by prior first crossing. The independent survival clock is required to exceed the full downstream travel time. Design comparisons are for equal initial numbers of larvae and identical nursery viability. A design is held fixed while downstream distance varies. The normalization of diffusion is \(\operatorname{Var}(X_i(t))=2D_it\); changing it changes the factors of four in \(\beta_i\).

## Proof

**1. Exact probability.** At time \(t>0\), \(X_i(t)\) is centered normal with variance \(2D_it\). Hence
\[
\Pr\{X_i(t)\ge w\}=\frac12\operatorname{erfc}\!\left(\frac{w}{\sqrt{4D_it}}\right).
\]
The independent exponential survival clock exceeds \(t\) with probability \(e^{-\mu_it}\). Substitute \(t=L/v_i\) and multiply to obtain \(P_i(L)\). It is strictly decreasing in each of \(\alpha_i\) and \(\beta_i\) at fixed \(L>0\). This immediately proves coordinatewise dominance and handles all equalities.

**2. Strict single-crossing lemma.** Suppose \(0<\beta_1<\beta_2\), \(\delta>0\), and define the logarithmic ratio
\[
J(L)=\log\frac{P_1(L)}{P_2(L)}
=-\delta L+\log\operatorname{erfc}(\beta_1/\sqrt L)
-\log\operatorname{erfc}(\beta_2/\sqrt L).
\]
For \(z>0\) set \(Q(z)=z e^{-z^2}/\operatorname{erfc}(z)\). The integral representation and strict comparison \(t/z>1\) for \(t>z\) give
\[
\operatorname{erfc}(z)=\frac2{\sqrt\pi}\int_z^\infty e^{-t^2}\,dt
<\frac{e^{-z^2}}{\sqrt\pi\,z}.
\]
Therefore \(e^{-z^2}/(\sqrt\pi\operatorname{erfc}(z))>z\). Differentiating yields
\[
\frac{Q'(z)}{Q(z)}
=\frac1z-2z+\frac{2e^{-z^2}}{\sqrt\pi\operatorname{erfc}(z)}
>\frac1z>0.
\]
Consequently, for every \(L>0\),
\[
J'(L)=-\delta+\frac{Q(\beta_1/\sqrt L)-Q(\beta_2/\sqrt L)}{\sqrt\pi\,L}
<-\delta<0.
\]
The standard Gaussian-tail asymptotics, also obtained by one integration by parts, yield
\[
J(L)=\frac{\beta_2^2-\beta_1^2}{L}
+\log\frac{\beta_2}{\beta_1}-\delta L+O(L)
\quad(L\downarrow0),
\]
and
\[
J(L)=-\delta L+\frac{2(\beta_2-\beta_1)}{\sqrt{\pi L}}
+O(L^{-1})\quad(L\to\infty).
\]
Thus \(J\) runs strictly from \(+\infty\) to \(-\infty\), crossing zero once with nonzero derivative. The signs give the stated ranking. Interchanging designs handles the other conflict case.

**3. Comparative statics.** At the crossing, \(J_L<0\). The partial derivatives of \(J\) in \(\delta,\beta_1,\beta_2\) are respectively negative, negative, positive. Implicit differentiation of \(J(L_*)=0\) gives the three claimed strict monotonicities.

**4. Both sharp scales.** At fixed \(0<\beta_1<\beta_2\), the identity \(J(L_*)=0\) and monotonicity imply \(L_*\to\infty\) as \(\delta\downarrow0\). Using the large-distance expansion,
\[
\delta L_*^{3/2}\longrightarrow
\frac{2(\beta_2-\beta_1)}{\sqrt\pi},
\]
which is exactly the first equivalence. Similarly \(L_*\to0\) as \(\delta\to\infty\), and the short-distance expansion yields
\[
\delta L_*^2\longrightarrow\beta_2^2-\beta_1^2,
\]
which gives the second equivalence. Both leading constants are attained in these limiting parameter regimes, so neither scaling constant can be uniformly improved.

## Verification

The accompanying standalone \(\texttt{check_crossing.py}\) uses only the Python standard library and can be run by `python check_crossing.py`. It computes crossover distances using monotone bisection on the logarithmic probabilities, avoids numerical Gaussian-tail underflow using a controlled large-argument expansion, and tests 1,000 randomly chosen strict-tradeoff parameter triples, sampled sign patterns, monotone ratio sequences, mortality-gap comparative statics, four weak-penalty and four strong-penalty asymptotic cases. It completed 38,011 supplementary checks. For \((\beta_1,\beta_2,\alpha_1,\alpha_2)=(1,2,0.5,0.1)\),
\[
L_*\approx 3.265197133263,\qquad P_1(L_*)=P_2(L_*)\approx0.042390783238.
\]
These finite tests are not a proof for all positive parameters; the strict monotonicity and limiting arguments above supply that proof. All decimal values are illustrations, not independently certified interval bounds.

## Relationship to prior work

Farò and Wolter (2024) explicitly integrate two-dimensional larval drift into spawning-to-nursery connectivity analysis and report limited lateral access in a channelized river. Meyer, Hastings and Largier (2021) study the interplay of mortality, mixing and settlement with spatially heterogeneous coastal habitat; their model can show nonmonotone dependence on diffusivity. These are biological motivations and broader mechanistic contexts, not the present fixed-design, variable-downstream-reach classification. The Gaussian tail formula, Gaussian Mills inequality and \(\operatorname{erfc}\) asymptotics are classical and not claimed as new. A published analysis of advective first-passage distributions compares two **first-arrival** CDFs at a common time, without independent survival multipliers; it does not entail this ranking of \(e^{-\alpha L}\operatorname{erfc}(\beta/\sqrt L)\) at variable longitudinal distances with independent time-to-arrival rules. The contribution here is the complete one-crossing classification of this ecology-motivated **terminal-location-plus-survival** observable, its strict comparative statics, and two different sharp crossover exponents; no priority beyond inspected sources is certified.

## Limitations

Real river larval transport is not an unbounded lateral Brownian motion: finite channel boundaries, heterogeneous velocities, turbulence, directed swimming, delayed competence, variable mortality, and nursery geometry can destroy the stated formula and therefore the one-crossing conclusion. No measured parameter calibration or intervention recommendation is claimed. The output compares probabilities of being on the target side of a downstream transect and alive, not first-passage nursery capture, population persistence, or long-term reproductive value. A general uninspected theorem on products of error-function tails and exponential survival could already imply the comparison; historical priority is limited to the cited and searched literature.

## References

1. D. Farò and C. Wolter, *Integrating Habitat Suitability and Larval Drift Modeling for Spawning-To-Nursery Functional Habitat Connectivity Analysis in Rivers*, Water Resources Research 60 (2024), e2023WR036827, first public 2024-09-16, https://doi.org/10.1029/2023WR036827 .
2. A. D. Meyer, A. Hastings and J. L. Largier, *Spatial heterogeneity of mortality and diffusion rates determines larval delivery to adult habitats for coastal marine populations*, Theoretical Ecology 14 (2021), 525–541, https://doi.org/10.1007/s12080-021-00512-y .
3. NIST Digital Library of Mathematical Functions, §§7.9 and 7.12, Gaussian-tail ratio identities and asymptotics, https://dlmf.nist.gov/7.12 .
4. D. E. Amos, *Bounds on Iterated Coerror Functions and Their Ratios*, Mathematics of Computation 27 (1973), 413–427 (first sections on Gaussian tail ratios; inspected in parsed text), https://doi.org/10.2307/2005632 .
5. *Sharp arrival-order crossover and vanishing-drift scaling for advective tracer passage*, publicly available mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-arrival-order-crossover-and-vanishing-drift-scaling-for-ad--620a5e737e4d .
