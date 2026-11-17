# Scientific review: clique-windmill vertex radii

## Correctness — PASS

The centered edge-generator normalization is fixed. Every acyclic orientation on the one-hub clique bouquet is uniquely specified by independent total orders on the cliques. Its local coordinate scores are the centered ranks, giving the exact identity \(Q=mC_k+2\sum_{i<j}H_iH_j\). The multinomial formula counts all vertex radii, including collisions, without overcounting. Mean and variance follow from independent centered ranks, and the fixed-clique-size limit follows from CLT, SLLN and Slutsky. The strict outer-contact condition is a pairwise-product equality. A separately implemented direct edge-sign enumerator checked 548,748 vertices in seven cases, all moments and exact shell counts. These finite checks are corroboration, not the infinite proof.

## Originality — PASS (historical priority provisional)

Sanchez–Kolesnik (arXiv:2009.09322, full HTML Sections 1–3) study tournament-score zonotopes and their realizability, not vertex squared-radius distributions. Padrol–Pilaud–Poullot (arXiv:2111.12422, full HTML sections 1–2) determine deformation cones and recall acyclic-orientation vertices. Pešović–Stojadinović (arXiv:2209.12053, full HTML sections 2–4) study combinatorial, not Euclidean radial, enumerators. The closest published general cone-law result already supplies the outer radius and farthest contacts, which are explicitly credited here. Its full proof and finding do not enumerate intermediate Euclidean vertex-radius shells or determine their variance and limiting law. The published cactus inertia result uses uniform interior volume, not uniform vertex counting, and cannot imply this distribution. Three directed mathematical-record searches for clique-windmill Euclidean vertex radii, shell multiplicities and chi-square limits did not identify equivalent/stronger coverage. Failure of search is not uniqueness proof; alternative terminology is the remaining bibliographic risk.

## Mathematical value — PASS

The joint hub coordinate couples otherwise independently oriented clique blocks and produces a nontrivial *quadratic* global radial statistic. The exact complete radius polynomial is a geometrically natural all-shell invariant. Its exact order-\(m^2\) variance and non-Gaussian chi-square limit show that vertex radii fail to concentrate even though every petal is fixed-size and all vertices arise from symmetric local permutahedra. This quantifies a distinction between typical vertices and exponentially rare extreme contacts; it is not implied by knowledge of only the outer radius or uniform-volume inertia.

## Closest literature and limitations

The claim concerns the full discrete uniform-vertex radial law in the canonical Euclidean realization, for integers \(k\ge3,m\ge2\), with fixed \(k\) in the limit. The comparison does not certify absolute historical priority, and no independent audit was conducted. Earlier outer-contact theorems remain credited as prior knowledge.

Self-review: passed. Independent audit: not yet performed.
