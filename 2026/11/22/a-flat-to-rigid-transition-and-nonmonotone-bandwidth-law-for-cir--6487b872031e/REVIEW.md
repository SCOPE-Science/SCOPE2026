# Scientific review

## Correctness — PASS

All assertions refer to full circular distributional variation and normalized Lebesgue \(L^2\). The Jordan decomposition of a zero-total-mass derivative measure reduces the operator norm to arcs with variation two. The exact arc autocorrelation gives an explicitly integrated polynomial in width and length, whose derivative is positive before the half-circle endpoint and zero on a natural plateau for short windows. The Hilbert equality condition and strict nonzero-frequency multiplier bound prove *all* extremizers; no finite grid is used to infer infinite-domain uniqueness. The bandwidth derivative gives the unique global peak. The packaged exact-rational and symbolic checker reports 7,354 assertions, including separate Fourier comparisons. Risks: changing the meaning of variation at the periodic seam, or replacing the forward by centered averaging, would change the statement; both are fixed explicitly in the result.

## Originality — PASS (qualified)

Angeloni–Vinti's 2016 full article treats convolution-operator estimates and convergence in variation, not the present sharp one-sided circular BV-to-L2 residual. The investigated 2014 Dron–Zhuk primary results are formulated as L2 error/modulus-of-smoothness inequalities for *modified* Steklov operators. Discrete cyclic window variation amplification and Hardy–Steklov weighted bilinear norms likewise do not contain this operator-error norm by implication. Direct searches for one-sided boxcar/Steklov BV L2 sharp constants, extremizer lengths, and the half-circle phase boundary did not expose an equivalent theorem. The older Zhuk–Puerov 2009 full text could not be read; its title is closely related to Steklov L2 errors, so an unindexed antecedent remains possible. This absence of a direct match is evidence-limited, not a proof of novelty.

## Value — PASS

The exact sharp all-bandwidth norm and complete equality classification separate two genuinely different regimes: all arc lengths in a nontrivial interval are worst for short windows, whereas only semicircles are worst for long windows. In addition, the uniquely most damaging bandwidth lies strictly between half-circle and full-circle width: even the sharp error is nonmonotone under increased smoothing. These features are natural for moving-average approximation of BV jump signals, not an arbitrary finite grid or numerical constant. The closed form supplies a precise benchmark for one-sided convolution error analysis.

## Limits and closest literature

The general convolution-BV approximation results of Angeloni–Vinti (2016) and the modified-Steklov L2 approximation inequalities of Dron–Zhuk (2014) are complementary but not directly covering on the reviewed material. Zhuk–Puerov (2009) was identifiable through reliable metadata only, so priority remains qualified. No claim is made for centered boxcars, generalized Steklov kernels, complex variation or other exponents.

Self-review: passed. Independent audit: not yet performed.
