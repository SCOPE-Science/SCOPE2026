# Scientific review of the triangular-graph open-neighborhood census

## Correctness — PASS

The graph-cut identity gives an exact reduction: each trace is the edge set meeting a two-element center in exactly one endpoint. The two-extra-vertex stabilization bound holds for every support graph, independently of ambient order. The full five-edge classification uses a recurrence covering every simple graph without isolates, verifies all \(1,2,5,11,26\) unlabeled types at each edge count, and hence rules out larger shattered supports. Automorphism-weighted embeddings yield each coefficient. `verify.py` independently compares every labelled support up to size four for \(2\le n\le10\). This is an exhaustive finite certificate for the universal theorem, not merely a small-order experiment.

## Originality — PASS, qualified

Adler, Benediktsson and Macpherson (arXiv:2007.16042, §3) already establish the universal Johnson-graph upper bound of four and the first order admitting a shattered four-support. Those facts are excluded from the novelty claim. The assessed new portion is the exact coefficientwise polynomial for all triangular graphs, including the global cut-motif criterion, availability thresholds, and uniform random-support probabilities. The closest inspected published primary work and scientific searches did not reveal an equivalent complete enumeration, but alternate terminology remains a historical-priority risk.

## Value — PASS

Counts of all shattered supports give a natural refinement of VC dimension for a standard family of NIP graph incidences. This result determines every coefficient, including \(s_4(7)=2625\), and gives precise asymptotic shattering frequencies \(12/n\) for triples and \(48/n^2\) for quadruples. It is not simply the known fact that VC dimension is four.

## Limits and source comparison

Only open neighborhoods of \(J(n,2)\) are treated, not the entire Johnson graph family. The earlier paper contains substantial local structural analysis and a cardinality bound; it does not display the coefficientwise counts. The 2024 general algorithm work addresses closed neighborhoods. The finite classification is supplied with reproducible code, and comprehensive historical priority is not certified.

Self-review: passed. Independent audit: not yet performed.
