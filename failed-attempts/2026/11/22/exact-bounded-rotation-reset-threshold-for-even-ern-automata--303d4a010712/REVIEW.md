# Independent mathematical audit

## correctness

PASS

Tracking each initial state, its number of advancing b actions has a different residue modulo n, because all trajectories have the same final state and the same number of rotations. Thus one trajectory has at least n-1 advancing b actions. In each of the n-2 disjoint gaps between selected consecutive advancing b actions it must traverse from 0 to n-1 using at least n-1 rotations; avoiding aaa requires at least m-1 intervening b actions in each gap. This gives the claimed lower bound without any normal-form assumption. For attainment, the odd block rotates the preceding all-even set and then creates O_r, with the exceptional first block reaching the all-even set from the post-b image by removing the odd residues under repeated a^2b. In the even block the odd residues of O_r shift through at most n-3 before ab; after ab there is one odd residue 2r-1, which reaches n-1 only at the last a^2b and is mapped into an already occupied 0. The other residues rotate to E_r; E_(m-1)={0}. The length, the prohibition, the penalty, and the asymptotic ratio all follow. Independent replay python3 /workspace/independent_checks.py 4 exhausts the finite subset/run-length graph up to first singleton at even sizes 4 through 16 and gives 11,33,67,113,171,241,323; the proof, not the finite computation, covers all even n. Frozen verification and verify.py were inspected, not executed.

## originality

FAIL

A distinct indexed same-day record, 8a6293fb58a5, explicitly gives the exact same constrained minimum for all n>=3 and proves constructive attainment. On n=2m its floor disappears and it gives exactly 6m^2-8m+3, including the implied penalty and ratio. This is demonstrable coverage; the common date does not establish publication order or priority. The decision is not based on a search hit, an inaccessible paper, or a correctness objection.

## value

FAIL

The contiguous-rotation constraint is mathematically natural and the frozen proof is useful exposition, but the exact invariant, penalty and asymptotic ratio are covered, and the broader theorem already gives a constructive optimal witness. No separate motivated theorem about this particular witness or a new unconstrained parameter range is established. The even-only invariant therefore does not supply a distinct scientific result, and no viable repair is evidenced.

The dated certificate retains the supplied scientific assessment, sources and limitations.
