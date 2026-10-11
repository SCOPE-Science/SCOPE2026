# Independent mathematical audit

## correctness

PASS

Hessian diagonalization decouples the dynamics. For one curvature mode \(q=\eta h\), the submitted state matrix has trace \(T=1+\alpha-q[1+\lambda(1-\alpha)]\) and determinant \(D=\alpha(1-q)\). The exact Jury expressions reduce to \(q(1-\alpha)(1+\lambda)\), \(2(1+\alpha)-q[(1+\alpha)+\lambda(1-\alpha)]\), and \(1-\alpha+\alpha q\); in the stated parameter range only the middle expression restricts stability. The largest curvature therefore gives the claimed iff threshold, and equality makes the characteristic polynomial vanish at \(-1\). The z-transform of the EMA gives \(A(-1)=1+\lambda(1-\alpha)/(1+\alpha)\), so the Nyquist expression is algebraically identical. The bundled randomized verifier corroborates the identities and the quoted numerical examples.

## originality

FAIL

The Grokfast source already specifies the exact EMA recurrence and residual gradient amplification. On a diagonalized quadratic, these equations give a two-state real linear recurrence immediately, and the submitted learning-rate ceiling follows by applying the standard second-order Jury/Schur criterion. The Nyquist formulation is then just evaluation of the already-given first-order EMA transfer function at \(z=-1\). Under the required implication standard this is a routine control-theory specialization, even though the source paper does not print the final formula.

## value

FAIL

The formula is useful as a practitioner-facing sanity check, but scientifically it is a routine application of Hessian diagonalization and the textbook Jury test to the source's two-state EMA recurrence. The Nyquist identity is the same inequality rewritten through the elementary transfer function, so no independently valuable mathematical gap remains under the required bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
