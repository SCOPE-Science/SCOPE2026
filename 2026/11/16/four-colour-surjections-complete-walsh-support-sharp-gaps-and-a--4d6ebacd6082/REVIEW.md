# Independent mathematical audit

## correctness

PASS

PASS. Starting from the actual frozen RESULT.md, translation of all four colour symbols by t∈V4 gives W_n(b)=0 for Σb_i≠0. Inclusion–exclusion over missing symbols supplies signed terms: full alphabet only b=0, three-letter sets contribute −4(−1)^k3^z, four singleton terms −4, and two-letter terms 2^(n+1) iff all nonzero coordinate frequencies are the same, yielding the complete displayed signed formula (and zero case). For t=1, balanced requires k even, and 2^(n−1)−1−3^z cannot vanish mod8 when n≥4; for t≥2, extra cancellations require z=0 and odd n. Character orthogonality counts exactly (3^n−3)/4 such exceptional b, giving full ranks. Every nonzero balanced coefficient is multiple of 8 (even n) or 16 (odd n); explicit frequencies with two a, two c and optionally one zero attain each gap, showing exact inverse norm. Translation-averaging any projection onto the invariant Fourier range gives the canonical multiplier-support projection with no larger l1/l∞ norm; when n even its kernel is four-translation averaging of norm 1, while for odd n≥5 the witness x=(a,c,0,..) produces negative kernel p(x)=−(3^(n−2)+5)/4^(n+1), forcing endpoint norm >1. The provided verify.py explicitly evaluates exact Walsh frequency arrays n=4..9, and independent reimplementation checked every coefficient for n=4..7, with ranks 64,196,1024,3550 and gaps 8,16,8,16. The infinite theorem follows from inclusion–exclusion, not extrapolation.

## originality

PASS

Best-of-knowledge original residual scientific increment after explicitly excluding known prior coverage; exact historical priority is not certified. Material compared at the statement and implication level; finite or generic overlaps are acknowledged.

## value

PASS

PASS. Full all-coordinate character spectra of an onto-word language yield a natural all-length parity transition between full balanced support and exceptional resonance, with sharp inverse gaps and a nontrivial contractivity dichotomy for the optimal range projection. This character-resolved inverse/functional-analysis fact is not a routine Stirling-number surjection count or a simple renaming of the degree-one covariance spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
