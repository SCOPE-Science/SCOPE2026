# Scientific review of the majority-equilibrium theorem

## Correctness — PASS
The mathematical statement is fully quantified for \(n\ge5\) in residue classes 0 and 1 modulo four; the graphs are labelled and updates use strict majority on open neighbors. The critical identity \(N_{ij}=T-d_i-d_j+\mathbf1_{ij\in E}\) follows by inclusion-exclusion. The sum of endpoint degrees over active pairs is \(\sum_i d_i^2\), and Cauchy--Schwarz yields the exact half-population lower bound. Complement symmetry supplies the opposite bound. The resulting equality forces an ordinary graph of uniform degree \((n-1)/2\); the integrality obstruction and converse neighbor-count calculation complete the proof. A finite direct implementation checks the smallest example and the identity on larger examples, but the proof does not depend on an exhaustive finite search.

## Originality — PASS, with historical-priority qualification
The nearest accessible general primary source, Benjamini et al. (arXiv:1405.2486), treats finite majority period-two convergence and random/unimodular networks, not fixed-state classification on two-subset Kneser graphs. Cannings (DOI 10.1109/GAMENETS.2009.5137464) discusses majority on complete, hypercube and cubic families; the publicly accessible abstract does not resolve this classification, and the full article was unavailable. Existing individual computations on the Petersen graph establish the \(n=5\) example, not the all-size modulo-four dichotomy. Results for NOR, parity dynamics, or majority on the complementary triangular graph have different local rules or different edge relations. Searches cannot exclude an unindexed equivalent theorem; this limits historical-priority confidence but does not create a known implication covering the theorem.

## Value — PASS
The two-subset Kneser graphs are a canonical infinite family of highly symmetric disjointness networks. A single increment in the underlying size across classes \(n\equiv0\) and \(n\equiv1\pmod4\) changes equilibrium structure from two consensus states to a natural family in bijection with labelled regular graphs. The proof uncovers the cause: equality in an extremal quadratic degree inequality forces exact half-regularity. The all-size classification and coefficient count expose structure beyond a small-graph census or an arbitrary parameter slice.

## Limits and checked literature
The theorem concerns fixed points only, not all eventually periodic configurations; the two even-degree residue classes remain outside the statement. The 2009 Cannings article could not be inspected in full, and additional unpublished or unindexed results may exist. No independent external validation has been performed.

Self-review: passed. Independent audit: not yet performed.
