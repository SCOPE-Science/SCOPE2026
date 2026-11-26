# Independent mathematical audit

## correctness

PASS

Assesses the corrected RESULT.md under /workspace/repairs/3/. The frozen Finding incorrectly says the product integrand is continuous at zero. For t>0 it behaves as t/(2π√λ); only the multiplier has a continuous extension to t. The corrected file specifies the integrable endpoint and clarifies that r=1 is on the unit circle. No formula, hypothesis or verification code changes. For the one-site unit-rate pulse, outward support growth has finite Poisson-dominated moments; the bond jump has drift (a−b)/(2W), telescoping over bonds, and second moment (a²−ab+b²)/(3W²). Thus X is a centered square-integrable martingale with variance derivative D=(2F_0−F_1)/3. Independently, track two energy labels with independent placements conditional on each bond split. Their separation law is p_0=F_0, p_k=2F_k for k≥1. Rates 0→1 and 1→0 are both 2/3 (same-bond split or reunion); 1→2 and both tail nearest-neighbor rates are 1. The forward equations reproduce the stated defect and tail coefficients. The decaying resolvent root yields D-hat=(1−b²)/(b(b²+2))=1/(2b)−3b/(2(b²+2)), b=1−r. At s=−λ+i0, Re b=λ/2, |b|²=λ and Im b=√(λ(4−λ))/2. Then |b²+2|²=3λ²−4λ+4, and −Im D-hat/π yields exactly the stated positive density. The physical branch |r|<1 off the cut has no poles; the O(s^−1/2) singularity at zero and the bounded upper endpoint contribute no atoms in the contour inversion. At t=0 the multiplier is zero; differentiating the compact-support representation gives strict increase and concavity and the generator yields D(0)=2/3 and D′(0)=−5/9. An independent bounded quadrature reproduced both spectral moment checks at numerical precision (replay: /workspace/branches/202609f9-72f6-462f-9b3a-0503c3f9f056/kmp_spectral_moments.py); this is not the inversion proof. Expanding b=√s−s/2+s^(3/2)/8+… gives D-hat=1/(2√s)+1/4−11√s/16+O(s); the density expansion and Watson's lemma give an integrable residual from the leading t^−1/2 derivative. Its integral is the transform limit 1/4 and its integrated tail gives −11/(16√(πt)). Rate two simply replaces t with 2t. Frozen support inspected, not executed.

## originality

PASS

The surviving claim is the exact finite-time microscopic variance (a compact spectral law for its derivative), including the subleading lattice terms. The leading long-time amplitude and the general moment-duality technique are not credited as new. The endpoint correction does not change the exact spectral or asymptotic claims compared with prior work.

## value

PASS

The first spatial moment is independently motivated by previous continuum work on localized energy release. Its exact lattice transient supplies a positive spectral benchmark and determines a nonzero additive correction and global concavity that the leading continuum law does not resolve. The repair fixes endpoint semantics without changing that scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
