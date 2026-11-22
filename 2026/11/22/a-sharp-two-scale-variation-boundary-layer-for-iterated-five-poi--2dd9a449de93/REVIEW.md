# Self-review

## Correctness — PASS

The two-input bounded-variation norm reduces exactly to the \(\ell^1\) norm of each finite convolution power, with a unit step attaining equality. Explicit Fourier analysis isolates two extremal points of the symbol at the critical parameter, with local quartic and Gaussian limits. Fourth-derivative integration-by-parts bounds establish summable spatial tails for each part. The intermediate cutoff \(r^{3/8}\) separates the two distinct spatial widths, so their absolute masses add, uniformly for bounded moving parameters. Fixed-parameter corollaries use the single surviving Fourier maximum. The accompanying rational/Fourier finite checks were executed; they are not a substitute for the infinite-scale argument.

## Originality — PASS (qualified)

The most important archival precedent is Diaconis–Saloff-Coste, arXiv:1205.6490, Proposition 2.4 and Example 2.2: it treats this exact Fourier symbol and identifies both critical peaks. This prior coverage is expressly acknowledged. Its fixed-parameter pointwise local-limit results do not themselves determine an \(\ell^1\) norm for parameters changing by order \(1/r\); summing their pointwise error across the wider Gaussian scale is not justified by those statements. Randles–Saloff-Coste, arXiv:1212.4700, is also a foundational local-limit source. Searches of indexed mathematical findings, relevant historical claims and primary literature did not locate the moving-parameter sharp BV law. The residual risk is an equivalent asymptotic hidden in older signed-convolution stability literature or as an unstated consequence of a stronger theorem not inspected in full.

## Value — PASS

The precise parameter \(1/8\) is the spectral stability edge for a canonical five-point, quadratic-reproducing fourth-order smoother. The norm distinguishes perturbation stability from pointwise convergence. The critical \(r^{-1}\) width and \(e^{16\lambda}\) crossover quantify a singular, previously under-accounted-for Gaussian contribution to a global stability metric, a natural question in long-iterate filtering and high-order difference schemes.

## Limitations

The proof is confined to real bilateral sequences and the displayed five-tap family. It does not treat finite-boundary versions or prove any independent external verification of novelty.

Self-review: passed. Independent audit: not yet performed.
