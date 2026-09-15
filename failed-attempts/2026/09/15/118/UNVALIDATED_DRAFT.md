# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified geodesic growth rate of the compact tetrahedral Coxeter group [3,5,3]

## 1. Result (target claim, proved)

Let

W = W_[3,5,3] = < s1,s2,s3,s4 | si^2 = 1, (s1 s2)^3 = (s2 s3)^5 = (s3 s4)^3 = 1,
  (s1 s3)^2 = (s1 s4)^2 = (s2 s4)^2 = 1 >

with standard generating set S = {s1,s2,s3,s4}.
Let gamma_n = #{geodesic words of length n over S} and
gamma(t) = sum_{n>=0} gamma_n t^n.

(a) The Brink-Howlett geodesic automaton Geo(W,S) was constructed in certified
exact arithmetic: the small-root set Sigma has exactly 32 elements (Brink
closure in Q(sqrt5) with exact sign tests a^2 vs 5 b^2), and breadth-first
search on subsets of Sigma gives exactly 687 reachable states with 1560
labelled transitions. The transition table is `artifacts/automaton.json`
(states listed as sorted index subsets of Sigma in `artifacts/sigma.json`).

(b) The geodesic growth series is rational, gamma(t) = N(t)/D(t), with the
exact denominator (D(0) = 1)

D(t) = 1 - 2 t^2 - 3 t^4 - 12 t^5 - 5 t^6 + t^7 - 3 t^8 - 52 t^9 - 53 t^10
  + 193 t^11 + 336 t^12 + 123 t^13 + 1213 t^14 + 1445 t^15 - 1052 t^16
  - 1415 t^17 - 342 t^18 - 4894 t^19 - 16338 t^20 - 7742 t^21 + 8754 t^22
  - 42272 t^23 + 6863 t^24 + 59436 t^25 + 193203 t^26 + 161592 t^27
  + 520676 t^28 + 1102996 t^29 - 173320 t^30 - 1576072 t^31 - 304853 t^32
  - 3145870 t^33 - 3010134 t^34 - 6727412 t^35 - 6134140 t^36
  - 10211930 t^37 - 9970184 t^38 + 16106324 t^39 + 23051104 t^40
  + 12647882 t^41 + 73387171 t^42 + 97450127 t^43 - 21769250 t^44
  + 29913618 t^45 + 135387443 t^46 - 289556889 t^47 - 73718847 t^48
  - 919102387 t^49 - 891257748 t^50 - 961377922 t^51 + 1338595818 t^52
  - 1830253884 t^53 + 1354954805 t^54 - 2451359379 t^55 + 1454098665 t^56
  + 1628041104 t^57 + 6721037195 t^58 - 4106192429 t^59 + 11033893384 t^60
  - 1149416643 t^61 + 7752939095 t^62 - 3132258348 t^63 - 1249526389 t^64
  - 23514439142 t^65 + 22589950226 t^66 + 16930280117 t^67
  + 38213861314 t^68 + 53705725601 t^69 + 60920422667 t^70
  + 75049812409 t^71 - 19880508890 t^72 - 35608676726 t^73
  - 122153976313 t^74 - 213755884935 t^75 - 79996972070 t^76
  + 265342020558 t^77 - 19936577050 t^78 - 374243559176 t^79
  - 396155349682 t^80 - 538093145572 t^81 - 1270054434849 t^82
  - 490217979579 t^83 + 65965584494 t^84 + 210306275538 t^85
  + 1433390142637 t^86 + 644417572905 t^87 + 66308129480 t^88
  - 113137223422 t^89 - 832277170084 t^90 - 976886564231 t^91
  - 1274195344194 t^92 + 585095943819 t^93 + 1463273102257 t^94
  + 754997113763 t^95 + 759024378374 t^96 + 529133710993 t^97
  - 191005040337 t^98 + 172928322580 t^99 + 243895998894 t^100
  + 292792082486 t^101 + 609485370503 t^102 + 700312159025 t^103
  + 1242818757764 t^104 + 454734754071 t^105 + 660706727176 t^106
  + 722372575973 t^107 + 507587956489 t^108 + 304204205674 t^109
  + 391536893434 t^110 - 199691589818 t^111 - 29938461878 t^112
  + 262050679164 t^113 + 256509224867 t^114 + 58166355279 t^115
  + 10261949255 t^116 - 26030989957 t^117 + 44603498416 t^118
  + 161610136341 t^119 + 93355524344 t^120 - 67460508445 t^121
  - 85597674761 t^122 - 43184710273 t^123 - 10947350320 t^124
  - 7330506440 t^125 - 4612096540 t^126 - 5894299616 t^127
  - 3328821527 t^128 - 1762703137 t^129 - 351498622 t^130
  + 236970622 t^131 + 294489345 t^132 + 249798390 t^133 + 90182725 t^134
  + 16374314 t^135 - 2189972 t^136 - 5752630 t^137 - 1900866 t^138
  - 557184 t^139 - 80060 t^140 + 105370 t^141 - 31592 t^142 - 1292 t^143
  - 8360 t^144 - 1564 t^145 + 391 t^146 + 34 t^148

(full coefficient vector: `artifacts/Dint.json`; note the BM recurrence has
order 151 with vanishing top coefficients, true degree 148). The numerator
N(t) has degree 150 and is given in `artifacts/Nstrip.json`; gcd(D, N) = 1
(exact sympy gcd over ZZ), so no pole cancellation occurs at R.

(c) D has a unique smallest positive root R, rigorously isolated by

R in [lo, hi] =
[3772253225924090671345626501131268438344572017297769567 /
  7662477704329444291791735135751545918093695610918010880,
 75445064518481813426912530022625368766891440345955391341 /
  153249554086588885835834702715030918361873912218360217600],

of width < 7e-57, certified by exact-rational arithmetic: D(lo) > 0,
D(hi) < 0 (exact Fraction evaluations), D > 0 on [0, lo] by a certified
grid-plus-derivative-majorant cover (1001 cells on [0, 1000/2048] and 131
cells plus a monotone tail on [1000/2048, lo]), and D strictly decreasing on
the tail into hi (exact upper bound -5.22 on D'). Certificate values in
`artifacts/smallest_root_cert.json`; verification script
`scratch/smallest_root_cert.py`.

(d) The geodesic growth rate gamma(W, S) = 1/R satisfies

gamma(W, S) in [2.031273417, 2.031273419] (width 2e-9),

hence gamma(W, S) = 2.0312734181... certified. Two independent certificates:
(i) gamma = 1/R from the rational series (pole analysis: N(R) != 0 with
N(lo), N(hi) > 0 exactly and variation bound 2.2e-55 across the bracket;
all non-big SCCs are transient singletons without self-loops, so no other
pole has smaller modulus; the big SCC is aperiodic, period gcd 1, so the
dominant pole is simple/positive); (ii) exact-rational Collatz-Wielandt
bounds l Z <= A Z <= u Z with a positive integer vector Z (file
`artifacts/pf_right.npy`) giving spectral radius of the 518-state recurrent
block in [2.031273417, 2.031273419] (`artifacts/cw_cert.json`).

(e) Perron character: the recurrent (518-state) block of the automaton
transition matrix is irreducible and aperiodic (single cyclic SCC, cycle
gcd 1), so its spectral radius gamma(W,S) is a Perron number: a real
algebraic integer > 1 strictly dominating its conjugates. The hypothesis
irreducibility + aperiodicity is verified exactly (SCC decomposition +
period gcd, `scratch/per.py`).

(f) Comparison with word growth: by the Steinberg formula in the correct
slot 1/W(1/t) = S(t), i.e. W(t) = 1/S(1/t), with the pair contributions
A2 x2 / I2(5) x1 / A1^2 x3 and triple contributions H3 x2 / A2xA1 x2, the
Steinberg sum has numerator
(t - 1)(t + 1)(t^2 + t + 1)(t^4 + t^3 + t^2 + t + 1)^2 q(t) with the corrected
q(t) = t^10 - t^9 - t^6 + t^5 - t^4 - t + 1 (exact ZZ factorisation;
`artifacts/steinberg_check.json`). The word growth rate is omega(W, S) = 1/r
where r is the smallest positive root of q, isolated by a fresh exact Sturm
sequence (11 polynomials): no root in (0, lo_omega], exactly one in
(0, hi_omega] (V0 = 6, Vlo = 6, Vhi = 5; q(lo) > 0, q(hi) < 0 by exact
Fraction evaluation), giving omega(W, S) = 1.350980337716237...,
disjoint from the gamma interval. In particular

gamma(W, S) > omega(W, S), certified with gap >= 0.68 (2.03127 > 1.35098).

## 2. Methods and verification summary

- Exact field Q(sqrt5) with elements a + b sqrt5, a, b in Q; signs decided by
  comparing a^2 with 5 b^2 (exact, no floats). Bilinear form B with
  B(s2, s3) = -(1 + sqrt5)/4; reflections; Brink small-root closure with the
  strict test -1 < B(alpha, alpha_s) < 0. Reproduced |Sigma| = 32.
- Transition rule delta(D, s) = {alpha_s} union s(D) cap Sigma; dead (-1)
  when alpha_s in D. Validated on the A2 and infinite-dihedral controls
  (exact geodesic counts [1,2,2,2,0,...] and [1,2,2,2,...]).
- Recurrence: minimal order 151 stable across 300/400/500/600/700-term
  prefixes; independently certified by 750 exact convolution equations
  sum_{j} d_j c_{n-j} = 0 for n = 151..900 with 0 failures (integers with up
  to 278 digits). Counts to length 900 in `artifacts/counts900.json`.
- Word growth from the corrected Steinberg sum (pairs A2 x2 / I2(5) x1 /
  A1^2 x3, triples H3 x2 / A2xA1 x2) in the slot 1/W(1/t) = S(t), with
  W(t) = 1/S(1/t) verified against the faithful reflection representation:
  matrix-BFS element counts 1, 4, 9, 16, 26, 41, 62, 90 match the corrected
  W(t) coefficients exactly (`artifacts/steinberg_check.json`). Omega bracket
  by a fresh exact degree-10 Sturm sequence.
- Root isolation: exact Fraction bisection to width 6.6e-57; smallest-root
  proof by certified grid cover + monotone tail; omega bracket by exact
  Sturm sequence (degree 10). All sign claims are exact rational evaluations.

## 3. Limitations and uncertainty

- The automaton construction follows Brink-Howlett; the scripts implement the
  standard rule delta(D,s) = {alpha_s} U s(D) cap Sigma with the descent
  condition alpha_s not in D. Correctness of this rule relative to the
  literature is assumed (validated on A2 and I2(inf) controls), not re-proved.
- The BM-discovered recurrence is certified as *satisfied* by 750 exact
  equations, but minimality/finiteness of the linear recurrence is a
  computational fact (rationality follows from automaton finiteness, which is
  proved by the closed 687-state BFS, not from BM).
- Perron: the "Perron number" conclusion uses the standard theorem that the
  spectral radius of a primitive nonnegative integer matrix is a Perron
  number; primitivity (irreducibility + aperiodicity) is computed exactly,
  and the characteristic-root dominance is the classical Frobenius theorem.
- No literature search was used; originality of the numerical certificate is
  not claimed beyond the computation itself.

## 4. Artifact inventory (verification-critical)

- artifacts/automaton.json: 687 states, transition table.
- artifacts/sigma.json: 32 small roots.
- artifacts/counts700.json / counts900.json: geodesic counts to length 900.
- artifacts/Dint.json / Dstrip.json: denominator coefficients.
- artifacts/Nstrip.json: numerator coefficients.
- artifacts/Rbracket.json / omega_bracket.json (corrected q, Sturm values) /
  steinberg_check.json: isolating intervals and Steinberg audit.
- artifacts/smallest_root_cert.json: smallest-root certificate values.
- artifacts/cw_cert.json + pf_right.npy: Collatz-Wielandt certificate.
- scratch/*.py: all computation scripts (co/black-box record).
