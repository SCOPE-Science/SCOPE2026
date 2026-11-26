# Independent mathematical audit

## correctness

FAIL

The announced complete-period and Haar theorems are sound, but the frozen scope section (line 23) asserts E_m(n)=O_n(m) for a fixed ordinary integer n under least nonnegative residues. The bound is false as written: for n=−1 each term is k−1, so E_m(−1)=m(m−1)/2. More generally any fixed negative n has n mod k=k+n for k>|n|. The linear bound is valid for n≥0. For the core theorem, with g=gcd(a,b), the uniform common residue modulo g has variance (g²−1)/12 and conditional CRT independence leaves just that covariance, including equal moduli and modulus 1. Sum the means and covariances and use the Jordan divisor identity. Möbius inversion gives the uniform summatory estimate x³/(3ζ(3))+O(x²) for J₂; summing against 2r−1 at x=m/r gives the stated cubic coefficient, harmonic error O(m² log(2m)), and tail O(m²). Haar level marginals match the complete-period laws; Chebyshev on the squares and monotone interpolation prove the almost-sure limit without independence. The recorded finite tests were inspected, not rerun; they corroborate the main identities, not the fixed-negative-input scope aside or the asymptotic theorem.

## originality

FAIL

A distinct October 12 Resultary finding already states the same covariance, exact Jordan identity, leading coefficient and error, and convergence in probability. The Haar sentence is a direct consequence of this exact complete-period model and its variance bound via the canonical compatible coupling and a general monotone interpolation argument. This is coverage of the mathematics, not a bibliographic priority determination.

## value

FAIL

Complete-period fluctuation scale was a motivated question for this arithmetic object, but the exact covariance, cubic constant, and concentration are already available. The only apparent addition is an almost-sure restatement in the natural compatible coupling, obtained by a standard square-subsequence squeeze from the existing bound. It requires no new arithmetic estimates and preserves no substantively distinct finding suitable for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
