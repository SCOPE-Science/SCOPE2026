# Independent mathematical audit

## correctness

PASS

The frozen stationary-product and lag-eigenvalue formulas are correct under the original unanimous update rule. The connected order-two statement and proof of labelled order-three reconstruction were not correct as written: complementing all edges in K₄ preserves their labelled line graph, but maps a three-edge star to a triangle and is not induced by a vertex permutation. The frozen proof checked triples only in whole triangle/claw components; this misses K₄. The completed repair uses the lag formula to recover by inclusion–exclusion the cardinality of the intersection of the endpoints of any one, two, or three observed edges; the coefficient ω(r−1)^|S|/N is nonzero at all stated rates. Every incident pair has exactly one common endpoint; the pair plus all edges that share that endpoint with the pair is exactly that vertex's full star. Hence all stars of size at least two are recovered and can be deduplicated, since simplicity excludes two distinct vertices sharing two edges. Each edge is completed by enough distinct private leaf endpoints to reach two; two leaves are added for a single-edge component. There are no isolated vertices to recover. This establishes the original universal order-three upper bound without appealing to a label-preserving Whitney statement. The distinct labellings of K₄ are the connected lower-bound witness: the probabilities of hitting neither, just one, or both of any fixed pair of labelled edges depend only on N and pair intersection, so their projected stationary trajectories coincide for every fixed singleton or pair. The common-endpoint flip on a triple is detected by ω(1−r)³/N. The seven-vertex frozen witness remains correct as a second example. Independently checked both witnesses with exact projected kernels and stationary laws and all 814 additional simple graphs without isolates on fixed vertex sets with 2–5 vertices using the lag formula (replay: python3 /workspace/repairs/5/check.py). The two exact gaps at the chosen rates are 9/128 and 9/224; the finite checks do not replace the proof. The frozen checker was inspected, not executed. Complete corrected RESULT.md, check.py and scientific VERIFICATION.md body are supplied, with the frozen verification metadata preserved.

## originality

PASS

For the final repaired theorem, prior work supplies the vertex-clock model, classical single-edge/tensor calculations and line-graph facts, including the potential non-induced edge maps. The supported distinct claim is the model-specific exact observation-order characterization: a third-degree lag statistic yields common-endpoint information anywhere, and the full stationary order-two projected trajectories can fail even at known N on connected graphs. The graph automorphism itself and recovering unlabelled roots up to the classical exception are not credited as new.

## value

PASS

For a specified vertex-clock stochastic model the result determines the smallest number of persistent edge IDs that must be observed jointly in the worst case. It converts short-lag stationary data into exact labelled incidence, including all ambiguous local triangles and leaf endpoints. The connected witness rules out using longer trajectories of singletons and pairs as a substitute. This is a structural identifiability threshold at all nondegenerate rates, not a finite-sample estimator or an unlabelled nonidentifiability theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
