# Self-review

## Correctness — PASS

The claim is confined to one transient outbreak, with the force of infection held fixed for the comparison between its existing vaccinated and unvaccinated groups. The backward equation of a two-state post-primary infection–recovery chain yields a positive integral for the recovered-minus-infectious expected future episode count. Hence expected repeats decrease strictly with first-infection time. Transforming to cumulative hazard produces a nonzero positive Stieltjes measure, strict alternating derivatives in susceptibility, and strict concavity. Conditioning on primary infection gives an exact truncated-exponential family whose monotone likelihood ratio yields the strict upper group ratio. Each analytic step and positivity condition was reconstructed. The known source aggregate identity then gives the displayed two-sided bounds. The accompanying `verify.py` was executed and passed all six numerical test cases. The finite numerical work is not treated as proof of the universal inequalities.

## Originality — PASS (literature-bounded)

The complete Gutierrez–Gog published article supplies primary counts and total leaky reinfections but expressly cannot separate the vaccinated and unvaccinated repeat totals (Sect. 4.3, eqs. 39–42); it gives equal ratios only under the *different* all-or-none mechanism. Edlefsen's full 2014 paper contains the related first-infection selection principle, but removes subjects after primary infection and does not give the needed post-primary reward monotonicity or quantitative repeat-infection brackets. Magpantay et al. (2014) concern immunizing SIR, and Katriel (2010) lacks vaccine groups in the abstracted scope. Relevant indexed findings on vaccination thresholds and SIS vaccination optimization, plus related mathematical claims, do not entail the theorem. The mathematical literature searches, implication comparisons and residual risks are recorded in AUDIT.json. The 2004 Gomes–White–Medley full text and 2010 Katriel full text were not available; historical priority remains open, and no global novelty certification is claimed.

## Value — PASS

The result quantifies a biologically interpretable subgroup gap in a model where aggregate final-size formulas alone do not resolve subgroup repeat burden. The universal strict inequality and final-pressure-only brackets distinguish the two immunity mechanisms more concretely than total prevalence alone. The fact is not an arbitrary fixed-parameter slice or mere recitation of aggregate formulas: it covers every transient outbreak in the specified model and any fixed integrable infection-pressure curve with the same post-primary mechanism.

## Scope and remaining limitations

The comparison is within an epidemic, not between counterfactual campaigns; allowing vaccine changes to alter infection force invalidates an inference from the fixed-force derivative hierarchy. The proof assumes identical post-primary susceptibility, an exponential recovery clock, no vital dynamics, finite total force, and an infinitesimal-seed epidemic branch. Numerical tests approximate that branch. The bounds do not determine exact separate reinfection counts. Older partly inaccessible primary texts create historical-priority uncertainty; no external independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
