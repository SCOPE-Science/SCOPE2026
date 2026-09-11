"""Grade-vanishing certificate for lane-680 target (p=5 V(1) stem-56 s=2).

Proves E2^{s,t}=0 unless 8|t, so bidegree (t-s=56,s=2), t=58, is empty.
Enumerates BP generator degrees and exhausts cobar monomial sums in window.
Stdlib only. Emits machine-readable log lines + VERIFY_OK.
"""
p = 5
q = 2*(p-1)  # 8
# generator degrees |vi| = 2(p^i - 1), |ti| = 2(p^i - 1)
def vdeg(i): return 2*(p**i - 1)

print(f"p={p} q=2(p-1)={q}")
for i in range(1, 6):
    d = vdeg(i)
    print(f"|v{i}|=|t{i}|={d} mod{q}={d % q}")
    assert d % q == 0

# claimed bidegree
stem, s = 56, 2
t = stem + s
print(f"claimed stem={stem} s={s} t={t} t mod {q} = {t % q}")
assert t == 58 and t % q == 2, "arithmetic"
print(f"BINCHECK t=58 mod8=2 nonzero -> cobar concentrated 0 mod 8 so E2^{s},{t}=0")

# Exhaust: any cobar monomial degree = deg(m) + sum deg(t_{i_k}) with
# deg(m) in ideal quotient (sums of v-degrees) and each t-degree 0 mod q
# => total 0 mod q. Enumerate small monomials to illustrate, then general lemma.
mods = set()
import itertools
vdegs = [vdeg(i) for i in range(1, 4)]  # v1..v3
tdegs = [vdeg(i) for i in range(1, 4)]
count = 0
for ev in itertools.product(range(4), repeat=3):
    dm = sum(e*d for e, d in zip(ev, vdegs))
    for sdeg in [0, 1, 2]:
        for et in itertools.product(range(3), repeat=max(1, sdeg)):
            dt = sum(e*d for e, d in zip(et, itertools.islice(itertools.cycle(tdegs), len(et)))) if sdeg else 0
            tot = dm + dt
            assert tot % q == 0
            count += 1
print(f"enumerated {count} cobar-monomial degree sums in window: all 0 mod {q}")
# d9 target bidegree
s2, t2 = s+9, t+9-1
print(f"d9 target s={s2} t={t2} stem={t2-s2} t mod{q}={t2 % q} -> also empty")
assert t2 - s2 == 55
assert t2 == 66 and t2 % q == 2
print("VERIFY_OK")
