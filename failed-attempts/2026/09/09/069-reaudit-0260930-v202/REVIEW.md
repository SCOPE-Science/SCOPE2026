# Review status

Fresh independent audit outcome: **failed**.

- Correctness: **PASS** — For tau=sigma^5 of type 3-(15;3), the odd-order fixed-code projection has dimension (15+3)/2=9 and the complementary component has binary dimension 15 with no nonzero tau-fixed vector. Hence its nonzero words would occur in orbits of size 3, forcing 3 to divide 2^15-1, which is false. The independent rho=sigma^3 type 5-(9;3) check analogously forces 5 to divide 2^18-1, also false.
- Originality: **FAIL** — The headline is a direct specialization of classical odd-prime automorphism decomposition for binary self-dual codes. Conway-Pless fixed-code self-duality is explicitly recalled by Borello-Nebe, and Yorgov's standard decomposition identifies the moving component with a Hermitian self-dual extension-field code when the order condition holds; for p=3 and 15 moving 3-cycles this requires a self-dual length-15 component, impossible by dimension. The order-15 literature already develops the same decomposition framework.
- Value: **FAIL** — Once the standard odd-prime decomposition is applied to sigma^5, the exclusion is a short parity/dimension corollary. It does not close a separately motivated unknown case or add a new structural lemma beyond the classical framework.
