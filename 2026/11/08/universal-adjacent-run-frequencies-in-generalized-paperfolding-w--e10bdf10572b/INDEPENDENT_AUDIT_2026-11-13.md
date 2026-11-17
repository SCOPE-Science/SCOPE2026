# Independent mathematical audit

## correctness

PASS

Read full frozen RESULT.md and verify.py. Odd-position signs alternate across adjacent odd sites, so runs have length ≤3. A complete consecutive run pair (a,b) is recognized by (-s)s^a(-s)^b s on a window of length a+b+2≤8, with boundary terms O(1). Every 8-window contains exactly one multiple of 8: the remaining seven letters are fixed by ε0,ε1,ε2 and start residue modulo16. The variable sign at multiples of 8 is conditionally asymptotically balanced by splitting the odd quotient modulo4 into equal classes at each 2-adic valuation, uniformly for arbitrary instruction tails. I independently reimplemented all 8 first-three-instruction choices ×16 residues ×2 upper signs ×9 run pairs; every choice yields integer count matrix [[0,3,1],[3,2,3],[1,3,0]]. The position pair density is count/32, their sum 1/2 equals run-start density, hence divide by 1/2 for run-index joint matrix/16. The mutual information follows from ratios 3/2,1/2,1 and row sums; no extrapolation of finite word prefixes.

## originality

PASS

Best-of-knowledge distinct claim after actual primary-source and published-record comparisons. An algorithm for factor locations could potentially imply this matrix after evaluation, but the published theorem statement/inspected main text does not directly dominate the explicit universal measure.

## value

PASS

An exact universal two-point stationary law for a deterministic run-length coding under completely arbitrary, even nonautomatic instruction sequences is a natural statistical invariant. It quantitatively reveals adjacent-run dependence via a nonzero exact mutual information where known factor support and complexity alone do not determine the probabilities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
