# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Mod-2 arithmetic DW sum 16 over Q(zeta_8) with S above 2,3
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1377
- **Disposition:** NO_RESULT
- **Domain:** arithmetic Chern-Simons/Dijkgraaf-Witten theory
- **Method:** exhaustive 32-representation enumeration with decomposition/gluing formula

## Problem

Let K be Q adjoin zeta_8 with integers O as above, let S consist of the unique prime above 2 and the two primes above 3, let U be Spec O minus S, and fix finite gauge group G equal Z over 2 with the standard normalized 3-cocycle representing the generator of H3 of G. The set of continuous homomorphisms rho from the etale fundamental group of U to G unramified outside S has 32 elements, since H1 of U with Z over 2 coefficients has dimension 5 over the field of 2 elements by the S-unit rank with class number 1, verified in the argument. For each rho let CS of rho in one-half Z modulo Z be the arithmetic Chern-Simons invariant defined by pullback of the 3-cocycle via rho followed by Artin-Verdier modified-etale fundamental-class evaluation. Decide by proof or disproof whether all 32 CS values vanish, equivalently whether the normalized arithmetic Dijkgraaf-Witten sum Z equal to one-half times the sum over all rho of exp of 2 pi i times CS of rho equals the stated value 16. Scope is fixed to this K, S, G, and cocycle with the stated count and normalization. A complete answer is a proof of the stated value by exhaustive enumeration of the 32 homomorphisms with explicit CS values and the decomposition gluing formula, or a rigorous disproof exhibiting the full rho list with at least one nonzero CS value and the corrected sum.

## Attempted claim

Let K be Q adjoin zeta_8 with integers O as above, let S consist of the unique prime above 2 and the two primes above 3, let U be Spec O minus S, and fix finite gauge group G equal Z over 2 with the standard normalized 3-cocycle representing the generator of H3 of G. The set of continuous homomorphisms rho from the etale fundamental group of U to G unramified outside S has 32 elements, since H1 of U with Z over 2 coefficients has dimension 5 over the field of 2 elements by the S-unit rank with class number 1, verified in the argument. For each rho let CS of rho in one-half Z modulo Z be the arithmetic Chern-Simons invariant defined by pullback of the 3-cocycle via rho followed by Artin-Verdier modified-etale fundamental-class evaluation. Decide by proof or disproof whether all 32 CS values vanish, equivalently whether the normalized arithmetic Dijkgraaf-Witten sum Z equal to one-half times the sum over all rho of exp of 2 pi i times CS of rho equals the stated value 16. Scope is fixed to this K, S, G, and cocycle with the stated count and normalization. A complete answer is a proof of the stated value by exhaustive enumeration of the 32 homomorphisms with explicit CS values and the decomposition gluing formula, or a rigorous disproof exhibiting the full rho list with at least one nonzero CS value and the corrected sum.

## Research outcome

Target blocked and clean-exited: the 32-homomorphism count was verified with an explicit S-unit basis, but the all-CS-vanishing claim is ill-posed as stated (no fundamental class for U, missing local sections) and the wild local computation is infeasible, so no auditable result is claimed.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The 32-count and S-unit basis were verified exactly, but no Chern-Simons value could be certified: the target's fundamental-class recipe has no valid construction for ramified representations, the correct secondary-invariant construction needs unfixed local sections, and wild 2-adic local symbols were computationally infeasible here.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The 32-count and S-unit basis were verified exactly, but no Chern-Simons value could be certified: the target's fundamental-class recipe has no valid construction for ramified representations, the correct secondary-invariant construction needs unfixed local sections, and wild 2-adic local symbols were computationally infeasible here.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
