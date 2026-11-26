# Independent mathematical audit

## correctness

PASS

For the exact multiplication table, the right multiplication commutators yield the right Leibniz identity. On the quotient by the product span, invertibility and [U,U]=0 force a=U1 and b=V2 nonzero. The symmetrized product and [[V,U],U]=0 force U5=U7=0. At that point [U,V]=−ab e3, so the symmetrized relation forces the e8 component of [V,U] to vanish; this justifies the step used to solve for V7. Equality of [φ(e5),V] and [φ(e6),V] gives a=3V1+b. Independently checked sufficiency from the three possible nonzero right slots: right multiplication by Y is Y1 R1+Y2 R2+Y3 R3; substituting the displayed columns into those three operators gives the generator images and all other defining products, and the higher slots are zero. Only 2, 3 and nonzero torus coordinates need be inverted. The block diagonal yields the eight weights and determinant a^6 b^15. For b not in μ2∪μ3, the four forbidden a's are distinct, and the extra quadratic roots exist exactly for square b and cannot coincide with any of the four. The square count n/2−g−ε and resulting quadratic prove the formula, the 5/7 boundary and the density limit. The independent branch check (branches/15be6f16-7356-47d7-bafe-a32ae7d4318c/independent_check.py) found the plus-sign residual at p=7 and matched the torus count at all even orders 4 through 120. These finite checks supplement the proof. Uploaded scripts and recorded output were inspected, not run.

## originality

PASS

The algebra, automorphism parameters over C and diagonal weights have direct prior coverage. The original computational claim that passes is the exact fixed-point-free count over each finite field of characteristic >3, including the repaired normal form needed there and the finite-field existence boundary; it is not a new algebra or a new complex automorphism classification.

## value

PASS

The input is a previously singled-out class-five example, not an arbitrary table. The answer resolves existence at every allowed field size and exposes both order-3 and order-4 arithmetic in the exact defect from total automorphisms. The explicit correction also matters to anyone using the published automorphism matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
