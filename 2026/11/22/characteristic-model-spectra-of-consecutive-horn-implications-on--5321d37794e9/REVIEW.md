# Independent mathematical audit

## correctness

PASS

For a last missing path atom i, any adjacent pair in its prefix would force i, and filling the suffix cannot force an earlier atom. Maximal omission of i is therefore exactly maximal independence of the prefix with the suffix filled. The independent-domination recurrence with initial polynomials 1,u,2u gives the stated weighted prefix series; substituting u=1/q and summing over the last omission gives the path denominator and numerator. On a ring an adjacent pair forces the full set. A proper independent set has one cover if it is maximal (the full set), or exactly as many covers as one-vertex independent extensions otherwise. In a gap of g zeros the number of extensions is max(g-2,0); the empty set is excluded for n>=3. With f=qt^2+q^2t^3, labelled pointing of ordinary gaps gives t d/dt[-log(1-f)], and pointing by the unique length-four block gives t d/dt[q^3t^4/(1-f)]. Removing 2qt^2 gives the claimed ring series. In particular the first three ring polynomials are 3q^2, 2q^2+4q^3, and 5q^3. At q=1 the dominant pole tau solves tau^2+tau^3=1 and is unique on its modulus by equality in the triangle inequality and gcd(2,3)=1. The simple-pole path constant is tau(1+tau+tau^2)/[(1-tau)(2tau^2+3tau^3)] = 2.945975616525679; the double-pole ring coefficient is tau^4/(2tau^2+3tau^3) = 1/(2rho^2+3rho). Fibonacci closed-set counts follow from independent prefixes and independent cycle sets respectively. The phrase 'zero-adjacent-free prefix' in Step 6 is a slip for 'prefix with no adjacent ones'; the earlier normal form, count and checker all use the latter.

## originality

PASS

Pass for the exact Horn classification and the resulting size-refined path/ring contrast, especially the ring term with one undominated vertex. Neither the generic maximal-omitter lemma nor the already-known weighted maximal-independent-set polynomials is itself a new result.

## value

PASS

Closing a single local rule system into a ring changes its irreducible-model growth by a factor of order n even though the leading exponential rate is unchanged. The classification locates the cause exactly in the unique undominated vertex and gives the size distribution of the canonical representation, not just a growth estimate or a renamed Padovan/Perrin count. This is useful for comparing representation sizes in these two explicit systems; it is not a general Horn tractability result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
