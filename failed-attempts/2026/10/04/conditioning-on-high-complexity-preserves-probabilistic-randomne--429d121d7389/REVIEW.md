# Independent mathematical audit

## correctness

PASS

Vovk's Theorem 2 gives the numerator bound \(m(B_a)\le c_3\sum_{k\ge a}2^{-g(k)}\). In the same primary paper, Proposition 1 gives \(m(H_a)=\Theta(\tau(a))\). The companion paper proves that \(\tau(a)/f(a)\to\infty\) for every computable positive decreasing \(f\to0\). Taking \(f=1/h\) (after a monotone computable normalization if needed) yields \(1/m(H_a)=o(h(a))\), so division proves the master conditional bound. The four displayed regimes follow from the same series estimates used by Vovk for Corollaries 3--6. The statement is mathematically sound.

## originality

FAIL

The final claim is a direct normalization corollary of results already stated in Vovk's two 2026 papers. The main paper itself places Proposition 1 immediately before Theorem 2 and says that the 'vast majority' of high-complexity objects are probabilistically random; its Corollaries 3--6 already give the four raw decay regimes. The companion paper's slow-tail lemma supplies exactly the missing denominator estimate. No new comparison, invariant, or theorem is needed beyond dividing the published numerator by the published high-complexity mass and choosing a computable slow factor.

## value

FAIL

The normalized conditional statement is useful exposition, but scientifically it is a routine quotient of adjacent published estimates, and each named rate is already computed in the source paper. It introduces no new structural lemma, sharp boundary, exact invariant, or nontrivial comparison under the stated value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
