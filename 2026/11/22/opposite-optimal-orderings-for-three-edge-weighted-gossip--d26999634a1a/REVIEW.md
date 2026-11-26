# Independent mathematical audit

## correctness

PASS

The symmetric contact matrices preserve the consensus direction and act as strict contractions along their own edge vectors for all p_i in (0,1). Equality through the entire sweep would require a vector orthogonal to all three edge vectors, hence zero in the centered space. The symbolic Frobenius difference directly checks as 4abc(1-a)(c-b), and reversal transposes the sweep, giving the strict middle-parameter order and all ties. On the centered space S=T^T T has det(S)=U=product(1-2p_i)^2. The telescoped loss I-S is a sum of three outer products with factors 2p_i(1-p_i); their vectors are obtained from the original star vectors by a unit-triangular basis change. The original Gram determinant is four, so det(I-S)=V=32 product p_i(1-p_i), positive and at most 1/2. Thus every largest root lies in (0,1), even with a singular contact. Independently, the centered characteristic polynomial of S is chi_E(s)=s^3-E s^2+(E+V-1+U)s-U. If E2>E1, then at the largest root r2 of chi_E2, chi_E1(r2)=-(E2-E1)r2(1-r2)<0, forcing r2 strictly below the largest root of the monic chi_E1. Equal E yields identical polynomials, covering ties. Separately, the product T has one common characteristic polynomial by cyclic permutation and transpose, including noninvertible factors. Two contacts give only reversals, so no smaller star has an ordering conflict under these hypotheses. Direct symbolic check and rational witness with numerical singular roots: python /workspace/replays/gossip.py. Only one sweep with three fixed contacts is claimed; the heat-edge special case restricts p_i to (0,1/2), not the theorem.

## originality

PASS

The supported distinct result is the exact largest-/smallest-parameter middle rule for heterogeneous fixed contacts on the three-leaf star. The separate same-day weighted path statement already shows the broader norm-ordering conflict with equal spectra but gives a different topology and optimizer law. Classical contraction and order-invariant spectral convergence are not claimed as new.

## value

PASS

A star with three contacts is the first star where reversal symmetry permits an ordering choice. The exact exhaustive schedule rule for arbitrary fixed strengths and all ties exposes the incompatibility of isotropic and worst-direction design even at equal asymptotic spectra. It is an analytically useful small benchmark, not a rule for long sweeps or arbitrary topologies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
