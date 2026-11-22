---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification details

Two standalone source programs are included, without compiled binaries or external data dependencies. Reproduce direct-state enumeration with C++17 by running `c++ -O3 -std=c++17 verify_extremizers.cpp -o verify_extremizers` and `./verify_extremizers`. Independently run `python3 verify_local.py` using Python 3 standard library. Their exact recorded output files are `verify_direct_output.txt` and `verify_local_output.txt`.

The direct checker enumerated every one of 14,348,907 initial states on the complete binary tree of height three, obtaining exactly twelve root excitations at time three; it also checked every 1,594,323 initial state on the ternary tree of height two, obtaining two. All smaller binary/ternary cases passed. With leaves fixed to state one, the checker enumerated 14,348,907 internal initial states at binary height four, obtaining 432, and 1,594,323 at ternary height three, obtaining 24. Counts agree with the exact formula, and the first two exhaustive cases also directly exclude noncanonical leaf assignments.

The second program exhausts 1,406,160 adversarial local input histories with freely chosen external parent states under the only final child-excitation timing constraints. All cases reach the claimed parent state zero immediately before the target step and state one at that step. The same code separately evolves 1,400 independently sampled canonical initial configurations on complete trees of branching two through five and heights two through six, including trees of 19,531 vertices.

These checks do not constitute an exhaustive search for all heights or branches and are not substituted for the causal-witness proof and height-by-height induction. The source date is the dated 1993 archival posting, not a later journal/revision date. Historical priority and independent mathematical validation remain outside the program checks.
