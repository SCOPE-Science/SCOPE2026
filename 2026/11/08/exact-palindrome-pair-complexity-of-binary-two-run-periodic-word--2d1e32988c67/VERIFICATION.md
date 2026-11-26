---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Direct run analysis gives all cases. Equal endpoints can be made symmetric by trimming the longer endpoint into a constant palindrome. Opposite endpoints with a full endpoint give a symmetric prefix or suffix and one constant palindrome. With at least four runs and both endpoints partial, a palindrome prefix ends only in the first run or at the initial run's depth in a later full run of its letter. Each cut leaves a non-palindromic suffix: its endpoints differ except at the first boundary, where its full first and partial last runs have unequal lengths. Splitting the first full run of the other letter yields the indicated three-piece factorization. These cases thus have exactly PL=3 and lengths kL+s+t with k>=1 and both residual counts positive and strictly below their full lengths. The two cyclic changes imply primitiveness and thus distinct phases for n>=L. The length cutoff, generating function, complexity in its asserted range, and exceptional-run threshold follow. The checker and VERIFICATION.md were read but the uploaded checker was not run. The separate explicit-cut replay /workspace/branches/replay_frozen.py matched distinct-factor counts and the ceiling in all 2304 cases for 1<=a,b<=8, 1<=n<=4L; the unbounded proof is the run argument.

## originality

PASS

The indexed exact match is the frozen record itself. Prior palindrome-pair results cover short run counts and minimal obstructions and introduce the complexity statistic, but they do not give the strict-endpoint criterion and resulting lengthwise counts for this period family. PASS is for the exact criterion and enumeration in this scope, not for the definition or global obstruction theory.

## value

PASS

The exact count for a natural primitive periodic family goes beyond bounding palindromic length or detecting minimal forbidden examples. It identifies precisely which phases and lengths require a third part, gives the sharp onset and permanent periodic profile, and supplies a tractable benchmark for the established palindrome-pair complexity statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
