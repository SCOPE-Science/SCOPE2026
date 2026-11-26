# Independent mathematical audit

## correctness

PASS

Independence and E[e₀e₀ᵀ]=I give the squared Frobenius cost for each triple, with no centering assumption. With s_ab=⟨u_a,u_b⟩, trace cyclicity and P_j²=P_j give C_ijk=s_ij²+s_jk²+(s_ik−s_ij s_jk)². Row signs can be chosen so the two adjacent inner products are √q. Reflection and reversal reduce the 27 triples to the stated ten classes. Subtracting the dual bound gives zero on permutations, and the distinct repeat slacks are 2−3q/2, 1−q, 1−3q/2, 1−2q, (q+2)(1−2q)/2, (2−q)(1−2q)/2 and 2−3q−q², all strictly positive for 0<q<1/2. Thus arbitrary dependent schedules are covered, not just a non-exhaustive list of samplers. The uniform marginals give expectation 2q+q²/3 of the certificate, and equality forces zero mass on all repeat triples. The permutation marginal system has rank five; the kernel direction is (−1,1,1,−1,−1,1), so positivity yields precisely the indicated closed segment (endpoints have only three positive masses). For the unit path the normalized adjacent overlaps have squared value 1/4 on the contrast space. The IID average is 8/9+20q/27+2q²/9, yielding 235/216 versus 25/48 and relative improvement 49/94. Independent replay: python /workspace/replay/checks.py 5 computes every cost in nonorthogonal row coordinates, independently verifies all repeat slacks on the open interval by positive polynomial coefficients after q=t/[2(1+t)], and checks the nullspace and fractions. No guarantee is asserted for deterministic or anisotropic errors, relaxed rows, arbitrary frames, or other horizons.

## originality

PASS

The strongest indexed exact overlaps cover one-sweep permutation costs, notably the four-site path, and thereby cover the restricted marginal optimum at q=1/4. The supported distinct claim is the exact repeat-allowing three-marginal optimum for all q in the independent symmetric path frame, together with proof that repeats are strictly excluded from every optimum. Neither permutation costs nor bounds comparing selected samplers imply this assertion.

## value

PASS

A short-horizon schedule obeying fairness at each time could exploit temporal correlation or repeats. The theorem decides the full comparison by an exact dual bound, proves every optimal law avoids repeats, and quantifies the freedom among optimal schedulers. That is useful beyond evaluating known permutations or comparing reshuffling to IID; the contrast-space path example gives a natural and sharply delimited benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
