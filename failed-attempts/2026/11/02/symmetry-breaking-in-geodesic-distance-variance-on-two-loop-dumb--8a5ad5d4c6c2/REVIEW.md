# Independent mathematical audit

## correctness

PASS

Arclength sampling gives independent component memberships and conditional uniform coordinates. Loop-to-attachment and within-loop distances are both uniform on [0,u/2]; cross-loop distances add the two independent radial coordinates and t; loop-to-bridge distances add a radial coordinate and a uniform bridge coordinate; the within-bridge distance has the triangular density. Weighting by length products (twice for different components) and integrating independently reproduces the two moment polynomials after s-normalization. For p=ab/s² in (0,1/4], the scaled variance derivative is [Q(r)+(1+32r−44r²)p]/[24(1+r)^4], with endpoint numerators proportional to Q(r) and (2r+1)C(r). C is strictly increasing on the positive axis; Q has exactly one positive zero by one Descartes sign change and existence from its endpoint signs. Exact rational substitutions bracket the two roots in the stated increasing order. The affine derivative is strictly negative inside the interval for r≤α, changes from negative to positive once for α<r<β, and is positive on the positive domain for r≥β. This verifies equality cases, uniqueness up to exchange, and the unattained infimum from p↓0; the positive length assumption is essential. The mean slope has sign r−1/4 and the exact witness at r=1/10 is p*=1079/4700 with improvement 384/17203175. Independent replay: python3 /tmp/opencode/nov02-independent-checks.py 5 (SymPy integration, differentiation, and exact identities). Numerical roots merely corroborate; the frozen attached script was inspected, not executed.

## originality

FAIL

Mathematically covered as a routine corollary, not shown to have been stated verbatim: earlier Resultary ea37b5fa3169 gives exact general first and second moments for this identical two-loop metric family and sampling, and the full pair-distance density. Its equations (1) and (4), not just an algorithm or moment formula at the resonance, are exactly the reviewed M and N after scaling. Centering and minimizing their one-variable quadratic by its two endpoint derivatives immediately give the claimed phase law. The asserted novelty as a separate result misses that directly available stronger calculation.

## value

PASS

As a mathematical corollary, identifying the full range of asymmetry, its contrast with minimizing the mean, and the sharp nonattainment boundary gives a useful geometric interpretation of the quadratic objective. This is more informative to a reader than evaluating one length allocation. It does not rescue the originality failure or justify presenting the earlier moment calculation as a separate contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
