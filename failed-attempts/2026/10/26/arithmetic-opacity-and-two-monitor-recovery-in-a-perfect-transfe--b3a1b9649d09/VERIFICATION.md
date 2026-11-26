---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Realizing the chain as the permutation-symmetric subspace of N spins with Hamiltonian the sum of their single-spin flips gives eigenvalues E=N−2k, simple in this subspace. The endpoint squared weights are binomial, from expanding the all-zero state in the flip eigenbasis. Dividing site amplitudes by their endpoint amplitude and multiplying by √binom(N,j) yields the polynomial recurrence E K_j=(N−j+1)K_{j−1}+(j+1)K_{j+1}. The first three terms give the stated K₂ and K₃. A real eigenvalue of the damped generator forces the vector into the kernel of the positive loss operator, so the real subspace is exactly the span of the K₃-zero eigenvectors of H_N. That subspace reduces the generator, and the remaining finite block decays. The side-root integer condition is 3N−2=s², with s automatically of the right parity and s≤N. The central root differs from the two side roots, and s of either parity coprime to three gives an infinite exceptional sequence. Taking the endpoint projection and averaging by trace gives the stated probabilities. Stirling at scaled displacement ±√(3−2/N) gives the e^(−3/2) side factors, while the center has factor one. The two loss sites cannot vanish together: K₂ on the dark levels equals −N/2 or N−1. Each former real eigenvalue is algebraically simple because its orthogonal complement in the dissipative decomposition has no additional copy. The left and right vectors there are the normalized Hermitian-chain eigenvector, so the first derivative is −i|u_k(2)|²/2. The two simplified coefficients follow directly. My recurrence and coefficient check used exact integers and fractions for 3≤N≤200. The frozen script's arithmetic loop is range(3,55), not through 70 as stated in RESULT.md; this discrepancy in advertised finite test coverage does not affect the analytic proof or this independent check.

## originality

FAIL

The arithmetic heart is an exact low-degree Krawtchouk zero classification appearing in an independently located paper. Its reliable priority relative to the frozen record is unresolved, so no assertion of earlier publication of that exact proposition is made. Independently of priority, the rest of the frozen scientific claim does not establish a distinct advance over the standard engineered-chain eigensystem, the nodal criterion, and direct low-degree evaluation: the parity classes read off the cubic, the survival constants apply binomial Stirling at its listed roots, and the adjacent-site recovery and slope are direct Jacobi recurrence and first-order diagonal perturbation. No nonroutine asymptotic or loss-opening result beyond these mechanical consequences is established. This is a judgment of scientific distinction, not a claim that a source prints the entire absorber theorem or that inaccessible papers contain it.

## value

FAIL

This is a natural Hamiltonian and the correct formulas are useful model calculations. The proposed arithmetic gap, however, is exactly the cubic nodal equation and its elementary evaluated zeros; the scaled survival weights are binomial Stirling at those zeros. Adding a neighboring monitor has a general immediate recurrence explanation, and its fixed-size linewidth here is just the site weight read from the first two recurrence steps. The remaining numerical constants do not amount to an independent unknown exact invariant not mechanically implied by these inputs. A uniform small-loss/large-size law or a genuinely new classification across detector positions would pose different questions, neither answered by the frozen record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
