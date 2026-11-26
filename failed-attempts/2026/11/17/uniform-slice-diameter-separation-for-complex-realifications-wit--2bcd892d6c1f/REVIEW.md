# Independent mathematical audit

## correctness

PASS

The assertion holds on the underlying real space, with no complex-linear rank-one assumption. For a real slice S=f>1-alpha, choose a unit x in S using sup over the unit sphere f=1. Independently deriving the exact needed slice criterion, apply real ADP to T(v)=f(v)ix, of norm one. Given 0<epsilon<min(alpha,1), take a unit v and sign sigma with ||v+sigma f(v)ix||>2-epsilon. Replacing v by -v if necessary preserves the norm and allows f(v)>=0. The triangle inequality forces f(v)>1-epsilon, so v is in S, and ||v+sigma ix||>2-2epsilon. On the other hand, ||v+sigma ix||<=||x+sigma ix||+||v-x||<=sqrt(2)+diam(S), with ||x+sigma ix||=sqrt(2) by complex homogeneity, not by any inner-product assumption. Taking epsilon down to zero gives the exact displayed lower bound for every real slice. This excludes denting points and a dentable unit ball; the RNP would make the ball dentable. Inspected frozen RESULT.md and VERIFICATION.md. No computational certificate is needed. The result is conditional on real ADP and does not prove sharpness, a diameter-two property, or a statement about weakly open sets.

## originality

FAIL

The claimed value is not located as a separately named theorem, but is a mechanical substitution into the established real-ADP slice characterization, reproduced verbatim in an accessible earlier primary source. Taking its arbitrary unit direction z to be ix for an arbitrary unit member x of the slice gives max-sign near-2 witnesses. Their distance from x is at least 2-epsilon minus max-sign ||x±ix||, which equals sqrt(2). No additional geometric estimate or unknown case is needed. The qualitative RNP consequence is not a separate novelty claim. The failure concerns prior implication, not falsity, inaccessible literature, or a claimed verbatim match.

## value

FAIL

Quantitative slice structure in this class is a natural question, but the frozen assertion is only a routine bound from the triangle inequality, with no evidence that the specific scale carries geometric significance. In fact the same witness immediately gives a strictly stronger bound of one: take a real norm-one functional g norming v+sigma ix for a witness with norm at least 2-epsilon. Then g(v)>=1-epsilon and sigma g(ix)>=1-epsilon. Applying g to the complex rotation circle of x gives g(x)^2+g(ix)^2<=1, so ||v-x||>=g(v)-g(x)>=1-epsilon-sqrt(2epsilon). Taking epsilon down to zero proves the comparison. This observation is not a repaired result or a priority claim. The frozen value does not settle a sharp threshold, introduce new geometry, or add a previously unknown qualitative consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
