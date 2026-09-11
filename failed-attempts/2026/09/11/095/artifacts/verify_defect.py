"""Verify the area-defect ledger for the pi/4 two-plane cone competitor.

Uses only integer arithmetic plus the hexagon bound pi > 3.
Run: python3 verify_defect.py
"""
import math

fail = []
def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (" | " + detail if detail else ""))
    if not cond:
        fail.append(name)

# 1. sqrt(2) enclosure by integer squares
check("14142^2 < 2*10^8", 14142**2 < 2 * 10**8, f"{14142**2} < {2*10**8}")
check("2*10^8 < 14143^2", 2 * 10**8 < 14143**2, f"{2*10**8} < {14143**2}")

# Hence 1.4142 < sqrt(2) < 1.4143, so 2 - sqrt(2) < 2 - 1.4142 = 0.5858.
# 2. delta0 = sqrt(2-2c), c=sqrt2/2, so delta0^2 = 2 - sqrt(2) < 0.5858 < 0.766^2.
lhs = 766**2 * 10**4  # 0.766^2 * 10^10 scaled
rhs = 5858 * 10**6    # 0.5858 * 10^10
check("delta0<0.766 via integers", lhs > rhs, f"{lhs} > {rhs}")
delta0_num = math.sqrt(2 - math.sqrt(2))
check("numeric delta0 < 0.766", delta0_num < 0.766, f"delta0~{delta0_num:.10f}")

# 3. |dt F| <= rho pointwise: (1-l*u)^2 + l^2*u*(1+c) = 1 - 2*l*u*(1-l) <= 1.
# Check identity coefficient: u + 1 + c = 2 with u = 1 - c.
c = math.sqrt(2) / 2
u = 1 - c
check("coefficient identity u+1+c==2", abs(u + 1 + c - 2) < 1e-15, f"{u+1+c}")
worst = max((1 - l*u)**2 + l**2 * u * (1 + c) for l in [i/1000 for i in range(1001)])
check("Jacobian factor <= 1 on grid", worst <= 1.0 + 1e-12, f"max={worst:.12f}")

# 4. Defect ledger: Delta >= (pi/2)(1 - 0.766) > (3/2)(0.234) = 0.351 > 0.02.
# pi > 3 from inscribed regular hexagon (perimeter 6 < 2*pi).
defect_lo = 3 * (1 - 0.766) / 2  # = 0.351
check("pi>3 hexagon bound assumed", math.pi > 3, f"pi~{math.pi:.10f}")
check("defect lower bound 0.351", abs(defect_lo - 0.351) < 1e-12, f"{defect_lo}")
check("defect >= 0.02 with margin", defect_lo >= 0.02, f"{defect_lo} >= 0.02")

# 5. True saving with actual constants (cross-check, not needed for certificate).
true_saving = math.pi / 2 * (1 - delta0_num)
check("true saving ~0.37", true_saving > 0.35, f"{true_saving:.6f}")

print("RESULT: " + ("VERIFY_OK" if not fail else f"VERIFY_FAIL {fail}"))
