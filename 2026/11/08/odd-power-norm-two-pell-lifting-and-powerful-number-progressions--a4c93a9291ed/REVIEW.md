# Independent mathematical audit

## correctness

PASS

If m is even then m^(2r+1) is divisible by 8, forcing X^2=2 mod 8, impossible. A solution at coefficient m^(2r+1) gives a base solution (x,y)=(X,m^r Z). For odd m, x,y odd and m=7 mod 8; eta=x+y sqrt(m), epsilon=eta^2/2=(x^2-1)+xy sqrt(m) is integral of norm 1. All odd eta^n/2^((n-1)/2) therefore give integral positive norm-two solutions. For each p|m, x^2=2 mod p forces p>=7 and p∤x. In Y_n binomial sum the j=0 term has valuation v_p(y)+v_p(n), while every higher term gains j v_p(m)-v_p(2j+1)>0 (since v_p(2j+1)<j); hence the exact valuation law, permitting index n=m^r(2j+1) and m^r|Y_n. This proves the iff and infinite families. I independently checked m=7 base (3,1) gives (11427,617) at r=1, and m=23 base (5,1) gives (15191131279719638885,137720427724123513); the resulting three powerful numbers form a progression. The n-th-power and infinite-m parameter claims follow algebraically, not from samples.

## originality

PASS

The motivating 2026 van Doorn article proves a specific cubic m=7 construction and explicitly asks how to determine valid cubic m. Mollin’s 2005 fixed-coefficient criterion and Chan’s other powerful progressions do not state a *uniform odd-power invariance* plus exact p-adic index law across all r. The lift uses classical Pell-unit and Lucas lifting techniques, which is a material priority risk, so novelty is limited to the explicit all-r statement in this application, not the method itself.

## value

PASS

The motivating paper poses a concrete arithmetic selection problem for coefficients m^3. The new exact lifting reduces every higher odd-power coefficient solvability test to a single norm-two Pell instance, supplies all primewise valuations and infinitely many powerful-number progressions, and locates m=23 beyond the known m=7 example. No false claim of consecutive powerful integers is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
