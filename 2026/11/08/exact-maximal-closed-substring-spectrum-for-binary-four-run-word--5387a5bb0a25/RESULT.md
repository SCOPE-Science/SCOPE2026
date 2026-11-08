# Exact maximal-closed-substring spectrum for binary four-run words

## Finding

Let \(a,b,c,d\) be arbitrary positive integers, let \(n=a+b+c+d\), and put
\[
W=0^a1^b0^c1^d.
\]
A **maximal closed substring occurrence** (MCS) is a half-open interval \([i,j)\) for which \(W[i:j]\) is a closed nonempty word and neither an available single-letter extension \(W[i-1:j]\) nor \(W[i:j+1]\) is closed. A word is closed if its length is one or it has a nonempty proper border occurring precisely as its prefix and suffix. Write \(K(W)\) for the number of MCS occurrences, counting positions, not distinct factor values.

**Complete classification.** Use zero-based positions and half-open endpoints. Every MCS occurrence is exactly one of the following, with no duplicates:

1. The four whole runs: \([0,a)\), \([a,a+b)\), \([a+b,a+b+c)\), and \([a+b+c,n)\).
2. \([a-x,a+b+x)\) for integers \(1\le x\le\min(a,c)\), except omit \(x=c\) when \(c\le a\).
3. \([a+b-y,a+b+c+y)\) for integers \(1\le y\le\min(b,d)\), except omit \(y=b\) when \(b\le d\).
4. The single interval \([a-\min(a,c),\,a+b+c+\min(b,d))\).

Consequently, with \(\mathbf1_E\) denoting the indicator of condition \(E\),
\[
\boxed{K(W)=5+\min(a,c)+\min(b,d)-\mathbf1_{c\le a}-\mathbf1_{b\le d}.}
\]
For every integer \(n\ge4\), the **entire attainable spectrum** as \(a,b,c,d\) range over positive integer compositions of \(n\) is
\[
\boxed{\{K(0^a1^b0^c1^d):a,b,c,d\ge1,\ a+b+c+d=n\}
=\{5,6,\ldots,H(n)\}},
\]
where \(H(4)=5\), and \(H(n)=\lfloor n/2\rfloor+4\) for every \(n\ge5\). Both extrema and every intermediate value occur.

## Assumptions and scope

The alphabet is exactly the binary alphabet. Exponents \(a,b,c,d\) are positive, so there are exactly four runs; the string is **linear**, not circular. Closedness uses occurrence counts within the examined factor; overlapping border occurrences count separately. A border is nonempty and proper. Single characters are closed by convention. A maximal occurrence may touch an endpoint, in which case the unavailable extension imposes no condition. MCS counts refer to occurrences \([i,j)\), not to distinct closed factor strings. All conclusions hold for *every* positive four-tuple, with no size cutoff.

## Proof

**Step 1: classify by the number of transitions.** Every factor of \(W\) has at most three transitions between adjacent unequal letters. A zero-transition closed factor lies inside one run. It is maximal if and only if it is the whole run: a proper subrun extends by the same letter to another closed unary factor, whereas extending a complete run across a boundary makes a one-transition factor, which has different first and last letters and cannot be closed. This yields the four intervals in family 1. Every one-transition factor is open because its first and last letters differ.

**Step 2: exactly two transitions.** A factor with two transitions has either the form \(0^u1^b0^v\), with \(1\le u\le a\) and \(1\le v\le c\), or \(1^u0^c1^v\), with \(1\le u\le b\) and \(1\le v\le d\). In the first form, any nonempty border must be all zeroes: a border containing a transition \(0\to1\) would have to occur twice, while there is only one such transition in that factor. The longest possible unary border has length \(\min(u,v)\). This border has an internal occurrence if \(u\ne v\), because its shorter length occurs at least twice within the longer of the two zero runs. Conversely, when \(u=v=x\), the border \(0^x\) occurs precisely twice, once at each end. Thus this factor is closed exactly when \(u=v\). The analogous conclusion holds for \(1^u0^c1^v\): closedness requires \(u=v=y\).

For \(0^x1^b0^x\), extending left by zero or right by zero (if available) produces unequal outer zero runs and is not closed. A right extension by one is available exactly when \(x=c\); then the extended word is closed, since its border \(0^c1\) occurs only as prefix and suffix. This extension is available when \(x=c\le a\); hence this boundary value must be excluded. An outside extension across the left run boundary, if it exists, changes the first letter to one, while the last letter is zero and thus cannot be closed. This proves family 2. Symmetrically, \(1^y0^c1^y\) is nonmaximal only at \(y=b\le d\), since the available left extension by zero has the unique border \(01^b\). This proves family 3. These endpoint cases include lengths equal to one, without exception.

**Step 3: exactly three transitions.** Such a factor necessarily has the form \(V=0^x1^b0^c1^y\), where \(1\le x\le a\), \(1\le y\le d\). A nonempty border must contain a \(0\to1\) transition. Since \(V\) has only one \(1\to0\) transition, the border cannot contain any \(1\to0\) transition (otherwise two occurrences would require two such transitions). Therefore the only possible border has the form \(0^x1^y\); it occurs as both prefix and suffix exactly if \(x\le c\) and \(y\le b\). In this case it occurs exactly twice because \(V\) has exactly two \(0\to1\) transitions, and hence \(V\) is closed. If either inequality fails, \(V\) has no border and is open.

For a closed \(V\), extending left by one zero, when available, stays closed exactly if \(x<c\). If \(x=c\), the suffix's zero block is too short to match the longer initial block, while any border would still have to contain \(0\to1\); an extension beyond the initial run, if present, also makes the first and last symbols different. Thus the left maximality condition is \(x=\min(a,c)\). Similarly a right extension by one is closed exactly when \(y<b\) and an extra last-run one is available, so right maximality is \(y=\min(b,d)\). Together these select precisely the unique interval in family 4.

There are no other cases because every nonempty factor has zero through three transitions. Families are pairwise disjoint: they have distinct transition counts (except the distinct two-transition centers), and their parameters determine unique endpoints. The four run intervals, the \(\min(a,c)-\mathbf1_{c\le a}\) intervals of family 2, the \(\min(b,d)-\mathbf1_{b\le d}\) intervals of family 3, and the single interval of family 4 give the claimed formula.

**Step 4: sharp upper/lower endpoints.** Put \(A=a+c\) and \(B=b+d\), so \(A,B\ge2\) and \(A+B=n\). For any two positive integers \(p,q\),
\[
\min(p,q)-\mathbf1_{q\le p}\le\left\lfloor\frac{p+q-1}{2}\right\rfloor.
\]
Indeed, for \(p<q\) the left side is \(p\le\lfloor(p+q-1)/2\rfloor\), and for \(p\ge q\) it is \(q-1\le\lfloor(p+q-1)/2\rfloor\). Therefore
\[
K(W)\le5+\left\lfloor\frac{A-1}{2}\right\rfloor+\left\lfloor\frac{B-1}{2}\right\rfloor\le\left\lfloor\frac n2\right\rfloor+4.
\]
Also \(K(W)\ge5\), since each of the two corrected minimum contributions is nonnegative. Equality at the lower end is attained by \((a,b,c,d)=(n-3,1,1,1)\), for every \(n\ge4\). At \(n=4\), that is the only four-tuple and \(K=5\).

For \(n=2m+1\ge5\), set \((a,b,c,d)=(m-1,1,m,1)\) to attain \(m+4=\lfloor n/2\rfloor+4\). For \(n=2m\ge6\), set \((a,b,c,d)=(1,m-1,2,m-2)\), again attaining \(m+4\). Hence the upper bound is sharp whenever \(n\ge5\).

**Step 5: no gaps.** For odd \(n=2m+1\ge5\), take \(b=d=1\), \(a=t\), and \(c=n-2-t\) for every integer \(1\le t\le m-1\). Then \(a<c\), and the count is \(5+t\), realizing every value from \(6\) through \(m+4\). The lower witness realizes \(5\). For even \(n=2m\ge6\), the same family with \(1\le t\le m-2\) realizes \(6\) through \(m+3\); the even-length upper witness from Step 4 realizes \(m+4\). Thus every integer in the claimed interval occurs. The case \(n=4\) is already done. This completes the all-length proof.

## Verification

The standalone script `verify.py` computes closedness by exact border occurrence tests, enumerates every factor interval and its available one-symbol extensions, and compares the resulting MCS endpoint sets directly to the classification above. It checks every positive run-length quadruple with each parameter at most eight (4,096 words), comparing exact endpoint sets and exact counts. Separately it enumerates all compositions of length at most 32 and checks that their attainable counts form exactly the asserted complete integer interval. These bounded checks are independent corroboration; the infinite theorem follows from the proof above, not from finite enumeration.

Run `python3 verify.py` with the Python standard library. All inputs and expected properties are defined in that file; no external dependencies, unpublished tables or other artifacts are required.

## Relationship to prior work

Badkobeh, De Luca, Fici and Puglisi introduced maximal closed substrings (MCSs) and their enumeration. Umezaki, Shibata, Nakashima and Inenaga (2026) give a general run-length-encoded framework, including unary-border interval families (their Lemma 4) that subsumes some of the classification mechanisms used here. Fischer and Köppl (October 28, 2026) give output-sensitive algorithms for arbitrary strings, emphasizing the output count \(k\). Jain and Mhaskar study algorithms and counts for Fibonacci words. These results motivate exact output-sensitive models but do not state the four-run **closed-form endpoint list, total count, or sharp fixed-length attainable spectrum** proved here. In particular, the universal algorithms are capable of computing each individual instance, but do not supply a symbolic maximization over all run lengths at a fixed total length. The specialized lemma and elementary proof here should be viewed as a concrete sharpened enumeration and extremal application, not as a replacement for those general algorithms.

## Limitations

This result treats *linear* binary words with exactly four positive runs. It does not cover cyclic boundary factors, more than four runs, a general fixed run count, or distinct-string rather than occurrence counts. The proof was subjected to same-author reasoning and bounded executable checks; it has not received an independent mathematical audit. A general run-length encoding paper supplies related structural lemmas, so unrecognized earlier explicit four-run specializations remain a historical-priority risk.

## References

- G. Badkobeh, A. De Luca, G. Fici, and S. J. Puglisi, "Maximal Closed Substrings" (first preprint 2022), https://arxiv.org/abs/2209.00271.
- S. K. Jain and N. Mhaskar, "Efficient Algorithms to Compute Closed Substrings" (first preprint 2025), https://arxiv.org/abs/2506.06452.
- H. Umezaki, H. Shibata, Y. Nakashima, and S. Inenaga, "Compact Enumeration of Maximal Closed Substrings in Run-Length Encoded Strings" (July 3, 2026), https://arxiv.org/abs/2607.02838.
- J. Fischer and D. Köppl, "Output-Sensitive Enumeration of Maximal Closed Substrings in Linear Space" (October 28, 2026), https://arxiv.org/abs/2610.38114.
