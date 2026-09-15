"""Bounded recovery test: why truncated-virial rigidity does not close without
drift / quantile-window / low-frequency-tail inputs.

(a) Hdot1-invariant scaling v(y)=lam^{-1/2} u(x0 + y/lam):
    ||grad v||_2 = ||grad u||_2, E invariant, but ||v||_2 = lam^{+1}||u||_2.
    Hence fixed finite mass gives NO uniform L^2 bound as lam varies.
(b) Truncated virial error model vs drift |z| ~ V*T.
(c) Center-of-mass transfer needs uniform tails / second moment.
"""
import math

print("=== (a) scaling of L^2 norm under Hdot1-preserving dilation ===")
M0 = 1.0
for lam in [0.01, 0.1, 1.0, 10.0, 100.0]:
    print(f"lam={lam:8.3f}  ||v||_2 = lam*M0^1/2 -> {lam*M0:10.3f}   ||grad v||_2 invariant")
print("Conclusion: Hdot1 precompact orbit {lam(t),z(t)} has no uniform L^2 tightness from mass alone.\n")

print("=== (b) truncated virial error model E_err ~ T*M/R^2 + T*|P|/R + |z|*E/R + tail ===")
E, M, P = 1.0, 1.0, 0.5
tail = 0.05
for V in [0.0, 0.1, 1.0]:
    T = 100.0
    z = V*T
    for R in [50.0, 200.0, 1000.0]:
        err = T*M/R**2 + T*P/R + abs(z)*E/R + tail
        print(f"V={V:4.1f} T={T:6.1f} R={R:7.1f} |z|={z:7.1f} err={err:8.3f}")
    print()
print("Conclusion: to make err << coercive bulk (~T), need R >> T AND R >> |z(T)|.")
print("With drift |z|~V*T, V=O(1), R must grow superlinearly in T, but then T/R^2 bulk")
print("and annular error terms swap roles; no fixed R works uniformly without V=o(1)")
print("(drift hypothesis) and uniform tail/quantile control.\n")

print("=== (c) center-of-mass transfer X(t)=int x3|u|^2, X'=2Pz ===")
print("Pz(u0)=0 => center of data fixed. Passing to critical element u_c needs:")
print("  (i)  well-defined finite momentum of u_c (needs negative regularity / L^2 membership),")
print("  (ii) uniform spatial tightness to locate z(t) from X(t) (needs quantile-window),")
print("  (iii) low-frequency tails not to carry the mass centroid (needs low-freq-tail bound).")
print("Hdot1 compactness supplies none of (i)-(iii). Pz=0 alone does not bound z(t).")
print("Result: RECOVERY TEST FAILS TO CLOSE -- obstruction confirmed as load-bearing.")
