# Self-review of the semidihedral endomorphism theorem

## Correctness — PASS

The presentation gives a unique \(r^is^\epsilon\) normal form. The orders of \(r^is\) split by parity, the involution list is complete, and all homomorphisms arise from three mutually exclusive cases for the generator image. The generating relations give four central-choice homomorphisms, \(m^2/2\) cyclic-image/outside-involution maps, and \(2m\) coset-image maps; the individual rank and kernel cases yield the stated polynomial, with correct boundary \(n=4\). Idempotence and automorphism conjugacy are derived explicitly, not inferred from small data. The geometric-tail estimate completes the total-variation assertion. Direct exhaustive enumerations through group order \(128\) in `check.py` and `CHECK_OUTPUT.txt` confirm the exact rank cells and conjugacy orbits. The infinite theorem still relies on its symbolic proof, not the experiments.

## Originality — PASS within the inspected material

The source-based comparison is to the *statements*, not merely titles. Beike et al. (2023) give a cyclic-index-two group classification and Hughes/tidy criteria, but not the semidihedral endomorphism-image polynomial. Flake–Thevis (2020) give maximal-class commutator/origami data, not an endomorphism census. Puusemp (1996), inspected in full, requires coprime cyclic-factor orders in the main comparison theorem, excluding this \(2\)-power semidirect product. The 2002 Puusemp paper concerns prime-power semidirect cyclic groups and could conceal an implicit more general parametrization; its full text could not be inspected, so the historical-priority risk is substantial but was not converted into a fictitious negative full-text check. The 2005 small-order classification and 2006 open article do not state an all-order index-limit law. Related dihedral and quaternion results, and results on modular group algebras, do not supply the asserted full semidihedral rank spectrum.

## Mathematical value — PASS

This is the complete natural image-type and retraction classification of the semidihedral group family, rather than an arbitrary numerical sample. It distinguishes the maximal-class dihedral/semidihedral/quaternion trichotomy by a sharp proper-retraction count, shows that nonabelian proper *images* of every admissible dihedral order occur but never as retracts, identifies the precise absence of order-four retracts despite abundant order-four images, and proves a parameter-uniform probabilistic limit for image index. Each property is motivated by the structure of homomorphism images and the known cyclic-index-two families, not by a parameter chosen after computation.

## Closest literature and residual limits

The primary context is Beike et al., *\(p\)-groups with cyclic or generalised quaternion Hughes subgroups: classifying tidy \(p\)-groups* (first public 2023-04-20, primary MSC 20D15), Sections 1–2, including Theorem 2.1. Supporting context is Flake–Thevis, arXiv:2003.13297. Potential dominance by Puusemp's 2002 general prime-power cyclic-semiproduct endomorphism classification remains unresolved due to inaccessible full text. The 2005 paper is abstract-only; the 1996 PDF and the 2006 open-access article were materially examined. No independent mathematical audit is claimed, and the proof does not extend to arbitrary metacyclic or maximal-class groups.

Self-review: passed. Independent audit: not yet performed.
