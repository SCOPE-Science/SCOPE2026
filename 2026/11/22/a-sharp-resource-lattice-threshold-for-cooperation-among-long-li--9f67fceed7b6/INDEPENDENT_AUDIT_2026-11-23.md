# Independent mathematical audit

## correctness

PASS

The four rates in RESULT.md 24–33 agree with Caruso et al. Eq. (1) and Supplemental Eqs. (S1),(S4), including clipping only the d-to-c factor. The ordered-pair weights sum to 1, so the assumed extraction inequalities give death rate at least e_cc r at every positive stock r. A finite all-deaths path from every state, with a common positive probability of completion in a fixed time, gives almost-sure extinction and an exponential survival tail. The pure-cooperator killed birth–death generator Q_c is irreducible and has a simple Perron eigenvalue -alpha<0. Skip-free stock chains can be coupled independently until meeting and together thereafter; their survival probabilities are ordered in the initial stock. Taking the Perron limit gives v_{i+1}>=v_i for its right eigenvector with v_0=0. A plateau v_{i+1}=v_i>0 makes the left side of the eigenvector equation at i+1 nonnegative, including at the capacity boundary, against -alpha v_{i+1}<0. Thus stock increases v strictly. Testing the other killed blocks on v(r) now gives Q_d v<-alpha v (strictly greater pure-defector deaths) and Q_I v<=-alpha v, strict at c=1 because the strategy loss there exits and kills the mixed-block trajectory. When R_c>1, r=1 permits both strategy directions inside the mixed block, and positive resource transitions connect each strategy layer, including the single layer when N=2. Multiplying by a positive left Perron vector gives strict spectral separation. In the block-triangular full generator the dominant simple eigenvalue has its left measure supported on c=N, with marginal pi_c. From every stated start a positive-probability path reaches that block via r=1 (or starts in it); survival via this finite-time path is bounded below by a positive multiple of exp(-alpha t), so the dominant coefficient cannot vanish. Jordan expansion and normalization give exponential total-variation convergence, with a possibly smaller exponent to absorb polynomial prefactors. If R_c<=1, the increase rate vanishes at every r>=1, so fixation at c=N before extinction is impossible from mixed starts. The threshold concerns initially mixed starts, not all-defectors, and uniqueness of pi_c is within the pure-cooperator class, not uniqueness of a QSD for the reducible full chain. Replay: this Perron comparison and RESULT.md 37–64; VERIFICATION.md and verify.py were read, not run. The finite numerical script checks examples and not the universal spectral comparison.

## originality

PASS

Best-of-knowledge pass for the paired sharp positive-stock attainability boundary and the strict all-cooperator Yaglom selection theorem in the specific finite commons chain. The microscopic model, the integer gate itself as read from its rates, and general quasi-stationary theory are not new. Mere reachability on the positive side of the gate does not imply it is the class selected among long-lived histories; the model-specific spectral dominance does that.

## value

PASS

A finite stock lattice creates a real obstruction absent from a continuum scarcity argument. The conditional theorem explains how crossing that boundary changes not just what is reachable but which strategy survives in the long-lived ensemble, with an explicit resource QSD and exponential convergence while unconditioned extinction remains certain. It distinguishes this fixed-capacity rare-history result from transient oscillations, indefinite sustainability, or a large-population claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
