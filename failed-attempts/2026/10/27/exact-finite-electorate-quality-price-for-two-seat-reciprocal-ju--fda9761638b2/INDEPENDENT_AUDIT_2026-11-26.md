# Independent mathematical audit

## correctness

PASS

For a two-seat committee W, a violating group exists for a candidate c if and only if the entire unrepresented part of c's support has size at least n/(2h_c), including equality. If a top pair (a,b) violates, choose any such witness with s supporters in that unrepresented part. At least one voter supports a, so s<=n-1 and h_c>=tau=n/[2(n-1)]. The witness group has at least n/2 members, all of whom approve c. These voters and at least one supporter of a outside the group make (a,c) represent a strict majority, even when n is even and h_c=1. So (a,c) is rJR. With alpha=h_a>=beta=h_b and alpha<=1, the price is at most (alpha+beta)/(alpha+h_c)<=2alpha/(alpha+tau)<=2/(1+tau). The three-candidate profile with one voter for both unit candidates and n-1 for the tau candidate attains the price, including n=2; subtracting it from 4/3 gives 4/[3(3n-2)]. At equality for n>=3 every top pair violates, and the inequality chain forces beta=alpha=1 and h_c=tau, whence s=n-1. The remaining voter approves both top candidates, and may or may not approve c. The source has a minor mislabeling of which step forces which equality, not a logical gap. I inspected checker.cpp and VERIFICATION.md, not running the submitted code. An independent exact replay at /workspace/branches/two_seat_replay.py directly compared group and supporter criteria on 96,875 exhaustive grid profiles, 400 sampled profiles and nine exact sharpness examples (n=2 through 10) and checked the necessary conditions at sampled equality. One tested n=3 example adds a 7/8-quality candidate supported by the same bloc as the 3/4 candidate; it preserves the geometry but raises the best rJR fraction to 15/16. Finite checks do not establish the universal result.

## originality

FAIL

The exact price is the reciprocal of the rJR part of the distinct frozen record ecfe633c0898 on the identical domain. The equality geometry is not stated there as a conclusion, but is a direct equality-case reading of its stronger constructive inequality for any optimal pair and any violating witness. Its equations (lines 27–41) have h_c>=tau and the nonnegative slack (1-tau)(alpha-beta)+2tau(1-beta). Extremality forces that slack and h_c-tau to vanish; for n>=3 this forces both top qualities to be one, and the budget equality then forces s=n-1. No materially independent theorem remains after the comparison. This assesses equivalent coverage, not priority between the same-day records.

## value

FAIL

The exact fixed-n frontier is a meaningful refinement of a limiting guarantee, but taking its reciprocal adds no independent information. The described geometry simply records which inequalities must be tight in the already available constructive bound; it neither adds an independent obstruction nor classifies sufficiency among more general profiles. There is no substantively distinct remainder to repair here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
