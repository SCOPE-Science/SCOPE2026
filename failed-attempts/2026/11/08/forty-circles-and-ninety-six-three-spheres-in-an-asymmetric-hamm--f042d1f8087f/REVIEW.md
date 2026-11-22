# Independent mathematical audit

## correctness

PASS

The fixed 36-point alphabet product [3]×[3]×[4] has Hamming distances 0,1,2,3. At 0≤r<1 it has 36 components. The radius-one clique complex is a union of 12,12,9 coordinate-line simplices intersecting at most at vertices, yielding the connected 36-vertex 75-edge graph and β1=40. At radius 2 the allowed faces are precisely independent sets of K3×K3×K4 because forbidden pairs differ in all three coordinates. An independent implementation from the metric (not the repository verifier) enumerated exactly 30,991 faces with f-vector (36,414,2028,4869,6804,6816,5184,3042,1324,396,72,6), constructed 15,447 vertex-toggle pairs, found one critical 0-cell and 96 critical dimension-three cells, and topologically sorted all 178,668 Morse-oriented Hasse incidences without a cycle. Separately read actual morse_certificate.json blob 409d734a3ed9e2f1db2f3f09740145ba881fa889 and verified each of its 30,991 face masks is legal, every lower face is present, pair list matches the vertex-toggle recipe, all 178,668 arc directions respect its complete 30,991-face order; no missing faces or wrongly ordered arcs. Hence the Forman discrete-Morse theorem proves the integral homotopy type ∨^96 S^3 (not just rational Betti numbers). From r≥3 the full 35-simplex is contractible. Since nontrivial reduced homology lives in degrees 0,1,3 on mutually disjoint radius intervals, the integral barcode has respectively 35 [0,1), 40 [1,2), 96 [2,3), no torsion. This is an exhaustive finite theorem for one fixed metric space, not an infinite parameter extrapolation.

## originality

FAIL

Direct exact coverage by an earlier complete result. SCOPE-Science/SCOPE2026/2026/10/25/a-96-three-sphere-stage-in-the-mixed-ternary-quaternary-hamming--98bfe9517ebf/RESULT.md (import commit dated 2026-10-25T18:08:03Z) establishes the identical (3,3,4) inclusive Hamming Rips homotopy stages, the exact same integral barcode, and Ind(K3×K3×K4)≃∨^96 S^3. Current source import is 2026-11-08T17:16:16Z. The earlier matching uses the augmented empty face (15,448 pairs); omitting empty converts it into exactly the 15,447 pairs and critical 0-cell/96 critical three-cells in the assigned work. The new second collapse/chain certificate adds verification but not a novel theorem or separately motivated invariant. This is full statement-by-statement and proof-level coverage, not mere topic similarity, and overrides unsuccessful searches or conjectural 2023 background.

## value

FAIL

The (3,3,4) Hamming space and integral homotopy/persistence are natural and the computation is mathematically substantive, but the earlier October 25 result already gives the same complete invariant with an exhaustive Morse certificate. The second independent certificate is useful reproducibility but does not solve a new classification problem, isolate a previously unknown natural invariant, or establish a new proof-method theorem; the duplicated value is already in the literature. Under the shared bar a repeat of an exact known finite classification is not a distinct valuable new mathematical contribution. Therefore the assigned original is not accepted or repaired by adding verification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
