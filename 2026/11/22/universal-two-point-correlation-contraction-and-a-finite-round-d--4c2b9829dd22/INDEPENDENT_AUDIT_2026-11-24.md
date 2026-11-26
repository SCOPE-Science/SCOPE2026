# Independent mathematical audit

## correctness

PASS

The sign gauge transforms each bond to rho>0 and the signed pair products to ordinary ferromagnetic correlations. The nearest observed endpoints give conditional means linear in their values, with nonnegative position-dependent coefficients, including absent endpoints. In a common gap the conditional two-spin table is proportional to (1+u a x)(1+d xy)(1+v b y), d=rho^(j-i), normalized by 4(1+duvab). Four times the determinant of this probability table is the spin covariance d(1-u^2)(1-v^2)/(1+duvab)^2. If the sites are separated by an observation it is zero by the Markov property. For adjacent unrevealed sites u,v<=rho, proving the claimed uniform positive bound. Induct on the disclosed positions: new-old moments propagate through the nonnegative linear mean coefficients; new-new moments of the decoder propagate through their products, while the target has the extra nonnegative conditional covariance averaged under the target, not under the decoder. Both diagonals equal one, so the comparison holds even when their revealed contexts have different laws. Pair moments are final upon reveal, with zero single-spin means by flip symmetry. Exogenous scheduling mixes those inequalities; iid labels give collision probability sum a_k^2>=1/K. The defect divides the bond shortfall by two, and the exact bond-log representation multiplies it by log((1+rho)/(1-rho)), not by a KL identity. No floor is implied for coordinated schedules. The frozen check.py uses finite fraction recursion; its stored counts are not proof. The independent full-law restriction checker /workspace/branches/178f0add-b045-4969-abc5-bbcd14821517/check_record4_independent.py confirmed 1177 pair inequalities, 214 adjacent bounds, and 8 exact all-singleton cases on its bounded grid and confirmed a nonuniform iid example.

## originality

PASS

Credit the deterministic all-pair signed comparison and the explicit co-reveal deficit and iid finite-round lower bound, not the already available exact output-defect and cross-entropy observable, the one-site decoder, or the chain energy identity. The strongest inspected same-model source has exact recursions for independent schedules, not the asserted deterministic all-pair inequality or explicit lower bound in the passages checked.

## value

PASS

The all-pair comparison turns a local conditional-independence approximation into a deterministic schedule-wide constraint even when the decoder has changed the revealed-context distribution. The explicit local covariance loss and iid collision bound give a length-independent finite-round limitation for every bond, without solving a decoder recurrence. Separating the guarantee from coordinated schedules matters for understanding when parallel exact-marginal decoding incurs thermodynamic error.

The dated certificate retains the supplied scientific assessment, sources and limitations.
