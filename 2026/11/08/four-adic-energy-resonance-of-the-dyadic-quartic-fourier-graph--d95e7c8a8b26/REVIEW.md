# Independent mathematical audit

## correctness

PASS

Reconstructed the all-k proof by conditioning on the linear sum s. The odd-square map modulo 2^j for j>=3 has kernel size four and image precisely the residues 1 mod 8, giving j*2^j square collisions after adding the even lift contribution 4*S_(j-2). For odd s, each even product x(s-x) has one preimage in each parity class by the odd derivative, and the quartic sum becomes 2(2z-s^2)^2-s^4; the factor 16 comes from two preimages per product and two lifts per odd residue after reducing the modulus by one, for each of the two inputs. This gives 8*N^2. For even s the input parities cannot collide. On odd inputs the centered factor z+z'+6(s/2)^2 has exact valuation one, using z,z'=1 mod 8 or 0 mod 4 as appropriate; the two even-s classes together give (k-2)*N^2. The all-even three-variable branch rescales by 16 and has 8^3 lifts, giving 512*E_(k-4). The k=1 case is the identity graph; for 2<=k<=4 the powers detect parity, giving 3*N^3/4. Dividing the recurrence by 4^k and adding k+14 yields a four-step doubling with the four listed bases. Orthogonality averaged over the two frequencies imposes both congruences with no extra factor. An independent direct x,d,e congruence enumeration through k=8 agreed, including both sides of the recurrence threshold. Replay: python3 /workspace/review_evidence/dyadic.py.

## originality

PASS

The supported distinct result is the all-exponent dyadic quartic energy and its four exact leading constants. The Fourier identity is standard. The closest same-day prime-power result shares the homogeneity-driven four-step form but expressly excludes 2, and its transformations need 2 invertible. The exact dyadic sums-of-even-powers table lacks the joint linear-sum condition. No examined source supplies the required characteristic-two residual count or its consequences.

## value

PASS

This gives the exact unweighted fourth moment for a natural quartic graph in the small-prime regime excluded by the invertible-coordinate calculation. In particular, it quantifies the leading residue-class variation, not just a growth exponent or a small table of checks. Such exact dyadic constants distinguish behavior invisible to an order-of-magnitude restriction bound; the result makes no claim about the weighted norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
