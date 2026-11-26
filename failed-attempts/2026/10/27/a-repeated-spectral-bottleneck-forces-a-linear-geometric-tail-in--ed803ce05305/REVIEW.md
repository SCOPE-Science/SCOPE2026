# Independent mathematical audit

## correctness

PASS

The fixed-n theorem is correct. For any j specified ascending adjacencies, contraction into blocks leaves (n-j)! permutations; summing over j selections gives the one-round factorial-moment coefficient (n-j)/(n j!). Subtracting the resulting one-round polynomials at zero gives p_(n+1,n+1)-p_(n,n)=-D_(n-1)/[n(n+1)(n-1)!]. Hence p_22=p_33=1/2, with all larger diagonal entries strictly smaller. The exact first-step time generating function gives F_2=z/(2-z), F_3=z(z+2)/(3(2-z)^2), and leading Laurent coefficient 2/3 in the normalization (1-z/2)^2. For n>=4 the multiplier at z=2 is 2/(1-2p_nn), so the stated recurrence follows; p_n3>0 ensures noncancellation. The survival transform (1-F_n)/(1-z) preserves the double-pole coefficient, with all other poles farther out, giving the claimed fixed-n remainder and the two base laws. Direct substitution gives c_4=6 and c_5=276/7. Frozen finite checks are corroboration only; the proof does not depend on them.

## originality

FAIL

A distinct Resultary record on exactly this chain already proves a stronger version: the same positive coefficient recurrence and repeated pole, an explicit constant term, and a sharper error bound. This is demonstrated coverage, not an inference from a title or date and not a verdict based on inaccessible literature.

## value

PASS

As mathematical content the fixed-state far-tail law exposes a genuine repeated transient eigenvalue in a natural merger process. The factor t corrects a purely geometric survival prediction and the coefficient makes the correction quantitative; the growing-initial-state CLT addresses a different question. This scientific usefulness does not represent an incremental contribution beyond the stronger indexed result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
