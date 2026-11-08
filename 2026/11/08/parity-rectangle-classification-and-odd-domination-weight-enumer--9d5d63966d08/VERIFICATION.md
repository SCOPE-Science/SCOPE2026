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
# Reproduction checks

Run `python3 check_binary.py` and `python3 check_linear.py` using Python 3.10 or later in the directory containing those files. Both programs are standalone standard-library scripts; there are no external data files, network calls, or packages. Their captured stdout is included in `direct_output.txt` and `affine_output.txt`.

`check_binary.py` enumerates every subset on each of the nine boards with \(2\le m,n\le4\), tests all closed-neighborhood parity conditions directly using cell incidence masks, then compares every coefficient with the theorem's polynomial. All nine cases passed, including \(W_{3,3}(z)=6z^3+9z^5+z^9\).

`check_linear.py` constructs a different representation: the binary augmented closed-neighborhood matrix, its complete reduced-row-echelon form, and the full affine family of solutions. It compares full weight distributions and affine dimensions against the theorem for all thirty-six boards with \(2\le m,n\le7\). All thirty-six passed. For example, \(5\times5\) has dimension eight and 256 solutions, while the largest tested board \(7\times7\) has nullity twelve, 4096 solutions and minimum weight seven with fourteen minimizers.

These checks are finite and are not offered as a substitute for the symbolic proof. They do not inspect the completeness of the historical literature. No independent scholarly audit has been performed.
