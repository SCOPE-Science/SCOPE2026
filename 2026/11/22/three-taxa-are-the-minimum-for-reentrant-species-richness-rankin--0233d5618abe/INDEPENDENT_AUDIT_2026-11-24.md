# Independent mathematical audit

## correctness

PASS

The marginal Poisson zero probabilities and linearity give the stated exponential difference, without requiring joint independence. The one-taxon sign is immediate. For two discordant taxa, divide Δ(v) by v and express it as the Laplace transform of 1_[b1,a1]−1_[a2,b2]. Nested intervals give one sign (or identity). Otherwise cancel their overlap: the two remaining intervals have opposite signs and are ordered. The ratio of the left to the right interval's Laplace masses is strictly increasing, by differentiating its log and comparing the two mean rates; thus any positive root is unique and transverse. Its existence is exactly opposite strict signs of the length difference at v=0 and of the leftmost surviving contribution at large v. Unequal minima give the latter sign; equal minima imply nesting. Equal total lengths give no interior zero. The concordant case is termwise. An independent exact check (python /workspace/branches/independent_frozen_checks.py 2) confirms the factorization for the six rates. Each of the two factors has one simple root in (0,1), and their roots are r and sqrt(r), so the signs and efforts follow. Simple crossings persist locally; compact subintervals away from the two roots retain their signs, and the positive total difference and separated smallest rate preserve the two tails uniformly for nearby rates. Appending identical rates cancels them exactly. No field validation or equal-total threshold is proved.

## originality

PASS

Supported distinct claim: the minimum of three for two reversals at common nominal effort with unrestricted positive capture rates, together with the exact two-taxon criterion and the three-rate witness. Expected-richness formulas, multiple ecological crossings in general, and the underlying exponential-sign tools are not original here. The closest theorem imposes a normalization constraint on the exponentials and does not cover the witness or arbitrary rates.

## value

PASS

The question arises when two methods have different total capture intensities but are compared at a common effort. The complete two-rate rule identifies when an endpoint reversal is possible, while the explicit robust three-rate example establishes where endpoint signs cease to determine the interior ranking. This is a sharp, interpretable boundary for the expectation model, not an empirical performance claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
