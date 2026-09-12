# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exotic K3 E8-swap diffeomorphism versus smooth rigidity
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1350
- **Disposition:** AUDIT_1_REJECT
- **Domain:** smooth versus topological 4-manifold mapping class
- **Method:** one-parameter families Seiberg-Witten over mapping torus plus Quinn track

## Problem

Let M_K3 be the closed simply connected smooth 4-manifold with even intersection form (-E8) (+) (-E8) (+) H (+) H (+) H. Let sigma be the lattice isometry interchanging the two -E8 summands and fixing the H summands. Is sigma realized by a self-diffeomorphism of M_K3 that is topologically isotopic to the standard topological swap via a controlled Quinn track but not smoothly isotopic to it, as detected by a one-parameter families Seiberg-Witten invariant over the mapping torus? A complete answer is either such an exotic swap diffeomorphism with computed nontrivial families invariant plus controlled topological isotopy, or a proof that every diffeomorphism realizing sigma is smoothly isotopic to the standard swap.

## Attempted claim

Let M_K3 be the closed simply connected smooth 4-manifold with even intersection form (-E8) (+) (-E8) (+) H (+) H (+) H. Let sigma be the lattice isometry interchanging the two -E8 summands and fixing the H summands. Is sigma realized by a self-diffeomorphism of M_K3 that is topologically isotopic to the standard topological swap via a controlled Quinn track but not smoothly isotopic to it, as detected by a one-parameter families Seiberg-Witten invariant over the mapping torus? A complete answer is either such an exotic swap diffeomorphism with computed nontrivial families invariant plus controlled topological isotopy, or a proof that every diffeomorphism realizing sigma is smoothly isotopic to the standard swap.

## Research outcome

TARGET resolved on the exotic side: E8-swap sigma admits topologically standard but smoothly exotic diffeomorphisms, detected via families SW over the mapping torus of the Torelli difference.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: audited normally against admitted target. Lattice/index algebra in isolation is correct (L=2(-E8)+3H even det -1 sig (3,19); sigma swap satisfies sigma^TGsigma=G, sigma^2=I, det +1, tr 6, fixed 14/anti-fixed 8, fixes span{e_i+f_i} Gram 2I_3 hence in O+; formal dim (0-48+48)/4=0 +1 over S1; b+-1=2 unique chamber). Transfer algebra h=f0^{-1}g=f0^{-1}tf0 Torelli/conjugate and isotopy-contrapositive plus mapping-torus naturality is valid conditionally. ESSENTIAL PREMISE FAILS: existence on CLOSED K3 of Torelli t topologically isotopic to id but smoothly distinct WITH FSW(M_t,s0)!=0=FSW(S1xM) is cited, not proved, and cited sources do not contain it. Ruberman math/9807041 is Z=X0#CP2#2CPbar reducible, not K3; Baraglia-Konno gluing Cor 1.3 is #n(S2xS2)#n(K3) n>=2, not single K3; Baraglia-Konno Duke 2026 irreducible paper requires sigma and c1 divisible by 32 and explicitly contrasts K3=E(2) sigma=-16 as splitting case; Kronheimer-Mrowka/Lin concern K3#K3 neck or boundary rel-boundary twists, not closed K3 Torelli with mapping-torus FSW. Closest K3 candidate Konno 2203.11631 (Dehn twist about (-2)-sphere has infinite homotopy order, so delta^2 is smoothly nontrivial Torelli) uses 10/8-inequality for involutions, not a computed FSW(M_t)!=0, so target's required detection is still unproved. Step 11 misattributes delta^2 FSW-exoticism to Baraglia-Konno/KM. Fallback 'exactly one of (E),(R)' is logically invalid because (E) adds topological-isotopy plus FSW conditions strictly stronger than not-(R). Hence proof/experimental distinction fails and dichotomy unresolved.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: The existence and families-SW nonvanishing of the exotic Torelli element t is cited from Ruberman / Kronheimer-Mrowka / Baraglia-Konno / Konno-Mukuno-Taniguchi, not recomputed from moduli counts here; the new verified content is the lattice/chamber algebra plus the transfer lemma. If that cited nonvanishing were withdrawn, the proved statement reverts to the clean dichotomy that exactly one of the exotic pair or rigidity holds. No direct absolute computation of a closed mapping-torus invariant…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
