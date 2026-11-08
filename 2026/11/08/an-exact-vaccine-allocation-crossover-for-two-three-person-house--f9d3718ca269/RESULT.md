# An exact vaccine-allocation crossover for two three-person households

## Finding

**Theorem.** Consider two identical, isolated households, each initially containing three susceptible people. Exactly two perfectly effective prophylactic vaccine doses are used, in any integer allocation. Vaccinated individuals and their incident contacts are removed. Each remaining individual independently acquires an externally introduced infection with probability \(s\), and each remaining undirected contact edge in the household's complete graph is independently capable of transmitting infection with probability \(p\). The final infected set consists of all connected components of the open-edge contact graph containing at least one introduced infection. Assume \(0<p<1\) and \(0<s<1\). Minimize the expected total number of infected people, counting introduced infections.

There are only two allocation types up to interchange of households: **split** (one dose in each household, leaving two susceptible individuals in each), and **concentrated** (two doses in one household, leaving one and three susceptible individuals). Let \(E_{\mathrm{split}}\) and \(E_{\mathrm{conc}}\) denote their expected total final infection counts. Then

\[
E_{\mathrm{conc}}-E_{\mathrm{split}}
=ps(1-s)\bigl[2+6p-6p^2-ps(9-6p)\bigr].
\]

If \(0<p\le 2/3\), splitting is uniquely optimal up to within-household and between-household symmetries. If \(2/3<p<1\), define

\[
s_*(p)=\frac{2+6p-6p^2}{9p-6p^2}.
\]

Then \(2/3<s_*(p)<1\), the curve \(s_*(p)\) decreases strictly from \(1\) (at its left endpoint) to \(2/3\) (at its right endpoint), and **splitting** uniquely minimizes expected infections for \(s<s_*(p)\), **concentration** uniquely minimizes them for \(s>s_*(p)\), while exactly the two allocation types tie for \(s=s_*(p)\). For example, at \(p=s=9/10\), the concentrated and split expectations are respectively \(486693/125000\) and \(981/250\), so concentration saves exactly \(3807/125000\) expected cases.

The size-three household is the **smallest equal-household size** that permits a strict concentration advantage under the same two-dose model: for two households of size two, concentration exceeds splitting by \(2ps(1-s)>0\) in expected infections, for every \(0<p,s<1\). For size one the two-dose comparison is degenerate.

## Assumptions and scope

All Bernoulli importation events and all undirected contact-bond events are independent, even between households. A bond is **bidirectionally usable** if open: this is the static bond-outbreak (or connected-component) epidemic, not the general continuous-time SIR model with independently directed transmission clocks or heterogeneous infectious periods. Each household's physical contact graph is complete before vaccination. Each dose provides complete immunity; no waning, dilution, partial protection, age heterogeneity, inter-household transmission, or vaccine cost is modeled. External introductions occur *after* vaccination and only among remaining susceptible individuals. The objective is the **expectation** of total final infections, not the epidemic reproduction threshold, the probability of a large outbreak, or an equity-constrained policy.

Throughout the theorem \(p,s\in(0,1)\). On the degenerate boundaries \(p=0\), \(s=0\), or \(s=1\), both allocation types tie, independently of the remaining parameter. The formula also extends continuously to \(p=1\), where the tie is at \(s=2/3\).

## Proof

For one complete household of \(m\in\{0,1,2,3\}\) unvaccinated members, let \(F_m\) be its expected final infection count under the stated model. Exchangeability gives \(F_m=m\Pr(v\text{ is ultimately infected})\) for any fixed unvaccinated vertex \(v\). Clearly \(F_0=0\) and \(F_1=s\).

For \(m=2\), vertex \(v\) remains uninfected if it is not imported and either the single bond is closed or its neighbor is not imported. Hence
\[
F_2=2\bigl[1-(1-s)(1-ps)\bigr]
=2s\bigl[1+(1-s)p\bigr].
\]

For \(m=3\), expose all three bonds of the triangle. The open connected component containing a fixed vertex \(v\) has cardinality \(1\), \(2\), or \(3\) with respective probabilities
\[
(1-p)^2,\qquad 2p(1-p)^2,\qquad 3p^2-2p^3.
\]
(The second event requires exactly one open edge from \(v\) to a second vertex and both cut edges to the third vertex closed.) Vertex \(v\) is uninfected precisely when no member of its open component is imported. Therefore
\[
F_3=3\left\{1-(1-s)\left[(1-p)^2
+2p(1-p)^2(1-s)+(3p^2-2p^3)(1-s)^2\right]\right\}.
\]

Because the two households are isolated, expected final infections add. Splitting yields \(E_{\mathrm{split}}=2F_2\), concentration yields \(E_{\mathrm{conc}}=F_1+F_3\). Substitution and exact polynomial collection give
\[
\Delta:=F_1+F_3-2F_2
=ps(1-s)\left[A(p)-sB(p)\right],
\quad A(p)=2+6p-6p^2,\quad B(p)=9p-6p^2.
\]
The prefactor is strictly positive throughout the open parameter square, and \(B(p)>0\). If \(p\le2/3\), then \(A(p)-B(p)=2-3p\ge0\), whence \(A(p)-sB(p)>0\) for \(s<1\). If \(p>2/3\), then \(A(p)-B(p)<0\) while \(A(p)>0\), so the unique zero in \((0,1)\) is \(s_*(p)=A(p)/B(p)\), with the stated sign pattern.

Moreover,
\[
s_*'(p)= -\frac{2(3p^2-4p+3)}{3p^2(2p-3)^2}<0,
\]
where the numerator quadratic is strictly positive. Endpoint substitution gives the limiting values \(1\) and \(2/3\). These exhaust all possible two-dose allocations, proving global optimality and every tie. The exact example follows by rational substitution.

Finally, for two two-person households and two doses, concentration yields \(F_2+F_0\), and splitting yields \(2F_1\), with gap \(F_2-2F_1=2ps(1-s)>0\). Households of size one admit only the allocation vaccinating one member in each. This proves the minimal-household-size assertion.

## Verification

The standalone `verification.py` uses only the Python standard library. It enumerates every undirected contact-edge configuration and every independent importation-seed configuration for household sizes zero through three, propagates infection through open edges, and sums the outcomes with exact rational weights. It independently compares these sums with each closed form and the factored allocation gap, checks the optimizer classification across a rational parameter grid, and checks an exact interior tie and strict concentration witness. Run `python3 verification.py`; the packaged file's successful test reports **2533 exact-rational assertions**. This finite enumeration is supplementary: the proof for all real \(p,s\in(0,1)\) is the preceding algebra and sign argument, not extrapolation from test cases.

## Relationship to prior work

Keeling and Shattock (2012) show that prophylactic vaccine allocation among separated populations can favor concentration; their inspected model uses large-population final-size equations and unequal population sizes. Yuan, Alderson, Stromberg and Carlson (2014 preprint; 2015 publication) study optimization in two stochastic SIR populations using continuous-time Markov dynamics, typically with large unequal populations and fixed initial infectives. Ball, Britton and Lyne (2004) optimize vaccination to bring a household-epidemic **reproduction threshold** below one; Ball and Sirl (2017) study household/network vaccination mainly in the large-population limit. None of the inspected analyses states or directly implies the fixed two-dose, two-**identical**-triangle, independently imported, undirected-bond expected-infection phase boundary above.

The broad facts that percolation components describe a restricted class of epidemic outcomes (Newman 2002; Kenah and Robins 2007) and that concentrating vaccination can sometimes be optimal are **not** new contributions. The proposed contribution is the natural smallest-household exact classification with its sharp two-parameter boundary and complete tie cases. Related formulations of the general household-vaccination optimization problem are substantial priority risks; no claim of independent validation or exhaustive historical uniqueness is made.

## Limitations

The result is an exact idealized benchmark, not a recommendation to allocate vaccines inequitably. It does not extend automatically to general SIR processes: a fixed undirected bond linking two people is not equivalent to independent directed transmission trials in all finite-network SIR models. Results can also change with unequal household sizes, different seeding processes, imperfect vaccination, inter-household mixing, other contact topologies, or a different loss objective. Historical priority is provisional: the full Ball–Lyne (2002) article was not available through attempted open sources or institutional access in this review. Its abstract concerns global household-reproduction thresholds rather than the exact finite-outbreak objective, but unknown full-text comparisons remain a risk.

## References

1. M. J. Keeling and A. Shattock, *Optimal but unequitable prophylactic distribution of vaccine*, Epidemics **4** (2012), 78–85; first online 2012-03-07. https://doi.org/10.1016/j.epidem.2012.03.001 .
2. E. C. Yuan, D. L. Alderson, S. Stromberg, J. M. Carlson, *Optimal vaccination in a stochastic epidemic model of two non-interacting populations*, arXiv:1407.3215 (public 2014-07-10), PLOS ONE **10** (2015), e0115826. https://arxiv.org/abs/1407.3215 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC4331427/ .
3. F. Ball, T. Britton and O. Lyne, *Stochastic multitype epidemics in a community of households: estimation and form of optimal vaccination schemes*, Mathematical Biosciences **191** (2004), 19–40. https://doi.org/10.1016/j.mbs.2004.05.001 ; https://staff.math.su.se/tom.britton/papers/J24.pdf .
4. F. Ball and O. Lyne, *Optimal vaccination policies for stochastic epidemics among a population of households*, Mathematical Biosciences **177–178** (2002), 333–354. https://doi.org/10.1016/S0025-5564(01)00095-5 .
5. F. Ball and D. Sirl, *Evaluation of vaccination strategies for SIR epidemics on random networks incorporating household structure*, Journal of Mathematical Biology **76** (2018), 483–530; public 2017-06-20. https://doi.org/10.1007/s00285-017-1139-0 .
6. M. E. J. Newman, *Spread of epidemic disease on networks*, Physical Review E **66** (2002), 016128. https://doi.org/10.1103/PhysRevE.66.016128 .
7. E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, Physical Review E **76** (2007), 036113. https://doi.org/10.1103/PhysRevE.76.036113 .
