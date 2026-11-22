# Scientific review: three-path random-cluster third cumulants

## Correctness — PASS

The connected three-edge cumulant of the weighted random-cluster law on a three-path theta graph has the exact explicit formula given in RESULT.md. The graph's cycle rank equals \(\max(R-1,0)\), where \(R\) counts fully open paths. Product Bernoulli reference weights at edge probabilities \(v_e/(q+v_e)\) therefore acquire precisely the \(q^{\max(R-1,0)}\) tilt. The eight-state generating function gives the displayed factorization for path-completion cumulants. Conditional independence of edges in separate paths, conditioned on each path-completion indicator, transfers the factorization to any choice of three marked edges. For \(1<q\le2\), elementary symmetric bounds make the sign factor positive. For \(q>2\), that factor has one negative constant and positive nonconstant coefficients, yielding exactly one zero along any common positive activity-scaling ray. The strictly positive finite-activity prefactors exclude accidental extra zeros.

An independent direct random-cluster state enumerator implemented in `check_theta.py` passed **972 exact rational cases** across five theta graph geometries, all placements of one marked edge per path, four cluster weights and three activity scales, with separate opposite-sign witnesses on the six-edge network. Exhaustion of these finite cases is supplementary evidence and not the proof for arbitrary lengths.

## Originality — PASS on examined evidence, provisional

Grimmett's classical random-cluster framework gives the bond measure and pairwise positive association for \(q\ge1\). Pairwise FKG inequalities do not imply the sign of a third connected cumulant. Shrock's 2011 Potts/Tutte treatment explicitly includes **hammock networks** in Section IX, so it is a relevant close primary source, but the inspected uniform-activity formulas do not state the all-weight three-marked-edge cumulant, the sign criterion, or the unique \(q>2\) reversal. Related indexed reports about \(q<1\) forest edge correlations or cactus connectivity covariances do not imply the \(q>2\) three-path result: their measures, graph cycles, observables, and order of cumulant differ. Exact graph/parameter equivalences and stronger-family coverage were searched by mathematical content. An unindexed earlier derivation of derivatives of the hammock partition function remains possible.

## Value — PASS

The result gives a sharp universal distinction between the two-state boundary and higher-state ferromagnetic random-cluster systems in a natural smallest multicyclic series-parallel network. It predicts a third-order response sign reversal for arbitrary path lengths, positive heterogeneous edge activities, and arbitrary selection of one edge per path; the threshold is explicitly computable and independent of marked-edge choice. This captures information absent from pairwise FKG correlation signs and is more than a numerical fixed-size observation.

## Limits and closely related sources

Grimmett, *The Random-Cluster Model*, first public 2002-05-23, arXiv:math/0205237. Shrock, *Exact Results on Potts/Tutte Polynomials for Families of Networks with Edge and Vertex Inflations*, first public 2011-01-30, arXiv:1101.5826, especially its Section IX on hammock networks. There is no claim about higher connected cumulants, arbitrary series-parallel graphs, negative activities, or thermodynamic transitions. The literature search cannot prove absolute historical novelty; independent scientific review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
