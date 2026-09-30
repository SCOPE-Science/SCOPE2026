"""Lane 1240 certificate: sublattice parity gap for symmetric 2-periodic (1,a) dimers.
Weighting W*: H edge in column x: 1 (x even), a (x odd); V edge in row y: 1/ a likewise. a=1/2.
K(z,w) = [[1+a z, i(1+a w^-1)],[i(1+a w), 1+a z^-1]], P = |1+az|^2+|1+aw|^2 > 0 on torus.
p_evenH = E[(1+a cosT)/P] = U+aC; p_oddH = aC+a^2 U (Fourier shift c_{-1,0}=E[z(1+az^-1)/P]).
Checks: E[P/P]=1 i.e. 2(1+a^2)U+4aC=1; vertex sum 2 p_even+2 p_odd=1; gap=(1-a^2)U>= (1-a^2)/E[P].
"""
import numpy as np, json
a = 0.5
res = {"a": a, "E_P": 2*(1+a*a), "Pmin_formula": 2*(1-a)**2, "Jensen_LB_gap": (1-a*a)/(2*(1+a*a))}
for N in [400, 1600]:
    t = (np.arange(N)+0.5)/N*2*np.pi
    T, P_ = np.meshgrid(t, t, indexing='ij')
    Pall = (1+a*a+2*a*np.cos(T)) + (1+a*a+2*a*np.cos(P_))  # |1+az|^2+|1+aw|^2
    inv = 1.0/Pall
    U = float(np.mean(inv)); C = float(np.mean(np.cos(T)*inv)); Cp = float(np.mean(np.cos(P_)*inv))
    pE = U + a*C; pO = a*C + a*a*U
    ident = 2*(1+a*a)*U + 2*a*(C+Cp)   # must be 1
    res[f"N{N}"] = {"Pmin": float(Pall.min()), "U": U, "C_cosT": C, "C_cosP": Cp,
        "E[P/P]_identity": ident, "p_evenH": pE, "p_oddH": pO,
        "vertex_sum": 2*pE+2*pO, "gap": pE-pO, "gap_formula_(1-a2)U": (1-a*a)*U}
print(json.dumps(res, indent=1))
with open("output/artifacts/gap_numbers.json","w") as f: json.dump(res, f, indent=1)
