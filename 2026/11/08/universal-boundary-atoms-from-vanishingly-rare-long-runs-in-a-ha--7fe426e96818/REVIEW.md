# Review of the rare-long-run stationary boundary law

**Correctness: PASS.** The sign-aligned renewal chain is a contraction in mean, the stationary occupation law is obtained from the equilibrium-time renewal-reward identity, and an explicit four-term Lipschitz comparison proves the stated uniform Wasserstein bound. The example's limit density and moments are integrated exactly; rational enclosures prove the strict cumulant lower bound and the finite-duration positivity cutoff. The packaged `verify.py` has passed deterministic checks; numerical recurrence tests do not establish the universal theorem.

**Originality: PASS, qualified.** Farago–Smith (arXiv:2401.01576, first public 2024-01-03) treat general non-Markovian tumbling and provide numerical equations for stationary position densities. Their inspected sections do not contain this singular fixed-mean clock limit, quantitative atom weights or a positive-cumulant witness. Sun–Ye–Podgornik (arXiv:2409.00578) instead treat exponentially timed run/zero-propulsion tumble phases. The conventional stationary-excess/renewal occupation theory and harmonic Markov telegraph model are prior building blocks rather than claimed new principles. Unindexed renewal-limit coverage is a remaining publication-priority risk; incomplete full-text access to a broad stationary-excess paper also limits absolute coverage claims.

**Mathematical value: PASS.** Weakly convergent waiting-time clocks of the same fixed mean can give discontinuously different stationary active-particle laws. The new universal atom masses and explicit convergence rate quantify how rare long propulsion intervals dominate time sampling. The strict kurtosis sign reversal supplies a substantive observable consequence in the natural harmonic model.

**Limitations.** The support-endpoint atoms occur in the limiting spatial measure, not necessarily at finite exceptional duration. This is an equilibrium-time and alternating-sign theorem with finite-mean positive runs, no thermal noise, no joint asymptotic scaling, and no claim of publication-priority certainty.

Self-review: passed. Independent audit: not yet performed.
