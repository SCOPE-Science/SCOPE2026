# Independent mathematical audit

## correctness

PASS

Restriction of a kernel vector to an ordinary zero-forcing set determines it: when the currently known blue coordinates are zero, the equation at a forcing vertex has only one remaining nonzero edge coefficient. The prefix signs make the coordinate flips symmetric involutions and anticommute by changing the sign of the higher-index flip exactly once. The integer weight identity gives K²=a²I and all edge coefficients are nonzero. The two-layer matrix has kernel (x,−Kx/a) and rank 2^(d−1). Its diagonal is zero, so in full-cube parity order it is [0 B; Bᵀ 0] and each parity-supported kernel has dimension 2^(d−2). Restriction to each parity therefore gives the stated lower bound even for nonminimum forcing sets. A coordinate facet attains the total, and each cube-edge slide changes the signature; opposite facets give disconnectedness, while K2 admits one slide. Read both frozen checkers without running them. An independent sequential bitset enumeration (`python3 /workspace/independent_checks.py 2`) exhausted subsets through the minimum in dimensions 1–4; it found 2, 4, 30, 2360 minima and 1, 0, 0, 0 undirected minimum slides respectively. The all-dimension proof does not rely on enumeration or modular rank tests. Minor documentation issue: the frozen scripts use int.bit_count (introduced in Python 3.10), so their Python 3.8+ requirement is too broad; it does not affect the result.

## originality

FAIL

The prior AIM minimum-rank proof already constructs, for every d≥2, a real symmetric zero-diagonal cube matrix H_d of rank 2^(d−1). This is not merely the earlier scalar minimum-rank number: H_d already has the exact block structure needed to read off both parity-supported kernel dimensions. The ordinary forcing kernel argument then gives both parity lower bounds immediately, and their equality at minimum size rules out one-edge slides. The submitted integer coefficients are an alternative witness, but integrality is not needed for the claimed rigidity and no new integer-rank invariant is established.

## value

PASS

A parity signature explains why a minimum ordinary forcing configuration can be completely immobile under adjacent moves even where unrestricted exchanges permit motion. The distinction is structurally useful across cube dimensions, independent of any finite enumeration. It does not furnish an original result here because the earlier algebraic witness already yields it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
