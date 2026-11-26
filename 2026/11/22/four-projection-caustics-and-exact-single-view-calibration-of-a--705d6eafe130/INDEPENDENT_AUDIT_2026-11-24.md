# Independent mathematical audit

## correctness

PASS

PASS for the complete replacement files in /workspace/repairs/1, not for the frozen claim. The original physical caustic positions and R-inversion were false: the orthonormal rotated components of each cardinal unit vector are ±1/√2, so their stationary half-width is R/√2, not R. For R=1 and (cos φ,sin φ)=(4/5,3/5) the original even places the outer caustic at 4√2/5>1, outside the particle's deterministic norm bound R; the true four locations are ±4/5 and ±3/5. The verified repair uses normalized coordinates √2 U/R and √2 V/R, corrects both projection coefficients and gives R=√(s²+h²). The two telegraph signs are independent by the equal-rate product generator; zero flux yields f(u) proportional to (1−u²)^(β−1). The line projection hits only four corners at the four generic locations; away from them one can integrate in a fixed endpoint coordinate with smooth bounded z derivatives on the other factor. The same-sign corner convolution is a beta simplex integral with coefficient B(β,β); at the opposite-sign corner either side rescales to the same integrable kernel t^(β−1)(1+t)^(β−1), giving B(β,1−2β). Both include the factor 2^(2β−2)/( (ab)^β B(1/2,β)^2 ), now using corrected physical a,b. Reflection gives the ratio 1/[2 cos(πβ)], strictly increasing on the relevant interval. The critical corner integral is 2 arsinh√(L/|δ|), with a bounded correction, giving the stated logarithmic coefficient; above criticality the unscaled corner integral has an integrable majorant. The outer limit at criticality is 1/(2π√(ab)), and the disjoint inner-corner contributions add in the coalesced view. The original checker was inspected, not executed: its abstract a,b geometry never ties the projected square to the actual speed. The privately supplied replacement RESULT.md, CHECK.py and VERIFICATION.md fix those affected materials. The newly written replay `python3 /workspace/repairs/1/CHECK.py` passed two direct physical-geometry comparisons, four ratio checks, 24 subcritical and six critical density comparisons; those are finite checks, not the proof. The original files and verification front matter are preserved.

## originality

PASS

For the repaired result, the supported distinct claim is the generic-view four-location leading-law extraction, including the two-sided coefficient and universal ratio, and identification from those particular singularity data. The stationary product law, the axis projection and its coalesced critical logarithm are prior coverage. Even the candidate corner locations are immediate from the known support geometry once physical speed is aligned. No originality is attributed to the normalization correction itself.

## value

PASS

The repair retains a motivated inverse problem: recovering a time-scale ratio, physical confinement length and orientation (up to square symmetry) from a single unit-axis stationary position readout using only singularity locations and leading amplitudes. The universal amplitude ratio is a quantitative, view-independent consequence of two different corner geometries and provides an exact structural statistic; the contribution is not the normalization correction or a re-evaluation of an axis marginal. The claim is limited to the athermal stationary law and generic subcritical views, with no assertion of finite-noise or finite-sample recovery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
