# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

**Disposition:** FAILED

## Correctness — PASS

Assuming the prior Kotwal--Menon closure parametrization \(W_k=V_kPV_{k-1}^*\) with \(V_0=I\) and \(V_N=Q\), the product telescopes to \(W_N\cdots W_1=QP^N\). Thus two labels through the same point differ by a unitary fixing \(E=\operatorname{im}P\) pointwise, and every such terminal-unitary change leaves the tuple unchanged, giving a \(U(d-r)\) label fiber. Pairwise and multiple intersections are exactly controlled by common equalizer subspaces. The fixed-rank dimension is \(2r(f-r)+r^2+(N-1)(d^2-(d-r)^2)=2r(f+(N-1)d)-Nr^2\). The \(N=2\) specialization agrees with the direct linear description. No internal mathematical error was found.

## Originality — FAIL

The final proof explicitly takes Kotwal--Menon's prior closure parametrization as its starting point, and the audited theorems are immediate stabilizer/equalizer/Grassmannian consequences of that parametrization. Under implication-based originality, unstated corollaries of a stronger prior structural description are covered even when the exact formulas were not printed.

The structured originality comparison, source inspections, checked sources, and residual risks are recorded in `INDEPENDENT_AUDIT_2026-10-01.json`.

## Scientific value — FAIL

The incidence formulas are clean and potentially useful, but the required value standard rejects routine deductions already mechanically implied by a stronger known parametrization. The audited result does not identify an independent mathematical gap beyond taking stabilizers, equalizers, and standard fixed-rank dimension counts.

## Limitations

- The linear-algebraic incidence formulas are correct if the cited Kotwal--Menon closure parametrization is used.
- The final claim is a short stabilizer/equalizer/Grassmannian deduction from that prior parametrization rather than an independent new mathematical gap.
- The full text of Kotwal's dissertation was not inspected; this does not rescue originality because the prior preprint parametrization already implies the claim.
