# Scientific review: square-flat prism winding and excitation

## Correctness

**PASS.** The domain is every prism \(C_n\square K_2\) for \(n\ge3\), with all three-color initial states satisfying zero circulation on every elementary square. Flatness leaves exactly one integer homology generator. Every longitudinal closed walk making \(w\) turns has at least \(n|w|\) edges and integral \(wH_n\); the original general finite-graph activity theorem then gives exact eventual rates \(|H_n|/n\) for CCA and \(|H_n|/(3n)\) for GHM. The GHM factor follows from an explicit coboundary identity valid on all nine oriented color pairs. The \(9\times9\) transfer counts each labelled square-flat coloring precisely once, and its characteristic polynomial is verified by exact rational arithmetic. The shift-invariant \(3\times3\) Perron block and its quadratic equation give the nonzero variance \(5/4-19\sqrt{33}/132\). An elementary Fourier spectral-radius argument restricts peripheral phases to the three cube roots, giving the factor three in the local limit. Independent direct orbit evolution confirms exact rates for every square-flat initial coloring at \(n=3,4,5\), but these finite checks do not replace the proof.

## Originality

**PASS under the inspected evidence, with historical-priority risk.** The fundamental graph-wide activity/irrotationality formula is [1, Theorem 3] and is prior work. The existence of global winding beyond local face constraints is a known topological principle; [2] discusses related winding obstructions for proper graph colorings. The new proposed content is the explicit square-flat prism classification, exact \(9\)-state census and characteristic spectrum, exact nontrivial winding variance, and the conditional synchronization local-limit constant. Relevant earlier records on generalized theta-graph activity distributions, cactus-graph activity, initial primitive-three GHM orbits on prisms, and open ladder activity counts have materially different parameters or state-space restrictions and do not imply this conditional law without the new transfer calculation. Search and available-source inspection identified no covering statement. Hidden or differently indexed exact enumerations remain a residual risk.

## Value

**PASS.** In finite-network excitability, absence of elementary-square circulation is a natural local no-defect diagnostic. On a cylinder, it misses globally sustained activity: the asymptotic conditional fraction of quiet colorings goes to zero at the quantified rate \(3/\sqrt{2\pi\sigma^2n}\), while their typical activity is itself only order \(n^{-1/2}\). The exact population \(F_n\) and coefficient formula are reproducible at any size. Thus the theorem separates global oscillation from local defects and reveals a nontrivial crossover under a natural topological closure, rather than merely renaming a general cycle theorem.

## Literature and limitations

[1] J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (2016), Sections 2 and 4, especially Theorem 3. The general dynamics and cycle mean are theirs.

[2] D. Eppstein, *Reconfiguring 3-colorings* (2019), paragraphs on height propagation, winding, and four-cycle bases. This discusses proper-coloring reconfiguration, not the same excitable dynamics or census.

Limits: conditioning on square-flat colorings, no unconditional phase census, no transient times, and no independent scientific assessment. Historical priority beyond accessible literature is not guaranteed.

Self-review: passed. Independent audit: not yet performed.
