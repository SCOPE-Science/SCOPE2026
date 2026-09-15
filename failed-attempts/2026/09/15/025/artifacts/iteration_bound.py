"""Reproducible numeric check for the HJKE covering-number iteration (Theorem 1.1)
and the direct-sum/amplification blow-up (Proposition 1.2 (i)=>(iii)).

Lemma 3.3 model: for 0<eta=eps^2<=eps<gamma/2,
  h_{eps^2}(x) <= h_{eps}(x) + K*eps*log(C/eps^2),  K = 12(d+1)/gamma.
Iterating eps_{j+1}=eps_j^2 gives the tail sum
  S = K * sum_{j>=0} eps^{2^j} * (log C + 2^{j+1} log(1/eps)),
which converges doubly-exponentially fast, so h(M) <= h_eps(x) + S < infinity.

Also checks the amplification/direct-sum scaling used in Prop 1.2:
  h(M^t) = t^{-2} h(M); with lam_j = 2^{-j}, M_j = N^{4^{-j}},
  lam_j^2 h(M_j) = 4^{-j} 4^{2j} h(N) = 4^j h(N) -> infinity if h(N)>0.
"""
import math, json

def tail_sum(eps, d, gamma, C, terms=12):
    K = 12.0*(d+1)/gamma
    log_inv = math.log(1.0/eps); logC = math.log(C)
    total = 0.0; terms_used = []
    for j in range(terms):
        log_term = logC + (2**(j+1))*log_inv
        lj = -((2**j)*log_inv) + math.log(log_term)  # log of summand
        contrib = math.exp(lj)
        total += contrib
        terms_used.append(contrib)
    return K*total, terms_used

out = {}
for (d, gamma, C, eps) in [(3,0.5,5.0,0.1),(5,0.1,5.0,0.1),(10,0.05,5.0,0.1)]:
    S, tj = tail_sum(eps,d,gamma,C)
    out[f"d={d},gamma={gamma}"] = {"tail_bound": S, "first_terms": tj[:5]}
    # convergence check: ratio of successive terms -> 0 fast
    ratios = [tj[j+1]/tj[j] for j in range(4)]
    out[f"d={d},gamma={gamma}"]["ratios"] = ratios
    assert ratios[1] < 0.05 and ratios[2] < 1e-2 and ratios[3] < 1e-5, ratios

# amplification scaling check
for j in [1,2,3,5,8]:
    t = 4.0**-j; lam2 = (2.0**-j)**2
    assert abs((t**-2) - 4.0**(2*j)) < 1e-9
    assert abs(lam2*(t**-2) - 4.0**j) < 1e-9
out["scaling"] = "lam_j^2 * t_j^-2 = 4^-j * 4^{2j} = 4^j -> infty; matches HJKE Prop 1.2 proof"

print(json.dumps(out, indent=1))
with open("output/artifacts/iteration_check.json","w") as f:
    json.dump(out, f, indent=1)
print("wrote output/artifacts/iteration_check.json")
