# Independent mathematical audit

## correctness

PASS

Stopping the centered martingale X_t+(epsilon/gamma)*sigma_t at the first hit of either -L or N is valid: the stopped process is bounded, and the finite strip has paths to absorption from every state, including at epsilon=D because flips remain possible. The far-left exit probability is at most (N+2epsilon/gamma)/(N+L) from 0, so contact is almost sure and bounded harmonic solutions are unique. Independently, at spatial jump times the interjump spin transition Q has eigenvalues 1 and c=D/(D+gamma); the right/left substochastic jump kernels A_+, A_- multiply Q's columns by the respective directional probabilities. Skip-free first passage and the strong Markov property give H=A_+ + A_- H^2 for passage through one level, with H^N for N levels. Direct exact symbolic substitution (python /workspace/review-work/check-arrival.py) verifies the candidate stochastic H with first column (K+(1-K)rho,K(1-rho)), invariant mark law (K,1-K), and eigenvalues 1,rho. Its powers give the bounded Dirichlet solution, hence the stated fair-start law. The b=1 contact must have plus mark, and at b=0 the mark at a spatial hitting time is fair under the fair initialization; the displayed formulas agree. The strictly increasing geometric approach holds only in the stated strict-bias range. On any fixed horizon the spatial clock is independent Poisson of rate 2D and conditional on its finitely many positive gaps, spins at jump times tend jointly to independent fair signs as gamma tends to infinity. The unmarked walk therefore converges to the symmetric walk while the marked contact law tends to (1+b)/2 for N>=1. At zero flip rate and positive bias the two initial signs have different contact probabilities, so the separate defective-hitting calculation does not contradict the theorem. The frozen reflected-left checker is a finite diagnostic, not the infinite-domain proof.

## originality

PASS

The existing exact lattice-model and scalar first-passage-time results do not give this state-resolved hitting law, and examined directional or continuum first-passage results use a different state or process. This best-of-knowledge judgment concerns the displayed lattice law and fast-tumbling contact bias, not the origin of the model or renewal method.

## value

PASS

The arrival spin is a natural capture statistic that cannot be replaced by the known time-to-hit or the deterministic incoming direction. The exact law gives its whole distance dependence and shows a residual directional sampling bias even in a symmetric unmarked fast-flip limit. This exact distinction can matter for mark-dependent boundary reactions and is not a recomputation of a scalar position observable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
