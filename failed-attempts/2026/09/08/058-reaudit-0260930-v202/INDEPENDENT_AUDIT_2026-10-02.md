# Independent mathematical audit

## correctness

PASS

The frozen repository omitted claimed generated atlas files and used a private absolute ART path; those were real reproducibility defects, not evidence that the mathematics was false. I independently ran the frozen two character-table algorithms in an isolated writable directory (altering only ART for the replay): Method B generated n=1..12 Kostka-inversion character tables; Method A recomputed them via Murnaghan–Nakayama and agreed entrywise. Orthogonality, dimensions and transpose checks passed. The full 74,088 ordered n=10 triples were enumerated with 40,860 nonzero, unique maximum 117 at ((4,3,2,1)^3), and ray values 4 for n=6..12. Mathematical C therefore passes; this does not certify the original package as self-contained for publication.

## originality

FAIL

Castilho Alcarás and Kota's 2010 full primary paper explicitly states that their implemented methods generated full downloadable inner-product tables for every n<20. Inner products of Schur functions are the same Kronecker coefficients, so this prior database covers the n<=10 atlas and ray values through n=12. Its Table 2 already gives the (4,3,2,1) square highest multiplicity 117 with constituent (4,3,2,1). Blasiak independently reports M(10)=117. The unique-maximizer detail is directly extractable from the prior complete n=10 table and is not a surviving new mathematical finding.

## value

FAIL

A certified duplicate table may be useful software infrastructure, but the SCOPE scientific value criterion rejects known/table recomputation absent a genuinely new substantive fact. The exact finite atlas and ray are already in prior n<20 tables; the certification pipeline alone does not turn them into a new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
