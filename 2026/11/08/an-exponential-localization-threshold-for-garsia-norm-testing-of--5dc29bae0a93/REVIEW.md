# Scientific review: Garsia localization transition

## Correctness — PASS

The claim is traced to the exact finite Hankel matrix \(E_{00}+tJ_m\), the Bonsall identity for normalized Szegő kernels, and a one-variable quadratic discriminant. The displayed lower root has a unique positive-radius minimum for \(m\ge4\); its limiting infimum is \(1/2\) for \(m=3\). The critical tie, the cubic optimizer, asymptotic threshold, and norm deficits follow by explicit differentiation or series expansion. `CHECK.py` separately tests finite matrices and representative amplitudes; its finite tests are not substituted for the global proof. The exact result requires \(m\ge2\) and \(t>0\).

## Originality — PASS relative to checked scientific literature

The motivating 2026 article introduces the SRKT equality problem and notes a quadratic-polynomial failure. An earlier published polynomial classification establishes *whether* SRKT holds and a separate finite-rank classification describes its equality cases, but neither calculation gives the critical amplitude at which the kernel-testing maximizer leaves the origin or the degree-dependent bifurcation. Dyakonov's 2025 Garsia-extremality article and Brevig–Seip's 2024 Hankel norm article study different extremal equalities. Actual phrase/alias/parameter queries and their closest indexed records are described in `AUDIT.json`. An equivalent older computation under alternate terminology remains a publication-priority risk; no independent priority certificate is claimed.

## Value — PASS

The Garsia norm is the natural computable kernel-testing norm for Hardy Hankel operators, but testing the origin can lose optimality. The exact localization threshold quantifies that loss for every two-term lacunary degree, revealing a genuine continuous-to-discontinuous transition between degree three and degrees at least four and an exponential separation of the critical amplitudes. This is a motivated sharp parameter classification, not a restatement of the existing qualitative monomial-rigidity theorem.

## Scientific limitations

The theorem does not cover general polynomial supports or solve the full SRKT characterization. The complete set of post-transition local maxima for degrees at least four is not classified. The checked close mathematical notes are prior input only and may have their own independent review status, which is not reassessed here.

Self-review: passed. Independent audit: not yet performed.
