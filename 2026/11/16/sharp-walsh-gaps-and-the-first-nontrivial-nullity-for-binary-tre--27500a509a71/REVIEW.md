# Self-review

## Correctness

**PASS.** The root-excluded signed enumerator provides a complete and exact recurrence at every Boolean character. The count-parity recurrence has residues \(0,1,1\) with period three; explicit root signs produce states \((0,1)\), \((1,0)\) and \((1,1)\) cyclically, with multiplier \(2\) also attained at the even class. Fourier diagonalization then yields the sharp \(\ell^2\) pseudoinverse norm. The complete height-two state-ratio list proves precisely \(120^2+2=14402\) height-three zeros, all with negative root sign, and the exact rank \(18366\). Independent integer FWHT and state-table checker implementations reproduced this finite theorem and Parseval.

## Originality

**PASS under bounded comparison.** Levit--Mandrescu (arXiv:0904.4819) and the public full-tree independence-complex analysis imply the *homogeneous* signed-sum three-cycle; with parity, this already implies the invertibility residue classes. **That residue criterion is background, not the claimed new priority.** The exact nonzero all-character gap, its sharp pseudoinverse norm, and the first complete nontrivial nullity \(120^2+2\) with exceptional reciprocal pairs are not statements or implications of the examined material. Trinks's deletion identities give methods but not these explicit spectral invariants. The all-graph independent-support Fourier *principal submatrix* result is a different operator. An unindexed earlier exact table or broader multivariate result remains a possible priority risk.

## Mathematical value

**PASS.** The exact spectral gap and Hilbert inverse norm persist for all tree heights even as the full Boolean ambient dimension grows rapidly. The complete first nontrivial Fourier nullity and its exceptional two-state mechanism supply a natural recoverability boundary, rather than an unmotivated parameter slice. No claim is made about ranks at all greater singular heights.

## Evidence and limitations

The two supplied standalone checker programs and the explicit seven-ratio table permit reconstruction of all finite integers. The all-height proof is symbolic. Relevant primary literature: Levit--Mandrescu (2009), Trinks (2014), a published analysis of full rooted-tree independence-complex homology, and a published Fourier principal-submatrix interpolation result. Only height three is classified by total zero count, and historical priority is bounded rather than certified.

Self-review: passed. Independent audit: not yet performed.
