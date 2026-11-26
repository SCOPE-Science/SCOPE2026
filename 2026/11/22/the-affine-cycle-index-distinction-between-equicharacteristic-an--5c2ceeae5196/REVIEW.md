# Independent mathematical audit

## correctness

PASS

For each (u,a) and k>=1, the displacement f^k(x)-x is (1+u+...+u^(k-1))((u-1)x+a). If u mod m is not 1, conjugate by the unique fixed point. The nonzero radical points then have period d=ord(ubar), and units have period ord(u). In the lift of each ubar exactly one unit has order d: on the kernel 1+m, the dth-power map is invertible, while the other lifts have order dp. This gives both divisor sums with q^2 translations per lift. For u=1+w, the geometric sum is k+binom(k,2)w. It is a unit for p not dividing k and equals k when p divides k, since p is odd and p m=0. With a in m, the fixed set is either all points (identity), none (nonzero radical translation), or one q-point residue fiber (w nonzero); all other points have exact period p. With a outside m the displacement factor (u-1)x+a is a unit for every x, so the exact period of every point is p in characteristic p and p^2 in characteristic p^2. The latter contributes q^2(q-1) maps with a pure p^2 cycle partition. Adding the identity, the q-1 nonzero radical translations, the q(q-1) maps with one fixed fiber, and all q^3(q-2) maps with ubar not 1 gives the stated index and fixed-count marginal with total q^3(q-1). The weighted degree is q^2, and d prime to p makes the listed nonzero cycle signatures distinct. At fixed residue field size there is one ring of each characteristic: in char p the roots of x^q-x lift uniquely and form a coefficient field, and a generator of m gives dual numbers. In char p^2, lift a residue-field generator as a root of a fixed monic lift of its irreducible polynomial, using the invertible derivative and m^2=0. The resulting map from the monic quotient of (Z/p^2)[t] surjects on the residue field and on pR=m, hence is an isomorphism by the order q^2. Thus the coefficient of the p^2-only monomial reconstructs the ring, not just its characteristic. Independently ran /workspace/audit_evidence/affine9.py using T^2+T+2 as the residue polynomial; all 5832 maps in each of the two q=9 models matched the predicted monomials and marginal. The symbolic argument, not this replay, establishes all odd p and all f.

## originality

PASS

The distinct claim supported here is the full natural-action cycle index and its contrast with the common fixed-point distribution for both characteristic families over all odd residue degrees, not the prime-cyclic mixed-characteristic case or the detection of characteristic by abstract element orders. The strongest same-day indexed comparator proves the latter for a wider family, but its stated order distribution is strictly less information than a full point-cycle partition, and does not give the fixed-point marginal. The proof needs the actual action on both residue and radical fibers, not just the order of a map. Priority beyond the inspected material remains bounded.

## value

PASS

The natural point action is canonical and its index gives concrete orbit-counting information, for example via substitutions giving colorings of the ring modulo its affine action. The same one-step fixed-point statistics conceal which points form long cycles and how those cycles are distributed. Quantifying that loss uniformly for the two length-two families, including nonprime residue fields, is useful beyond the already covered yes/no diagnostic from abstract element orders. The contribution is the complete action-level comparison, not a general claim about all chain-ring lengths or even characteristic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
