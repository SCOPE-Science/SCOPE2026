# Scientific review: reflection-fixed cycle-power independence complexes

## Correctness

**PASS.** The asserted domain is \(n\ge2k+2\), \(k\ge1\), with a subgroup containing a reflection; this avoids conflating a geometric fixed-point locus with a quotient complex. The proof first takes rotation-orbit barycenters, then reflection-orbit barycenters. It explicitly proves (i) the empty case \(t\le k\), (ii) admissibility inequalities for both reflection-axis types, and (iii) that the surviving conflict edges are exactly indexed distances at most \(k\). The chordal conclusion and exact wedge recursion follow from the established simplicial-vertex splitting, not from finite experimentation. The standalone verifier independently checked 3,340 cases and 452,220 actual face subsets. Its evidence is supportive, not an infinite proof.

## Originality

**PASS relative to examined evidence.** The primary nonequivariant cycle-power reference is Adamaszek (arXiv:1106.6250, 2011), which studies cycle-power independence homotopy recurrences but not reflection subgroup-fixed PL models. The chordal wedge/splitting machinery is known and explicitly credited (Adamaszek arXiv:1508.02426, 2015, and Kawamura, 2010). Closest indexed results treat dihedral fixed spaces of higher *consecutive-vertex* independence complexes of cycles, the three-cut complexes of cycle powers, ordinary matching complexes of wheels, and forest independence complexes. The objects and statements differ: their results do not imply the complete cycle-power reflection-index formulas or the mixed-dimensional fixed example. The general vertex-orbit-to-fixed-face correspondence is not separately claimed as novel.

## Value

**PASS.** The cyclic distance parameter and all reflection-containing subgroups are intrinsic, not arbitrary finite slices. The new interval-graph compression implies universal torsion-freeness and permits the complete *integral* sphere-multiplicity calculation for every parameter. The edge-axis reflection of the third power of the 22-cycle produces a mixed-dimensional \(S^0\vee S^1\) fixed space. This is a qualitative phenomenon not obtainable from the ordinary ambient homotopy result alone. The result requires no conjecture about purely rotational fixed spaces.

## Closest literature and residual limitations

Adamaszek's 2011 paper, Theorem 1.1 and Remark 6.6, distinguishes its ordinary cycle-power recurrence from its unresolved small initial cases; the present result invokes neither a blanket sphere-wedge theorem for ordinary cycle powers nor any equivariant conclusion from that paper. His 2015 chordal-graph work states the previously known chordal wedge theorem and develops strong collapses. Possible equivalent formulations in unindexed work on reflection-folded circulants or interval graphs remain a publication-priority risk. The source comparison does not constitute independent certification.

Self-review: passed. Independent audit: not yet performed.
