# Scientific review

## Correctness — PASS
Every shattered support must fit inside one radius-one ball. The proof classifies all allowable three-point configurations, provides separate witnesses for their eight traces, verifies empty-trace obstructions at small parameters, and excludes all four-point supports by a center-forcing argument. The single- and double-support counts use direct Hamming-distance enumeration. A separate program checks the trace definition over 859801 tested nonempty supports across twelve parameter pairs. Residual correctness risk is implementation or proof transcription error, not a known counterexample.

## Originality — PASS within inspected sources
The closest primary source is Adler–Benediktsson–Macpherson, arXiv:2007.16042 (2020), whose full Hamming-graph section establishes bounds and sharpness for the *open* relation and remarks only on boundedness for closed neighborhoods. Coudert–Csikós–Ducoffe–Viennot, SEA 2024, offers a general closed-neighborhood computation algorithm rather than this classification. Housholder–Mangiapanello–Senger, arXiv:2505.14641 (2025), studies open-neighborhood problems on induced vertex subsets. None of the inspected statements implies the uniform closed-neighborhood polynomial. This is a best-knowledge priority assessment, not a claim of exhaustive historical uniqueness: the same enumeration might exist under alternative reflexive-incidence terminology.

## Mathematical value — PASS
The theorem provides the full distribution of shattered support sizes for a canonical distance-transitive graph family, rather than only an extremal dimension. It resolves the specific closed-neighborhood gap explicitly left bounded but not sharpened by the principal 2020 source and isolates small-alphabet exceptional geometry; in particular, \(H(3,2)\) separates open and closed dimensions. The exact coefficients also give the probability that a uniformly chosen support of size at most three is shattered.

## Verification and limitations
Run `python check_closed_hamming.py` with standard Python 3. Testing is exhaustive for sizes one through four on eleven named graphs and for sizes one through three on \(H(4,3)\), with reproducible sampling of four-point supports there. Testing does not replace the universal proof. Priority beyond the listed sources and an independent audit remain open.

Self-review: passed. Independent audit: not yet performed.
