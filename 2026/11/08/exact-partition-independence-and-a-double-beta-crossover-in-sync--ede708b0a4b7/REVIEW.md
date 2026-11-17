# Independent mathematical audit

## correctness

PASS

Positive reset probability makes every one-step state-to-state transition positive, ensuring a unique invariant law. Conditional next-part A uses only old B and independent fresh randomness, and conditional next-part B only old A; a product law across parts is preserved and uniqueness makes the invariant law a product. On a complete biclique, the A fraction two-step law is the composition of binomial sampling via r(u)=epsilon/2+(1-epsilon)u; total variance gives the exact two-step drift and variance in the source. Scaling by h=1/a+1/b gives limiting Wright–Fisher drift λ(1-2u) and diffusion u(1-u)/2. A uniform third-moment bound allows passing polynomial test functions to the stationary generator; the resulting moments uniquely determine Beta(2λ,2λ). Independent partwise limits then yield product Beta. Pair-spin covariance equations, including the 1/a,1/b finite self-copy terms, settle zero- and high-noise endpoints by second moments. A separate exact-rational K2,2 check preserved cross-part product structure under 35 full synchronous updates; the source exact-rational stationary checker (inspected) verifies K_ab cases more broadly. The finite check is not proof of the limiting law.

## originality

PASS

The primary Benjamini–Helman Tov–Zhukovskii paper studies the same discrete-time simultaneous model but local temporal repetition statistics, not the invariant two-part factorization and independent-Beta crossover. Earlier Resultary exact Beta/Gaussian theorems use continuous-time asynchronous rate-one copying: there the two parts synchronize to a common Beta variable, an opposite joint law. The update convention is a decisive mathematical distinction, not a title difference.

## value

PASS

The precise update protocol creates an unusual exact independence of the entire same-time vertex-part states despite continual cross-part copying. A three-regime joint stationary phase classification at the natural inverse-population noise scale, with two independent nondegenerate Beta limits and no aspect-ratio restriction, differs qualitatively from the known asynchronous common-Beta phenomenon and is mathematically motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
