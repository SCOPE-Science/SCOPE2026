# Scientific review

## Correctness — PASS

The scope is indexed binary words of exact Hamming weight two, with the standard cyclic overlapping-pair metric and threshold seven. Two distinct supports must be disjoint because a shared coordinate gives at most four changed reads. For disjoint supports the exact identity \(d_{\mathrm p}(x_A,x_B)=8-e_n(A\cup B)\) converts the problem to edge incidence in the coordinate cycle. The capacity upper bound is \(\lfloor n/2\rfloor\); occupied-edge counting excludes three codewords at lengths seven and eight and four at length nine, and excludes two at all shorter lengths. Explicit witnesses settle these exceptions. For every \(k\ge5\), a connected four-regular circulant graph has an Euler tour with twice-occurring vertex labels, giving a valid \(k\)-code at lengths \(2k\) and \(2k+1\). At equality with length \(2k\), every coordinate is occupied and the incidence criterion forces a simple four-regular Euler graph. Thus the converse is also proved. `verify.py` provides independently implemented small-case and long-witness checks. No external certificate is used to replace a mathematical step.

## Originality — PASS, qualified

The Cassuto–Blaum paper defines and studies symbol-pair codes, and Chee–Ji–Kiah–Wang–Yin's Proposition 3.2 introduces the Euler-graph construction from an MDS source code. These are acknowledged direct methodological antecedents; the finite equality cutoff and the converse for binary Hamming-weight-two codes are not asserted in the inspected passages. This comparison is substantive: a general graph construction cannot by itself yield the sharp small-length cutoffs or classify every optimum. The 2025 Zhao–Chang constant-**pair**-weight paper treats a super-family including many of the same permissible pair-weight-four codewords. Its abstract is available, but full text could not be obtained; overlap or coverage of some extremal parameters cannot be excluded without it. No broad literature-search null result is treated as a proof of novelty. Historical priority remains qualified.

## Value — PASS

Low-weight signaling under overlapping pair reads is a natural constrained coding problem, and seven is the extremal symbol-pair separation attainable by many disjoint two-pulse patterns. The theorem closes its entire optimal-size function, pinpoints a genuine short-block obstruction at lengths below ten, and supplies a structural equivalence between all even-length optimizers and four-regular Eulerian graphs. This is more than the elementary disjointness upper bound and is not merely a finite table. The result does not imply unrestricted channel capacity improvements.

## Limitations and closest literature

No conclusion is claimed for larger Hamming weight, other distance thresholds, or classification of all odd-length optimizers. The strongest directly adjacent published methods are Cassuto–Blaum (2010/2011), Chee et al. (2012/2013), and the closely overlapping but inaccessible full Zhao–Chang (2025) article. Independent audit remains unperformed.

Self-review: passed. Independent audit: not yet performed.
