# Independent mathematical audit

## correctness

PASS

Every aligned 2^k-block is V_k a with V_k a fixed prefix and a in {0,1}. Every length-2^k factor is a rotation of one of the two aligned blocks. At k>=2 one block is a double of the preceding odd-weight primitive block and the other has odd weight, giving N/2+N distinct factors, weights differing by 1. For fixed length, all scattered order-two counts are determined by weight m and position sum S, since #01=S-binomial(m,2). Rotating an odd-weight binary word of length 2^h by d changes S by 2^h*t-d*m, so distinct rotations cannot share S; doubled rotations inherit this. Therefore b2=P=3*2^{k-1}, b1=2. The two distinct length-5 factors 10001 and 01010 have the same (m,S), excluding arbitrary-length extension. Independently checked 3069 dyadic factor signatures, not substituted for universal proof.

## originality

PASS

The published cyclic-class doubling bijection proves c_p(2^k)=2 but does not state that scattering moment signatures separate all rotations; its cyclic classes concern a different equivalence relation. Parikh-collinear binomial morphism results are inapplicable since images 01 and 00 have independent Parikh vectors. Dyadic two-binomial reconstruction remains plausible original, though known cyclic structure makes a short implication possible with extra argument.

## value

PASS

Dyadic lengths are an intrinsic substitution scale. The exact minimal scattered-order of factor reconstruction and the sharp non-dyadic counterexample answer a motivated word-combinatorics question, not a rebranding of 2-abelian or cyclic complexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
