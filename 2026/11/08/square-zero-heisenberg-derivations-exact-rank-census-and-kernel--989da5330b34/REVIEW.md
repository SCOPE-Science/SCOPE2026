# Scientific review

## Correctness

**PASS.** The derivation identity is derived directly from the Heisenberg bracket; square-zero forces the central scalar to vanish and imposes \(T^2=0\) and \(fT=0\). The image of a square-zero symplectic endomorphism is isotropic, and the induced map from the symplectic quotient is a nondegenerate symmetric form. These statements work without division by two. The two cases for \(f\) give the rank and kernel-bracket formula, and the counting factors come from isotropic ordered bases and nonsingular symmetric forms. The geometric assertions are about smooth open/vector subbundles over the isotropic Grassmannian. The checker tests original bracket equations directly over several fields, including characteristic two and a genuine degree-two extension field. Finite checks do not establish the general theorem; the written proof does.

## Originality

**PASS, with historical-priority limitations.** Feldvoss, Siciliano and Weigel (arXiv:1102.2629) give existence of outer square-zero **restricted** derivations, not the classification or rank multiplicities of all ordinary Heisenberg derivations. Brouwer, Gow and Sheekey (2014) study finite-field nilpotent matrices, including their symplectic Lie-algebra total, rather than the stated two-layer derivation ranks, kernel conservation, and geometric strata. Lusztig's 1976 fixed-rank nilpotent-matrix work is pertinent background and may cover related linear-algebra counts, but no decisive implication of this full package has been established. Specialized orbit-count tables or later classifications may overlap and warrant further historical verification. No claim of exhaustive priority or independent novelty certification is made.

## Value

**PASS.** Square-zero derivations are natural structural operators on nilpotent Lie algebras, and their ranks alone do not immediately expose the symplectic restrictions. The theorem determines every finite-field rank multiplicity and identifies a field-independent relation between differential rank and the inherited bracket on its kernel. Each positive-rank locus has two different geometric mechanisms and consecutive stratum dimensions. These are motivated structural invariants, not a prescribed numerical slice or an unsupported small-field phenomenon.

## Computational reproducibility and limits

Run `python3 checker.py` and compare its output with `verification_output.txt`. The checks exhaust the original linear derivation and square-zero equations for \(n=1\) over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\) and \(n=2\) over \(\mathbb F_2\). Larger parameters are formula evaluations, not exhaustive searches. The result does not classify restricted derivations, conjugacy classes, all nilpotent derivations, or global nonreduced schemes.

Self-review: passed. Independent audit: not yet performed.
