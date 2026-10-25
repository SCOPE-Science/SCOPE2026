# Independent mathematical audit

## correctness

PASS

For the printed Kong–Shao delayed fear/Crowley–Martin predator-stage system, positivity and global boundedness follow from the quasipositive vector field, logistic upper control of P1 and bounded maturation forcing. With q=d2+c2, K=(r-d1)/c1, a=c2/q and R=eta*b2*c2*K/[q*d3*(1+b1*K)]<1, choose eps>0 with a*eta*b2*h(K+eps)<d3, h(x)=x/(1+b1*x). The actual Lyapunov–Krasovskii functional L=a*P2+P3+c2*int_{t-tau2}^t P2(s)ds has exact derivative Ldot=a*eta*b2*P1*P3/[(1+b1*P1)(1+k*b3*P3)]-d3*P3-c3*P3^2; the current and delayed juvenile terms cancel. For sufficiently large t, Ldot<=-delta*P3-c3*P3^2. Since L>=0 and decreasing eventually, P3 is integrable; bounded P2 and delayed P2 make dot P3 bounded, hence P3->0 by uniform continuity/Barbalat. Variation of constants then gives P2->0; P3(t-tau1)->0 and logistic upper/lower comparison give P1->K. This holds for all fixed nonnegative delays and positive histories, not at R=1. A compact invariant set entirely within the strict positive cone cannot carry an orbit converging to the boundary. Independently reproduced exact symbolic denominator factorization, cancellation, local-condition equivalence, the equality of candidate and earlier R, and the example 93/928 versus 1/12. The earlier published proof also establishes the same general theorem, so scientific correctness is unaffected by failure of originality.

## originality

FAIL

Direct statement-level coverage is decisive. The published Resultary record dated 2026-10-04, “A corrected delay-independent predator-extinction threshold in a fear-stage model”, studies the IDENTICAL P1/P2/P3 delayed Kong–Shao equations and proves from every positive continuous history that P2,P3->0 and P1->K for arbitrary tau1,tau2 whenever R_P=eta*b2*c2*K/[(1+b1*K)(d2+c2)d3]<1. Substitution K=(r-d1)/c1 gives exactly the audited R_mat. Its full RESULT.md supplies an explicit positive-weight Lyapunov–Krasovskii functional, logistic comparison and Barbalat proof. The audited L is, up to a positive scalar, its functional at the limiting boundary alpha=q/c2 (outside the earlier strictly interior alpha choice), a different presentation not a distinct theorem. Kong–Shao Theorem 3.1(ii) already prints the undelayed local threshold, and the audited 93/928 example is a direct arithmetic specialization of the earlier global theorem. Nonexistence of a strict-positive compact recurrent set is a corollary of that same global attraction. The earlier published result therefore fully implies every asserted new global conclusion. The repository’s visible prior import (2026-10-11 13:59 UTC) postdates the assessed source import (2026-10-11 13:03 UTC), while the older result’s scientific record and dated audit identify 2026-10-04; this priority-timestamp distinction is explicitly retained, not silently resolved. As of this review the theorem is already present in the published result corpus, and no independently new mathematical claim remains.

## value

FAIL

Global delay-independent predator extinction at a maturation-adjusted invasion threshold is mathematically meaningful in its own right, but it had already been established for the identical Kong–Shao system in the dated 2026-10-04 published Resultary finding. That earlier finding even repairs the faulty source extinction calculation and exhibits a strict threshold improvement. The candidate’s distinct exposition, limiting choice of Lyapunov weight, algebraic interpretation as the undelayed local stability surface, derived absence of interior recurrence, and specific sample value 93/928 supply no new theorem, boundary case, natural invariant or independently valuable classification. Repackaging this covered result as another standalone contribution is a known-result recomputation, not a motivated new mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
