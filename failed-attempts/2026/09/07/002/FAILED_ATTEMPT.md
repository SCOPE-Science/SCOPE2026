# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact spectral gaps for 4-regular dicyclic Cayley graphs and their Schreier quotients via two-dimensional interlacing and trace checks
- **Round:** 2026-09-07-pilot-01
- **Lane:** 3
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Graph Theory
- **Method:** spectral interlacing and trace methods

## Problem

Let Dic_n=Q_{4n}=<a,x | a^{2n}=1, x^2=a^n, x^{-1}ax=a^{-1}> of order 4n (n>=3) with symmetric 4-element set S={a,a^{-1},x,x^{-1}}. Let Gamma_n=Cay(Dic_n,S) (4-regular, 4n vertices) and Sigma_n=Sch(Dic_n/<x>,S) (4-regular with loops/multi-edges, n vertices, H=<x> of order 4). Using only explicit 2-dimensional irreps, Cauchy interlacing / regular-vs-permutation spectrum inclusion, and trace-moment identities, prove a certifiable spectral-gap lower bound and Cheeger corollary for both families.

## Attempted claim

For n>=3, Gamma_n has lambda2 = 2+2*cos(2*pi/n), hence spectral gap d-lambda2 = 2-2*cos(2*pi/n) = 4*sin^2(pi/n) >= 16/n^2 (via sin x>=2x/pi), with edge-expansion h(Gamma_n) >= 2*sin^2(pi/n) >= 8/n^2. The Schreier graphs Sigma_n satisfy Spec(Sigma_n) subset Spec(Gamma_n), so gap(Sigma_n) >= 4*sin^2(pi/n) >= 16/n^2 and same Cheeger bound. Proof uses only 2x2 blocks rho_k(S): even k gives 2+2*cos(pi*k/n), odd k gives 2*cos(pi*k/n), non-trivial linears <=0, so k=2 maximizes; plus trace identities Tr(A^2)=16n as check.

## Research outcome

Proved sharp 4-regular dicyclic gaps 4sin^2(pi/n)>=16/n^2 with Cheeger >=8/n^2 for Cayley Gamma_n and Schreier Sigma_n via explicit 2-dim blocks, spectrum inclusion, uniform 38 trace count, and machine audit to n=30 (<1e-8). Honest partial-theorem packaging of known formulas plus new quotient/certificate.

## Why this attempt failed

Failed axes: value.

value: Correct and new but not independently worth finding later: textbook restatement + parameter substitution + unmotivated polynomial gain + enumeration. Given classical 2x2 irreps (admitted 'inputs are classical'), maximizing over k to get lambda2 is a 10-line trig exercise (2c(2c-1)>=0) any reader of Babai+dicyclic theory derives immediately; Schreier inclusion Spec(Sigma) subset Spec(Gamma) is immediate from standard permutation-subrepresentation theorem, and explicit Fourier diagonalization i->i+1,i-1,-i,-i to 2cos±2 is parallel to dihedral exercise; trace 38 (6+24+8) is elementary length-4 word count whose only use is consistency (draft admits fourth-moment bound trivial for n>3); Cheeger h>=8/n^2 is direct plug into known inequality. Dicyclic vs dihedral is dihedral-like parameter substitution: same 2D-block mechanism, Theta(1/n^2) polynomial decay, unique involution/C4 vs C2xC2/off-diagonal differences do not create new method or phenomenon. Gap ~1/n^2 is explicitly not uniform expansion (draft: 'not LPS-type expander'), so 'explicit expander/TCS/coding' motivation is generic with no downstream use; sharp constant 4sin^2 vs 16/n^2 rarely matters for non-expanders. Choice H=<x> to get n vertices is arbitrary among subgroups, tables n<=30 audit rather than prove, no transferable technique beyond known interlacing+trace. A later worker needing dicyclic gap would re-derive in minutes, not cite this packaging. Falls squarely under reject textbook restatements, mere parameter substitutions, tiny unmotivated gains, unexplained enumerations even if correct and new. Mitigations in topic.json (Schreier loops, trace check, reproducible audit) add packaging, not independent scientific value.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: 2x2 eigenvalue inputs are classical (Babai; dicyclic literature) — novelty is gap extraction + new Schreier quotient + uniform trace count + Cheeger packaging, not irrep discovery. Gap Theta(1/n^2) is polynomial, not uniform expansion. Numerics to n=30 audit the analytic proof for all n>=3; floating point is corroboration only. Fourth-moment independent bound (152n-256)^1/4 is weak (nontrivial only n=3, ~3.76) — recorded honestly as consistency check, not sharp proof. Schreier regularity uses l…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
