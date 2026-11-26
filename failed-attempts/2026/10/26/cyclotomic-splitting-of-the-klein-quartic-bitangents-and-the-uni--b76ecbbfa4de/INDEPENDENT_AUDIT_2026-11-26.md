# Independent mathematical audit

## correctness

PASS

The gradient test gives 28(XYZ)^3=0 at a singular point, forcing a zero coordinate and then all zero at every permitted prime (in characteristic three the gradient consists of cubes). The rational line A=(1,1,1) restricts the quartic to minus a square. I checked the table independently in Z[z]/(Phi_7), without the frozen script: in basis 1,z,...,z^5 put B=A G S with coordinates (-1,0,0,-1,0,2), (-3,-2,-2,-2,-2,-3), (0,1,1,3,1,1). Direct cyclic polynomial multiplication modulo Phi_7 checks F(Sx)=49F(x), sigma_2(B)=(B_3,B_1,B_2) and sigma_6(B)=BG. The four seeds A,B,sigma_2(B),sigma_4(B) each give a 7-element orbit under G (two nonzero coordinates suffice), all lying among the bitangents since G and S preserve the curve projectively. Their projective orbits are distinct: G preserves coordinate absolute squares; the squared moduli of B sum to 21 and have distinct entries (their coefficient tuples are (6,0,-4,1,1,-4), (10,0,5,4,4,5), (5,0,-1,-5,-5,-1)), and the two conjugate vectors cyclically rotate them. A has uniform normalized coordinate moduli. This constructs all 28 geometric lines. Sigma_2 cycles the three non-A orbits and acts by j->2j on A G^j. Sigma_6 preserves each orbit and acts on indices by j->c-j, fixing one per orbit. The generator sigma_5=sigma_6 sigma_2 has only 3- and 6-cycles on the three non-A orbits together; its cube is sigma_6 with three fixed points there, so these are one 3-cycle and three 6-cycles. On the A orbit it adds one fixed point and one 6-cycle. The order-six permutation is faithful, which proves the minimal field. In characteristic not two, the odd theta-characteristic torsor component is finite étale of degree 28. On a plane quartic an odd theta characteristic has exactly one section by Clifford and parity, and doubling its effective divisor gives a unique canonical line, including hyperflexes. Smoothness and finite étale base change over Z[1/14] transport these permutations to each allowed Frobenius, sending z to z^q. Read the frozen finite-field certificate; dual row multiplication by a generator rather than its inverse produces the same orbit. The frozen script was not executed. Neither the exact check nor the theorem asserts rationality of tangency points.

## originality

FAIL

The arithmetic invariant is correct, but the same-model projective generators over Q(zeta_7) and a seed for their full 28-line orbit are explicit in Elkies, enabling a mechanical exact Galois orbit comparison; faithfulness reads off from the cycle lengths and the all-good-prime assertion follows by standard finite-étale specialization. The source does not have to print the resulting permutations to cover the calculation this directly. There is also a distinct exact full indexed match, dated later, which establishes catalogue overlap and is not used to infer earlier priority. The same-day characteristic-three result and the real bitangent count are narrower partial coverage, not sole grounds for failure.

## value

FAIL

The mod-7 table is a natural and useful presentation for applications, but as a standalone exact-invariant finding it recomputes data mechanically encoded by the prior explicit same-model orbit, then uses a standard unramified specialization. The finite-field computation and explicit table improve convenience and reproducibility without establishing a surviving scientifically distinct invariant or structural result in this frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
