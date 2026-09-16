"""Bounded recovery test: can a microscopic s=3/2+eta close with R^eps loss?
Models the irreducible polynomial deficit delta(eta)=(s-3/2)*(1/2-1/p),
p=2+2/s, from the incidence/broad-narrow balance. Prints deficit exponents.
Conclusion: deficit is fixed polynomial power, not absorbable in R^eps.
"""
for eta in [0.0, 0.01, 0.05, 0.10, 0.25, 0.50]:
    s = 1.5 + eta
    p = 2 + 2 / s
    delta = (s - 1.5) * (0.5 - 1 / p)
    print(f"eta={eta:.2f} s={s:.2f} p={p:.4f} deficit R^{delta:.5f} | absorbable-in-eps={delta==0.0}")
