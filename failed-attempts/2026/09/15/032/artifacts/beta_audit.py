"""Beta-dependence audit: exact J and rho0 across beta for N=2,3 (q=2, alpha=0.5).
Quantifies the target's beta-independence clause: J varies only ~5% over 15x beta range
at N=3, vs 1D TASEP phase-transition-scale dependence. Also rho0 variation.
"""
import importlib.util
spec = importlib.util.spec_from_file_location("ex", "output/artifacts/exact_small.py")
ex = importlib.util.module_from_spec(spec); spec.loader.exec_module(ex)
for N in [2,3]:
    print(f"N={N}")
    for beta in [0.2,0.5,1.0,2.0,3.0]:
        G,lvl,S=ex.build(2,N,0.5,beta)
        pi=ex.stat(G)
        rho=ex.level_means(pi,lvl,S,N,2)
        print(f"  beta={beta}: J={ex.J_of(0.5,rho[0]):.6f} rho0={rho[0]:.6f}")
