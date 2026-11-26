---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Put E(t)=exp(At) and D_i=I-(1-p_i)P_i for the two coordinate projectors. In the trace expansion cyclicity and E(T-tau)E(tau)=E(T) make the terms with zero or one P_i phase-independent; the remaining term is (1-p_1)(1-p_2) E(T-tau)_{12}E(tau)_{21}, zero at synchrony. Since (A-(a+d)I/2)^2=chi^2 I, this is exactly the stated product. The determinant is a fixed h>0 and every Q is strictly positive, hence both eigenvalues are real and positive and the larger strictly increases with the trace. The hyperbolic product is strictly increasing up to T/2 and strictly decreasing after; 0 and T are the same phase modulo T. If rho(Q_0)<1 then h<1, so the smaller eigenvalue never reaches 1; det(I-Q) has the claimed threshold sign. Solving the equality gives the two endpoints when 0<L<H, with equality only at the midpoint when L=H. Shared scalar crowding is removable by a time-dependent scalar amplitude, unchanged at linear pulses; integration gives the stated projective census map. Summing the Perron component proves exponential extinction below one, convergence to the unique positive periodic orbit above one from every nonzero nonnegative census, and n*u_n tending to v/(kappa*k_tau^T*v) at one. The critical nonlinear population still goes extinct, algebraically. Independent replay: python3 /workspace/branches/replay_exact_audit.py 1 used the two exact eigenspace projectors to get rho(Q_0)=24/25, midpoint det(I-Q)=-17/5000, and the arcosh argument 693/676; an independent 40th-order matrix series reproduced the asymmetric trace and determinant numerically at ten phases. The uploaded checker was read, not executed; its midpoint hyperbolic check itself uses floats.

## originality

FAIL

Distinct Resultary record 61cfe5d6932c covers the central all-parameter trace law, both unique extremizers, the complete phase threshold and an exact rational-matrix reversal witness. The two schedules, generators, survival multipliers and Perron criteria coincide under notation changes. The literal numerical example in the frozen record differs, but exhibits the same covered phenomenon. The nonlinear statement is a standard projective consequence under precisely shared scalar crowding: lift the census map to the block linear matrix with first row of blocks (Q,0) and second row of blocks (kappa*k_tau^T,1), then divide by the last coordinate. The Perron geometric sum above one, linear sum at one and dominated numerator below one give the whole claimed extension and its coefficient with no independent timing phenomenon. The frozen package itself credits an earlier shared-crowding threshold construction. This is a coverage decision, not a priority assertion: the distinct comparator's catalogue path date is later, and that does not establish priority or provenance. Inaccessible papers are not the reason for FAIL.

## value

FAIL

The exact phase window is a meaningful benchmark for the mathematical culling model, but it and an exact phase-only reversal are already supplied by an equivalent theorem. What remains here is a different parameter example and the immediate scalar-crowding/Perron consequence of the same multiplier, not a distinct phase mechanism, separate nonlinear theorem outside that reduction, or independently needed exact invariant. Those additions do not meet the contribution standard for a repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
