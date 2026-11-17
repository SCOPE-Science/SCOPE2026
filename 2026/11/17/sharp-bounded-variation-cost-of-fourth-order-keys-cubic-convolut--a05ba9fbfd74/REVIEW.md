# Review: Sharp bounded-variation cost of fourth-order Keys cubic convolution

## Correctness — PASS
The kernel is explicitly specified as three even radial cubics and reproduces constants. For every finite-variation sequence, decomposition into its summable discrete jumps reduces the operator norm to the continuum variation of one step response. That response has five exact cubic pieces; a direct calculation locates the far and near lobes at \(1/81\) and \((260+43\sqrt{43})/5832\), with a strictly increasing central piece. Their variations sum to \((1790+43\sqrt{43})/1458\). The single-step sequence attains equality, and the difference theorem follows from linearity. The accompanying algebra checker reproduced the critical equations and random finite examples. Domain, support, constant component, end behavior and sharpness have been checked.

## Originality — PASS (qualified)
Keys (1981, pp. 1154 and 1160) supplies the exact four- and six-tap cubic convolution kernels and their approximation orders, not this discrete-BV to continuous-BV sharp norm. Meijering–Unser (2003) proves an equivalence with Karup–King and Henderson osculatory interpolation and does not state this norm. Malgouyres–Guichard (2001) analyzes direction-preserving zooming and total-variation-based nonlinear image restoration, not the present one-dimensional six-tap operator gain. The closest independently recorded cubic-interpolation results concern pointwise overshoot, global cardinal cubic splines or nonlinear Hermite slope choices; these do not imply the exact six-tap gain. Stronger unindexed results on oscillatory kernels remain a residual historical-priority risk.

## Value — PASS
Six-tap fourth-order Keys reconstruction and four-tap third-order Keys reconstruction are classical competing accuracy choices. Edge variation is a natural stability metric that captures oscillatory ringing invisible to polynomial-reproduction order alone. The new exact attained norm resolves the worst-case BV cost of the higher-order choice and shows a strict increase of \((43\sqrt{43}-100)/1458\). This precise invariant supports stability-conscious comparison without assuming a general downstream theorem; it is neither a renaming nor a computation reproduced from a published table.

## Limitations
Applies to real bi-infinite uniformly sampled data of finite discrete variation and exactly the even six-tap support-three Keys cubic-convolution kernel. No result for arbitrary fourth-order interpolation kernels, nonuniform meshes, boundary closures, or two-dimensional image total variation. The printed 1981 Keys paper is known at month precision, while the dated openly released 2001-02-21 source is the earliest independently day-verified public archival lead used in chronology; this is not a claim of 2001 invention. Historical mathematical priority remains qualified pending unindexed literature.

Self-review: passed. Independent audit: not yet performed.
