# Independent mathematical audit

## correctness

PASS

PASS. Exact continuous-time SI likelihood for a fixed infected prefix {1,...,k} at known u=lambda*t is L_s=e^{-u} u^{k-s}/(k-s)! times Q_{s-1}(u), since the left independent infection front must have crossed s-1 edges and saturates at physical vertex 1, while the right front must make exactly k-s jumps without infecting k+1. The adjacent ratio R_s=(k-s)Q_s/(u Q_{s-1}); for s=1 it is (k-1) integral_0^1 e^{-ux}dx, and for s>=2 it is (k-s)/(s-1) times an exponentially tilted expectation of x. Differentiating gives a strictly negative variance, so R_s decreases with age. Posterior ratios inherit strict ordering for any fixed positive prior, implying strict leftward MLR and first-order stochastic shift. Poisson tail/mass expansion proves the upper-tail hazards increase in s and hence R_s decreases strictly in s, making likelihood strictly log-concave. Limits R_s(0+)=(k-s)/s and R_s(infinity)=0 give exactly floor((k-1)/2) strictly ordered unique crossings and the entire uniform-prior MAP staircase; direct k=2 special case correctly excluded. Independent SciPy Poisson-tail diagnostics check 480 ordered age/spatial inequalities across k=3..12; these do not replace the all-parameter analytic proof.

## originality

PASS

PASS best of knowledge. The fixed-age full-path endpoint conditioning differs materially from rumor-centrality unknown-age tree snapshots, event-order source probabilities and discrete-time SIR time sensitivity. The combination of a strict age-MLR posterior ordering under every positive prior and the complete uniform-MAP crossing staircase is not present in the compared published records. Residual risk: an alternative derivation for one-dimensional Poisson fronts may exist in older source-inference literature not retrieved in complete text.

## value

PASS

PASS. Infection source identification from a known-time full-state prefix of a finite path is a natural inverse problem. Endpoint saturation changes likelihoods, and hypothetical observation age induces rigorous all-prior posterior stochastic shifts and an exact finite collection of mode transitions, giving a precise benchmark and a boundary case for rumor centrality. This is a structural theorem, not a generic Bayes formula or small-instance numerical pattern.

The dated certificate retains the supplied scientific assessment, sources and limitations.
