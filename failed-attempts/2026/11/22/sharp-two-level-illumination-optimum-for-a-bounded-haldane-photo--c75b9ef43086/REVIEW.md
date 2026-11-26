# Independent mathematical audit

## correctness

PASS

For d(u)=1+u+cu², differentiation gives f′=(1−cu²)/d² and f″=2Q/d³, Q(u)=c²u³−3cu−1. The cubic decreases until 1/sqrt(c) and then increases through its unique positive root r_c. Thus when L≤r_c strict Jensen gives the unique point mass, including L=r_c. For L>r_c the quadratic P(q)=c²Lq²−2cq−cL−1 has one positive root; P(L)=Q(L)>0 gives q<L, and substitution gives Q(q)=(2cq+1)(q/L−1)<0. The positive root is exactly the stated radical. I independently checked the polynomial coefficient identity d(q)^2 d(u)[ell(u)−f(u)]=(u−q)^2[(1+2cq)+c(1−cq²)u] for the tangent ell at q. The quadratic makes c(1−cq²)=−(1+2cq)/L, so the gap is nonnegative and its exact contact set on [0,L] is {q,L}. Joining f on [0,q] to ell yields a differentiable concave majorant; Jensen bounds all Borel laws, and the point mass or the stated two-atom law attains the bound, proving it is the least concave majorant. For a mean below q a tangent of this majorant meets it only at the mean by strict curvature on [0,q] and the strictly lower slope beyond q. For m≥q integrating the exact tangent gap forces support {q,L} and the mean fixes the weights, reducing to the appropriate point mass at each endpoint. The exact loss identity and the c=1,L=10,m=4 numerical example were checked independently; replay with python3 /workspace/checks/frozen_exact.py 5. The submitted verifier was inspected, not executed. Uniqueness concerns the probability law, not any ordering or timing of exposures, and does not extend to transient photobioreactor control.

## originality

FAIL

The directly comparable Resultary record fd7932496d0a publishes the sharp bounded fixed-mean constant-versus-two-level classification for the Haldane substrate-inhibition response, including uniqueness, and additionally treats the uncapped problem. Standard positive scaling identifies the bounded equilibrium optimization problems exactly; calling the control irradiance instead of substrate does not add a constraint or change the objective. The radical and factored deficit are explicit useful formulas, but once the nontrivial Haldane envelope is identified the formulas are mechanical consequences of its contact and the rational denominator. I do not claim that the other record literally displays the same formulas, or infer publication order from its date. This judgment rests on the express published scientific statement and mathematical reduction, not on unavailable text.

## value

FAIL

The mean-and-cap model is naturally motivated, and its optimizer and loss formula would be useful if the exact invariant were not already covered. For the frozen mathematical objective, changing substrate to equilibrium irradiance is only a scaling; the remaining explicit gap rewrites the supporting-line deficit using the same rational curve and contact set. No substantive new regime or independently useful unknown exact invariant survives that comparison. The record supplies no distinct transient or experimental result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
