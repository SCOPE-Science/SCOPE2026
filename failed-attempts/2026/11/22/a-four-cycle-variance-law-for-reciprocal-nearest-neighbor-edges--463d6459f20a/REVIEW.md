# Independent mathematical audit

## correctness

PASS

The finite simple graph has one common atomless weight law on independent unordered edges, so every strict edge order has equal probability. Write N_e for the closed incident-edge neighborhood. The marginal is 1/|N_e|; adjacent candidate edges are mutually exclusive. For disjoint e,f, the smallest weight on N_e union N_f must be e or f if both succeed. Conditioning on it being e, f must be the first-ranked member of N_f in the remaining uniform order, giving contribution 1/[b(a+b-h)] with a=|N_e|, b=|N_f| and h=|N_e intersection N_f|. With f smallest the contribution is 1/[a(a+b-h)]. Subtracting 1/(ab) gives the claimed covariance, and the zero pairs come from disjoint determining weight sets; this yields the induced-matching characterization of mutual independence. In a triangle-free d-regular host the marginal variances cancel the touching-pair contribution. Each potential cross edge between disjoint candidate edges has exactly (d-1)^2 choices of those candidates; no triangle ensures they are disjoint. Cross edges themselves form a matching, so only h=0,1,2 occur. Exactly two opposite-edge pairs per four-cycle have h=2, giving N_2=2c_4 and N_1=m(d-1)^2-4c_4. Substitution gives the displayed baseline and positive coefficient, including d=2, and c_4(K_{d,d})=binom(d,2)^2 gives the example. Independent exact order enumeration passed for all 76 labeled host graphs of orders 0 through 4 (1,977 graph-order instances) and for C4, C5, C6 and C8, with variances 2/9, 2/9, 4/15 and 16/45 respectively. Frozen verifier inspected, not executed. Finite checks corroborate, not establish, the universal result; replay: python3 /workspace/evidence/reciprocal_exact.py.

## originality

FAIL

The frozen central pairwise identity is Baldi and Rinott's 1989 local-maximum covariance law on an arbitrary vertex-labeled graph, applied to the host's line graph and with label order reversed. Their proof of Proposition 3, p. 1650, Eq. (3), explicitly gives the three distance regimes and exact overlap-dependent covariance summands for the variance. The regular triangle-free four-cycle formula is a direct specialization of that variance identity: two elementary overlap counts give all the required multiplicities, and the regular-degree cancellation is already stated there. A separate printed four-cycle formula is not needed for coverage.

## value

FAIL

The randomized observable and four-cycle recovery are natural, but the exact result is mechanically supplied by the classical common-neighbor variance identity on the line graph and elementary opposite-edge counting. The frozen record does not give a further non-implied probabilistic or structural result. The correct calculation could be an illustrative corollary, but that is not a surviving new exact finding under the stated standard. No repair is proposed or delivered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
