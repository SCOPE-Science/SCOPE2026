# Independent mathematical audit

## correctness

PASS

With L=T/2 and u=|t-L|, the nonconstant part is 2a exp(-αL) cosh(αu) - 2b exp(-βL) cosh(βu). On u>0 the sign of its derivative is that of aα exp((β-α)L)/(bβ) - sinh(βu)/sinh(αu). The ratio increases strictly: its log derivative is β coth(βu)-α coth(αu)>0 since (x coth x)'=(sinh x cosh x-x)/sinh²x>0. Thus an interior stationary point can only be a strict maximum, and the tied endpoint values are strictly below all intervening values. Factoring the endpoint-minus-midpoint difference as a(1-exp(-βL))²(R²-r), where R=(1-exp(-αL))/(1-exp(-βL)), proves the comparison. Indeed R is the weighted mean of (α/β)exp((β-α)v) over 0≤v≤L with weight β exp(-βv), so R increases strictly from α/β to 1, with neither limit attained at a finite positive horizon. This checks equality at r=c² and r=1 and all the stated tie counts. In slope balance, r=c, the curvature changes sign at exp((β-α)L)=β/α; at equality the fourth derivative is 2aα² exp(-αL)(α²-β²)<0. The inward derivative at the left endpoint is aα(exp(-αT)-exp(-βT))>0. Hence above the local threshold there is exactly one intervening maximum per half, and at the local threshold the center is still strictly worse than the global minimum, proving strict ordering of the thresholds. The normalized case factors R=1/(1+exp(-T/2)) and sinh(2u)/sinh(u)=2cosh u, giving both elementary thresholds and the quoted maxima. Positive minimum separation just truncates the same derivative argument. The open-domain comment should be read as excluding endpoint schedules: if they are the only closed-interval minima the infimum is unattained, whereas at the three-way tie the midpoint still attains the infimum. The source checker was inspected, not run; its assertions are only finite diagnostics.

## originality

PASS

Best of inspected evidence for the exact constrained optimization and the distinct earlier local threshold, not for the two-exponential ingredient or the biological idea of priming. Related timing objectives, the opposite-sign problem, and classical Morse lattice minimization do not furnish these minimizers or imply their thresholds under the stated quantifiers.

## value

PASS

A pinned three-event schedule is the smallest nontrivial free-gap experiment for a pairwise memory cost. Giving the full optimizer set and proving a nonempty interval where a locally optimal midpoint remains globally worse is useful even without further model extensions: local optimization can return the wrong schedule. Exact coexistence of the local minima and exact global ties make the result a usable mathematical benchmark, not evidence of ecological efficacy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
