# Independent mathematical audit

## correctness

PASS

Reconstructed the result on the precise affine family. The one-sided images yield all-ones rows except for deletion of the first column after a -,+ turn or of the last column after a +,- turn. Nonempty open-cell paths are realizable by backward affine pullback; the cylinder entropy is the logarithm of the Perron root. With A,B the two turn counts and with z_0 normalized to one, the first row gives sum(z)=lambda and the last row gives r=z_last=1, 1-1/lambda or lambda/(lambda+1). The remaining rows reconstruct a positive eigenvector for the unique root of lambda(n-lambda)=A+B r on [n-1,n] for n>=3: the left-minus-right side has opposite weak endpoint signs and is strictly decreasing. Specializing the turn counts yields the three equations, and choosing the preterminal flip positions gives the binomial counts. For n=2 the constant words give radius 2; the two nonconstant radii are 1 and the golden ratio in the stated order. For n>=3 the alternating scores are at least n-1-floor(n/2)/(n-1)>n-2, whereas every nonalternator scores at most n-2. The negative-start advantage at fixed lambda is (lambda-m+1)/(lambda(lambda+1)) for n=2m and m/(lambda(lambda+1)) for n=2m+1; a larger score gives a strictly smaller root. Only zero flips achieve radius n. Writing its worst root as n-1+a gives (n-2)a+a^2=1/2+O(1/n), so a=1/(2n)+O(n^-2) and the n^-2 term in log(n/lambda) cancels. For all words, Delta=n-lambda satisfies n Delta-kappa=Delta^2-B(1-r), a difference of quantities in [0,1]; the log remainder gives the claimed uniform bound. The word-to-first-sign-and-flips bijection gives independent fair bits and fixes both the variance 1/4 and negligible centering correction in the CLT. Read the frozen checker but did not execute it: its one-winner update does not itself rule out ties, and its determinant checks are finite evaluations only. The analytic strict comparison and root proof supply what that diagnostic cannot. Replay: RESULT.md, Steps 1–5, with Oliveira Theorems 7.1–7.2 for the canonical premises.

## originality

PASS

Pass for the strict global optimizer and sharp worst-versus-typical entropy comparison, including the random-word deficit law, not for the known representation, the direct cubic specializations or elementary multiplicities as standalone discoveries. The relevant primary and strongest distinct indexed statements use either the same reduction without the extremal comparison, or different statistics/probability spaces.

## value

PASS

The least-entropy orientation among a canonical rank-minimal family is specified and unique, despite superficially similar opposite-start alternators. The uniform error and fluctuation law also quantify the factor-two separation between typical and extremal leading loss. These address a concrete all-word structural question, rather than just evaluating the already known cubic at a few words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
