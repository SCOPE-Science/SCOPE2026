# Independent mathematical audit

## correctness

PASS

For W=0^a 1 0^b 1 0^c and root 0^x 1 0^(d-x), d=m-1, the first and last blocks force x<=a<=2x and d-x<=c<=2(d-x). The two remaining counts of middle zeros are nonnegative and sum to b, giving sufficiency and an interval of root indices. Applying the inequalities at both ends of a t-run leaves x from t-1 through d-2t+2, with (x-t+2)(d-x-2t+3) independent choices for a and c; their upper bounds ensure a+c<=2d. The convolution gives the binomial block count and the second difference isolates multiplicity t. The generating function, zero class and endpoint cases follow. The three exceptional terminal positive levels have O(1) counts and the rest give a Riemann sum against continuous test functions, yielding the atom and stated triangular law. The m/9 mean is conditional on R>0 as stated in the proof; the unconditional mean is asymptotic to m/12. Independent direct subsequence-coloring enumeration (branches/audit2.py and audit2.out) agrees for m=1..8, corroborating rather than proving the all-m formula. The bundled code's algebraic checks are m=1..100, not 100 new lengths beyond the finite DP range.

## originality

FAIL

Distinct same-day Resultary entry ee8a475fe7fb already contains the exact multiplicity spectrum, and indeed the more direct tail count and a contraction bijection. The spectra agree algebraically for every m and t. The additional rational generating function and scaled law are immediate consequences of that exact table (coefficient summation and rescaling), not independent new content. Publication order within that date is not established or used as evidence.

## value

FAIL

The complete inverse multiplicity distribution itself would be a worthwhile natural measure of shuffle ambiguity, but it is already supplied by the matching entry. The residual generating-function display, tail rescaling and conditional mean follow directly from its exact algebraic counts. They do not establish a separate useful unknown gap or warrant repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
