# Independent mathematical audit

## correctness

PASS

The entropy gradient produces the three population deviations with the apex weight 1/a₃, cancelling both cross terms. The numerator of F(u)−v_* is a quadratic of leading coefficient −a₁ and roots u_−,u_+, so its factorization gives the claimed signed derivative. The entropy is proper on the positive octant and its strict threshold B is the minimum on u≤u_−; any initial closed sublevel below B is compact and positively invariant. On it the zero set forces u≡u_+, then v≡v_* and w≡w_* on an invariant trajectory, so LaSalle applies. Every larger complete sublevel reaches u<u_−. The strict open certificate is a proper subset of the basin: at (u_−,v_*,w_*) on its boundary, u'=0 and u''=u_−v_*(u_+−u_−)>0, giving immediate entry into u>u_− and then H<B. On a periodic orbit, integrating the signed derivative excludes staying on either side unless u and hence the state are constant. Integrating the three log derivatives yields the stated means, and strict F''<0 yields the strict Jensen conclusion since nonconstant state entails nonconstant prey. The periodic assertions are conditional. Read RESULT.md, VERIFICATION.md and VERIFY.py; the script was inspected, not run, and its single integration is not used as a global certificate.

## originality

PASS

The same rational three-level model, its two coexistence equilibria, local stability and numerical basin behavior are already studied; the classical entropy method is also prior. The inspected same-model and same-method comparisons do not provide the sharp complete sublevel certificate or the paired crossing and strict mean constraints for this chain.

## value

PASS

The explicit initial-state inequality addresses a natural gap left by local stability and numerical basin plots in a bistable model. It provides a rigorous nonlocal guarantee with a precisely delimited sharpness claim. The same identity, combined with concavity, gives testable restrictions on candidate positive cycles without pretending to classify the full basin or prove cycle existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
