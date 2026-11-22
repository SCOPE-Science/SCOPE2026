# Scientific review: A wildfire-hazard reversal in the optimal fire deadline for maturing canopy seed banks

## Correctness — PASS

The object is a continuous single-cohort fire-deadline yield-rate problem, not demographic persistence. Maturation is strict age \(m>0\), viable-seed loss is \(\delta>0\), wildfire hazard is \(\mu>0\), and production scale is \(r>0\). The stock and expected reward/duration are derived from the same first-fire time. The exact critical equation \(Q(T)=0\) has a single global root because \(Q'\) changes sign once and \(Q\) ultimately tends to minus infinity. The strict global signs of deadline derivatives follow from the negative derivative \(g_T=-\delta\ell\) and increasing auxiliary function \(H\); all boundary regimes and the limiting deadlines are handled separately. Replay of `check.py` passed 91,091 deterministic numerical assertions, supplementing rather than replacing the proof. Model normalizations and the impossibility of inferring regeneration or ecological safety from this proxy are stated.

## Originality — PASS, with historical priority risk

The relevant primary sources are McCarthy, Possingham and Gill (2001), DOI 10.1046/j.1365-2664.2001.00617.x, on state-dependent prescribed-fire management under stochastic wildfire; Enright et al. (1998), DOI 10.1046/j.1365-2745.1998.00312.x, on serotinous population growth and variable fire cycles; and Lamont and Enright (2000), DOI 10.1046/j.1442-1984.2000.00036.x, on aerial seed storage and viability. Their available full texts were examined, including substantive methods/results. Reed's scanned 1986 forest-rotation and protection report was inspected on representative pages, but not in complete searchable text; its objective is discounted commercial timber returns with protection spending. General renewal reward calculations are established prior art and are not claimed as new. The nearest related historical mathematical claim concerns power-law timber value under Weibull disaster risk and salvage, rather than a bounded post-maturity canopy seed-stock reward, and does not imply the new hazard-sign statement. The 1997 Boshuizen age-dependent replacement study was accessible only at abstract level, leaving a priority risk. No full-corpus historical uniqueness claim is made.

## Value — PASS

Maturation delay and seed decay are meaningful opposing mechanisms in serotinous canopy seed stocks. The result gives one global optimizer, an explicit root bracket, strong hazard and decay comparative statics, and sharp disappearance of the finite optimum if either mechanism is removed. It explains a counterintuitive competition between premature wildfire and deliberate release. These exact outcomes are valuable as a transparent model diagnostic, while not justifying real prescribed burning without demographic and field calibration.

## Boundaries and independent validation

The theorem assumes exponential wildfire arrival and viability loss, perfect complete fire release, constant post-maturity production, and an expected-yield-per-expected-time proxy; demographic persistence, recovery from premature fire and operational feasibility remain unproved. General age-replacement literature may contain broader results. An independent audit has not been carried out.

Self-review: passed. Independent audit: not yet performed.
