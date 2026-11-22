# Self-review

**Claim reviewed:** Complete global waiting-time minimizer for one guaranteed periodic departure and three correlated optional departures under the specified four-mode operating law; in particular, the exact co-dispatch criterion \(uv\geq w(u+v+w)\) and the symmetric threshold \(3-2\sqrt2\).

## Correctness — PASS
The actual four-mode gap-squared expectation is derived directly from uniform passenger arrival. For every specified positive real scenario weight the full quadratic is strictly convex since the all-service mode has positive weight. Symmetry reduces the two terminal gaps to equality; the free stationary solution and boundary KKT derivatives exactly prove the unique global minimizer. Formula normalization, positive remaining gaps, the radical threshold and rational benchmark were checked. The standalone checker ran successfully against the current mathematical files, with 165 rational probability triples plus exact competition and benchmark checks. These finite checks supplement rather than replace the proof.

## Originality — PASS, with residual priority risk
Statement-level comparisons with opaque earlier records `823a3384-8ec8-4e13-a9b3-6a5ef8ed7179` and `5690be0c-1bb0-4d68-ad4d-4e4598ea12cf` distinguish independent-service and two-candidate results from the new three-optional correlated family. Full primary HTML text of Gkiotsalitis (2020) and Dou and Li (2023) describes different objectives and stochastic inputs and does not state the proved activation threshold. The familiar headway-squared waiting-time identity is credited. Zhao et al. (2006) and a 2019 rolling-rescheduling paper were only partially accessible; a broader exact scenario-optimization result remains a possible priority risk. Search nonmatches alone have not been treated as proof of novelty.

## Value — PASS
The exact co-dispatch phase occurs despite strictly positive probability that all optional vehicles operate, reversing the intuition that any positive simultaneous service warrants strict timetable separation. The complete three-weight classification and the exact \(3-2\sqrt2\) threshold identify a reproducible decision boundary, while the \(u=v=9/20\), \(w=1/10\) benchmark reduces mean waiting by exactly \(151/1311\) relative to uniform nominal headways. The result serves as a tractable diagnostic for correlation-aware dispatch assumptions, not an empirical operational recommendation.

## Closest literature and limitations
Zhao, Dessouky and Bukkapatnam (2006), DOI 10.1287/trsc.1060.0170; Gkiotsalitis (2020), DOI 10.1049/iet-its.2019.0725; Dou and Li (2023), DOI 10.3390/pr11020574; and Gkiotsalitis's 2019 rolling-horizon study, DOI 10.1080/15472450.2019.1681992. There is no observed capacity, running time, advance passenger information, minimum spacing or transfer penalty in the model. Independent bibliographic priority review and empirical validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
