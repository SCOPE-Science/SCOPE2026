# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact Bloch-Kato rank one over an imaginary biquadratic field in the factorable anticyclotomic balanced range
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20242
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Arithmetic Geometry
- **Method:** Euler systems and Iwasawa-theoretic descent

## Problem

Fix a p-ordinary elliptic curve E/Q (weight-2 newform f, trivial nebentypus, p>=5, p not dividing N_f), a fixed imaginary biquadratic field K0/Q in which p splits completely with p not dividing 6*h(K0), and a factorable anticyclotomic Hecke character chi = tilde psi1 tilde psi2 N^{(k1+k2-2)/2} as in Do Assumption 6.1 with symmetric weights k1=k2=:m>=2 (so for k=2, k1+k2-2>=k>=k2-k1+2, global sign -1 and L(f/K0,chi,1)=0). Assume rho-bar_f absolutely irreducible, p-distinguished, f non-Eisenstein of big image, (p*N_f, Norm(f1)*Norm(f2)*D(K0))=1 with the level decomposition of Do Theorem 6.5.1(2), and that Hsieh's f-unbalanced triple-product p-adic L-function is generically nonzero so Do's Lambda-adic anticyclotomic Euler-system base class z_{f,chi} is non-torsion. For V_{f,chi}=V_f^vee tensor chi^{-1}, prove the finite-exact Bloch-Kato rank-one formula dim Sel_BK(K0,V_{f,chi})=1, upgrading Do Theorem 6.7.1's lower bound >=1 to equality via the Jetchev-Nekovar-Skinner Kolyvagin-system upper bound applied to Do's biquadratic Euler system and the Lemma 4.0.4 identification Sel_BK=Sel_{rel,str,ord,ord} in this weight range.

## Attempted claim

Fix a p-ordinary elliptic curve E/Q (weight-2 newform f, trivial nebentypus, p>=5, p not dividing N_f), a fixed imaginary biquadratic field K0/Q in which p splits completely with p not dividing 6*h(K0), and a factorable anticyclotomic Hecke character chi = tilde psi1 tilde psi2 N^{(k1+k2-2)/2} as in Do Assumption 6.1 with symmetric weights k1=k2=:m>=2 (so for k=2, k1+k2-2>=k>=k2-k1+2, global sign -1 and L(f/K0,chi,1)=0). Assume rho-bar_f absolutely irreducible, p-distinguished, f non-Eisenstein of big image, (p*N_f, Norm(f1)*Norm(f2)*D(K0))=1 with the level decomposition of Do Theorem 6.5.1(2), and that Hsieh's f-unbalanced triple-product p-adic L-function is generically nonzero so Do's Lambda-adic anticyclotomic Euler-system base class z_{f,chi} is non-torsion. For V_{f,chi}=V_f^vee tensor chi^{-1}, prove the finite-exact Bloch-Kato rank-one formula dim Sel_BK(K0,V_{f,chi})=1, upgrading Do Theorem 6.7.1's lower bound >=1 to equality via the Jetchev-Nekovar-Skinner Kolyvagin-system upper bound applied to Do's biquadratic Euler system and the Lemma 4.0.4 identification Sel_BK=Sel_{rel,str,ord,ord} in this weight range.

## Research outcome

Proved exact Bloch-Kato rank one over the imaginary biquadratic field in the symmetric-weight balanced range by upgrading Do Theorem 6.7.1 with the JNS Kolyvagin-system bound.

## Why this attempt failed

Failed axes: originality, value.

originality: ADMISSION_DEFECT: the exact headline was already recorded as a conditional corollary in the cited prior work. Do Thm 6.4.1 proves non-torsion base class implies Sel_{rel,str,ord,ord} one-dimensional for general weights, and Do Remark 6.7.2 explicitly states z_{f,chi}!=0 implies dim Sel_BK=1 by Thm 6.4.1. The submission restricts to symmetric k1=k2=m (a strict parameter special case) and assumes the non-torsion input rather than establishing it, so it is a corollary/repackaging of the stronger known conditional fact. The DRAFT itself cites Remark 6.7.2. Admission's novelty judgment was materially false. value: As a new record the symmetric-weight conditional equality adds no independently retrievable value beyond Do's general conditional theorem: a future researcher needs the general JNS bound plus the non-torsion criterion, not this narrower instantiation. The key arithmetic input (Hsieh generic nonvanishing / non-torsion class) is assumed, not established, so the headline is a mechanically implied formal consequence of the assumed black boxes and a mere parameter substitution into an already-published implication.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The proof assembles cited black boxes expressly assumed in the target rather than re-proving them: Do's Euler-system construction and local behavior, the Jetchev-Nekovar-Skinner machinery (via Do Theorem 6.4.1, with JNS still preprint), the BSV explicit reciprocity law, and Hsieh's generic nonvanishing of the f-unbalanced triple-product p-adic L-function. The m=2 boundary case uses Do's stated identification including equality. No independent construction of Kolyvagin primes or new Iwasawa-theo…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
