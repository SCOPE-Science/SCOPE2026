# Independent mathematical audit

## correctness

PASS

For real path data on n observations, quotient seminorm V(x)=||D1 x||_1 and step reconstruction R with D1 R=I give the exact induced matrix norm max absolute column sum of A=D1 S R. For p=1, A=(I+lambda D1 D1^T)^(-1), an entrywise positive irreducible M-matrix inverse with every row/column sum strictly <1 due to Dirichlet edge losses. For p=2, S is self-adjoint and fixes exactly affine sequences; since A 1=1, if no column endpoint contrast exceeded 1 then S would fix e_n-e_1 in addition to affine sequences, contradiction for n>=4. The resulting positive column-sum witness is a monotone binary jump for every lambda>0. At n=3, A has unit column sums, and at n=4 direct inversion and sign-separated outer-column estimates prove exact L=(1+12lambda)/(1+10lambda) with central step. Inspected package RESULT.md and check.py verify symbolic A for n3,n4, and independently repeated SymPy rational-function checks plus rational parameter examples; finite examples corroborate but all n and all strengths follow from the self-adjoint affine fixed-space proof. The n=2 p2 case is explicitly excluded; no unsupported norm formula for longer n is claimed.

## originality

PASS

Best-of-knowledge original BV-norm threshold at FOUR samples and all-length self-adjoint affine obstruction. Exact HP coefficient and range-preservation results are genuine antecedents, but neither asserts or directly entails the sharp variation statement. The 2016 complete source access limitation remains explicit.

## value

PASS

Unweighted quadratic first- and second-difference Whittaker filters are standard signal-processing objects; adjacent total variation is a natural stability norm independent of the quadratic objective. The theorem locates a sharp universal transition at four samples, gives the exact first unstable amplification factor and an attaining monotone binary jump for any smoothing strength, and explains it through an all-dimension affine-fixed-space obstruction. The fact that 3-sample range-undershoot still has TV norm exactly 1 makes this a distinct motivated stability classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
