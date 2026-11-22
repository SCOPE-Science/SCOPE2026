# Scientific review

**Claim.** For every integer precision \(k\ge1\), the four aligned Fibonacci/Lucas square-status frequencies over their period modulo \(3^k\) are \((T_k+2B_k,2T_k,2T_k,3T_k-2B_k)\), with the explicit square-residue count \(B_k\). The limiting three-adic joint law is \((5/32,1/4,1/4,11/32)\), with \(O(\log(2N))\) error for every cutoff.

## Correctness — PASS

The matrix identity \(M^8=I+3A\) gives an exact period and the eight residue branches; the four normalized singular functions have unit leading slopes, implying exact isometries. Each singular square event is a single family of valuation cylinders. The finite square-residue count \(S_m\) yields the entire four-cell table, and the cylinder measures give the limiting values and discrepancy. The standalone verifier independently confirmed nine finite prime-power tables and 4,644 finite branch-isometry comparisons. The proof, rather than experimental extrapolation, supports every infinite conclusion. Zero is included as a square residue at finite precision; the three-adic distinction is explicit.

## Originality — PASS, qualified

Bundschuh–Bundschuh (2011), *Distribution of Fibonacci and Lucas Numbers Modulo \(3^k\)*, Theorems 1.1–1.2, provides the individual value-frequency distributions, while Southwick (2014), *The Lucas Numbers and Other Gibonacci Sequences Mod \(m\)*, establishes residue completeness. Neither inspected statement gives aligned two-sequence square statuses. The marginal histograms cannot reconstruct the joint table because index alignment is lost. The 2025 value-image density theorem concerns output residues, not joint index frequency. The 2006 integer perfect-powers theorem is global rather than local. An equivalent formulation in older, unindexed local-character literature is possible; no negative search establishes absolute novelty.

## Mathematical value — PASS

This determines a natural and previously unaccounted-for two-sequence local obstruction: although Fibonacci and Lucas numbers share their recurrence, the square events are negatively correlated, with an exact covariance. The four-cell law covers every three-power precision and translates to a quantitative all-index asymptotic; it requires a structural account of four distinct singular index branches, not a bare re-expression of marginal residue frequencies. It does not claim a general theorem at all primes or solve any global perfect-square classification.

## Limits and reproducibility

The result is for the fixed prime three. The standalone checker is a finite diagnostic, not an infinite proof. Source comparisons were made with the primary 2011 full PDF and the 2014 arXiv text, together with searches for equivalent and stronger local square statements. The possibility of an undiscovered older equivalent result remains a historical-priority risk.

Self-review: passed. Independent audit: not yet performed.
