# Review of the coincidence sparsity theorem

## Correctness — PASS

The proof uses only exact multiplicativity and \(U(p)=p+1\), \(T(p)=p\). If \(n=pm\) with \(p\nmid m\), equality forces \(p(T(m)-U(m))=U(m)\), uniquely fixing \(p\) from \(m\). Partition by the largest prime factor and its exponent to obtain the explicit inequality with \(\Psi(X,y)\). Rankin's inequality and the prime-harmonic bound give \(\Psi(X,y)\ll X\exp(-\log X/\log y)(\log y)^e\) for \(y\ge e^4\), yielding the stated bound at \(\log y=\sqrt{\log X}\). The finite exact computation through \(500000\) and all \(1174163\) exponent-one prime-removal tests passed; these do not replace the proof.

## Originality — PASS, with residual priority risk

Relevant primary text: Trudgian (arXiv:1312.4615), especially the conclusion discussing infinitude of equality and a density for the strict inequality. OEIS A236474 tabulates equality values; A322446 counts strict inequality. The closest available research records include a finite 49-exponent classification for two-prime forms and a numerical lower bound for the strict-comparison density; these are not statements of the global equality-count bound. Searches for density-zero, sparsity, largest-prime uniqueness, and equality aliases did not identify a covering theorem. A general preexisting multiplicative-function coincidence theorem could conceivably imply this estimate, and some related repository full texts could not be inspected; this historical-priority uncertainty remains.

## Mathematical value — PASS

The equality \(\sigma^*(n)=\sigma^{(e)}(n)\) is a specifically posed question in the 2013 source, with rare known examples in OEIS A236474. The result rigorously proves that even if there are infinitely many such integers, their count is smaller than \(X/(\log X)^A\) for every fixed \(A>0\), an actual quantitative distribution statement rather than a finite census. The argument supplies a reusable prime-removal rigidity mechanism and distinguishes the equality boundary from the already studied strict-comparison density. No claim of infinitude or exact asymptotics is made.

Self-review: passed. Independent audit: not yet performed.
