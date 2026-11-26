# Independent mathematical audit

## correctness

PASS

The state matrix M is a swap modulo p, fixing the all-ones seed and ensuring nonzero unit denominators even for negative a. With M^2=I+aM, the first binomial term for an index difference d has scalar valuation h+v_p(d), since its projected factor is another sequence term. In the regular range (j-1)h-v_p(j)>=1 for j>=2, so higher terms cannot cancel it. Each parity is then a bijection at depth k-h; an odd scalar period 2u+1 would require both u and u+1 divisible by p by the first two terms modulo p^(h+1). Constancy for k<=h follows from M^2=I mod p^h. The principal unit subgroup and the denominator x_0=1 give the regular quotient closure. For a=2u with u odd, M^4=I+4B, B mod 2 is I+M, B^2 is even, and B applied to the orbit is even. Modulo four the projected B-value is x_r+3u x_(r+1), which is 2 for both selected branches in each parameter class. Thus their leading valuations are 3+v_2(d), strictly below the higher terms; the branches fill the depth-three balls at 1 and 7. A fixed term c=3 mod 8 and division by each of those balls fill the remaining odd balls; the closed unit group excludes nonunits. Only the two specified value subballs and the full quotient closure are claimed at h=1, not the whole exceptional value classification. Independent bounded checks passed over 5,848 orbit positions for a=3,-3,25,4,-16,2,-2,6,-6 at the corresponding primes. Frozen replay path is check.py beside RESULT.md; the finite checks supplement the proof and do not establish the universal quantifiers.

## originality

PASS

The supported distinct claim is the all-power parity isometry, exact least periods and fibers at regular primes, and the precise quotient closure including the v_2(a)=1 lift for the all-ones seed. Generic non-density in Q_p is already covered and is not counted as original.

## value

PASS

For this natural unit-seeded test of the known non-density theorem, the useful refinement is the exact arithmetic structure: a scale and multiplicity for every regular power and a dyadic lift where individual values miss a residue class modulo 8 but quotients nevertheless fill the unit group. The uniform branch information is stronger than non-density and is not inferred from finite sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
