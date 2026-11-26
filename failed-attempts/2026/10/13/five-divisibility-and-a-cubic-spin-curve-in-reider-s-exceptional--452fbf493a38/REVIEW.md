# Independent mathematical audit

## correctness

PASS

The asserted implications are correct. The inline fraction at Reider Theorems 2 and 3 is ambiguous in linearized PDF text. The decisive check is the derivation on PDF pp. 42 and 45: (78) is c2(X)−K²=c2(F_xi)−K²/4 and the displayed substitution is c2(F_xi)=3K²/4, giving c2(X)=3K²/2, hence K²=2c2(X)/3, not the reciprocal. The same theorem gives q=2, smooth irreducible E and an actual line-bundle equality K_X~2E; canonical nefness on a minimal general-type surface makes the rational-curve exclusion match the theorem’s requirement. Noether yields K²=24chi/5 and c2=36chi/5; integrality and K²>0 give chi=5m with m positive, and 1−q+p_g=chi gives p_g=5m+1. Then E²=K²/4=6m, and smooth adjunction gives 2g−2=3E²=18m and K_E=O_E(K_X+E)=O_E(3E)=N_E^3 as line bundles. For the compact Kähler surface b1=4, so b2=c2−2+2b1=36m+6. With b2^+=1+2p_g and b2=2p_g+h^{1,1}, the remaining ranks are precisely as claimed. This is an implication, not a construction. The frozen arithmetic script and stored output were inspected but not executed and do not verify the source premise. The earlier Naie–Reider vanishing theorem has the opposite Chern-ratio regime (c2/K²<5/6 instead of 3/2), so it does not show that this branch is empty.

## originality

FAIL

The package is mechanically covered by the stronger exceptional-branch theorem plus standard identities. It is not necessary that Reider list the tuple of numbers or call the normal bundle cubic spin. The proof introduces no additional branch restriction other than substituting the already-forced identities and enforcing integrality. This is established prior implication, not a verdict based on absence from a search or based on the ambiguous text extraction.

## value

FAIL

The integrality shorthand can be convenient when reading Reider, but as a standalone result every coefficient and normal-bundle label is a routine consequence of the same explicit source identities, standard adjunction, Noether and Hodge formulas. There is no independently derived branch restriction, existence result, or worthwhile unresolved exact invariant verified here. Narrowing to five-divisibility alone or to the cubic-root identification would still leave only direct textbook consequences, so no repair is warranted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
