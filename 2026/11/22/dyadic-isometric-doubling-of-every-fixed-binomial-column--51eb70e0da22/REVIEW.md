# Independent mathematical audit

## correctness

PASS

Fix a=floor(log2 m), L=a+1 and representatives 0<=r<2^L. The roots cover all residues mod 2^a and are distinct mod 2^L, so the closest j_* is unique: if two roots agree with r mod 2^a exactly one agrees mod 2^L. Write e=v2(r-j_*) and S_r for the sum of the other root valuations. On the branch all the other valuations stay fixed and are below min(e,L). In the telescoped divided difference the term omitting j_* is the unique one of valuation S_r. Thus differences on the branch have valuation d_r+v2(t-s), d_r=L+S_r-v2(m!), with d_r>=0 by integrality. The normalized branch is an isometry onto Z_2 because each finite reduction is bijective and the reductions are compatible. In the doubled branch the same-parity roots add m-1 to S_r, opposite-parity roots contribute zero, and v2((2m)!) adds m to the denominator valuation, so the scale is unchanged. Centers are all zero for r<m; for r>=m the common center valuation is d_r+e-L>=d_r-1. At the only potentially smaller valuation d_r-1 all centers have the same odd unit modulo two, hence are congruent modulo 2^d_r. This also covers d_r=0 and m=1. Inverting one branch on the common output ball constructs the desired bijective branch isometry. Because different branches retain their residues, the assembled isometry is global and Haar preserving; each finite branch permutation gives precisely the asserted local multiset equality. Iteration gives odd-part invariance, not an assertion that different odd parts always yield different laws.

## originality

PASS

The meaningful distinct claim is the all-column, class-preserving isometric reparametrization in each parity branch, with localized complete residue laws. Existing dyadic support and individual-column laws receive full credit. The closest exact comparisons do not cover the cross-column theorem.

## value

PASS

The theorem replaces infinitely many full fixed-column residue-law problems by the odd-index cases. It transports both global and conditional counts at arbitrary depths by explicit local inverse maps; that is materially stronger than transferring a few valuations, proving surjectivity, or reproducing the fifth- and sixth-column tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
