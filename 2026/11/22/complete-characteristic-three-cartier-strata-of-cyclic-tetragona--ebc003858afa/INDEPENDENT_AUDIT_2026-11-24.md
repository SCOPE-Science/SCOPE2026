# Independent mathematical audit

## correctness

PASS

There are six tame totally ramified points including infinity, giving genus six. At a finite root y is a uniformizer and dx has order 3; at infinity x,y,dx have orders −4,−5,−5. These valuations and distinct pole orders give the stated basis. Extracting terms x^{3t+2}dx after writing y^{-j}=f^e(y^{-j'})^3 gives the two blocks: on j=2 the coefficient pattern is (B,C;1,0) up to cube roots; on j=1,3 one has ω5→ω0→v with v's ω3,ω4,ω5 coefficients the cube roots of C²−BD, −D−AB, −A, respectively. The vector v cannot vanish: that forces A=D=C=0, contradicting squarefreeness. Thus the second block has rank 2 for all powers if A≠0 (invertible on its image), or ranks 2,1,0 thereafter if A=0. On the first block C≠0 gives rank 2 throughout, C=0 and B≠0 gives 1 throughout, and B=C=0 gives 1,0 thereafter. All these rank arguments respect inverse-Frobenius semilinearity. Their sums recover the six profiles and both invariants, including the codimension-three zero-rank case. Centering is unique since translation changes the quartic coefficient by twice the shift. The independent /workspace/reproduction/check_4.py checks all 6561 centered tuples over F9 using explicitly twisted Cartier iteration; all 5832 squarefree tuples agree, including the 54 over F3, and the six stated witnesses are squarefree with the prescribed profiles (check_4.out). This finite check supplements the symbolic proof over an algebraically closed field.

## originality

PASS

The distinct result is the complete rank-of-powers stratification on the full smooth centered cyclic (4,5) family in characteristic three. Related geometry, general Hasse–Witt formulas and computations in other characteristics are prior. No inspected statement gives or implies the six coefficient strata without the additional small-characteristic calculation. Historical priority is qualified.

## value

PASS

A full tame cyclic degree-four family at a small characteristic outside familiar large-prime generic theorems is a natural test case for rank stratification. The equations describe every jump on the smooth locus, distinguish degenerations with the same stable rank, and give realizable examples in each stratum. The result supplies concrete small-characteristic input beyond a generic p-rank or an algorithm for testing examples; it does not purport to classify Newton polygons or unmarked isomorphism classes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
