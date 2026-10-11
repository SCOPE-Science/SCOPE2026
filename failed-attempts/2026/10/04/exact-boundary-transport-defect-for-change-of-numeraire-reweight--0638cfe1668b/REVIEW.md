# Independent mathematical audit

## correctness

PASS

The one-dimensional transport lemma is correct: weak convergence plus convergence of absolute first moments to \(L\) gives a limiting \(W_1\) defect of \(L-M\), with the lower bound from the test \(|x|\) and the matching upper bound from clipping. Perspective cancellation gives \(\int |z|\,d\Gamma_n=\mathbb E|B_n|/m_n\), so the missing boundary mass is exactly \(c/m\). The call and put limits follow from uniform integrability of \(|B_n|+RA_n\) on bounded strike ranges and the boundary values \(b^+\) and \((-b)^+\); one-Lipschitz strike dependence upgrades pointwise convergence to compact-uniform convergence. The finite three-atom sanity family was independently checked but is not used as a proof.

## originality

FAIL

The final claim is mathematically implication-covered by Huang's focal primary paper plus the standard one-dimensional \(W_1\) moment characterization. Huang Proposition 2.1 already gives the exact perspective identities for calls and first absolute moments; Corollary 3.4 identifies the boundary residue \(\int_{a=0}|b|\,dQ\) as the sole first-order obstruction and proves the zero-defect criterion through convergence of absolute first moments. Replacing the binary question 'is the defect zero?' by the numerical limit \(L-M\) is the standard weak-plus-first-moment formula, and splitting \(|b|=b^++(-b)^+\) in the already printed call perspective identity gives the two one-sided offsets. Under the required implication standard this is covered even though the exact nonzero constants are not highlighted as a standalone theorem in the source.

## value

FAIL

The statement is correct and clean, but after Huang's exact first-order boundary theorem and perspective identities are accounted for, the nonzero \(W_1\) constant is a standard first-moment remainder and the call/put constants are the positive/negative parts of the same residue. Compact-uniformity follows from routine Lipschitz equicontinuity. Under the stated value bar this is a useful explanatory corollary, not a separately motivated mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
