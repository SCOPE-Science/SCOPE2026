# Exact co-location and square-root hotspot staircases for two essential Monod resources

## Finding

Consider independent identical patches with local uptake proportional to the **product** of two essential-resource Monod saturation factors. When the two available budgets are equal **after normalizing each by its own half-saturation constant**, both nutrients optimally occupy exactly the same patches, at identical normalized doses within each occupied patch. As the common budget rises, the number of occupied patches changes in a strict staircase from one to all patches, with consecutive transition budgets \(\sqrt{k(k+1)}\).

For an integer \(n\ge2\) and dimensionless budget \(T>0\), the exact maximum is
\[
U^*(n,T)=\max_{1\le k\le n}\frac{T^2k}{(T+k)^2}.
\]
The optimal number \(k\) of occupied sites is unique if \(T\) is not one of \(\sqrt{j(j+1)}\) for \(1\le j<n\); at \(T=\sqrt{k(k+1)}\), only support sizes \(k\) and \(k+1\) tie. For a selected support size \(k\), every occupied site receives \(T/k\) of **each** normalized resource, and all other sites receive zero.

For example, at \(n=3\) and \(T=1,2,3\), the optimal numbers of hotspots are respectively \(1,2,3\), with exact total uptake proxies \(1/4,1/2,3/4\). The two transitions are at \(\sqrt2\) and \(\sqrt6\).

## Assumptions and scope

There are exactly \(n\) identical, noninteracting patches, each with the same reference microbial biomass and time-independent local response. Let \(C_i,N_i\ge0\) be supplied concentrations and \(K_C,K_N>0\) be fixed Monod half-saturation constants. Set \(c_i=C_i/K_C\) and \(q_i=N_i/K_N\). Assume independent conserved budgets \(\sum_i c_i=\sum_i q_i=T>0\), i.e. a stoichiometrically balanced *normalized* supply; the two unnormalized total amounts need not be equal. The local dimensionless initial uptake proxy is
\[
\phi(c_i)\phi(q_i),\qquad\phi(t)=\frac{t}{1+t}.
\]
Thus \(U(c,q)=\sum_i\phi(c_i)\phi(q_i)\). Nutrient and carbon are both essential: if either is absent at a site, that site's contribution is zero. The theorem quantifies *all* real feasible dose vectors, not merely a finite menu or a discretized allocation. Sites may remain unfunded, and total supply is positive. The claim concerns instantaneous potential uptake with no diffusion, mortality, depletion, microbial heterogeneity, cost of placement, or time evolution.

## Proof

**Step 1: independent resources optimally coincide.** Define \(g(t)=\phi(t)^2\). At each site the exact square identity
\[
2\phi(c_i)\phi(q_i)=g(c_i)+g(q_i)-[\phi(c_i)-\phi(q_i)]^2
\]
shows
\[
U(c,q)\le\tfrac12\sum_i g(c_i)+\tfrac12\sum_i g(q_i)\le M_n(T),
\quad M_n(T)=\max_{x_i\ge0,\,\sum x_i=T}\sum_i g(x_i).
\]
Any scalar maximizer \(x\) is feasible as \(c=q=x\) and attains \(M_n(T)\), so this is the exact two-resource maximum. If a feasible pair attains the maximum, every discarded square must be zero. Because \(\phi\) is strictly increasing, it follows that \(c_i=q_i\) at every site; both vectors must then be scalar maximizers. This also proves that spatial co-location is **necessary**, not merely sufficient.

**Step 2: scalar optimum has equal positive doses.** We have
\[
g'(x)=\frac{2x}{(1+x)^3},\quad
 g'(x)-g'(y)=\frac{2(x-y)[1-xy(3+x+y)]}{(1+x)^3(1+y)^3}.
\]
Suppose two entries of a scalar maximizer are unequal and both positive. Keep their sum \(t=x+y>0\) fixed and consider \(H(u)=g(u)+g(t-u)\) for \(0\le u\le t\). On \(0<u<t/2\),
\[
\operatorname{sgn}H'(u)=-\operatorname{sgn}[1-u(t-u)(3+t)].
\]
Since \(u(t-u)\) strictly increases throughout that interval, \(H'\) can switch sign only from negative to positive. Hence there is no strict or weak local maximum with \(0<u<t/2\); the same holds by symmetry for \(t/2<u<t\). Every unequal pair of positive doses could therefore be varied, holding the budget fixed, to strictly improve the objective. This contradicts optimality. Consequently, **all positive scalar entries are equal**. If precisely \(k\) entries are positive, their common value is \(T/k\), and the objective is
\[
F_k(T)=k\,g(T/k)=\frac{T^2 k}{(T+k)^2}.
\]
Conversely each of these \(n\) support patterns is feasible, so \(M_n(T)=\max_{1\le k\le n}F_k(T)\). This argument also handles all boundary faces, including full concentration on one site.

**Step 3: support transitions and equality cases.** For adjacent integers \(k,k+1\), canceling positive factors shows
\[
F_{k+1}(T)\gtreqless F_k(T)
\quad\Longleftrightarrow\quad
T\gtreqless\sqrt{k(k+1)}.
\]
For clarity, this follows from comparing \(\sqrt{k+1}/(T+k+1)\) with \(\sqrt{k}/(T+k)\), whose cross-multiplied equality reduces to \(T=\sqrt{k(k+1)}\). Since the thresholds \(\sqrt{k(k+1)}\) strictly increase with \(k\), the finite sequence \(F_1(T),\ldots,F_n(T)\) rises up to one index and falls thereafter; at a threshold exactly two adjacent indices tie. Combining all three steps gives the asserted classification of every optimizer, including the transition ties.

**One essential resource gives a different answer.** When uptake is instead \(\sum_i\phi(c_i)\) under one fixed sum \(T\), \(\phi''(t)=-2/(1+t)^3<0\); strict Jensen concavity makes \(c_i=T/n\) for every site the unique maximum at every \(T>0\). Thus the support staircase is a consequence of essential-resource complementarity, not the individual Monod saturation law alone.

## Verification

The standalone `check.py` uses only the Python standard library. It checks the square identity and two-dose derivative formula with exact rational arithmetic, checks all adjacent support-score inequalities over a rational parameter grid, exhaustively compares independently chosen carbon and nutrient allocations on finite rational meshes in up to four patches, and checks exact small-budget examples. Nineteen supplementary square-root tie computations are numerical. Running `python check.py` on the attached source completed 60,282 assertions. These tests corroborate the algebra and examples; the proof above, not finite enumeration, establishes the universal assertion for every real dose vector and arbitrary integer \(n\ge2\).

## Relationship to prior work

Endress et al. (2024) examined experimentally and dynamically modeled heterogeneously supplied glucose, nutrient limitation, and microbial growth; their growth kinetics use two essential substrates with Monod-type response. Shi et al. (2021) investigated experimentally one, two, or four glucose-fed compartments, but did not jointly optimize two freely allocated resource budgets. These studies motivate the static benchmark; neither is claimed to validate the response under field conditions. The general mathematical problem of allocating resources to sigmoidal utilities long predates this calculation (Vicentini, 1970; Udell and Boyd, 2015). The scalar objective \(g(t)=\phi(t)^2\) is sigmoidal. The specific additional claim is an exact **two-independent-budget co-location theorem** followed by a complete closed-form global optimizer and strict square-root support-switch law; it is not a claim that generic sigmoidal allocation was first discovered here.

## Limitations

The two total budgets must be equal **in normalized Monod units**. Heterogeneous patch capacities, unequal normalized resource totals, different kinetics, spatial diffusion, nutrient replenishment, oxygen effects, substrate depletion, varying microbial biomass, and costs of targeting are outside the theorem. The benchmark optimizes **instantaneous potential uptake**, not cumulative respiration, crop yields or microbial biomass. Generic earlier S-shaped utility-allocation research may imply parts of the scalar reduction; a relevant older report was accessible only as an abstract, so priority over that literature remains uncertain. No independent external validation has been performed.

## References

1. Endress, M.-G., Dehghani, F., Blagodatsky, S., Reitz, T., Schlüter, S. and Blagodatskaya, E. (2024). *Spatial substrate heterogeneity limits microbial growth as revealed by the joint experimental quantification and modeling of carbon and heat fluxes*. *Soil Biology and Biochemistry* 197, 109509. First online 28 June 2024. https://doi.org/10.1016/j.soilbio.2024.109509
2. Shi, A., Chakrawal, A., Manzoni, S., Fischer, B.M.C., Nunan, N. and Herrmann, A.M. (2021). *Substrate spatial heterogeneity reduces soil microbial activity*. *Soil Biology and Biochemistry* 152, 108068. First online 18 November 2020. https://doi.org/10.1016/j.soilbio.2020.108068
3. Khurana, S. and collaborators (2022). *Predicting the impact of spatial heterogeneity on microbially mediated nutrient cycling in the subsurface*. *Biogeosciences* 19, 665–688. https://doi.org/10.5194/bg-19-665-2022
4. Vicentini, F.M. (1970). *On the Resource Allocation Problem with S-Shaped Utility Functions*. Technical Memorandum 201, Case Western Reserve University. https://commons.case.edu/wsom-ops-reports/370/
5. Udell, M. and Boyd, S. (2015). *Maximizing a Sum of Sigmoids*. https://web.stanford.edu/~udell/doc/max_sum_sigmoids.pdf
