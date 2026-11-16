# Scientific review of the four-class Paley sampling spectrum

## Correctness — PASS

The claim specifies the exact row measure and Fourier normalization, the prime class \(p\equiv1\pmod4\), and the four consecutive frequency indices. Satake's quadratic Gauss-sum evaluation gives the character Gram identity, and the reflection parity decomposition gives two explicit real-symmetric two-by-two blocks. Direct characteristic-polynomial calculations yield the four claimed spectra. The displayed radical comparisons identify both sharp bounds and all least-eigenvalue equality spaces; the exceptional rank-two case \(p=5\) follows by distinct-node Vandermonde rank. The asymptotics are exact consequences of the formulas, with infinitely many primes in each progression. Independently assembled Fourier matrices agree with the claimed eigenvalues across 37 primes. Finite calculations do not prove the general theorem.

## Originality — PASS, provisional historical priority

The nearest inspected source is Satake (arXiv:2011.02907), whose Lemmas 11–12 supply the essential character-sum Gram ingredient for the **augmented** Paley matrix, but whose main result gives conditional, general sparse RIP estimates rather than an explicit low-band spectrum after deletion of its constant sensing row. Magsino–Mixon–Parshall (arXiv:1905.04360) study random subensemble limits for Paley conference frames rather than the fixed consecutive four-frequency restriction. Waldron (arXiv:1806.06067) gives broad group-frame Fourier/Gramian theory, not this residue-class spectral statement. The strongest nearby research-record finding concerns four-column quadratic-residue sampling for \(p\equiv3\pmod4\), with a skew-character/tournament structure absent here. The present claim is not merely a relabeling of those statements: the four congruence classes, the rank-one removal term, and the least-eigenspace descriptions require an additional explicit calculation. Relevant inaccessible or differently titled specialist results remain a possible priority risk.

## Value — PASS

The four-character band is the first natural consecutive harmonic band in which both quadratic characters \(\chi_p(2)\) and \(\chi_p(3)\) affect a Paley-style sampling Gramian. Its exact four-class spectrum supplies deterministic sharp stability constants and worst-observed waveforms after omitting the constant sensing row, the simplest hardware/data-loss modification of the Paley matrix. The golden-ratio extremizer and the change from a three-dimensional worst space to rigid one-dimensional spaces are spectral structure, rather than a bare finite table. The result is intentionally bounded to this natural low-band regime; it does not establish uniform RIP or arbitrary-band estimates.

## Closest literature and limitations

The characteristic Gauss-sum step is classical and credited; no claim of a new Gauss-sum evaluation is made. Published general frame constructions, random spectral laws and conditional RIP bounds do not logically determine the displayed special four-band eigenvalues without further calculations. The consulted primary texts were inspected in their relevant theorem/proof sections, not asserted to have undergone complete line-by-line inspection. Residual priority risk concerns other specialized Paley submatrix and discrete harmonic sampling literature. Scientific verification is limited to self-review and a reproducible standalone numerical check; no independent expert audit was performed.

Self-review: passed. Independent audit: not yet performed.
