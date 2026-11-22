# Independent mathematical audit

## correctness

PASS

The onto-word indicator is exhaustively transformed with the four-by-four complex C4 character table and the V4 Hadamard table. Independently implemented NumPy tensor character transforms over all 4^n words and 4^n frequencies give exactly both histogram rows at n=4 and 5, and at n=6 cyclic {0:3072,8:510,24:110,40:192,88:15,104:150,120:1,200:45,1560:1} versus Klein {0:3072,8:540,40:270,88:45,104:120,120:3,200:45,1560:1}. Their fourth moments differ by 1132462080. Parseval agrees with 4^6*1560, and division by |G|=4096 gives the additive-energy difference 276480. The finite theorem is complete for n=4,5,6; neither later n nor a global uniqueness theorem follows.

## originality

PASS

The full Klein-group surjection spectrum for all n is already published, including exact multiplicities, so the Klein histogram alone is covered. The simultaneous C4-versus-V4 comparison and first divergence at n=6 are not implied by that V4-only formula, nor by first-band sampling results or graph-colouring analogies. Bounded original-work search found no exact prior comparison; this remains best-of-knowledge with unindexed weighted occupancy literature as risk.

## value

PASS

The group law can change a natural surjection indicator’s full character spectrum without changing its support rank or second moment. The exact earliest threshold and additive-energy discrepancy distinguish two abelian four-colour structures and answer a motivated natural finite Fourier question, beyond a routine general character orthogonality deduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
