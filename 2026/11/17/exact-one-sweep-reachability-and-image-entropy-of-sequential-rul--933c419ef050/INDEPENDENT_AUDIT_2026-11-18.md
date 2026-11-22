# Independent mathematical audit

## correctness

PASS

PASS: Rule30 f=l XOR(c OR r) yields d_i=y[i-1] XOR y_i = x_i OR x[i+1] for 1<=i<=n-2, while final difference equals x[n-1] OR y0. P=E_d1...E_d[n-2] is a Boolean relation between old x1 and x[n-1]. The first equation x0 OR x1=y0 XOR x[n-1] produces three mutually exclusive viable endpoint tests, and a passing relation path together with x0 chosen as required constructs a genuine inverse. All 12 Boolean relation states are exactly closed under E0/E1. Weight w(P)=P00+(P01 OR P11)+(P00 OR P01 OR P10) counts valid (y0,dlast) labels, not predecessor multiplicity. Hence I_n=e0^T T^(n-2)w. The full 12-component vector T^2(T^3-2T^2+T-I)w=0 was independently recomputed with integer arithmetic, proving the recurrence for all allowed n and the rational GF from initial values. Leading root of λ^3-2λ²+λ-1 is 1.754877..., other roots smaller in modulus. Exhaustive independent sweeps n=3..11 give exactly 4,8,14,25,44,77,135,237,416. No claim for later sweeps or arbitrary permutations.

## originality

PASS

PASS (qualified): rule-specific one-pass image language and all-n enumerator are mathematically different from synchronous Rule30 predecessor studies, periodic-state order-independence and Wong sequential Rule30 illustrations. Literature retrieved neither identifies exact 12-relation endpoint census nor gives the one-sweep image series; same entropy cubic as sequential Rule184 does not mean same image sets.

## value

PASS

PASS: determining which states are reachable by one deterministic sweep of paradigmatic chaotic Rule30, plus exact entropy and effective inverse, is a mathematically natural image/language invariant. The scan-origin boundary test and all-length generating formula characterize an information-loss mechanism not furnished by finite simulations or known parallel Rule30 images. Usefulness does not require universality or multiple-sweep claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
