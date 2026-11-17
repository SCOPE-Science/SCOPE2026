# Independent mathematical audit

## correctness

PASS

PASS: conditional on N_j=r, remaining n-r draws choose m-1 other boxes, giving E[H|N_j=r]=1_{r odd}+(m-1)(1-u^(n-r))/2; the unconditioned parity mean is m(1-v^n)/2. Exchangeability gives the exact normalized covariance. For even r Jensen's strict inequality is valid for n>=r>=2 and 0<=u<v<1; for odd r the first difference 2(u^(n-r)-v^n) changes sign at most once, and the sequence has negative initial value for r>=3 and positive limit 1. n=1 singleton zero, m=3 zero-power convention explicitly works. Uniform logarithmic expansions imply the unique root e^(2c)+2c=2r-1 for fixed odd r>=3, without proving a finite-m error bound. Independent weighted enumeration directly confirmed 5 (m,n,r) cases including m3 boundary and n1; no finite sample replaces this analytic proof.

## originality

FAIL

FAIL: November 2 previously published checkerboard covariance theorem gives the identical all-parameter formula for m>=4, identical parity sign laws and the same threshold root, with a strictly stronger O_r(1) localization. The excluded m=3 and n=1 cases reduce by a one-line substitution and cannot support a distinct result.

## value

FAIL

FAIL: after exact earlier full coverage, the only remaining n=1 and m=3 cases are routine binomial-parity boundary substitutions; there is no new nontrivial structural lemma, meaningful classification or unknown natural invariant to credit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
