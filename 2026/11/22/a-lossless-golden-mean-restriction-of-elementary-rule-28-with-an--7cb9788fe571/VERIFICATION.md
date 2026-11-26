---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The Wolfram truth table gives 1 on 010, 011 and 100; forbidding adjacent input ones leaves just 010 and 100 as one-producing triples. The former has preceding output zero and the latter preceding output one, so the decoder x_i=y_i(1−y_{i−1}) identifies input ones as output run starts. Three consecutive output ones would decode the last two to zeros, making the last output zero by the forward rule. A factor 0100 would decode its singleton to an input one and the next two sites to zero, making the first following output zero impossible. Conversely the decoded word has no adjacent ones; an output-one run start is reproduced by 010 and its second site by 100. At an output zero the only possible spurious one would be due to an input one immediately to the left with no input one immediately to the right. The forbidden 0100 condition forces an output run start to the right in that case, ruling out the spurious one. Both maps are sliding block codes. Every indexed length-n ring can be lifted to its n-periodic bi-infinite word, on which the same argument applies also for n=1,2. Indexed counts are the trace of the golden-mean adjacency matrix (not primitive necklaces), giving L_n by its quadratic identity and the determinant formula for the zeta function. The periodic words (1100)^Z and (01)^Z supply the required maximal proper factors 11, 100 and 010; one can witness irredundancy by 1^Z and (10000)^Z separately. A separate exact finite replay confirmed images, counts and decoder for all indexed n=1–18; the local proof supplies the unbounded statement. No unrestricted inversion or iteration on the no-11 domain is claimed.

## originality

PASS

The surviving claim is a two-site inverse and exact irredundant image SFT for Rule 28 with a no-11 input constraint. Salo's broader-domain image theorem and different no-00 input restriction are not the same conjugacy or a stronger version of it. The same-rule exact cyclic precursor counts include mixed source types and their reduced matrices lose information necessary to detect the additional obstruction. The Lucas enumeration and zeta formula are standard consequences, not credited as new.

## value

PASS

It answers a natural exact constrained-reconstruction question for a standard nonregular elementary rule, contrasting the known flipped-golden-mean restriction and unrestricted image. The short local inverse and a necessary-and-sufficient pair of minimal forbidden blocks yield an immediately usable membership and unique decoding test for every ring and bi-infinite word. This utility is in the constrained image and decoder, not in a finite prefix of counts, a generic algorithm to find a presentation, or the familiar Lucas numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
