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

For A=1+x+x^-1, write A^3=A(x^3)+3B; modulo nine only zero and one insertions of B survive. For r=0,1,2 the correction constant terms before 3m are 2T_(m-1), 6T_(m-1)+2[x]A^(m-1), and 16T_(m-1)+8[x]A^(m-1); 2[x]A^(m-1)=T_m-T_(m-1). This verifies all three recurrences and the initial case. Modulo three the digit 2 annihilates, and digits 0/1 copy. Modulo nine, a binary prefix acquires six exactly at an appended 0 after 1. Its first 2 creates 3 or 6 according to its predecessor, the first subsequent 0/1 adds three, and further binary appends leave the class unchanged. With a second 2 the residue becomes zero and stays there, since whenever a nonzero correction multiplier is possible the prefix minus one still contains an earlier 2. Sentinels 0 and 1 give a bijection between binary words with d descents and 2d+1 chosen transitions. Counting unique-2 positions yields the stated 3 and 6 counts and then the zero count by subtraction, with L=0,1 checked separately. For omega=e^(2pi i/3), the odd binomial part at sqrt(omega)=e^(pi i/3) has dominant term of modulus 3^((L+1)/2)/2 and a remainder of modulus 1/2. Orthogonality gives sum of squared centered counts = 2|F_L(omega)|^2/3, so cancellation in individual classes cannot remove the claimed maximum order. Independent replay: python3 -I -B /workspace/reproduce.py 1 directly multiplied Laurent polynomials modulo nine through n=6560 and checked every residue and the nine complete histograms. The uploaded checker and its reported run were inspected, not executed.

## originality

PASS

The exact zero criterion, zero-class count, and equivalent recurrences are already in f302476becb1; density-one divisibility also follows from Kohen's general theorem. Credit all of that. The reviewed contribution is the remaining five residue classes, their joint exact histograms and sharp conditional discrepancy. These can be developed from the known recurrences, but require the descent and unique-digit analysis, counting and Fourier argument; the cited automata methods give computability, not the explicit spectrum or sharp fluctuation scale.

## value

PASS

The first square of the digit prime distinguishes residue distributions that both divisibility tests collapse. The exact spectra and the optimal within-support fluctuation scale give reusable arithmetic information for complete ternary blocks; density-one zeros alone would entirely mask that behavior. The case is a natural refinement of the classical sequence, and the counting and bias law are not just a finite table or the old zero class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
