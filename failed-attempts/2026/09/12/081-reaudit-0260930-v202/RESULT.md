# Ordinary-trace non-summability for the Kaad-Kyed Dirac at t=q=1/2

## Corrected status
This record gives an explicit ordinary-trace non-summability witness for the Kaad-Kyed operator D_{t,q}. The calculation is correct, but it is a corollary/explicitization of already-known non-compactness in the t=q specialization, not a new dimension-spectrum theorem. Kaad-Kyed state that D_{q,q} agrees with the Kaad-Senior Dirac operator; Kaad-Senior already emphasize that its resolvent becomes compact only relative to a semifinite trace, not in the ordinary operator sense.

## Witness
Set t=q=1/2. On the one-dimensional boundary blocks V^n_{i0}=C(u^n_{i0},0), the horizontal term vanishes by the stated U_q(su2) pairing formulas. The vertical eigenvalue is

e_n = (t^{n+1}-1)/(t^{-1}-t).

Hence at t=1/2, e_n -> -2/3 and |e_n|>=1/2. For each n there are n+1 orthogonal vectors indexed by i=0,...,n. Therefore D has an infinite orthogonal family of eigenvectors whose eigenvalues stay in a compact interval bounded away from infinity. The ordinary resolvent is not compact.

For every real s, the positive-operator trace satisfies

Tr(|D|^{-s}) >= sum_{n>=1} (n+1)|e_n|^{-s}=+infinity.

For complex z, the appropriate conclusion is that the ordinary operator trace defining Tr(|D|^{-z}) has no half-plane of trace-class convergence; it should not be described as the extended-real value +infinity for non-real z. Thus the proposed ordinary-trace zeta function has no initial convergence half-plane from which a meromorphic continuation could be taken.

## Reproducibility
`artifacts/eigenvalue_check.py` checks the eigenvalue formula and divergent partial sums. `artifacts/kk_formulas.txt` records the formulas used from Kaad-Kyed.

## Originality and value
The explicit boundary-block derivation is a useful warning against applying an ordinary 1-2-3 dimension-spectrum ansatz to this operator, but the underlying ordinary-resolvent obstruction is not new for the t=q case. Any novelty claim should be limited to this concise derivation and its application to the proposed zeta question.

## References
- J. Kaad and D. Kyed, *The quantum metric structure of quantum SU(2)*, arXiv:2205.06043.
- J. Kaad and R. Senior, *A twisted spectral triple for quantum SU(2)*, arXiv:1109.2326.
