# Self-review

## Correctness — PASS

For the two-parameter recurrence, the exact solution \(f_n=q^n u_n\) has a three-periodic nonzero weight. For each column width and generalized-binomial shift, cancellation of common normalizers gives the valuation identity \(\nu_p(B_{C_c}(m+k,k))=\nu_p(q)ckm+\nu_p(t)E_2+\nu_p(t+1)E_0\). The complete residue table establishes \(E_0\ge0\), \(E_2\ge-1\), with \(ckm\ge4\) whenever \(E_2=-1\). This proves sufficiency for every prime and all indices if \(t\mid q^4\). The exact coefficient \(B_f(4,2)=-q^4(t+1)/t\) establishes necessity, and the direct \(f_2\)–\(f_4\) comparison proves nondivisibility when \(t\nmid q^2\). The standalone checker reconstructs columns from the recurrence and confirms the finite residue lemma. It does not substitute for the unbounded proof. No unresolved mathematical premise is used.

## Originality — PASS within examined sources

Shapiro's original full paper introduces all-level binomidness and explicitly asks whether it forces divisibility for second-order recurrence sequences. An earlier public cyclotomic-family proof provides exactly the base-level classification \(t\mid q^4\) and the divisibility cutoff \(t\mid q^2\), but expressly leaves the higher-level property undetermined. This result resolves that missing higher-level property for every column width, and produces an all-level nondivisible recurrence. The published interlaced-divisor-chain criterion cannot cover the example because it requires \(f_2\mid f_4\), while the periodic-recurrence recognition theorem excludes exponentially growing sequences. The 2024 work of Caalim and Tanaka concerns lexicographically minimal binomid prime-exponent indexes, not the simultaneous all-column recurrence property. Exact source comparisons and associated remaining priority risks are in AUDIT.json. As always, incomplete indexing cannot establish absolute novelty; an implicit earlier all-level statement may exist.

## Mathematical value — PASS

The all-level counterpart of the nondivisibility question is stated explicitly in the primary 2023 literature and was left unresolved by the earlier base-level example. An exact if-and-only-if condition on a natural infinite cyclotomic order-two family, coupled with a small explicit counterexample, answers that stronger question negatively. The structural three-residue argument explains why the same fourth-power threshold persists at every column width rather than merely providing more examples of base-level integrality.

## Limitations and closest literature

This does not classify all second-order recurrences, establish the all-level property for every ComboSum sequence, nor exhibit an everywhere-positive counterexample. The finite checks are corroborating only. The directly overlapping prior cyclotomic-family proof is explicitly credited for the original base-level criterion; Shapiro (2023), Caalim–Tanaka (2024), the public interlaced-chain proof, and the public eventual-periodic recognition theorem were inspected. No independent scientific validation was performed.

Self-review: passed. Independent audit: not yet performed.
