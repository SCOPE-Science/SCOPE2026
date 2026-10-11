# Two missing spectrum members for perfect nine-ary length-four two-deletion codes

## Finding

For alphabet \(X=\{0,1,\ldots,8\}\), there exist perfect length-four two-deletion-correcting codes of sizes \(16\) and \(17\). Equivalently, \(16,17\in\operatorname{Spec}(9,4,2)\). Combining these explicit constructions with the published existence of sizes \(18\) and \(19\), and with the published bounds \(14\le |C|\le19\), gives

\[
\{16,17,18,19\}\subseteq\operatorname{Spec}(9,4,2)\subseteq\{14,15,16,17,18,19\}.
\]

Thus, relative to those published bounds and constructions, only sizes \(14\) and \(15\) remain undecided for \(q=9\).

A size-16 code is the following set of words, written as four decimal symbols from \(X\):

```
1670 5506 5141 5772 1533 4247 3820 0122
8664 0403 2635 3746 4588 6218 8731 0785
```

A size-17 code is:

```
8348 6158 4221 0445 2436 7778 8511 3335 5255
1407 5370 0163 8627 7564 6660 7312 0280
```

## Assumptions and scope

For a word \(x=(x_1,x_2,x_3,x_4)\in X^4\), let \(D_2(x)\subseteq X^2\) be the set of ordered length-two descendants obtained by deleting any two coordinates while preserving order. A code \(C\subseteq X^4\) is perfect for two deletions exactly when the sets \(D_2(x)\), for \(x\in C\), partition all \(81\) ordered pairs in \(X^2\).

The finding is only an existence result for the two displayed codes. It does not classify all perfect codes of either size and does not decide existence at sizes \(14\) or \(15\).

## Proof

For each displayed word \(x\), form the set

\[
D_2(x)=\{(x_i,x_j):1\le i<j\le4\}.
\]

The supplied deterministic verifier enumerates these descendants as sets, so repeated descendants internal to one word are counted once, exactly as in the deletion-ball definition. For the size-16 code it obtains

\[
\sum_{x\in C_{16}}|D_2(x)|=81,
\]

and every ordered pair in \(X^2\) occurs in exactly one \(D_2(x)\). It obtains the same two facts for the size-17 code. Hence both descendant families partition \(X^2\), proving that both displayed codes are perfect two-deletion-correcting codes.

The literature gives the surrounding interval. For \(q=9\) and length \(4\), the general lower bound is \(DL(9,4)=14\), while the optimal size is \(19\). The earlier general construction gives a perfect code of size \(18\). Therefore adjoining the two verified constructions yields the stated inclusion for the spectrum.

## Verification

Run `python3 artifacts/verify.py`. It checks that every displayed word has four symbols in \(X\), that words are distinct, generates all six coordinate pairs before set deduplication, and verifies that the resulting deletion-descendant sets cover each of the \(81\) ordered pairs exactly once. The expected terminal line is `VERIFY_OK`.

The JSON data used by the verifier are in `artifacts/codes.json`; no external package is required.

## Relationship to prior work

Chee, Ge, and Ling define \(\operatorname{Spec}(q,n,t)\), prove the perfect-code/directed-packing equivalence, establish \(\operatorname{Spec}(q,n,n-2)\subseteq[DL(q,n),DU(q,n)]\), and leave \(q=9\) among the possible exceptions to their complete length-four spectrum theorem. Their summary states that only a finite list of alphabet sizes remains unresolved. Their cited constructions give a perfect \((4,2)_9\) code of size \(18\), while Wang's optimal construction gives size \(19\).

The present contribution supplies explicit perfect codes at the two intermediate sizes \(16\) and \(17\). Searches under both deletion-code and directed-packing terminology found no source asserting these two spectrum memberships. That absence is evidence, not a proof of novelty; an obscure or unindexed earlier construction remains a residual bibliographic risk.

## Limitations

The result does not settle whether \(14\) or \(15\) belongs to \(\operatorname{Spec}(9,4,2)\). It proves existence, not isomorphism classification or enumeration, at sizes \(16\) and \(17\). The originality assessment is limited by the discoverability of older directed-packing literature.

## References

1. Y. M. Chee, G. Ge, and A. C. H. Ling, *Spectrum of Sizes for Perfect Deletion-Correcting Codes*, SIAM Journal on Discrete Mathematics 24 (2010), 33–55. DOI: 10.1137/090751311. Public preprint: arXiv:1008.1343v1.
2. J. Wang, *Some combinatorial constructions for optimal perfect deletion-correcting codes*, Designs, Codes and Cryptography 48 (2008), 331–347. DOI: 10.1007/s10623-008-9212-8.
3. D. B. Skillicorn, *Directed packings of pairs into quadruples*, Journal of the Australian Mathematical Society, Series A 33 (1982), 179–184. DOI: 10.1017/S1446788700018310.
