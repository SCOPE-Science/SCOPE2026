# Independent mathematical audit

## correctness

PASS

PASS: For any bounded convex planar Ω, the solution of (Δ−μ²)v=0 with boundary data 1 satisfies 0<v<1. The centered inscribed disk B_d(x) is contained in Ω; its explicit radial comparison b(z)=I_0(μ|z−x|)/I_0(μd) has b=1 on the circle, and the maximum principle gives v(x)≤I_0(μd)^{-1}. Strong maximum principle forces equality only if Ω equals the disk. A supporting line to Ω at a closest boundary point y gives an inward normal distance s with s(x)=d, and φ=e^{-μs} solves the same PDE while φ≤1 on ∂Ω; strict maximum principle gives v(x)>e^{-μd} for bounded Ω. Large tangent disks B_R((0,R)) with x=(0,d) have v(x)=I_0(μ(R−d))/I_0(μR)→e^{-μd}. This proves the exact infimum/supremum and nonattainment at finite R for the stated domain class.

## originality

FAIL

FAIL: The two-sided envelope is mechanically implied by stronger prior results and standard named comparison principles rather than a new theorem. Nazarov (arXiv:2609.06523v1, Theorem 1) already proves |∇v|≤μv throughout every bounded convex Lipschitz planar Ω, which integrated from the boundary gives v(x)≥e^{-μd}; his Section 3 explicitly constructs the supporting-half-plane exponential barrier and proves V_μ<v_μ throughout Ω, yielding the claimed strict lower inequality at the nearest supporting point directly. Kuznetsov (arXiv:2403.09382v2) records exact half-plane exponential and disk Bessel model solutions. The upper bound is the immediately standard maximum-principle domain comparison with the inscribed disk; the equality case follows automatically by the strong principle, while the lower tangent-disk limit is the standard I_0 asymptotic. The full optimization is a direct recombination of those known comparisons, not a distinct mathematical advance; an absence of matching wording is immaterial.

## value

FAIL

FAIL: Sharp universal distance envelopes are a natural PDE question, but in this precise package both components and their extremizers follow without an additional mathematical obstruction from Nazarov's existing supporting-line barrier, Kuznetsov's explicit disk/half-plane models, ordinary monotonicity and the textbook Bessel asymptotic. No new structural lemma, nontrivial cutoff, boundary classification beyond an immediate equality application, or unknown exact invariant is established. Mathematical correctness and convenient packaging alone do not satisfy the substantive-value requirement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
