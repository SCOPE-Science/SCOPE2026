# Independent mathematical audit

## correctness

PASS

Independently checked the moving-switch derivative. Write A_r(t)=∫_0^t exp(-rv)dv, U=T-h, z=C_0 exp(-bτ)+qA_b(τ) and w=exp(-ah)z+qA_a(h) for the start and end concentrations. Translation of both switches gives J'=(a-b){z[A_a(h)+exp(-ah)A_b(U-τ)]-wA_b(U-τ)}=(a-b)A_a(h)[z-qA_b(U-τ)]. The leading factor is exactly the strictly positive G in the result, even when b=0. For b>0 and E=q/b, C_0≥E makes J' strictly positive, and C_0<E makes it strictly increasing and positive at U. Its sign at zero is the sign of C_0-E(1-exp(-bU)), with equality giving the unique boundary minimum. The interior zero gives the stated logarithm. For b=0 the derivative is affine with slope 2Gq>0, giving the clipped formula. At an interior optimum with b>0 the derivative is 2Gk sinh[b(τ-τ_*)]; integrating it, and integrating the appropriate derivative on the boundary and for b=0, verifies all four regret cases. An independent segment calculation gave 2.578509392222384 and 2.196190111820411 for the canonical immediate and optimal exposures. VERIFICATION.md and check.py were inspected; the optional replay path is python3 check.py from the frozen package directory. The finite checks are not the proof.

## originality

PASS

The constant-source impulse counterpart is exactly, not merely qualitatively, related to the fixed window. The joint comparison narrows the incremental content to the nontrivial reduction of a finite translated rate interval to that impulse timing objective, its consequences for the entire admissible window (including exact regret and the zero baseline), and the positive rate factor. No inspected work was found to establish that finite-window reduction or an equally strong solution. This is not a priority claim for the positive-baseline impulse timing law alone.

## value

PASS

Under a genuine operating constraint (one contiguous fixed-runtime episode), the exact cancellation of the enhanced rate from all timing comparisons is a useful model benchmark. The result quantifies how much, not just which way, mistiming hurts; the finite interval has exactly the time-ordering and regret of the calibrated instantaneous proxy despite its continuing emissions and two switches. This does not assert optimality for split schedules, physical safety, or HVAC performance outside the well-mixed constant-source model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
