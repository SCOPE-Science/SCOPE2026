# Independent mathematical audit

## correctness

PASS

An independent geometric derivation takes L=range(Omega), S=diag(1,delta I) and (SL)^perp=S^(-1)L^perp. For X=||proj_(L^perp)e_1||^2, the unit projected direction has axial squared component X; its rescaling under S^(-1) stays orthogonal to S^(-1)(L^perp intersect e_1^perp). The squared component in the new complement is therefore X/[X+delta^(-2)(1-X)]. Haar L gives X~Beta((n-s)/2,s/2), hence the stated independent chi-square ratio. Trace splitting gives the exact rank-s baseline plus the weighted deficit, and Euler's beta integral gives the moment formula. With a=s/2, b=(n-s)/2, the odds N/D have density t^(a-1)(1+t)^(-a-b)/B(a,b). For q<a use integrability of t^(-q); for q>a substitute t=delta^2 v and obtain B(a,q-a). At q=a the scaled kernel is 1/v+O(v^(-2)) on [1,delta^(-2)] before damping; the damping changes the integral by O(1) there and the two outside pieces are O(1), proving the factor 2 in front of log(1/delta). The fixed-threshold tail integrates the odds density to delta^2(1-u)/u, giving the stated coefficient. Substitution at q=1 verifies all probe-count and leading residual claims. The full-rank QR identity makes p=2 the row-aware left space, not its right factor or final reconstruction. This does not assert uniformity as n,s,q vary. The uploaded checker was inspected, not executed; archived finite-check claims are not an independent certificate.

## originality

FAIL

The bundled exact one-spike range-residual law and the titular mean transition are already stated in an equivalent natural parameterization in a distinct available Resultary record. In particular, apparent odd-power coverage does not leave a separate even-power overlap law: the zero-power-step case permits any positive spike ratio, and a change of spike variable plus a deterministic loss conversion gives the entire frozen overlap law and its mean comparison. The frozen all-q constants and fixed-u tail are not separately printed there, but follow from its exact ratio by the beta integral, the same endpoint rescaling with exponent q, and the beta CDF at zero. The date labels do not settle who derived the results first. No narrowed repair is submitted.

## value

PASS

The problem is a natural test of pass count and sketch width at fixed rank, not a numerical slice. The exact critical order and leading constants explain which losses are dominated by rare nearly missed spikes, and the baseline comparison identifies what extra passes buy for the left range. This scientific motivation does not undo the demonstrated originality overlap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
