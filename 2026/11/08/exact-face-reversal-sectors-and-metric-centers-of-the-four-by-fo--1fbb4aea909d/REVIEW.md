# Scientific review

## Correctness

**PASS.** The configuration space and face moves are completely defined. A 16-word row-transfer enumeration and an independent 32-edge constraint-propagation enumeration both generate exactly 2970 orientations, 8768 face-transition edges, and the same 69 connected components. Each implementation performs all-source shortest-path computations and independently reports the sector diameters and eccentricity distributions. A direct twelve-face path and a height-potential argument establish the extremal lower bound without relying on the graph search for sharpness. All computations are finite and exhaust all labelled assignments satisfying the stated constraints.

## Originality

**PASS (qualified).** Lieb's ice configurations and the OEIS count of 2970 are prior knowledge, as are the flux/homology and general face-flip frameworks of Felsner and Zhang–Qian. The exact 4-by-4 single-directed-plaquette graph, including its labelled components, sector radii, diameters, two central centers, and all-pairs central distance histogram, is not implied by those published statements. The related Borodin–Bufetov process uses different elementary updates. Several primary sources were read substantively, but unindexed historical computations remain a real priority risk. An absence of search hits is not treated as proof of uniqueness.

## Value

**PASS.** Small periodic ice is a canonical constrained configuration space, and elementary face reversals are its geometrically smallest local rearrangements. Exact sector connectivity alone does not determine reconfiguration cost; the sharp diameter difference between flux classes and the two exceptional central states provide natural, reusable benchmarks for local dynamics and height-based path methods. The nontriviality is visible in the coexistence of isolated states, differently sized mobile sectors, and two different mobile diameters. The claim is finite but solves a complete naturally defined problem, not an arbitrary sample.

## Evidence and limits

Reproducibility uses `verify_transfer.py` and `verify_vertex_constraints.cpp`; source comparisons include Lieb (1967), Felsner (2004), Borodin–Bufetov (2015), Zhang–Qian (2020), and OEIS A054759. Only this exact labelled four-by-four model is covered. Dates refer to the verified original Lieb source, not to a later database revision. The numerical enumeration and self-review do not constitute independent publication certification.

Self-review: passed. Independent audit: not yet performed.
