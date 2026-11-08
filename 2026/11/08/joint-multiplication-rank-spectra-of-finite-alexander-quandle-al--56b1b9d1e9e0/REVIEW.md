# Scientific review: simultaneous multiplication-rank enumerator

## Correctness — PASS

The proof begins with the exact Fourier product identity \(\widehat{uv}(\chi)=\widehat u(S\chi)\widehat v((I-S)\chi)\), available because the character table is invertible over the stated coefficient field. It separately proves that the right rank counts nonzero Fourier coefficients in the image, multiplied by the kernel size, and that the left rank counts occupied kernel cosets. Their intersection sizes follow from the linear-algebra identity \(\dim(\ker B\cap\operatorname{im}B)=\operatorname{rank}B-\operatorname{rank}B^2\). The independent coset count gives every polynomial coefficient. Boundary cases with zero and full rank are included. The attached exact checker enumerates 33,048 algebra elements across eight examples and agrees for all 66,096 one-sided ranks. The proof, not enumeration, establishes the general statement.

## Originality — PASS, qualified

Zhang's 2026 group-ring transport supplies the fundamental factorized multiplication; it does not state a simultaneous distribution of multiplication-operator ranks. The 2026 medial-quandle zero-divisor study and the 2026 study of extended zero-divisor graphs focus on different invariants and small models. The closest accessible prior research result concerning complex right Peirce eigenvalues restricts to idempotents; another concerns derivations in defining characteristic. The present enumerator applies to **all elements**, uses two operator ranks simultaneously, and identifies the kernel-image intersection, equivalently \(\operatorname{rank}((I-\varphi)^2)\), which both marginals miss. Search comparisons included general group-ring, Fourier, annihilator, quandle and rank aliases. This is a qualified originality judgment: searches cannot rule out unindexed equivalent formulas; intermittent source-fetch errors left portions of plausible full texts unreviewed.

## Mathematical value — PASS

Simultaneous left and right annihilator dimensions are natural structural invariants for finite nonassociative algebras and refine the zero-divisor geometry motivating recent quandle-ring research. The polynomial supplies the complete frequency of every possible rank pair in a parameterized infinite family, not merely an individual example. Its dependence on \(\ker(I-\varphi)\cap\operatorname{im}(I-\varphi)\) is genuinely joint: the marginal distributions are independent of this information. Explicit eight-dimensional algebras over \(\mathbb F_3\) with matching marginals but distinct joint spectra illustrate why this precise invariant matters. The field-splitting hypothesis and residual historical-priority risks are disclosed.

Self-review: passed. Independent audit: not yet performed.
