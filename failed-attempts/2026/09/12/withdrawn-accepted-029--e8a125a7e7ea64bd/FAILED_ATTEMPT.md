# FAILED ATTEMPT — NOT A VALIDATED FINDING

Record: `2026/09/12/029`  
Independent audit date: 2026-09-28 (UTC)  
Task: `e18be9f5efb960e9c92ed317c6afd109`

This package is not accepted as a validated research finding under the three-axis audit. It is retained intact for provenance and should be relocated to the assignment-designated failed path.

## Correctness

The central braided-algebra conclusion is correct: the four basis vectors have q_ij=-1 for all i,j, so c=-flip and the Nichols algebra is the exterior algebra of a four-dimensional space, of dimension 16 with Hilbert series (1+t)^4. However, the published result and slogan explicitly give the generalized Cartan matrix as I_4 with determinant 1. Under the report’s own definition a_ii=2 and the off-diagonal entries are 0, so the Cartan matrix is 2 I_4 and its determinant is 16. The frozen braiding log itself records the correct diagonal-2 matrix, directly contradicting the prose. Because the matrix and determinant are advertised components of the headline ledger, the package is not correct as published.

## Originality

Andruskiewitsch and Fantino (2007), Table 2 and the surrounding proof for even dihedral D_n, already state that for the rotation class O_{y^h}={y^{±h}} and a character with omega^{hj}=-1, the Nichols algebra is the exterior algebra and has dimension 4. For the order-8 dihedral group, n=4, h=1 and the character xi(r)=-1 are exactly this case for the simple summand X. Doubling the same module and observing the identical -1 cross-braiding makes B(X⊕X)=Lambda(X⊕X) of dimension 16 by the standard negative-braiding calculation. The submitted doubled statement is therefore a mechanically implied direct-sum specialization, not a new classification result.

## Scientific value

Once the known two-dimensional rotation-class module is recognized as exterior and the cross-braiding between two identical copies is computed as -flip, the 16-dimensional answer, ten quadratic exterior relations, Hilbert series, and finite A1^4 root datum follow immediately. This is useful target triage, but it is a small direct-sum calculation already controlled by standard Nichols-algebra theory, and the package also misstates the Cartan matrix. It does not clear the standalone scientific-value threshold.

## Consequence

The original package remains useful as computational evidence or target triage, but its research headline must not be represented as an independently validated standalone finding.

## Evidence

- [Andruskiewitsch–Fantino, On pointed Hopf algebras associated with alternating and dihedral groups](https://arxiv.org/abs/math/0702559): For even D_n, Table 2 states that rotation-class modules O_{y^h} with omega^{hj}=-1 have exterior Nichols algebra of dimension 4; n=4,h=1,xi(r)=-1 is the submitted simple summand X.
- [Angiono–Lentner–Sanmarco, Pointed Hopf algebras over nonabelian groups with nonsimple standard braidings](https://doi.org/10.1112/plms.12559): Provides modern context for finite Nichols algebras over nonabelian groups and standard root-system methods; its D4 example concerns reflection-class sums, not the submitted rotation double.
