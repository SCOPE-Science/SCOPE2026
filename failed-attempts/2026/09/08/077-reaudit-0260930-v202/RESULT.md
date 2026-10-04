# Exact Ehrhart, h*, and non-IDP certificates for three 6D reflexive simplices on the line a(t)=(1,1,2,2,2,t)

## Context

After Mustaţă–Payne (even dimensions > 5) and Payne (all dimensions > 5)
disproved general Gorenstein h*-unimodality, the live question is the
Hibi–Oda / Brenti conjecture: IDP reflexive (Gorenstein) implies unimodal h*.
Braun–Davis–Solus (arXiv:1608.01614) proved this for the natural two-part
Payne generalization q=(r^m,s^x) (Theorem 4.1) and explicitly extended
investigation to a broader simplex class as new results plus open problems
(Section 5, Questions 5.1–5.4). Dimension 6 is the lowest dimension admitting
Gorenstein non-unimodality. The present record closes exact data on a
pre-committed Payne-generalizing 6D line at that threshold.

## Definitions

Fix dimension n = 6. For a = (a_1,...,a_6) in positive integers put

    P(a) = conv{e_1,...,e_6, v_0},  v_0 = -(a_1,...,a_6),

with e_i the standard basis vectors. Write Q = 1 + sum a_i. Up to the standard
identification this is the simplex of weight system (1,a_1,...,a_6) with total
weight Q; its normalized volume is Q.

P(a) is reflexive (origin the unique interior lattice point, all facet
distances 1) iff a_i | Q for every i. The seven facets are S(x) := sum x_i <= 1
and, for each i, sum_{j != i} x_j - (Q/a_i - 1) x_i <= 1, integral iff a_i | Q.

Pre-committed line (fixed before counting):

    a(t) = (1,1,2,2,2,t),  Q(t) = 9 + t.

Reflexivity needs 2 | Q (t odd) and t | Q, i.e. t | 9. The divisor-closed
admissible set is t in {1,3,9}, Q in {10,12,18}. Weight systems are
q = (1,1,1,2,2,2,t): t = 1 is the two-part control case (1^4,2^3), while
t = 3,9 are genuinely three-part, outside the Braun–Davis–Solus two-part
theorem and inside their stated open regime.

## Result

For the three simplices P_1, P_3, P_9:

| member | Q (norm. vol) | |P∩Z^6| | |2P∩Z^6| | Ehrhart L(k) (k=0..6) | h* | unimodal? | IDP? |
|---|---|---|---|---|---|---|---|
| t=1 | 10 | 8 | 37 | 1,8,37,128,366,911,2038 | (1,1,2,2,2,1,1) | yes | NO |
| t=3 | 12 | 8 | 37 | 1,8,37,130,380,967,2206 | (1,1,2,4,2,1,1) | yes | NO |
| t=9 | 18 | 9 | 46 | 1,9,46,172,522,1360,3151 | (1,2,4,4,4,2,1) | yes | NO |

Full tallies L(0..9): t=1: 1,8,37,128,366,911,2038,4187,8023,14506;
t=3: 1,8,37,130,380,967,2206,4607,8947,16354;
t=9: 1,9,46,172,522,1360,3151,6651,13015,23923.

Exact Ehrhart polynomials (interpolated from k=0..6, verified at k=7,8,9):

- t=1: L(k) = 1 + (29/12)k + (211/72)k^2 + (25/24)k^3 + (5/9)k^4 + (1/24)k^5 + (1/72)k^6.
- t=3: L(k) = 1 + (49/20)k + (353/120)k^2 + k^3 + (13/24)k^4 + (1/20)k^5 + (1/60)k^6.
- t=9: L(k) = 1 + (51/20)k + (129/40)k^2 + (11/8)k^3 + (3/4)k^4 + (3/40)k^5 + (1/40)k^6.

In each case the leading coefficient times 720 equals Q. All three h*-vectors
are palindromic (as required for reflexive 6-polytopes) and unimodal
(h_0 <= h_1 <= h_2 <= h_3). Yet none of the three is IDP; explicit lattice
points in 2P not expressible as a sum of two lattice points of P:

- t=1: z = (0,0,-1,-1,-1,0);
- t=3: z = (0,0,-1,-1,-1,-1);
- t=9: z = (0,0,-1,-1,-1,-4).

Consequences: (i) within this segment "IDP => unimodal" holds vacuously (no IDP
member); (ii) the segment separates the converse: three certified
unimodal-but-not-IDP witnesses in dimension 6.

## Proof / evidence

Exact integer arithmetic throughout; two independent code routes plus an
auditor recount.

- Facet membership: x in kP(a) iff S(x) <= k and
  a_i(S(x)-x_i) - (Q-a_i)x_i <= k*a_i for all i; equivalently
  Q*x_i >= a_i*(S-k). Counter and verifier implement this test independently.
- Ehrhart counts: exact S-slice stars-and-bars summation (shift bijection
  proved in DRAFT) cross-checked by tight-box facet brute force (k=1,2,3),
  by an independent bounded-composition recount (k=1..9, all members matched),
  by Vandermonde QQ interpolation on k=0..6 with prediction checks at k=7,8,9,
  and by the volume check 720*c_6 = Q.
- h*: two agreeing routes — triangular solve of
  L(k) = sum_{j<=k} h_j*C(k-j+6,6) and the reflexive-simplex age histogram
  h_j = #{b in [0,Q) : age(b)=j}, age(b) = (1/Q)*sum q_i*(b*q_i mod Q);
  agreement plus palindromicity and sum(h*) = Q.
- IDP: full simplicial-cone fundamental-parallelepiped criterion (all Q <= 18
  representatives per member, fold-sumset DP) agreeing with exhaustive 2P
  pair-splitting over the full enumerated S1/S2 sets; full per-point 2P tables
  (37+37+46 rows) stored; each witness above verified in 2P with zero P+P
  splittings. One bad 2P point suffices to prove non-IDP.
- Replay: output/artifacts/verify.py from committed weights only prints
  ALL VERIFY_OK; independently re-ran during audit.

## Limitations

- The segment-wide "IDP => unimodal" verdict is vacuous (0 IDP members), so no
  advance on the Hibi–Oda forward direction beyond vacuity here.
- No non-unimodal member was found.
- Claims are confined to t in {1,3,9} above; methods (age formula,
  parallelepiped IDP criterion, Ehrhart interpolation) are classical — the new
  content is the closed decision data for this pre-committed open-regime
  segment.
- t=1 lies in the Braun–Davis–Solus two-part family, so its implication
  instance is covered by their theorem; its exact polynomial/vector/witness and
  the t=3,9 out-of-theorem data are the reusable novelty.

## Reproducibility

- output/artifacts/compute.py — exact counter + interpolation + age + IDP tables.
- output/artifacts/results.json — tallies L(0..9), Ehrhart coefficients, h*,
  parallelepiped tables, full 2P decomposition rows, witnesses.
- output/artifacts/verify.py — independent replay from committed weights only:
  tight-box facet enumeration (k=1,2,3), fresh Vandermonde solve with k=7,8,9
  prediction, age histogram, cone-membership of representatives, full 2P table
  recheck and witness non-splitting. Prints ALL VERIFY_OK.
- Run: python3 output/artifacts/verify.py (seconds).

## References

- Braun–Davis–Solus, Detecting the Integer Decomposition Property and Ehrhart
  Unimodality in Reflexive Simplices, arXiv:1608.01614 (two-part theorem +
  open broader class).
- Braun–Davis, Ehrhart series, unimodality, and integrally closed reflexive
  polytopes, arXiv:1403.5378 (integrally closed operations).
- Mustaţă–Payne / Payne (Gorenstein non-unimodality above dimension 5).
- Konoike, A new class of magic positive Ehrhart polynomials of reflexive
  polytopes, arXiv:2409.16648 (magic positivity, different families).
