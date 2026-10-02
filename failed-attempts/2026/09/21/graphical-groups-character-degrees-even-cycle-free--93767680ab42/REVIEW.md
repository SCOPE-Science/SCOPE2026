# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Disposition: **FAILED**.

## Final claim

For odd \(q\), graphical groups attached to graphs with no even cycle have character-degree counts obtained by summing \((q-1)^{|S|}\) over edge supports of fixed matching number, and cycle graphs admit explicit polynomial character-degree formulas with a single full-support Pfaffian-cancellation correction on even cycles.

## Correctness — PASS

The character-count formula follows from the graphical-group rank formula. For a support graph with no even cycle, the alternating matrix rank is \(2
u(S)\), so summing nonzero edge assignments by support yields the stated matching-support polynomial. For a cycle, proper supports are forests and have the same rank rule; on full support the Pfaffian has exactly the two perfect-matching monomials. Choosing all but one nonzero edge label determines a unique nonzero cancellation label, giving exactly \((q-1)^{2r-1}\) rank-drop points on an even \(2r\)-cycle. Deleting two adjacent vertices leaves a nonsingular path principal minor, so the drop is exactly by two. These arguments establish the formulas for odd \(q\).

## Originality — FAIL

An earlier published SCOPE record already proves the stronger rank-count identity \(\operatorname{ch}(\Gamma,i;q)=q^{n-2i}\#\{y:\operatorname{rank}B_\Gamma(y)=2i\}\) for every graph and every prime power. Wang–Zhou independently gives rank \(2
u(G)\) for every graph with no even cycle. Their combination mechanically yields the record's first theorem. The cycle formulas are likewise an elementary specialization of the earlier general rank-count theorem using the two-term cycle Pfaffian. Under the required implication-based standard, absence of the exact displayed polynomial in the earlier title does not restore originality.

## Scientific value — FAIL

The graph classes are natural, but after the earlier general graphical-group rank theorem and the established no-even-cycle skew-rank theorem, the claimed formulas are mechanically obtained by support enumeration; the even-cycle correction is the direct two-term Pfaffian count. No independently motivated unresolved invariant remains that requires a new structural idea at the level claimed.

## Residual risks and limits

- The formulas are mathematically correct but fail the originality and value bars because stronger earlier rank-count coverage plus known rank/Pfaffian facts mechanically imply them.
- The failure is scientific, not an access or correctness failure.

This is a mathematical review, not formal proof-assistant verification or external certification.
