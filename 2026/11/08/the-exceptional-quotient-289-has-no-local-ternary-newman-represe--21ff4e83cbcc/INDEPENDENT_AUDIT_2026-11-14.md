# Independent mathematical audit

## correctness

PASS

Every finite ternary 0/1 digit representation of p(3)=289q(3), with constant digits both one, induces integral carries c_{i+1}=(c_i+289q_i-p_i)/3 starting and ending at zero, bounded in [0,144]. Independently reconstructed all legal transitions: exactly 32 reachable states decompose into 20 returnable live states and 12 forward-trapped dead states. On all 26 live-to-live edges, the superincreasing weights (96,32,11,4,1) uniquely encode the five latest q bits, shift by one step and enforce p_i=q_i-q_{i-2}-q_{i-3}+q_{i-4}+q_{i-5}. Initial zero encoding and finite-state induction give polynomial identity p=(1-x^2-x^3+x^4+x^5)q at arbitrary length, not an extrapolation from finite sampled paths. Verified R(3)=289 and explicit p(3)=80920=289*280.

## originality

PASS

Anders, Dawsey, Reznick and Sisneros-Thiry (2023) explicitly mark multiplier 289 as unknown local/universal in their table; their universal-only families and the specific 100 theorem do not force the 289 identity. The current Nov 8 Resultary exact-title match is the audited item, not earlier coverage; published October 25 nearby ternary-quotient examples have other multipliers. Best-of-knowledge originality survives primary comparison.

## value

PASS

The multiplier 289 was an explicitly unresolved exceptional entry in a primary published classification. Establishing all-degree universal divisibility, with a finite 32-state trapping certificate and stronger fixed factor R(x), resolves a motivated natural exact question. The single-number scope is mathematically justified by the prior open case, not an arbitrary tiny enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
