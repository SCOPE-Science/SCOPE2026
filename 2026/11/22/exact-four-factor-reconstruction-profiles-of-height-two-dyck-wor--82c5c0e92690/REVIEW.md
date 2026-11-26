# Independent mathematical audit

## correctness

PASS

The height bound forces a unique sequence of primitive components 1(10)^(p−1)0. A length-four window is internal, crosses one boundary, or crosses two around a unit component. The stated table follows by counting the four adjacency types and interior unit components; in particular 1100, 1101 and 0011 recover b, c and d, and 0110 and 1001 separately recover the two endpoint bits. The endpoint bits determine the terminal length-three words, so successively summing over one-symbol extensions and adding a terminal indicator recovers all shorter counts. The all-unit word has no 1100 or 1101; n=1 only has this case. With k=L−d runs there are k−1 required nonempty separating groups, plus the specified endpoint groups. An extended component absorbs all surplus when c>0; otherwise surplus must go into an existing unit group, with none available precisely in the forced-all-long case. Independently summing the common tail first via the geometric factor (1−z^L)/(1−z), then subtracting z^3/((1−z)(1−z²)) for the exceptional surplus, gives the boxed numerator and all initial values. The numerator at 1 is 4, giving 1/[3(1−z)^4] as leading pole; primitive third and fourth poles survive (remainders 1 and −2z), and the possible polynomial part is constant, irrelevant for n≥1. Thus the least period is twelve and the leading term is n³/18. The observation capacity follows by taking one witness per attainable vector.

## originality

PASS

The exact feasibility and count for linear four-Abelian profiles on height-at-most-two Dyck words are distinct from the strongest inspected nearby findings: a strictly coarser unrestricted-Dyck profile, cyclic restricted binary profiles, single-pattern Dyck statistics, and general k-Abelian or sequence-profile machinery. Priority of statements actually shared with related records is not inferred from their dates.

## value

PASS

Height two is the first nontrivial bounded Dyck language. Joint four-factor observations already collapse an exponentially large family to cubic growth; unlike individual pattern averages, the tuple constraints tell which observation vectors are possible and construct witnesses. The exact period and zero-error code size are usable as benchmarks in structured reconstruction or in testing general constrained sequence-profile methods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
