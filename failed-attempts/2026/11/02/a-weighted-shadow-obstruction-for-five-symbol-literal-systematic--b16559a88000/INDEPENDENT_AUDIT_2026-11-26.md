# Independent mathematical audit

## correctness

PASS

All equality patterns are represented over a five-element alphabet, and relabeling preserves the weighted shadow. I independently canonicalized all 5^5 words, and generated distinct subsequences by scanning the word and updating sets indexed by retained length in descending order. This yields exactly 52 classes and the stated eight groups; minima for equal and different first symbols are respectively 22 and 30. Type counts in the entire output space are q, q(q-1) for each two-equal type, and q(q-1)(q-2). Thus total weight is q(3q^2+7q+12). Pairwise disjoint shadows give the claimed universal inequality and the q and q(q-1) literal-prefix counts yield a mandatory excess q(q-1)(20-3q). Direct checks of the available weights and mandatory excess for q=2 through 7 gave excesses 28, 66, 96, 100, 60, -42. At q=7 the obstruction no longer applies; it does not prove existence. The supplied verifier and recorded output were inspected without executing the uploaded script.

## originality

FAIL

The frozen headline q>=7 for the literal-prefix endpoint is demonstrably covered by a distinct indexed record with the same constraints and a stronger result: its fractional problem is feasible iff q>=7 and every integral encoder maps to a feasible 0–1 point. Its necessity proof already uses the same five ordered equality classes and the same 52-pattern reduction, with different numerical weights. The catalogue dates coincide, and the stronger record itself credits earlier weighted converses; no chronological priority or copying is inferred. The particular universal inequality for arbitrary prefix composition is algebraically distinct from the compared aggregate bounds, so this finding is not that those exact coefficients are already printed or that the mathematics is false. That distinction does not make the frozen endpoint finding original as delivered.

## value

FAIL

Excluding q=5 and q=6 at the first meaningful literal-prefix endpoint is a natural and worthwhile goal, but the stronger exact relaxation already resolves exactly the frozen cutoff and explains why capacity weights cannot raise that cutoff there. Changing the weights and recording the resulting arbitrary-code inequality is correct, but the frozen result supplies no separate motivated extremal question or demonstrated use for this exact mixed-prefix inequality beyond that covered cutoff. Nonimplication by two aggregate inequalities alone is not sufficient evidence of an independently valuable remaining finding. No narrower replacement is accepted on this evidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
