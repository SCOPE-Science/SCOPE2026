# Independent mathematical audit

## correctness

PASS

PASS — The fixed point of 0→001,1→110 satisfies w(3j)=w(3j+1)=w(j), w(3j+2)=1−w(j). Its adjacent-difference c(j)=w(j) xor w(j+1) obeys c(3j)=0,c(3j+1)=1,c(3j+2)=1−c(j). For an antisquare of order k≥4, compare adjacent differences at distance k: if k mod3 is 1 or2, residues force a mismatch inside the length k−1 comparison window; hence 3|k. Substitution and complement-commuting blocks reduce order divisible by 3 to order k/3, and base orders1,2 are witnessed, giving exactly 3^t and 2·3^t. For start i=q·3^t+r, h=k/3^t∈{1,2}, the claimed c(q) tests characterize every residue r; c recursion and O(log N) discrepancy establish c=1 density1/2 and the exact fixed-t densities 1/6+3^(−t−1), 1/9+2·3^(−t−2). Independently generated ternary-digit-parity word length4000 and compared 74,500 start/order pairs (0≤i<500,1≤k<150); no mismatches and 1,049 true antisquare occurrences. The universal proof uses recursion, not bounded enumeration.

## originality

PASS

PASS — The final result is a necessary-and-sufficient entire antisquare-order spectrum, position-level criteria and per-order natural densities for the Mephisto Waltz word. Meleshko et al. §4.1 treat the exact same fixed point but a different pseudoperiodicity predicate. Baranwal et al. treat general antisquare avoidance; the 2026 same-word square and Abelian-cube spectra classify equal blocks or Parikh vectors, not adjacent complements. Exact complement order/positions/densities are not implied by the inspected primary statements.

## value

PASS

PASS — A naturally defined 3-uniform automatic word has a complete lacunary but infinite antisquare order spectrum and positive explicit starting densities even at arbitrarily large orders. The classification connects substitution, complement structure and ternary residue arithmetic at every scale, exceeding a finite factor census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
