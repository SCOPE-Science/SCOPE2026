# Review of Fourier-null rigidity of residue-deformed cubic moment curves

## Correctness — PASS
The domain is the complete additive character group of \((\mathbb Z/p^2\mathbb Z)^3\), for every prime \(p\) and every triple of residue-dependent functions. The key equality is exact orthogonality on each input residue fibre, not an asymptotic stationary-phase approximation. When the derivative quadratic has at most two roots, their odd-order roots of unity cannot cancel. At the two small primes, the only identically-zero derivative cases are checked by residue parity and divisibility by the ninth cyclotomic polynomial; these prevent spurious cancellation. Imprimitive frequencies reduce to prime-level permutation polynomials. Independent count of rootless derivatives and a collision argument for depressed permutation cubics lead to the exact nullity and rank. The supplied cyclotomic verifier was executed successfully in addition to the proof.

## Originality — PASS under bounded comparison
Cochrane–Zheng's general prime-power stationary phase is fundamental prior art, so the reduction itself is **not** claimed as new. The published prime-square \(\{(t,t^3)\}\) spectrum theorem uses the same prime-square cancellation mechanism for a two-coordinate cubic graph but classifies orthonormal bases, not the full Fourier-null set for \(\{(t,t^2,t^3)\}\) and its \(p^{2p}\) distinct deformations. Haessig's cubic exponential-sum \(L\)-functions concern prime fields, while Segers–Zúñiga-Galindo provide general prime-power estimates. A published local finite-field moment-curve stability result treats a different extension invariant. Searches found no directly covering exact three-coordinate rank law or all-residue-perturbation invariance. The primary literature may contain an equivalent unindexed specialization; absence of a result in search is not itself a proof of priority.

## Mathematical value — PASS
The cubic moment curve is a canonical arithmetic Fourier object. Its exact prime-square convolution rank, three-characteristic boundary behavior, asymptotic half-density of Fourier zeros, and invariance across an exponentially large family of genuinely distinct deformations provide a complete natural spectral invariant. This is not an arbitrary finite slice or a restatement of point counts: it determines every zero Fourier direction and thus the entire convolution kernel. It does not purport to solve more general higher-power or arbitrary-polynomial questions.

## Risks and verification limits
The independent mathematical audit has not occurred. The all-prime proof depends on exact cyclotomic cancellations and classical permutation-polynomial reasoning, all reconstructed here. Exhaustive numerical runs stop at finite moduli; their role is reproducibility, not infinite certification. The literature survey is bounded; there may be a stronger historical theorem that subsumes this result.

Self-review: passed. Independent audit: not yet performed.
