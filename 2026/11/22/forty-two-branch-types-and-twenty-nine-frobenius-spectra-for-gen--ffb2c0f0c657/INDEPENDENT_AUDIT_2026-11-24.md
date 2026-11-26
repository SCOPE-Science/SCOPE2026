# Independent mathematical audit

## correctness

PASS

The original theorem is correct; the repair changes the principal claim, not the existing table. Even subsets of ten branch points modulo complementation are an eight-dimensional symplectic F_2-space with intersection pairing, and maximal isotropic subspaces model the finite étale kernel scheme in odd characteristic. To independently verify the enumeration and table, /workspace/audit_lagrangians.py was written and executed against the frozen kernel_spectra.csv. It enumerates via a symplectic decomposition X+Y: for a projection U into X, the intersection with Y is Ann(U) and the lifting datum modulo Ann(U) is a symmetric form on U. This generates all 2295 Lagrangians without using the stored enumerators' RREF or extension of isotropic subspaces. A 10-cycle and one adjacent transposition give orbit sizes 945 and 1350. Fixed points of divisor powers and inversion reproduce every aggregate and component row, including all fixed torsion counts and the original 151-versus-39 example; 29 aggregate spectra and 38 ordered component spectra occur. The 945-element orbit consists of matchings: five disjoint pairs span a Lagrangian with exactly those five weight-two classes, uniquely recovering the matching. A preserved matching is a commuting fixed-point-free involution: it pairs equal-length branch cycles with d shifts per pair, and each unpaired cycle must have even length with its unique antipodal pairing. The resulting product formula checked every relevant power. For (4,2,2,2) and (4,2,2,1,1), the distinct split rows both sum to 1:7 2:64 4:540 and both have eight rational torsion points. The realizations use the irreducible quartic x^4+2 over F_5 (no root or quadratic factor), plus the stated distinct irreducible quadratics and, in the second equation, two linears. Squarefree degree ten gives smooth projective genus four. The repaired verification script independently checks the matching counts, ordered-count total, witness and factor tests against the frozen CSV and was run successfully using that path. Original source scripts were inspected but not run. All claims remain conditional on odd characteristic and the realized branch partition, and no Jacobian-target claim is made.

## originality

PASS

The frozen novelty framing fails for the aggregate table and equal-torsion 151-versus-39 distinction: the same-date fixed-count table directly includes the distinction and mechanically determines all aggregate spectra, irrespective of which record came first. This is not a mathematical error in the frozen table. The replacement RESULT withdraws that originality claim and states a substantive narrower result: the full ordered component table, 38 ordered spectra and an explicit realized collision for equal aggregate spectra and equal torsion counts that is resolved by the components. Pass for that repaired claim only; the geometric split and standard fixed-matching formula are credited as input, and the independent status is not a priority certification.

## value

PASS

The repaired exact invariant distinguishes two intrinsic families of polarized kernels. The concrete realizable collision shows why an investigator of descent may need the two component zeta functions, even with the total zeta function over all extensions and rational torsion in hand. It shows a strict loss of information upon summing, not merely a repackaging of the public fixed-count table or an arbitrary numerical slice. The component count over every natural branch partition maps the size of the refinement (38 instead of 29), while the explicit pair shows its need for actual curves. This is independent value without a claim of classifying quotient Jacobians.

The dated certificate retains the supplied scientific assessment, sources and limitations.
