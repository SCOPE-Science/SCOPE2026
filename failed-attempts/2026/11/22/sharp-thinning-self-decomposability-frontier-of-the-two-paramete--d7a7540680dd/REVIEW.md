# Independent mathematical audit

## correctness

PASS

The normalized pgf has one numerator zero and a single negative-binomial factor; expanding its logarithm gives (alpha q^k-r^k)/k>0 and absolute summability. Under thinning, q_t=t/(theta+t) and r_t=t/(theta+1+t). Differentiating the logarithmic coefficients in t shows that the ratio of the subtracted to the positive derivative, before the factor alpha, is ((theta+1)/theta)((theta+t)/(theta+1+t))^2(r_t/q_t)^(k-1). It is strictly less than A(theta) for t<1, and tends to A(theta) for k=1 as t tends to one. Integration proves the strictly positive innovation intensities including equality; if alpha<A(theta), the first logarithmic coefficient, and hence H_t'(0), is negative for t close enough to one. The pgf quotient determines the innovation law uniquely. A(theta)-1 has numerator 1-theta-theta², confirming the admissible-shape transition. At the rational WNBL witness q=49/51, r=49/100, q_(1/2)=49/53 and r_(1/2)=49/151; the exact first log coefficient is -249361/2400900. Bakouch's original mgf/pgf and stated parameter range admit this witness, and Definition 5.3 uses the same thinning convention. Read VERIFICATION.md and check.py; did not execute the frozen script.

## originality

FAIL

The distinct indexed record 6076ca6aa947 covers the main finding in a strictly broader family. Denote its lower Gamma shape by m and its lower-shape weight by s. Set m=alpha-1 and s=theta/(theta+1). Its pgf is then identical, its all-parameter condition (m+1)(theta+s)^2 >= s(theta+1)^2 becomes the claimed A(theta), and its innovation formula and first-probability obstruction specialize directly. It is a separate record, not an index hit for the assigned article. Both records are dated the same day, which does not establish order, but the material coverage is demonstrable. The WNBL witness correctly flags a false literature assertion, but this particular obstruction is also a parameter substitution in the broader theorem, not an uncovered new mathematical claim.

## value

FAIL

The phase law is useful, and the WNBL application usefully illustrates a literature error. As a separate mathematical finding, however, the complete frontier, innovation construction and obstruction are direct specializations of the already covering adjacent-Gamma result. The particular rational example is one evaluation of its explicit obstruction. No distinct nonmechanical result survives this comparison for a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
