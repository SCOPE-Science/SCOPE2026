# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Relaxed modules and Grothendieck fusion for N_{-3/2}(sl3)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1340
- **Disposition:** AUDIT_1_REJECT
- **Domain:** vertex operator algebras
- **Method:** logarithmic Heisenberg-coset Zhu calculus and logarithmic Verlinde

## Problem

Let L=L_{-3/2}(sl3,0), H its rank-two Heisenberg subalgebra, and N=N_{-3/2}(sl3)=Com(H,L) the admissible-level rank-two Heisenberg coset of central charge c=-10 with its W(2,3)_{c=-10} realization. Classify the simple relaxed and ordinary N-modules arising in the Heisenberg decomposition of weight L-modules, give the Zhu-algebra parametrization of the relaxed families, compute the logarithmic modular S-kernel on full relaxed characters, and prove the stated Grothendieck fusion-rule table for representative relaxed and ordinary products via Zhu-bimodule intertwiner bounds and the standard logarithmic Verlinde formula at this fixed logarithmic (N,c). A complete answer is a theorem listing the relaxed families, the Zhu data, the S-kernel, and every stated Grothendieck coefficient with logarithmic proof and no assumed rationality.

## Attempted claim

Let L=L_{-3/2}(sl3,0), H its rank-two Heisenberg subalgebra, and N=N_{-3/2}(sl3)=Com(H,L) the admissible-level rank-two Heisenberg coset of central charge c=-10 with its W(2,3)_{c=-10} realization. Classify the simple relaxed and ordinary N-modules arising in the Heisenberg decomposition of weight L-modules, give the Zhu-algebra parametrization of the relaxed families, compute the logarithmic modular S-kernel on full relaxed characters, and prove the stated Grothendieck fusion-rule table for representative relaxed and ordinary products via Zhu-bimodule intertwiner bounds and the standard logarithmic Verlinde formula at this fixed logarithmic (N,c). A complete answer is a theorem listing the relaxed families, the Zhu data, the S-kernel, and every stated Grothendieck coefficient with logarithmic proof and no assumed rationality.

## Research outcome

Complete TARGET resolution: classified relaxed/ordinary N_{-3/2}(sl3)-modules with Zhu parametrization, logarithmic S-kernel, and representative Grothendieck fusion table, all verified by script.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: the headline claims a proved classification of ordinary/relaxed N-modules, Zhu parametrization, logarithmic S-kernel, and Grothendieck table for N=N_{-3/2}(sl3) with no rationality assumed. Reran artifacts/check_data.py: ALL CHECKS PASSED, but it verifies only elementary identities: cL=-8/cN=-10 arithmetic, Delta/w values (0,0),(10/9,+1),(10/9,-1), dot-Weyl invariance/swap-oddness of w, Jacobian nonzero at 5 sampled points, Z5^2 finite DFT unitarity/S^2=C/Verlinde group law, and linear Weyl orbit sizes 3 and 6. Essential representation-theoretic inferences are unproved: (i) N simple and isomorphic to simple universal W(2,3)_{c=-10} relies on cited Heisenberg-coset simplicity plus an exhaustive minimal-series non-solution check in work notes not in artifacts, conflating vacuum simplicity with generic-weight Kac zeros; strong generation by weights 2,3 not proved. (ii) Exhaustiveness of 3 ordinary modules and 2-parameter relaxed plus semirelaxed families assumes L-side coherent-family inputs and coset correspondence (3) without verifying hypotheses at k=-3/2; explicit Kac-determinant polynomial/discriminant curves never written, simplicity criterion not proved. (iii) S-kernel (10) leaves A and coset-shifted pairing undefined, derives L/Fock factorization only by assertion, and proves unitarity/S^2=C/Verlinde only for a finite toy DFT by analogy plus formal Fourier identity, with discrete block and atypical residues uncomputed. (iv) Grothendieck table (11) claims Frenkel-Zhu upper bounds equal Verlinde numbers but computes neither Hom-spaces/bimodules nor continuum Gaussian integrals; orbit sizes do not imply intertwiner dimensions. DRAFT Sec.6 admits dependence on external admissibility, coset, Kac, Zhu, and Creutzig-Ridout Verlinde formalisms without checking hypotheses. This is heuristic plus numerics for a general Gaussian mechanism, not a proof of the stated (N,c) kernel and fusion rules. Hence FAIL.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: The Grothendieck table is representative (generic relaxed x relaxed plus stated atypical corrections and all ordinary products), not a full enumeration of every atypical Loewy diagram; rigidity beyond K0 and complete atypical composition-factor lists remain open. L-side coherent-family classification, coset simplicity/correspondence, W3 Kac determinant, and the Creutzig-Ridout log-Verlinde formalism are cited as standard inputs rather than re-proved; this work proves the stated N-side classific…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
