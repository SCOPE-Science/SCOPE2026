# Independent mathematical audit

## correctness

PASS

Positive axes are invariant by the coordinate factors. In the equation for M=u+v the dispersal terms sum to −δ(u−v)²; the resulting logistic upper bound gives global bounded trajectories with bounded derivatives. Logistic comparison for v gives liminf v≥v_0. At limsup times for v the derivative tends to zero, implying V≤v_0+aU for the two limsups. If U>0, its own fluctuation sequence then gives 0≤U[1/(m+U)−H]<0, so u→0 and the v equation gives v→v_0. For w=v−v_0−au the exact filter is w'=−(s+δ)vw−au'. Since u'/u→0, the initial memory decays after division by any fixed u^p, and u(t−τ)^p/u(t)^p→1 on each fixed lag. On a sufficiently late tail this ratio is at most exp(pητ), while the filter is bounded by exp(−(s−η)τ). For η<s/(p+1), dominated convergence gives w/u^p→−aL/s whenever u'/u^p→L. In the strict branch, p=1 gives w=o(u); hence u'/u²→−(H−1/m), and p=2 gives the lag limit. At equality, the exact per-capita drift is −H²u²/(1+Hu); p=1 and then p=2 give w=o(u²), so u'/u³→−H² and p=3 gives the cubic lag. Integrating the derivatives of u^-1 and u^-2 gives precisely the two reported amplitudes. Conclusions concern patch one and positive data only, not extinction of both patches. Frozen VERIFICATION.md and verify.py were inspected, not executed. The recorded symbolic and BDF checks are not needed to prove the global or infinite-time results.

## originality

FAIL

The four rate and lag limits are coefficient consequences of the prior same-model local reduction, and the claimed extension to all positive data follows from that paper's existing global proof ingredients at these parameters. The latter is not a stated theorem in Xia et al., but it is a direct implication, not merely a resemblance to their theorems on adjacent branches. The decisive comparison is to the earlier paper, not to a later catalogue match.

## value

FAIL

An extinction rate and lag valid throughout a basin can be useful. Here the basin on the stated parameter surface follows by applying the prior same-model no-cycle and local-attraction arguments, with a scalar logistic boundary check. The four constants are forced by the existing local reduction. The alternate direct proof is clear, but the frozen claim gives no additional rate regime, uniform transition or independent phenomenon beyond those implications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
