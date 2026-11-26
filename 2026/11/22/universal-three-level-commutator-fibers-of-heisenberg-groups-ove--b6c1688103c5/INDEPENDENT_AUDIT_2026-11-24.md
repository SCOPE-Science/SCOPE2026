# Independent mathematical audit

## correctness

PASS

The commutator is the standard alternating dot product and the independent central coordinates contribute exactly t^2. An independent count avoids splitting the ring or using a generating character. Set n=2h, regroup into a pairing of two n-tuples, and fix the first tuple. The image of the pairing is its generated ideal and each target in the image has t^n divided by the ideal size preimages. If the tuple has a unit, this contributes (t^n-v^n)t^{n-1}=A-B to every target. Otherwise the image is the residue-field span of its coordinates in the radical, since the radical squares to zero. For a uniform radical tuple regarded as a linear map F_q^n to the radical, E(q^{-rank})=q^{-n}(1+(q^n-1)/v), by counting vectors in the kernel (each nonzero vector is sent to zero with probability 1/v). The zero fiber then receives the additional t^n v^n E(q^{-rank})=qB+(t-q)C. All nonzero radical targets receive the same additional weight by the GL_d action on the radical tuples and targets; their additional total, together with that at zero, is t^n v^n, giving q(B-C) for each nonzero target. Thus the precise three stated levels hold also in mixed characteristic. The level gaps tC and q(B-C) are positive and the unit level is positive. Pairing with coordinate unit vectors identifies the center; it equals the image and hence the derived subgroup. Dividing the zero count by t^{4h} gives the displayed commuting probability, and (v/t)^{4h}=q^{-4h} of all pairs have both horizontal vectors in the radical and automatically commute. The limiting fraction is conditional, not a claim that ordinary commuting probability tends to one. The provided checker and recorded output were inspected, not executed. Independently `python /workspace/branches/audit_checks.py heisenberg` checked rank one and two over the eight-element split ring by product-distribution convolution and verified the four-level Z/8 determinant comparator by direct enumeration.

## originality

PASS

The inspected fixed-determinant work covers principal rings, including the Z/8 comparison, not the nonprincipal square-zero family. Work covering the same coefficient rings studies other invariants. The contribution is the evaluation for all central targets and symplectic ranks in this nonprincipal class, not the general character-sum method, determinant counts for principal rings, or mere centrality of commutators.

## value

PASS

Prescribed commutators refine ordinary commuting probability and connect directly to a natural determinant-counting question for local rings outside the classical principal class. The theorem computes every fiber in the nonprincipal square-zero class rather than just detecting that all targets are reached, and identifies an entire conditional commuting concentration regime. The exact comparison with Z/8 illustrates that the shape of this invariant, not just a normalization, can change at fixed ring size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
