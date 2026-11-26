# Independent mathematical audit

## correctness

PASS

Sano's Theorem 1.1, Proposition 3.4 and Corollary 5.4 match the parameter and characteristic-zero type lists, for c lying in some CM field; K=Q(c) need not itself be CM. All the listed c are integral. A characteristic-zero first repeat survives reduction, so the only way the type can change is a collision among its initially distinct marked entries. For d≥3, c=0 is fixed; c^(d−1)=−1 gives the two-cycle 0,c with c a unit. For c^(d−1)=ω a primitive cube root, write u=1+ω=−ω², of order six. Then 0,c,uc are the three distinct entries; (uc)^d+c=uc if d≡0 and is 0 if d≡1 mod 6. The three differences up to sign are c,uc,ωc, all units, so no proper ideal causes a collision, even in degenerate residue characteristics. Quadratic 0 and −1 have no nonunit differences; −2 gives 0,−2,2,2, with differences of absolute sizes 2,2,4, hence exactly the displayed changes mod (2) and (4). For c=±i the four distinct entries are 0,c,c−1,−c and the next is c−1. Of six differences only c−1,2c,2c−1 (up to signs) are nonunits. Their respective principal ideals are p₂, p₂², p₅, where p₂=(1+i) and p₅=(2c−1) has norm 5 and is conjugated by changing c's sign. Mod p₂ the first/third and second/fourth entries coincide; mod p₂² only second/fourth; mod p₅ only third/fourth, giving the three reduced types in the stated order. Mixed ideals cannot create any collision because none divides a listed nonunit difference ideal; equivalently their product orbit has maximum preperiod and least common multiple period, so the two different exceptional Gaussian primes together restore (2,2). This proves exhaustiveness for all exponents and all products of ideals. Frozen VERIFICATION.md and check_portraits.py were read but the script was not executed: its prime-power, composite ideal and prime-field tests have finite bounds and do not certify the unbounded classification.

## originality

PASS

Sano's characteristic-zero classification is used without novelty credit. The supported distinction is the exact all-ideal collision spectrum of the marked orbit, notably the nonzero-to-nonzero collisions determining the second dyadic layer and split prime over 5. Known results on the ideals of individual orbit entries, primitive divisors and field-level liftability cover ingredients or special questions, not this marked orbit's full quotient-ring type. Higher-degree preservation by unit differences is an elementary consequence of these specific orbit shapes; the novelty assessment is for the complete specialization classification.

## value

PASS

The natural invariant is exact specialization of the marked critical relation over every integral quotient, distinct from map good reduction and from whether 0 returns. The arithmetic classification identifies precisely which moduli destroy the characteristic-zero distinctness, including the positive-preperiod intermediate portraits at dyadic level two, the conjugate norm-five exceptions, and the lack of mixed-ideal exceptions. These are useful exact ring-level data and a uniform higher-degree rigidity statement, not a sample over small prime fields.

The dated certificate retains the supplied scientific assessment, sources and limitations.
