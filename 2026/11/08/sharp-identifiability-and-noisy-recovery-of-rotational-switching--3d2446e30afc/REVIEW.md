# Independent mathematical audit

## correctness

PASS

For p>=5, 2<=ell<=p-2 and unit m mod p, bijectively change index to a circle interval of ell residues. Its lag correlation is max(ell-s,0)+max(ell-(p-s),0); subtract from ell to get exactly T=2 min(ell,p-ell,m,p-m). Only lags +/-m^{-1} maximize the nonzero correlation, yielding precisely phi(p)/2 necklaces modulo rotation (m and -m coincide). For odd prime p, balanced ell=(p+/-1)/2 gives injective T, while unbalanced ell has the claimed saturated fiber. Under independent phase resampling with known bit-flip epsilon, each noisy disagreement is Bernoulli with Q_r=2epsilon(1-epsilon)+2(1-2epsilon)^2 r/p. Hoeffding yields the upper error, and KL/Hellinger adjacent central hypotheses yield the lower, with epsilon=1/2 unidentifiable. The proof distinguishes independent phases from a continuous orbit.

## originality

PASS

The original Simpson rotation-word theorem supplies the dynamical symbolic family, Frid/Jamet enumerate broad rotation words, and Berstel/Vuillon recode rotations; the inspected complete primary materials do not give the sharp inverse adjacent-disagreement fiber classification and statistical noisy minimax p^2(1-2epsilon)^-4 law in this restricted family. Resultary searches returned closest rotation counting results with different observables. This is a best-of-knowledge PASS, not absolute novelty certification.

## value

PASS

This resolves a motivated identifiability problem for a concrete symbolic-dynamical family: exactly which period/occupancy regimes admit reconstruction from a single natural count, and how repeated noisy adjacent measurements scale. The sharp ambiguity phase and matching minimax lower/upper bounds separate inherent information loss from statistical error; they are reusable exact properties, not merely a tiny computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
