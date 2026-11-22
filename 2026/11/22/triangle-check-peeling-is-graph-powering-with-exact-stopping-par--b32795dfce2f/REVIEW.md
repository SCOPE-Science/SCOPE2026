# Scientific assessment: complete triangle-check peeling

## Correctness

**PASS.** The check-to-length-two-path identity proves a graph-square recurrence, then the distance-doubling induction proves every round. The no-induced-path characterization proves the exact partition classification; reverse partition refinement proves the minimal stopping-set assertion. Vertex-potential representation over \(\mathbb F_2\) gives the code dimension and residual completion count. The component-containing-a-marked-vertex argument yields the random graph recurrence. Two differently written exhaustive checkers verified every erasure pattern for orders three through six; a separate partition enumeration checked polynomial and connectivity sequences through order seven. These finite checks do not substitute for the all-order proof.

## Originality

**PASS, with priority risk.** Kashyap and Vardy (2003, doi:10.1109/ISIT.2003.1228136) already supply a lower bound that yields the minimum nonempty stopping size \(n-1\). That lower bound is expressly excluded from new claims. Psota and Pérez (2010, doi:10.1155/2010/432495) establish the general Tanner stopping-set framework. Related indexed projective-plane stopping enumerations use a different check matrix; Hamming-code matrix enumeration was assessed only at abstract level. Comparisons of alternative formulations as graph squaring, induced-path-free cluster graphs, cut-code decoding and partitions did not reveal an equivalent complete dynamic theorem. An unindexed equivalent result or stronger classical statement remains possible.

## Value

**PASS.** All-initial-state peeling dynamics for this natural complete pair-by-triple check family are reduced to exact graph-distance calculations, with sharp iteration bounds, exact stopping-set geometry and polynomial, and a precise boundary between unique completion and ambiguity. The result connects a practical iterative-decoding limitation to connected labelled graphs and gives all-order formulas rather than a one-off enumeration.

## Limitations and relevant sources

The proof requires all triple checks and synchronous erasure recovery, and says nothing about sparse check selections, corrupted observations or asynchronous update counts. Code-cut equivalences, generic stopping bounds, Bell-number counts and graph connectivity laws are acknowledged as known ingredients. Relevant scientific literature: Kashyap–Vardy 2003 DOI 10.1109/ISIT.2003.1228136; Psota–Pérez 2010 DOI 10.1155/2010/432495; Abdel-Ghaffar–Weber 2006 arXiv:cs/0603007 (abstract-level comparison only). Independent validation of novelty and scientific correctness is outstanding.

Self-review: passed. Independent audit: not yet performed.
