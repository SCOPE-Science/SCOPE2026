# Scientific review of the rank-by-weight census

## Correctness (C): PASS

The normalized Fourier transform diagonalizes convolution on the finite abelian group. At a nonzero fifth-root character, a zero multiplier is equivalent to equal populations on its five affine fibres, by the minimal polynomial \(1+X+X^2+X^3+X^4\). This yields packet sizes of four characters and reduces rank calculation to counting balanced pencils. The action of \(\operatorname{PGL}(2,5)\) justifies uniform intersection counts \(N_t\). Single and double intersections have elementary formulas; triple intersections are exact finite sums (3,125 or 100,000 row assignments). Four- and five-pencil intersections follow from a proof of Boolean additive-separability rigidity, not from a random test. Binomial inversion proves the complete table; complement symmetry handles weights fifteen and twenty. `line_incidence_checker.py` and `full_direct_check.c` independently verify the exact counts, the latter checking all \(2^{25}\) masks. The empty/full exceptions were checked explicitly. No claim beyond this finite group is proved.

## Originality (O): PASS under a bounded literature comparison

Meshulam (2003/2006) gives general inequalities but no rank-by-weight population table. Biró–Lev (2018/2021) improves the possible support-size region without the displayed full enumeration. Kiss–Somlai (2021/2024) establishes that exactly two special directions are impossible and classifies sets with exactly three special directions. Those results respectively cover the *absence of rank nine* and the geometry of the rank-thirteen class, so neither is claimed as original here. The new unit of contribution is the **entire exact joint distribution by support size and convolution rank**, including the ranks 17, 21, and 25 and their complete multiplicities; these were not stated or calculated in the inspected sources. A published 25-point Fourier-minor census concerns ranks of rectangular Fourier submatrices, not diagonal convolution operators. Published-record searches covering equivalent terminology and dimensions found no directly matching all-mask table. No search establishes absolute historical priority; unindexed tables remain a risk.

## Value (V): PASS

The problem is a canonical complete Fourier-support statistic: given an arbitrary binary sampling or averaging mask on the first nontrivial odd-prime affine plane, determine exactly how often convolution loses each possible number of Fourier directions. The output is a complete 33,554,432-mask, rank-resolved distribution and a constructive incidence method identifying how mask weight changes singularity. It distinguishes almost-full-rank masks from the rare three-direction deficient class, with exact frequencies rather than an undifferentiated singularity count. The proof combines a structural rigidity theorem, 2-factor counting, a manageable exact three-pencil coefficient enumeration, and binomial inversion. This is not a claim of universal recovery stability, and neither its correctness nor reproducibility alone is offered as its mathematical motivation.

## Closest sources and limits

- Roy Meshulam, *An Uncertainty Inequality for Finite Abelian Groups* (arXiv:math/0312407, 22 December 2003), general uncertainty bound.
- András Biró and Vsevolod F. Lev, *Uncertainty in finite planes* (arXiv:1808.07424, 22 August 2018), sharper finite-plane bounds and exceptions.
- Gergely Kiss and Gábor Somlai, *Special directions on the finite affine plane* (arXiv:2109.13992, 28 September 2021), the known no-two-special-directions theorem and exact three-special-directions geometry.
- *Complete rank incidence of fourth-order Fourier minors on \(\mathbb F_5^2\)*, public mathematical record, 8 November 2026, different restriction-of-matrix problem.

The finite census does not treat arbitrary complex weights, different primes, or quantitative inversion conditioning. The possibility of an unindexed earlier rank-resolved enumeration cannot be excluded. Code outputs are repeatable, not independent peer review.

Self-review: passed. Independent audit: not yet performed.
