# Scientific review: four-support cycle-length covariance for successions

## Correctness — PASS

Every conditioned succession specifies two distinct outgoing and incoming arrows. They form two fixed loops, one path of two edges, or two disjoint single-edge paths. Uniform completion is bijective to a permutation of \(n-2\) contracted vertices, and cycle-length shifts are determined by whether a contracted cycle contains zero, one, or two marked vertices. The cycle-index mark probabilities \(1/m\) and \((h-1)/[m(m-1)]\) lead to exact conditional polynomials and the displayed positionwise identity. Direct exhaustive enumeration through order nine and 2,688 independent rational comparisons agreed. No finite check was used as a substitute for the all-size proof.

## Originality — PASS, with bounded historical-priority risk

The Diaconis–Evans–Graham theorem concerns the marginal succession-position set, not its joint law with the original permutation's cycle counts. Mansour–Shattuck's joint count uses **cycle-notation** successions and total cycles and explicitly warns that this differs for other joint statistics from the one-line succession count. An earlier full fixed-point-indicator/succession-indicator covariance matrix already implies the entire \(j=1\) positionwise coefficient and is not credited as new. The nontrivial new component is the complete length- and position-resolved covariance identity, its \(j=2,n-1,n\) coefficients, and the cancellation for all \(3\le j\le n-2\). Exact searches did not reveal a dominating statement; this does not prove absolute novelty. Broader historical cycle-index enumerations remain an explicit risk.

## Value — PASS

Successions are a natural shuffle-diagnostic local statistic, whereas cycle lengths encode global orbit topology of the same permutation. The theorem completely locates their **linear dependence** in four extremal cycle lengths, supplies an explicit boundary/interior mechanism, and gives exact orthogonality to the entire span of intermediate cycle counts. It resolves a natural joint-statistic question not answered by matching marginal distributions; it is not merely a numeric special case or routine substitution.

## Closest literature and limitations

Sources inspected include Diaconis–Evans–Graham (2013 technical report, introduction and enumeration), Mansour–Shattuck (2016, author-uploaded full text, especially the introduction, Sections 2–4), and records concerning Reilly–Tanny (1980) and Du–Ji (2024/2026). Previously recorded fixed-point covariance overlaps one coefficient only. The result does not assert independence, higher-order joint laws, or a nonuniform extension. Some older papers were available only through abstracts or references, so historical priority requires further expert review.

Self-review: passed. Independent audit: not yet performed.
