# Scientific review

## Correctness
**PASS.** For each specified phase alphabet, the three independent phase symmetries give a unique representative with three coefficients equal to one. Thus the remaining search contains exactly \(q^5\) arrays. The two fourth-moment identities, exact cyclotomic norm calculations, and complete deterministic loop are all given explicitly. Reproduced output independently compares autocorrelation and convolution moments for all 12,200 representatives and exactly matches every optimizer tuple in the catalog. This is a finite exhaustive proof; it does not infer infinite claims from a sample. Discrete Fourier sampling at orders at least five follows from no-aliasing of \(P^2\).

## Originality
**PASS, with bibliographic risk.** The two focal 2021 array papers construct complementary pairs/sets, whereas the present result optimizes the whole aperiodic sidelobe sum for a **single** punctured planar aperture. The 2021 correlation-optimization study provides iterative methods, not these exact finite tables. Existing published full-square and eight-vertex cube fourth-moment statements do not imply this claim: their additive geometry and coefficient domains differ. Their respective original arguments were compared, not merely their titles. The possibility of an unindexed prior eight-site array catalog remains.

## Mathematical value
**PASS.** The centered-hole \(3\times3\) support is a natural symmetric sparse Fourier aperture with eight active sites. Exact integrated-sidelobe optima across five practical small phase alphabets provide hardware-resolution benchmarks and a complete count of optimal designs. A nontrivial irrational fifth-root optimum, nonmonotone behavior at ternary phases, and two rigid sixth-root optimizers distinguish the result from a single ad hoc numerical optimum. No result for unrestricted phases is claimed.

## Closest literature and limitations
Primary sources are the two-dimensional complementary array constructions of Pai--Chen and Zhang--Fan--Mesnager (2021), as well as Raei and colleagues' 2021 phase-only correlation optimization work. Published complete Fourier-aperture results treat the full nine-site square and a three-dimensional eight-site cube, not the punctured planar square. A specialist historical equivalent remains possible. All completeness assertions concern \(q=2,3,4,5,6\) only; there has been no independent review.

Self-review: passed. Independent audit: not yet performed.
