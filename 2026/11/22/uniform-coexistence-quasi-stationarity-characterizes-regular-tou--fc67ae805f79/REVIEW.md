# Independent mathematical audit

## correctness

PASS

The affine divergence of the selection drift is λ 1ᵀAx and the covariance double divergence is −γd(d−1); thus L*1=−γ binom(d,2)−λ 1ᵀAx. Necessity follows by interior compactly supported tests: the linear term must be constant, is zero at the barycenter, and vanishes at all vertices, giving A1=0 because λ>0. For sufficiency one can avoid a killed-generator core assumption: in the regular case h=∏x_i satisfies Lh=−αh with α=γ binom(d,2) and h=0 at the first boundary. Stopped Itô and boundedness on finite time intervals give P_t^k h=e^(−αt)h and hence a conservative h-transform. Its neutral drift γ(1−dx_i) is (2h)⁻¹∑_j ∂_j(h a_ij) in affine coordinates. The remaining drift b satisfies div(hb)=0 by the divergence identity and b·∇h=0. Boundary flux in the stationary integration by parts vanishes. This gives stationarity of hν for the transformed process by the well-posed compact-simplex martingale problem and invariant-measure criterion (neutral positive mutation plus a bounded Girsanov drift b=a(λ Ax/γ)). Undoing the transform with nonnegative f/h establishes the killed eigenmeasure identity for every measurable set, with no issue of unbounded f/h by monotone convergence. The invariant law after normalization is Dirichlet(2,…,2).

## originality

PASS

On the strength of the bounded comparison, the supported distinct result is the iff classification of uniform first-boundary quasi-stationarity for positive tournament selection, and its exact law in the regular case. The tournament generator, neutral laws, general adjoint methods and the Doob transform construction are not original here.

## value

PASS

The result gives a checkable structural criterion for an exact first-species-loss law despite nonzero circulating selection. It distinguishes QSD of a killed law from deterministic coexistence and from stationarity of the conditioned diffusion, and gives the converse rather than only a construction of examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
