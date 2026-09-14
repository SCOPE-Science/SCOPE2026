"""Fast deterministic checks for SH large-deviation heuristic (no heavy simulation)."""
import math

mu = 2.0
alpha = 1.5
# 1) Rate identity: r_n = 1/(mu^n P(|X|>gamma_n)); check gamma_n with mu^n P = 1/n -> o(1)
print("rate check:", flush=True)
for n in [4, 5, 6, 8, 10]:
    p = 1.0 / (n * mu**n)
    gamma = p ** (-1.0 / alpha)  # Pareto tail P(|X|>t)=t^{-alpha}
    check = mu**n * gamma**(-alpha)
    print(f"n={n}: gamma={gamma:.2f} mu^n*P={check:.4f} (=1/n={1/n:.4f}) r_n={1/check:.1f}")
# 2) Coefficient domination without Kesten-Stigum: term_l = mu^{-(l+1)} E[1-exp(-Z_l)] <= mu^{-(l+1)}
#    and with Z_l in {0,inf} limit -> q-survival constant <=1. Series converges geometrically.
print("series domination:", flush=True)
C = 0.0
for l in range(0, 21):
    bound = mu ** (-(l + 1))
    C += bound
    if l in (0, 2, 5, 10, 20):
        print(f"l={l}: term-bound={bound:.6f} partial={C:.6f}")
print(f"geometric sum inf = {1/(mu-1):.6f}; partial-20 = {C:.6f}")
# 3) SH-scale separation: c_n/mu^n -> 0 illustration (c_n = mu^n/(log n) toy); large-dev scale gamma_n >> c_n regime
print("scale separation (toy c_n=mu^n/log(n+1)):", flush=True)
for n in [5, 10, 20, 50]:
    cn = mu**n / math.log(n + 1)
    print(f"n={n}: c_n/mu^n={cn/mu**n:.4f} -> 0; r_n scale uses mu^n, not c_n")
print("ALL CHECKS DONE", flush=True)
