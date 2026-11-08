# Mathematical review

## Correctness: PASS

The hypotheses are exactly a path on \(2m\) vertices, \(m\ge2\), total weight at most \(B>0\), and a single positive upper capacity \(u>0\) on edge \(m\). A centered monotone Fiedler test vector with unit differences off the middle edge gives a global Rayleigh upper bound valid even for asymmetric and disconnected competitors. The telescoping eigenvector flux gives explicit positive weights that exhaust the budget and attain this bound. The Jacobi oscillation theorem places the constructed eigenvalue in the second position. Equality in the global Rayleigh bound then pins down the same eigenvector and each individual edge weight, proving uniqueness even against asymmetric competitors. The rational identities, capacity boundary, characteristic-polynomial Sturm signs, and a six-vertex exact example were replayed by the included standalone verifier, `VERIFY_OK 9911`. Finite tests support the proof; they are not used to extrapolate across all \(m\) and all positive real parameters.

## Originality: PASS on the checked literature, with a stated access risk

Fiedler (1990), Wan and collaborators (2008), and an available earlier mathematical record cover the *uncapped* path optimum. This is explicitly excluded from the newness claim. Shakeri and collaborators (2015) study a different interlayer connectivity design with a resource-dependent threshold, not a hard cap on one independently adjustable edge of a path. Shafi, Arcak and El Ghaoui (2010) give general semidefinite eigenvalue constraint formulations, but no inspected cap-specific closed form. An earlier edge-sensitivity article by Kirkland and Neumann (2004) varied one edge while holding others fixed; its abstract was accessible but the entire article was not. The remaining priority risk is that inaccessible or unindexed literature could contain a simultaneous cap-and-budget solution. Existing unrestricted-budget solutions and fixed-edge sensitivity do not by themselves imply the specific positive-cap transition, allocation, asymptotic and unconditional uniqueness established here.

## Mathematical value: PASS

A single congested bridge in a path is a canonical bottleneck of network diffusion and consensus. Rather than merely solving a small instance or rephrasing an SDP, the theorem locates an exact parameter phase boundary for every even path order, gives a one-root exact allocation formula in the binding regime, proves unrestricted global uniqueness, and determines the sharp vanishing-cap decay \(\lambda_*(u)\sim 2u/m\). It distinguishes physical edge-capacity scarcity from pricing and from generalized edge-resistance costs. This supports systematic conductance design for bottleneck-limited chain networks. The theorem does not claim other graph classes or multiple bottlenecks.

## Closest literature and limits

- Fiedler, *Absolute algebraic connectivity of trees* (1990), DOI `10.1080/03081089008817967`: total-budget tree optimum; not a capped central edge.
- Wan et al., *On the Structure of Graph Edge Designs that Optimize the Algebraic Connectivity* (2008), DOI `10.1109/CDC.2008.4738734`: unconstrained tree-edge allocation and eigenvector structure, without the independent hard cap.
- Shakeri et al., *Maximizing Algebraic Connectivity in Interconnected Networks* (2015), arXiv `1510.06785`: threshold in one-to-one interlayer links, a different feasible set.
- Shafi, Arcak and El Ghaoui (2010), *Designing Node and Edge Weights of a Graph to Meet Laplacian Eigenvalue Constraints*: general LMI framework.
- Kirkland and Neumann (2004), *On algebraic connectivity as a function of an edge weight*, DOI `10.1080/0308108031000119663`: relevant but full text unavailable, leaving a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
