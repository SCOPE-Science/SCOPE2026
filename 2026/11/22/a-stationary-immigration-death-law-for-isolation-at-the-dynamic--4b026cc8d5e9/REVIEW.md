# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md (1)–(5). Conditional on an edge being absent, absence across a gap Δ at scaled times has probability 1-p_n(1-e^(-Δ/log n)): either there was no refresh or the most recent sample was absent. Stationarity and the Markov property give q_n(S). Taking logs, the first factor contributes -(log n+x)+o(1) to (n-1)log q_n(S); the remaining factors contribute the negative sum of consecutive requested gaps, since n p_n/log n→1. Edges between two tags must meet the union of their requests, while untagged incident edges factor independently. With r fixed this gives the exact tagged product and its product limit after scaling by n^r. Inclusion–exclusion annihilates omitted indices interior to an exact signature, and for a block the left and right sums factor; selecting any index further out makes selecting the nearest exterior index immaterial, so only the two nearest-neighbor differences survive. Multiplying the limiting tagged probabilities by (n)_r yields all mixed factorial moments; bounded higher moments give uniform integrability of each fixed order and the independent Poisson moment law is determinate. In the stationary Poisson lifetime construction, the intensity alive at t_a but not at t_(a-1) is λ(1-e^(-gap)) for a>1 and λ at a=1; exponential survival through t_b and death before the next sample give the other factors. For t>0 the three Poisson intensities yield joint zero probability exp[-λ(2-e^(-t))]; t=0 is the identical-snapshot case. Snapshot connectivity agrees asymptotically with having zero isolates, simultaneously at fixed finitely many times by the classical threshold theorem and a union bound. This does not show path tightness or rule out short unobserved isolation episodes. The supplied checker and verification notes were inspected, not executed; their finite tests do not replace this limit argument.

## originality

PASS

The critical refresh scale, static Poisson marginals, and nonvanishing critical two-time dependence are prior. The supported addition is the quantitative graph-specific joint law for exact multitime signatures and the resulting immigration–death finite-dimensional limit, including the exact two-time connectivity probability. No equivalent or stronger graph theorem was established in the examined material.

## value

PASS

At the known critical refresh scale, one-time connectivity probabilities or qualitative sensitivity do not quantify persistence across snapshots. The theorem gives both an explicit joint reliability probability and a structural Poisson decomposition that distinguishes persistent from newly appearing isolates at the observed times. This is worthwhile without making an unsupported claim about episodes between observations or full path convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
