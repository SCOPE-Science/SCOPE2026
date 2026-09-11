"""Scale-barrier certificate for lane-1045 (stdlib only).

Checks:
 1. SW log-power relative saving vs required N^{-1/120}: ratio -> infinity.
 2. VK sub-polynomial saving vs required: ratio -> infinity.
 3. GRH-conditional closure margin: ratio -> 0.
 4. sum_{q<=X} 1/phi(q)^2 convergence (~2.39): truncation tail is log-power only.
"""
import math


def phi(n):
    r = n
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            r -= r // p
        p += 1 if p == 2 else 2
    if x > 1:
        r -= r // x
    return r


print("== 1. SW (K=10 and K=2) vs required N^-1/120 ==")
for logN in [50, 100, 1000, 5000, 12000, 20000]:
    for K in (2, 10):
        attain = logN ** (-K / 2.0)
        req = math.exp(-logN / 120.0)
        print(f"logN={logN} K={K}: attain={attain:.3e} req={req:.3e} R={attain/req:.3e}")

print("== 2. VK ceiling vs required ==")
for logN in [50, 100, 1000, 5000, 12000]:
    vk = math.exp(-0.5 * logN ** 0.6 / max(math.log(logN), 1) ** 0.2)
    req = math.exp(-logN / 120.0)
    print(f"logN={logN}: vk={vk:.3e} req={req:.3e} R={vk/req:.3e}")

print("== 3. GRH margin: R = N^-59/120 (logN)^4 -> 0 ==")
for logN in [50, 100, 1000, 5000, 12000]:
    R = math.exp(-59 * logN / 120.0) * logN ** 4
    print(f"logN={logN}: R={R:.3e}")

print("== 4. sum_{q<=X} phi(q)^-2 ==")
s = 0.0
for q in range(2, 200001):
    f = phi(q)
    s += 1.0 / f / f
    if q in (1000, 10000, 100000, 200000):
        print(f"X={q}: S={s:.6f}")
print("ALL_SCALE_CHECKS_DONE")
