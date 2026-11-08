# Review of the three-source Fourier cluster result

## Correctness
**PASS.** The weighted moment assumption ensures \(\mu_2>0\) and \(\Delta>0\). A three-term Fourier expansion, the exterior-square and exterior-cube singular-product identities, and explicit Vandermonde algebra prove the exact coefficient. The shape factor has a unique maximum at the midpoint; the largest singular value tends to \(\sqrt3\). The accompanying high-precision checks support, but do not establish, the limiting theorem.

## Originality
**PASS, provisional.** The 2018 and 2019 Batenkov-led papers establish sharp *scaling exponents* and two-sided bounds for the same type of matrix, and they explicitly acknowledge classical equispaced/prolate analysis. The present claim is restricted to the exact constant and universal weighted-aperture design comparison, which are not stated by those inspected theorems. Kunis–Nagel analyze two-node collisions, not the three-node shape optimum. Residual risk: an older confluent-Vandermonde or prolate analysis could yield this constant implicitly.

## Mathematical value
**PASS.** In three-source superresolution, the quadratic loss in the smallest singular value translates directly into amplitude noise amplification. The theorem gives its exact physically normalized coefficient and, under a fixed source diameter, identifies the uniquely best internal source geometry independent of symmetric sensor apodization. This is a natural design question rather than an arbitrary numerical instance.

## Scope and limits
The optimization concerns only the *leading small-separation coefficient* for a fixed finite frequency set and fixed source shape; it is not an exact finite-separation minimax or a nonlinear source-location guarantee. The sharp power of two was previously known and is not claimed new.

Self-review: passed. Independent audit: not yet performed.
