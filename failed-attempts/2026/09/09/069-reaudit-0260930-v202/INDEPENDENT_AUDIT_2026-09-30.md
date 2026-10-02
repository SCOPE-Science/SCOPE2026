# Independent mathematical audit — SCOPE-20260909-069

Outcome: **FAILED**.

## Correctness
**PASS** — For tau=sigma^5 of type 3-(15;3), the odd-order fixed-code projection has dimension (15+3)/2=9 and the complementary component has binary dimension 15 with no nonzero tau-fixed vector. Hence its nonzero words would occur in orbits of size 3, forcing 3 to divide 2^15-1, which is false. The independent rho=sigma^3 type 5-(9;3) check analogously forces 5 to divide 2^18-1, also false.

## Originality
**FAIL** — The headline is a direct specialization of classical odd-prime automorphism decomposition for binary self-dual codes. Conway-Pless fixed-code self-duality is explicitly recalled by Borello-Nebe, and Yorgov's standard decomposition identifies the moving component with a Hermitian self-dual extension-field code when the order condition holds; for p=3 and 15 moving 3-cycles this requires a self-dual length-15 component, impossible by dimension. The order-15 literature already develops the same decomposition framework.

## Value
**FAIL** — Once the standard odd-prime decomposition is applied to sigma^5, the exclusion is a short parity/dimension corollary. It does not close a separately motivated unknown case or add a new structural lemma beyond the classical framework.

## Source inspections
- **Borello-Nebe, On involutions in extremal self-dual codes and the dual distance of semi self-dual codes, arXiv:1401.6036** — Abstract/full bibliographic record inspected; explicitly recalls the Conway-Pless theorem that the natural projection of the fixed code for an odd-prime automorphism of a binary self-dual code is self-dual. Consequence: standard fixed-code half of the proof is prior
- **Bouyuklieva-Willems-Yankov, Binary self-dual codes with automorphisms of composite order, IEEE Trans. Inf. Theory 50 (2004), DOI 10.1109/TIT.2003.822598** — Primary abstract and section structure inspected; the paper develops decomposition for odd composite order and has a dedicated section for odd-prime automorphisms. Consequence: same order-15 decomposition framework is prior
- **Yorgov odd-prime decomposition theorem as reproduced in Topics in Finite Fields (Theorem 2.2)** — The theorem text was inspected: when s(p)=p-1, self-duality is equivalent to self-duality of the fixed projection and Hermitian self-duality of the moving extension-field component. Consequence: for p=3, moving length 15 is impossible by half-dimension

## Residual risk
See the accompanying JSON audit for the explicit residual-risk record.
