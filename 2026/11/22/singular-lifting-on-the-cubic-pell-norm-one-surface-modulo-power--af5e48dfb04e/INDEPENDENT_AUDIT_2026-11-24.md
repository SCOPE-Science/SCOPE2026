# Independent mathematical audit

## correctness

PASS

Writing s=x+y+z and t=xy+yz+zx gives F=s^3-3st. Modulo 3 the target is s=1, with nine triples. For such s, s^3=1 modulo 9, so lifting to modulo 9 requires t=0 modulo 3. The number of nonzero coordinates is then 1 modulo 3, hence exactly one, with residue 1. In the class (1,0,0), substitution gives F(1+3a,3b,3c)-1=9[a+3(a^2+a^3+b^3+c^3-bc-3abc)]. The bracket is a modulo 3 and its a-derivative is 1 modulo 3: at precision 3^(k-2), each b,c pair has a unique root (vacuously for k=2), with three choices for the unused digit of a. This gives 3^(2k-1) points in each of three classes. Since every partial derivative of F is a multiple of 3, the linear Taylor increment by 3^k digits vanishes modulo 3^(k+1), and the higher terms vanish because 2k>=k+1. Thus each nonempty fiber has 27 elements and the count gives an image of size 3^(2k-1) at every k>=1.

## originality

PASS

Best of the available evidence supports a distinct integer-ring count and singular projection law. The same Resultary record is not a separate prior result. The closest distinct catalog statement is for a different map; the reported finite-field and split-prime results supply no matching integer 3-adic lifting statement. Full-text access limits this comparison; unsuccessful retrieval is not evidence of novelty.

## value

PASS

The prime 3 is the intrinsic ramified case of this cubic norm: the usual gradient test gives no separation of roots. The result describes both the point count and the compatible part of the solution tower, exposing the contrast between only one third of residues lifting and all 27 digits working when a residue does lift. This supplies the missing local data for the norm-one problem at its singular prime, not just a finite point count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
