# Scientific review of the displaced-target last-visit theorem

## Correctness — PASS (self-review)

For each fixed \(p\in(3/4,1)\) and \(q\in[0,1]\), the exact transition rule makes the future discount \(R_{n,m}S_m\) a martingale. Its conditional quadratic variation has deterministic Brownian-clock limit \(v_a(t)=[1-(1+t)^{-\delta}]/\delta\) for starting positions of order \(\sqrt n\). The target at \(k_n/\sqrt n\to c\) is transformed into the genuinely moving boundary \(c(1+t)^{-a}\). A nearest-neighbor crossing argument gives its finite-horizon hitting kernel; a Doob maximal bound and a Gaussian small-window estimate eliminate hits beyond rescaled time \(T\to\infty\). A maximal Azuma bound supplies an integrable spatial envelope. The proved uniform lattice local limit theorem justifies the normalized parity-lattice sum and the conditional position distribution. Brownian path continuity and Tonelli's theorem identify the integral as an expected range. Convexity, Brownian sign symmetry, full support near the zero path, and deterministic range inequalities prove evenness, strict increase, bounds and asymptotic growth. The proof establishes the continuum theorem; the 3,174 exact rational checks and three seeded grid diagnostics in `verify.py` do not purport to prove any infinite claim.

The dependence on the initial bias disappears only in the coefficient \(f_{q,a}(0)=f_a(0)\), a published property; conditional future laws are treated for every admissible starting state, not assumed independent of bias.

## Originality — PASS against accessible evidence

The closest published source is Trinas, *The Prodigal Elephant Returns* (arXiv:2611.01279v1, submitted 2026-10-31), which proves last visits for fixed sets or sets inside \(o(\sqrt n)\), and explicitly lists target locations of order \(\sqrt n\) as future work. A 2026-11-08 public result on *centered intervals* at radius order \(\sqrt n\) (published-finding corpus `07dd1168bd98`) determines the expected length of a union of *intervals* swept by Brownian motion. It does not determine the range of a *single displaced point*: its theorem requires a symmetric interval centered at zero, and the elephant dynamics are not spatially translation invariant. The present theorem's strict monotonicity in the absolute displacement and coefficient asymptotic to \(|c|\) are also outside the prior centered-interval statements, which have large-radius coefficient \(2|c|\). Trinas and Valle (arXiv:2609.14753v1) prove an LLT, not displaced-target hitting; Fang (arXiv:2509.15049v2) treats trained initial histories and first returns in diffusive/critical regimes, not the superdiffusive displaced-site last-visit tail. Classical Brownian moving-boundary literature gives relevant tools but not this combined elephant-walk theorem. This priority assessment compares mathematical implications, not merely similar titles.

The risk remains that unlocated literature may include a general target-set extension implying the result; exhaustive priority or independent assessment is not asserted.

## Mathematical value — PASS

The source paper explicitly identifies \(\sqrt n\)-scale *location* as a gap. A displaced singleton is a canonical test of this gap, different from target enlargement. The theorem determines both the sharp probability exponent/coefficient and the complete conditional position law for all finite displacements. The new range functional is mathematically structural: it is even, strictly increasing, and has the exact universal large-displacement slope one, contrasting with the centered interval's slope two. These are not routine renamings of the zero-target result, because translating the elephant walk alters its transition law.

## Closest literature and scientific limitations

The strongest related statements inspected were Trinas (2026), Trinas–Valle (2026), the public 2026-11-08 centered-interval theorem, and Fang (2025/2026). The primary results and proof sections were examined directly where available. No rate in the observation index, parameter-uniform estimate, growing width, time-dependent target or elementary closed expression for the nonzero-displacement expected range is claimed. The published LLT and martingale FCLT are relied on as inputs. Historical priority is provisional and no independent mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
