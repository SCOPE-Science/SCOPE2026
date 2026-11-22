# Scientific review: affine monomial Aluthge orbits

## Correctness — PASS

The theorem is proved by a unitary logarithmic change of coordinates, followed by an explicit polar decomposition and a direct-integral spectral analysis. The generalized Aluthge map multiplies the damping by \(q=1-\eta+\eta/a\) at every step. Unitary conjugation by a positive spatial dilation shows exact unitary equivalence across the entire orbit. Dominated convergence applied to both multiplication factors and their adjoints establishes strong-star limits; essential-supremum calculations give a constant positive consecutive norm gap. The logarithmic direct integral produces bilateral weights with limits zero and one at opposite tails, proving point-versus-residual spectral orientation, infinite multiplicity, and the Fredholm disk. The exact self-commutator is multiplication by a difference of two exponentials, whose maximum is elementary. The standard-library checker returned `CHECKS_OK 17378`; these finite checks supplement rather than replace the infinite-dimensional argument.

## Originality — PASS, with priority uncertainty

Benhida–Budzyński–Trepkowski, arXiv:1809.01205, prove the **general one-step** Aluthge formula for weighted composition operators; that result is prior art, not part of the claimed contribution. Agler–McCarthy, arXiv:2205.01857, give the structural monomial class; Chalendar–Partington, arXiv:2212.02172, address affine-index boundedness and compactness. Their inspected texts do not give the stated joint fixed-unitary-orbit classification, two strong-star limits, exact norm gap, and point/residual orientation. A published weighted-Hardy monomial example has nonconvergent Aluthge iterations, unlike the present positive-damping continuous-space family. Other published compact shift iteration results have operator-norm or Schatten convergence, incompatible with the persistent norm gaps here. A 2009 weighted-translation Aluthge result proves convergence under broad assumptions, so **the convergence assertion alone** is not claimed as original; the complete coupled phase diagram is the novelty assessment. Its full text was not available for inspection, and further equivalent formulations could exist.

## Mathematical value — PASS

The problem is naturally motivated by affine-index monomial operators and the convergence of iterated generalized Aluthge transforms. This single explicit family shows that all iterates may remain unitarily equivalent with identical nonnormal spectral disks while converging strongly-star to a normal operator of radically different spectral type. It distinguishes forward and backward dilation by an exact point/residual spectrum reversal, and quantifies the failure of norm convergence by a fixed positive gap, not merely a nonconvergence assertion. These are structural, infinite-dimensional phenomena applicable to an entire two-parameter family, not a reparametrized finite computation.

## Literature limits and evidence

Relevant inspected full texts: Benhida–Budzyński–Trepkowski (2018, arXiv:1809.01205), Agler–McCarthy (2022, arXiv:2205.01857), and Chalendar–Partington (2022, arXiv:2212.02172). Limited evidence: abstract of Burnap–Jung–Lee–Park (2009) and abstract of Lahiri–Ojha–Birbonshi (2026, arXiv:2604.27762). The former's full text could not be obtained; it remains the most substantial priority risk because weighted dilation becomes weighted translation after a logarithmic change of variables. No equivalent joint classification was found in the accessible comparisons, but a negative search does not establish uniqueness. No independent validation is represented.

Self-review: passed. Independent audit: not yet performed.
