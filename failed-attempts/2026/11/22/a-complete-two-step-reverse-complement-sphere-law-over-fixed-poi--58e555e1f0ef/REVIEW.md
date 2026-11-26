# Independent mathematical audit

## correctness

PASS

The mathematical claims in RESULT.md lines 3–19 hold. Two insertions at distinct original sites commute and the same-site possibilities are exactly a bar(a) bar(a) and a bar(a) a. Distinct one-step insertion sites i<j differ at output coordinate j+1 (original x_j versus bar(x_j)). On appending a to u, the n distinct outputs ending in bar(a) come from a one-step output of u followed by a bar(a), or from the repeated final-site expansion. The only additional candidate ending in a is u a bar(a) a. For its membership test u a bar(a) in D_2(u), track the last original letter. If it lies outside {a,bar(a)}, both insertions would have to follow it, which cannot yield a bar(a); if it equals bar(a), perform two suffix duplications. If it equals a, the two histories with both insertions after that original a end in bar(a) bar(a) or bar(a) a, not a bar(a). Thus exactly one insertion follows the last original a. It can be scheduled last because the other insertion is earlier and independent. The other insertion must change u into u a; comparison from its insertion site forces an inserted a in the terminal a-run, introduced by a preceding bar(a). This also supplies a clarification of the source's overly literal 'second inserted' at line 39: it need not be second chronologically in every history. The converse duplicates that preceding bar(a) and then the last a. This gives exactly the increment of C and proves the base n=1 and the induction. Independently, later runs have weights z u/(1-z u) or (q-2)z/(1-z); multiplying out gives the displayed series. At position j the mean penalty indicator is the sum of q^{-(j-i+1)} for possible boundary indices i=2,...,j (equivalently sum_{h=1}^{j-1} q^{-h}, indexing h=j-i+1). Its sum over j gives the expectation; c=0 is realized by constant words and c=1,...,n-1 by complementary two-run words. For exact replay, enumerate tuples w in range(q)^n, define T(v,i)=v[:i+1]+((v[i]+q//2)%q,)+v[i+1:] with zero-based i; form {T(T(w,i),j) : 0<=i<n, 0<=j<=n}. Count the deficit histogram B_n, with B_0=1; compare its coefficients using (1-(q-1)z-2zu+qz^2u) sum B_n(u)z^n=1+z-2zu. The bounded check exercised 3,172 sources (q=2 through n=7, q=4 through n=5, q=6 through n=4), including the wordwise run penalty, full histogram, endpoints and mean; terminal histograms at q=4 and q=6 were [324,324,232,112,32] and [750,390,132,24]. No frozen verifier was executed. Finite corroboration is not the proof.

## originality

FAIL

A second public record gives the identical all-word law, identical full distribution and identical extrema. The reviewed append argument is a different presentation; the extra expectation is an elementary derivative of the already identical generating series. The two GitHub histories show the same visible reconciliation commit dated 2026-11-22 UTC; this establishes a redundant published pair, not which version was first developed or an allegation of copying.

## value

FAIL

The complete law is worthwhile in isolation, but this record does not provide a distinct valuable scientific finding once compared with the companion. The marginal changes are a short alternative count proof, elementary extraction of the mean, and inclusion of the empty term. The frozen finding neither claims nor establishes a new application, range, or independently needed proof advance. Recommend cross-reference or consolidate as an alternative derivation, not validate as a separate law. No repaired finding is proposed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
