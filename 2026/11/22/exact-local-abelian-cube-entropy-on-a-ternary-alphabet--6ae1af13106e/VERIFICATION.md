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

The two included Python programs are independent scientific checks. `check_transfer.py` builds the letter-symmetry quotient of a terminal-forbidden-factor automaton from first principles, obtains its exact 49-by-49 characteristic polynomial with SymPy, and proves the all-length recurrence using Cayley–Hamilton together with the finite early-index checks. `check_direct.py` directly enumerates ternary words up to length eleven and separately uses literal-letter suffix-state dynamic programming through length 130. Both programs completed with all assertions passing.

The computed Perron root and asymptotic constant follow from the displayed integer polynomial and rational generating function. Numerical root approximations are not substitutes for the exact polynomial, the determinant check, or the primitivity argument.

No independent mathematical audit has been performed. The claim does not count avoidance of Abelian cubes of arbitrary block length; the two languages first differ at length nine.
