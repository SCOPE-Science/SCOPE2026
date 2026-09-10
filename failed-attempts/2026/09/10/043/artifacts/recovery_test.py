"""Recovery test: can the TARGET's K-explicit chain be closed from cited theorems?
Checks (i) R1 algebra on the proxy one-scale numbers; (ii) whether a uniform
Markov-type-2 bound M_2(X) <= C*K*(1+log K) can hold over the target class
{2-uniformly-convex X}: NO — L^p (1<p<2) is 2-uniformly convex (power type 2,
K~(p-1)^(-1/2)) yet fails Markov type 2 (Ball: Markov type 2 => Enflo type 2;
L^p has Enflo type exactly min(p,2)=p<2). So M_2(L^p)=+inf while the claimed
RHS is finite: the Markov-type route as stated is structurally void on the
full target class. The only remaining route (cotype/Poincare uniform envelope
(+)) is K-inexplicit in Mendel-Naor (per-X C(X), eps(X), p(X), delta0(X)).
Writes output/artifacts/recovery_test_result.json
"""
import json, math

R = json.load(open("output/artifacts/one_scale_check.json"))
eta, Abar, n = R["eta"], R["avg_sq_dist_all"], R["n"]
# R1 check: D >= sqrt(Abar/gamma_hilbert), gamma_hilbert = 1/eta
gamma_h = 1.0/eta
D_lb = math.sqrt(Abar/gamma_h)
assert abs(D_lb - R["hilbert_distortion_lb_sqrt_eta_Abar"]) < 1e-9
# Target-shape check at proxy scale: sqrt(log n) template value
template = math.sqrt(math.log(n))  # c*=K=1 normalization
# L^p obstruction (analytic facts, recorded as logical check):
# p=1.5: 2-UC constant K finite (~(p-1)^-1/2 = sqrt2), M_2 = +inf.
p = 1.5
K_Lp = (p-1)**(-0.5)
M2_Lp = float("inf")
rhs = K_Lp*(1+math.log(K_Lp))  # finite
obstruction = (M2_Lp > rhs)  # True => uniform Markov-type-2 bound impossible

out = {
    "R1_proxy_check": {"gamma_hilbert": gamma_h, "D_lb": D_lb,
                       "sqrt_log_n_template": template, "pass": D_lb > 0},
    "markov_type2_uniformity": {
        "witness_class": "L^1.5 (2-uniformly convex, power type 2)",
        "K_finite": K_Lp, "M2": "inf (fails Enflo type 2, Ball implication)",
        "claimed_RHS_finite": rhs, "uniform_bound_refuted": obstruction},
    "result": ("BLOCKED: R1+R2 give only per-scale/per-X numbers; "
               "Markov-type-2 uniform route refuted on target class; "
               "cotype uniform envelope (+) absent from Mendel-Naor."),
}
json.dump(out, open("output/artifacts/recovery_test_result.json", "w"), indent=2)
print(json.dumps(out, indent=2))
