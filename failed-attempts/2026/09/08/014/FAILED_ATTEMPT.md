# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A sharp commuting-probability gap for groups of order p^4 with centralizer and character-degree stratification
- **Round:** 2026-09-07-first-light-01
- **Lane:** 89
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Finite Group Theory
- **Method:** class-equation counting with finite group-library exhaustion

## Problem

Let p be an odd prime and G nonabelian of order p^4. Determine the set of values cp(G)=k(G)/|G| (k=number of conjugacy classes), the centralizer-size partition, and the character-degree multiset cd(G). Prove the top value, the second-maximum upper bound, and the resulting empty interval, with |Z(G)|-stratification, and certify by GAP SmallGroups enumeration for all nonabelian groups of order <=96 (in particular 16,27,81).

## Attempted claim

For every odd prime p and every nonabelian G of order p^4: (i) |Z(G)| is p or p^2; (ii) cp(G)=(p^3+p^2-p)/p^4 iff |Z(G)|=p^2 (in which case every noncentral class has size p, every noncentral centralizer has order p^3, and cd(G)={1,p} with p^3 linears); (iii) if |Z(G)|=p then cp(G)<=(p^3+p-1)/p^4 via k=p^3+p-1-b(p-1), b>=0; hence the open interval ((p^3+p-1)/p^4,(p^3+p^2-p)/p^4) of width (p-1)^2/p^4 contains no commuting probability of any group of order p^4 (e.g. for p=3 no group of order 81 has cp in {30/81,31/81,32/81}, top is 33/81=11/27); (iv) GAP SmallGroups check over all nonabelian orders <=96 confirms the stratification and attainer list, with witness H_p x C_p attaining the top.

## Research outcome

Proved a uniform sharp commuting-probability gap for nonabelian groups of order p^4 (odd p): top (p^3+p^2-p)/p^4 on the |Z|=p^2 stratum with full centralizer/character-degree description, at most (p^3+p-1)/p^4 on the |Z|=p stratum, hence an empty interval of width (p-1)^2/p^4. Attainment by H_p x C_p; p=3 instance fully computed (top 33/81=11/27; 30,31,32/81 absent). Pure-Python exact certificates for five explicit groups; full SmallGroups<=96 GAP check not done (no GAP in sandbox) and listed as a limitation.

## Why this attempt failed

Failed axes: value.

value: FAIL under independent-worth-finding-later test. The result is two standard class-equation calculations plus division by |G|: centre dichotomy, top-stratum count, lower-stratum count a=p^3-1-bp, subtraction to get width (p-1)^2/p^4, and routine sum-of-squares degree count once |G'|=p is known. Ingredients explicitly admitted classical; proof uses only F1-F5 taught in a first p-group course. This is a textbook exercise / mere parameter specialization of general cp theory to the tiny order p^4, with no new method, no surprising phenomenon, and no demonstrated downstream use: the claimed feeds to recognition algorithms / Eberhard / Burness / Bogomolov programmes are speculative name-dropping with no algorithm, conjecture, or asymptotic consequence delivered. The promised SmallGroups<=96 certificate was not delivered (only five hand-picked witnesses), second-max sharpness (b=0 realizability) is not established, the |Z|=p degree side is only a bound, and anyone needing the p^4 values rederives them in minutes rather than retrieving this record. Falls squarely under textbook restatement / tiny unmotivated gain / single-small-order extremal, the same value defect as SCOPE-FAIL-20260907-014 (order-96 enumeration REJECT on value); adding an elementary parametric subtraction does not repair it. Correct and narrowly new, but not independently worth finding later.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: ["No GAP/SmallGroups enumeration run (no GAP binary, no root to install): the '<=96 library certificate' part of the audit plan is NOT delivered; only the five explicit groups above are machine-checked. The uniform p^4 theorem is fully hand-proved so it does not depend on the library.", 'Sharpness of the second-max bound (b=0 realizability per p) not established; upper bound only.', 'p=2 excluded from theorem statement by convention (same algebra gives top 10/16=5/8); single computed instance D…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
