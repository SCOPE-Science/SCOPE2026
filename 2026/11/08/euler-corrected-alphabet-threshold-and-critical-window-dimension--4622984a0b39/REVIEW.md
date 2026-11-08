# Self-review

## Correctness — PASS
The finite pressure is a strictly decreasing function of the dimension and has the exact value \(aH_N\) at the convergence exponent. Euler–Maclaurin plus the zeta Laurent expansion gives the polynomially corrected integer threshold. In the centered window, the first logarithmic-pressure derivative is asymptotic to \(-1/(2a)\), with second derivative bounded by \(O(a^{-2})\), yielding the uniform \(2t\) window law. The same bounds apply to the slowly diverging centered coordinate of the unshifted exponential cutoff and give its strictly positive logarithmic amplitude. All limits are analytic consequences of these equations; the finite numerical checker is not an infinite proof.

## Originality — PASS within checked sources
The closest published result, *Exponential-alphabet crossover for Zipf-normalized expanding maps* (2026), explicitly covers the same affine IFS, the same dimension pressure root and the first-order phase transition at \(\tau=1/\lambda\). It explicitly refrains from assigning a sign at equality. The present finding instead determines the integer cutoff to a multiplicative \(1+o(1)\) factor, including the polynomial prefactor and Euler constant, obtains the second-scale profile and resolves the previously unsettled sign at the unshifted cutoff. The primary expanding-map paper of Cunha, Novaes and Ponce (2026), including its affine example, supplies neither the Zipf cutoff nor its second-scale expansion. Standard dimension-spectrum and infinite-IFS theory provides the pressure framework, not the specific asymptotic. Targeted searches found no stronger result, though unlocated earlier equivalent calculations remain possible.

## Mathematical value — PASS
The exact first-order cutoff misses an asymptotically unbounded **multiplicative** factor in the minimum finite alphabet needed for the dimension to cross the natural branch convergence exponent. The polynomial correction therefore matters for finite-alphabet approximation cost and changes the answer at the critical first-order phase. The second-scale profile quantifies the entire narrow crossing window; the unshifted boundary sign and its logarithmic scale answer a specific limitation recorded in the closest earlier theorem. This is a motivated sharp boundary refinement, not a restatement of the pressure identity or an arbitrary finite parameter sample.

## Scope and risks
The analysis assumes exactly Zipf-normalized affine branches and fixed \(0<\lambda<1\). It does not cover nonlinear maps or arbitrary truncation renormalizations. No finite-parameter sign is claimed at exactly centered \(t=0\). Priority is provisional because no search can exclude all earlier equivalent asymptotic calculations. Independent verification has not occurred.

Self-review: passed. Independent audit: not yet performed.
