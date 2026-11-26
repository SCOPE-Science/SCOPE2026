# Independent mathematical audit

## correctness

PASS

Split a function on the union into line functions h_1,h_2 with h_2(0)=0 to count the shared origin once. The equations at the two lines become H_1(Aa)+H_2(Ca)=0 and H_1(Ca)+H_2(Ba)=0 for their additive transforms. The transforms are invertible for every nontrivial additive character: for nonzero b, multiplication by b sends all field elements bijectively to the field, so sum_a psi(ba)=0 even if psi has a trace kernel. The Gram determinant is det[u,v]^2 in all characteristics. Thus if C=0 both diagonal parameters are nonzero and both transforms are constant; if C is nonzero and either diagonal parameter vanishes the same constancy follows successively using the C terms. In each case the zero-sum constraint on H_2 and then the equations force both to vanish. Otherwise eliminate H_1 to obtain H_2(rho z)=H_2(z) with rho=C^2/(AB). The nonzero orbits all have size ord(rho); the zero orbit adds one degree of freedom, and sum_z H_2(z)=0 fixes precisely that scalar. The stated complex nullity and rank follow, including in characteristic two, and generator rescaling preserves rho and the zero cases. The supplied checker was read, not executed: it checks modular ranks in auxiliary characteristics and is not a complex-rank certificate or a premise of the proof.

## originality

FAIL

Demonstrable full statement coverage by a distinct indexed result: 754730fed24a states the same principal Fourier matrix, same scope, same zero-parameter invertibility case, and the identical complex nullity and rank formulas, and goes further with a basis and a distribution. The frozen orbit proof is presented differently, but the frozen Finding is not a different mathematical claim. The comparator's 2026-11-08 catalogue path is later than the frozen record's 2026-11-01 path; this decision records duplicate statement coverage, not that the comparator was chronologically first, that the frozen authors relied on it, or that a pre-2026 antecedent was proved. There is no uncovered theorem within the accepted scope to save by narrowing.

## value

PASS

As mathematics, the classification answers a natural self-sampling identifiability question over all finite fields: it gives both the geometric nonsingular cases and the exact number of independent reconstruction obstructions in each singular case. The orbit proof gives a useful explanation rather than a finite table. This structural value is distinct from originality and does not rescue the duplicate theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
