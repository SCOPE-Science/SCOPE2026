# Independent mathematical audit

## correctness

PASS

The normalized history kernel preserves the zero-frequency blocks. For each other block with frequency w, the Volterra equation reduces to the Kummer equation with a=i beta w/(r+iw); the analytic solution also solves the original Volterra equation because t^beta(f'+(r+iw)f) vanishes at zero. Volterra uniqueness follows by the integrated supremum bound and Gronwall. Both Euler exponents have positive real part. Splitting at u=1/2 and expanding at zero gives the nonzero leading coefficient B and an O(t^(-Re a-1)) plus exponential remainder. Re a strictly increases with |w|; orthogonal active blocks cannot cancel. At the threshold the minimal-gap primitive has nonzero logarithmic phase and an integrable remainder; larger-gap blocks are absolutely integrable. The real and imaginary Hermitian directions formed by A and its adjoint are orthogonal with equal norm since tr(A^2)=0, proving a genuine circle with the asserted radius and period. Above threshold, an independent check integrates the Volterra equation in time: the integrated history term equals beta/(beta-1) times the scalar integral by absolute Fubini, so -1=[-(r+iw)+r beta/(beta-1)] times that integral. This reproduces the rational coefficient; conjugate pairing gives the strict negative sign. The commuting case is stationary.

## originality

PASS

The scalar history equation and Kummer machinery are substantial prior ingredients. The pass concerns the integrated operator across the variable bias parameter, particularly the critical accumulation set and signed supercritical value, not the scalar solution, logarithmic instantaneous phase, or least-gap control of uniform-history relaxation by itself.

## value

PASS

The primitive is a natural measure of accumulated coherence and is not predicted by the fact that instantaneous coherence decays. The exact active-gap boundary separates power growth, bounded nonconvergence on a nonzero circle, and absolute convergence. The computable limiting response has strictly negative projection on the initial coherence, adding a sign constraint rather than only a convergence bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
