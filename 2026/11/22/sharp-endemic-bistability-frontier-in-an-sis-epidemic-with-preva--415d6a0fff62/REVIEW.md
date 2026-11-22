# Self-review of a sharp SIS–logit endemic fold

## Correctness — PASS

The full proof reduces every endemic equilibrium to a level set of \(g(I)=(1-I)\ell(c+dI)\), with strictly decreasing logarithmic derivative. The Lambert maximum is derived by the exact stationary equation, not fitted numerically. The exact Jacobian determinant is \(-\beta I g'(I)\), giving sink and saddle types with strict trace. The disease-free equality case is explicitly nonhyperbolic; no unsupported stability claim is made there. An entirely elementary witness uses \(2<e<4\). The accompanying `verify.py` rechecked 175 parameter triples and numerical root locations; those checks supplement rather than replace the analytic proof.

## Originality — PASS, literature-bounded

The originating source [1] introduces the SIS–logit system, and its Lemma 3 assumes a conditional monotonicity inequality for a uniqueness claim. For the specialization here, that inequality has negative terms \(-\beta B\) and \(-\gamma B\), so it does not apply. The new scope is the necessary-and-sufficient, all-parameter Lambert-W fold frontier and exact three-equilibrium witness. A published mathematical result for the same ODE proves a universal no-periodic-orbits threshold, not this stationary multiplicity classification; that prior claim is credited and not repackaged. Other relevant studies use replicator updating or opinion feedback. A broad feedback-logit paper was compared only via abstract because its full text was unavailable: historical priority consequently remains subject to external scrutiny.

## Value — PASS

The exact boundary describes when disease freedom can resist small invasion yet stable endemic infection can also persist, resolving the complete equilibrium-count problem for a natural, explicitly realizable payoff subfamily outside the originating paper's sufficient-uniqueness regime. The bistable wedge is not inferred from one numerical example; it is derived with an explicit sharp fold and a certified rational interior witness. The social response is intentionally anti-protective, and the work is a deterministic theoretical result, not an epidemiological recommendation.

## Scientific limitations and closest work

The population is homogeneous; the behavioral payoff difference must be independent of opponents and rise affinely with infection; rationality is finite. No global basin characterization, network/stochastic generalization, or empirical calibration is established. Closest literature is Maitra–Paarporn–Eksin, arXiv:2610.03173v1; the published same-model universal slope-four no-cycle theorem; Park et al., arXiv:2401.15475; Ordorica Arango et al., arXiv:2410.12993; and Gavin–Paarporn–Cao, doi:10.1109/TAC.2026.3685548 (abstract only). General behavioral epidemic bistability is already known in other models.

Self-review: passed. Independent audit: not yet performed.
