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

# Verification record

The symbolic proof in `RESULT.md` is the argument for all finite fields. The attached checker is an independent implementation of finite-field arithmetic, group multiplication, group inverse, cube and nested commutator in upper unitriangular coordinates. It tests the theoretical word map against explicit group operations and then tests complete value distributions against direct enumeration.

Run the standalone checker with `python verify_word_joint.py` from the directory holding the two files. It depends only on Python 3's standard library. The complete recorded stdout is `verification_output.txt`; it was reproduced by executing the packaged source.

Cases: every six-tuple of first-superdiagonal coordinates over fields of orders 2, 3, 4, 5, 7, 8, 9 (931748 pairs in all), with the cube/Engel joint fibers checked in the characteristic-three extensions 3 and 9. Direct multiplication, inverse, cube and Engel-word tests cover every ordered pair of full group elements over field orders 2 and 3 (4096 and 531441 pairs) and 6000 reproducibly sampled pairs for each of 4, 5, 7, 8, 9 (565537 direct pairs total). The \(q=9\) and \(q=4,8\) tests exercise polynomial-extension fields, not only prime fields.

The tests do not enumerate larger unitriangular dimensions and do not prove the infinite prime-power identity; that rests on the separate symbolic fiber-counting proof. No independent audit has been performed.
