# Independent mathematical audit

## correctness

PASS

Independently checked RESULT.md lines 5–66, the two frozen verification programs, and ran the independently written standard-library script /workspace/branches/reproduce_square_ice.py. It selects two outgoing neighbors per vertex and enforces complementary choices on each shared edge when its second endpoint is visited. Thus every accepted assignment is an ice orientation, and each such orientation appears once. The coordinate construction checks all directed incidences belong to exactly one square; the enumeration returned 1 empty set with coefficient 144, six singletons each 24, all 15 pairs each 8, eight triples each 16 (all opposite-pair transversals), and the full set with coefficient 64. Reversal on a directed square preserves vertex balances and alters no edge of another square. Each component is therefore a free orbit of the commuting flips, exactly Q_d, with per-set multiplicity obtained by division by 2^d. Replay returned 600 states, 576 edges, the histogram {0:144,1:72,2:30,3:16,6:1}, and the exact isotropic spectrum including 224 zero eigenvalues. For any positive couplings tensor flip eigenvectors give the stated signed sums on each cube and RK eigenvalues given by twice subset sums. Only one six-cube realizes the kinetic minimum; every smaller cube omits at least three faces, so it cannot supply the first excitation. The full cube supplies the kinetic and RK gaps 2 min_i t_i; the RK zero count is one per cube, including isolated vertices.

## originality

PASS

Best-of-knowledge pass for the joint labelled six-square activity and complete square-only sector census. The 600 and 192 marginal counts and the general square-plaquette Hamiltonian framework are antecedents, not part of this originality verdict. The indexed same-ensemble result gives a different Fourier invariant; the weighted cube and RK conclusions follow from the exact square-only census rather than an independent claim to tensor-product spectral machinery.

## value

PASS

Separating quadrilateral resonance from the allowed triangular dynamics is a meaningful restricted model for the same curved-ice configuration space. The joint activity invariant identifies the entire fragmented Hilbert-space decomposition, including the rare six-cube and exact frozen fraction, and gives the full weighted excitation and RK degeneracy data, not just another computation of the known state total or marginal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
