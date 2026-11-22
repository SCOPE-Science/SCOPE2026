# Independent mathematical audit

## correctness

PASS

PASS: Checked baseline compactness, ||S_m^k||=(k!)^-1/m and singular values n^-1/m. Taylor coefficient matching uniquely forces gamma_(mj)=a^j Gamma(mj)^(1/m)/j!, zero otherwise; Stirling gives (m|a|)^j j^{-(m+1)/(2m)}, squared endpoint j^{-1-1/m} summable, strict overflow divergent. Thus boundedness iff |a|<=1/m. Since gamma_1=0 for m>=2, F^2=0. Resolvent rank-one identity reduces nonzero eigenvalue equation to 1=alpha(e^{a/lambda^m}-1). For alpha=0 or -1 there are none; otherwise logarithm branches L+2pi ik give m distinct roots per admissible k, with simple scalar zeros and algebraic multiplicity one. Counting vertical lattice sites inside a disk of radius |a|r^-m gives m|a|/pi r^-m+O(1). Rank-one approximation inequalities squeeze s_n(A) between shifted singular values of S_m, proving s_n(A)~n^-1/m, ratio and 2m angular rays. Independently checked coefficient ratios and integer lattice counts for m=2,3,5, several interior/endpoint a, three complex/real couplings. These numerics do not prove the infinitely many poles or endpoint boundedness.

## originality

PASS

PASS qualified: Tcaciuc 2018/2019 describes an m=1 factorial-shift degree-one exponential example and exceptional coupling; it does not imply the m>=2 prescribed bounded-functional realization at the sharp Hilbert-space threshold or the weak-Schatten spectral-density formula. Hansmann (2026) allows selection of suitable operators to realize spectral configurations, but the accessible summary does not fix the prescribed factorial background or quantify this exact endpoint. Fixed-background spectral realization is stronger than merely being some special case of unconstrained existence; full Hansmann text was not accessible this run and is recorded as a residual risk.

## value

PASS

PASS: For compact quasinilpotent operators whose baseline nonzero spectrum is empty, creation of spectrally dense 2m-ray stars by one nilpotent rank-one perturbation with the *same counting order as singular values* is quantitatively meaningful. The sharp attained boundedness boundary and universal 1/pi ratio constrain possible realization, while exceptional coupling collapses the spectrum without changing the singular scale. This is beyond a routine degree-one parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
