# Independent mathematical audit

## correctness

PASS

A forbidden window ending at an append has length four or six, so the last five characters and the used-hole bit suffice. Complement symmetry gives 16/40/16 states in the before/visible/forgotten blocks; initializing with actual valid prefixes avoids counting invalid suffix states. A hole-bearing suffix survives at most four further steps inside its block; configurations with the hole already forgotten use the same binary matrix Q as those before insertion. Thus the denominator divides det(I−zQ)^2, and with both binary resolvents the numerator degree is at most 5+15+15+1+4+1=41. Paths omitting a resolvent cost at most deg(D)=6 for its missing factor and do not increase the bound; the length<5 contribution has degree at most 16 after multiplication. Independent difference-bit states and principal-minor expansion gave det(I−zQ)=D. The pair-of-completions recurrence reproduces D²H through degree 42, including the entire asserted numerator and zeros above degree 18, enough by the degree bound. The binary graph has a single eight-state recurrent core, with cycles of lengths two and three and no other cyclic component; this gives the simple unique dominant Perron root. Exact polynomial gcd verifies noncancellation. The leading coefficient of the double pole is nonzero and must be positive by nonnegative counts and the strict gap to other poles. Extracting that pole gives the stated c and n factor.

## originality

PASS

The compatibility definition is prior, and the distinct cyclic result shares D and the growth base. The supported distinct result is the exact indexed one-hole linear enumerator with numerator N and squared denominator, and its positive double-pole prefactor. Neither bounds on factors in an individual partial word nor no-hole periodic counts give that statement.

## value

PASS

This is an all-length count for one erasure under a fixed natural local constraint. It quantifies erasure tolerance under both possible fillings, gives exact finite counts, and shows that the marked location contributes a genuine linear prefactor without changing the exponential base. The result supplies information absent from no-hole periodic counts, not just a rerun of the binary zeta calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
