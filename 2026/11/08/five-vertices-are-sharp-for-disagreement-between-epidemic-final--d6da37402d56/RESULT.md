# Five vertices are sharp for disagreement between epidemic final size and peak infectious burden

## Finding

**Theorem.** Consider a homogeneous continuous-time susceptible–infectious–removed (SIR) epidemic on a connected finite simple undirected graph \(G=(V,E)\). Each susceptible–infectious edge transmits at rate \(\beta>0\), each infectious vertex recovers at rate \(1\), and the initially infectious set is one vertex \(v\). Let \(F_G(v;\beta)\) be the expected final number of vertices ever infected and \(H_G(v;\beta)\) the expected maximum number of vertices simultaneously infectious during the outbreak.

For **every** \(G\) with \(1\le |V|\le4\), every \(\beta>0\), and all vertices \(u,v\),
\[
\operatorname{sgn}(F_G(u;\beta)-F_G(v;\beta))
=\operatorname{sgn}(H_G(u;\beta)-H_G(v;\beta)).
\]
In particular, the sets of maximizers of the two expected outbreak objectives coincide, including exact ties.

The bound is sharp. Let \(V=\{0,1,2,3,4\}\) and
\[
E=\{\{0,1\},\{1,3\},\{1,4\},\{2,3\},\{2,4\},\{3,4\}\}.
\]
At \(\beta=2\), the complete exact values are:

| Seed \(v\) | \(F_G(v;2)\) | \(H_G(v;2)\) |
| --- | --- | --- |
| 0 | \(6359/2025\) | \(232439/85050\) |
| 1 | \(2617/675\) | \(5176097/1559250\) |
| 2 | \(2471/675\) | \(119299/38500\) |
| 3, 4 | \(3679/945\) | \(16018271/4851000\) |

Thus the final-size maximizers are exactly vertices \(3,4\), whereas the peak-burden maximizer is exactly vertex \(1\). In particular,
\[
F_G(3;2)-F_G(1;2)=76/4725>0,
\qquad H_G(1;2)-H_G(3;2)=766277/43659000>0.
\]
The five-vertex graph consists of a diamond (four vertices, five edges) with a leaf attached to one of its degree-two vertices. The result concerns **expected maximum concurrent prevalence**, not peak incidence over a reporting window.

## Assumptions and scope

The graph is finite, undirected, loopless, and unweighted. Recovery is permanent (SIR, not SIS); vertex infectious periods are independent exponential random variables with mean one; each undirected edge carries independent infectious contact events at rate \(\beta\) in the infectious-to-susceptible direction. The count \(H_G\) is the maximum of the integer-valued process of currently infectious individuals over all real times before absorption, including the initial state. Isolated one-vertex graphs are permitted, and connectedness excludes irrelevant disjoint components. Time rescaling makes any common positive recovery rate equivalent to rate one; the variable \(\beta\) is consequently a dimensionless transmission-to-recovery ratio.

## Proof

Write \(n=|V|\). Each transient state is \((S,I,h)\), with disjoint subsets \(S,I\subseteq V\), all other vertices recovered, and \(h\) the largest infectious count attained so far (so \(h\ge |I|\)). For \(j\in S\), define \(k_j=|N(j)\cap I|\) and total event rate
\[
R(S,I)=|I|+\beta\sum_{j\in S}k_j.
\]
Let \(f(S,I,h)\) and \(g(S,I,h)\) be the expected final cumulative count and expected final peak, conditional on that state. The terminal values at \(I=\varnothing\) are \(f=n-|S|\) and \(g=h\). For nonempty \(I\), first-event conditioning gives, for either \(q=f\) or \(q=g\),
\[
q(S,I,h)=\frac1{R(S,I)}\left(
\sum_{i\in I}q(S,I\setminus\{i\},h)
+\beta\sum_{j\in S}k_j q(S\setminus\{j\},I\cup\{j\},\max\{h,|I|+1\})
\right).
\]
This recurrence is **finite and acyclic**: an infection reduces \(|S|\), while a recovery preserves \(|S|\) and reduces \(|I|\). Hence induction in lexicographic order determines the unique expectations as rational functions of \(\beta\). Initial values are \(f(V\setminus\{v\},\{v\},1)\) and \(g(V\setminus\{v\},\{v\},1)\).

For the universal small-graph assertion, there are exactly \(1,1,2,6\) connected simple-graph isomorphism types at orders \(1,2,3,4\). At order four these are the two trees (star and path), two four-edge unicyclic graphs (cycle and triangle with pendant leaf), the diamond, and the complete graph. The order-three representatives are a path and triangle. For each representative, the displayed recurrence gives an exact rational pair for every vertex. The accompanying `check_symbolic.py` forms, for every one of the \(43\) unordered vertex pairs among the \(11\) types, the differences \(\Delta_F\) and \(\Delta_H\), checks that either both are identically zero or neither is, then reduces \(\Delta_F\Delta_H\) to a rational expression whose numerator and denominator have **nonnegative polynomial coefficients** in \(\beta\), with nonzero numerator. Thus its sign is strictly positive for all \(\beta>0\). This is an exact algebraic coefficient certificate, not numerical sampling. There are \(18\) nonzero comparisons across the selected representatives. The distinct-vertex ranking in each non-vertex-transitive graph is, from greatest to least, the center then leaf of the three-vertex path; star center then leaf; internal then terminal path-four vertices; triangle attachment then remaining triangle vertices then pendant leaf; and diamond degree-three then degree-two vertices. Vertex-transitive graphs have all ties. Each pair has the same order for the two objectives.

For sharpness, substitute the six listed edges and \(\beta=2\) into the same absorbing recursion. Exact rational evaluation yields the five rows above. All inequalities and all ties hold as written. Therefore order five is both necessary and sufficient for different optimal single-seed sets.

## Verification

Run `python check_symbolic.py` with SymPy installed (dependency listed in `requirements.txt`). It recomputes every small-graph rational function, checks simultaneous ties and validates coefficientwise positivity for every pair, giving `PASS: 11 connected classes, 43 root pairs, 18 strict pairs; all beta>0`. Run `python check_witness.py` with Python's standard library alone; it independently evaluates the witness by direct set-state conditional probabilities with rational arithmetic, tests both global optimal sets, and prints its exact values. This reports `PASS witness` and visits \(378\) distinct conditional states. Both scripts were executed successfully on the included source files. The general sign assertion follows from exact symbolic identities and coefficient positivity, not from finite parameter samples.

## Relationship to prior work

Mills and Riley (2014, published April 10, 2014) show that epidemic peaks and cumulative attack rates need not react identically to spatial model resolution, but analyze simulation-based incidence peaks in spatial metapopulations rather than the **expected maximum concurrent prevalence** of finite graph-rooted SIR processes. Economou, Gómez-Corral and López García (2014 online / 2015 issue) give algorithms for maximal concurrent infectives in a heterogeneous **SIS** process, in which recovered individuals may become susceptible again; their model does not impose the irreversible-recovery ranking established here. Holme (2017) exhaustively studies small-graph SIR seed influence by **final size**, vaccination and sentinel time; the full text does not include concurrent-peak seed rankings. Its exact CT-SIR transition law matches ours, but none of its three optimized objectives is \(H_G\). No theorem in these inspected sources directly supplies the universal four-vertex agreement or the five-vertex divergence. These statements may nevertheless have unlocated equivalents, especially in graph epidemic peak-demand literature; they are not claimed independently audited or definitively first in history.

## Limitations

Only homogeneous, exponential-recovery, undirected, finite-network SIR dynamics with a single seed are covered. The exact five-vertex model is a structural counterexample, not a calibrated estimate of health-care demand. No assertion is made for the probability of exceeding a specified peak, for peak incidence (new cases per interval), or for several initial seeds; different objectives can have different rankings. The symbolically proved small-order bound holds for every positive transmission-to-recovery ratio, while the particular witness uses \(\beta=2\). All originality assessments are limited by accessible search and reading, and external independent validation has not been performed.

## References

1. Mills, H. L. and Riley, S. (2014). The Spatial Resolution of Epidemic Peaks. *PLoS Computational Biology* 10(4), e1003561. Public online date April 10, 2014. https://doi.org/10.1371/journal.pcbi.1003561
2. Economou, A., Gómez-Corral, A., and López García, M. (2015). A stochastic SIS epidemic model with heterogeneous contacts. *Physica A* 421, 78–97. First online November 13, 2014. https://doi.org/10.1016/j.physa.2014.10.054 . Accepted manuscript: https://eprints.whiterose.ac.uk/id/eprint/90144/
3. Holme, P. (2017). Three faces of node importance in network epidemiology: Exact results for small graphs. *Physical Review E* 96, 062305. Published December 5, 2017. https://doi.org/10.1103/PhysRevE.96.062305
