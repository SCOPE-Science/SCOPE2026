# Independent mathematical audit

## correctness

PASS

For a prescribed marked path on k+1 vertices, the forest-extension count is (k+1)n^(n-k-2). Deleting a specified non-path leaf and choosing its neighbor gives probability a_n^(n-k-2); deleting a marked endpoint when it is a leaf gives k/(k+1) times this probability. The formula handles the spanning path. Direct subtraction gives the stated cubic numerator and all ties, including n=3. The centered profile starts at zero since mu(n,1)=E L_n, is positive at k=2 for n>=4, and has one crossing to negative values before or at k=n-1. Subtracting a distance at the crossing in the covariance proves strict negativity. The distance probabilities are (k+1)/n times the product for j=2,...,k of 1-j/n, giving a Gaussian envelope and Rayleigh moment convergence. Multiplying the expansion of a_n^(n-k-2) by n-k+1-2/(k+1) yields the displayed 5/2-k^2/(2n) correction, with the stated error and an exponentially small tail. The Rayleigh moment identity Cov(R,R^2)=sqrt(pi/2) gives the covariance constant; Prüfer empty-box indicators give the leaf variance coefficient and the correlation constant follows. No exact finite covariance magnitude is asserted.

## originality

FAIL

The titular and principal exact conditional-mean, cubic-turning-point and tie claims are directly covered by two identifiable earlier Resultary statements. The added dependence formulas are correct, but the finite sign follows by a single-crossing comparison from the established profile and the standard marginal mean. The sharp asymptotic covariance and correlation constants are also consequences of the prior random-mapping law under the doubly marked tree coupling, with the bounded endpoint contributions asymptotically constant after conditioning. This is a coverage verdict, not a claim that the exact finite sign was written verbatim before or that the mathematics is false.

## value

FAIL

The peak versus typical-distance disparity has mathematical interest, but the principal exact theorem is already known. The incremental dependence statements are a short single-crossing deduction and a transfer of known sharp constants. Neither supplies an independently valuable new result here; no repair is offered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
