# Two-versus-four exposure windows for hidden coexistence in first-arrival ecology

## Finding

**Theorem (sharp exposure-window identification law).** Consider a resource that may be available to two species, A and B, with unknown joint site-availability probabilities \(\pi_{00},\pi_{10},\pi_{01},\pi_{11}>0\) summing to one. If present, each species has an independent exponential time to first discovery with the **same unknown rate** \(r>0\). A resource is consumed by the first discovering species; if neither is present, it is never discovered. For a fixed known \(T>0\), suppose exact probabilities of the three recorded labels—A wins, B wins, or no arrival—are available separately at exposure deadlines \(jT\), for selected positive integers \(j\), but exact event times are not recorded.

Define the two marginal availability probabilities \(u=\pi_{10}+\pi_{11}\) and \(v=\pi_{01}+\pi_{11}\). Then:

1. If \(u\ne v\), just the two deadlines \(T,2T\) uniquely recover \(r\) and all four latent probabilities. One deadline never suffices uniformly in the strictly positive parameter space.
2. If \(u=v\), four deadlines \(T,2T,3T,4T\) uniquely recover all parameters. Two deadlines admit a local continuum of alternatives at every strictly interior balanced parameter point. Three deadlines **do not suffice uniformly**: there are strictly positive pairs of models with different rates, opposite signs of latent species association, and exactly the same first-arrival labels at all three deadlines.
3. Thus four equally spaced deadlines are sufficient for **every** strictly positive joint availability table and are sharply necessary for a uniform guarantee, while two suffice off the balanced-marginal hypersurface. This is a statement of **population structural identifiability**, not of finite-sample estimation precision.

An exact three-deadline ambiguity has \(z=e^{-rT}\) and \((\pi_{00},\pi_{10},\pi_{01},\pi_{11})\) equal respectively to
\[
\left(\frac12;\frac9{50},\frac{33}{100},\frac{33}{100},\frac4{25}\right),\qquad
\left(\frac35;\frac{43}{256},\frac{11}{64},\frac{11}{64},\frac{125}{256}\right).
\]
For **both** models, the probability that A wins by the first three deadlines, and equally that B wins, is
\[
\left(\frac9{40},\frac{129}{400},\frac{147}{400}\right).
\]
Nonetheless their latent occupancy covariances \(\pi_{11}-uv\) are respectively \(-801/10000\) and \(3439/65536\): the observed three-window laws cannot even determine whether the two species tend to avoid or co-occur. The fourth-window A-winning probabilities are, respectively, \(249/640\) and \(9741/25000\), which differ by \(231/400000\).

## Assumptions and scope

Each experimental resource has a time-independent latent pair of species-availability indicators \((I_A,I_B)\) distributed according to the above \(2\times2\) table. Availability may be positively associated, negatively associated, or independent. Conditional on joint availability, first-discovery clocks of present species are independent and identically distributed as \(\operatorname{Exp}(r)\); an absent species has infinite discovery time. First consumption removes the resource. The recorded event is the winner's identity if arrival occurred no later than the assigned deadline, otherwise the label 'none'. Independent resource replicates may be assigned to the different deadlines. Equality of the two conditional discovery rates is an assumption; no equivalence to general competing-risk or dependence models is asserted. All model probabilities are exact theoretical population quantities.

Let \(A_j\) and \(B_j\) be the cause-specific cumulative first-arrival probabilities at \(jT\), and put \(z=e^{-rT}\in(0,1)\) and \(F_j=1-z^j\). The basic observation law is
\[
A_j=uF_j-\frac{\pi_{11}}2F_j^2,\qquad
B_j=vF_j-\frac{\pi_{11}}2F_j^2.
\]
The third probability is \(1-A_j-B_j\). This assumes that the labels distinguish A from B; a pooled 'any species' indicator is a different experiment.

## Proof

**Observation law.** If only A is present, A wins before \(t\) with probability \(1-e^{-rt}\). If both are present, symmetry of the two independent exponential clocks gives probability \((1-e^{-2rt})/2\) that A wins by \(t\). Therefore
\[
 A_j=\pi_{10}F_j+\frac{\pi_{11}}2(1-z^{2j})
 =(\pi_{10}+\pi_{11})F_j-\frac{\pi_{11}}2F_j^2.
\]
The B formula is analogous. This derivation does not assume independence of the two latent availability indicators.

**Unbalanced inversion.** If \(u\ne v\), define \(D_j=A_j-B_j\). Since \(D_j=(u-v)(1-z^j)\), we have \(D_1\ne0\) and
\[
 z=\frac{D_2}{D_1}-1,\qquad r=-\frac{\log z}{T}.
\]
With \(F_1=1-z\), \(F_2=1-z^2\), solve
\[
 q:=\pi_{11}=\frac{2}{F_2-F_1}
 \left(\frac{A_1}{F_1}-\frac{A_2}{F_2}\right),
 \quad u=\frac{A_1}{F_1}+\frac{qF_1}{2},
 \quad v=\frac{B_1}{F_1}+\frac{qF_1}{2}.
\]
Finally \(\pi_{10}=u-q\), \(\pi_{01}=v-q\), and \(\pi_{00}=1-u-v+q\). Every denominator is nonzero in the stated interior domain. Hence the inverse is unique.

**Balanced inversion.** If \(u=v\), the two winning probabilities agree at every time. Write \(A_0=0\) and \(b_j=A_j-A_{j-1}\) for \(j=1,2,3,4\). With \(d=\pi_{10}=\pi_{01}>0\) and \(q=\pi_{11}>0\), the observation law yields
\[
 b_j=c z^{j-1}+e z^{2(j-1)},\qquad
 c=d(1-z)>0,\qquad e=\frac q2(1-z^2)>0.
\]
Consequently
\[
 \Delta:=b_1b_3-b_2^2=ce(z-z^2)^2>0,
\]
and the sequence obeys \(b_{j+2}=(z+z^2)b_{j+1}-z^3b_j\). Eliminating \(z^3\) from the two available recurrence equations gives
\[
 S:=\frac{b_1b_4-b_2b_3}{b_1b_3-b_2^2}=z+z^2,
 \qquad z=\frac{\sqrt{1+4S}-1}{2}.
\]
The map \(z\mapsto z+z^2\) is strictly increasing for \(z>0\), so \(z\) is unique. Moreover,
\[
 c=\frac{b_2-z^2b_1}{z-z^2},\quad
 e=\frac{zb_1-b_2}{z-z^2},\quad
 d=\frac{c}{1-z},\quad
 q=\frac{2e}{1-z^2}.
\]
These reconstruct the full table as \((\pi_{00},\pi_{10},\pi_{01},\pi_{11})=(1-2d-q,d,d,q)\), and the rate as before. The positive determinant rules out any singularity for strictly positive tables.

**Sharpness.** For one deadline, choose a nearby different \(z\) and \(q\); the two observed probabilities then determine \(u\) and \(v\), leaving a local family of strictly positive tables because positivity is open. On the balanced stratum, the same argument using \(A_1=A_1(z,u,q)\) and \(A_2=A_2(z,u,q)\) gives a continuum when \(z\) varies near any interior point: the corresponding two linear equations in \(u,q\) are nonsingular because \(F_1\ne F_2\). To rule out a universal three-window identification, substitute the two explicit rational models in the theorem into the observation formula. Each gives \(A_1=B_1=9/40\), \(A_2=B_2=129/400\), and \(A_3=B_3=147/400\), but their rates and the signs of \(\pi_{11}-uv\) differ. All four table entries are strictly positive and sum to one in both cases. Their fourth-window probabilities are different. Thus three windows cannot provide a uniform guarantee and four is sharp. \(\square\)

## Verification

Run `python check.py` with Python 3 and no external dependencies. The checker exactly verifies both rational probability tables, all three shared winner-label distributions, opposite exact covariance signs, and the nonzero fourth-window separation. It additionally performs 10,000 seeded randomized balanced four-window inverse tests and more than 9,000 seeded unbalanced two-window inverse tests in floating point. These numerical trials supplement, but do not replace, the algebraic proof of global identifiability. No empirical field data, confidence interval, or claim about finite-sample performance is supplied.

## Relationship to prior work

Nakashima, Hashizume, and Kanda (2024) develop a time-to-detection model for two species competing to use ephemeral resources, treating rival use as censoring. Their formulation motivates first-consumer observations; their independent-species modeling and time-resolved likelihood are not the joint-availability, winner-label-only, multiple-fixed-deadline inverse problem analyzed here. Ferry et al. (2024) analyze recurrent camera-trap events, rather than the first-consumer endpoint experiment. Chambert et al. (2018) analyze two-species occupancy and misidentification with confirmatory records; Lonsinger (2022) analyzes closure-related co-occurrence bias. Koley and Dewanji (2021, 2023) study current-status competing risks and missing types, providing a related statistical class but not an inspected proof of these sharp window thresholds. The four-window exponential reconstruction uses the classical Hankel/Prony idea (see Plonka and Tasche, 2014); the present narrow contribution is the ecology-specific minimal-window dichotomy and an explicit **opposite-association** three-window alias, not the invention of Prony reconstruction or competing-risk models.

## Limitations

The theorem requires exactly two potentially competing species; strict positivity of all latent table cells; equal, constant, unknown conditional exponential discovery rates; independent clocks conditional on availability; and known integer-multiple deadlines. The results describe structural identifiability at exact population probabilities, not stable statistical recovery under noise. In particular, the unbalanced two-window inverse is ill-conditioned near \(u=v\), and the balanced four-window Hankel determinant shrinks near zero coefficients or extreme rates. Species encounters may be non-exponential, rate-heterogeneous, behaviorally dependent, or subject to environmental censoring. No inference about actual species competition, causation, or management intervention is justified without validating the model. General latent competing risks need not be identifiable without parametric assumptions. A full priority search cannot conclusively rule out a mathematically equivalent result elsewhere.

## References

- Nakashima, Y., Hashizume, A., and Kanda, A. (2024). *A statistical approach to assess interspecific consumptive competition and functional redundancy in ephemeral resource uses using camera traps*. Ecology and Evolution 14, e70031. First published 2024-07-24. https://doi.org/10.1002/ece3.70031
- Ferry, N., Dupont, P., Bender, A., and Heurich, M. (2024). *Introducing recurrent event analyses to assess species interactions based on camera-trap data*. Methods in Ecology and Evolution 15, 1233–1246. https://doi.org/10.1111/2041-210X.14338
- Chambert, T. et al. (2018). *Two-species occupancy modelling accounting for species misidentification and non-detection*. Methods in Ecology and Evolution 9, 1468–1477. https://doi.org/10.1111/2041-210X.12985
- Lonsinger, R. C. (2022). *Co-occurrence models fail to infer underlying patterns of avoidance and aggregation when closure is violated*. Ecology and Evolution 12, e9104. https://doi.org/10.1002/ece3.9104
- Koley, T., and Dewanji, A. (2021). *Current status data with two competing risks and missing failure types: a parametric approach*. Journal of Applied Statistics. https://doi.org/10.1080/02664763.2021.1881453
- Koley, T., and Dewanji, A. (2023). *Current status data with two competing risks and time-dependent missing failure types*. Journal of Applied Statistics. https://doi.org/10.1080/02664763.2023.2231174
- Plonka, G., and Tasche, M. (2014). *Prony methods for recovery of structured functions*. GAMM-Mitteilungen 37, 239–258. https://doi.org/10.1002/gamm.201410011
