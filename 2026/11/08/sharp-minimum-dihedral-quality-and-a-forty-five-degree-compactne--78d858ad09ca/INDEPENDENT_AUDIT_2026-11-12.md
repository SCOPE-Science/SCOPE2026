# Independent mathematical audit

## correctness

PASS

PASS: for a,b,c>0 three dihedrals are right and the other three are arctan(a/b), arctan(c/b), arccos(ac/(sqrt(a²+b²)sqrt(b²+c²))). Reconstructed face-normal sign convention (interior angle = arccos(-n_i·n_j)), so δ is minimum of those three acute angles. With t<=δ, sin²t<=cos t; equality yields t=acos(1/φ) with a/b=c/b=sqrt(φ), and these values are attainable. For π/4<t<=θ*, sin α sin γ<=cos t yields individual bounds tan t<=a/b,c/b<=cos t/sqrt(sin²t-cos²t), attained with the opposite angle exactly t. For t<=π/4, one ratio diverges with the other angle equal t. This exactly proves open/closed/empty boundary cases, not a numerical optimization. Independent outward-face-normal and trigonometric computations on 2000 random triples plus equality and superlevel samples corroborated.

## originality

PASS

PASS, qualified: the 2026 same-object Korotov–Křížek primary text supplies dihedral formulas but establishes sharp bounds on their SUM, not the maximum of the MINIMUM or compactness transition. A separate same-family sharp minimum *solid* angle optimizer gives a different constant, so it does not imply this dihedral quality result. No dominating theorem was found among inspected sources, with specialist FEM priority risk explicit.

## value

PASS

PASS: smallest interior dihedral angle is a natural finite-element tetrahedral quality functional. This result gives its exact unique optimizer on all two-parameter path orthoschemes together with a complete sharp shape-feasibility profile; the previously unknown π/4 compactness threshold is an independently useful geometric boundary, not just a numerical golden-ratio evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
