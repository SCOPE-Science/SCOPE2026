# Independent mathematical audit

## correctness

PASS

Reconstructed the parity action from the local Lagrange polynomials and independently checked the exact Fourier trace, determinant, Schur–Cohn residual and compensation identity with audit-support/simpson_symbol.py. For 0<d<1 the determinant modulus is at most 1−d+d²<1 and the residual is strictly positive off the constant block, where the two eigenvalues are 1 and 1−2d. Reflection and a commuting two-node translation transfer this to the second half of the Courant interval. At f=1 the cyclic permutation has a unique normalized invariant but no general convergence, consistent with the Finding. Simpson integration and subtracting the two parity weightings give the exact checkerboard extremum. Products preserve the Simpson row precisely when the ordered scalar equation holds; the given radical solves it with both displacements nonresonant. The supplied finite checker was inspected, not executed.

## originality

FAIL

The earlier paper gives both the same zero-mode matrix through its printed stencil and the same strict Fourier contraction, including the exact Schur residual. The stationary mass, resonances, bias and compensation equation are direct two-by-two algebra from that earlier update, not a distinct result beyond its implications. The paper does not explicitly state Simpson conservation or the compensation curve; this is a finding of coverage by implication, not a claim of verbatim prior publication.

## value

FAIL

The difference between reconstructed and conserved mass is physically motivated, and the formula is pedagogically useful. But the exact same prior stencil and strict contraction already dictate the entire fixed-grid classification; the two-step result is a single multiplication of the published zero-mode matrices, with no additional stability or useful smooth-grid conclusion. Under the scientific standard this is a mechanically implied exact invariant, not a surviving distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
