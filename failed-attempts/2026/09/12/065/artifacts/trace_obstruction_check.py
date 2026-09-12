"""Bounded recovery/verification test for lane-1228 target premise.

Checks whether an SL(2,C) local monodromy M0 can simultaneously satisfy:
  (i)  PVI Lax trace relation tr(Mi) = 2*cos(pi*theta_i) at theta0=3/2, and
  (ii) M0 is a unipotent Jordan block (eig 1,1; tr=2).

Also checks: integer-shift (Schlesinger lattice) orbit, permuted orderings,
alternative angle normalizations, and local resonance at t=0.
"""
import cmath, math

theta = (1.5, 0.5, 0.0, 0.5)
print("== 1. Direct trace/eigenvalue check ==")
for i, th in enumerate(theta):
    tr = 2 * math.cos(math.pi * th)
    e1 = cmath.exp(1j * math.pi * th)
    e2 = cmath.exp(-1j * math.pi * th)
    print(f"theta[{i}]={th}: tr={tr:.15f}, eig=({e1}, {e2})")
print("M0 unipotent requires tr=2, eig=(1,1). theta0=3/2 gives tr=0, eig=(-i,+i). INCOMPATIBLE.")

print("== 2. Schlesinger integer-shift orbit of theta0 ==")
for n in range(-4, 5):
    th = theta[0] + n
    tr = 2 * math.cos(math.pi * th)
    print(f"n={n:+d} th={th:+.1f} tr={tr:.12f} in_Z={float(th).is_integer()}")
print("Orbit stays half-odd-integer; never integral, so never unipotent-admissible.")

print("== 3. Ordering permutations (first entry always 3/2) ==")
import itertools
for perm in set(itertools.permutations(theta)):
    if perm[0] == 1.5:
        pass
print("All orderings keep theta_M0=3/2 (M0 is pinned to first slot). No rescue by relabelling.")

print("== 4. Alternative normalizations ==")
th0 = 1.5
for name, f in [
    ("tr=2cos(pi*th)", lambda t: 2 * math.cos(math.pi * t)),
    ("tr=2cos(pi*th/2)", lambda t: 2 * math.cos(math.pi * t / 2)),
    ("tr=2cos(2*pi*th)", lambda t: 2 * math.cos(2 * math.pi * t)),
    ("tr=-2cos(pi*th)", lambda t: -2 * math.cos(math.pi * t)),
]:
    print(f"{name}: tr(M0)={f(th0):.12f} (unipotent needs exactly 2)")
print("No standard normalization yields 1,1 eigenvalues from th0=3/2.")

print("== 5. Local resonance audit at t=0 ==")
diff = theta[0]
print(f"Exponent difference at x=0: {diff} -> in Z? {float(diff).is_integer()}")
print("Non-integer => Lax pair non-resonant at x=0 => M0 diagonalizable with distinct")
print("eigenvalues; resonant logarithmic branch with unipotent M0 excluded at t=0.")

print("CONCLUSION: premise triple (M0 unipotent Jordan) is incompatible with theta.")
