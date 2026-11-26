---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The shortest factor carrying j+1 ones has length j+1 plus the minimum sum of j successive inter-one gaps. The shortest prefix carrying them uses the leading j gaps, since a nonzero prefix-normal word starts with one. Prefix normality is equivalent to equality of these shortest lengths for every j, and palindrome symmetry also forces the last bit to be one. In (a,b,c,d,c,b,a), the one-gap comparisons give a<=b,c,d. The two-gap comparisons add only a+b<=c+d; the three-gap competitor sums are b+c+d and 2c+d (up to reversal and the leading sum), giving a<=d and a+b<=c+d. Four gaps give a<=c, five give a<=b, and six and seven gaps add no restrictions. This includes empty gaps. Substituting (a,b,c,d)=(t,t+x,t+y,t+v) yields 8+7t+2x+2y+v and condition x<=y+v; excluded tuples x=y+v+1+k have length 10+7t+4y+3v+2k. The two geometric products give the stated series, with no words below length eight. Their order-four coefficients at z=1 differ by 1/28-1/168=5/168; all other poles have multiplicity at most two, so the cubic coefficient is 5/1008 and the error O(n^2). The total fixed-weight palindrome count is choose(floor(n/2),4), with odd center necessarily zero, giving 40/(21n)+O(n^-2). Independent bounded span enumeration (python3 /workspace/replay_independent.py 1) matched every coefficient at n=8..34, reproducing the displayed initial list. The proof handles all n and does not rely on the finite range.

## originality

PASS

Pass for the explicit fixed-eight palindrome rational series and its sharp conditional asymptotic, not for the generic sliding-gap criterion or mere availability of a counting algorithm. The four tests are a specialization of the known gap criterion. Neither aggregate palindrome counts nor known fixed-density formulas for unrestricted words cover the evaluated intersection. No independently matching series or density coefficient was found in the compared statements; this is not an exhaustive priority claim.

## value

PASS

The fixed-composition count refines a specifically studied prefix-normal palindrome family. Weight eight is a concrete even-weight test where mirrored local gap comparisons alone do not suffice: the coupled middle constraint changes the leading coefficient and controls the conditional rare-event probability among all eight-one palindromes. The result gives an exact simple series and an implementable structural characterization, not just a finite table. The judgment does not rely on calling this the first coupled example across both parities, nor on implying aggregate enumeration or density among general binary words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
