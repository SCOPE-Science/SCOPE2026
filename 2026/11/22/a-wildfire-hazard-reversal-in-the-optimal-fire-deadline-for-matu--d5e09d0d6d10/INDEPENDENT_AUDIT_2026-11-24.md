# Independent mathematical audit

## correctness

PASS

For the same stock released at either fire, integrate the marginal stock B'(t) against survival up to T and divide by the survival integral for elapsed time. This gives the reviewed ratio, with zero reward for T<=m and positive limiting rate at infinity. The sign of its derivative is the sign of Q, with Q(m)>0, Q increasing up to bm/delta and strictly decreasing thereafter to minus infinity. This proves global uniqueness including comparison with no planned fire; dividing the root equation by mu exp(mu T) proves the bracket. At the root the common logarithmic derivative ell gives g_T=-delta*ell. The derivative of L(k,z) in k is negative and strictly increasing in kz, since the derivative sign of that auxiliary function is controlled by (u-2)exp(u)+u+2 whose second derivative is u exp(u)>0. The bracket orders b(T-m)>mu T, giving the hazard, decay and maturity signs with the implicit derivative. As a cross-check on the hazard sign, J is the exp(-mu t)-weighted average of B'(t). At the maximizer the weighted mean of B'(t)-B'(T) is zero, with negative sign before m and positive sign between m and T, so increasing mu decreases that average at fixed T and moves the crossing later. The positive-parameter bracket gives the high-hazard and zero-decay limits. The critical log-derivative equality gives exp(-b(T-m))/exp(-mu T)=(mu+ell)/(b+ell)>mu/b, proving the upper bound on the relative gain. At zero hazard Q/mu converges locally uniformly to 1+delta T-exp(delta(T-m)) and brackets its unique root on either side. At zero maturity the rate decreases; at zero decay and positive maturity it increases after m; with both zero the rate is constant. No survival, population optimization or real-world fire prescription follows. The frozen check.py and VERIFICATION.md were read, not executed; numerical checks are corroboration, not proof.

## originality

PASS

Credit existing renewal-reward and quotient-oscillation machinery, and overlapping random rotation models. The supported distinct bundle is the strict hazard reversal for a delayed, exponentially saturating reward with equal payout at either type of event, together with the explicit bracket, other strict comparative statics and singular limit. No universal planning-heuristic reversal or priority over all replacement-policy models is asserted.

## value

PASS

The hazard sign answers a natural comparison for a delayed replenishing but saturating reward at a random event or a chosen deadline. The rate can fall and a scheduled fire become less useful while the optimal elective age rises; the bracket and vanishing relative gain make that distinction quantitative. The zero-loss boundary explains why finite scheduling is specific to positive viability loss and delay. This is an interpretable result about the stated proxy, not a management recommendation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
