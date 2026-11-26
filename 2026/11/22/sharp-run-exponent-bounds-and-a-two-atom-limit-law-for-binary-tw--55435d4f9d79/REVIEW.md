# Independent mathematical audit

## correctness

PASS

For a finite linear binary word with exactly two ones, period one gives precisely the qualifying maximal constant blocks. Any run of period p>1 has a one and repeats it at distance p (a factor of length at least 2p meets each residue at least twice); thus both ones are used and p=b+1. Its maximal p-periodic interval extends their span by min(a,b) and min(c,b); at another extension beyond either cap a third one would be required. If length is at least 2p it has no smaller period by the same residue argument. For n≥8, with P=floor((n+1)/3), a non-unary run contributes at most 3−1/p for p≤P and at most n/p for p>P, while the constant-run part is n−2 minus the number of singleton zero gaps. The p>P case is strictly below the claimed maximum because n≤3P+1; equality in the other case forces p=P and both outer gaps at least P−1, yielding the full displayed list. At lengths 4–7, period 2 loses a singleton gap, period 3 contributes at most 2 for n=6 and cannot improve on 7 at n=7 (either a singleton or a truncated outer extension); adjacent ones followed by zeros attain n. For uniform labeled position pairs the normalized gaps converge by Riemann sums to simplex density 2, with zero/one gaps negligible. The non-unary condition is exactly a+c≥b when b≥1. In the limit B>1/2 gives the atom −2 of mass 1/4, and A,C≥B gives the atom 1 of mass 1/3. For 0<t<1 the tail is the integral of 2[1−(1+2t)B] over 0<B<1/(2+t), giving 3/(2+t)^2 and density 6/(2+y)^3. There is no leftover mass or atom at zero. Integrating this tail and the atom at −2 gives mean 0 and second moment 6 log(3/2)−1; uniform boundedness of the centered quantities ensures moment convergence. Replay python3 /workspace/branches/independent_checks.py 4 exhausts a separate bounded slice (969 words through length 18); frozen 2,600-case enumeration and the seeded trials are recorded supplementary checks, not proofs of the asymptotics.

## originality

PASS

Best-knowledge pass for the fixed-weight-two exact exponent invariant, sharp maximizers and weak law. Earlier unrestricted exponent bounds, a same-day sharp weight-three exponent result, and a same-day weight-two limit for another statistic are materially relevant but do not state or demonstrably imply that complete claim. Independent full-text access limits historical priority.

## value

PASS

Run exponents are an established repetitive-structure invariant. Weight two is the first binary sparse-content class with a nonconstant run, making the maximal length contribution and the competition between clipping and gap total natural rather than an arbitrary small case. The rigid exact maximizing family and nondegenerate limit law are distinct quantitative information unavailable from an unrestricted bound or run counts. No bound for unrestricted words or higher weights follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
