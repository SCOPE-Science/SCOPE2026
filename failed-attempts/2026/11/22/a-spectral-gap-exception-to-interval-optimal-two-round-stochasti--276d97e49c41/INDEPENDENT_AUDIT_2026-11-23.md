# Independent mathematical audit

## correctness

PASS

Under the frozen hypotheses (finite irreducible reversible chain, no holding, bipartite support, at least three states, 0<s<3−2sqrt(2)), sign conjugation gives the actual modes −1 and s and all other nonstationary modes in [−s,s]. The self-adjoint homogeneous factors reduce the centered norm to max |p(lambda)| with p(lambda)=(1−alpha+alpha lambda)(1−beta+beta lambda), p(1)=1 and p(0)>=0. An independent lower bound follows by interpolation at −1,0,s: 1=((1−s)/(1+s))p(−1)−(2(1−s)/s)p(0)+(2/(s(1+s)))p(s). The positive endpoint weights sum to (2−s)/s, so R>=s/(2−s), and equality forces p(0)=0 and both endpoint values equal to R. One gain is then 1 and the other is uniquely 1/(2−s). Its multiplier lambda(lambda+1−s)/(2−s) attains R at the two endpoints and has modulus <=R on [−s,s]. The single repeated factor is minimized by balancing s and −1, yielding 2/(3−s) and the stated squared norm and strict difference. For the enclosing interval [−1,s] in lambda, the normalized degree-two Chebyshev polynomial is feasible precisely through the stated low-s branch, with its largest lambda-root at most zero (equivalently both Richardson gains are <=1). Its value is (1+s)^2/(s^2−14s+17), and subtraction gives the stated strict gap in the open range, vanishing at the threshold. The crown block (J−I)/(m−1) gives the displayed spectrum; m=7 is the first subthreshold order and gives the concrete exact actual/repeated/interval values 1/11, 49/289, 49/529. The supplied verify.py and VERIFICATION.md were inspected, not executed. These are conclusions about the stated fixed two-gain family, not unrestricted graph weights or total variation.

## originality

FAIL

Concrete prior implication: the cited Richardson frontier's published boundary-branch proof already contains the sharp endpoint-only minimax inequality, extremizer and equality cases needed here, even in the audited low-s regime. Although the earlier statement of its interval boundary branch restricts the normalized lower endpoint a to a<=sqrt(2)−1, the actual endpoint argument uses only 0<a<1/2. Translating that argument gives exactly this two-round lower bound and unique gains. The one-line check on the bipartite inner cluster makes that same endpoint extremizer admissibly optimal; the comparison is then subtraction from the frontier's already published low-condition-number branch. This is a direct consequence of the earlier proof plus the spectral enclosure, not just a similar interval theorem in a different parameter range. No distinct surviving result is established by the crown specialization.

## value

FAIL

Actual-spectrum versus robust interval tuning is a meaningful design comparison, and the numbers are correct. But the claimed distinct contribution consists of rescaling the already solved endpoint problem, checking a linear factor on the bipartite enclosure, subtracting the known interval optimum, and evaluating a standard crown spectrum. There is no independent new extremal invariant, witness requiring additional analysis, or nonroutine scientific remainder to retain as a separate finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
