# Independent mathematical audit

## correctness

PASS

Incidence counting gives the nonconstant singular value s=q^((d-1)/2). On the zero-sum space, the half-constant contrast has eigenvalue gamma=(v-1)2^p-k-q^d3^p, and each paired nonconstant singular space gives -2^p ± s(3^p-1), with multiplicity v-1 each. The plus mode has exactly one crossing. Gamma decreases from -1 for q>=3 and for (q,d)=(2,2). For binary d=3,4 I independently bracketed the transverse root and obtained rational upper bounds -15906713/15625000 and -125361721/500000000 for gamma there. For d=5,6,7 the listed rational witnesses give gamma lower bounds 88976967/250000000, 7416389/250000000 and 11390161/125000000, with the transverse mode strictly negative. Replay: /tmp/opencode/pg-incidence-independent-certificate.py uses a 10^-9 grid, with (m/10^9)^b <= A^a for each bare power A^(a/b), and integer square roots for s. This also checked the needed quarter-power/log inequalities. For d>=8 the Taylor witness p=4/2^d gives gamma>1.12-8/2^d-1.022>0 and s(3^p-1)<1; for binary d>=5 the normalized derivative comparison is positive up to sigma<1/4. Strict lower negative type follows by applying the integral representation of x^r (0<r<1) to Gaussian kernels on the distinct Euclidean representatives, which also excludes larger exponents once a zero mode occurs. At p=0 the hollow unit off-diagonal matrix gives strict negative type. The centered Gram rank gives the two endpoint dimensions, and distinct representatives give strict positive definiteness at each bandwidth including the endpoint. At the binary contrast root gamma'(0)=2^d log(4/3)-2 log 2, and the witness gives p=O(2^-d); the quadratic remainder is O(2^d p^2), yielding the claimed error. The frozen checker was inspected, not executed.

## originality

FAIL

A distinct, published same-date Resultary record states the same theorem on the same graph, including the full all-bandwidth cutoff, the q=2,d=5 switch, strict Gaussian positivity and both endpoint nullities and embedding dimensions. This establishes equivalent coverage, not chronological priority or identity of the two records. The tighter binary asymptotic error displayed here is an immediate estimate from that record's Taylor argument, not an independent surviving claim.

## value

FAIL

The exact switch and endpoint rank are meaningful invariants of a natural incidence metric, but the separately available classification already supplies those facts. The only apparent increment, making the error in the leading binary scale explicit in big-O form, follows routinely from the same Taylor estimates and gives no new obstruction or geometric parameter. No independently valuable remainder is supported for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
