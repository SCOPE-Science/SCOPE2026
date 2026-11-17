# Independent mathematical audit

## correctness

PASS

PASS: For 0<alpha<1, beta real, and 2r-1 independent strata-wise jitters at every n (also independent across n), total variation of f outside the first stratum provides deterministic o(1) remainder. The first-stratum crossing occurs at u~(alpha^beta/epsilon)^{1/alpha} n^{-(1-alpha)/alpha}(log n)^{-beta/alpha}. A binomial median tail gives exact leading choose(2r-1,r)*u^r. The integral test and both Borel–Cantelli lemmas yield a.s. convergence iff alpha<r/(r+1), or critical with beta>1/(r+1); independence across n is necessary for the failure direction. Fixed-n tail integration gives p-moment iff p<r/alpha or the equality log condition r beta/alpha>1. Remaining variance bound yields L1 convergence for all parameters. Source verifier checked, but finite checks cannot establish Borel–Cantelli.

## originality

PASS

PASS best-of-knowledge: Hofstadler–Rudolf provides general sufficient median-Latin-hypercube consistency under integrability and replication but not this family-specific necessary-and-sufficient sharp logarithmic boundary, divergence limsup, or exact tail prefactor. The exact critical alpha/beta/r frontier is a meaningful addition even where prior sufficient hypotheses overlap.

## value

PASS

PASS: The complete strong-law and finite-moment phase diagram gives a sharp example where fixed-sample finite variance and convergence in mean coexist with arbitrarily large a.s. spikes. The log boundary clarifies the actual robustness gained by a given replication count for a standard endpoint singularity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
