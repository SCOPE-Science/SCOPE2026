# FAILED ATTEMPT — NOT A VALIDATED FINDING

The central short-interval zero-density theorem in this record is not validated by
the supplied evidence.

First, the record uses the first-version Qi–Qiao threshold
`T^(4/7) < M <= T` and calls `T^(4/7)` the sharp/smallest method boundary.
Qi–Qiao revised arXiv:2608.29558 on 2026-09-09, before this record was
published, and version 2 improves the effective short-interval range to
`sqrt(T) < M <= T`. The record therefore builds its headline sharpness claim
on a superseded version of its main input.

Second, the step from a twisted spectral large-sieve inequality to the displayed
zero-density theorem is only sketched. The record does not supply the complete
zero-detection and mollifier argument, the parameter inequalities needed to
control every dyadic block, or the error analysis needed for the asserted
uniformity up to `H <= T^2`. The referenced
`output/artifacts/threshold_check.py` file is not present in the audited
repository tree; in any event, checking continuity of the three sieve branches
would verify only threshold algebra, not the zero-density theorem.

Third, spectral-aspect zero-density for these Hecke–Maass L-functions is not
new in the broad sense asserted by the framing. Liu and Streipel, *International
Journal of Number Theory* 20 (2024), 849–866, already prove a weighted
spectral zero-density estimate (their Theorem 1.3) from a mollified twisted
second moment; the underlying moment theorem allows Gaussian spectral windows
with `T^epsilon <= M <= T^(1-epsilon)`. Their smoothing and `H` range differ
from the present record, so this is not a verbatim duplicate of every desired
parameter, but it is decisive prior work that a corrected result must compare
against precisely.

A future attempt could still seek a hard-cutoff or larger-`H` refinement using
the current Qi–Qiao theorem. That would require a complete derivation and a
careful comparison with the existing spectral zero-density literature. The
present package does not provide that derivation, so it must not be imported as
a validated finding.
