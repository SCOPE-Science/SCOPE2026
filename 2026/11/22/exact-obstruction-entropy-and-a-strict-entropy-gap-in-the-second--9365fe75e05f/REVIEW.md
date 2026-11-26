# Independent mathematical audit

## correctness

PASS

The bilateral XOR differences d_i=x_i⊕x_(i+1) are unrestricted, and the first-step output is d_(i−1)∨d_i. This output has no isolated one; conversely any word on the bilateral shift avoiding 010 is recovered by taking differences d_i=y_i∧y_(i+1). For the second image, the independent reconstruction used an eight-vertex de Bruijn graph on three difference bits instead of the supplied 16-vertex graph on original bits. Label the edge for four bits a,b,c,d by whether a∨b,b∨c,c∨d are not all equal. All difference blocks integrate and extend to bilateral inputs. Determinizing from all vertices and refining right languages gave 17 live subsets and 13 accepting minimized states. For the forbidden computation, accept precisely a dead final prefix-state transition with a live suffix-state transition; all proper contiguous factors are contained in the prefix or suffix missing one letter. Both individual letters occur. The count is of distinct words because the machines are deterministic and each productive path specifies its letters. The independent pair graph had 29 reachable and 16 productive states. Exact transfer arithmetic reproduced the characteristic polynomials, coefficients through degree 17 of det(I−zA)M(z), and the displayed list through length 25. The degree bound 2+15 proves the all-length identity. There is one 14-state primitive component with self-loops on productive paths; the other two states are transient, giving m_2(n)∼Cλ^n with C>0 and hence a strictly sofic image. The image automaton's Perron growth governs all admitted words since all accepting states are accessible. Independent exact shifted-power coefficient signs isolate both largest real roots in the stated disjoint rational intervals. Wu–Zhang Theorem A applies since the minimal forbidden words generate the shift, so h_G≤h_M<h_top; this gives the stated finite ergodic, Bernoulli-up-to-period and characteristic maximal-entropy-measure conclusions without asserting how many such ergodic measures there are.

## originality

PASS

Credit the exact second-image minimal-forbidden series, its Perron growth, and the evaluated strict gap. The one-step benchmark, first missing word at length twelve, finite-state methods and general measure theorem are prior work. Known presentations of the second-image language make related invariants computable; available evidence does not show an earlier evaluated all-length minimal-forbidden series or this comparison of the two entropy rates. Direct full-text access to the closest older Rule 126 paper was unavailable after lawful attempts, so priority there remains an explicit bounded risk rather than evidence of noncoverage.

## value

PASS

Rule 126 is a natural benchmark with an unusually simple first image and a known sharp finite discrepancy. The all-length second-image obstruction series demonstrates a change to strictly sofic behavior with exponentially many minimal forbidden words after just one further update. Its rate is provably separated from the language entropy; this is an evaluated nontrivial test case for the entropy-gap theorem, beyond an arbitrary finite enumeration or the previously known shortest witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
