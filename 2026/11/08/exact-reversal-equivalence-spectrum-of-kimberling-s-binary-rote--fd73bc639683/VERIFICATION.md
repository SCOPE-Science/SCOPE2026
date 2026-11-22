---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

Inspected all seven actual frozen files (RESULT.md, SLOGAN.txt, AUDIT.json, METADATA.json, REVIEW.md, VERIFICATION.md, verify.py), with Git blob IDs reconstructing exact expected source-tree SHA 59263e5401b8897a57b6541d067f007a20df85aa. Independently rebuilt the Tribonacci 2-factor language {00,01,02,10,20} under phi=(01,02,0); every phi^4(a) has length >=7, so six-factors are exhausted by fifth two-letter boundary images, yielding 13 distinct six-factors. Since pi(0)=100,pi(1)=101,pi(2)=10 have image length >=2, a binary factor of length <=11 can touch at most six consecutive images; exact B languages equal all factors of pi(L6(T)) plus the one exceptional initial prefix. Independently computed each complete length 1..11 factor set via this cover and a second different phi^3 six-window cover from the previously published October 25 result, and compared them with a long prefix only as corroboration. Obtained factor counts 2,4,..,22, P=[2,2,2,2,2,1,2,1,1,0,0], Q=[0,1,2,2,2,3,2,1,0,0,0], and r=[2,3,4,6,8,9,12,15,18,20,22]. Length 10 has exactly the submitted 20 distinct factors and no reversals; any longer pair would induce a length-ten reversed factor pair. External Theorem 5 establishes #L_n=2n for every n>=1, giving r(n)=2n-Q(n). This is an infinite logical reduction, not an inference from a finite sampled prefix. Only n>=1 and the fixed exact word are claimed; reversal without binary complementation.

## originality

PASS

Best-of-knowledge PASS for the substantive NEW exact Q(n)/r(n) reversal-equivalence classification and sharp n=10 cutoff, NOT for the already-known P(n) spectrum. The October 25 published theorem proves all 15 palindromes and provides an exact six-word finite factor cover, so it substantially overlaps and makes the new reversal check short and mechanically reproducible; nevertheless it does not state or imply from palindromic counts alone that nonpalindromic reverse pairs vanish at length ten, nor give the complete Q-vector. This is a narrow, explicit natural invariant; historical priority and low computational novelty remain serious residual risks.

## value

PASS

The exact reversal-equivalence class spectrum is a natural standalone invariant introduced and actively studied in primary reflection-complexity literature. Its permanent sharp cutoff at n=10 distinguishes the absence of ALL reversal pairs from mere eventual absence of palindromes, and records a meaningful classification of a named 2n-complexity Rote word that is not complement-symmetric. This precise Q-vector and r(n) formula can serve as a reference example distinguishing different symmetry classes, despite very substantial overlap with the published P-spectrum and finite-cover method. The result is narrow and computationally inexpensive once the October 25 cover is known; no new general theorem, historical priority or major methodological advance is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
