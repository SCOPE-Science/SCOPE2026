import math

# Exact radial quadratic model h(z)=|z|^2/2 with total cap coefficient C.
# The formulas below check the constants in the two-dimensional asymptotics.
C = math.pi

for t in (1e2, 1e4, 1e6):
    # tau = t + A, A = sqrt(tau/C).  Set y=sqrt(tau) and solve exactly.
    y = (1 / math.sqrt(C) + math.sqrt(1 / C + 4 * t)) / 2
    tau = y * y
    q = 1 / math.sqrt(C * tau)
    A = math.sqrt(tau / C)
    phi = q / (2 - q)
    A_prime = 1 / (2 * math.sqrt(C * tau) - 1)

    mass_residual = C * tau * q * q - 1
    time_residual = tau - t - A
    phi_residual = phi - A_prime

    print(
        f"t={t:.0e} "
        f"mass_residual={mass_residual:.3e} "
        f"time_residual={time_residual:.3e} "
        f"phi_residual={phi_residual:.3e} "
        f"q_ratio={q * math.sqrt(C * t):.12f} "
        f"A_ratio={A * math.sqrt(C / t):.12f} "
        f"phi_ratio={2 * phi * math.sqrt(C * t):.12f}"
    )

# The universal rescaled cap has mass pi in two dimensions.
# Area = 2*pi and integral of h=|y|^2/2 over |y|<sqrt(2) is pi.
cap_mass = math.pi
cap_area = 2 * math.pi
cap_h_moment = math.pi
print(f"cap_mass={cap_mass:.12f} cap_area={cap_area:.12f} cap_h_moment={cap_h_moment:.12f}")
