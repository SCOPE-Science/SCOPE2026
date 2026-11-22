# Independent mathematical audit

## correctness

PASS

Computed f(A)=aI+sqrt2 b J3+2c J3², Frobenius norm²=3|a|²+4|b|²+4|c|², and Parseval bounds yielding ||f(A)||<=2. At equality b cannot be the only surviving mode because sqrt2 J3 has norm sqrt2; coefficient domination and Schur transform c=(1-r²)(g1-abar g0²) give |c|<=1-r²-|b|²/(1+r). Near equality forces |a|,|b|→0 and |c|→1. Direct top singular-value perturbation of f(A) yields ||f(A)||=2|c|+|a|²/2+|b|²+o(|a|²+|b|²), giving deficit≥(1-o(1))(1-|c|). H² phase distance²≤2(1-|c|) then proves upper sqrt2. Degree-two Blaschke f_t=z(z-t)/(1-tz) has H² norm one, distance²=2t² and deficit t²+O(t⁴), proving sharp lower constant and exponent. The derivation applies to all Schur symbols, not just polynomials.

## originality

PASS

Qualitative Crouzeix equality for 3x3 matrices and some operator-level near-equality stability are already published, and explicitly not claimed novel. Relevant primary Åhag–Czyż–Virtanen Theorem 10.8 controls operator proximity with coefficient 8sqrt(deficit), not sharp Hardy-space function-symbol distance; their Proposition 12.1 addresses polynomial equality. Independent full relevant text comparison did not produce the sharp H² sqrt2 coefficient.

## value

PASS

Quantifies a natural rigidity question at the simplest nontrivial extremal Crouzeix matrix, controlling entire analytic symbols rather than only matrix evaluations. The sharp coefficient and Blaschke extremal family provide a meaningful endpoint stability invariant, not mere equality restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
