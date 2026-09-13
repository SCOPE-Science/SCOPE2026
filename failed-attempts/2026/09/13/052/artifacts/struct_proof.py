# Structural attempt: characterize sigma-invariant Pasch 6-sets by orbit type.
# Under sigma (9 swaps + 3 fixed), a sigma-invariant 6-set S (union of orbits) has orbit-type:
#  (a) 3 swap-pairs (0 fixed pts); (b) 2 swap-pairs + 2 fixed (2 fixed pts); (c) 1 swap-pair + 4 fixed: IMPOSSIBLE (only 3 fixed).
# Non-invariant Pasch 6-sets come in sigma-image pairs. Single-Pasch + sigma-invariance forces the unique Pasch 6-set to be sigma-INVARIANT (else it would pair with a distinct image Pasch).
# So unique Pasch 6-set S is type (a) or (b).
# The target additionally REQUIRES type (b)-compatible: preserving S setwise with the involution = sigma itself? Re-read target: "admitting an involutory automorphism fixing exactly three points and preserving its unique Pasch 6-set setwise" — sigma fixes exactly 3 points. Any involution with 3 fixed points on 21 points is conjugate to sigma. So WLOG sigma, and S must be sigma-invariant: type (a) or (b).
# Count data: in 450 sampled systems, min Pasch 8. Enumerate Pasch 6-set types in the verified 20-Pasch example: how many type-(a)/(b) invariant ones?
import sys; sys.path.insert(0,'.'); json as j
