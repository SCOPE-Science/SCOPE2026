# FAILED ATTEMPT — NOT A VALIDATED FINDING

## Scientific disposition

The retained mathematical package was reassessed on correctness, originality, and value.

- Correctness: PASS. The power-map lemma is correct: writing \(e=db\), \(\ell=da\) with \(b\) odd shows \(\gcd(2^\ell+1,2^e-1)=1\), so every nonzero Lagrange coefficient has a unique \((2^\ell+1)\)-st root. Substituting those roots into the cited GRL dual equations, equality on the unscaled coordinates forces \(g=f^{2^\ell}\) by the degree bound; the extension equation kills the top \(s\) coefficients, and the scaled coordinates force exactly \(k-s-h\) prescribed roots. The converse gives an \(h\)-dimensional polynomial space. The inspected verifier independently checks the gcd identity and hundreds of generator-matrix hull dimensions, including \((e,\ell)=(5,2)\).
- Originality: FAIL. The primary GRL paper was inspected in full. Its Proposition III.2 already proves every hull dimension for arbitrary extension matrix whenever normalized Lagrange coefficients lie in the relevant power-root class, using exactly the multiplier scaling and root-count argument reproduced by the audited proof. In the odd-quotient binary regime, the sole extra step is the elementary identity \(\gcd(2^\ell+1,2^e-1)=1\), which makes that root condition automatic for every nonzero coefficient. Wan--Zhu already treat the same finite-field regime for GRS/EGRS hulls. Under the implication standard, this is covered.
- Value: FAIL. The parameter observation is useful for practitioners, but the mathematical work is essentially a substitution: a standard cyclic-group gcd identity makes every multiplier root exist, after which the published GRL hull construction runs unchanged. The distance-neutral statement is then a routine monomial-isometry fact. This is too mechanical to qualify as a separate valued finding under the stated bar.

Acceptance requires all three axes to pass. This package is retained as failed scientific evidence and is not a validated finding.

## Preserved evidence

The original result, slogan, metadata history, and reproducibility artifacts remain part of the archived package. The dated audit files record the literature comparison and residual risks.
