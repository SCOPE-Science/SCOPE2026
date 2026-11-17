# Independent mathematical audit

## correctness

PASS

For rho>1 and kappa=1/(rho-1), N_j=ceil(2^{j/(2kappa)})+j is strictly increasing; exponential inversion yields h(k)=2kappa log2(k+1)+O_kappa(1). At block endpoints n=2k+h, #2=k+h, hence B_n≈2^{n/2}(n+2)^kappa; bounded gap between endpoints extends uniformly. For finite p, Hölder gives A_{n+1}≥|lambda|^p A_n/b_n^{p-1}; radial f(v)=lambda^n/B_n is an exact eigenfunction and its norm series is ∑|lambda|^{pn}/B_n^{p-1}. At |lambda|=r_p its terms compare to n^{-kappa(p-1)}, converging exactly p>rho. At p∞ radial eigenfunction bounded through |lambda|=sqrt2 and a local descendant-growth upper bound excludes larger. Disjoint descendant supports give exact ||S_p^j||=(sup_n B_{n+j}/B_n)^{1-1/p}; Gelfand gives full disk, interior infinite eigenspace multiplicity gives Fredholm essential closed disk. Independently checked endpoint population bookkeeping for rho=1.5,2,4 at 1,000 blocks; finite tests are illustrations, not the infinite proof.

## originality

PASS

Best-of-knowledge contribution is a *single unweighted* (1,2)-branching tree whose entire ℓp family has a prescribed strict peripheral eigenvalue transition at arbitrary rho>1, while full and Fredholm spectra remain disks. Nearest ℓ2 radius-threshold and weighted-tree operator papers do not imply the variable-p critical boundary comparison.

## value

PASS

Controlling whether spectral-circle points are eigenvalues as a function of the ambient Banach exponent is a motivated operator-theoretic boundary problem. A single unweighted binary/unary tree with *arbitrary* critical p and complete point/full/Fredholm spectra is a genuine structural phenomenon, not a finite numerical curiosity or a renaming of weighted shifts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
