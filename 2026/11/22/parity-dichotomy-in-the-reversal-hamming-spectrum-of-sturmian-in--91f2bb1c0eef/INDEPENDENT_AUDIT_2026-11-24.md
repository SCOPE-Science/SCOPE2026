# Independent mathematical audit

## correctness

PASS

Every finite difference factor has a generic mechanical realization and every initial residue is obtained by an integer phase translation, so interval coding on the length-m circle gives precisely the required factor language. For the forward/reversed pair the phases at position i add to a constant C. In a given symbol cell the equality set is its overlap with the reflection of that same cell about C/2, with periodic triangular length centered at 2j+1. The centers run over every residue once at odd m and over the odd residues twice at even m; the resulting agreement lengths are 1 and 2 dist(C,2Z), respectively. Uniform arc discrepancy applies to all these finite unions, including when C depends on n. At every length any C can be prescribed while avoiding both phases' countable boundary sets, giving the reverse Hausdorff inclusion as well as the forward one. Uniformity is for fixed irrational alpha and m, over factor pairs. For bounded type, alpha/m remains badly approximable, and denominator blocks of its rotation have bounded arc discrepancy; the bounded-digit continued-fraction decomposition needs O(log(n+1)) blocks. This proves both the spectrum and its minimum, with the pairwise estimate at odd m understood for d_H(u,rev(v)). Exact midpoint-grid overlap checks and independent substitution-based full spectra for m=2,...,7 at n=37,91 are in python3 /workspace/checks/finite_review.py 1 and /workspace/checks/1.txt. Those are finite checks, not evidence for all slopes or the asymptotic rate.

## originality

PASS

The modular-difference model, general rotation-coding and discrepancy machinery, and a direct overlap about exact reversals are already known. The supported distinct claim is the full parity-dependent asymptotic spectrum in ordinary Hamming distance and its uniform approximation, not the lift, strict ergodicity, or the obstruction to nonconstant exactly reversed pairs. The comparison is best-of-knowledge rather than a certification of priority.

## value

PASS

Reversal is a natural symmetry test for a low-complexity language. Classifying the whole distance spectrum, not merely ruling out exact reversals or calculating a typical frequency, distinguishes odd alphabets with uniform asymptotic separation from even alphabets admitting a continuum of distances. The fixed-slope uniform bound makes the classification applicable to the entire finite language at every large length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
