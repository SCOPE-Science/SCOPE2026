"""Finite diagnostics for the integer-power Fock density. Standard library only."""
import math


def logsum(values):
    largest = max(values)
    return largest + math.log(sum(math.exp(z - largest) for z in values))


def ratio(m, alpha, a, gamma, x):
    c = alpha * (1 - a ** m) / 2
    r = (x / c) ** (1 / m)
    y = alpha ** (2 / m) * a * a * r * r
    limit = int(8 * m * alpha * a ** m * r ** m + 200)
    kernel_terms = [n * math.log(y) - math.lgamma((2 * n + 2) / m)
                    for n in range(limit)]
    log_kernel = math.lgamma(2 / m) + logsum(kernel_terms)
    limit = math.ceil(x + 14 * math.sqrt(x) + 50)
    angular_terms = [2 * k * math.log(x) - 2 * math.lgamma(k + 1 + gamma)
                     for k in range(limit + 1)]
    log_angular = logsum(angular_terms)
    log_density = (math.log(m * alpha ** (2 / m) / math.gamma(2 / m))
                   + math.log(r) - alpha * r ** m
                   + log_kernel + log_angular)
    const = (m * m * alpha * a ** (m - 2) / (4 * math.sqrt(math.pi))
             * c ** (-2 * gamma - 0.5))
    log_asymptotic = (math.log(const)
                      + (m / 2 - 1 - 2 * m * gamma) * math.log(r))
    return math.exp(log_density - log_asymptotic)


def main():
    count = 0
    for m in (1, 2, 3, 4, 6):
        for gamma in (0.10, 0.25, 0.60):
            near = ratio(m, 1.3, 0.6, gamma, 150)
            far = ratio(m, 1.3, 0.6, gamma, 500)
            assert abs(near - 1) < 0.003, (m, gamma, near)
            assert abs(far - 1) < abs(near - 1), (m, gamma, far, near)
            count += 2
    print(f"PASS: {count} finite radial-kernel/coefficients asymptotic diagnostics")


if __name__ == '__main__':
    main()
