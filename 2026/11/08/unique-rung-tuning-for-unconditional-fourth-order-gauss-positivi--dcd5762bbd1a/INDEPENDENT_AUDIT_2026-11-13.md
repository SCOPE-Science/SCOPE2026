# Independent mathematical audit

## correctness

PASS

Read the full frozen RESULT.md. The rail-symmetric/-antisymmetric splitting gives P and M=P+2diag(b_i/a), with G=M^{-1}; the exact graph Laplacian pseudoinverse has off-diagonal entries (P^+_ij±G_ij)/2. F(hL)=I-12L^+/h+O(h^-2) off the diagonal as h→∞, so universal positivity forces G11,G33>=5/9, G22>=2/9 and G12,G23<=1/9. The identities (1+2r1)G11-G12=1 and (1+2r1)G12=G22 force r1=1/2; reflection gives r3=1/2; the middle row forces r2=7/4. I independently recomputed G, both eigenprojector blocks and all 15 offdiagonal rational entries with exact SymPy: six complete numerator-orbit polynomials have strictly positive coefficients over a positive denominator; F(x)=((x-3)^2+3)/(x²+6x+12)>0 establishes positive diagonals. The unweighted h=8 witness is negative. This is an infinite h proof using algebra, not sample positivity; h=0 is I.

## originality

PASS

Best-of-knowledge distinct claim after actual primary-source and published-record comparisons. The published P4 and method-wide statements neither substitute the 3-rung Green inverse rigidity nor provide a graph-specific six-orbit positivity certificate. Inaccessible older Padé literature remains a genuine priority risk.

## value

PASS

The exact conductance design on the first nontrivial two-rail three-rung heat discretization is a naturally motivated, sharp iff weight-rigidity criterion for unconditional positivity of a non-SSP high-order step. Its unique nonuniform tuning is structurally informative and experimentally actionable, not a mere checking exercise; wider unequal-rail ladders are not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
