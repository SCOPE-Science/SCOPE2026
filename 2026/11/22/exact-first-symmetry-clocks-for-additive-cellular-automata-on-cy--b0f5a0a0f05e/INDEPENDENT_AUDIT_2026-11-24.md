# Independent mathematical audit

## correctness

PASS

T is elapsed time to the first nonidentity spatial symmetry, with T=0 for initially symmetric words, counting indexed words. In the cyclic module over F_q with modulus z^n-1, for each d|n the period-dividing-d condition at time t is the kernel of (z^d-1)(1-z)^t. The kernel dimension is the degree of its gcd with z^n-1: writing n=p^a m and d=p^b d0 with p not dividing m,d0, z^d-1 divides z^n-1 and has root-1 multiplicity p^b, so the dimension is d+min(t,p^a-p^b). This includes a=0. Commutation makes symmetry persistent, so M_t=#(T>t) is precisely the Möbius inversion sum over d|n of mu(n/d) times q to that kernel dimension. M_0=B_q(n). If p does not divide n the sum is time independent. Otherwise, only terms with b=a or b=a-1 survive; the latter have d=n/(pr), r|rad(m), and mu(pr)=-mu(r). Hence M_t=B_q(n)-(q^min(t,L)-1)H_q(n,p). Taking differences and the eventual constant gives precisely the finite, zero-time and infinite masses. H counts words of length n/p avoiding all prime-order symmetries from primes dividing m, so is positive (use a word with one marked site, or the vacuous one-site case). This ensures the sharp cutoff and well-defined conditional reverse-lag law, obtained by dividing by (q^L-1)H. For every prime ell different from p, the kernel dimension d=n/ell is constant in time, and the preimage kernels are nested, so such a symmetry cannot first appear. Any wholly new nontrivial stabilizer therefore contains the order-p subgroup. For m=1 the formula gives M_L=0. A commuting unit factor preserves each shift fixed subspace bijectively, so it preserves each word's clock, not just the distribution. Independently compared direct entry-or-repeat simulations with the per-divisor kernel-count formula in 26 rings over F_2, F_3, F_4 and F_9: all 30852 initial words agreed in the complete histograms. Replay: python3 /workspace/independent_replays.py 3.

## originality

PASS

The nearest checked literature gives static symmetry and stabilizer irreversibility, or temporal orbit periods. The closest distinct Resultary clocks apply to different update rules. No examined result gives the positive-time order-p shells with the exclusion of preexisting other-prime spatial symmetry, the complete first-spatial-passage law, and its reversed geometric consequence for the stated family.

## value

PASS

The invariant quantitatively refines general symmetry irreversibility for a canonical cyclic linear rule: a period drop may never occur, but if it occurs after time zero it has a characteristic-prime cutoff and an exact reversed lag law independent of the prime-to-p factor. Counting every start and showing pointwise invariance under multiplication of the rule by a unit make this structural rather than an isolated cycle enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
