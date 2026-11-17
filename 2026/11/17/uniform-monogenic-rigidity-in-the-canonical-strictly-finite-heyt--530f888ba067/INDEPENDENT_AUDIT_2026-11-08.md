# Independent mathematical audit

## correctness

PASS

The source order has width W=2^n+1>=3 and x_(i,l)<=x_(j,m) iff i>=j+2 or i=j+1 with m != l+1; only TOP contains the minimum x_infinity. Every clopen proper upset is finite. A nonzero upset with level>=2 forces all L0 and is dense, so its closure is {0,U,1}. Rank-1 upsets are either L0 plus a nonempty L1 subset (dense) or exactly E_j=(L0\{q_j}) union {r_(j-1)} for 1<=j<W (five elements). At rank 0, every nonempty subset S of L0 has complement-negation L0\S if |S|>=2; singletons q_j have negation E_j (j>=1), or L0\{q0} at j=0. Thus the only nine-element generators are L0\{q_j}, 1<=j<W; their explicit closure {0,1,a,b,c,d,e,f,g} is verified by direct implication identities with K_j empty for j=1 and K_j={x_2^(j-2)} otherwise. Rank-0 multiplicities are 1 size-3, 2^W-W-1 size-5, W-1 size-9; rank-1 multiplicities are 2^W-1 size-3 and W-1 size-5. Including constants gives 2 size-2, 2^W-2 size-5, W-1 size-9, countably infinitely many size-3. A separate direct implication/closure implementation enumerated every low-rank upset for W=3..8, including all nine-element closures, but the infinite statement follows from the structural lemma and symbolic classification.

## originality

PASS

The 2023 construction preprint (Definition 7, Proposition 18) and the 2024/2026 joint journal article (Definition 4.1, Proposition 4.10) establish the same X_n and qualitative finite bounds, but the inspected statements neither quantify the singleton-generated spectrum nor imply the constant sharp maximum 9 or exact generator multiplicities. The nearby published classification of a universal homogeneous Heyting algebra concerns a different algebra. This is a best-of-knowledge result, not a proof of historical priority.

## value

PASS

The exact one-generator size spectrum in the naturally defined canonical strictly n-finite Heyting family is an invariant directly relevant to quantitative finite-generation control. It is not a reparameterized textbook identity: the abrupt n=0 free-Heyting exception, n-independent sharp maximum 9, and exact exponentially varying generator multiplicities give a structural classification beyond the prior qualitative bound. The full two-generated spectrum is not asserted; this exact first-arity result has independent mathematical use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
