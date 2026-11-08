# Self-review

**Correctness — PASS.** The theorem uses the exact Radau IIA rational function, a four-class quotient with two leaf zero-sum eigenspaces, and all seven actual entry orbits. For the four surviving integer branch counts, 28 exact Sturm root-count certificates and positive denominators establish all-step positivity. For every higher branch count, the displayed shifted polynomial is strictly negative at step \(h=10\); its denominator is strictly positive. Taylor and Laplacian spectral arguments establish small- and large-step positivity. A separate exact full-matrix reconstruction tests all seven orbit types at 15 rational graph/step configurations. No finite sample is used as the proof of the infinite statement.

**Originality — PASS on the inspected evidence.** Horváth's full 2005 article explicitly treats two-stage Radau IIA and diffusion examples; its general step-threshold and special-cone results do not imply this symmetric double-star all-step theorem. Bonaventura and Della Rocca's 2015 full preprint studies another L-stable method (TR-BDF2). Indexed and accessible graph-family results for paths/cycles and complete multipartite graphs do not subsume proper double stars. The sharp \(m=5\) boundary and universal \(h=10\) witness were not found in inspected sources. Equivalent unindexed work remains a publication-priority risk; the older Horváth 1998 article was inspected through abstract only.

**Value — PASS.** A natural two-hub, unit-weight family reveals a qualitative topology/branching threshold for positivity of a standard third-order stiff solver. For high branching, the endpoint fails positivity at an intermediate time step despite being positive at both small and sufficiently large time steps. This exactly classifies the whole family without requiring a general theorem for other networks.

**Limitations.** The result concerns completed endpoints on equal-armed double stars, not intermediate stages, unequal arms, other integration schemes or an explicit equation for every failure-window boundary.

Self-review: passed. Independent audit: not yet performed.
