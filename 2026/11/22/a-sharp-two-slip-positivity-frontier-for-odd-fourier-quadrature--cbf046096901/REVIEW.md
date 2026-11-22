# Scientific review: two-slip positivity frontier

## Correctness — PASS

The coefficient-transport proof starts from the exact odd-grid Dirichlet cardinal basis and uses only invertibility of the distinct-node Fourier Vandermonde matrix. Symmetry uniquely identifies the two shifted-node weights. The remaining explicit weights are algebraic consequences of the two old-coordinate replacement identities; their signs follow from strict convexity of cosecant on \((0,\pi)\). Each term in the threshold equation is strictly increasing in the displacement, proving one crossing and excluding second sign changes. Monotonicity with grid size follows from the strictly decreasing function \(t\cot t\) on \((0,\pi)\), and the expansion is derived at its simple limiting root. A second, independent cardinal-vector argument establishes the noise variance identity. The standalone high-precision verifier agrees with independent Fourier-system solves for the tested sizes and displacements. Mathematical validity does not rely on those finite tests.

## Originality — PASS, with historical risk

Austin–Trefethen (2016) establish smooth-function convergence on arbitrary perturbed periodic grids, not an explicit two-node positivity boundary. Yu–Townsend (2022), Section 4, construct negative quadrature weights for alternating disturbance of many grid nodes even at arbitrarily small fixed jitter; that is the opposite support-size regime. The present exact first-failure indices, increasing root \(\alpha_n\), and limiting constant for exactly two outward adjacent slips do not follow from either claim. Van den Bos–Sanderse (2021) describe general polynomial-moment node replacement; their work does not exhibit the Fourier trigonometric identity or this all-odd-grid positivity frontier. A known three-node perturbation case includes the boundary \(\alpha_3=1/4\); the novel quantified theorem is explicitly restricted to odd \(n\ge5\). No exhaustive literature uniqueness claim is made; an older equivalent interpolation formula is a genuine remaining priority risk.

## Value — PASS

Localized timestamp failure differs structurally from simultaneous correlated jitter. The theorem identifies the first loss of nonnegative integration weights under exactly two adjacent, symmetrically outward displaced nodes, for all odd grid sizes, and proves the tolerance increases from beyond \(1/4\) toward \((\sqrt3-1)/2\). This provides a sharp benchmark for fault-tolerant periodic integration, including exact noise amplification, rather than an arbitrary finite table. The claim does not assert actual floating-point speedup, broader arbitrary-two-node tolerance, or nonsmooth-function convergence.

## Source and scope limitations

The relevant primary text inspected comprises Austin–Trefethen (arXiv:1612.04018), Yu–Townsend (arXiv:2202.04722, particularly Section 4), and van den Bos–Sanderse (2021, especially Sections 2 and 4). Comparisons are at the level of mathematical implications, not title similarity. High-precision numerical checks are supplementary and independent scholarly validation is not performed.

Self-review: passed. Independent audit: not yet performed.
