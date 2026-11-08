# Scientific review

## Correctness — PASS
The proof constructs the exact reachable minimal DFAO using trailing maximal digits and proves distinctness of all \(a+p\) output residuals from minimal eventual period and onset. In higher bases two reset digits give a shortest conflicting path of length two; in binary with positive preperiod every state has single-label incoming edges; in binary with zero preperiod the shortest mixed path has length exactly \(p+1\). The normalized formula then follows from Allouche–Yao [1, Theorems 1–2]. This establishes all quantifiers, including constants and composite bases. A standalone finite verifier tested 4,094 actual parameter configurations and 237,440 direct integer evaluations; these tests do not stand in for the proof.

## Originality — PASS, with residual risk
Allouche–Yao [1] define the measure, prove the intrinsic graph criterion, and calculate the binary period-doubling example \(p=2,a=0\), which is explicitly excluded from the novelty claim. Their accessible arXiv full text does not state a valuation-controller classification. The exact general formula covers every ultimately periodic controller and alphabet base and distinguishes preperiod from least period. Previously reported residue-clock opacity formulas concern the modular sequence \(n\bmod m\), not valuation sequences; results on finite digit-pattern counters also do not imply this universal tail-cycle description. Semantic research comparisons did not locate a covering result, but searches cannot prove absence. A 2026 revised journal text and unindexed literature remain risks.

## Value — PASS
A complete classification of a natural infinite family of automatic words is more informative than a single special-case calculation: the automaton-state minimum and the entire opacity spectrum are exact and exhibit a sharp, structural base dichotomy. Every higher base forces maximal opacity, whereas binary allows either full transparency or any dyadic opacity level, determined solely by the controller's least preperiod and period. This exposes a phenomenon invisible from the classic period-doubling example and identifies the exact mechanism (competing reset labels versus cycle closure). No downstream theorem is claimed.

## Scope and limitations
The claims concern the prefix metric of [1] and ultimately periodic controllers. Numerical checks have finite scope; the proof supplies the infinite result. Related comparison metrics and general automatic sequences are outside scope. The later journal revision of [1] was not fully inspected.

Self-review: passed. Independent audit: not yet performed.

## Reference
[1] J.-P. Allouche and J.-Y. Yao, *Opacity complexity of automatic sequences. The general case*, arXiv:2404.13601v1 (2024-04-21), https://arxiv.org/html/2404.13601v1.
