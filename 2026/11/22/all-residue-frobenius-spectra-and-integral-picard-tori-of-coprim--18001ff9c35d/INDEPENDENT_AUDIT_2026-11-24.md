# Independent mathematical audit

## correctness

PASS

The degrees of the two polynomial maps from the parameter line are m and n, so the intermediate function field has index dividing gcd(m,n)=1. Integrality of the parameter and the degree-m minimal relation then give the asserted affine normalization. In the stated characteristics the distinct Chebyshev critical points with the same critical value give exactly (m-1)(n-1)/2 nodes with nonsingular quadratic tangent cones. I checked label completeness directly: for any 1<=a<mn divisible by neither m nor n, choose k,l in the specified ranges with A=kn+lm congruent to a modulo mn. Either A represents a modulo 2mn or the B-label with k replaced by m-k does, because that label is A-mn. Conversely the proposed branches are different modulo sign, have the same image, and their indices are divisible by neither m nor n, so neither image coordinate is an endpoint and both are critical. The free involution (k,l)->(m-k,n-l) duplicates the unordered pairs; the preimage count proves there are no further identifications. Frobenius powers the roots of unity, and the nodal factor is the integral branch-ratio torus, with inversion exactly for a swap. The conductor unit quotient at the unique geometric branch at infinity has no torus, since the residue-unit factors cancel and only principal-unit quotients remain; Pic^0 of the normalization is zero. Positive and negative signed cycles give respectively the induced trivial and quadratic-sign integral lattices, not just rational factors. The normalization correction per rational node is 1 minus its number of rational preimages, which gives the signs in the point counts and both zeta formulas. Independent finite-field enumeration of the worked example returned 10 and 42 points and confirmed the seven distinct labeled nodes and signed orbit types. Replay: /workspace/branches/059122b1-fdb5-44ae-9859-01941256b9a8/independent_check.py and independent_check_output.txt in the same directory. The example does not prove the uniform statement; the geometric and lattice argument does. The frozen checker was inspected, not executed.

## originality

PASS

Credit the known parametrization and even the explicit geometric branch pairs, and credit the earlier exact zeta in the simultaneous signed subfamily. The independently supported distinction is the arithmetic signed-orbit computation on the paired branches for every unit residue and its integral descent to an explicit product of tori. The latter does not follow from a zeta polynomial or a point order. The standard local nodal torus construction and root-of-unity powering are inputs, not themselves attributed discoveries. No inspected result gives the all-residue paired-branch arithmetic together with the resulting torus; the example shows concrete scope beyond the closest earlier zeta formula.

## value

PASS

The precise integral isomorphism class of this natural generalized Jacobian torus, together with all extension-field counts, is finer than the known geometry, a single point count, or an isogeny class. The nonsigned example demonstrates the need for the extension by exhibiting both branch exchange and nontrivial node orbits. The result gives an exact arithmetic invariant uniformly without factorization, rather than an isolated parameter computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
