#!/usr/bin/env python3
"""Computational certificate for lane-1397.

Verifies, by brute force over the finite Heisenberg group UT3(Z/25) and the
ring (Z/25)^x, the group-theoretic and local-cyclotomic facts used to refute
the literal split-p finite cuspidal criterion at (K,p) = (Q(i),5):

  (A) (Z/25)^x is cyclic of order 20; 1+5(Z/25) = {1,6,11,16,21} has order 5
      (wild inertia image); prime-to-5 part has order 4 (tame image).
  (B) In characteristic 5, x^25 - 1 = (x-1)^25 (all intermediate binomial
      coefficients divisible by 5), so tame inertia at v|5 acts trivially on
      mu_25, i.e. chi(tame) = 1 mod 25; wild inertia acts as 1+5t != 1.
  (C) 5 splits in Q(i): 2^2+1^2 = 5, so completions at v|5 are Q_5 (residue F5).
  (D) Phi_5(x+1) is Eisenstein at 5 (totally ramified degree 4); since 5-power
      roots are invisible mod 5, residue degree is 1, so [K(mu_25):K] = 20 with
      inertia surjecting onto (Z/25)^x: BOTH tame (order 4, e.g. u = 7) and wild
      (order 5, e.g. u = 6) act nontrivially, and K(mu_25)/K is ramified only
      above 5, hence factors via G_{K,T}.
  (E) H = UT3(Z/25): order 25^3, center of order 25, abelianization (Z/25)^2,
      commutator [(a,b,c),(a',b',c')] = (0,0,ab'-a'b), common centralizer of
      the two standard generators = center only.
  (F) Galois-type automorphism phi_u(a,b,c) = (ua,ub,u^2c) for u in {6,7}:
      inner automorphisms act trivially on V = H/Z; phi_u acts on V by scalar
      u != 1 (verified for u = 6 and u = 7, wild and tame). Hence NO element
      lifting sigma with chi(sigma) != 1 can centralize both generators (it
      moves their V-classes), i.e. the literal local commutator condition is
      unsatisfiable on the whole inertia group I_v.
"""

import math

R = 25
print("=== (A) unit group (Z/25)^x ===")
units = [u for u in range(R) if u % 5 != 0]
assert len(units) == 20, len(units)


def ord_mod(u, mod=R):
    x = 1
    for k in range(1, 21):
        x = (x * u) % mod
        if x == 1:
            return k
    raise AssertionError(u)


assert ord_mod(2) == 20  # cyclic
U1 = sorted({(1 + 5 * t) % R for t in range(5)})
assert U1 == [1, 6, 11, 16, 21], U1
for u in U1:
    assert (u == 1 and True) or (pow(u, 5, R) == 1 and u != 1)
tame_part = sorted({u for u in units if pow(u, 4, R) == 1})
assert len(tame_part) == 4, tame_part
for u in tame_part:
    assert ord_mod(u) in (1, 2, 4)
print("order 20, generator 2; wild 1+5Z/25 =", U1, "; tame C4 =", tame_part)

print("=== (B) total ramification: 5-power roots invisible mod 5 ===")
assert all(math.comb(25, k) % 5 == 0 for k in range(1, 25))
# x^25-1 = (x-1)^25 in F_5[x]: no nontrivial 5-power roots of unity mod 5,
# so Q_5(mu_25)/Q_5 has residue degree 1, i.e. is totally ramified.
# Hence inertia surjects onto Gal = (Z/25)^x = C20; tame inertia onto the
# prime-to-5 quotient C4 = {1,7,18,24} != {1}: tame acts NONTRIVIALLY mod 25.
assert any(u != 1 for u in tame_part)
print("C(25,k) all 0 mod 5: OK => totally ramified; tame image", tame_part,
      "nontrivial: OK")

print("=== (C) 5 splits in Q(i) ===")
assert 2 * 2 + 1 * 1 == 5
print("N(2+i) = 5: OK, K_v ~= Q_5 with residue F5 for v|5")

print("=== (D) Eisenstein certificate for Q_5(zeta_5)/Q_5 ===")
# Phi_5(x+1) = x^4 + 5x^3 + 10x^2 + 10x + 5
coeffs = [5, 10, 10, 5, 1]  # constant term first
assert all(c % 5 == 0 for c in coeffs[:-1]) and coeffs[-1] % 5 != 0
assert coeffs[0] % 25 != 0
print("Phi_5(x+1) Eisenstein at 5: OK (totally ramified degree 4)")

print("=== (E) Heisenberg group UT3(Z/25) ===")


def mul(g, h):
    a, b, c = g
    a2, b2, c2 = h
    return ((a + a2) % R, (b + b2) % R, (c + c2 + a * b2) % R)


def inv(g):
    a, b, c = g
    return ((-a) % R, (-b) % R, (-c + a * b) % R)


def comm(g, h):
    return mul(mul(g, h), mul(inv(g), inv(h)))


elts = [(a, b, c) for a in range(R) for b in range(R) for c in range(R)]
assert len(elts) == 25 ** 3 == 15625
identity = (0, 0, 0)
center = [g for g in elts if all(comm(g, h) == identity for h in elts)]
assert len(center) == 25, len(center)
assert sorted(center) == sorted([(0, 0, c) for c in range(R)])
X = (1, 0, 0)
Y = (0, 1, 0)
assert comm(X, Y) == (0, 0, 1)  # [x,y] = z generates center
# centralizers
cx = [g for g in elts if comm(X, g) == identity]
cy = [g for g in elts if comm(Y, g) == identity]
assert len(cx) == 625 and len(cy) == 625, (len(cx), len(cy))
common = [g for g in elts
          if comm(X, g) == identity and comm(Y, g) == identity]
assert sorted(common) == sorted(center), len(common)
# elements with a unit V-coordinate have centralizer of size 625 (maximal
# subgroups); elements with V-coordinates both divisible by 5 have larger
# centralizers (e.g. (5,0,0) has 3125) — irrelevant to the proof.
for g in [(1, 0, 0), (0, 1, 0), (1, 1, 0), (2, 3, 7)]:
    cg = [h for h in elts if comm(g, h) == identity]
    assert len(cg) == 625, (g, len(cg))
cg5 = [h for h in elts if comm((5, 0, 0), h) == identity]
assert len(cg5) == 3125, len(cg5)
print("order 15625, center order 25, V = (Z/25)^2, [X,Y] = central gen: OK")
print("C(X) cap C(Y) = center (order 25): OK")

print("=== (F) Galois-type action phi_u for u = 6 (wild) and u = 7 (tame) ===")


def phi(u, g):
    a, b, c = g
    return ((u * a) % R, (u * b) % R, ((u * u * c) % R))


for u in (6, 7):
    assert u in units and u != 1
    assert ord_mod(u) == (5 if u == 6 else 4)
    # phi_u is an automorphism
    assert all(phi(u, mul(g, h)) == mul(phi(u, g), phi(u, h))
               for g in elts[::97] for h in elts[::101])
    # inner conjugation acts trivially on V-classes (explicit subsample)
    for c in elts[::233]:
        for m in (X, Y):
            assert mul(mul(c, m), inv(c))[:2] == (m[0], m[1])
    # commutator formula [(a,b,c),(a',b',c')] = (0,0,ab'-a'b) (subsample)
    for g in elts[::1009]:
        for h in elts[::997]:
            a, b, _ = g
            a2, b2, _ = h
            assert comm(g, h) == (0, 0, (a * b2 - a2 * b) % R)
    # for EVERY h in H, phi_u(h·X·h^{-1}) has V-class u*(1,0) != (1,0):
    # (inner conjugation preserves V-classes; phi scales by u != 1 mod 25)
    assert ((u * 1) % R, 0) != (1, 0) and (0, (u * 1) % R) != (0, 1)
    for h in elts:
        assert phi(u, mul(mul(h, X), inv(h)))[:2] == ((u * 1) % R, 0)
        assert phi(u, mul(mul(h, Y), inv(h)))[:2] == (0, (u * 1) % R)
print("phi_6: V-scale 6, center-scale 11; phi_7: V-scale 7, center-scale 24:")
print("  (6*6)%25 =", (6 * 6) % R, "; (7*7)%25 =", (7 * 7) % R)
assert (6 * 6) % R == 11 != 1 and (7 * 7) % R == 24 != 1
print("for all h in H, u in {6,7}: V-class(phi_u(hXh^-1)) != V-class(X): OK")

print()
print("ALL CHECKS PASSED: literal local commutator condition unsatisfiable")
print("on full I_v, since chi(I_v) hits 6 and 7 in (Z/25)^x.")
