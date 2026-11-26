# Independent mathematical audit

## correctness

PASS

For gcd(t,m)=1, powering permutes primitive m-th roots, hence the monic quotient is integral. Expanding U_m/(1-x^m) gives the stated coefficient word in each block. There are d-1 length-t blocks and a final length-(t-d+1) block. The j-th cyclic word cannot vanish: vanishing modulo x^m-1 would imply Phi_m divides the partial numerator P_j(x^r) after cancellation of U_m, and thus Phi_m divides nonzero P_j by the permutation of primitive roots, impossible for j<d. The last block is occupied by monicity even if it is shorter than a period. Inserting m positions preserves the first supported offset, moves the last support forward by m, and inserts exactly a full cyclic multiset of gaps, including wraparound; end-to-start boundary gaps are unchanged. Iterating from t=m+r gives the formula; the prime identity applies since p does not divide m. Independently reconstructed coefficients by truncated cyclotomic Möbius products, with no periodic word or division by Phi_m. All eight base and first-difference rows match, as do higher-Q arithmetic checks including composite multipliers; the sets of lengths and N_8=2Q follow directly from the matched rows.

## originality

FAIL

A distinct published record, Resultary 0500051e2451, already covers the same general affine histogram and the complete m=15 table in a broader cofactor domain, with the same cyclic support construction. This is demonstrable equivalent coverage on the entire assigned domain, not merely a title match. Both records are dated the same day; the evidence does not resolve ordering or priority. The decision does not depend on an inaccessible ternary paper.

## value

FAIL

The entire gap histogram of a natural cyclotomic family is a meaningful invariant, but this particular submission contributes neither a new evaluated case nor a distinct structural or computational method beyond the directly matching broader law, cyclic slope proof and table already represented in 0500051e2451. A repeat verification is not a new mathematical finding, and no surviving valuable remainder was identified to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
