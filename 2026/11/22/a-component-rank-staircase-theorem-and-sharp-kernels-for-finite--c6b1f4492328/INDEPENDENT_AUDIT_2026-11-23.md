# Independent mathematical audit

## correctness

PASS

For the corrected full finding in /workspace/repairs/2/RESULT.md. The original scope assertion that all ranks of finite hosts are finite fails for arbitrary local hereditary classes. If the base class has only the empty structure and one singleton type, a marked singleton has no challenge, hence satisfies every finite threshold; so does the empty position of the singleton host. Indeed two singleton components have global rank 2, and capping the local ranks at host order would wrongly reject this. The repair instead takes local values in the extended nonnegative integers. For each finite threshold r, every move is local to one occupied class or starts a fresh singleton class. Necessity: arbitrary occupied-class challenges must admit local replies at threshold r-1; a fresh challenge requires using an unused class with original local rank at least r while the remaining classes meet r-1,...,1. Sufficiency: use the local rank reply or consume the highest unused local rank, respectively; the other requirements survive at the lower threshold. This proves the induction including vacuous terminal local positions. Repeating fresh challenges bounds the global rank by the number of unused classes. Induced embeddings of the principal local kernels must go to distinct named E-classes because these kernels are nonempty and E is reflected. In chains, splitting a gap into two gaps of size at least 2^(r-1)-1 is exactly the recursion giving 2^r-1; incomparability separates chains. Summing the ladder gives N_r=2^(r+1)-r-2. One excess point lengthens one chain or adds a singleton; only the latter has a size-two automorphism group. The resulting count is (r+1/2)(N_r+1)!, and the next threshold needs more than one extra vertex. Independent direct recursion by extension relation signatures agreed with the scalar formula in 8,800 positions (all markings through size 8; empty markings through size 12), and gave minima 1,4,11, next-order type counts 2,3,4 and labelled counts 3,300,1676505600. This was a bounded working check, not a preserved replay script or proof of generality; the frozen checkers and their reported outputs were inspected, not run.

## originality

PASS

Best of knowledge for the repaired claim. The rank recursion, single-chain gap threshold, and the pure-equivalence staircase are antecedents. The surviving new point is the exact transfer for arbitrary compatible local hereditary classes, including possibly infinite local capacities, and its simultaneous application to marked unions of chains. This does not rely on claiming priority for the pure-equivalence special case or for the one-dimensional gap lemma.

## value

PASS

The formula separates local extension capacity from the consumption of independent classes, so it turns a marked game into local rank computations and yields a constructive principal-kernel transfer. This has content even when local ranks are infinite but global ranks are finite. The chain case gives a usable simultaneous test at every marked position and a sharp minimum and next-order classification, not just a re-count of the known single chain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
