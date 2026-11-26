# Independent mathematical audit

## correctness

PASS

For the symmetric telegraph chain with directional rate s, let φ_i be the starting-state-conditioned homogeneous propagator, and order states as on, off. Its backward generator A has rows (−k−s,s) and (s,−s). The stationary partial second moments q follow from the state-specific diffusion input D and stiffness loss 2kq_1, giving q=(D/k,D/k+D/s). The covariance is qφ, the unconditioned impulse response is (φ_1+φ_0)/2, and −qA/D=(0,1), so −C′/D=φ_0 exactly. The stationary convolution has finite variance by the strictly negative eigenvalues of the killing generator at stiffness 2k; coupling with common future noise gives uniqueness since occupation of the on state grows unboundedly almost surely. The gap solves the scalar characteristic equation with decay-rate sum k+2s and product ks, and initial data (0,k/2). The two distinct positive decay rates give the stated positive sign, area 1/(2s) and precisely one derivative zero at exp(−Ωt)=λ_−/λ_+. Substitution gives the height and the stated slow/fast switching limits follow from the roots. The k=3,s=2,D=5 check reduces exactly to G=(3/10)(e^(−t)−e^(−6t)). The supplied verification/check_fdt.py was inspected as diagnostic evidence, not run; the exact argument is the replay, not the script or an attestation.

## originality

FAIL

Verified existing coverage by a distinct indexed theorem, not a finding of historical priority. Its two-rate, two-stiffness defect specializes to the entire frozen positive gap and sum rule at the same force-response convention. The remaining off-conditioned interpretation follows directly from that theorem and the two-state propagator; peak, slope and reconstruction are direct deductions of the same defect.

## value

FAIL

The stiffness-independent integral in this natural response experiment is scientifically meaningful, but the frozen contribution does not add a distinct invariant to the stronger existing defect theorem. The off-conditioned identity and the inversion of area and slope are routine consequences that do not constitute a surviving repaired contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
