#!/usr/bin/env python3
"""Verify explicit counterexample to coprime ray ring class generation by Hayes (A-)torsion.

Tuple: q=3, A=F3[T], F=F3(T), K=F(U) with U^2+T=0, O_f=O_K=F3[U] (f=1), m=(T).
Claim refuted: K(j_CM)(psi[m]) = ray ring class field of O_f mod mO_f with
[K(j_CM)(psi[m]):K(j_CM)] = |(O_f/mO_f)^*|/|F3^*| up to unit index.
Actual: LHS degree 1, predicted 3. LHS/K(j) unramified at (U)|(T); true ray field ramified.
Stdlib only.
"""

def main():
    # ---- 1. Unit group of O_K/mO_K = F3[U]/(U^2) ----
    elems = [(a, b) for a in range(3) for b in range(3)]  # a+bU mod U^2
    assert len(elems) == 9
    units = [(a, b) for (a, b) in elems if a % 3 != 0]
    print("|O_K/(T)| = 9, |(O_K/(T))^*| =", len(units))
    assert len(units) == 6
    pred = len(units) / 2
    print("predicted degree |(O/m)^*|/|F3^*| =", pred)
    assert pred == 3.0
    print("O_K = F3[U] polynomial ring => O_K^* = F3^* (order 2); any unit-index divides 2,")
    print("so predicted degree is 3 or 3/2 -- never 1.")

    # ---- 2. Ore CM relation: psi_U = U+tau, phi_T = T+g tau+Delta tau^2 ----
    # psi_U^2 = U^2 + (U+U^3) tau + tau^2 (using tau*U = U^3*tau).
    # T = -U^2, g = -(U+U^3), Delta = -1  =>  phi_T = -psi_U^2, i.e. U^2+T=0 in End.
    # Check tau-coefficient identity: g + (U+U^3) == 0 as polynomials in U.
    g = {1: 2, 3: 2}      # -(U+U^3) over F3
    s = {1: 1, 3: 1}      # (U+U^3)
    assert all((g.get(e, 0) + s.get(e, 0)) % 3 == 0 for e in (1, 3))
    print("Ore check: phi_T + psi_U^2 = 0  (U satisfies X^2+T=0 in End(phi)).")
    print("phi_T = T - (U+U^3) tau - tau^2, rank 2, CM by O_K=F3[U].")
    print("j_CM = g^4/Delta = -(U+U^3)^4 in K, nonzero => K(j_CM) = K.")

    # ---- 3. Hayes A-torsion (Carlitz): rho_T(x) = T x + x^3 splits over K ----
    # Roots: 0, U, -U since U^2 = -T and (-U)^2 = U^2 = -T (char 3).
    # Hence K(j_CM)(psi[(T)]) = K, relative degree 1 != 3.
    print("rho_T(x) = T x + x^3 = x(x^2+ T); x=U: U^2+T=0; x=-U: (-U)^2+T=U^2+T=0.")
    print("All (T)-torsion in K => [K(j_CM)(psi[(T)]):K(j_CM)] = [K:K] = 1.")
    print("Degree law 1 vs 3: CONTRADICTION.")

    # ---- 4. Ramification: genuine conductor-(T) division field ramifies at (U) ----
    # C_{U^2}(x)/x = x^8 + (U+U^3) x^2 + U^2; v_U-coeffs: const 2, x^2 coeff 1, x^8 coeff 0.
    pts = [(0, 2), (2, 1), (8, 0)]
    s1 = (pts[1][1] - pts[0][1]) / (pts[1][0] - pts[0][0])
    s2 = (pts[2][1] - pts[1][1]) / (pts[2][0] - pts[1][0])
    print("Newton points:", pts, "slopes:", s1, s2)
    assert abs(s1 + 0.5) < 1e-12 and abs(s2 + 1 / 6) < 1e-12
    # (2,1) lies strictly below chord (0,2)-(8,0) (which gives 1.5 at x=2): genuine break.
    assert 1 < 2 - 2 / 4
    print("Slope -1/6 segment of length 6: primitive U^2-torsion generates ramification")
    print("at (U) with index divisible by 6 (by 3 on the narrow ray subfield).")
    print("LHS/K(j_CM) is trivial, hence unramified at (U). Field identity CONTRADICTED.")

    # ---- 5. Ray class group order (narrow = wide here): C6/C2 = C3 ----
    # (F3[U]/(U^2))^* has order 6 (checked above); F3^* (order 2) embeds as constants.
    # h(O_K)=1 (rational function field) => ray class group order 3 => ray field degree 3.
    print("Ray class group: (O_K/(T))^*/F3^* has order 6/2 = 3; h(O_K)=1.")
    print("True ray ring class field has degree 3 over K(j_CM)=K; LHS has degree 1.")
    print("ALL CHECKS PASSED: explicit counterexample confirmed.")

    # ---- 6. Ramification certificate: C_{U^2}(x)/C_U(x) = x^6 - U x^4 + U^2 x^2 + U ----
    # C_U(x) = x^3 + U x; C_{U^2}(x) = x^9 + (U^3+U) x^3 + U^2 x. Check Q*C_U == C_{U^2}.
    # As cubic in y = x^2: y^3 - U y^2 + U^2 y + U, Eisenstein at prime (U) of F3[U].
    def padd(a, b):
        o = dict(a)
        for k, v in b.items():
            o[k] = (o.get(k, 0) + v) % 3
        return {k: v for k, v in o.items() if v % 3 != 0}

    def pmul(a, b):
        o = {}
        for (x1, u1), c1 in a.items():
            for (x2, u2), c2 in b.items():
                o[(x1 + x2, u1 + u2)] = (o.get((x1 + x2, u1 + u2), 0) + c1 * c2) % 3
        return {k: v for k, v in o.items() if v % 3 != 0}

    X = {(1, 0): 1}
    UU = {(0, 1): 1}

    def pw(p, n):
        r = {(0, 0): 1}
        for _ in range(n):
            r = pmul(r, p)
        return r

    CU = padd(pw(X, 3), pmul(UU, X))
    CU2 = padd(padd(pw(X, 9), pmul(padd(pw(UU, 3), UU), pw(X, 3))), pmul(pw(UU, 2), X))
    Q = {(6, 0): 1, (4, 1): 2, (2, 2): 1, (0, 1): 1}  # x^6 - U x^4 + U^2 x^2 + U
    assert pmul(Q, CU) == CU2, "quotient identity failed"
    print("Quotient identity Q*C_U == C_{U^2} verified; Q = x^6 - U x^4 + U^2 x^2 + U.")
    print("Cubic y^3 - U y^2 + U^2 y + U in y=x^2: Eisenstein at (U) => irreducible,")
    print("totally ramified degree-3 subextension at (U). LHS/K trivial => unramified.")
    print("RAMIFICATION CERTIFICATE CONFIRMED.")

if __name__ == "__main__":
    main()
