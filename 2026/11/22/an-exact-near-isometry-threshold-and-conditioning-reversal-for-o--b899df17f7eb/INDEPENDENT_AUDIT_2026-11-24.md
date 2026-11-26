# Independent mathematical audit

## correctness

PASS

For the oriented cycle vector c, UU^T=P=I-cc^T/ell. For a sole collision of e,f with sign product tau, set x=U^T e_e and y=U^T e_f. The Gram perturbation is tau(xy^T+yx^T), with two eigenvalues tau<x,y> +/- ||x||||y|| and n-3 zeros; x,y are independent since c has at least three nonzero coordinates. Here <x,y>=-c_e c_f/ell and ||x||^2=1-c_e^2/ell. This gives all four stated spectra, including both sign relations. For subunit tolerance only the collision-free and mixed cycle–bridge cases pass, the latter including equality at sqrt(1-1/ell). At most n-2 occupied buckets forces a nontrivial sketch kernel on the incidence hyperplane. The falling-factorial counts then apply also for m<n and ell=n. Taking square roots of the Gram ratios gives the stated reversal of singular-value condition numbers. A separate exact-rational program checked 20 pair/sign cases on a triangle with two bridges; its print banner incorrectly says 22, but its explicit class counts are 3+3+12+2. The same program counted 288 subunit successes at tolerance 9/10 and 432 rank successes among the 1296 configurations on a triangle with one pendant edge; that count uses the proved collision classes, not an independent solver for all Gram spectra.

## originality

PASS

Best-of-knowledge pass for the exact whitened Gram spectra, the strictly subunit probability law, and the opposite ranking of two successful collision types. Not a priority claim for the sketch construction, circulation hyperplane, or exact rank survival.

## value

PASS

Exact preservation of metric information is an independent question once algebraic success is known. This gives the precise probability step and a structural example where minimizing squared-norm distortion chooses the worse-conditioned full-rank sketch. It separates metrics used for different numerical objectives on the same elementary graph and sketch, not just two definitions or a rank recount.

The dated certificate retains the supplied scientific assessment, sources and limitations.
