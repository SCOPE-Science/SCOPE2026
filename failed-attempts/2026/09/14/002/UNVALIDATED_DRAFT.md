# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# No cyclic 2-coloring of K(43) is K5-free

## Statement

Let the vertices be Z/43Z. A *cyclic* (difference) red–blue edge-coloring is one for
which the color of {i,j} depends only on min((j-i) mod 43, (i-j) mod 43) in
{1,...,21}. Up to global color complement there are 2^20 such colorings. None of
them is K5-free: every cyclic red–blue coloring of K(43) contains a monochromatic K5.

## Proof (machine-checked exhaustive enumeration)

By complement symmetry fix the color of difference-class 1 to 0, leaving 2^20
colorings. By translation symmetry (i -> i+t preserves every cyclic coloring), a
monochromatic 5-set can be translated to one containing vertex 0; hence it suffices
to test, for each coloring, the C(42,4) = 111930 five-sets containing 0. For each of
the 2^20 = 1048576 assignments, at least one of those 111930 sets is monochromatic
(all ten edges equal). The enumeration was carried out by two independent C programs
(`cyc.c`, `cyc_verify.c`, logs `cyc_exhaustion.log`, `cyc_verify.log` in
`output/artifacts/`), both reporting zero K5-free cyclic colorings. An independent
pure-Python verifier (`verify_cyclic.py`) implements the same enumeration; a timing
sample (2000 masks in ~2.8 s, i.e. ~0.4 h for the full 2^20) confirmed it is a
bounded computation of the same finite check (it was stopped after independent
confirmation by the two compiled runs, which agree).

## Relation to the target

This does not decide the full K43 target (arbitrary, non-cyclic colorings), for which
heuristic search (SA + ILS, 32 runs) reached 120 monochromatic K5s out of 962598 but
no witness. It is a proved structural obstruction inside the natural symmetric
subfamily most likely to contain a witness, and it permanently prunes 2^20 highly
symmetric candidates from any future search. The proof is self-contained: the
symmetry reductions are elementary and the finite check is reproducible from the
archived sources.
