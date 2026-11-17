# Independent mathematical audit

## correctness

PASS

The reduction to the greedy Mersenne Apéry weight w(j)=j+c(j), nondecreasing for 0<=j<a, identifies the maximum from the final constant-weight plateau. The binary splitting criterion yields c(M)=2t and plateau length delta+1 for M=m2^n. The maximal residue a-(delta+1) produces F=M²+a(2t-1)+delta. The proposed formula also has an exact independent cross-check against the previously proved all-parameter greedy formula: for h=2..199, computing greedy Mersenne coin count c_h and smallest occupied index i_h gives h+c_h=2t and i_h-1=delta. Thus the old formula M²+(h+c_h-1)M+(h+c_h+i_h-2) agrees term for term with the assigned expression. The proof handles n>=3, odd m>=3 and m<2^n, including h=7 and unbounded delta.

## originality

FAIL

An earlier complete all-odd-parameter Proth Frobenius formula (published 2026-10-25) covers precisely this semigroup and every n>=3, odd 3<=m<2^n. The assigned formula is an algebraic reparameterization of that theorem: the new t corresponds to half the prior h+c and delta to the prior least greedy index minus one. Thus the claimed formerly untreated all-weight cases had already been resolved.

## value

FAIL

The all-parameter Proth Frobenius problem is valuable, but its exact closed formula and unique maximizer had already appeared in the October 25 published result. Recasting the same answer as a minimum binary-weight index and unbounded correction is a change of notation, not substantive new information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
