# Independent mathematical audit

## correctness

PASS

Enomoto's general lower-bound formula, specialized to \(q=7,a=2n,b=n\) and the full \(2n\)-by-\(n\) rectangle, gives modules of length \(11n\) and the stated factorial/hook-product lower bound. The rectangular hook identity is exact. Stirling summation gives \(\log L_n=(4+8\log2-7\log3)n^2+O(n\log n)\), hence the normalized coefficient after dividing by \(121n^2\). A fresh exact hook-product replay for \(1\le n\le6\) and a fresh numerical comparison confirmed \(0.015329681188\ldots>(1-\log2)/25\).

## originality

FAIL

The source's general \(q\)-Kronecker theorem already gives the filtration-count lower bound for every admissible \(q,a,b,
u\). The assigned result chooses \(q=7,a=2n,b=n\), inserts the standard rectangular hook product, and applies Stirling/Riemann-sum asymptotics. A current published four-arrow result already demonstrates the same strategy of improving the endpoint by parameter specialization. Under the implication bar, the seven-arrow number is therefore a routine special-case optimization of a stronger prior theorem, not a new theorem merely because this parameter choice was not printed in the source.

## value

FAIL

The approximately \(24.9\%\) numerical improvement is nontrivial as a benchmark, but it is obtained by an elementary parameter/partition substitution into a general theorem specifically designed for such choices, followed by standard hook asymptotics. Without an optimality theorem or new mechanism, this does not clear the bar against routine parameter specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
