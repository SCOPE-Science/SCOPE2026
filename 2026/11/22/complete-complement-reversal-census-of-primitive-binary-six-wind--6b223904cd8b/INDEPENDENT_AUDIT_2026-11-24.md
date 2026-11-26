# Independent mathematical audit

## correctness

PASS

A cyclic host has 54 starts and one occurrence of each primitive window; overlap identifies it with an Euler tour on the 5-bit prefix/suffix graph. Rotating a window one bit bijects incoming and outgoing edges, and the edge 000001 fixes the rotation uniquely. An independent rebuild via equality to nontrivial cyclic rotations and exact rational Gaussian elimination obtained the rooted cofactors 389120 and 320, degree counts (10,22) and (5,11) at degrees one and two, and 13 quotient edges with odd voltage. Positive cofactors and balance ensure Eulerian connectivity; the BEST factorials are all one. Complement acts freely on edges and vertices. A complement-fixed host must be complemented by the half-turn: two applications give a period, forbidden at any nonzero shift by window uniqueness. Its first half traverses the 27 distinct edge classes exactly once. Conversely every quotient Euler tour has odd total voltage, so its lift starting at 000001 reaches the complement sheet and its second lap is the complementary first lap; this is a bijection with the complement-fixed classes. The independent list contains four palindromes and six reverse-complement palindromes. Either reflected operation acts on window starts by i -> s−i−5 modulo 54 for some s, and hence has at most two fixed starts; every relevant symmetric window would require one since windows are unique. Burnside then gives 97360 orbits; exactly 160 have size two and 97200 size four. The frozen scripts were inspected but not executed. The computation is exact for this window set, not an all-length census.

## originality

PASS

The result uses classical Euler-tour counting; its distinct part is the exact whole primitive-window census with all complement and reflection stabilizers. The nearest inspected constructions use different window predicates, and the nearby length-six orientable and deficit records count different hosts. No inspected theorem determines the four fixed-point numbers without the primitive-graph, quotient-voltage and reflection analysis. Full texts of two plausible secondary sources were inaccessible, so historical priority is not certified.

## value

PASS

Six is the first binary window length at which two distinct proper nontrivial divisor periods must both be excluded. The exact test case quantifies the effect of that mixed restriction and separates the nonempty complement-fixed stratum from the two impossible reflections. The quotient-lifting argument explains the symmetry count, so this is more than a raw enumeration of a convenient small graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
