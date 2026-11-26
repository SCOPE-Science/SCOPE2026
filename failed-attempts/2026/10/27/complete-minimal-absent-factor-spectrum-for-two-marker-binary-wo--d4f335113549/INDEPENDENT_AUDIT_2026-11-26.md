# Independent mathematical audit

## correctness

PASS

For a missing word both one-letter end truncations must occur, which is sufficient for proper contiguous factors. A zero-only obstruction is one past the longest gap. One-one factors form the union of the rectangles [0,a]x[0,b] and [0,b]x[0,c]; the axial missing points need the zero-only truncation to occur and the only possible interior corner arises when the rectangles are incomparable. With two ones the bare-core obstructions are all gaps k<=max(b,min(a,c)) except b, and a flanked obstruction can only extend the unique two-one occurrence past one end by one zero, subject to its other truncation occurring. Three ones without wings force both gaps to be b and demand a,c>=b; four ones cannot pass either necessary end test. At b=0 the same reasoning includes the word 111 and works also when the alphabet letter zero is missing. Counting gives the stated three cases. Subtracting each count from n gives respectively a+c, q+b-1-1_{a!=c}, and m+q-1; their zero sets give precisely the stated equality cases. For the series one can sum b+2 over all triples and add corrections. The mixed chamber m<=b<q gives 2z/[(1-z)(1-z^2)(1-z^3)]. In b<m put a=b+1+i,c=b+1+j; the correction is 2+min(i,j)+1_{i!=j}. Its series is z^2/(1-z^3) times [3/(1-z)^2 + z^2/((1-z)^2(1-z^2)) - 1/(1-z^2)]. Together with the base term 2/(1-z)^3+z/(1-z)^4 this yields the stated rational numerator. Its pole at 1 has leading coefficient 7/6 and all other poles are simple; dividing the coefficient asymptotic by binom(n,2) gives (7/18)n+O(1). Independent /workspace/branches/audit_word_obstructions.py checks 2925 words of length 2–26 by actual substring membership, including all small extremizers and 25 series coefficients. The universal claims are established by the symbolic reasoning, not the finite replay.

## originality

FAIL

Distinct indexed result e744971e8c41 already gives the exact two-marker antidictionary and equivalent cardinality on the entire separated-marker regime and a stronger limiting distribution there, including the same limiting slope. Its structural proof extends unchanged to b=0. The exact series and equality classification were not found as quoted statements, but follow by routine geometric sums and elementary inequalities from the same exact templates. The decision is about overlap and implication, not a priority assertion from catalogue dates.

## value

FAIL

The two-marker contiguous antidictionary is a natural structural problem, but its identified templates and count already explain the phenomenon. Extending the same tests to adjacent markers and applying geometric sums and elementary equality checks produces useful closed expressions, not an independently substantive uncovered finding under the value criterion. In particular the known limiting slope is not a new effect and the remaining exact-series arithmetic does not require any additional structural or computational discovery. No genuine repair is warranted on the evidenced remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
