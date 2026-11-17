# Independent mathematical audit

## correctness

PASS

For all d>=1,m>=2,0<=r<m, the count f(z)=binom(z,d) mod m has least period P=product_{p^a||m}p^{a+floor(log_p(d))}: Vandermonde expansion and unitriangular binomial-basis evaluations give the necessary-and-sufficient congruences binom(T,j)=0 for 1<=j<=d; Lucas and p-adic valuation prove the prime-power criterion. The complete DFA (zeros mod P, scattered count mod m) is reachable via 0^d 1^c 0^(Z-d). For two hypothetically equivalent states, independent numbers of ones between P successive zero counts generate a subgroup H in (Z/m)^2. Acceptance equivalence and both surjective projections force H to be the graph of a cyclic-group automorphism a; the d-th forward difference gives a=1, the least period gives equal zero residue, and varying count increments gives equal count residue. No finite extrapolation. Independently minimized 35 d,m cases (1<=d<=5,2<=m<=8), all matching mP.

## originality

PASS

Earlier 2026-10-26 exact prime-modulus DFA staircase is a direct special case m=p: p^(2+floor(log_p d)); its full RESULT.md does not treat prime powers p^a (a>1) or composite moduli. The reviewed theorem gives a genuinely stronger exact all-m state complexity and new modular p-adic/surjective-subgroup distinguishability; the older 2011 trie automaton may contain a hidden equivalent and its full text was unavailable.

## value

PASS

The complete minimal DFA complexity of a natural modular scattered-subword language is an exact all-parameter invariant. Composite moduli introduce non-field p-adic period phenomena genuinely outside the earlier prime-only classification; sharp minimality is useful for automata and modular subword statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
