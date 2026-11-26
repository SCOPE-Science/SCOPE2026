# Independent mathematical audit

## correctness

PASS

The prescribed affine branches delete column 0 precisely on a minus-to-plus switch and column n−1 precisely on a plus-to-minus switch. With X=(epsilon,u,v) and Y rows (1^T,−e_0^T,e_{n−1}^T), direct multiplication and expansion of det(zI−YX) give the coefficients −E−b, AU−BV+Eb, and U(Ba−Ab); Sylvester includes the residual n−3 zero roots. An independent integer Bareiss determinant check compared both sides at n+1 distinct integer arguments for all 248 words of lengths 3–7, without executing the frozen checker. The interior Rademacher sum has the standard CLT independently of the endpoints; the variance of each switch count is O(n) by one-dependence. After scaling the polynomial the terminal and constant contributions vanish and the quadratic coefficient of degree zero is (U−V)/4. Continuity of the maximal root modulus includes repeated roots. For U=+1,V=−1 the complex roots have constant modulus 1/sqrt(2) on |Z|<sqrt(2); the boundary has zero probability and each other branch has zero mass at any single given value. The atom mass is erf(1)/4 = 0.21067519823742872. Row sums give the unsigned bounds, and the reciprocal determinant has the asserted singularity scale as a symbolic identity (if the matrix is nilpotent the reciprocal is identically 1, hence entire). No geometric zeta equality or finite-size exact atom of this mass is required.

## originality

PASS

Best-of-knowledge pass for the random signed spectral law and atom, not for the deterministic construction, its ordinary entropy estimate, the orientation cover, or weighted kneading theory.

## value

PASS

The atom is a concrete, non-Gaussian consequence of bounded-rank sign cancellation in a natural high-entropy family: conjugate roots lock the modulus on an interval of Gaussian values. Together with the different scaling of signed and unsigned growth this is useful spectral information not reducible to an entropy estimate or a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
