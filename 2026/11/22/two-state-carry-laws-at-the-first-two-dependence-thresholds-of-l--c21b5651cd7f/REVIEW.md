# Independent mathematical audit

## correctness

PASS

Normalized integration selects exactly the signed strings with sum d_j q^j=0. Reducing successive prefixes modulo q yields unique integer carries c_(j+1)=(d_j+c_j)/q, with both terminal carries zero. The bound p+1<2q traps carries in {-1,0,1}, including p=4,q=3. Reflection folds the two nonzero states by summing their weights, which accounts for the factor 2 only on the outward transition from 0. The explicit top coefficients imply a_(p-2)+a_p>a_(p-1)>a_p. A two-step excursion followed by zero steps supplies a strictly larger contribution at each adjacent base for n>=2; no excursion leaves zero if q>=p+1. Equality for n=1 is intentional. For constant amplitude, Cayley–Hamilton and positivity give the recurrence and rate; expanding the larger eigenvalue via (Lambda-A)(Lambda-B)=2a_q a_1 and A-B→1 gives the two leading constants. Substituting the five order-four coefficients gives the displayed radicals. The independent bounded replay python /workspace/reproduce_frozen.py compares direct signed-digit sums with the matrix products for p=4..7, q=p-1..p+2 and three unequal amplitudes; this is supplemental, not a proof for all lengths/orders. The frozen checker was inspected, not executed. Here independence means factorization of the specified moments, not probabilistic independence of the trigonometric factors.

## originality

PASS

Best of current knowledge, the supported distinct contribution is the variable-amplitude transfer law over both adjacent resonances and the strict comparison and different small-amplitude onsets. Credit the independent-range factorization and the exact q=p, amplitude-one specialization, including its recurrence and rate, to the sources below. The judgment is on the extension and comparison, not on those covered components or on carry methods generally.

## value

PASS

The slice is the two nearest dependent bases next to exact factorization, not an arbitrary parameter selection. The transfer gives exact moments for nonidentical factors, separates the two bases at every eligible length, and resolves the distinct orders at which weak modulation changes the long-product growth. These are useful quantitative answers beyond the previously known flat critical recurrence and factorization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
