# Independent mathematical audit

## correctness

PASS

With the specified coproduct and D sigma = zeta sigma D, applying the relation to x forces D(x)=f(x^m); conversely the skew derivative with that generator value has the required relation on every monomial. Descent is precisely [N]_zeta x^(N-1) f=0, equivalent to forbidding a constant when r>0. The skew derivation annihilates every invariant polynomial; iterating on x^i gives the product of the j consecutive quantum integers with x^(i-j) f^j, or zero for i<j. A factor vanishes in any m-step iteration. Independently, put y=x^m and split into residues c mod m. For c>=j the j-step image in residue c-j is multiplication by y^(js) times a unit and a nonzero scalar; for c<j it is zero. The target residue has length ell+1 if c-j<r, else ell. The source has at least target length minus one, which is sufficient for js>=1, while s=0 is allowed only for r=0 so source and target lengths agree there. Summing max(0,target length-js) over c=j,...,m-1 recovers the stated rank including ell=js and ell<js. Rank one power determines s for a nonzero parameter; the Jordan second differences and the coefficient counts then give exactly the claimed partition frequencies. N<m leaves only zero, and at N=m a nonzero constant gives one block of length m. The frozen checker enumerates permitted parameters over prime fields, not arbitrary linear maps. The separate bounded probe `python3 -B /workspace/review_evidence/small_field_checks.py` verified quotient descent and all power ranks on 189 assignments with m=3 over F4, N=2 through 10; general exhaustiveness is by the generator proof.

## originality

PASS

The distinct supported contribution is the dependence of every power rank on truncation residue and valuation, the reconstruction from the first rank, and exact frequencies of those profiles for fixed scaling across all truncations. This does not claim the skew-derivation framework or the dimension-equals-order boundary. Inspected local comparisons are different operators, and the accessible primary statements do not imply this all-N stratification.

## value

PASS

The first-rank rigidity and residue-controlled higher-power cutoffs give a complete usable invariant of the skew generator in the fixed-scaling local algebra family. The exact frequency lets a reader count any nilpotent module profile over fields admitting the root without enumerating all parameter polynomials. This is an all-truncation structural result and not just a check of the single known cyclic boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
