# Independent mathematical audit

## correctness

PASS

Telescoping gives u-v=final bit minus initial bit. When u=v=r>0 the two possible endpoint symbols contribute distinct words with (r+1,r) or (r,r+1) zero/one run counts. Adding their weak-composition counts gives (n-1)/r times the product of binomials with lower index r-1; imbalanced transitions have r runs of each symbol and one endpoint orientation per profile. For r>1 a loop-balancing exchange strictly gains unless the split is already even to within one; r=1 is flat. With t=floor((n-1)/2), the adjacent balanced ratios are (t-r)^2/[r(r+1)] at odd length and (t-r)(t-r+1)/[r(r+1)] at even length, yielding exactly the stated balanced maxima and the even tie. The imbalanced peaks occur at floor((t+2)/2) for odd n and floor(t/2)+1 for even n. At these r the balanced-to-imbalanced ratios are 2(t-r+1)/r and (2t+1)(t-r+1)/(rt), respectively. The former is 1 only at t=2, where B_1=4 exceeds U_2=2; the latter is strictly greater than 1 even at t=1. Constant-word profiles cannot win for n>=3. Substitution and Stirling give the stated formulas and coefficient, with the empty and one-pair observations handled directly. Independently, appending bits in a dynamic program with terminal-symbol-tagged profiles recovered all maxima and ties through n=80, cross-checked by direct words through n=10 (python3 /workspace/repro/frozen_checks.py). The proof supplies validity beyond those bounds.

## originality

FAIL

An earlier distinct Resultary record explicitly solves the same linear, binary, ordered adjacent-pair problem. Its general formula transforms into the four displayed residue formulas and its set of maximizing profiles matches including all small-length ties at n=3 through 6. The values at n=1,2 are immediate from seeing no pair or the entire word. No substantive uncovered claim remains. This finding of prior scientific coverage does not assert a provenance or authorship relationship.

## value

FAIL

Worst-case ambiguity and its maximizing profiles are natural information-loss quantities. However, the earlier exact result already provides both, including the asymptotic constant. Rewriting by residue class and adding the trivial n=1,2 cases does not constitute a distinct valuable finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
