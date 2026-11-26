# Independent mathematical audit

## correctness

PASS

Re-audited repairs/1/RESULT.md. At zero cyclic separation the Green recurrence yields c(r⁻¹−r)(1−r^n)=1 and off zero the characteristic relation gives zero. Independent, class-restricted Rademacher probes sum unbiasedly; pair coefficients give 4 Σ_same G_ij², or 2 Σ_d f_d(n+C_d). The telescoping relation f_d−f_m=2 Σ_(k>d)(k−d)a_k gives the exact window certificate, with each coefficient positive and each window difference nonnegative by parity. A one-defect reference fills the odd/even window lower bounds and has C_d=(−1)^d(n−2d). Any nonoptimal word has at least three defects, forcing T₂ to increase by at least eight. On flipping reference sites 2 and 3, only the windows ending at 2 or starting at 3 may change, with pair of sums (1,−1)→(−1,1) at odd k≥3 and (2,0)→(0,2) at even k≥4. Therefore the higher T_k are unchanged; the word is admissible and attains 16a₂, including m=2 where only the endpoint coefficient is defined. For the baseline comparison, same solve count means averaging two independent full-support probes; domination by a geometric series justifies the fixed-μ limit. An independent exact rational replay in branches/268a8060-5c50-42cb-afd7-111b79b45d79/gap_check.py and gap_check_output.txt confirmed 20 parameter cases (21,824 words modulo color exchange, including the inadmissible constant words in the scan); it uses weights f_d/c², direct pair enumeration and the admissible witness, not the window formula as an oracle. These finite tests are corroboration only; the analytic proof establishes all allowed n and μ. Uploaded code was not executed.

## originality

PASS

The repair makes the exact first gap and its attaining perturbation the distinct claim. It credits the exact minimum variance and one-frustrated-bond classification to verified same-day coverage, without inferring order, and does not treat the ordinary variance identity, same-solve baseline, or antiferromagnetic ground-state ordering as the gap result.

## value

PASS

For the natural fixed two-solve scheme, the exact positive first gap measures the smallest cost of leaving the one-defect family and certifies when a near-optimal coloring must be optimal. Its change from endpoint difference at n=5 to local curvature at n≥7, with an explicit witness preserving all larger window costs, adds information not contained in either the exact minimum or the asymptotic parity penalty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
