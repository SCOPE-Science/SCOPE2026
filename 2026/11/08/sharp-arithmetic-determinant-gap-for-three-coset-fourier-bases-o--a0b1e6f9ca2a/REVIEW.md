# Independent mathematical audit

## correctness

PASS

Splitting over [0,1) gives the three lifts 0,m,m+1 and a unitary Fourier-series reduction up to phase factors. Thus the squared determinant is the product of the three squared chords between 1, exp(2πimτ), exp(2πi(m+1)τ), with no normalization factor. The chord-square sum is 9 minus the squared node sum; AM–GM gives 27 only for an equilateral triple. Two successive nodes have ratio exp(2πiτ), so exactly τ=1/3 or 2/3 can give equality, and they do so exactly for m=1 mod 3. For the other residues I checked localization and the displacement via a centered phase error. Set δ=τ−1/3, M=m+1/2, c in Z+1/3 or Z−1/3 as appropriate, and w=Mδ−c; the phase errors near the equilateral offsets are w−δ/2 and w+δ/2. Analytic expansion of the log of the chord product gives log D=log 27−(4π²/3)(2w²+3δ²/2)+O((|w|+|δ|)³), with first-derivative remainder quadratic. The trial w=0 with |c|=1/3 gives defect O(m^−2). Compactness in the two free node phases followed by the positive definite Taylor bound places every maximizing pair of phases within O(m^−1) of equilateral. Reflection then puts τ near 1/3 with bounded c and |w|=O(m^−1). The loss for each such alias is at least 54π²c²/m²+O(m^−3); only the unique |c|=1/3 can match the trial, giving the coefficient 6π². Differentiating with respect to w along δ=(w+c)/M gives at the maximum 4w+3δ/M=O(m^−2), hence τ=1/3+c/M+O(m^−3). All maxima near 1/3 are therefore in one zero-free neighborhood within this alias, where the displayed log-sine second derivative is strictly negative; symmetry gives exactly one partner near 2/3. A generic shift has positive determinant for every allowed m, and each maximizer therefore has noncolliding frequencies and invertible fiber. The argument is uniform in the two residue classes and needs no numerical threshold.

## originality

PASS

The Fourier-fiber reduction, Vandermonde factorization and equilateral bound are standard, and some other equal-step three-coset determinant designs have been evaluated. The supported distinct claim is the arithmetic defect with exact leading coefficient, surviving alias and maximizing-shift expansion for the one-parameter constant-fiber {0,m,m+1} family. Neither the strongest same-day comparator nor the inspected general results supply it or a stronger statement that implies it. This judgment is limited to the inspected evidence.

## value

PASS

An integer-gap domain with only one free shift is a concrete multi-tile design problem in which exact orthogonality becomes unavailable. The result quantifies the unavoidable loss at its sharp scale and specifies the detuning and number of best designs when selecting realizable frequency cosets. A generic construction of some Riesz basis or an upper bound of 27 would not provide that information. The practical and mathematical claim is specific to determinant design, not to the best condition number or arbitrary spectra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
