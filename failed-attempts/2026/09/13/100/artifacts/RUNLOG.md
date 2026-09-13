# Reproducibility log (exact commands, all run in workdir, gcc -O2, 32-core box)

1. `gcc -O2 -o work/enum27 work/enum27.c`
   `./work/enum27 > output/artifacts/qprofiles.txt`
   Result: NODES=29971377 P12=3744 SURVIVORS=3744 TIME=6.0s
   Meaning: quotient profiles m: F3^3->{0..3}, sum 16, sumsq 22, all 13 plane-coset
   triples a permutation of (3,6,7), all 26 nontrivial autocorrelations = 9.
   NOTE: every P1+P2 passer also passed autocorr (P12=3744=SURVIVORS).

2. `python3 work/symreps2.py` (GL(3,3)-orbit reduction via 4 generators + BFS)
   Result: 3744 profiles fall in 3 orbits; reps in output/artifacts/qprofile_reps.txt.

3. `gcc -O2 -o work/liftdirect work/liftdirect.c`
   `./work/liftdirect "<rep>"` for each of the 3 reps (abelian C3^4 fiber layout):
   TESTED=1594323 (= prod_q C(3,m[q])), DS-FOUND=0 for all three. (~1s each)

4. `gcc -O2 -o work/nonab_liftdirect work/nonab_liftdirect.c`
   `./work/nonab_liftdirect G1 "<rep>"`, `./work/nonab_liftdirect G2 "<rep>"` (3 reps each):
   TESTED=1594323, FOUND=0 in all 6 runs. Group tables self-check identity/inverse
   (FATAL on failure); associativity cross-checked in Python (work/verify_nonab.py, 3000 triples).

5. `gcc -O2 -o work/enum_c9c3 work/enum_c9c3.c`
   `./work/enum_c9c3 > output/artifacts/qprofiles_c9c3.txt`
   Result: NODES=1063299948 P12=5202144 SURVIVORS=0 TIME~67s.
   Meaning: NO quotient profile exists on Q=C9xC3 (all 4 order-9-subgroup triple
   constraints + sum/sumsq), after autocorrelation filter nothing survives — kills DS in
   H=C27:C3 (verified presentation, |Z|=9, S=<x^9> central, abelian Q with orders
   {1:1,3:8,9:18}) and in C9:C9 (verified presentation, |Z|=9, abelian Q, same orders).

6. `python3 output/artifacts/verify_quotient_layer.py` — independent Python re-verification
   of P1/P2/P3 on all 3 reps: ALL CHECKS PASSED.
   `python3 output/artifacts/fiber_triple_proof.py` — fiber-triple classification,
   reversibility obstruction, absolute-point count, normalized-polarity lemma: all print.

7. Positive controls: work/verify_known.py finds the (16,6,2) Hadamard DS (E=0) with the same
   SA machinery (search code sound); work/control93.py confirms the exact DS tester accepts a
   known DS (tester sound — no false negatives by construction: full difference enumeration).

Boundary (NOT claimed): nonabelian groups of order 81 whose order-27 quotients are all
nonabelian (maximal-class / class-3 groups, e.g. Heis27:C3-type with twisted action) are not
covered by this pipeline; abelian groups beyond C3^4 need no DS analysis for the polarity
question by the reversibility theorem (uses Kantor/Jungnickel correspondence, cited).
