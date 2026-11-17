# Independent mathematical audit

## correctness

PASS

Using the exact balancing recurrence X_{n+2}=6X_{n+1}−X_n for B0=0,B1=1, C0=1,C1=3 and c0=−1,c1=1, the proof derives three initial square-window sums from Pell companion identities. Consecutive sliding-window differences are B_k B_{2n+k+2}, 8B_k B_{2n+k+2} and 8B_k B_{2n+k+1}; strong divisibility reduces each infinite GCD to an exact two-integer GCD. Dyadic valuations (v2(B_k)=v2(k)), ternary triplication and all other odd prime factors establish G_B(k)=gcd(k,B_k)/(2 if even k else 1), G_C(k)=gcd(k,B_k), and G_c(k)=gcd(k,3B_k) for odd k or gcd(k,B_k) for even k. These match the prior complete proofs. Independent exact integer checks for k≤31 with 12 windows in each family agree; finite checks are not used to justify the infinite GCD.

## originality

FAIL

Two separate Resultary results published November 2 state and prove exactly the same all-k three-family formulas, using the same sequence initial values, same index shift n+1, and the identical gcd(k,B_k) reduction. Earlier October results also separately solved individual parity and companion branches. No surviving independent claim or new parameter is present.

## value

FAIL

The GCD invariant is naturally motivated by Mbirika–Schrader–Spilker Question 30, but all three submitted infinite identities were published and proved before this record. Exact reproduction and a different exposition supply no distinct unknown invariant or mathematical advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
