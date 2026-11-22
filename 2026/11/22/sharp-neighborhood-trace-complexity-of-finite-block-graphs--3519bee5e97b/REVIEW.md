# Self-review

## Correctness — PASS

The quantified domain is **every finite nonempty simple block graph**, **every** marked vertex set of size \(m\), and every open-neighborhood center, including marked centers. For \(m\ge4\), the proof partitions multi-element traces into marked centers, centers supported in one marked component, and cross-component centers; the vertex–clique incidence forest gives the \(\sum b_i\) and \(c-1\) bounds. The exact defect identity \(u+b+1=2t-(\ell+\delta)\) and its only two exceptional connected components (singletons and triangles) yield the universal \(3m-2\) upper bound. The path of triangular blocks with pendants and an isolate attains equality for every \(m\ge4\); separate constructions attain \(2^m\) for \(0\le m\le3\). The standalone standard-library checker independently exhausts all labelled block graphs through six vertices and all their parameter subsets, checks explicit witnesses through 18 markers, and checks random larger block graphs. It does not substitute for the incidence-forest proof.

## Originality — PASS within inspected evidence

The closest full-text primary source, Dreier et al. (2026), proves \(|A|^{1+o(1)}\) neighborhood complexity for monadically dependent classes and supplies no exact coefficient or block-graph bound. The earlier full-text graph-VC paper of Benediktsson et al. (2020) treats Johnson/Hamming graphs. Chakraborty et al. (2018) use neighborhoods for identifying codes in block graphs, not the maximum number of distinct trace types on an arbitrary parameter set. Publicly indexed results on block-graph neighborhood-complex homotopy, convexity, color refinement, and general rank-width-one traces do not state or imply this all-size exact block-graph shatter function. In particular, a previously recorded rank-width-one result treats only the four-marker maximum (12 for the larger class), and a cograph bound concerns a different restricted graph class. A potential equivalent formulation under an alternative terminology or in uninspected full text remains a priority risk; a search failure is not a proof of novelty.

## Value — PASS

The new exact \(3m-2\) coefficient and exceptional three-marker threshold refine generic almost-linear neighborhood-complexity results by resolving an all-parameter structural extremum, not just the exponent. The contrast between adjacency VC dimension three and VC density one matters when bounding the number of adjacency types over named parameter sets in finite-model arguments; every coefficient and the additive constant are sharp. The path-of-triangles witness also exhibits which marked-component features attain the maximum.

## Closest literature and limitations

The most relevant prior full texts are Dreier et al. (2026), Benediktsson–Macpherson–Adler (2020), and Chakraborty–Foucaud–Parreau–Wagler (2018). Further indexed block-graph and rank-width results were compared at the level actually accessible. The proof does not cover closed-neighborhood systems or general chordal graphs. Earlier historical records beyond accessible material are not claimed checked, nor is historical uniqueness certified. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
