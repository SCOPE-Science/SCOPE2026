# Independent mathematical audit

## correctness

PASS

The normalized inverse Fourier transforms are absolutely meaningful as improper integrals because sin(p_j)/E(p)=O(1/|p|) and (cos p1-cos p2)/E(p)=O(1) near 0. With square-lattice potential kernel a(x), formal Green G=C-a/2 cancels in the differences: R_j=(a(x-e_j)-a(x+e_j))/(4i), Q=-(a(x+e1)+a(x-e1)-a(x+e2)-a(x-e2))/4. Applying the published a(x)=2/pi log r + const -cos(4θ)/(6pi r²)+O(r^-4) gives R_j=i x_j/(pi r²)+O(r^-3) and Q=(x1²-x2²)/(pi r^4)+O(r^-4), uniformly in lattice direction. The published correction contributes only error order; the bundled numerical checker tests leading logarithmic finite differences and cannot alone prove asymptotics.

## originality

FAIL

The asserted spatial asymptotics are a direct routine consequence of two existing exact source statements: Hiroshima–Muminov–Kuljanov identify the very same normalized threshold momentum functions, and Friedrich–Levine state the complete square-lattice potential-kernel expansion with the leading logarithm and anisotropic O(r^-2) term. Fourier shift identities and one elementary Taylor differentiation immediately force both coefficients and orders. This is prior implication coverage even though no one earlier source phrases it as dipole/quadrupole tails.

## value

PASS

Spatial localization profiles of the threshold resonance/eigenfunction are motivated mathematical information, distinguishing dipole r^-1 from quadrupole r^-2 decay and nodal directions. The fact may aid finite-volume and defect interactions despite having a short derivation; this value does not cure the lack of originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
